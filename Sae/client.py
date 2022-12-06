import socket
import threading

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import *

class Client(threading.Thread):
    def __init__(self, host, port):
        super().__init__()
        self.__host = host
        self.__port = port
        self.__socketC = socket.socket()

    def get_host(self):
        return self.__host

    def set_host(self,host):
        self.__host = host

    def get_port(self):
        return self.__port

    def set_port(self, port):
        self.__port = port

    def get_socketC(self):
        return self.__socketC

    def set_socketC(self, socketC):
        self.__socketC = socketC

    def client_connect(self):
        self.__socketC.connect((self.__host,self.__port))


    def envoyer(self):
        msg = ""
        while msg != "kill" and msg != "disconnect" and msg != "reset":
            msg = input("client: ")
            self.__socketC.send(msg.encode())
            reply = self.__socketC.recv(1024).decode()
            print(reply)
        self.__socketC.close()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)

        grid = QGridLayout()
        widget.setLayout(grid)

        cs = QLabel("Connexion à un server :")
        host2 = QLineEdit('')
        port2 = QLineEdit('')
        co = QPushButton("Connexion")
        aa = QLabel("Discussion : ")

        s = QPushButton("Envoyer")
        msg = QLineEdit()
        recu = QLabel("")

        co.clicked.connect(self.connexion)
        s.clicked.connect(self.send())

        self.__cs = cs
        self.__host2 = host2
        self.__port2 = port2
        self.__msg = msg
        self.__recu = recu
        self.__aa = aa
        self.__co = co
        self.__s = s


        grid.addWidget(cs, 0, 0)
        grid.addWidget(host2, 0, 1)
        grid.addWidget(port2, 0, 2)
        grid.addWidget(co, 0, 3)
        grid.addWidget(aa, 1, 0)
        grid.addWidget(msg, 1, 1)
        grid.addWidget(recu, 1, 2)

        self.setWindowTitle("Connexion à un server :")

    def connexion(self):
        host=str(self.__host2.text())
        port=int(self.__port2.text())
        a=Client(host,port)
        Client.client_connect(a)


    def send(self):
        m=self.__msg.text()
        Client.envoyer(m)
