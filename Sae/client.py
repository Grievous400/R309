import socket
from threading import Thread
import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)

        grid = QGridLayout()
        widget.setLayout(grid)

        cs= QLabel("Connexion à un server :")
        host = QLineEdit('')
        port = QLineEdit()
        co = QPushButton("Connexion")
        aa=QLabel("Discussion : ")

        msg =QLineEdit()
        recu =QLabel("")

        co.clicked.connect(self.connexion)

        self.__cs=cs
        self.__host=host
        self.__port=port
        self.__msg=msg
        self.__recu=recu
        self.__aa=aa
        self.__co=co

        grid.addWidget(cs, 0, 0)  # composant, ligne, colonne
        grid.addWidget(host, 0, 1)  # composant, ligne, colonne
        grid.addWidget(port, 0, 2)  # composant, ligne, colonne
        grid.addWidget(co, 0, 3)  # composant, ligne, colonne
        grid.addWidget(aa, 1, 0)  # composant, ligne, colonne
        grid.addWidget(msg, 1, 1)  # composant, ligne, colonne
        grid.addWidget(recu, 1, 2)  # composant, ligne, colonne

        self.setWindowTitle("Connexion à un server :")



    def connexion(self):
        client_socket = socket.socket()
        client_socket.connect((self.__host.text(), self.__port.text()))