from tkinter import *
from  tkinter import  messagebox,ttk
from  PIL import ImageTk,Image
import HOSPITAL_SYSTEM
import  pyodbc

# conn = pyodbc.connect(
#     "Driver={SQL Server Native Client 11.0};"
#     "Server= DESKTOP-N9PT8FH/SQLEXPRESS;"
#     "Database=hospital;"
#     "Trusted_Connection=yes;"
# )

class DEPS:
    def dep(self):
        self.screen=Toplevel()
        self.screen.focus_force()
        self.screen.geometry('500x470')
        self.screen.resizable(0,0)
        self.screen.config(bg='white')
        self.screen.title('Departments')
        #LABELS
        Label(self.screen,text='Manage Departments',bg='#00008b',fg='white',
              font=('Verdana',18,'bold')).pack(fill=X)

        Label(self.screen,text='DepID',bg='white',fg='black',font=('Verdana',16,'bold')).place(x=20,y=60)
        # global depID,depName
        self.depID=Entry(self.screen,font=('Verdana',16,'bold'),bg='#f4f4f4',fg='black',
                    bd=3,relief='groove')
        self.depID.place(x=20,y=100,width=120)

        Label(self.screen, text='DepName', bg='white', fg='black', font=('Verdana', 16, 'bold')).place(x=220, y=60)
        self.depName = Entry(self.screen, font=('Verdana', 16, 'bold'), bg='#f4f4f4', fg='black',
                      bd=3, relief='groove')
        self.depName.place(x=220, y=100, width=150)

        self.addBtn=Button(self.screen,text='Add',bg='#189',fg='white',font=('Verdana', 16, 'bold'),
                      bd=3,relief='sunken',command=self.add_)
        self.addBtn.place(x=20,y=160)

        self.update=Button(self.screen,text='Update',bg='#189',fg='white',font=('Verdana', 16, 'bold'),
                      bd=3,relief='sunken')
        self.update.place(x=100,y=160)

        self.Delete=Button(self.screen,text='Delete',bg='#189',fg='white',font=('Verdana', 16, 'bold'),
                      bd=3,relief='sunken')
        self.Delete.place(x=230,y=160)
        # ===========================END LABLS==============

        # TREEVIEW STYLES
        self.style=ttk.Style()
        # style.configure("Treeview")


        self.style.theme_use('clam')
        self.style.configure("Treeview", background='#f4f4f4', foreground='#fff', font=('Verdana', 10),
                        fieldbackground='#f4f4f4')
        self.data_frame=Frame(self.screen,bg='white',bd=3,relief='ridge',width=900,heigh=100)
        self.data_frame.place(x=40,y=230)

        self.scrollbar=Scrollbar(self.data_frame,orient=VERTICAL)

        # global  tree_data
        self.tree_data=ttk.Treeview(self.data_frame,columns=("DepartID",'DepartName'),yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.tree_data.yview)
        self.scrollbar.pack(fill=Y,side=RIGHT)
        self.tree_data.column('#0',width=0,stretch=NO)
        self.tree_data.column("DepartID")
        self.tree_data.column("DepartName")
        self.tree_data.heading("DepartID",text='DepartID')
        self.tree_data.heading("DepartName",text='Depart-Name')
        self.tree_data.pack(fill=BOTH,expand=1)

        self._fetch_()

        # print(pyodbc.drivers())
        mainloop()

    def add_(self):
        hos=HOSPITAL_SYSTEM.DARUL_SHIFA_HOSPITAL()
        if self.depID.get()=='' or self.depName.get()=='':
            messagebox.showerror('DaruShifa_Hospital','All Fields Are required')
        else:
            try:
                conn = pyodbc.connect(
                    "Driver={SQL Server Native Client 11.0};"
                    "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
                    "Database=DaruShifa_Hospital;"
                    "Trusted_Connection=yes;"
                )
                cursor = conn.cursor()
                cursor.execute('INSERT INTO departments VALUES(?,?)',(self.depID.get(),self.depName.get()))
                conn.commit()
                messagebox.showinfo('TEST',f'Successful Added\nDepartment [{self.depName.get()}]')
                self.tree_data.delete(*self.tree_data.get_children())
                self._fetch_()
                hos.show_counts()
                # self.test='HELLO'
            except Exception as err:
                messagebox.showerror('Error Occurred',f'Error Occurred Due\n{err.args}')



    def _fetch_(self):
        conn=pyodbc.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
            "Database=DaruShifa_Hospital;"
            "Trusted_Connection=yes;"
        )
        cursor=conn.cursor()
        cursor.execute('select *from departments')
        rows=cursor.fetchall()
        for row in rows:
            self.tree_data.insert('',END,values=(
                row[0],row[1]
            ))


# ob=DEPS()
# ob.dep()