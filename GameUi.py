from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, Qt
from PyQt5.QtGui import QPixmap
import time
import random

from PyQt5.sip import settracemask
import userdatabase
import LoginUi

class game:
    def __init__(self):
        self.user=LoginUi.login()
        self.userdata=userdatabase.UserData()
        self.game_x=500
        self.game_y=500
        self.setupUi()
        self.enemyfight=gamethread(label=self.label2,label2=self.label,pic1=self.enemyrock,pic2=self.enemyscissor,pic3=self.enemypaper)
        self.eventcount=0
        self.animesc = QtCore.QPropertyAnimation(self.scissorbutton,b"geometry")
        self.animepa = QtCore.QPropertyAnimation(self.paperbutton,b"geometry")
        self.rockani=rockanimation(self.rockbutton)
        self.scissorani=scissoranimation(self.scissorbutton)
        self.paperani=paperanimation(self.paperbutton)
        self.winani = QtCore.QPropertyAnimation(self.winlabel,b"geometry")
        self.loseani=QtCore.QPropertyAnimation(self.loselabel,b"geometry")
        self.tieani=QtCore.QPropertyAnimation(self.tielabel,b"geometry")
        self.gameevent()
        self.animation()
        

    def gameevent(self):
        
            self.rockbutton.enterEvent=lambda event, label=self.label,pic=self.myrock:self.enterevent(event,label,pic)
            self.rockbutton.leaveEvent=lambda event, label=self.label:self.leaveevent(event,label)

            self.scissorbutton.enterEvent=lambda event, label=self.label,pic=self.myscissor:self.enterevent(event,label,pic)
            self.scissorbutton.leaveEvent=lambda event, label=self.label:self.leaveevent(event,label)

            self.paperbutton.enterEvent=lambda event, label=self.label,pic=self.mypaper:self.enterevent(event,label,pic)
            self.paperbutton.leaveEvent=lambda event, label=self.label:self.leaveevent(event,label)    
        
    def gamestart(self):
        self.enemyfight.start()   

    def animation(self):
        
        self.rockani.start()
        self.scissorani.start()
        self.paperani.start()

    def winanimation(self,label):
        self.finalwin=label
        self.zoomevent(self.winani,self.finalwin,600,60)
    
    def loseanimation(self,label):
        self.finallose=label
        self.zoomevent(self.loseani,self.finallose,700,60)

    def tieanimation(self,label):
        self.fianltie=label
        self.zoomevent(self.tieani,self.fianltie,600,60)
        

    def zoomevent(self,animation,label,x,y):
        
        self.finalwin=label
        animation.setStartValue(QtCore.QRect(self.finalwin.x(),self.finalwin.y(),self.finalwin.width(),self.finalwin.height()))
        animation.setEndValue(QtCore.QRect(self.finalwin.x(),self.finalwin.y(),self.finalwin.width()+x,self.finalwin.height()+y))
        animation.setDuration(1000)
        animation.start() 
        

    def zoomoutevent(self,animation,label,x,y) :
        
        animation.setStartValue(QtCore.QRect(self.finalwin.x(),self.finalwin.y(),self.finalwin.width(),self.finalwin.height()))
        animation.setEndValue(QtCore.QRect(self.finalwin.x(),self.finalwin.y(),self.finalwin.width()+x,self.finalwin.height()+y))
        animation.setDuration(5000)
        animation.start() 
   
    
        
    def setupUi(self):

        
        
        
        self.victorypic=QPixmap('victory.png')
        self.victorypic=self.victorypic.scaledToWidth(500)
        self.victorypic=self.victorypic.scaledToHeight(60)

        self.tiepic=QPixmap('tie.png')
        self.tiepic=self.tiepic.scaledToWidth(500)
        self.tiepic=self.tiepic.scaledToHeight(60)

        self.losepic=QPixmap('lose.png')
        self.losepic=self.losepic.scaledToWidth(500)
        self.losepic=self.losepic.scaledToHeight(60)


        self.enemyrock=QPixmap('rock2.png')
        self.enemyrock=self.enemyrock.scaledToWidth(140)
        self.enemyrock=self.enemyrock.scaledToHeight(140)

        self.enemyscissor=QPixmap('scissor2.png')
        self.enemyscissor=self.enemyscissor.scaledToWidth(135)
        self.enemyscissor=self.enemyscissor.scaledToHeight(140)

        self.enemypaper=QPixmap('paper2.png')
        self.enemypaper=self.enemypaper.scaledToWidth(140)
        self.enemypaper=self.enemypaper.scaledToHeight(140)

        self.myrock=QPixmap('myrock.png')
        self.myrock=self.myrock.scaledToWidth(140)
        self.myrock=self.myrock.scaledToHeight(140)

        self.myscissor=QPixmap('myscissor.png')
        self.myscissor=self.myscissor.scaledToWidth(135)
        self.myscissor=self.myscissor.scaledToHeight(140)

        self.mypaper=QPixmap('mypaper.png')
        self.mypaper=self.mypaper.scaledToWidth(140)
        self.mypaper=self.mypaper.scaledToHeight(140)

        self.gamepage=QtWidgets.QWidget()
        self.label=QtWidgets.QLabel(self.gamepage)
        self.label.setGeometry(50,50,150,150)
        self.label.setStyleSheet('background:white;')
        self.label2=QtWidgets.QLabel(self.gamepage)
        self.label2.setGeometry(300,50,150,150)
        self.label2.setStyleSheet('background:white;')

        self.myinfobutton=QtWidgets.QPushButton(self.gamepage)
        self.myinfobutton.setGeometry(50,400,100,25)
        self.myinfobutton.setText('내 정보 보기')

        self.rockbutton=QtWidgets.QPushButton(self.gamepage)
        self.rockbutton.setGeometry(60,300,80,25)
        self.rockbutton.setText('바위')
        

        self.scissorbutton=QtWidgets.QPushButton(self.gamepage)
        self.scissorbutton.setGeometry(210,300,80,25)
        self.scissorbutton.setText('가위')

        self.paperbutton=QtWidgets.QPushButton(self.gamepage)
        self.paperbutton.setGeometry(350,300,80,25)
        self.paperbutton.setText('보')

        self.againbutton=QtWidgets.QPushButton(self.gamepage)
        self.againbutton.setGeometry(210,400,100,25)
        self.againbutton.setText('다시 하기')
        self.disable_but(self.againbutton)
        self.againbutton.clicked.connect(self.again)

        self.rankingbutton=QtWidgets.QPushButton(self.gamepage)
        self.rankingbutton.setGeometry(350,400,100,25)
        self.rankingbutton.setText('랭킹')

        self.winlabel=QtWidgets.QLabel(self.gamepage)
        self.winlabel.setGeometry(160,200,0,0)
        self.winlabel.setPixmap(self.victorypic)

        self.logoutbutton=QtWidgets.QPushButton(self.gamepage)
        self.logoutbutton.setGeometry(400,470,80,22)
        self.logoutbutton.setText('로그아웃')

        self.loselabel=QtWidgets.QLabel(self.gamepage)
        self.loselabel.setGeometry(190,200,0,0)
        self.loselabel.setPixmap(self.losepic)

        self.tielabel=QtWidgets.QLabel(self.gamepage)
        self.tielabel.setGeometry(160,200,0,0)
        self.tielabel.setPixmap(self.tiepic)

        self.myid=QtWidgets.QLabel(self.gamepage)
        self.myid.setGeometry(0,0,200,22)
        self.myid.setStyleSheet('color:red;')

    def again(self):
        self.eventcount=0
        self.loselabel.setGeometry(190,200,0,0)
        self.winlabel.setGeometry(160,200,0,0)
        self.tielabel.setGeometry(160,200,0,0)
        self.gamestart()
        self.label.clear()
        self.able_but(self.rockbutton)
        self.able_but(self.scissorbutton)
        self.able_but(self.paperbutton)
        
    def disable_but(self, vbutton):
         vbutton.setEnabled(False)
    def able_but(self,vbutton):
         vbutton.setEnabled(True)

    def enterevent(self,event,label,pic):
        if self.eventcount==0:
            self.pic=pic
            self.anylabel=label
            self.anylabel.setPixmap(self.pic)

    def leaveevent(self,event,label):
        if self.eventcount==0:
            self.anylabel=label
            self.anylabel.clear()


    def fightresult(self,event,id,label,myresult,win,lose,tie):
            
         
            self.eventcount=2
            
            
            self.able_but(self.againbutton)
            self.disable_but(self.rockbutton)
            self.disable_but(self.scissorbutton)
            self.disable_but(self.paperbutton)
            self.enemyfight.b=0
            self.player=id
            self.picture=label
            self.myresult=myresult
            self.win=win
            self.userdata.data()
            self.lose=lose
            self.tie=tie
            if self.enemyfight.ran==1:
  
                if self.myresult==1:
                    self.label.setPixmap(self.myrock)
                    self.userdata.draw(self.player.text())
                    self.tieanimation(self.tie)
                    self.userdata.findwinrate(self.player.text())
                elif self.myresult==2:
                    self.label.setPixmap(self.myscissor)
                    self.userdata.lose(self.player.text())
                    self.loseanimation(self.lose)
                    self.userdata.findwinrate(self.player.text())
                elif self.myresult==3:
                    self.label.setPixmap(self.mypaper)
                    self.winanimation(self.win)
                    self.userdata.win(self.player.text())
                    self.userdata.findwinrate(self.player.text())
                    
                    
            elif self.enemyfight.ran==2:
                
                if self.myresult==1:
                    self.label.setPixmap(self.myrock)
                    self.userdata.win(self.player.text())
                    self.winanimation(self.win)
                   
                    self.userdata.findwinrate(self.player.text())
                elif self.myresult==2:
                    self.label.setPixmap(self.myscissor)
                    self.userdata.draw(self.player.text())
                    self.tieanimation(self.tie)
                    self.userdata.findwinrate(self.player.text())
                elif self.myresult==3:
                    self.label.setPixmap(self.mypaper)
                    self.userdata.lose(self.player.text())
                    self.loseanimation(self.lose)
                    self.userdata.findwinrate(self.player.text())

            elif self.enemyfight.ran==3:
                
                if self.myresult==1:
                    self.label.setPixmap(self.myrock)
                    self.userdata.lose(self.player.text())
                    self.loseanimation(self.lose)
                    self.userdata.findwinrate(self.player.text())
                elif self.myresult==2:
                    self.label.setPixmap(self.myscissor)
                    self.userdata.win(self.player.text())
                    self.winanimation(self.win)
                    self.userdata.findwinrate(self.player.text())
                elif self.myresult==3:
                    self.label.setPixmap(self.mypaper)
                    self.userdata.draw(self.player.text())
                    self.tieanimation(self.tie)
                    self.userdata.findwinrate(self.player.text())
            


