from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import userdatabase
from PyQt5.QtWidgets import QMessageBox

class Signup:
    def __init__(self):
        
        self.setupUi()
        self.resister_x=200
        self.resister_y=280
        self.userdata=userdatabase.UserData()
        self.msg=QMessageBox()
        
        
    def setupUi(self):

       

        self.resisterpage=QtWidgets.QWidget()
        self.resisterpage.resize(300,400)
        self.idlabel=QtWidgets.QLabel(self.resisterpage)
        self.idlabel.setGeometry(20,30,40,20)
        self.idlabel.setText('id')
        self.id=QtWidgets.QLineEdit(self.resisterpage)
        self.id.setGeometry(80,30,100,20)

        self.pwlabel=QtWidgets.QLabel(self.resisterpage)
        self.pwlabel.setGeometry(20,60,40,20)
        self.pwlabel.setText('pw')
        self.password=QtWidgets.QLineEdit(self.resisterpage)
        self.password.setGeometry(80,60,100,20)

        self.pwchecklabel=QtWidgets.QLabel(self.resisterpage)
        self.pwchecklabel.setGeometry(20,90,60,20)
        self.pwchecklabel.setText('checkpw')
        self.pwcheck=QtWidgets.QLineEdit(self.resisterpage)
        self.pwcheck.setGeometry(80,90,100,20)

        self.namelabellabel=QtWidgets.QLabel(self.resisterpage)
        self.namelabellabel.setGeometry(20,120,40,20)
        self.namelabellabel.setText('name')
        self.name=QtWidgets.QLineEdit(self.resisterpage)
        self.name.setGeometry(80,120,100,20)

        self.emaillabel=QtWidgets.QLabel(self.resisterpage)
        self.emaillabel.setGeometry(20,150,40,20)
        self.emaillabel.setText('email')
        self.email=QtWidgets.QLineEdit(self.resisterpage)
        self.email.setGeometry(80,150,100,20)

        self.phonelabel=QtWidgets.QLabel(self.resisterpage)
        self.phonelabel.setGeometry(20,180,80,20)
        self.phonelabel.setText('phone')
        self.phonenumber=QtWidgets.QLineEdit(self.resisterpage)
        self.phonenumber.setGeometry(80,180,100,20)

        self.resisterbutton=QtWidgets.QPushButton(self.resisterpage)
        self.resisterbutton.setGeometry(60,220,80,25)
        self.resisterbutton.setText('Resister!')
        

    def openmessage(self):
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setWindowTitle('비밀번호 틀림!')
        self.msg.setText('비밀번호를 다시 확인해주세요')
        self.msg.setStandardButtons(QMessageBox.Ok)
        retval = self.msg.exec_()

    def openmessage2(self):
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setWindowTitle('회원가입 완료!')
        self.msg.setText('회원가입이 완료되었습니다.')
        self.msg.setStandardButtons(QMessageBox.Ok)
        retval = self.msg.exec_()
        
    def openmessage3(self):
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setWindowTitle('아이디 중복!')
        self.msg.setText('중복된 아이디입니다.')
        self.msg.setStandardButtons(QMessageBox.Ok)
        retval = self.msg.exec_()

    def openmessage4(self):
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setWindowTitle('로그인 실패!')
        self.msg.setText('아이디나 비밀번호를 잘못 입력하셨습니다.')
        self.msg.setStandardButtons(QMessageBox.Ok)
        retval = self.msg.exec_()


            
            
        