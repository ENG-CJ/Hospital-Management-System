from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox,ttk




class NURSES:
    def products(self):
        self.Nurses=Tk()
        # self.product.geometry('1100x740+30+20')
        # self.Nurses.state('zoomed')
        self.Nurses.geometry('1500x500')
        self.Nurses.focus_force()
        self.Nurses.title('Nursess')
        self.Nurses.resizable(0,0)
        self.Nurses.config(bg='#fff')
        # self.Nurses.iconbitmap('logo.ico')




        # Nurses
        Label(self.Nurses,text='DARUL-SHIFA HOSPITAL | MANAGE NURSES',bg='blue',fg='white',bd=3,relief='flat',
              font=('Verdana',20,'bold'),height=2).pack(fill=X)


        Label(self.Nurses,text='TakID',bg='white',fg='#6c63ff',font=('Verdana',19,'bold')
              ).place(x=10,y=100)
        self.takID=Entry(self.Nurses,bg='#c0b6ff',fg='black',font=('Verdana',15,'bold'),
                         bd=4,relief='sunken',width=10)
        self.takID.place(x=10,y=150)

        # Nurses name
        # 10 250/
        Label(self.Nurses,text='PatienID',bg='white',fg='#6c63ff',font=('Verdana',19,'bold')
              ).place(x=10,y=200)
        self.pat_id_lists = [1, 2, 3]
        self.pat_id_var = StringVar()
        self.pat_lists = ttk.Combobox(self.Nurses, value=self.pat_id_lists, textvariable=self.pat_id_var,
                                      font=('Verdana', 15, 'bold'), justify=CENTER)
        self.pat_lists.place(x=10, y=250, width=130)
        self.pat_id_var.set('Select')
        self.pat_lists['state']='readonly'


        # price

        Label(self.Nurses,text='MedicineID',bg='white',fg='#6c63ff',font=('Verdana',19,'bold')
              ).place(x=10,y=300)
        self.med_id_lists = [1, 2, 3]
        self.med_id_var = StringVar()
        self.med_id_var.set('Select')
        self.med_lists = ttk.Combobox(self.Nurses, value=self.med_id_lists, textvariable=self.med_id_var,
                                      font=('Verdana', 15, 'bold'), justify=CENTER)
        self.med_lists.place(x=10, y=350, width=130)
        self.med_lists['state']='readonly'
        # quantity
        Label(self.Nurses, text='QTTY', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=320, y=100)
        self.QTTY = Entry(self.Nurses, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                           bd=4, relief='sunken', width=10)
        self.QTTY.place(x=320, y=150)


        # address
        Label(self.Nurses, text='Date', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=320, y=300)
        self.date = Entry(self.Nurses, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                           bd=4, relief='sunken', width=10)
        self.date.place(x=320, y=350)

        # baner

        # self.banner_img = Image.open('images/female-nurse.jpg')
        # self.res = self.banner_img.resize((650, 600), Image.ANTIALIAS)
        # self.baner = ImageTk.PhotoImage(self.res)
        # Label(self.Nurses, image=self.baner, bg='white', bd=0).place(x=980, y=120)




        #Date
        Label(self.Nurses, text='Price', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=320, y=200)
        self.Price_ = Entry(self.Nurses, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                           bd=4, relief='sunken', width=10)
        self.Price_.place(x=320, y=250)




        # Buttons
        self.add_btn=Button(self.Nurses,text='Add',bg='#019',fg='white',
                            bd=7,relief='flat',font=('Verdana',18,'bold'),
                            command=self.add)
        self.add_btn.place(x=800,y=420,width=120)

        self.update_btn = Button(self.Nurses, text='Update', bg='#019', fg='white',
                              bd=7, relief='flat', font=('Verdana', 18, 'bold')
                                 )
        self.update_btn.place(x=950, y=420)

        self.dele = Button(self.Nurses, text='Delete', bg='#019', fg='white',
                              bd=7, relief='flat', font=('Verdana', 18, 'bold'))

        self.dele.place(x=1100, y=420)

        # self.search = Button(self.Nurses, text='Delete', bg='#019', fg='white',
        #                    bd=7, relief='ridge', font=('Verdana', 18, 'bold'), command=self.Delete)
        #
        # self.search.place(x=445, y=420)

        self.search = Entry(self.Nurses, bg='#fff', fg='#019', font=('Verdana', 15, 'bold'),
                          bd=4, relief='ridge', width=15)
        self.search.place(x=1240, y=15)
        # self.Nurses.bind('<Control-f>',self.find)
        # self.Nurses.bind('<Button-1>',self._find_)
        # self.Nurses.bind('<Return>',self._Return_)
        # self.drid.focus()

        self.search.insert(0,'Search NurseID')
        self.search.config(state=DISABLED)




        # tree-view table


        self.frame_tree=Frame(self.Nurses,bg='white',width=1090,bd=3,relief='groove')
        self.frame_tree.place(x=500,y=140)
        scrollbar=Scrollbar(self.frame_tree,orient=VERTICAL)
        scrollbar.pack(side=RIGHT,fill=Y)
        self.tree_taking=ttk.Treeview(self.frame_tree,yscrollcommand=scrollbar.set,
                               columns=('TakMedicineID','PatientID','MedicineID','QTTY','Price','Date'))
        self.tree_taking.pack(fill=BOTH,expand=True)
        # self.tree.bind('<ButtonRelease-1>',self.select)
        scrollbar.config(command=self.tree_taking.yview)
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("Treeview", background='#f4f4f4', foreground='#fff', font=('Verdana', 10),
                        fieldbackground='#f4f4f4')

        self.style2 = ttk.Style()
        self.style2.theme_use('clam')
        self.style2.configure("Combobox", background='red', foreground='#fff', font=('Verdana', 10),
                             fieldbackground='#f4f4f4')
        self.tree_taking.column('#0',width=0,stretch=NO)
        self.tree_taking.column('TakMedicineID',width=80)
        self.tree_taking.column('PatientID',width=220)
        self.tree_taking.column('MedicineID',width=90,anchor=CENTER)
        self.tree_taking.column('QTTY',width=200,anchor=CENTER)
        self.tree_taking.column('Price',width=240,anchor=CENTER)
        self.tree_taking.column('Date',width=120,anchor=CENTER)

        self.tree_taking.heading('TakMedicineID',text='TakMedicineID')
        self.tree_taking.heading('PatientID',text='PatientID')
        self.tree_taking.heading('MedicineID',text='MedicineID')
        self.tree_taking.heading('QTTY',text='QTTY')
        self.tree_taking.heading('Price',text='Price')
        self.tree_taking.heading('Date',text='Date')



        mainloop()
    #
    def add(self):
        pass
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
        messagebox.showinfo('INFO', f'You Write {self.search.get()}', parent=self.Nurses)

    def clock_(self):
        import time
        self.hour=time.strftime('%I')
        self.minutes=time.strftime('%M')
        self.secons=time.strftime('%S')
        self.satte=time.strftime('%p')
        self.clock.config(text=f'Time: {self.hour}:{self.minutes}:{self.secons} {self.satte}')
        self.clock.after(1000,self.clock_)

obj=NURSES()
obj.products()