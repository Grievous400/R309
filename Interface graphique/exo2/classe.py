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

        lab = QLabel("Température")
        text = QLineEdit()
        lab2 = QLabel("°C")

        convertir = QPushButton("Convertir")
        bouton = QPushButton("?")

        choix=QComboBox()
        choix.addItem(" °C -> K")
        choix.addItem(" K -> °C")


        lab3 =QLabel("Conversion")
        lab4=QLineEdit("")
        lab4.setEnabled(False)
        #fais apparaitre la case grisé
        lab5 =QLabel("K")


        self.__lab=lab
        self.__lab2=lab2
        self.__lab3=lab3
        self.__lab4=lab4
        self.__lab5=lab5

        self.__text=text
        self.__choix=choix

        self.__convertir=convertir
        self.__bouton=bouton

        # Ajouter les composants au grid ayout

        grid.addWidget(lab, 0, 0)  # composant, ligne, colonne
        grid.addWidget(text, 0, 1)  # composant, ligne, colonne
        grid.addWidget(lab2, 0,2 )  # composant, ligne, colonne

        grid.addWidget(convertir, 1,1 )  # composant, ligne, colonne
        grid.addWidget(choix, 1,2 )  # composant, ligne, colonne

        grid.addWidget(lab3, 2,0 )  # composant, ligne, colonne
        grid.addWidget(lab4, 2,1 )  # composant, ligne, colonne
        grid.addWidget(lab5, 2,2 )  # composant, ligne, colonne

        grid.addWidget(bouton, 3,3 )  # composant, ligne, colonne

        convertir.clicked.connect(self._convertion)
        bouton.clicked.connect(self._aide)
        choix.currentTextChanged.connect(self._changer)

        self.resize(750,750)

        self.setWindowTitle("Convertiseur :")

    def _convertion(self):

        try:

            a = self.__choix.currentText()
            #déclaration de la valeur en float pour effectuer la convertion dessus
            b=float(self.__text.text())
        except:
            msg = QMessageBox()
            msg.setWindowTitle("Erreur")
            msg.setText("La valeur entrée est pas bonne")
            msg.exec_()

        else:
            # test la valeur de c pour savoir dans quel sens se fait la convertion

            if a == " °C -> K":
                self.__lab4.setText(f'{b+273.15}')
            else:
                self.__lab4.setText(f'{b - 273.15}')

    def _aide(self):
        msg = QMessageBox()
        msg.setWindowTitle("Aide")
        msg.setText("Permet de convertir un nombre soit de Kelvin vers Celcius vers Kelvin")
        msg.exec_()

    def _changer(self):
        c = self.__choix.currentText()
        #Change les unités en fonction de la convertion
        if c == " °C -> K":
            self.__lab2.setText("°C")

            self.__lab5.setText("K")

        else:
            self.__lab5.setText("°C")
            self.__lab2.setText("K")
