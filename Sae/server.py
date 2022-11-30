import socket
import os
import subprocess
import platform
import psutil
import sys

def discussion(conn):

    data = conn.recv(1024).decode()
    if data =='Disconnect':
        print("a")

    elif data=='kill':
        conn.close()
        server_socket.close()

    elif data=='reset':
        sys.stdout.flush()
        os.execv("server.py")

    elif data=='OS':
        reply=platform.system()
        conn.send(reply.encode())

    elif data=="RAM":
        reply =f'La mémoire totale est {psutil.virtual_memory().total >>30} GB. Il y a {psutil.virtual_memory().used >>30 } GB de  ram utilisé et {psutil.virtual_memory().total-psutil.virtual_memory().used>>30} GB de libre'
        conn.send(reply.encode())
    elif data=='CPU':
        reply=f'Le cpu est utilisé à {psutil.cpu_percent(5)} % dans les 5 dernières secondes'
        conn.send(reply.encode())
    elif data=='Connexion information':
        reply=f'L ip de la machine est {socket.gethostbyname(socket.gethostname())} et son nom est {socket.gethostname()}'
        conn.send(reply.encode())
    elif data=='IP':
        reply=socket.gethostbyname(socket.gethostname())
        conn.send(reply.encode())
    elif data=='Name':
        reply=socket.gethostname()
        conn.send(reply.encode())
    elif data=="python --version":
        reply=subprocess.check_output("python --version", shell=True).decode().strip()
        conn.send(reply.encode())
    elif "ping" in  data:
        try:
            r=data.split(" ")
            k =subprocess.check_output(f"ping {r[1]}", shell=True).decode('windows-1252').strip()
        except:
            k="Le ping ne passe pas"
            conn.send(k.encode())
        else:
            conn.send(k.encode())

    else :

        x=data.split(":")
        a=(x[1])
        b=(x[0])
        if b=="Linux" or b=="linux":
            reply =str(os.system(a))
            conn.send(reply.encode())

        elif b=="dos" or b=="Dos":
            reply= str(os.system(a))
            conn.send(reply.encode())

        elif b=="powershell" or b=="Powershell":
            reply = subprocess.check_output(["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe",a], shell=True).decode('windows-1252').strip()
            conn.send(reply.encode())

        else:
            reply=subprocess.check_output(b, shell=True).decode().strip()
            conn.send(reply.encode())




if __name__ == '__main__':
    server_socket = socket.socket()

    try:
        server_socket.bind(("127.0.0.1", 1000))
        server_socket.listen(1)
        conn, address = server_socket.accept()

    except:
        conn, address = server_socket.accept()
    else:
        while True:
            discussion(conn)