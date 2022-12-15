import socket
import os
import subprocess
import platform
import psutil
import sys

def discussion(conn):
    data = conn.recv(1024).decode()
    print(f"Commande reçue : {data}")
    if data.lower() == 'disconnect':
        conn.send(data.encode())
        conn.close()
    elif data.lower() == 'kill':
        conn.send(data.encode())
        server_socket.close()
    elif data.lower() == 'reset':
        conn.send(data.encode())
        os.execv(sys.executable,['python3'] + sys.argv)
        print("Serveur reset")
    elif data.lower() == 'os':
        reply = platform.system()
        a=platform.release()
        b=os.name
        reply=f"OS = : {reply} {b} {a}"
        conn.send(reply.encode())
    elif data.lower() == "ram":
        reply =f'La mémoire totale est {psutil.virtual_memory().total >>30} GB. Il y a {psutil.virtual_memory().used >>30 } GB de  ram utilisé et {psutil.virtual_memory().total-psutil.virtual_memory().used>>30} GB de libre'
        conn.send(reply.encode())
    elif data.lower() == 'cpu':
        reply = f'Le cpu est utilisé à {psutil.cpu_percent(5)} % dans les 5 dernières secondes'
        conn.send(reply.encode())
    elif data.lower()=='connexion information':
        reply = f'L ip de la machine est {socket.gethostbyname(socket.gethostname())} et son nom est {socket.gethostname()}'
        conn.send(reply.encode())
    elif data.lower() == 'ip':
        reply=socket.gethostbyname(socket.gethostname())
        conn.send(reply.encode())
    elif data.lower() == 'name':
        reply=socket.gethostname()
        conn.send(reply.encode())
    elif data == "python --version":
        if platform.system() == 'Linux':
            reply=subprocess.check_output("python3 --version", shell=True).decode().strip()
            conn.send(reply.encode())
        else:
            reply = subprocess.check_output("python --version", shell=True).decode().strip()
            conn.send(reply.encode())
    elif "ping" in data:
        try:
            r = data.split(" ")
            if platform.system()=='Linux':
                k = subprocess.check_output(f"ping -c 4 {r[1]}", shell=True).decode().strip()
            else:
                k = subprocess.check_output(f"ping {r[1]}", shell=True).decode('cp850').strip()
        except:
            k="Le ping ne passe pas"
            conn.send(k.encode())
        else:
            conn.send(k.encode())
    else:
        try:
            x = data.split(":")
            a = (x[1])
            b = (x[0])
        except:
            reply = "Commande non interprété du à des fautes d'orthographes"
            conn.send(reply.encode())
        else:
            if b.lower() == "linux":
                try:
                    reply =subprocess.check_output(a, shell=True).decode().strip()
                except:
                    reply = "Commande non interprété du à des fautes d'orthographes ou non existante"
                    conn.send(reply.encode())
                else:
                    conn.send(reply.encode())
                    if reply == "":
                        reply = "Commande exécuté et réussi "
                        conn.send(reply.encode())
            elif b.lower() =="dos":
                try:
                    reply =subprocess.check_output(a, shell=True).decode('cp850').strip()
                except:
                    reply="Commande non interprété du à des fautes d'orthographes ou non existante"
                    conn.send(reply.encode())
                else:
                    conn.send(reply.encode())
                    if reply == "":
                        reply = "Commande exécuté et réussi "
                        conn.send(reply.encode())
            elif b.lower() == "powershell":
                try:
                    reply = subprocess.check_output(["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe",a], shell=True).decode('cp850').strip()
                except:
                    reply = "Commande non interprété du à des fautes d'orthographes ou non existante "
                    conn.send(reply.encode())
                else:
                    conn.send(reply.encode())
                    if reply == "":
                        reply = "Commande exécuté et réussi "
                        conn.send(reply.encode())
            elif b.lower() =="mac":
                try:
                    reply =subprocess.check_output(a, shell=True).decode().strip()
                except:
                    reply="Commande non interprété du à des fautes d'orthographes ou non existante "
                    conn.send(reply.encode())
                else:
                    if reply == "":
                        reply = "Commande exécuté et réussi "
                    conn.send(reply.encode())
            else:
                reply = "Commande non interprété du à des fautes d'orthographes ou non existante "
                conn.send(reply.encode())

if __name__ == '__main__':
    server_socket = socket.socket()
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("0.0.0.0", 10005))
    server_socket.listen(1)
    conn, address = server_socket.accept()
    print("Un client est connecté")
    while True:
        try:
            discussion(conn)
        except:
            conn, address = server_socket.accept()
            print("Un client est connect")
