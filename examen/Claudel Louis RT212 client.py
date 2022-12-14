import socket
import threading
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import *
from PyQt5.uic.properties import *


# Lien de mon github https://github.com/Grievous400/R309
#il sera dans la partie examen

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
        self.__socketC.send(msg.encode())
        reponse = self.__socketC.recv(1024).decode()
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

        self.serveurl=QLabel("Serveur:")
        self.serveurc=QLineEdit("localhost")

        self.portlabel=QLabel("Port :")
        self.portc=QLineEdit("10000")

        self.boutonco=QPushButton("Connexion")

        self.chat=QTextEdit("")
        self.msg=QLabel('Message :')
        self.msgc=QLineEdit("")
        self.msgc.setEnabled(False)

        self.boutonenvoyer=QPushButton("Envoyer")
        self.boutonenvoyer.setEnabled(False)
        self.boutonquitter=QPushButton("Quitter")
        self.boutoneffaccer=QPushButton("Effacer")



        grid.addWidget(self.serveurl,0 ,0)
        grid.addWidget(self.serveurc,0, 1,1,2)
        grid.addWidget(self.portlabel,1 , 0)
        grid.addWidget(self.portc, 1,1 ,1,2)
        grid.addWidget(self.boutonco, 2, 0,1,3)
        grid.addWidget(self.chat, 3, 0,2,3)
        grid.addWidget(self.msg, 6, 0)
        grid.addWidget(self.msgc,6,1,1,3)
        grid.addWidget(self.boutonenvoyer,7,0,1,3)

        grid.addWidget(self.boutoneffaccer,8,0,1,1)
        grid.addWidget(self.boutonquitter,8,2,1,2)




        self.boutonco.clicked.connect(self.connexion)
        self.boutonenvoyer.clicked.connect(self.envoyer)
        self.boutoneffaccer.clicked.connect(self.effacer)
        self.boutonquitter.clicked.connect(self.quitter)
        self.threadrecevoir=None
        self.client=None
        self.setWindowTitle("Un logiciel de chat:")

    def connexion(self):
        if self.boutonco.text() == "Connexion":
            try:
                host = self.serveurc.text()
                port = int(self.portc.text())
            except:
                msg = QMessageBox()
                msg.setWindowTitle("Erreur")
                msg.setText("Le type de valeur entr??e n'est pas bon ")
                msg.exec_()
            else:
                try:
                    self.client=Client(host,port)
                    self.client.client_connect()
                except:
                    msg = QMessageBox()
                    msg.setWindowTitle("Erreur")
                    msg.setText("Le serveur n'est pas d??marr??")
                    msg.exec_()
                else:
                    self.boutonenvoyer.setEnabled(True)
                    self.msgc.setEnabled(True)
                    self.boutonco.setText("D??connexion")
        else:
            self.client.envoyer("deco-server")
            self.client.close()
            self.boutonenvoyer.setEnabled(False)
            self.msgc.setEnabled(False)

    def envoyer(self):
        msg = self.msgc.text()
        self.chat.append(msg)
        self.chat.setAlignment(Qt.AlignLeft)
        reponse=self.client.envoyer(msg)
        self.chat.append(reponse)
        self.chat.setAlignment(Qt.AlignRight)

    def effacer(self):
        self.msgc.clear()

    def quitter(self):
        try:
            self.boutonco.text() == "D??connexion"
        except:
            msg = QMessageBox()
            msg.setWindowTitle("Erreur")
            msg.setText("Vous ne pouvez pas vous d??connectez ")
            msg.exec_()
        else:
            self.threadrecevoir.join()
            self.client.envoyer("deco-server")
            self.client.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()