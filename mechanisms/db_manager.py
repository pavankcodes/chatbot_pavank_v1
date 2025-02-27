import mysql.connector as connector
from tkinter import simpledialog
class dbhelper:
    def __init__(self):
        paswd='mysql'
        try:
            self.con = connector.connect(
            host='localhost',user='root',password=paswd,)
        except:
            paswd=simpledialog.askstring("SQL error", "Please enter your sql pass:")
            self.con = connector.connect(
            host='localhost',user='root',password=paswd,)
        query='create database if not exists neo'
        cur = self.con.cursor()
        cur.execute(query)
        self.con = connector.connect(
        host='localhost',user='root',password=paswd,database='neo')
        query='create table if not exists user(id int primary key, name varchar(100), pwd varchar(100))'
        cur = self.con.cursor()
        cur.execute(query)
        try:
            query="""INSERT INTO user VALUES(0,'admin','admin')"""
            cur = self.con.cursor()
            cur.execute(query)
        except:pass
        query='create table if not exists chat(user varchar(100), messages longtext)'
        cur = self.con.cursor()
        cur.execute(query)
        query='create table if not exists settings(property varchar(255) primary key,value varchar(255))'
        cur = self.con.cursor()
        cur.execute(query)
        try:
            query="""INSERT INTO settings(property, value) VALUES('mode', 'Light'),('theme', 'themes/red.json')"""
            cur = self.con.cursor()
            cur.execute(query)
        except:pass
        query='create table if not exists chat_storage(uid int , msg_no int , query longtext, response longtext)'
        cur = self.con.cursor()
        cur.execute(query)
    def inser_user(self,uid,name,role):
        query="insert into user (id,name,pwd) values({},'{}','{}')".format(uid,name,role)
        c=self.con.cursor()
        c.execute(query)
        self.con.commit()
    def fetchall(self):
        query='select * from user'
        cur=self.con.cursor()
        cur.execute(query)
        return cur
    def delusr(self,uid):
        query = 'delete from user where user_id ={}'.format(uid)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
    def fetch_settings_table(self):
        query='select * from settings'
        cur=self.con.cursor()
        cur.execute(query)
        return cur
    def update_settings(self,name,value):
        query="update settings set value='{}' where property='mode'".format(name)
        c=self.con.cursor()
        c.execute(query)
        self.con.commit()
        query="UPDATE settings SET value='{}' WHERE property='theme'".format(value)
        c=self.con.cursor()
        c.execute(query)
        self.con.commit()
    def add_chat(self,usr,msgs):
        query="""insert into chat (user,messages) values("{}","{}")""".format(usr,msgs)
        c=self.con.cursor()
        c.execute(query)
        self.con.commit()
    def clear_chat(self,usr):
        query="""delete from chat where user="{}" """.format(usr)
        print(query)
        c=self.con.cursor()
        c.execute(query)
        self.con.commit()
    def fetch_chat_table(self):
        query='select * from chat'
        cur=self.con.cursor()
        cur.execute(query)
        return cur
    def delete_user(self,u_id):
        query="""delete from user where id={} """.format(u_id)
        print(query)
        c=self.con.cursor()
        c.execute(query)
        self.con.commit()
    def update_table_chatmem(self,u,x,y):
        query='select count(msg_no) from chat_storage where uid={}'.format(u)
        cur=self.con.cursor()
        cur.execute(query)
        print(query,cur)
        print(cur)
        n=cur.fetchall()[0][0]
        print(cur)
        x=x.replace('\n','{-new-}')
        y=y.replace('\n','{-new-}')
        if "'" in x:  x.replace("'",'')
        if "'" in y:  y.replace("'",'')
        if '"' in x:  x.replace('"','')
        if '"' in y:  y.replace('"','') 
        query="insert into chat_storage values({},{},'{}','{}')".format(u,n+1,x,y)
        print(query)
        c=self.con.cursor()
        c.execute(query)
        self.con.commit()
