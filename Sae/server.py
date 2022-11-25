import socket
import os
import subprocess


def discussion(conn):
    while True:
            data = conn.recv(1024).decode()
                if data =='Disconnect':
                    conn.close()
                    conn, address = server_socket.accept()

                elif data=='kill':
                    server_socket.close()

                elif data=='reset':
                    server_socket.close()
                    conn.close()
                elif data=='OS':

                elif data=="RAM":

                elif data=='CPU':

                elif data=='IP':

                elif data=='Name':



                else :

                    x=data.split(":")
                    a=str(x[1])
                    b=str(x[0])
                    if b=="Linux" or b=="linux":
                        os.system(a)
                    elif b=="dos" or b=="Dos":
                        os.system(a)
                    elif b=="powershell" or b=="Powershell":
                        os.system(f'powershell -NoProfile -ExecutionPolicya {a}')
                    else:
                        os.system(b)

                    reply = input("serveur :")
                    conn.send(reply.encode())




if __name__ == '__main__':
    server_socket = socket.socket()
    server_socket.bind(("127.0.0.1", 10085))
    server_socket.listen(1)
    conn, address = server_socket.accept()

    print("un client est connecté ")
    discussion(conn)