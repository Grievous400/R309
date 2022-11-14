import socket
import sys
import threading

def envoyer(conn):

    while True:
        reply = input("serveur :")
        if reply =='bye' or reply=='arret':
            conn.close()
            sys.exit()
        elif reply:
            conn.send(reply.encode())




def recevoir(conn):


    while True:
        data = conn.recv(1024).decode()
        if data =='arret':
            conn.close()
            sys.exit()
        elif data:
            print(f'Message reçu : {data}\n')





if __name__ == '__main__':
    try:
        server_socket = socket.socket()
        server_socket.bind(("127.0.0.1", 10001))
        server_socket.listen(1)
        conn, address = server_socket.accept()

    except (TimeoutError,ConnectionRefusedError,socket.gaierror,ConnectionResetError,BrokenPipeError):
        print("il y a une erreur")
    except(OSError,ConnectionAbortedError):
        print("Arret de la discussion")
    else:
        while True:
            t1=threading.Thread(target=envoyer,args=[conn])
            t2=threading.Thread(target=recevoir,args=[conn])

            t1.start()
            t2.start()
            t1.join()
            t2.join()
