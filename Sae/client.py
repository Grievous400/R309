import socket
import sys
import threading

from PyQt5.QtCore import QCoreApplication, Qt
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

    def envoyer(self, msg):
        #while msg != "kill" and msg != "Disconnect" and msg != "reset":
        self.__socketC.send(msg.encode())
        reponse = self.__socketC.recv(32000).decode()
        return reponse

    def close(self):
        self.__socketC.close()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)


        self.cs = QLabel("Connexion à un server :")
        self.host2 = QLineEdit('127.0.0.1')
        self.port2 = QLineEdit('1003')
        self.co = QPushButton("Connexion")
        self.aa = QLabel("Discussion : ")

        self.s = QPushButton("Envoyer")
        self.msg = QLineEdit("")
        self.recu= QTextEdit("")



        self.co.clicked.connect(self.connexion)
        self.s.clicked.connect(self.envoyer)

        grid.addWidget(self.cs, 0, 0)
        grid.addWidget(self.host2, 0, 1)
        grid.addWidget(self.port2, 0, 2)
        grid.addWidget(self.co, 0, 3)
        grid.addWidget(self.aa, 1, 0)
        grid.addWidget(self.msg, 1, 1)
        grid.addWidget(self.recu, 2, 1,9,6)
        grid.addWidget(self.s, 1, 2)
        self.resize(750,750)

        self.client = None

        self.setWindowTitle("Gestionnaire de serveur :")

    def connexion(self):
        host = str(self.host2.text())
        port = int(self.port2.text())
        self.client=Client(host,port)
        self.client.client_connect()
        self.co.setEnabled(False)

    def envoyer(self):
        msg = self.msg.text()
        if msg =="cls" or msg =="clear":
            self.recu.clear()
        else:
            reponse = self.client.envoyer(msg)
            self.recu.append(reponse)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
