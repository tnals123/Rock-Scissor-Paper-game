from PyQt5 import QtCore, QtGui, QtWidgets

class rank:
    def __init__(self):
        self.rank_x=500
        self.rank_y=400
        self.setupUI()
        
    def setupUI(self):

        self.rankpage=QtWidgets.QWidget()
        self.rank1=QtWidgets.QLabel(self.rankpage)
        self.rank1.setGeometry(0,0,500,22)
        

        self.rank2=QtWidgets.QLabel(self.rankpage)
        self.rank2.setGeometry(0,25,500,22)
      
        self.rank3=QtWidgets.QLabel(self.rankpage)
        self.rank3.setGeometry(0,50,500,22)
        

        self.rank4=QtWidgets.QLabel(self.rankpage)
        self.rank4.setGeometry(0,75,500,22)
        
        self.rank5=QtWidgets.QLabel(self.rankpage)
        self.rank5.setGeometry(0,100,500,22)

        self.rank6=QtWidgets.QLabel(self.rankpage)
        self.rank6.setGeometry(0,125,500,22)

        self.rank7=QtWidgets.QLabel(self.rankpage)
        self.rank7.setGeometry(0,150,500,22)

        self.rank8=QtWidgets.QLabel(self.rankpage)
        self.rank8.setGeometry(0,175,500,22)

        self.rank9=QtWidgets.QLabel(self.rankpage)
        self.rank9.setGeometry(0,200,500,22)

        self.rank10=QtWidgets.QLabel(self.rankpage)
        self.rank10.setGeometry(0,225,500,22)

        self.returnbutton=QtWidgets.QPushButton(self.rankpage)
        self.returnbutton.setGeometry(210,340,80,22)
        self.returnbutton.setText('돌아가기!')