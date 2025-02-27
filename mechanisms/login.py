import os
import customtkinter as ctk
from sub_scripts.data import login_app_data as dat
from PIL import Image,ImageTk
from sub_scripts import brain
import tkinter
from tkinter.simpledialog import askstring
from tkinter import messagebox as msgbx
def combobox_callback(choice): print("combobox dropdown clicked:", choice)
def login():
    def login_event():
        if brain.authcheck( usrname.get(),usrpwd.get() ):
            dat.currUser=usrname.get()
            dat.uid=_names.index(dat.currUser)
            app.destroy()
        else:msgbx.showinfo('Ops','Incorrect Password.\nTry again.')
    def register_event():
        if usrname.get().strip()!='':
            print('registering')
            n=askstring('Registry Name:','Name')
            p=askstring('Registry pass:','Pass')
            if n.replace(' ','') not in _names and n.replace(' ','') not in (None,'' ) and p not in (None,''):
                brain.db_add_user(n,p)
                msgbx.showinfo('Info','Done registering, restart to apply')
            else:
                msgbx.showinfo('Ops','1. Retry with different user name\n2. Fill non empty password')
    def delete_event():
        if usrname.get().strip()!='':
            print('registering')
            n=askstring('Registry Name:','Name')
            p=askstring('Registry pass:','Pass')
            print(n,p)
            if n.replace(' ','') in _names and n.replace(' ','') not in (None,'' ) and p not in (None,''):
                brain.db_del_usr(_names.index(n.strip())+1)
                msgbx.showinfo('Info','Deleted User')
                msgbx.showinfo('Info','Done, restart to apply changes')
            else:
                msgbx.showinfo('Ops','1. Incorrect User\n2. Incorrect password')
    app=ctk.CTk()
    app.title(dat.title)
    app.resizable(False,False)
    ctk.set_default_color_theme(dat.theme)  
    ctk.set_appearance_mode(dat.mode)
    app.geometry(dat.geometry)
    img = Image.open('res/logo.jpg')
    i = ctk.CTkImage(light_image=img,dark_image=img,size=(250,250))
    frame = ctk.CTkFrame(app) 
    frame.pack(pady=20,padx=40,fill='both',expand=True) 
    label = ctk.CTkLabel(frame,text='AUTHORIZATION REQUIRED',font=ctk.CTkFont(size=20, weight="bold")) 
    label.pack(pady=12,padx=10) 
    label = ctk.CTkLabel(frame,text='', image=i) 
    label.pack(pady=12,padx=10) 
    _names=[]
    for i in dat.auths:_names.append(i)
    usrname = ctk.CTkComboBox(master=frame, values=_names, command=combobox_callback)
    usrname.pack(padx=20, pady=10)
    usrpwd= ctk.CTkEntry(frame,placeholder_text="Password",show="*") 
    usrpwd.pack(pady=12,padx=10) 
    button = ctk.CTkButton(frame,text='Login',command=login_event) 
    button.pack(pady=12,padx=10) 
    button = ctk.CTkButton(frame,text='Register',command=register_event) 
    button.pack(pady=12,padx=10)
    button = ctk.CTkButton(frame,text='Delete Account',command=delete_event) 
    button.pack(pady=12,padx=10)
    app.mainloop()