class gamethread(QThread):
    def __init__(self,label,label2,pic1,pic2,pic3):
        QThread.__init__(self)
        self.label=label
        self.label2=label2
        self.pic1=pic1
        self.pic2=pic2
        self.pic3=pic3
        self.ran=random.randint(1,3)
        
        self.a=1

    def run(self):
        self.ran=random.randint(1,3)
        self.b=1
      
        while True:
            self.a+=1
            time.sleep(0.5)
    
            if self.a==4:
                self.a=1
            if self.a==1:
                self.label.setPixmap(self.pic1)
            elif self.a==2:
                self.label.setPixmap(self.pic2)
            elif self.a==3:
                self.label.setPixmap(self.pic3)
            if self.b==0:
                self.final()
                break

    def final(self):
        if self.ran==1:
            self.label.setPixmap(self.pic1)       
        if self.ran==2:
            self.label.setPixmap(self.pic2)
        if self.ran==3:
            self.label.setPixmap(self.pic3)        

class rockanimation(QThread):
    def __init__(self,button):
        QThread.__init__(self)
        self.button=button
    
    def run(self):
        self.animero = QtCore.QPropertyAnimation(self.button,b"geometry")
        self.button.showEvent=lambda event,animation=self.animero ,button=self.button,y=900:self.slideevent(event,animation,button,y)
      
    def slideevent(self,event,animation,button,y):
        self.button=button
        animation.setStartValue(QtCore.QRect(self.button.x(),self.button.y()+y,self.button.width(),self.button.height()))
        animation.setEndValue(QtCore.QRect(self.button.x(),self.button.y(),self.button.width(),self.button.height()))
        animation.setDuration(1000)
        animation.start()

