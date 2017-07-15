import sys
from PyQt4 import QtCore, QtGui

from PyQt4.uic import loadUiType
 
Ui_MainWindow, QMainWindow = loadUiType('tela_inicial.ui')
import socket
HOST = socket.gethostbyname('192.168.0.15 ')
PORT = 2003
data=''
print("rodando o cliente")

tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Estrutura inicial do client TCP/IP
tcp_client_socket.connect((HOST,PORT))

#preparando menssagem

home=0
class Main(QMainWindow, Ui_MainWindow) :
    def __init__(self, ) :
        super(Main, self).__init__()
        self.setupUi(self)
        self.bt_up.clicked.connect(self.maisum)
        
    def maisum (self):
        global home
        message = "1"
        byte_msg = message.encode('utf_8')
        tcp_client_socket.send(byte_msg)
        tcp_client_socket.close
        print("MSG recebida:", repr(data))
        home+=1
        self.Lbhome.setNum(home)
        


if __name__ == '__main__' :
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
