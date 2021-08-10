from PyQt5 import QtCore, QtGui, QtWidgets
import sys

import PyQt5
import GameUi
class login:
    def __init__(self):
        
        self.login_x=200
        self.login_y=220
        self.setupUi()
        
        self.effect = QtWidgets.QGraphicsOpacityEffect()
        self.loginpage.setGraphicsEffect(self.effect)
        self.animation = QtCore.QPropertyAnimation(self.effect, b"opacity")
        self.unfade(self.loginpage)

        


    def setupUi(self):
        self.loginpage=QtWidgets.QWidget()
        
        self.title=QtWidgets.QLabel(self.loginpage)
        self.title.setGeometry(40,15,200,22)
        self.title.setText('가위바위보 게임!')
        self.effect = QtWidgets.QGraphicsOpacityEffect()
        
        self.id=QtWidgets.QLineEdit(self.loginpage)
        self.id.setGeometry(40,50,120,20)
        self.password=QtWidgets.QLineEdit(self.loginpage)
        self.password.setGeometry(40,80,120,20)
        self.loginbutton=QtWidgets.QPushButton(self.loginpage)
        self.loginbutton.setGeometry(60,110,80,22)
        self.loginbutton.setText('Login!')
        self.resisterbutton=QtWidgets.QPushButton(self.loginpage)
        self.resisterbutton.setGeometry(100,180,80,22)
        self.resisterbutton.setText('Resister!')
        
   

    def unfade(self, widget):

        self.effect = QtWidgets.QGraphicsOpacityEffect()
        self.effect.setOpacity(0)
        self.loginpage.setGraphicsEffect(self.effect)
        self.animation = QtCore.QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(3000)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()