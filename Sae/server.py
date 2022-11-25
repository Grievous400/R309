import socket



def envoyer(conn):
    while True:
            reply = input("serveur :")
            if reply =='bye' or reply=='arret':
                conn.close()
            elif reply:
                conn.send(reply.encode())
def recevoir(conn):
    while True:
            data = conn.recv(1024).decode()
            if data =='arret':
                conn.close()
            elif data:
                print(f'Message reçu : {data}\n')

if __name__ == '__main__':

    server_socket = socket.socket()
    server_socket.bind(("127.0.0.1", 10003))
    server_socket.listen(1)
    conn, address = server_socket.accept()
    print("un client est connecté ")