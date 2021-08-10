import sqlite3

class UserData:
    def __init__(self):
        self.player=None

    def data(self):
        self.conn=sqlite3.connect('userdata.db')
        self.cur=self.conn.cursor()
        #self.cur.execute('DROP TABLE user')
        #self.cur.execute("CREATE TABLE user(id PRIMARY KEY, password TEXT,name TEXT,email TEXT,phonenumber TEXT,win INTEGER,lose INTEGER,winrate INGETER, game INTEGER,draw INTEGER)")
        
        
    def resister(self,id,pw,name,email,phonenumber):
        self.data()
        self.id=id
        self.pw=pw
        self.name=name
        self.email=email
        self.phonenumber=phonenumber
        self.cur.execute('INSERT INTO user VALUES("'+self.id+'","'+self.pw+'","'+self.name+'","'+self.email+'","'+self.phonenumber+'",0,0,0,0,0)')
        self.conn.commit()



    def win(self,id):
        self.player=id 
        self.cur.execute('UPDATE user SET win = win+1, game = game+1 where id = "'+self.player+'" ')
        self.conn.commit()

        

    def lose(self,id):
        self.player=id 
        self.cur.execute('UPDATE user SET lose = lose+1, game = game+1 WHERE id = "'+self.player+'" ')
        self.conn.commit()
        
    def draw(self,id):
        self.player=id
        self.cur.execute('UPDATE user SET draw = draw+1, game = game+1 WHERE id = "'+self.player+'" ')
        self.conn.commit()

    def findwinrate(self,id):
        self.player=id
        self.cur.execute('SELECT win,game from user WHERE id ="'+self.player+'"')
        self.result=self.cur.fetchall()
        
        self.winrate=int(self.result[0][0]/self.result[0][1]*100)
        self.cur.execute('UPDATE user SET winrate = "'+str(self.winrate)+'" WHERE id = "'+self.player+'" ')
        self.conn.commit()

    def myinfo(self,id):
        self.player=id
        self.cur.execute('SELECT * from user WHERE id ="'+self.player+'" ')
        self.resultinfo=self.cur.fetchall()
        self.conn.commit()
        return self.resultinfo

    def myname(self,id):
        self.player=id
        self.cur.execute('SELECT name from user WHERE id ="'+self.player+'" ')
        self.myidname=self.cur.fetchall()
        self.conn.commit()
        return self.myidname

    def ranking(self):
        self.cur.execute('SELECT name,win,lose,winrate,game,draw FROM user ORDER BY winrate DESC ')
        self.rankinginfo=self.cur.fetchall()
        return self.rankinginfo

        

