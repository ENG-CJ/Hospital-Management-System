from tkinter import *
from PIL import ImageTk,Image
import  webbrowser


def activate(e):
    image_label.config(text='ADMIN',image='',bg='white',fg='blue',font=('Verdana',50,'bold','underline'))
    image_label.place(x=180,y=210)
def leave(e):
    image_label.config(image=new)
    image_label.place(x=100, y=100)
def my_fb():
    webbrowser.open('https://www.facebook.com/abdulrahman.haaji.1')
def my_git():
    webbrowser.open('https://github.com/ENG-CJ')




def developers():
    dev=Toplevel()
    dev.state('zoomed')
    dev.focus()
    dev.title('Developers Of This System')
    dev.resizable(0,0)
    dev.config(bg='white')

    # images


    CJ =Image.open('Dev_Images/ENG-CJ.png')
    resize=CJ.resize((400,400),Image.ANTIALIAS)
    global new
    new=ImageTk.PhotoImage(resize)
    global image_label
    image_label=Label(dev,bg='white',image=new
          ,bd=0)
    # image_label.bind('<Enter>',activate)
    # image_label.bind('<Leave>',leave)
    image_label.place(x=100,y=100)
    Label(dev,text='Abdulrahman Haaji',bg='white',fg='#151b54',font=('Verdana',14,'bold')
          ).place(x=190,y=380)

    Label(dev,text='Software Dev',bg='white',fg='blue',font=('Verdana',8)
          ).place(x=250,y=410)

    # icons social
    facebook=Image.open('icons/fb.png')
    fb_res=facebook.resize((30,30),Image.ANTIALIAS)
    new_fb=ImageTk.PhotoImage(fb_res)
    Button(dev,command=my_fb,cursor='hand2',image=new_fb,bg='white',bd=0,activebackground='white').place(x=250,y=432)

    # github
    github=Image.open('icons/Git.png')
    git=github.resize((35,35),Image.ANTIALIAS)
    new_github=ImageTk.PhotoImage(git)
    Button(dev,command=my_git,cursor='hand2',image=new_github,bg='white',bd=0,activebackground='white').place(x=290,y=430)


    #icon 2

    qadra =Image.open('Dev_Images/qadra.png')
    res_qadra=qadra.resize((370,370),Image.ANTIALIAS)
    new2=ImageTk.PhotoImage(res_qadra)
    Label(dev, bg='white', image=new2
          , bd=0).place(x=450, y=70)
    Label(dev, text='Qadra Mohamud', bg='white', fg='#151b54', font=('Verdana', 14, 'bold')
          ).place(x=550, y=380)

    Label(dev, text='Unknown', bg='white', fg='blue', font=('Verdana', 8)
          ).place(x=620, y=410)

    #icons
    facebook2 = Image.open('icons/fb.png')
    fb_res2 = facebook2.resize((30, 30), Image.ANTIALIAS)
    new_fb2 = ImageTk.PhotoImage(fb_res2)
    Button(dev, image=new_fb2,cursor='hand2', bg='white', bd=0, activebackground='white').place(x=610, y=432)

    # github
    github2 = Image.open('icons/Git.png')
    git2 = github2.resize((35, 35), Image.ANTIALIAS)
    new_github2= ImageTk.PhotoImage(git2)
    Button(dev, image=new_github2,cursor='hand2', bg='white', bd=0, activebackground='white').place(x=655, y=430)


    # icon 3
    kavi = Image.open('Dev_Images/kaavi.png')
    kavi2 = kavi.resize((380, 380), Image.ANTIALIAS)
    new3 = ImageTk.PhotoImage(kavi2)
    Label(dev, bg='white', image=new3
          , bd=0).place(x=780, y=65)
    Label(dev, text='Mohamed Ali', bg='white', fg='#151b54', font=('Verdana', 14, 'bold')
          ).place(x=890, y=380)

    Label(dev, text='Web Dev', bg='white', fg='blue', font=('Verdana', 8)
          ).place(x=930, y=410)

    facebook3 = Image.open('icons/fb.png')
    fb_res3 = facebook3.resize((30, 30), Image.ANTIALIAS)
    new_fb3 = ImageTk.PhotoImage(fb_res3)
    Button(dev, image=new_fb3, bg='white', bd=0, activebackground='white',cursor='hand2').place(x=920, y=432)

    # github
    github3 = Image.open('icons/Git.png')
    git3 = github3.resize((35, 35), Image.ANTIALIAS)
    new_github3 = ImageTk.PhotoImage(git3)
    Button(dev, image=new_github3, bg='white', bd=0, activebackground='white',cursor='hand2').place(x=965, y=430)
    mainloop()


