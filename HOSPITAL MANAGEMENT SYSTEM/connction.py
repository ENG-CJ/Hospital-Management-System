import urllib
from  urllib.request import urlopen
from tkinter import messagebox
from  tkinter import *
import time

def isinternet():
    window = Tk()
    window.geometry('400x200')
    window.config(bg='white')
    window.resizable(0,0)
    # global error
    error = Label(window, text='', bg='white', fg='red', font=('Verdana', 16, 'bold'))
    error.pack(pady=60)

    error2 = Label(window, text='', bg='white', fg='#dc143c', font=('Verdana', 13))
    error2.place(x=90,y=90)
    try:
      active=urlopen('https://www.google.com',timeout=1)
      if active:
          window.destroy()
          import HOSPITAL_SYSTEM as hp
          hp=hp.DARUL_SHIFA_HOSPITAL()
          hp.login_page()
          return True
      else:
          error.config(text='No Internet Connection')
          return  False

    except Exception as err:
        window.title('Network Error')
        error.config(text='No Internet Connection')
        error2.config(text='Turn On Your Internet')

    mainloop()

isinternet()
