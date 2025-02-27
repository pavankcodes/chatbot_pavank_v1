import os,time
import customtkinter as ctk
import tkinter as tk
import speech_recognition as sr
from tkinter import messagebox as mb
from tkinter.filedialog import askopenfilename,asksaveasfilename
import google.generativeai as genai
from PIL import Image,ImageTk
import pyperclip as pclip
import threading
from mechanisms import login,about
from sub_scripts import data,brain
class tmp_data_:tmp_msgs={}
print('starting')
try:
    genai.configure(api_key='AIzaSyB98MiNh1yZnXpWoV9vcWedoj58R2Wh6DU')
    model = genai.GenerativeModel('gemini-pro')
    modelvision = genai.GenerativeModel('gemini-1.5-flash')
    chat=model.start_chat()
    for i in data.inst_txt:
        chat.send_message(i).text
        print('loading ..')
    chat.send_message('my name is '+data.login_app_data.currUser)
except:None
_theme = data.settings['theme']
_mode = data.settings['mode']
ctk.set_default_color_theme(_theme)  
ctk.set_appearance_mode(_mode)
class tmp:
    fullScreen,i_search = True,False
    img_file,_chat_id ='', -1
class Neo( ctk.CTk ):
    def __init__(self):
        super().__init__()
        self.title('Neo ChatBot')
        self.geometry('1000x600')
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=10)
        self.sidebar_frame.grid(row=0, column=0, rowspan=6, sticky="nsew", padx=10,pady=10)
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.sidebar_frame2 = ctk.CTkFrame(self, width=140, corner_radius=10)
        self.sidebar_frame2.grid(row=1, column=3, rowspan=6, sticky="nsew", padx=10,pady=10)
        self.sidebar_frame2.grid_rowconfigure(4, weight=1)
        self.sidebar_button_1 = ctk.CTkLabel(self.sidebar_frame2, text='Features', font=ctk.CTkFont(size=20, weight="bold"))
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_1 = ctk.CTkButton(self.sidebar_frame2, text='Voice-IN', command=self.listen_to_user )
        self.sidebar_button_1.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_1 = ctk.CTkButton(self.sidebar_frame2, text=data.login_app_data.currUser, command=lambda: mb.askokcancel('Info','Current Logged User :'+data.login_app_data.currUser))
        self.sidebar_button_1.grid(row=9, column=0, padx=20, pady=10)
        self.sidebar_button_1 = ctk.CTkButton(self.sidebar_frame2, text='ClearChat', command=self.clear_chat_btn)
        self.sidebar_button_1.grid(row=10, column=0, padx=20, pady=10)
        self.sidebar_button_1 = ctk.CTkButton(self.sidebar_frame2, text='Quit', command=self.on_closing)
        self.sidebar_button_1.grid(row=11, column=0, padx=20, pady=10)
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Neo ChatBot", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = ctk.CTkButton(self.sidebar_frame, text='About', command=about.about_page)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = ctk.CTkButton(self.sidebar_frame, text='Features', command=about.featpge)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.fullscrn_button=ctk.CTkCheckBox(master=self.sidebar_frame, text="Full Screen", command=self.full_screen_event, onvalue="on", offvalue="off")
        self.fullscrn_button.grid(row=4,column=0)
        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],command=self.change_apr_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.appearance_mode_optionemenu.set(_mode)
        self.scaling_label = ctk.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))
        self.scaling_optionemenu.set('100%')
        self.scaling_label = ctk.CTkLabel(self.sidebar_frame, text="Theme:", anchor="w")
        self.scaling_label.grid(row=9, column=0, padx=20, pady=(10, 0))
        self.theme_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=['red',"blue", "green", "marsh", "sky", "violet",'orange'], command=self.change_theme_event)
        self.theme_optionemenu.grid(row=10, column=0, padx=20, pady=(10, 20))
        self.theme_optionemenu.set(data.settings['theme'].split('/')[1][:-5] if '/' in data.settings['theme'] else data.settings['theme'])
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.title_label = ctk.CTkLabel(self, text='Neo',font=ctk.CTkFont(size=20, weight="bold"))
        self.title_label.grid(row=0, column=1, sticky="ew", padx=10,pady=10)
        self.scrollable_frame = ctk.CTkScrollableFrame(self, label_text="Neo",label_font=('Helvetica',18) ,height=self.winfo_screenheight())
        self.scrollable_frame.grid(row=1, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.entry = ctk.CTkEntry(self,placeholder_text="message here")
        self.entry.grid(row=3, column=1, padx=(20, 20), pady=(20, 5), sticky="WENS")
        self.main_button_1 = ctk.CTkButton(master=self,width=self.winfo_width()//0.8, text="\U00002713",command=self.send_query, border_width=2, text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=4, column=1, padx=(20, 20), pady=(0, 5),sticky='NSEW')  
        self.main_button_1 = ctk.CTkButton(master=self,width=self.winfo_width()//0.8, text="Image", command=self.img_in, border_width=2, text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=5, column=1, padx=(20, 20), pady=(0, 5),sticky='NSEW')  
        if data.login_app_data.usr_data_old=='Yes':
            olddata=data.login_app_data.data
            print(olddata)
            for _m in olddata:
                import os
                os.system('cls')
                for i in range( _m.count('[{(') ):
                    _k=str(_m).split(')}]')
                    print(_k[i],_k[i+1])
                    _k = _k[i].split('|||')
                    os.system('cls')
                    print(_k)
                    self.send_query(_k[0],_k[1]) 
    def update_theme(self):print('updated')
    def listen_to_user(self):
        self.entry.delete(0,'end')
        with sr.Microphone() as source:
            r = sr.Recognizer()
            r.adjust_for_ambient_noise(source)
            print('speak now')
            audio = r.listen(source)
        try:text = r.recognize_google(audio)
        except:
            text="Sorry, I couldn't understand that."
            print(text)
        self.entry.insert(0,text)
    def change_apr_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)
        _mode=new_appearance_mode
        data.settings['mode']=new_appearance_mode
    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)
    def full_screen_event(self):
        def full():self.attributes('-fullscreen', True)
        def fex():self.attributes('-fullscreen', False)
        if mb.askokcancel('Full Screen','want to update settings? '):full()
        else:fex()
    def change_theme_event(self, theme_name:str):
        new_theme=theme_name.lower()
        if new_theme not in ['blue']: new_theme='themes/'+new_theme+'.json'
        res=mb.askquestion('Exit Application', 'Apply , quit and reopen?')
        if res=='yes':
            data.settings['theme']=new_theme
            brain.db_upd_settings(data.settings)
            self.quit()
    def on_closing(self):
        if mb.askokcancel('Quit','Do you want to quit/update? '):
            msgs=''
            if tmp_data_.tmp_msgs!={}:
                for i,j in tmp_data_.tmp_msgs.items():
                    msgs=msgs+'[{( '+i+' ||| '+j+ ' )}]'
                brain.db_upd_chats(msgs)
            quit()
    def sidebar_button_event(self):print("sidebar_button click")
    def img_in(self):
        tmp.img_file = askopenfilename()
        tmp.i_search=True
        if tmp.img_file!='':
            img=Image.open(tmp.img_file)
            f=ctk.CTkFrame(self.scrollable_frame)
            ctk.CTkLabel(f,text='',image=ctk.CTkImage( light_image=img,	dark_image=img,	size=(500,350) )).grid(row=0,column=0)
            if tmp._chat_id%2!=0:tmp._chat_id+=1
            if tmp._chat_id%2==0:f.grid(row=tmp._chat_id,column=0,sticky='e', pady=(5,10),padx=(10,10))
            else:f.grid(row=tmp._chat_id,column=0,sticky='w',pady=(5,10),padx=(10,10))
    def clear_chat_btn(self):
        brain.db_clr_cht()
        self.on_closing()
    def send_query(self,um=0,gm=0):
        if um==gm==0:
            f=ctk.CTkFrame(self.scrollable_frame)
            if tmp.i_search:
                img=Image.open(tmp.img_file)
            _lbl = ctk.CTkLabel(f,text=self.entry.get(),font=ctk.CTkFont(size=15, weight="bold"))
            btns_f = ctk.CTkFrame(f)
            cpy_btn = ctk.CTkButton(btns_f, fg_color="transparent",text='copy')
            cpy_btn.grid(row=1,column=0)
            cpy_btn = ctk.CTkButton(btns_f, fg_color="transparent",text='speak', command= lambda: brain.saytxt(self.entry.get()))
            cpy_btn.grid(row=1,column=1)
            cpy_btn = ctk.CTkButton(btns_f, fg_color="transparent",text='save')
            cpy_btn.grid(row=1,column=2)
            tmp._chat_id+=1
            if tmp._chat_id%2!=0:tmp._chat_id+=1
            if tmp._chat_id%2==0:
                f.grid(row=tmp._chat_id,column=0,sticky='e', pady=(5,10),padx=(10,10))
                _lbl.grid(row=1,column=0,sticky='w')
            else:
                btns_f.grid(row=2,column=0)
                f.grid(row=tmp._chat_id,column=0,sticky='w',pady=(5,10),padx=(10,10))
                _lbl.grid(row=1,column=0,sticky='e')
            try:
                res=''
                if tmp.i_search:
                    res=modelvision.generate_content(contents=[self.entry.get(),img]).text
                else:res=chat.send_message(self.entry.get()).text
            except:res='Connect to internet'
            tb_h=(len(res.split())/80*25)//1 +  res.count('\n')*3
            if tb_h>350:tb_h=300
            f=ctk.CTkFrame(self.scrollable_frame,)
            _lbl = ctk.CTkTextbox(f,height=tb_h+50,width=500)
            _lbl.insert(1.0,res)
            if tmp.i_search:    
                tmp.i_search=False
                tmp_data_.tmp_msgs[tmp.img_file+'#imgIimg#'+ self.entry.get()]=res
            else:tmp_data_.tmp_msgs[tmp.img_file+ self.entry.get()]=res
            btns_f = ctk.CTkFrame(f)
            brain.send_mem_data(tmp.img_file+ self.entry.get(),res) 
            def cpy_cmd():pclip.copy(res)
            def savebtn():
                saveTofile=asksaveasfilename()
                currtime=time.ctime()
                with open(saveTofile,'a+') as file:
                    file.write(res)
                _cmd = f'notepad {saveTofile}'
                os.system(_cmd)
            def spkbtn():
                brain.saytxt(res)
            cpy_btn = ctk.CTkButton(btns_f,command=cpy_cmd, fg_color="transparent",text='copy')
            cpy_btn.grid(row=1,column=0)
            cpy_btn = ctk.CTkButton(btns_f, fg_color="transparent",text='speak', command=spkbtn)
            cpy_btn.grid(row=1,column=1)
            cpy_btn = ctk.CTkButton(btns_f,command=savebtn, fg_color="transparent",text='save')
            cpy_btn.grid(row=1,column=2)
            tmp._chat_id+=1
            if tmp._chat_id%2==0:
                f.grid(row=tmp._chat_id,column=0,sticky='e', pady=(5,10),padx=(10,10))
                _lbl.grid(row=1,column=0,sticky='e')
            else:
                btns_f.grid(row=2,column=0)
                f.grid(row=tmp._chat_id,column=0,sticky='w',pady=(5,10),padx=(10,10))
                _lbl.grid(row=1,column=0,sticky='w')
        else:
            f=ctk.CTkFrame(self.scrollable_frame)
            if '#imgIimg#' in um:
                img=Image.open(um.split('#imgIimg#')[0][4:])
                img=ctk.CTkLabel(f,text='',image=ctk.CTkImage( light_image=img,	dark_image=img,	size=(500,350) )).grid(row=0,column=0)
                _lbl1 = ctk.CTkLabel(f,image=img,text='')
                _lbl1.grid(row=0,column=0,sticky='e')
                _lbl = ctk.CTkLabel(f,text=um.split('#imgIimg#')[1],font=ctk.CTkFont(size=15, weight="bold"))
            else:_lbl = ctk.CTkLabel(f,text=um[4:],font=ctk.CTkFont(size=15, weight="bold"))
            btns_f = ctk.CTkFrame(f)
            cpy_btn = ctk.CTkButton(btns_f, fg_color="transparent",text='copy')
            cpy_btn.grid(row=1,column=0)
            cpy_btn = ctk.CTkButton(btns_f, fg_color="transparent",text='speak')
            cpy_btn.grid(row=1,column=1)
            cpy_btn = ctk.CTkButton(btns_f, fg_color="transparent",text='save')
            cpy_btn.grid(row=1,column=2)
            tmp._chat_id+=1
            if tmp._chat_id%2!=0:tmp._chat_id+=1
            if tmp._chat_id%2==0:
                f.grid(row=tmp._chat_id,column=0,sticky='e', pady=(5,10),padx=(10,10))
                _lbl.grid(row=1,column=0,sticky='w')
            else:
                btns_f.grid(row=2,column=0)
                f.grid(row=tmp._chat_id,column=0,sticky='w',pady=(5,10),padx=(10,10))
                _lbl.grid(row=1,column=0,sticky='e')
            try:
                res=gm.replace('{-n-}','\n')
            except:res='Connect to internet'
            tb_h=len(res.split())//15*50 +  res.count('\n')*10
            if tb_h>350:tb_h=300
            f=ctk.CTkFrame(self.scrollable_frame,)
            _lbl = ctk.CTkTextbox(f,height=tb_h+50,width=500)
            _lbl.insert(1.0,res)
            btns_f = ctk.CTkFrame(f)
            def cpy_cmd():pclip.copy(res)
            def savebtn():
                saveTofile=asksaveasfilename()
                currtime=time.ctime()
                with open(saveTofile,'a+') as file:
                    file.write(res)
                _cmd = f'notepad {saveTofile}'
                os.system(_cmd)
            cpy_btn = ctk.CTkButton(btns_f,command=cpy_cmd, fg_color="transparent",text='copy')
            cpy_btn.grid(row=1,column=0)
            cpy_btn = ctk.CTkButton(btns_f, fg_color="transparent",text='speak', command=lambda: brain.saytxt(res))
            cpy_btn.grid(row=1,column=1)
            cpy_btn = ctk.CTkButton(btns_f,command=savebtn, fg_color="transparent",text='save')
            cpy_btn.grid(row=1,column=2)
            tmp._chat_id+=1
            if tmp._chat_id%2==0:
                f.grid(row=tmp._chat_id,column=0,sticky='e', pady=(5,10),padx=(10,10))
                _lbl.grid(row=1,column=0,sticky='e')
            else:
                btns_f.grid(row=2,column=0)
                f.grid(row=tmp._chat_id,column=0,sticky='w',pady=(5,10),padx=(10,10))
                _lbl.grid(row=1,column=0,sticky='w')
            if tmp_data_.tmp_msgs!={}:
                for i,j in tmp_data_.tmp_msgs.items():
                    msgs=msgs+'[{( '+i+' ||| '+j+ ' )}]'
                brain.db_upd_chats(msgs)
                tmp_data_.tmp_msgs={}
if __name__ == '__main__':
    brain.saytxtnogui("Please pass your credentials.")
    login.login()
    brain.saytxtnogui("welcome "+data.login_app_data.currUser)
    if data.login_app_data.status=='in':
        Neo().mainloop()
