from sub_scripts import data
from mechanisms import db_access
import os
import speech_recognition as sr
import tkinter as tk
from tkinter import messagebox as mb
t,old_msgs='','no'
def authcheck(usr,pwd):
    global t
    t=usr
    dat=data.login_app_data
    usrs=dat.auths.keys()
    if usr.strip()=='' or pwd.strip()=='':print('Entry is missing')
    elif usr in usrs:
        if pwd==dat.auths[usr]:
            print('Successfully Login.')
            data.login_app_data.status='in'
            data.login_app_data.currUser=usr
            check_old_stuff()
            return True
        else:print('incorrect pwd')
    else:print('incorrect user name')    
    data.login_app_data.status='out'
    return False
def check_old_stuff():
    if data.login_app_data.status=='in':
        usrmsg,chat = db_access.get_chat()
        if t in usrmsg:
            data.login_app_data.usr_data_old= 'Yes'
            data.login_app_data.data = chat
def db_add_user(n,p):
    try: db_access.add_usr(n,p)
    except:
        print('err')
        import tkinter.messagebox as msg 
        msg.showerror('Ops','Try Again')
def db_upd_settings(_s):db_access.update_settings(_s)
def db_upd_chats(msgs,):
    print(data.login_app_data.currUser,msgs)
    db_access.update_chats(t,str(msgs))
def db_clr_cht():
    global t
    print('hkh',t)
    db_access.update__clrchats(t)
def saytxt(x):
    if '\n' in x:cmd='start cmd /c python mechanisms/t2s.py '+x.replace('\n',' ')+' gui'
    else:cmd='start cmd /c python mechanisms/t2s.py '+x+' gui'
    print(cmd)
    os.system(cmd)
def saytxtnogui(x):
    try:
        if '\n' in x: cmd='start cmd /c python mechanisms/t2s.py '+x.replace('\n',' ')+' nogui'
        else:cmd='start cmd /c python mechanisms/t2s.py '+x+' gui'
        print(cmd)
        os.system(cmd)
    except:print('no audio support')
def db_del_usr(u_id):
    db_access.del_user(u_id)
def send_mem_data(x,y):
    print(data.login_app_data.uid, x, y)
    db_access.upd_chat_mem(data.login_app_data.uid,x,y)