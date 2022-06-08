from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox,ttk




class NURSES:
    def products(self):
        self.Nurses=Tk()
        # self.product.geometry('1100x740+30+20')
        self.Nurses.state('zoomed')
        self.Nurses.focus_force()
        self.Nurses.title('Nursess')
        self.Nurses.resizable(0,0)
        self.Nurses.config(bg='#fff')
        # self.Nurses.iconbitmap('logo.ico')




        # Nurses
        Label(self.Nurses,text='DARUL-SHIFA HOSPITAL | MANAGE NURSES',bg='#127',fg='white',bd=3,relief='flat',
              font=('Verdana',20,'bold'),height=2).pack(fill=X)
        self.clock= Label(self.Nurses,bg='#127',fg='white',bd=3,relief='flat',
              font=('Verdana',18,'bold'),height=2)
        self.clock.place(x=0,y=0)
        self.clock_()

        # image
        self.log = Image.open('icons/lg.png')
        self.resizing = self.log.resize((60, 60), Image.ANTIALIAS)
        self.new_icon = ImageTk.PhotoImage(self.resizing)
        self.lb = Label(self.Nurses,bg='#127', image=self.new_icon, bd=0)
        self.lb.place(x=330, y=5)

        Label(self.Nurses,text='IPID',bg='white',fg='#6c63ff',font=('Verdana',19,'bold')
              ).place(x=10,y=100)
        self.ipID=Entry(self.Nurses,bg='#c0b6ff',fg='black',font=('Verdana',15,'bold'),
                         bd=4,relief='sunken',width=10)
        self.ipID.place(x=10,y=150)

        # Nurses name
        self.pat_list_p = [1, 2]
        self.pat_var_p = StringVar()
        self.pat_var_p.set('Select')
        Label(self.Nurses,text='PatientID',bg='white',fg='#6c63ff',font=('Verdana',19,'bold')
              ).place(x=10,y=200)
        self.pat_id = ttk.Combobox(self.Nurses,textvariable=self.pat_var_p,value=self.pat_list_p,
                                   font=('Verdana', 15, 'bold'), justify=CENTER)
        self.pat_id.place(x=10, y=250, width=130)
        self.pat_id['state']='readonly'


        # price
        self.dag_list = [1, 2]
        self.diag_var = StringVar()
        self.diag_var.set('Select')
        Label(self.Nurses,text='DiagnoseID',bg='white',fg='#6c63ff',font=('Verdana',19,'bold')
              ).place(x=10,y=300)
        self.diagid = ttk.Combobox(self.Nurses,textvariable=self.diag_var,value=self.dag_list,
                                   font=('Verdana', 15, 'bold'), justify=CENTER)
        self.diagid.place(x=10, y=350, width=130)
        self.diagid['state']='readonly'

        # quantitys
        self.tak_list=[1,2]
        self.tak_var=StringVar()
        self.tak_var.set('Select')
        Label(self.Nurses, text='TakeMedID', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=320, y=100)
        self.Takid = ttk.Combobox(self.Nurses,textvariable=self.tak_var,value=self.tak_list,
                                   font=('Verdana', 15, 'bold'), justify=CENTER)
        self.Takid.place(x=320, y=150, width=130)
        self.Takid['state']='readonly'





        # baner

        self.banner_img = Image.open('images/female-nurse.jpg')
        self.res = self.banner_img.resize((650, 600), Image.ANTIALIAS)
        self.baner = ImageTk.PhotoImage(self.res)
        Label(self.Nurses, image=self.baner, bg='white', bd=0).place(x=980, y=120)

        # shifts
        Label(self.Nurses, text='Date Out', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=550, y=100)
        self.date_admin = Entry(self.Nurses, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                          bd=4, relief='sunken', width=10)
        self.date_admin.place(x=550, y=150)


        # self.shifts.config(background='red')



        #Date
        Label(self.Nurses, text='RoomID', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=320, y=200)
        self.r_list=[1,2]
        self.r_var=StringVar()
        self.r_var.set('Select')
        self.rid = ttk.Combobox(self.Nurses,textvariable=self.r_var,value=self.r_list,
                                font=('Verdana', 15, 'bold'), justify=CENTER)
        self.rid.place(x=320, y=250, width=130)
        self.rid['state']='readonly'

        # Departs
        Label(self.Nurses, text='No-OfDays', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=550, y=200)
        self.nodays = Entry(self.Nurses, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                              bd=4, relief='sunken', width=12)
        self.nodays.place(x=550, y=250)



        # sALARAY
        # Label(self.Nurses, text='Salary', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
        #       ).place(x=650, y=300)
        # self.salary = Entry(self.Nurses, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
        #                         bd=4, relief='sunken', width=10)
        # self.salary.place(x=650, y=350)

        Label(self.Nurses, text='Date Admis', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=320, y=300)
        self.date_admin = Entry(self.Nurses, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                            bd=4, relief='sunken', width=13)
        self.date_admin.place(x=320, y=350)


        # Buttons
        self.add_btn=Button(self.Nurses,text='Add',bg='#019',fg='white',
                            bd=7,relief='sunken',font=('Verdana',18,'bold'),
                            command=self.add)
        self.add_btn.place(x=190,y=420)

        self.update_btn = Button(self.Nurses, text='Update', bg='#019', fg='white',
                              bd=7, relief='sunken', font=('Verdana', 18, 'bold')
                                 )
        self.update_btn.place(x=290, y=420)

        self.dele = Button(self.Nurses, text='Delete', bg='#019', fg='white',
                              bd=7, relief='sunken', font=('Verdana', 18, 'bold'))

        self.dele.place(x=445, y=420)

        # self.search = Button(self.Nurses, text='Delete', bg='#019', fg='white',
        #                    bd=7, relief='ridge', font=('Verdana', 18, 'bold'), command=self.Delete)
        #
        # self.search.place(x=445, y=420)

        self.search = Entry(self.Nurses, bg='#fff', fg='#019', font=('Verdana', 15, 'bold'),
                          bd=4, relief='ridge', width=15)
        self.search.place(x=1290, y=15)
        # self.Nurses.bind('<Control-f>',self.find)
        # self.Nurses.bind('<Button-1>',self._find_)
        # self.Nurses.bind('<Return>',self._Return_)
        # self.drid.focus()

        self.search.insert(0,'Search')
        self.search.config(state=DISABLED)




        # tree-view table


        self.frame_tree=Frame(self.Nurses,bg='white',width=1090,bd=3,relief='groove')
        self.frame_tree.place(x=5,y=600)
        scrollbar=Scrollbar(self.frame_tree,orient=VERTICAL)
        scrollbar.pack(side=RIGHT,fill=Y)
        self.tree_ip=ttk.Treeview(self.frame_tree,yscrollcommand=scrollbar.set,
                               columns=('IPID','PatientID','DiagnoseID','TakmedID','RoomID','DateAdmis','DateOut','NoOfDays'))
        self.tree_ip.pack(fill=BOTH,expand=True)
        # self.tree.bind('<ButtonRelease-1>',self.select)
        scrollbar.config(command=self.tree_ip.yview)
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("Treeview", background='#f4f4f4', foreground='#fff', font=('Verdana', 10),
                        fieldbackground='#f4f4f4')

        self.style2 = ttk.Style()
        self.style2.theme_use('clam')
        self.style2.configure("Combobox", background='red', foreground='#fff', font=('Verdana', 10),
                             fieldbackground='#f4f4f4')
        self.tree_ip.column('#0',width=0,stretch=NO)
        self.tree_ip.column('IPID',width=80)
        self.tree_ip.column('PatientID',width=220)
        self.tree_ip.column('DiagnoseID',width=90,anchor=CENTER)
        self.tree_ip.column('TakmedID',width=200,anchor=CENTER)
        self.tree_ip.column('RoomID',width=240,anchor=CENTER)
        self.tree_ip.column('DateAdmis',width=220,anchor=CENTER)
        self.tree_ip.column('DateOut',width=230,anchor=CENTER)
        self.tree_ip.column('NoOfDays',width=210,anchor=CENTER)


        self.tree_ip.heading('IPID',text='IPID')
        self.tree_ip.heading('PatientID',text='PatientID')
        self.tree_ip.heading('DiagnoseID',text='DiagnoseID')
        self.tree_ip.heading('TakmedID',text='TakmedID')
        self.tree_ip.heading('RoomID',text='RoomID')
        self.tree_ip.heading('DateAdmis',text='DateAdmis')
        self.tree_ip.heading('DateOut',text='DateOut')
        self.tree_ip.heading('NoOfDays',text='NoOfDays')



        mainloop()

    def add(self):
        pass
       # / self.tree.insert('',END,values=(self.drid.get(),self.drname.get(),self.age.get(),self.mobile.get(),self.email.get(),self.gender_var.get(),self.address.get(),self.specialist.get(),self.salary.get(),self.shift_var.get(),self.dep_var.get()))


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
ob=NURSES()
ob.products()