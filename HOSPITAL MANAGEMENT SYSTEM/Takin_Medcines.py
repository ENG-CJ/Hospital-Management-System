from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox,ttk




class TAK_MEDS:
    def products(self):
        self.product=Tk()
        # self.product.geometry('1100x740+30+20')
        self.product.state('zoomed')
        self.product.focus_force()
        self.product.title('Products')
        self.product.resizable(0,0)
        self.product.config(bg='#fff')
        # self.product.iconbitmap('logo.ico')

        # product
        Label(self.product,text='DARUL-SHIFA HOSPITAL | MANAGE TAKING MEDICINES',bg='#015',fg='white',bd=3,relief='flat',
              font=('Verdana',20,'bold'),height=2).pack(fill=X)
        self.clock= Label(self.product,bg='#015',fg='white',bd=3,relief='flat',
              font=('Verdana',18,'bold'),height=2)
        self.clock.place(x=0,y=0)
        self.clock_()

        # image
        self.log = Image.open('icons/lg.png')
        self.resizing = self.log.resize((60, 60), Image.ANTIALIAS)
        self.new_icon = ImageTk.PhotoImage(self.resizing)
        self.lb = Label(self.product,bg='#015', image=self.new_icon, bd=0)
        self.lb.place(x=330, y=5)

        Label(self.product,text='TAKES_ID',bg='white',fg='#6c63ff',font=('Verdana',19,'bold')
              ).place(x=10,y=100)
        self.takID=Entry(self.product,bg='#c0b6ff',fg='black',font=('Verdana',15,'bold'),
                         bd=4,relief='sunken',width=10)
        self.takID.place(x=10,y=150)

        # product name
        Label(self.product,text='MedID',bg='white',fg='#6c63ff',font=('Verdana',19,'bold')
              ).place(x=10,y=200)

        self.medVar = StringVar()
        self.medVar.set('MedID')
        self.lists4= ['Get', 'Normal', 'ITS']
        self.medID = ttk.Combobox(self.product, value=self.lists4, textvariable=self.medVar,
                                  font=('Verdana', 15, 'bold'), justify=CENTER)
        self.medID.place(x=10, y=250, width=180)
        self.medID['state'] = 'readonly'

        # price
        Label(self.product,text='PatID',bg='white',fg='#6c63ff',font=('Verdana',19,'bold')
              ).place(x=10,y=300)
        self.patID_VAR = StringVar()
        self.patID_VAR.set('PatientID')
        self.lists3 = ['Get', 'Normal', 'ITS']
        self.patID = ttk.Combobox(self.product, value=self.lists3, textvariable=self.patID_VAR,
                                  font=('Verdana', 15, 'bold'), justify=CENTER)
        self.patID.place(x=10, y=350, width=180)
        self.patID['state'] = 'readonly'

        # quantity
        Label(self.product, text='Quantity', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=320, y=100)
        self.qttvar=IntVar()
        self.qty = Spinbox(self.product,textvariable=self.qttvar,from_=1,to=100, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                           bd=4, relief='sunken', width=9)
        self.qty.place(x=320, y=150)


        # address
        Label(self.product, text='Price', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=320, y=200)
        self.price = Entry(self.product, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                           bd=4, relief='sunken', width=10)
        self.price.place(x=320, y=250)

        Label(self.product, text='Date', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=320, y=300)
        self.date = Entry(self.product, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                           bd=4, relief='sunken', width=10)
        self.date.place(x=320, y=350)

        # baner

        self.banner_img = Image.open('images/female-nurse.jpg')
        self.res = self.banner_img.resize((650, 600), Image.ANTIALIAS)
        self.baner = ImageTk.PhotoImage(self.res)
        Label(self.product, image=self.baner, bg='white', bd=0).place(x=980, y=120)

        # shifts

        # Buttons
        self.add_btn=Button(self.product,text='Add',bg='#019',fg='white',
                            bd=7,relief='ridge',font=('Verdana',18,'bold'),
                           )
        self.add_btn.place(x=190,y=420)

        self.update_btn = Button(self.product, text='Update', bg='#019', fg='white',
                              bd=7, relief='ridge', font=('Verdana', 18, 'bold')
                                 )
        self.update_btn.place(x=290, y=420)

        self.dele = Button(self.product, text='Delete', bg='#019', fg='white',
                              bd=7, relief='ridge', font=('Verdana', 18, 'bold'))

        self.dele.place(x=445, y=420)

        # self.search = Button(self.product, text='Delete', bg='#019', fg='white',
        #                    bd=7, relief='ridge', font=('Verdana', 18, 'bold'), command=self.Delete)
        #
        # self.search.place(x=445, y=420)

        self.search = Entry(self.product, bg='#fff', fg='#019', font=('Verdana', 15, 'bold'),
                          bd=4, relief='ridge', width=15)
        self.search.place(x=1290, y=15)
        self.product.bind('<Control-f>',self.find)
        self.search.bind('<Button-1>',self._find_)
        self.search.bind('<Return>',self._Return_)
        self.takID.focus()

        self.search.insert(0,'TakesID')
        self.search.config(state=DISABLED)




        # tree-view table


        self.frame_tree=Frame(self.product,bg='white',width=1090,bd=3,relief='groove')
        self.frame_tree.place(x=5,y=600)
        scrollbar=Scrollbar(self.frame_tree,orient=VERTICAL)
        scrollbar.pack(side=RIGHT,fill=Y)
        self.tree=ttk.Treeview(self.frame_tree,yscrollcommand=scrollbar.set,
                               columns=('TakesID','MedID','PatientID','QTTY','Price','Date'))
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
        self.tree.column('TakesID',width=100)
        self.tree.column('MedID',width=240)
        self.tree.column('PatientID',width=210,anchor=CENTER)
        self.tree.column('QTTY',width=320,anchor=CENTER)
        self.tree.column('Price',width=240,anchor=CENTER)
        self.tree.column('Date',width=400,anchor=CENTER)


        self.tree.heading('TakesID',text='TakesID')
        self.tree.heading('MedID',text='MedID')
        self.tree.heading('PatientID',text='PatientID')
        self.tree.heading('QTTY',text='QTTY')
        self.tree.heading('Price',text='Price')
        self.tree.heading('Date',text='Date')



        mainloop()
    #
    # def add(self):
    #     self.tree.insert('',END,values=(self.drid.get(),self.drname.get(),self.age.get(),self.mobile.get(),self.email.get(),self.gender_var.get(),self.address.get(),self.specialist.get(),self.salary.get(),self.shift_var.get(),self.dep_var.get()))


    def find(self,e):
        self.search.config(state=NORMAL)
        self.search.delete(0,END)
        self.search.focus()

    def _find_(self, e):
        self.search.config(state=NORMAL)
        self.search.delete(0, END)
        self.search.focus()

    def _Return_(self, e):

        messagebox.showinfo('INFO', f'QTY {self.qty.get()}', parent=self.product)

    def clock_(self):
        import time
        self.hour=time.strftime('%I')
        self.minutes=time.strftime('%M')
        self.secons=time.strftime('%S')
        self.satte=time.strftime('%p')
        self.clock.config(text=f'Time: {self.hour}:{self.minutes}:{self.secons} {self.satte}')
        self.clock.after(1000,self.clock_)
