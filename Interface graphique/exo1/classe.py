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

        lab = QLabel("Saisir votre nom")
        text = QLineEdit("")

        lab2 =QLabel("")


        ok = QPushButton("Ok")

        quit = QPushButton("Quitter")

        self.__lab2 = lab2
        self.__text = text
        # Ajouter les composants au grid ayout

        grid.addWidget(lab, 0, 0)  # composant, ligne, colonne
        grid.addWidget(text, 1, 0)  # composant, ligne, colonne
        grid.addWidget(lab2, 2, 0)  # composant, ligne, colonne
        grid.addWidget(ok, 3, 0)  # composant, ligne, colonne
        grid.addWidget(quit, 4, 0)  # composant, ligne, colonne


        ok.clicked.connect(self._actionOk)

        quit.clicked.connect(self._actionQuitter)
        self.resize(250,250)
        self.setWindowTitle("Une première fenêtre")


    def _actionOk(self):
        self.__lab2.setText(f'Bonjour {self.__text.text()}')


    def _actionQuitter(self):
        QCoreApplication.exit(0)