class scissoranimation(QThread):
    def __init__(self,button):
        QThread.__init__(self)
        self.button=button
    
    def run(self):
        self.animesc = QtCore.QPropertyAnimation(self.button,b"geometry")
        self.button.showEvent=lambda event,animation=self.animesc ,button=self.button,y=1300:self.slideevent(event,animation,button,y)
        
    def slideevent(self,event,animation,button,y):
        self.button=button
        animation.setStartValue(QtCore.QRect(self.button.x(),self.button.y()+y,self.button.width(),self.button.height()))
        animation.setEndValue(QtCore.QRect(self.button.x(),self.button.y(),self.button.width(),self.button.height()))
        animation.setDuration(1500)
        animation.start()

class paperanimation(QThread):
    def __init__(self,button):
        QThread.__init__(self)
        self.button=button
    
    def run(self):
        self.animepa = QtCore.QPropertyAnimation(self.button,b"geometry")
        self.button.showEvent=lambda event,animation=self.animepa ,button=self.button,y=2200:self.slideevent(event,animation,button,y)
        
    def slideevent(self,event,animation,button,y):
        self.button=button
        animation.setStartValue(QtCore.QRect(self.button.x(),self.button.y()+y,self.button.width(),self.button.height()))
        animation.setEndValue(QtCore.QRect(self.button.x(),self.button.y(),self.button.width(),self.button.height()))
        animation.setDuration(2000)
        animation.start()
        
        
