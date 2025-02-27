import sys
import pyttsx3
import tkinter as tk
import threading
lst,s = sys.argv, ''
gc=lst[-1]
lst = lst[1:-1]
for i in lst:
    s+=i+' '
fs=s
for i in range(len(s)):
    if i%100==0:
        fs=fs[:i]+'\n'+fs[i:]
def speak(x:str):
    engine = pyttsx3.init()
    print(x,x.replace('\n',''))
    x=x.replace('\n','')
    engine.say(x)
    engine.runAndWait()
    try:app.quit()
    except:pass
app=''
def gui(fs):
    global app
    app = tk.Tk()
    tk.Label(app,text=fs).pack()
    app.mainloop()
if gc=='gui':
    p1 = threading.Thread(target=gui, args=[fs, ])
    p1.start()
p2 = threading.Thread(target=speak,args=[s,])
p2.start()
if gc=='gui': p1.join()
p2.join()