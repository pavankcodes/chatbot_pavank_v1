import os
from mechanisms import  db_manager
from sub_scripts import data
dMan = db_manager.dbhelper()
def get_usrs():
    usrs,usrpwd=[],{}
    for i in dMan.fetchall(): usrs.append(i)
    for i in usrs: usrpwd[i[1]]=i[2]
    return usrpwd
def add_usr(n,p):
    i=len(get_usrs())
    dMan.inser_user(i,n,p)
def get_settings():
    x,settings=dMan.fetch_settings_table(),{}
    for i in x: settings[i[0]]=i[1]
    return settings
def update_settings(n):
    dMan.update_settings(n['mode'],n['theme'])
def update_chats(n,m):
    print('msg:',m)
    m=m.replace('"',"'")
    m=m.replace('\n','{-n-}')
    dMan.add_chat(n,m)
def update__clrchats(n):
    dMan.clear_chat(n)
    print('cleared')
def get_chat():
    usr_msg,chat={},[]
    print(data.login_app_data.currUser,'hoiu')
    for i in dMan.fetch_chat_table():
        usr_msg[i[0]]=i[1]
        if i[0]==data.login_app_data.currUser:    chat.append(i[1])
    return usr_msg,chat
def del_user(u_id):
    dMan.delete_user(u_id)
def upd_chat_mem(u,x,y):
    try:dMan.update_table_chatmem(u,x,y)
    except:pass