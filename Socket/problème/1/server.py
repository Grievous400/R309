import socket


def discussion():

    data = conn.recv(1024).decode()
    print("Message reçu", data)
    reply=input("Server :")

    if reply == 'bye' or reply == 'arret':
        conn.close()
    else:
        conn.send(reply.encode())



if __name__ == '__main__':
    server_socket = socket.socket()
    server_socket.bind(("127.0.0.1", 10002))
    try:

        server_socket.listen(1)
        conn, address = server_socket.accept()

    except:
        conn, address = server_socket.accept()
    else:
        while True:
            discussion()