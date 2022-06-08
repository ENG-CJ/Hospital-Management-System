from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox,ttk




class NURSES:
    def products(self):
        self.Nurses=Tk()
        # self.product.geometry('1100x740+30+20')
        # self.Nurses.state('zoomed')
        self.Nurses.geometry('1280x500')
        self.Nurses.focus_force()
        self.Nurses.title('Nursess')
        self.Nurses.resizable(0,0)
        self.Nurses.config(bg='#fff')
        # self.Nurses.iconbitmap('logo.ico')




        # Nurses
        Label(self.Nurses,text='DARUL-SHIFA HOSPITAL | MANAGE NURSES',bg='#657',fg='white',bd=3,relief='flat',
              font=('Verdana',20,'bold'),height=2).pack(fill=X)


        Label(self.Nurses,text='DiagnoseID',bg='white',fg='#6c63ff',font=('Verdana',19,'bold')
              ).place(x=10,y=100)
        self.diagID=Entry(self.Nurses,bg='#c0b6ff',fg='black',font=('Verdana',15,'bold'),
                         bd=4,relief='sunken',width=10)
        self.diagID.place(x=10,y=150)

        # Nurses name
        # 10 250/
        Label(self.Nurses,text='PatienID',bg='white',fg='#6c63ff',font=('Verdana',19,'bold')
              ).place(x=10,y=200)
        self.pat_id_list = [1, 2, 3]
        self.pat_id_var_diag = StringVar()
        self.pat_list = ttk.Combobox(self.Nurses, value=self.pat_id_list, textvariable=self.pat_id_var_diag,
                                      font=('Verdana', 15, 'bold'), justify=CENTER)
        self.pat_list.place(x=10, y=250, width=130)
        self.pat_id_var_diag.set('Select')
        self.pat_list['state']='readonly'


        # price

        Label(self.Nurses,text='Test-Type',bg='white',fg='#6c63ff',font=('Verdana',19,'bold')
              ).place(x=10,y=300)
        self.test_type = Entry(self.Nurses, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                          bd=4, relief='sunken', width=10)
        self.test_type.place(x=10, y=350)

        # quantity
        Label(self.Nurses, text='Result', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=10, y=390)
        self.result = Entry(self.Nurses, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                           bd=4, relief='sunken', width=10)
        self.result.place(x=10, y=440)


        # Buttons
        self.add_btn=Button(self.Nurses,text='Add',bg='#019',fg='white',
                            bd=7,relief='flat',font=('Verdana',18,'bold'),
                            command=self.add)
        self.add_btn.place(x=400,y=430,width=120)

        self.update_btn = Button(self.Nurses, text='Update', bg='#019', fg='white',
                              bd=7, relief='flat', font=('Verdana', 18, 'bold')
                                 )
        self.update_btn.place(x=540, y=430)

        self.dele = Button(self.Nurses, text='Delete', bg='#019', fg='white',
                              bd=7, relief='flat', font=('Verdana', 18, 'bold'))

        self.dele.place(x=700, y=430)

        # self.search = Button(self.Nurses, text='Delete', bg='#019', fg='white',
        #                    bd=7, relief='ridge', font=('Verdana', 18, 'bold'), command=self.Delete)
        #
        # self.search.place(x=445, y=420)

        self.search = Entry(self.Nurses, bg='#fff', fg='#019', font=('Verdana', 15, 'bold'),
                          bd=4, relief='ridge', width=14)
        self.search.place(x=1060, y=15)
        # self.Nurses.bind('<Control-f>',self.find)
        # self.Nurses.bind('<Button-1>',self._find_)
        # self.Nurses.bind('<Return>',self._Return_)
        # self.drid.focus()

        self.search.insert(0,'Search')
        self.search.config(state=DISABLED)




        # tree-view table


        self.frame_tree=Frame(self.Nurses,bg='white',width=1090,bd=3,relief='groove')
        self.frame_tree.place(x=250,y=120,height=300)
        scrollbar=Scrollbar(self.frame_tree,orient=VERTICAL)
        scrollbar.pack(side=RIGHT,fill=Y)
        self.tree_lab=ttk.Treeview(self.frame_tree,yscrollcommand=scrollbar.set,
                               columns=('DiagID','PatientID','Test-type','Result'))
        self.tree_lab.pack(fill=BOTH,expand=True)
        # self.tree.bind('<ButtonRelease-1>',self.select)
        scrollbar.config(command=self.tree_lab.yview)
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("Treeview", background='#f4f4f4', foreground='#fff', font=('Verdana', 10),
                        fieldbackground='#f4f4f4')

        self.style2 = ttk.Style()
        self.style2.theme_use('clam')
        self.style2.configure("Combobox", background='red', foreground='#fff', font=('Verdana', 10),
                             fieldbackground='#f4f4f4')
        self.tree_lab.column('#0',width=0,stretch=NO)
        self.tree_lab.column('DiagID',width=280)
        self.tree_lab.column('PatientID',width=320)
        self.tree_lab.column('Test-type',width=190,anchor=CENTER)
        self.tree_lab.column('Result',width=120,anchor=CENTER)


        self.tree_lab.heading('DiagID',text='DiagID')
        self.tree_lab.heading('PatientID',text='PatientID')
        self.tree_lab.heading('Test-type',text='Test-type')
        self.tree_lab.heading('Result',text='Result')




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

    # def clock_(self):
    #     import time
    #     self.hour=time.strftime('%I')
    #     self.minutes=time.strftime('%M')
    #     self.secons=time.strftime('%S')
    #     self.satte=time.strftime('%p')
    #     self.clock.config(text=f'Time: {self.hour}:{self.minutes}:{self.secons} {self.satte}')
    #     self.clock.after(1000,self.clock_)

obj=NURSES()
obj.products()