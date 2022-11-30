import socket

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

class client():
    def __init__(self,host:str,port:int):
        self.__host=host
        self.__port=port
        self.__connexion=False


    def etatco(self):
        return(self.__connexion!=False)

    def connexion(self):
        client_socket=socket.socket()
        client_socket.connect((self.__host,self.__port))

    def envoyer(self, reply):
        socket.send(reply.encode())
    def recevoir(self,data):
        
    #def fermer(self):
    #    .close()
