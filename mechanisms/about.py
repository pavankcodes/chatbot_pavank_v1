import webbrowser
import os
def about_page():
    print('about-secd', os.path.join(os.getcwd(),'mechanisms','guide_page','index.html'))
    # webbrowser.open("https://www.google.com")
    webbrowser.open(os.path.join(os.getcwd(),'mechanisms','guide_page','index.html'))

def featpge():
    webbrowser.open(os.path.join(os.getcwd(),'mechanisms','guide_page','index.html#features'))
# about_page()