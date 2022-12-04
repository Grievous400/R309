import socket,threading,sys

#def a(client_socket):
    #reply = input("client :")

    #if reply=='Disconnect':
     #   client_socket.close()
    #else:
   #      client_socket.send(reply.encode())

  #       data = client_socket.recv(32000).decode()
 #        print(f'{data}\n')

#if __name__ == '__main__':
#       client_socket = socket.socket()
#       client_socket.connect(("127.0.0.1", 1003))
#       while True:
#           a(client_socket)

class client(threading.Thread):
    def __init__(self,host:str,port:int):
        super().__init__()
        self.__host=host
        self.__port=port
        self.__client=socket.socket

    def connexion(self):
        self.__client.connect((self.__host,self.__port))

    def envoyer(self):
        reply=input("client :")
        self.__client.send(reply.encode())
    def recevoir(self):
        self.__client.recv(1024).decode()

    def fermer(self):
        self.__client.close()
