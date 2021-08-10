from PyQt5 import QtWidgets
import userdatabase


class myinfoUi:
    def __init__(self):
        self.mydata=userdatabase.UserData()
        self.myinfoUi_x=200
        self.myinfoUi_y=175
        self.setupUi()
    def setupUi(self):
        self.myinformation=QtWidgets.QWidget()
        self.mywin=QtWidgets.QLabel(self.myinformation)
        self.mywin.setGeometry(0,0,200,22)
        
        self.mylose=QtWidgets.QLabel(self.myinformation)
        self.mylose.setGeometry(0,25,200,22)
        
        self.mydraw=QtWidgets.QLabel(self.myinformation)
        self.mydraw.setGeometry(0,50,200,22)
       
        self.mywinrate=QtWidgets.QLabel(self.myinformation)
        self.mywinrate.setGeometry(0,75,200,22)

        self.mygame=QtWidgets.QLabel(self.myinformation)
        self.mygame.setGeometry(0,100,200,22)

        self.returnbutton=QtWidgets.QPushButton(self.myinformation)
        self.returnbutton.setGeometry(65,150,65,22)
        self.returnbutton.setText('돌아가기')
       
