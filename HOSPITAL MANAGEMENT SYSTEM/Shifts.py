from tkinter import *
from  tkinter import  messagebox,ttk
from  PIL import ImageTk,Image
# import HOSPITAL_SYSTEM




class SHIFTS:
    def __shifts__(self):
        self.screen=Tk()
        self.screen.focus_force()
        self.screen.geometry('410x480')
        self.screen.resizable(0,0)
        self.screen.config(bg='white')
        self.screen.title('Shifts')
        #LABELS
        Label(self.screen,text='Manage Shifts',bg='#00008b',fg='white',
              font=('Verdana',18,'bold')).pack(fill=X)

        Label(self.screen,text='ShiftID',bg='white',fg='black',font=('Verdana',16,'bold')).place(x=20,y=60)
        global depID,depName
        self.shiftID=Entry(self.screen,font=('Verdana',16,'bold'),bg='#f4f4f4',fg='black',
                    bd=3,relief='groove')
        self.shiftID.place(x=20,y=100,width=120)

        Label(self.screen, text='ShiftType', bg='white', fg='black', font=('Verdana', 16, 'bold')).place(x=220, y=60)
        self.shiftType = Entry(self.screen, font=('Verdana', 16, 'bold'), bg='#f4f4f4', fg='black',
                      bd=3, relief='groove')
        self.shiftType.place(x=220, y=100, width=150)





        self.addBtn=Button(self.screen,text='Add',bg='#189',fg='white',font=('Verdana', 16, 'bold'),
                      bd=3,relief='sunken')
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

        self.data=[
            ['Geedi','Mohamed'],
            ['Geedi','Mohamed'],
            ['Geedi','Mohamed'],
            ['Geedi','Mohamed'],
            ['Geedi','Mohamed'],
            ['Geedi','Mohamed'],
            ['Geedi','Mohamed'],
            ['Geedi','Mohamed'],
            ['Geedi','Mohamed'],
            ['Geedi','Mohamed'],
            ['Geedi','Mohamed'],
            ['Geedi','Mohamed'],
            ['Geedi','Mohamed'],
            ['JHSJ','Mohamed'],
            ['CHIOL','Mohamed'],
            ['FREE','Mohamed'],
            ['FARA','Mohamed'],
            ['MOHA','Mohamed'],
        ]
        self.style.theme_use('clam')
        self.style.configure("Treeview", background='#f4f4f4', foreground='#fff', font=('Verdana', 10),
                        fieldbackground='#f4f4f4')
        self.data_frame=Frame(self.screen,bg='white',bd=3,relief='ridge',width=900,heigh=100)
        self.data_frame.place(x=0,y=230)

        self.scrollbar=Scrollbar(self.data_frame,orient=VERTICAL)

        global  tree_data
        self.tree_data=ttk.Treeview(self.data_frame,columns=("shiftID",'shiftType'),yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.tree_data.yview)
        self.scrollbar.pack(fill=Y,side=RIGHT)
        self.tree_data.column('#0',width=0,stretch=NO)
        self.tree_data.column("shiftID",width=120)
        self.tree_data.column("shiftType",width=266)

        self.tree_data.heading("shiftID",text='ShiftID')
        self.tree_data.heading("shiftType",text='ShiftType')

        self.tree_data.pack(fill=BOTH,expand=1)
        for row in self.data:
            self.tree_data.insert('',END,values=row)

        # TREE-END========================
        # self.show()/

        mainloop()
    #
    # def add_(self):
    #     tree_data.insert('', END, values=(self.depID.get(), self.depName.get()))
    #
    # def delete(self):
    #     self.depID.delete(0,END)
    #     self.depName.delete(0,END)
    #     item=self.tree_data.focus()
    #     select=self.tree_data.item(item,'values')
    #     self.depID.insert(0,select[0])
    #     self.depName.insert(0,select[1])



obj=SHIFTS()
obj.__shifts__()




