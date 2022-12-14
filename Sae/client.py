import socket
import sys
import threading
import csv
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import *
from PyQt5.uic.properties import *


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
        msg='disconnect'
        self.__socketC.send(msg.encode())
        reponse = self.__socketC.recv(32000).decode()
        return reponse


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)

        self.cs = QLabel("Connexion à un server :")
        self.host2 = QComboBox()
        self.newip =QLineEdit("")

        self.fichiercsv =QLineEdit("")
        self.fichierla =QLabel("Nom du fichier csv a importé :")
        self.fichiercsvlire =QPushButton("Lire le fichier csv")


        self.port2 = QLineEdit('10005')
        self.co = QPushButton("Connexion")
        self.aa = QLabel("Discussion : ")
        self.newipl = QLabel("Nouvelle IP : ")

        self.s = QPushButton("Envoyer")
        self.msg = QLineEdit("")
        self.recu= QTextEdit("")

        self.q=QPushButton("Quitter")
        self.new=QPushButton("Sauvegarder la nouvelle adresse ")
        self.newd=QPushButton("Nouvelle fenetre")
        self.q.setEnabled(False)
        self.s.setEnabled(False)

        self.co.clicked.connect(self.connexion)
        self.s.clicked.connect(self.envoyer)
        self.q.clicked.connect(self.quit)
        self.new.clicked.connect(self.newa)
        self.newd.clicked.connect(self.create_new_document)
        self.fichiercsvlire.clicked.connect(self.lirefichiercsv)

        grid.addWidget(self.cs, 1, 0)
        grid.addWidget(self.host2, 1, 1)
        grid.addWidget(self.port2, 1,2 )
        grid.addWidget(self.co, 1, 3)
        grid.addWidget(self.q, 3, 3)
        grid.addWidget(self.aa, 3, 0)
        grid.addWidget(self.msg, 3, 1)
        grid.addWidget(self.recu, 4, 0,9,6)
        grid.addWidget(self.s, 3, 2)

        grid.addWidget(self.newipl, 2, 0)
        grid.addWidget(self.newip, 2, 1)
        grid.addWidget(self.new, 2, 2)
        grid.addWidget(self.newd, 0, 0)

        grid.addWidget(self.fichierla, 0, 1)
        grid.addWidget(self.fichiercsv, 0, 2)
        grid.addWidget(self.fichiercsvlire, 0, 3)



        self.resize(750,750)
        self.client = None
        self.wind2 =None
        self.setWindowTitle("Gestionnaire de serveur :")
        self.fichiercsvnom=None

    def connexion(self):
        try:
            host = str(self.host2.currentText())
            port = int(self.port2.text())
            self.client = Client(host, port)
            self.client.client_connect()
        except:
            msg = QMessageBox()
            msg.setWindowTitle("Erreur de connexion ")
            msg.setText("Les valeurs de l'adresse ip et du port sont incorrectes ou le serveur n'est pas allumé")
            msg.exec_()
        else:
            self.co.setEnabled(False)
            self.q.setEnabled(True)
            self.s.setEnabled(True)


    def envoyer(self):
        try:
            msg = self.msg.text()
        except:
            msg = QMessageBox()
            msg.setWindowTitle("Erreur")
            msg.setText("Erreur d'envoie de message")
            msg.exec_()
        else:
            if msg =="cls" or msg =="clear":
                self.recu.clear()
            elif msg =="disconnect" or msg=='reset':
                histo = f'Commande utilisé: {msg}\n'
                self.recu.append(str(histo))
                reponse = self.client.envoyer(msg)
                self.recu.append(reponse)
                self.q.setEnabled(False)
                self.co.setEnabled(True)
            else:
                histo=f'Commande utilisé: {msg}'
                self.recu.append(str(histo))
                reponse = self.client.envoyer(msg)
                self.recu.append(reponse)


    def quit(self):
        self.co.setEnabled(True)
        self.q.setEnabled(False)
        self.s.setEnabled(False)
        msg = QMessageBox()
        msg.setWindowTitle("Quitter")
        msg.setText("Vous etes déconnectés")
        msg.exec_()
        self.client.close()


    def newa(self):
        try:
            a=self.newip.text()
            self.host2.addItem(a)
            with open(self.fichiercsvnom,'a',newline='') as csvfile:
                spamwriter =csv.writer(csvfile)
                spamwriter.writerow([a])
        except:
            msg = QMessageBox()
            msg.setWindowTitle("Ajout d'une addrese Ip")
            msg.setText("L'adresse a été correctement ajouté")
            msg.exec_()

        else:
            msg = QMessageBox()
            msg.setWindowTitle("Ajout d'une addrese Ip")
            msg.setText("L'adresse a été correctement ajouté ")
            msg.exec_()
            self.newip.clear()


    def lirefichiercsv(self):
        try:
            self.fichiercsvnom=self.fichiercsv.text()
            with open(self.fichiercsvnom) as csvfile:
                fichiercsv = csv.reader(csvfile)
                for row in fichiercsv:
                    a = str(row)
                    characters = "[] ' "
                    s = ''.join(x for x in a if x not in characters)
                    self.host2.addItem(s)
        except:
            msg = QMessageBox()
            msg.setWindowTitle("Erreur")
            msg.setText("Fichier non trouvé")
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Lecture de fichier csv")
            msg.setText("Le fichier a été lu avec succès")
            msg.exec_()
            self.fichiercsv.clear()


    def create_new_document(self):
        self.wind2=MainWindow()
        self.wind2.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()