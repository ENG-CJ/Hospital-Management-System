from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox,ttk




class NURSES:
    def products(self):
        self.Nurses=Toplevel()
        # self.product.geometry('1100x740+30+20')
        self.Nurses.state('zoomed')
        self.Nurses.focus_force()
        self.Nurses.title('Nursess')
        self.Nurses.resizable(0,0)
        self.Nurses.config(bg='#fff')
        # self.Nurses.iconbitmap('logo.ico')




        # Nurses
        Label(self.Nurses,text='DARUL-SHIFA HOSPITAL | MANAGE NURSES',bg='#015',fg='white',bd=3,relief='flat',
              font=('Verdana',20,'bold'),height=2).pack(fill=X)
        self.clock= Label(self.Nurses,bg='#015',fg='white',bd=3,relief='flat',
              font=('Verdana',18,'bold'),height=2)
        self.clock.place(x=0,y=0)
        self.clock_()

        # image
        self.log = Image.open('icons/lg.png')
        self.resizing = self.log.resize((60, 60), Image.ANTIALIAS)
        self.new_icon = ImageTk.PhotoImage(self.resizing)
        self.lb = Label(self.Nurses,bg='#015', image=self.new_icon, bd=0)
        self.lb.place(x=330, y=5)

        Label(self.Nurses,text='NurseID',bg='white',fg='#6c63ff',font=('Verdana',19,'bold')
              ).place(x=10,y=100)
        self.drid=Entry(self.Nurses,bg='#c0b6ff',fg='black',font=('Verdana',15,'bold'),
                         bd=4,relief='sunken',width=10)
        self.drid.place(x=10,y=150)

        # Nurses name
        Label(self.Nurses,text='Nurse-Name',bg='white',fg='#6c63ff',font=('Verdana',19,'bold')
              ).place(x=10,y=200)
        self.drname=Entry(self.Nurses,bg='#c0b6ff',fg='black',font=('Verdana',15,'bold'),
                         bd=4,relief='sunken',width=15)
        self.drname.place(x=10,y=250)

        # price
        Label(self.Nurses,text='Age',bg='white',fg='#6c63ff',font=('Verdana',19,'bold')
              ).place(x=10,y=300)
        self.age=Entry(self.Nurses,bg='#c0b6ff',fg='black',font=('Verdana',15,'bold'),
                         bd=4,relief='sunken',width=15)
        self.age.place(x=10,y=350)

        # quantity
        Label(self.Nurses, text='Mobile', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=320, y=100)
        self.mobile = Entry(self.Nurses, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                           bd=4, relief='sunken', width=15)
        self.mobile.place(x=320, y=150)


        # address
        Label(self.Nurses, text='Address', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=650, y=100)
        self.address = Entry(self.Nurses, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                           bd=4, relief='sunken', width=10)
        self.address.place(x=650, y=150)

        # baner

        self.banner_img = Image.open('images/female-nurse.jpg')
        self.res = self.banner_img.resize((650, 600), Image.ANTIALIAS)
        self.baner = ImageTk.PhotoImage(self.res)
        Label(self.Nurses, image=self.baner, bg='white', bd=0).place(x=980, y=120)

        # shifts
        Label(self.Nurses, text='Shift', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=850, y=100)
        self.shift_var=StringVar()
        self.shift_var.set('Select ShiftName')
        self.lists=['Get','Normal','ITS']
        self.shifts=ttk.Combobox(self.Nurses,value=self.lists,textvariable=self.shift_var,font=('Verdana',15,'bold'),justify=CENTER)
        self.shifts.place(x=850,y=150,width=230)
        self.shifts['state']='readonly'
        # self.shifts.config(background='red')



        #Date
        Label(self.Nurses, text='Email', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=320, y=200)
        self.email = Entry(self.Nurses, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                           bd=4, relief='sunken', width=15)
        self.email.place(x=320, y=250)

        # Departs
        Label(self.Nurses, text='Departs', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=850, y=200)
        self.dep_var = StringVar()
        self.dep_var.set('Select Departs')
        self.lists2 = ['Get', 'Normal', 'ITS']
        self.departs = ttk.Combobox(self.Nurses, value=self.lists2, textvariable=self.dep_var,
                                   font=('Verdana', 15, 'bold'), justify=CENTER)
        self.departs.place(x=850, y=250, width=230)
        self.departs['state'] = 'readonly'

        # specialist
        Label(self.Nurses, text='Specialist', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=650, y=200)
        self.specialist = Entry(self.Nurses, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                          bd=4, relief='sunken', width=10)
        self.specialist.place(x=650, y=250)

        # sALARAY
        Label(self.Nurses, text='Salary', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=650, y=300)
        self.salary = Entry(self.Nurses, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                                bd=4, relief='sunken', width=10)
        self.salary.place(x=650, y=350)

        Label(self.Nurses, text='Gender', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=320, y=300)
        self.gender_var=StringVar()
        self.male=Radiobutton(self.Nurses,bg='white',fg='#1b1b1b',font=('Verdana', 14,'bold'),text='Male',value='Male',variable=self.gender_var)
        self.male.place(x=320,y=350)

        self.female = Radiobutton(self.Nurses, bg='white', fg='#1b1b1b', font=('Verdana', 14, 'bold'), text='Female',
                                value='Female', variable=self.gender_var)
        self.female.place(x=420, y=350)

        # Buttons
        self.add_btn=Button(self.Nurses,text='Add',bg='#019',fg='white',
                            bd=7,relief='ridge',font=('Verdana',18,'bold'),
                            command=self.add)
        self.add_btn.place(x=190,y=420)

        self.update_btn = Button(self.Nurses, text='Update', bg='#019', fg='white',
                              bd=7, relief='ridge', font=('Verdana', 18, 'bold')
                                 )
        self.update_btn.place(x=290, y=420)

        self.dele = Button(self.Nurses, text='Delete', bg='#019', fg='white',
                              bd=7, relief='ridge', font=('Verdana', 18, 'bold'))

        self.dele.place(x=445, y=420)

        # self.search = Button(self.Nurses, text='Delete', bg='#019', fg='white',
        #                    bd=7, relief='ridge', font=('Verdana', 18, 'bold'), command=self.Delete)
        #
        # self.search.place(x=445, y=420)

        self.search = Entry(self.Nurses, bg='#fff', fg='#019', font=('Verdana', 15, 'bold'),
                          bd=4, relief='ridge', width=15)
        self.search.place(x=1290, y=15)
        self.Nurses.bind('<Control-f>',self.find)
        self.Nurses.bind('<Button-1>',self._find_)
        self.Nurses.bind('<Return>',self._Return_)
        self.drid.focus()

        self.search.insert(0,'Search NurseID')
        self.search.config(state=DISABLED)




        # tree-view table


        self.frame_tree=Frame(self.Nurses,bg='white',width=1090,bd=3,relief='groove')
        self.frame_tree.place(x=5,y=600)
        scrollbar=Scrollbar(self.frame_tree,orient=VERTICAL)
        scrollbar.pack(side=RIGHT,fill=Y)
        self.tree=ttk.Treeview(self.frame_tree,yscrollcommand=scrollbar.set,
                               columns=('NurseID','Nurse-Name','Age','Mobile','Email','Gender','Address','Salary','Shift','Depart'))
        self.tree.pack(fill=BOTH,expand=True)
        # self.tree.bind('<ButtonRelease-1>',self.select)
        scrollbar.config(command=self.tree.yview)
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("Treeview", background='#f4f4f4', foreground='#fff', font=('Verdana', 10),
                        fieldbackground='#f4f4f4')

        self.style2 = ttk.Style()
        self.style2.theme_use('clam')
        self.style2.configure("Combobox", background='red', foreground='#fff', font=('Verdana', 10),
                             fieldbackground='#f4f4f4')
        self.tree.column('#0',width=0,stretch=NO)
        self.tree.column('NurseID',width=80)
        self.tree.column('Nurse-Name',width=220)
        self.tree.column('Age',width=90,anchor=CENTER)
        self.tree.column('Mobile',width=200,anchor=CENTER)
        self.tree.column('Email',width=240,anchor=CENTER)
        self.tree.column('Gender',width=120,anchor=CENTER)
        self.tree.column('Address',width=200,anchor=CENTER)
        self.tree.column('Salary',width=130,anchor=CENTER)
        self.tree.column('Shift',width=100,anchor=CENTER)
        self.tree.column('Depart',width=130,anchor=CENTER)

        self.tree.heading('NurseID',text='NurseID')
        self.tree.heading('Nurse-Name',text='Nurse-Name')
        self.tree.heading('Age',text='Age')
        self.tree.heading('Mobile',text='Mobile')
        self.tree.heading('Email',text='Email')
        self.tree.heading('Gender',text='Gender')
        self.tree.heading('Address',text='Address')
        self.tree.heading('Salary',text='Salary')
        self.tree.heading('Shift',text='Shift')
        self.tree.heading('Depart',text='Depart')


        mainloop()

    def add(self):
        self.tree.insert('',END,values=(self.drid.get(),self.drname.get(),self.age.get(),self.mobile.get(),self.email.get(),self.gender_var.get(),self.address.get(),self.specialist.get(),self.salary.get(),self.shift_var.get(),self.dep_var.get()))


    def find(self,e):
        self.search.config(state=NORMAL)
        self.search.delete(0,END)
        self.search.focus()

    def _find_(self, e):
        self.search.config(state=NORMAL)
        self.search.delete(0, END)
        self.search.focus()

    def _Return_(self, e):
        messagebox.showinfo('INFO', f'You Write {self.search.get()}', parent=self.Nurses)

    def clock_(self):
        import time
        self.hour=time.strftime('%I')
        self.minutes=time.strftime('%M')
        self.secons=time.strftime('%S')
        self.satte=time.strftime('%p')
        self.clock.config(text=f'Time: {self.hour}:{self.minutes}:{self.secons} {self.satte}')
        self.clock.after(1000,self.clock_)
