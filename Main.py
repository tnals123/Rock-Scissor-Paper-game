from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import sqlite3
import LoginUi
import resisterUi
import userdatabase
import GameUi
import myinfo
import Ranking

class Mainui(object):
    def __init__(self):

        self.mainwindow=QtWidgets.QMainWindow()
        self.login=LoginUi.login()
        self.resister=resisterUi.Signup()
        self.userdata=userdatabase.UserData()
        self.game=GameUi.game()
        self.myinfopage=myinfo.myinfoUi()
        self.rankingpage=Ranking.rank()

       
        self.SetupUi()
        self.login.resisterbutton.clicked.connect(self.Signuppage)
        self.resister.resisterbutton.clicked.connect(self.signup)
        self.login.loginbutton.clicked.connect(self.trylogin)
        self.game.myinfobutton.clicked.connect(self.myinfo)

        self.game.rockbutton.mousePressEvent= lambda event, id=self.login.id,label=self.game.label,myresult=1,win=self.game.winlabel,lose=self.game.loselabel,tie=self.game.tielabel:self.game.fightresult(event,id,label,myresult,win,lose,tie)
        self.game.scissorbutton.mousePressEvent= lambda event, id=self.login.id,label=self.game.label,myresult=2,win=self.game.winlabel,lose=self.game.loselabel,tie=self.game.tielabel:self.game.fightresult(event,id,label,myresult,win,lose,tie)
        self.game.paperbutton.mousePressEvent= lambda event, id=self.login.id,label=self.game.label,myresult=3,win=self.game.winlabel,lose=self.game.loselabel,tie=self.game.tielabel:self.game.fightresult(event,id,label,myresult,win,lose,tie)

        self.game.rankingbutton.clicked.connect(self.ranking)
        self.rankingpage.returnbutton.clicked.connect(self.gamereturn)
        self.game.logoutbutton.clicked.connect(self.logout)
        
        
    def show(self):
        self.mainwindow.show()

    def logout(self):
        self.login.id.setText(None)
        self.login.password.setText(None)
        self.mainwindow.resize(self.login.login_x,self.login.login_y)
        self.paper.setCurrentIndex(0)
        self.login.unfade(self.login.loginpage)
        
    def gamereturn(self):
        self.mainwindow.resize(self.game.game_x,self.game.game_y)
        self.paper.setCurrentIndex(2)

    def ranking(self):
        self.mainwindow.resize(self.rankingpage.rank_x,self.rankingpage.rank_y)
        self.userdata.ranking()
        self.userdata.myname(self.login.id.text())

        self.rankingpage.rank1.setStyleSheet('color:black;')
        self.rankingpage.rank2.setStyleSheet('color:black;')
        self.rankingpage.rank3.setStyleSheet('color:black;')
        self.rankingpage.rank4.setStyleSheet('color:black;')
        self.rankingpage.rank5.setStyleSheet('color:black;')
        self.rankingpage.rank6.setStyleSheet('color:black;')
        self.rankingpage.rank7.setStyleSheet('color:black;')
        self.rankingpage.rank8.setStyleSheet('color:black;')
        self.rankingpage.rank9.setStyleSheet('color:black;')
        self.rankingpage.rank10.setStyleSheet('color:black;')

        self.paper.setCurrentIndex(4)
        try:
            self.rankingpage.rank1.setText('1등: '+str(self.userdata.rankinginfo[0][0])+'님 / 승리: '+str(self.userdata.rankinginfo[0][1])+', 패배: '+str(self.userdata.rankinginfo[0][2])+', 승률: '+str(self.userdata.rankinginfo[0][3])+'%, 무승부: '+str(self.userdata.rankinginfo[0][5])+', 게임 수: '+str(self.userdata.rankinginfo[0][4])+'게임')
            if self.userdata.rankinginfo[0][0]==self.userdata.myidname[0][0]:
                self.rankingpage.rank1.setStyleSheet('color:red;')
            self.rankingpage.rank2.setText('2등: '+str(self.userdata.rankinginfo[1][0])+'님 / 승리: '+str(self.userdata.rankinginfo[1][1])+', 패배: '+str(self.userdata.rankinginfo[1][2])+', 승률: '+str(self.userdata.rankinginfo[1][3])+'%, 무승부: '+str(self.userdata.rankinginfo[1][5])+', 게임 수: '+str(self.userdata.rankinginfo[1][4])+'게임')
            if self.userdata.rankinginfo[1][0]==self.userdata.myidname[0][0]:
                self.rankingpage.rank2.setStyleSheet('color:red;')
            self.rankingpage.rank3.setText('3등: '+str(self.userdata.rankinginfo[2][0])+'님 / 승리: '+str(self.userdata.rankinginfo[2][1])+', 패배: '+str(self.userdata.rankinginfo[2][2])+', 승률: '+str(self.userdata.rankinginfo[2][3])+'%, 무승부: '+str(self.userdata.rankinginfo[2][5])+', 게임 수: '+str(self.userdata.rankinginfo[2][4])+'게임')
            if self.userdata.rankinginfo[2][0]==self.userdata.myidname[0][0]:
                self.rankingpage.rank3.setStyleSheet('color:red;')
            self.rankingpage.rank4.setText('4등: '+str(self.userdata.rankinginfo[3][0])+'님 / 승리: '+str(self.userdata.rankinginfo[3][1])+', 패배: '+str(self.userdata.rankinginfo[3][2])+', 승률: '+str(self.userdata.rankinginfo[3][3])+'%, 무승부: '+str(self.userdata.rankinginfo[3][5])+', 게임 수: '+str(self.userdata.rankinginfo[3][4])+'게임')
            if self.userdata.rankinginfo[3][0]==self.userdata.myidname[0][0]:
                self.rankingpage.rank4.setStyleSheet('color:red;')
            self.rankingpage.rank5.setText('5등: '+str(self.userdata.rankinginfo[4][0])+'님 / 승리: '+str(self.userdata.rankinginfo[4][1])+', 패배: '+str(self.userdata.rankinginfo[4][2])+', 승률: '+str(self.userdata.rankinginfo[4][3])+'%, 무승부: '+str(self.userdata.rankinginfo[4][5])+', 게임 수: '+str(self.userdata.rankinginfo[4][4])+'게임')
            if self.userdata.rankinginfo[4][0]==self.userdata.myidname[0][0]:
                self.rankingpage.rank5.setStyleSheet('color:red;')
            self.rankingpage.rank6.setText('6등: '+str(self.userdata.rankinginfo[5][0])+'님 / 승리: '+str(self.userdata.rankinginfo[5][1])+', 패배: '+str(self.userdata.rankinginfo[5][2])+', 승률: '+str(self.userdata.rankinginfo[5][3])+'%, 무승부: '+str(self.userdata.rankinginfo[5][5])+', 게임 수: '+str(self.userdata.rankinginfo[5][4])+'게임')
            if self.userdata.rankinginfo[5][0]==self.userdata.myidname[0][0]:
                self.rankingpage.rank6.setStyleSheet('color:red;')
            self.rankingpage.rank7.setText('7등: '+str(self.userdata.rankinginfo[6][0])+'님 / 승리: '+str(self.userdata.rankinginfo[6][1])+', 패배: '+str(self.userdata.rankinginfo[6][2])+', 승률: '+str(self.userdata.rankinginfo[6][3])+'%, 무승부: '+str(self.userdata.rankinginfo[6][5])+', 게임 수: '+str(self.userdata.rankinginfo[6][4])+'게임')
            if self.userdata.rankinginfo[6][0]==self.userdata.myidname[0][0]:
                self.rankingpage.rank7.setStyleSheet('color:red;')
            self.rankingpage.rank8.setText('8등: '+str(self.userdata.rankinginfo[7][0])+'님 / 승리: '+str(self.userdata.rankinginfo[7][1])+', 패배: '+str(self.userdata.rankinginfo[7][2])+', 승률: '+str(self.userdata.rankinginfo[7][3])+'%, 무승부: '+str(self.userdata.rankinginfo[7][5])+', 게임 수: '+str(self.userdata.rankinginfo[7][4])+'게임')
            if self.userdata.rankinginfo[7][0]==self.userdata.myidname[0][0]:
                self.rankingpage.rank8.setStyleSheet('color:red;')
            self.rankingpage.rank9.setText('9등: '+str(self.userdata.rankinginfo[8][0])+'님 / 승리: '+str(self.userdata.rankinginfo[8][1])+', 패배: '+str(self.userdata.rankinginfo[8][2])+', 승률: '+str(self.userdata.rankinginfo[8][3])+'%, 무승부: '+str(self.userdata.rankinginfo[8][5])+', 게임 수: '+str(self.userdata.rankinginfo[8][4])+'게임')
            if self.userdata.rankinginfo[8][0]==self.userdata.myidname[0][0]:
                self.rankingpage.rank9.setStyleSheet('color:red;')
            self.rankingpage.rank10.setText('10등: '+str(self.userdata.rankinginfo[9][0])+'님 / 승리: '+str(self.userdata.rankinginfo[9][1])+', 패배: '+str(self.userdata.rankinginfo[9][2])+', 승률: '+str(self.userdata.rankinginfo[9][3])+'%, 무승부: '+str(self.userdata.rankinginfo[9][5])+', 게임 수: '+str(self.userdata.rankinginfo[9][4])+'게임')
            if self.userdata.rankinginfo[9][0]==self.userdata.myidname[0][0]:
                self.rankingpage.rank10.setStyleSheet('color:red;')
        except IndexError:
            pass

    def myinfo(self):
        self.mainwindow.resize(self.myinfopage.myinfoUi_x,self.myinfopage.myinfoUi_y)
        self.paper.setCurrentIndex(3)
        self.userdata.myinfo(self.login.id.text())
        self.myinfopage.mywin.setText('승: '+str(self.userdata.resultinfo[0][5]))
        self.myinfopage.mylose.setText('패: '+str(self.userdata.resultinfo[0][6]))
        self.myinfopage.mydraw.setText('무승부 : '+str(self.userdata.resultinfo[0][9]))
        self.myinfopage.mywinrate.setText('승률 : '+str(self.userdata.resultinfo[0][7])+'%')
        self.myinfopage.mygame.setText('게임 수: '+str(self.userdata.resultinfo[0][8]))
        self.myinfopage.returnbutton.clicked.connect(self.returngame)
        
    def returngame(self):
        self.mainwindow.resize(self.game.game_x,self.game.game_y)
        self.paper.setCurrentIndex(2)


    def SetupUi(self):
        self.mainwindow.resize(200,220)
        self.mainwindow.setWindowTitle('rock scissor paper')
        self.paper=QtWidgets.QStackedWidget(self.mainwindow)
        self.paper.setGeometry(0,0,500,500)
        
    def Page(self):
        self.paper.addWidget(self.login.loginpage)
        self.paper.addWidget(self.resister.resisterpage)
        self.paper.addWidget(self.game.gamepage)
        self.paper.addWidget(self.myinfopage.myinformation)
        self.paper.addWidget(self.rankingpage.rankpage)
        self.paper.setCurrentIndex(0)
        
    def Signuppage(self):
        self.mainwindow.resize(self.resister.resister_x,self.resister.resister_y)
        self.paper.setCurrentIndex(1)

    def signup(self):
        if self.resister.password.text()!=self.resister.pwcheck.text():
            self.resister.openmessage()
            self.resister.password.setText(None)
            self.resister.pwcheck.setText(None)
        
        else:
            try:
                self.userdata.resister(self.resister.id.text(),self.resister.password.text(),self.resister.name.text(),self.resister.email.text(),self.resister.phonenumber.text())
                self.resister.openmessage2()
                self.resister.id.setText(None)
                self.resister.password.setText(None)
                self.resister.pwcheck.setText(None)
                self.resister.name.setText(None)
                self.resister.email.setText(None)
                self.resister.phonenumber.setText(None)
                self.paper.setCurrentIndex(0)
            except sqlite3.IntegrityError:
                self.resister.openmessage3()
                self.resister.id.setText(None)

    def trylogin(self):
        self.userdata.data()
        self.userdata.cur.execute("SELECT id,password FROM user WHERE id = '" +self.login.id.text()+"' and password = '"+self.login.password.text()+"'")
        self.result=self.userdata.cur.fetchall()
        
        if len(self.result)==0:
            self.resister.openmessage4()
            self.login.password.setText(None)
        elif len(self.result)!=0:
            self.loginsuccess()

    def loginsuccess(self):
        
        self.mainwindow.resize(self.game.game_x,self.game.game_y)
        self.paper.setCurrentIndex(2)
        self.game.enemyfight.start()
        self.userdata.myname(self.login.id.text())
        self.game.myid.setText('어서오세요 '+self.userdata.myidname[0][0]+' 님')

    


if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    asdf=Mainui()
    asdf.Page()
    asdf.show()
    
    sys.exit(app.exec_())