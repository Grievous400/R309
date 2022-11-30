import socket

def a():
    reply = input("client :")
    if reply == 'bye' or reply == 'arret':
        client_socket.close()
    else:
        client_socket.send(reply.encode())

    data = client_socket.recv(1024).decode()
    print(f'Message reçu {data}\n')






if __name__ == '__main__':
        client_socket = socket.socket()
        client_socket.connect(("127.0.0.1", 10002))
        while True:
            a()

