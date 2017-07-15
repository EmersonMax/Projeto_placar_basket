import sys
import socket
from PyQt4 import QtCore, QtGui
from PyQt4.uic import loadUiType
Ui_MainWindow, QMainWindow = loadUiType('placar.ui')
HOST = '192.168.0.15 '
PORT = 2003
message=''
home=0

    

class Main(QMainWindow, Ui_MainWindow) :
    def __init__(self, ) :
        super(Main, self).__init__()
        self.setupUi(self)
        
       
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#associacao de porta ao processo servidor
        tcp_server_socket.bind((HOST,PORT))
        tcp_server_socket.listen()

        client, addr = tcp_server_socket.accept()
        print ("rodando servidor")
        while True:
    #receber os dados do cliente
            data = client.recv(1024)
            byte_msg = client.recv(1024)
    #preparo mensagem de confirmacao de recebimento
    #envio da mensagem de confirmacao
            if not data: break
            print("\n IP:",addr)
            print(" Mensagem recebida:", data)
            
            print (int(byte_msg))
            global home
            home= home +int(byte_msg)
            self.Lbhome.setNum(home)
        
    
        
    def maisum (self):
        global home
        home+=1
        self.Lbhome.setNum(home)
         


if __name__ == '__main__' :
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
    
   
