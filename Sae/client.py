import socket

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
        host = QLineEdit()
        port = QLineEdit()


        co = QPushButton("Convertir")

        co.clicked.connect(self.connexion)

        self.__cs=cs
        self.__host=host
        self.port=port

        grid.addWidget(cs, 0, 0)  # composant, ligne, colonne
        grid.addWidget(host, 1, 1)  # composant, ligne, colonne
        grid.addWidget(port, 1, 2)  # composant, ligne, colonne
        self.setWindowTitle("Connexion à un client :")


    def connexion(self):
        client_socket = socket.socket()
        client_socket.connect((self.__host, self.__port))

