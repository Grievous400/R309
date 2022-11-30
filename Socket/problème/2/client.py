import socket
import sys
import threading

def envoyer(client_socket):

    while True:
            reply = input("client :")
            if  reply=='arret' or reply=='bye':
                client_socket.close()
                sys.exit()
            elif reply:
                client_socket.send(reply.encode())

def recevoir(client_socket):
    while True:

            data = client_socket.recv(1024).decode()
            if data =='arret':
                client_socket.close()
                sys.exit()
            elif data:
                print(f'Message reçu : {data}\n')



if __name__ == '__main__':
    try:
        client_socket = socket.socket()
        client_socket.connect(("127.0.0.1", 1000))

        while True:
            t1=threading.Thread(target=envoyer,args=[client_socket])

            t2=threading.Thread(target=recevoir,args=[client_socket])
            t1.start()
            t2.start()
            t1.join()
            t2.join()
    except:
        print("La connexion n'a pas été établie")
