# ========IMPORTS==============
from tkinter import *
from tkinter import  ttk
from  tkinter import messagebox
import  pyodbc
import time
import webbrowser
from PIL import  ImageTk,Image
import Developers as Dev
from twilio.rest import Client
import  random
import Departs
import  Doctor
import nurses
import Patients
import  Pharamcist
import Medicines
import Rooms
# import Sales
import Purchase
import Bloods
import Reports
# import


#=======END IMPORTS=================
# otp_random=random.randint(1000,9999)

# tokens Ports
account_sid = "AC83ae619de1e047eb9d5332549bf9d389"
author_token = "009097ff3e88f8139c08a47073d278ee"
client = Client(account_sid, author_token)

#==========================
#========== a===============
#========Class=============
class DARUL_SHIFA_HOSPITAL:
    def login_page(self):
        self.log=Tk()
        self.log.iconbitmap('icons/Hospital-icon.ico')
        self.log.state('zoomed')
        self.log.config(bg='#434fff')
        self.log.resizable(0, 0)
        self.log.title('login DARUL-SHIFA HOSPITAL SYSTEM')
        # self.log.focus()
        Label(self.log,text='DARUL-SHIFA HOSPITAL SYS',bg='#6c3fff',height=2,fg='#fff',font=('verdana',28,'bold')).pack(fill=BOTH)
        self.frame_login=Frame(self.log,bg='#fff',width=1300,height=620,bd=1,relief="sunken")
        self.frame_login.place(x=110,y=100)

        self.background=Image.open('images/bg-2.png')
        self.resize_img_bg=self.background.resize((950,690),Image.ANTIALIAS)
        self.image_bg=ImageTk.PhotoImage(self.resize_img_bg)
        Label(self.frame_login,image=self.image_bg,bd=0,bg='#fff').place(x=0,y=10)

        Label(self.frame_login, text='LOGIN', bg='#fff', fg='#6c3fff', font=('verdana', 50, 'bold')).place(x=700, y=70)
        Label(self.log, text='ONLY ADMINS CAN USE THIS', bg='#fff', fg='red', font=('Verdana', 9, 'bold')).place(
            x=830,
            y=245)
        #
        # # Options
        #
        self.admins = ['Abdirahman Haaji', 'Mohamed Ali', 'Qadra Mohamud', 'Abdullahi Mascud', 'Mascuud Abdirahman']
        self.admin_str = StringVar()
        self.admin_str.set('Select Your Username')
        self.admin_list = ttk.Combobox(self.log, font=('Verdana', 10, 'bold'), textvariable=self.admin_str,
                                       value=self.admins,
                                       justify=CENTER)
        self.admin_list['state'] = 'readonly'
        self.admin_list.bind("<<ComboboxSelected>>", self.active)
        self.admin_list.place(x=835, y=290)
        #
        # # text-box
        Label(self.log, text='Username', bg='#fff', fg='#003e53', font=('Verdana', 16, 'bold'),
              ).place(x=835, y=340)
        self.username = Entry(self.log, bg='white', fg='#34013f', font=('Verdana', 13, 'bold')
                              , bd=5, relief='groove')

        self.username.place(x=835, y=375, height=35)
        #
        Label(self.log, text='OTP Code↴', bg='#fff', fg='#003e35', font=('Verdana', 16, 'bold'),
              ).place(x=835, y=440)
        # # global sepascode
        self.pascode = Entry(self.log, bg='white', fg='blue', font=('Verdana', 13, 'bold')
                             , bd=5, relief='groove', show='')

        self.pascode.place(x=835, y=475, height=35)
        self.login_icon=Image.open('images/login.png')
        self.resize_login=self.login_icon.resize((200,60),Image.ANTIALIAS)
        self.login_btn=ImageTk.PhotoImage(self.resize_login)
        #


        # # login
        self.Login = Button(self.log,image=self.login_btn, bg='#fff',
                            command=self.Login,bd=0,activebackground="#fff",cursor='hand2')
        self.Login.place(x=860, y=540)

        Button(self.log, cursor='hand2', text="↪ Resend OTP?",
               font=('Verdana', 8, 'bold'), bg='#fff', fg='#018', bd=0,
               activebackground='#fff', activeforeground='red',
               command=self._resend_).place(x=980, y=520)

        mainloop()


        #=========================end Login page ==================================

    def _main_Dashboard(self):
            self.root=Toplevel()
            self.root.config(bg='#f4f4f4')
            self.root.state('zoomed')
            self.root.resizable(0,0)
            self.root.title('DARUL-SHIFA HOSPITAL')
            self.root.iconbitmap(r'C:\Users\PC\PycharmProjects\RoomProjects\GUIs Projects\PROJECT\HOSPITAL MANAGEMENT SYSTEM\icons\Hospital-icon.ico')
            #========END SETUP===========

            # ===DASHBOARD INFORMATION======
            Label(self.root,text='DARUL-SHIFA HOSPITAL',bg='#f4f4f4',fg='#513B1C',
                  font=('Festive',30,'bold')).place(x=390,y=10)

            Label(self.root, text='MANAGEMENT SYSTEM', bg='#f4f4f4', fg='#151B54',
                  font=('Festive', 10)).place(x=500, y=55)
            self.clock_lable=Label(self.root,text='',bg='#f4f4f4',fg='#191970'
                                   ,font=('Verdana',20,'bold'))
            self.clock_lable.place(x=1020,y=0)

            self.date_label = Label(self.root, text='', bg='#f4f4f4', fg='#191970'
                                     , font=('Verdana', 16, 'bold'))
            self.date_label.place(x=1025, y=36)
            self._clock_()

            Label(self.root,text='______________________________________________________________________________________________________________________________________________',
                  bg='#f4f4f4',fg='#DCDCDC',font=(10),width=135).place(x=0,y=90)

            self.admin_icon=Image.open('icons/admin.ico')
            self.open=ImageTk.PhotoImage(self.admin_icon)
            self.admin_label=Label(self.root,image=self.open,text='ADMIN DASHBOARD',bg='#f4f4f4',fg='#565051',
                  font=('Verdana',15,'bold'),compound=LEFT)
            self.admin_label.place(x=320,y=130)



            # dr frame
            self.dr_frame=Frame(self.root,cursor='hand2',bg='white',bd=1,relief='flat',width=300,height=130)
            self.dr_frame.place(x=320,y=200)

            self.dr_icon=Image.open('images/dr.png')
            self.res=self.dr_icon.resize((110,110),Image.ANTIALIAS)
            self.new=ImageTk.PhotoImage(self.res)
            self.dr_icon_lbl=Label(self.dr_frame,image=self.new,bg='white',bd=0)
            self.dr_icon_lbl.place(x=1,y=30)
            self.count_dr=Label(self.dr_frame,text='10',bg='white',fg='#191970',font=('Verdana',27,'bold')
                  ,bd=0)
            self.count_dr.place(x=160,y=20)

            self.text_dr=Label(self.dr_frame, text='Doctor', bg='white', fg='red', font=('Verdana', 18, 'bold')
                  , bd=0)
            self.text_dr.place(x=160, y=70)
            self.dr_frame.bind('<Enter>',self._dr_hover)
            self.dr_frame.bind('<Leave>',self._dr_leave_hover)

            # patient frame
            self.p_frame = Frame(self.root,cursor='hand2', bg='white', bd=1, relief='flat', width=300, height=130)
            self.p_frame.place(x=700, y=200)
            self.p_icon_=Image.open('images/patient.png')
            self.res1_=self.p_icon_.resize((110,110),Image.ANTIALIAS)
            self.new_icon_p=ImageTk.PhotoImage(self.res1_)
            self.p_icon_lbl=Label(self.p_frame,image=self.new_icon_p,bg='white',bd=0)
            self.p_icon_lbl.place(x=0,y=30)
            self.count_p=Label(self.p_frame, text='10', bg='white', fg='#191970', font=('Verdana', 27, 'bold')
                  , bd=0)
            self.count_p.place(x=160, y=20)
            self.text_p=Label(self.p_frame, text='Patient', bg='white', fg='red', font=('Verdana', 18, 'bold')
                  , bd=0)
            self.text_p.place(x=160, y=70)
            self.p_frame.bind('<Enter>', self._patient_hover_)
            self.p_frame.bind('<Leave>', self._patient_leave_hover_)
            # nurse frame

            self.nurse_frame = Frame(self.root, cursor='hand2',bg='white', bd=1, relief='flat', width=300, height=130)
            self.nurse_frame.place(x=1080, y=200)
            self.n_icon = Image.open('images/Nurse.png')
            self.n_resize = self.n_icon.resize((110, 110), Image.ANTIALIAS)
            self.new_nurse = ImageTk.PhotoImage(self.n_resize)
            self.nurse_icon=Label(self.nurse_frame, image=self.new_nurse, bg='white', bd=0)
            self.nurse_icon.place(x=0, y=30)
            self.count_nurse=Label(self.nurse_frame, text='5', bg='white', fg='#191970', font=('Verdana', 27, 'bold')
                  , bd=0)
            self.count_nurse.place(x=160, y=20)
            self.text_nurse=Label(self.nurse_frame, text='Nurse', bg='white', fg='red', font=('Verdana', 18, 'bold')
                  , bd=0)
            self.text_nurse.place(x=160, y=70)

            self.nurse_frame.bind('<Enter>', self._nurse_hover_)
            self.nurse_frame.bind('<Leave>', self._nurse_leave_hover_)
            # information about pharmacist

            # pharmacist
            self.pharma_frame = Frame(self.root,cursor='hand2', bg='white', bd=1, relief='flat', width=300, height=130)
            self.pharma_frame.place(x=320, y=360)
            self.pha_icon = Image.open('images/Pharmacy (2).png')
            self.pha_res = self.pha_icon.resize((110, 110), Image.ANTIALIAS)
            self.new_pha = ImageTk.PhotoImage(self.pha_res)
            self.pharma_icon_lbl=Label(self.pharma_frame, image=self.new_pha, bg='white', bd=0)
            self.pharma_icon_lbl.place(x=0, y=30)
            self.count_pharma=Label(self.pharma_frame, text='9', bg='white', fg='#191970', font=('Verdana', 27, 'bold')
                  , bd=0)
            self.count_pharma.place(x=140, y=20)
            self.text_pharma=Label(self.pharma_frame, text='Pharmacist', bg='white', fg='red', font=('Verdana', 18, 'bold')
                  , bd=0)
            self.text_pharma.place(x=140, y=70)
            self.pharma_frame.bind('<Enter>', self._pharma_hover_)
            self.pharma_frame.bind('<Leave>', self._leave_pharma_hover)



            # medicals
            self.med_frame = Frame(self.root, bg='white', cursor='hand2',bd=1, relief='flat', width=300, height=130)
            self.med_frame.place(x=700, y=360)
            self.med_icon = Image.open('images/medicine.png')
            self.med_res = self.med_icon.resize((120, 100), Image.ANTIALIAS)
            self.new_med = ImageTk.PhotoImage(self.med_res)
            self.med_icon_lbl=Label(self.med_frame, image=self.new_med, bg='white', bd=0)
            self.med_icon_lbl.place(x=0, y=40)
            self.count_med=Label(self.med_frame, text='9', bg='white', fg='#191970', font=('Verdana', 27, 'bold')
                  , bd=0)
            self.count_med.place(x=140, y=20)
            self.text_med=Label(self.med_frame, text='Medicine', bg='white', fg='red', font=('Verdana', 18, 'bold')
                  , bd=0)
            self.text_med.place(x=140, y=70)
            self.med_frame.bind('<Enter>', self._med_hover_)
            self.med_frame.bind('<Leave>', self._leave_med_hover)

            # rooms
            self.room_frame = Frame(self.root, cursor='hand2',bg='white', bd=1, relief='flat', width=300, height=130)
            self.room_frame.place(x=1080, y=360)
            self.rom_icon = Image.open('images/room.png')
            self.room_res = self.rom_icon.resize((110, 110), Image.ANTIALIAS)
            self.new_room = ImageTk.PhotoImage(self.room_res)
            self.rom_icon_lbl=Label(self.room_frame, image=self.new_room, bg='white', bd=0)
            self.rom_icon_lbl.place(x=0, y=40)
            self.count_rom=Label(self.room_frame, text='9', bg='white', fg='#191970', font=('Verdana', 27, 'bold')
                  , bd=0)
            self.count_rom.place(x=140, y=20)
            self.text_room=Label(self.room_frame, text='Rooms', bg='white', fg='red', font=('Verdana', 18, 'bold')
                  , bd=0)
            self.text_room.place(x=140, y=70)
            self.room_frame.bind('<Enter>', self._roms_hover_)
            self.room_frame.bind('<Leave>', self._leave_rom_hover)

            # departments
            self.dep_frame = Frame(self.root,cursor='hand2', bg='white', bd=1, relief='flat', width=300, height=130)
            self.dep_frame.place(x=320, y=520)
            self.dep_icon = Image.open('images/deprt.png')
            self.dep_res = self.dep_icon.resize((120, 90), Image.ANTIALIAS)
            self.new_dep = ImageTk.PhotoImage(self.dep_res)
            self.dep_icon_lbl=Label(self.dep_frame, image=self.new_dep, bg='white', bd=0)
            self.dep_icon_lbl.place(x=0, y=40)
            self.count_dep=Label(self.dep_frame, text='9', bg='white', fg='#191970', font=('Verdana', 27, 'bold')
                  , bd=0)
            self.count_dep.place(x=140, y=20)
            self.text_dep=Label(self.dep_frame, text='Departs', bg='white', fg='red', font=('Verdana', 18, 'bold')
                  , bd=0)
            self.text_dep.place(x=140, y=70)
            self.dep_frame.bind('<Enter>', self._departs_hover_)
            self.dep_frame.bind('<Leave>', self._leave_departs_hover_)


            # purchases
            self.pur_frame = Frame(self.root,cursor='hand2', bg='white', bd=1, relief='flat', width=300, height=130)
            self.pur_frame.place(x=700, y=520)
            self.pu_icon = Image.open('images/sales.png')
            self.pur_res = self.pu_icon.resize((120, 90), Image.ANTIALIAS)
            self.new_pur = ImageTk.PhotoImage(self.pur_res)
            self.pur_icon_lbl=Label(self.pur_frame, image=self.new_pur, bg='white', bd=0)
            self.pur_icon_lbl.place(x=0, y=40)
            self.count_pur=Label(self.pur_frame, text='9', bg='white', fg='#191970', font=('Verdana', 27, 'bold')
                  , bd=0)
            self.count_pur.place(x=140, y=20)
            self.text_pur=Label(self.pur_frame, text='Purchases', bg='white', fg='red', font=('Verdana', 18, 'bold')
                  , bd=0)
            self.text_pur.place(x=140, y=70)
            self.pur_frame.bind('<Enter>', self._pur_hover_)
            self.pur_frame.bind('<Leave>', self._leave_pur)

            # reports
            self.sales = Frame(self.root,cursor='hand2', bg='white', bd=1, relief='flat', width=300, height=130)
            self.sales.place(x=1080, y=520)
            self.sale_icon = Image.open('images/RPOR.png')
            self.sales_res = self.sale_icon.resize((100, 90), Image.ANTIALIAS)
            self.new_sales = ImageTk.PhotoImage(self.sales_res)
            self.sales_icon_label=Label(self.sales, image=self.new_sales, bg='white', bd=0)
            self.sales_icon_label.place(x=15, y=40)
            self.count_sales_label=Label(self.sales, text='9', bg='white', fg='#191970', font=('Verdana', 27, 'bold')
                  , bd=0)
            self.count_sales_label.place(x=140, y=20)
            self.text_sales_label=Label(self.sales, text='Reports', bg='white', fg='red', font=('Verdana', 18, 'bold')
                  , bd=0)
            self.text_sales_label.place(x=140, y=70)
            self.sales.bind('<Enter>', self._sales_hover_)
            self.sales.bind('<Leave>', self._leave_sales_hover_)

            # BLOODS
            self.customer = Frame(self.root,cursor='hand2',bg='white', bd=1, relief='flat', width=300, height=130)
            self.customer.place(x=320, y=670)
            self.cus_icon = Image.open('images/BLOODS.png')
            self.cu_res = self.cus_icon.resize((90, 120), Image.ANTIALIAS)
            self.new_cus = ImageTk.PhotoImage(self.cu_res)
            self.customer_icon_label=Label(self.customer, image=self.new_cus, bg='white', bd=0)
            self.customer_icon_label.place(x=10, y=10)
            self.count_customer_label=Label(self.customer, text='9', bg='white', fg='#191970', font=('Verdana', 27, 'bold')
                  , bd=0)
            self.count_customer_label.place(x=140, y=20)
            self.text_customer_label=Label(self.customer, text='Bloods', bg='white', fg='red', font=('Verdana', 18, 'bold')
                  , bd=0)
            self.text_customer_label.place(x=140, y=70)
            self.customer.bind('<Enter>', self._customer_hover_)
            self.customer.bind('<Leave>', self._leave_customer_hover)




            # inpatient frame
            self.ip_frame = Frame(self.root, cursor='hand2', bg='white', bd=1, relief='flat', width=300, height=130)
            self.ip_frame.place(x=700, y=670)
            self.ip_icon = Image.open('images/IP.png')
            self.ip_res = self.ip_icon.resize((100, 90), Image.ANTIALIAS)
            self.new_ip = ImageTk.PhotoImage(self.ip_res)
            self.ip_icon_lbl=Label(self.ip_frame, image=self.new_ip, bg='white', bd=0)
            self.ip_icon_lbl.place(x=0, y=40)
            self.count_ip_label=Label(self.ip_frame, text='9', bg='white', fg='#191970', font=('Verdana', 27, 'bold')
                  , bd=0)
            self.count_ip_label.place(x=140, y=20)
            self.text_ip_label=Label(self.ip_frame, text='Inpatient', bg='white', fg='red', font=('Verdana', 18, 'bold')
                  , bd=0)
            self.text_ip_label.place(x=140, y=70)
            self.ip_frame.bind('<Enter>',self._ip_hover)
            self.ip_frame.bind('<Leave>',self._ip_leave)


            # outpatient
            self.op_frame = Frame(self.root, cursor='hand2', bg='white', bd=1, relief='flat', width=300, height=130)
            self.op_frame.place(x=1080, y=670)
            self.op_icon = Image.open('images/OP.png')
            self.op_res = self.op_icon.resize((100, 90), Image.ANTIALIAS)
            self.new_op = ImageTk.PhotoImage(self.op_res)
            self.op_icon_label=Label(self.op_frame, image=self.new_op, bg='white', bd=0)
            self.op_icon_label.place(x=0, y=40)
            self.count_op_lbl=Label(self.op_frame, text='9', bg='white', fg='#191970', font=('Verdana', 27, 'bold')
                  , bd=0)
            self.count_op_lbl.place(x=140, y=20)
            self.text_op_label=Label(self.op_frame, text='Outpatient', bg='white', fg='red', font=('Verdana', 18, 'bold')
                  , bd=0)
            self.text_op_label.place(x=140, y=70)

            # event hovers
            self.op_frame.bind('<Enter>',self.__hover__)
            self.op_frame.bind('<Leave>',self.__leave__)





            #=====MENUS======
            self.menu=Menu(self.root)
            self.root.config(menu=self.menu)
            self.file_menu=Menu(self.menu,tearoff=0)
            self.menu.add_cascade(label='File',menu=self.file_menu)
            self.file_menu.add_command(label='Developers',command=self.devs,accelerator='Ctrl+D')
            # self.file_menu.add_command(label='About')
            self.file_menu.add_separator()
            self.file_menu.add_command(label='Exit ',accelerator=' Ctrl+X',command=self.Exit)

            self.others = Menu(self.menu, tearoff=0)
            self.menu.add_cascade(label='Others', menu=self.others)
            self.others.add_command(label='InPatient',command=self.inpatient)
            self.others.add_command(label='OutPatient')
            # self.file_menu.add_command(label='About')
            self.others.add_separator()
            self.others.add_command(label='LabDiagnose ',command=self.diagnose)
            self.others.add_command(label='Takes Medicine ',command=self.taking_medcine)
            self.others.add_command(label='Shifts ',command=self.__shifts__)
            self.others.add_command(label='Billing Info ')

            self.report = Menu(self.menu, tearoff=0)
            self.menu.add_cascade(label='Reports', menu=self.report)
            self.report.add_command(label='Report', accelerator='Ctrl+R',command=self.__report__)
            self.report.add_command(label='View Reports', accelerator='Alt+V')

            # backup
            self.backup_menu= Menu(self.menu, tearoff=0)
            self.menu.add_cascade(label='Backups',menu=self.backup_menu)
            self.backup_menu.add_command(label='Full')
            self.backup_menu.add_command(label='Differential')

            # events
            self.root.bind('<Control-x>',self.quit)
            self.root.bind('<Control-d>',self.dev_s)
            self.root.bind('<Control-n>',self.minimize)






            # self.root.bind('<Control-l>',self.logout)

            #=======Dashboard-frame=========

            self.frame=Frame(self.root,bg='#2C3539',bd=4,relief='flat',width=300,height=870)
            self.frame.place(x=0,y=0)



            self.logo_icon=Image.open('icons/lg.png')
            self.resize_logo=self.logo_icon.resize((120,120),Image.ANTIALIAS)
            self.new_logo=ImageTk.PhotoImage(self.resize_logo)
            Label(self.frame,image=self.new_logo,bg='#2c3539',bd=0).place(x=0,y=0)

            self.menu_icon = Image.open('icons/menu_.png')
            self.menu_res = self.menu_icon.resize((90, 60), Image.ANTIALIAS)
            self.new_menu = ImageTk.PhotoImage(self.menu_res)

            Label(self.frame,cursor='hand2', image=self.new_menu, bg='#2c3539', bd=0).place(x=210, y=26)


            # admins pictures
            # me
            self.cj_icon=Image.open('Dev_Images/ENG-CJ.png')
            self.resize_image=self.cj_icon.resize((120,120),Image.ANTIALIAS)
            self.new_image=ImageTk.PhotoImage(self.resize_image)

            # Mohamed Ali
            self.kavi_icon = Image.open('Dev_Images/kaavi.png')
            self.resize_kaavi = self.kavi_icon.resize((120, 120), Image.ANTIALIAS)
            self.new_resize_kavi = ImageTk.PhotoImage(self.resize_kaavi)

            # Qadra
            #===============
            # Abdullahi Mascuud
            #===========
            # Mascuud
            #==========

            # ==== end admin images======




            # append labels
            self.admin_image=Label(self.frame,image=self.new_image, bd=0,bg='#2c3539')
            self.admin_image.place(x=20,y=120)
            self.subtitle = Label(self.frame, text='Admin', bg='#2c3539', fg='yellow',
                                  font=('Verdana', 9, 'bold'))
            self.subtitle.place(x=120, y=170)
            self.admin_title=Label(self.frame,text='Abdulrahman',bg='#2c3539',fg='white',
                                   font=('Verdana',12,'bold'))
            self.admin_title.place(x=120,y=145)
            #=====end Admin Appendings



            # ====ADMIN CONDITIONS===========
            # if self.admin_str.get() == self.admins[0]:
            # if self.admin_str.get()=='Abdirahman Haaji':
            #     self.admin_image.config(image=self.new_image, bg='#2c3539', bd=0)
            #     self.admin_image.place(x=20,y=120)
            #======end admin conditions

            Label(self.frame, text='____________________________________', bg='#2c3539', fg='#DCDCDC',
                  font=('Verdana', 10)).place(x=0, y=100, width=300)


            # btns dashboard
            self.dep=Image.open('images/deprt.png')
            self.res_=self.dep.resize((40,30),Image.ANTIALIAS)
            self.new_dep_icon=ImageTk.PhotoImage(self.res_)
            self.bg_dep=Label(self.frame,bg='#25283c',width=290)
            self.bg_dep.place(x=0,y=230,height=38)
            self.depButton=Button(self.bg_dep,command=self._deps_,cursor='hand2',text='Department',bg='#25283c',fg='white',
                                  image=self.new_dep_icon,bd=0,compound=LEFT,
                                  font=('Verdana',14,'bold'),activebackground='#008b8b',
                                  activeforeground='white'
                                  )

            self.depButton.place(x=0,y=2)
            self.depButton.bind('<Button-1>',self.activ)

            # self.depButton.bind('<Button-1>',self.activ)

            # btn dr
            self.Dr=Image.open('images/dr.png')
            self.dr_res=self.Dr.resize((30,30),Image.ANTIALIAS)
            self.new_dr_res=ImageTk.PhotoImage(self.dr_res)
            self.bg_dr=Label(self.frame,bg='#25283c',width=290)

            self.bg_dr.place(x=0,y=290,height=38)
            self.drButton=Button(
                    self.bg_dr,cursor='hand2',text='Doctor',bg='#25283c',fg='white',
                  image=self.new_dr_res,bd=0,compound=LEFT,
                  font=('Verdana',14,'bold'),activebackground='#008b8b',
                  activeforeground='white',
            command=self.drs)
            self.drButton.place(x=0,y=2)
            self.drButton.bind('<Button-1>',self.act_dr)
            # btn nurse
            self.NURSE = Image.open('images/n-icon.png')
            self.N_RES = self.NURSE.resize((30, 30), Image.ANTIALIAS)
            self.new_N = ImageTk.PhotoImage(self.N_RES)
            self.bg_nurse = Label(self.frame, bg='#25283c', width=290)

            self.bg_nurse.place(x=0, y=350, height=38)
            self.nrButton = Button(self.bg_nurse,cursor='hand2', text='Nurse', bg='#25283c', fg='white',
                                   image=self.new_N, bd=0, compound=LEFT,
                                   font=('Verdana', 14, 'bold'), activebackground='#008b8b',
                                   activeforeground='white'
                                   ,command=self.nurse)
            self.nrButton.bind('<Button-1>',self.actv_nurse)
            self.nrButton.place(x=0, y=2)

            # patient btn
            self.pat = Image.open('icons/pate-icon-btn.png')
            self.p_ = self.pat.resize((30, 30), Image.ANTIALIAS)
            self.n_p = ImageTk.PhotoImage(self.p_)
            self.bg_patient = Label(self.frame, bg='#25283c', width=290)

            self.bg_patient.place(x=0, y=410, height=38)
            self.pBtn = Button(self.bg_patient, cursor='hand2', text='Patient', bg='#25283c', fg='white',
                                   image=self.n_p, bd=0, compound=LEFT,
                                   font=('Verdana', 14, 'bold'), activebackground='#008b8b',
                                   activeforeground='white'
                                   ,command=self.manage_patient)
            self.pBtn.place(x=0, y=2)



            # pharmacist

            self.phrma = Image.open('icons/pha.png')
            self.ph_icon = self.phrma.resize((30, 30), Image.ANTIALIAS)
            self.n_ph = ImageTk.PhotoImage(self.ph_icon)
            self.bg_pharma = Label(self.frame, bg='#25283c', width=290)

            self.bg_pharma.place(x=0, y=460, height=38)
            self.phBtn = Button(self.bg_pharma, cursor='hand2', text='Pharmacist', bg='#25283c', fg='white',
                               image=self.n_ph, bd=0, compound=LEFT,
                               font=('Verdana', 14, 'bold'), activebackground='#008b8b',
                               activeforeground='white'
                               ,command=self.pharmcits)
            self.phBtn.place(x=0, y=2)


            # medicine
            self.med_ = Image.open('icons/med.png')
            self.medIcon = self.med_.resize((30, 30), Image.ANTIALIAS)
            self.n_med = ImageTk.PhotoImage(self.medIcon)
            self.bg_med = Label(self.frame, bg='#25283c', width=290)

            self.bg_med.place(x=0, y=520, height=38)
            self.medBtn = Button(self.bg_med, cursor='hand2', text='Medicine', bg='#25283c', fg='white',
                                image=self.n_med, bd=0, compound=LEFT,
                                font=('Verdana', 14, 'bold'), activebackground='#008b8b',
                                activeforeground='white'
                                ,command=self.medicine)
            self.medBtn.place(x=0, y=2)


            # rooms

            self.rooms_ = Image.open('icons/ro.png')
            self.romIcon = self.rooms_.resize((30, 30), Image.ANTIALIAS)
            self.n_room = ImageTk.PhotoImage(self.romIcon)
            self.bg_rom = Label(self.frame, bg='#25283c', width=290)

            self.bg_rom.place(x=0, y=575, height=38)
            self.romBtn = Button(self.bg_rom, cursor='hand2', text='Rooms', bg='#25283c', fg='white',
                                 image=self.n_room, bd=0, compound=LEFT,
                                 font=('Verdana', 14, 'bold'), activebackground='#008b8b',
                                 activeforeground='white'
                                 ,command=self.rooms)
            self.romBtn.place(x=0, y=2)

            # purchase

            self.pur_ = Image.open('images/patient.png')
            self.purIcon = self.pur_.resize((30, 30), Image.ANTIALIAS)
            self.n_pur = ImageTk.PhotoImage(self.purIcon)
            self.bg_pur = Label(self.frame, bg='#25283c', width=290)

            self.bg_pur.place(x=0, y=630, height=38)
            self.purBtn = Button(self.bg_pur, cursor='hand2', text='Purchases', bg='#25283c', fg='white',
                                 bd=0, compound=LEFT,
                                 font=('Verdana', 14, 'bold'), activebackground='#008b8b',
                                 activeforeground='white'
                                 ,command=self.purchase)
            self.purBtn.place(x=0, y=2)


            # sales
            self.sales_ = Image.open('icons/blood.png')
            self.saleIcon = self.sales_.resize((30, 30), Image.ANTIALIAS)
            self.n_sales = ImageTk.PhotoImage(self.saleIcon)
            self.bg_sales = Label(self.frame, bg='#25283c', width=290)

            self.bg_sales.place(x=0, y=685, height=38)
            self.saleBtn = Button(self.bg_sales, cursor='hand2', text='Bloods', bg='#25283c', fg='white',
                          bd=0, compound=LEFT,
                                 font=('Verdana', 14, 'bold'), activebackground='#008b8b',
                                 activeforeground='white'
                                 ,command=self.__bloods__)
            self.saleBtn.place(x=0, y=2)

            # reports
            self.sales_ = Image.open('images/patient.png')
            self.saleIcon = self.sales_.resize((30, 30), Image.ANTIALIAS)
            self.n_sale = ImageTk.PhotoImage(self.saleIcon)
            self.bg_reports = Label(self.frame, bg='#25283c', width=290)

            self.bg_reports.place(x=0, y=735, height=38)
            self.reportBtn = Button(self.bg_reports, cursor='hand2', text='Reports', bg='#25283c', fg='white',
                                  bd=0, compound=LEFT,
                                  font=('Verdana', 14, 'bold'), activebackground='#008b8b',
                                  activeforeground='white'
                                  ,command=self.__report__)
            self.reportBtn.place(x=0, y=2)
            self.pBtn.bind("<Button-1>",self.actv_pat)
            self.saleBtn.bind('<Button-1>',self.activ_sales)
            self.reportBtn.bind('<Button-1>',self.active_report)
            self.phBtn.bind('<Button-1>',self.actv_phara)
            self.purBtn.bind('<Button-1>',self.activ_pur)
            self.medBtn.bind('<Button-1>',self.activ_med)
            self.romBtn.bind('<Button-1>',self.activ_rooms)

            # logout btn
            self.logout_icon=Image.open('icons/logout.png')
            self.logout_resize=self.logout_icon.resize((110,115),Image.ANTIALIAS)
            self.new_logout_icon=ImageTk.PhotoImage(self.logout_resize)
            self.logout_btn=Button(
                self.root,image=self.new_logout_icon,bd=0,
                bg='#f4f4f4',
                activebackground='#f3f4f7',
                cursor='hand2',
                command=self.logout
            )
            self.logout_btn.place(x=1390,y=15)

    #        fetching
            self.show_counts()



    def activ(self,e):
        # self.depButton.focus()
        self.depButton.config(bg='#008b8b',fg='white',activebackground='#008b8b',
                              activeforeground='white')
        self.bg_sales.config(bg='#25283c')
        self.saleBtn.config(bg='#25283c', fg='white')

        self.bg_reports.config(bg='#25283c')
        self.reportBtn.config(bg='#25283c', fg='white')

        self.bg_pur.config(bg='#25283c')
        self.purBtn.config(bg='#25283c', fg='white')
        self.bg_dep.config(bg='#008b8b')
        self.bg_nurse.config(bg='#25283c')
        self.nrButton.config(bg='#25283c', fg='white')
        self.bg_pharma.config(bg='#25283c')
        self.phBtn.config(bg='#25283c', fg='white')
        self.bg_patient.config(bg='#25283c')
        self.pBtn.config(bg='#25283c', fg='white')
        self.bg_med.config(bg='#25283c')
        self.medBtn.config(bg='#25283c', fg='white')
        self.bg_rom.config(bg='#25283c')
        self.romBtn.config(bg='#25283c', fg='white')


        self.bg_dr.config(bg='#25283c')
        self.drButton.config(bg='#25283c', fg='white'
                            )
    def act_dr(self,e):
        self.bg_dep.config(bg='#25283c')
        self.depButton.config(bg='#25283c',fg='white'
                             )
        self.bg_nurse.config(bg='#25283c')
        self.nrButton.config(bg='#25283c', fg='white')
        self.bg_patient.config(bg='#25283c')
        self.pBtn.config(bg='#25283c', fg='white')
        self.bg_pharma.config(bg='#25283c')
        self.phBtn.config(bg='#25283c', fg='white')
        self.bg_med.config(bg='#25283c')
        self.medBtn.config(bg='#25283c', fg='white')
        self.bg_pur.config(bg='#25283c')
        self.purBtn.config(bg='#25283c', fg='white')
        self.bg_rom.config(bg='#25283c')
        self.romBtn.config(bg='#25283c', fg='white')
        self.bg_sales.config(bg='#25283c')
        self.saleBtn.config(bg='#25283c', fg='white')
        self.bg_reports.config(bg='#25283c')
        self.reportBtn.config(bg='#25283c', fg='white')


        self.drButton.config(bg='#008b8b',fg='white',activebackground='#008b8b',
                              activeforeground='white')
        self.bg_dr.config(bg='#008b8b')

    def actv_nurse(self,e):
        self.bg_dep.config(bg='#25283c')
        self.depButton.config(bg='#25283c', fg='white'
                              )
        self.bg_rom.config(bg='#25283c')
        self.romBtn.config(bg='#25283c', fg='white')
        self.bg_dr.config(bg='#25283c')
        self.drButton.config(bg='#25283c', fg='white')
        self.bg_patient.config(bg='#25283c')
        self.pBtn.config(bg='#25283c', fg='white')
        self.bg_pharma.config(bg='#25283c')
        self.phBtn.config(bg='#25283c', fg='white')
        self.bg_med.config(bg='#25283c')
        self.medBtn.config(bg='#25283c', fg='white')
        self.bg_pur.config(bg='#25283c')
        self.purBtn.config(bg='#25283c', fg='white')
        self.bg_sales.config(bg='#25283c')
        self.saleBtn.config(bg='#25283c', fg='white')
        self.bg_reports.config(bg='#25283c')
        self.reportBtn.config(bg='#25283c', fg='white')

        # config
        self.bg_nurse.config(bg='#008b8b')
        self.nrButton.config(bg='#008b8b',fg='white')

    def actv_pat(self,e):
        self.bg_dep.config(bg='#25283c')
        self.depButton.config(bg='#25283c', fg='white'
                              )
        self.bg_dr.config(bg='#25283c')
        self.drButton.config(bg='#25283c', fg='white')
        self.bg_nurse.config(bg='#25283c')
        self.nrButton.config(bg='#25283c', fg='white')
        self.bg_pharma.config(bg='#25283c')
        self.phBtn.config(bg='#25283c', fg='white')
        self.bg_med.config(bg='#25283c')
        self.medBtn.config(bg='#25283c', fg='white')
        self.bg_pur.config(bg='#25283c')
        self.purBtn.config(bg='#25283c', fg='white')
        self.bg_rom.config(bg='#25283c')
        self.romBtn.config(bg='#25283c', fg='white')
        self.bg_sales.config(bg='#25283c')
        self.saleBtn.config(bg='#25283c', fg='white')
        self.bg_reports.config(bg='#25283c')
        self.reportBtn.config(bg='#25283c', fg='white')

        self.bg_patient.config(bg='#008b8b')
        self.pBtn.config(bg='#008b8b', fg='white')

    def actv_phara(self,e):
        self.bg_dep.config(bg='#25283c')
        self.depButton.config(bg='#25283c', fg='white'
                              )
        self.bg_rom.config(bg='#25283c')
        self.romBtn.config(bg='#25283c', fg='white')
        self.bg_pur.config(bg='#25283c')
        self.purBtn.config(bg='#25283c', fg='white')
        self.bg_dr.config(bg='#25283c')
        self.drButton.config(bg='#25283c', fg='white')
        self.bg_nurse.config(bg='#25283c')

        self.nrButton.config(bg='#25283c', fg='white')
        self.bg_sales.config(bg='#25283c')
        self.saleBtn.config(bg='#25283c', fg='white')

        self.bg_patient.config(bg='#25283c')
        self.pBtn.config(bg='#25283c', fg='white')
        self.bg_med.config(bg='#25283c')
        self.medBtn.config(bg='#25283c', fg='white')
        self.bg_reports.config(bg='#25283c')
        self.reportBtn.config(bg='#25283c', fg='white')

        self.bg_pharma.config(bg='#008b8b')
        self.phBtn.config(bg='#008b8b',fg='white')

    def activ_med(self, e):
        self.bg_dep.config(bg='#25283c')
        self.depButton.config(bg='#25283c', fg='white'
                              )
        self.bg_rom.config(bg='#25283c')
        self.romBtn.config(bg='#25283c', fg='white')

        self.bg_dr.config(bg='#25283c')
        self.drButton.config(bg='#25283c', fg='white')
        self.bg_nurse.config(bg='#25283c')
        self.nrButton.config(bg='#25283c', fg='white')

        self.bg_patient.config(bg='#25283c')
        self.pBtn.config(bg='#25283c', fg='white')

        self.bg_pharma.config(bg='#25283c')
        self.phBtn.config(bg='#25283c', fg='white')
        self.bg_pur.config(bg='#25283c')
        self.purBtn.config(bg='#25283c', fg='white')
        self.bg_sales.config(bg='#25283c')
        self.saleBtn.config(bg='#25283c', fg='white')
        self.bg_reports.config(bg='#25283c')
        self.reportBtn.config(bg='#25283c', fg='white')

        self.bg_med.config(bg='#008b8b')
        self.medBtn.config(bg='#008b8b',fg='white')

    def activ_pur(self, e):
        self.bg_dep.config(bg='#25283c')
        self.depButton.config(bg='#25283c', fg='white'
                              )
        self.bg_dr.config(bg='#25283c')
        self.drButton.config(bg='#25283c', fg='white')
        self.bg_nurse.config(bg='#25283c')
        self.nrButton.config(bg='#25283c', fg='white')

        self.bg_patient.config(bg='#25283c')
        self.pBtn.config(bg='#25283c', fg='white')

        self.bg_pharma.config(bg='#25283c')
        self.phBtn.config(bg='#25283c', fg='white')

        self.bg_med.config(bg='#25283c')
        self.medBtn.config(bg='#25283c', fg='white')
        self.bg_rom.config(bg='#25283c')
        self.romBtn.config(bg='#25283c', fg='white')
        self.bg_sales.config(bg='#25283c')
        self.saleBtn.config(bg='#25283c', fg='white')
        self.bg_reports.config(bg='#25283c')
        self.reportBtn.config(bg='#25283c', fg='white')

        self.bg_pur.config(bg='#008b8b')
        self.purBtn.config(bg='#008b8b',fg='white')

    def activ_rooms(self, e):
        self.bg_dep.config(bg='#25283c')
        self.depButton.config(bg='#25283c', fg='white'
                              )
        self.bg_sales.config(bg='#25283c')
        self.saleBtn.config(bg='#25283c', fg='white')
        self.bg_dr.config(bg='#25283c')
        self.drButton.config(bg='#25283c', fg='white')
        self.bg_nurse.config(bg='#25283c')
        self.nrButton.config(bg='#25283c', fg='white')

        self.bg_patient.config(bg='#25283c')
        self.pBtn.config(bg='#25283c', fg='white')

        self.bg_pharma.config(bg='#25283c')
        self.phBtn.config(bg='#25283c', fg='white')

        self.bg_med.config(bg='#25283c')
        self.medBtn.config(bg='#25283c', fg='white')

        self.bg_pur.config(bg='#25283c')
        self.purBtn.config(bg='#25283c', fg='white')
        self.bg_reports.config(bg='#25283c')
        self.reportBtn.config(bg='#25283c', fg='white')

        self.bg_rom.config(bg='#008b8b')
        self.romBtn.config(bg='#008b8b', fg='white')

    def activ_sales(self, e):
        self.bg_dep.config(bg='#25283c')
        self.depButton.config(bg='#25283c', fg='white'
                              )
        self.bg_dr.config(bg='#25283c')
        self.drButton.config(bg='#25283c', fg='white')
        self.bg_nurse.config(bg='#25283c')
        self.nrButton.config(bg='#25283c', fg='white')

        self.bg_patient.config(bg='#25283c')
        self.pBtn.config(bg='#25283c', fg='white')

        self.bg_pharma.config(bg='#25283c')
        self.phBtn.config(bg='#25283c', fg='white')

        self.bg_med.config(bg='#25283c')
        self.medBtn.config(bg='#25283c', fg='white')

        self.bg_pur.config(bg='#25283c')
        self.purBtn.config(bg='#25283c', fg='white')

        self.bg_rom.config(bg='#25283c')
        self.romBtn.config(bg='#25283c', fg='white')

        self.bg_reports.config(bg='#25283c')
        self.reportBtn.config(bg='#25283c', fg='white')

        self.bg_sales.config(bg='#008b8b')
        self.saleBtn.config(bg='#008b8b', fg='white')


    def active_report(self, e):
        self.bg_dep.config(bg='#25283c')
        self.depButton.config(bg='#25283c', fg='white'
                              )
        self.bg_dr.config(bg='#25283c')
        self.drButton.config(bg='#25283c', fg='white')
        self.bg_nurse.config(bg='#25283c')
        self.nrButton.config(bg='#25283c', fg='white')

        self.bg_patient.config(bg='#25283c')
        self.pBtn.config(bg='#25283c', fg='white')

        self.bg_pharma.config(bg='#25283c')
        self.phBtn.config(bg='#25283c', fg='white')

        self.bg_med.config(bg='#25283c')
        self.medBtn.config(bg='#25283c', fg='white')

        self.bg_pur.config(bg='#25283c')
        self.purBtn.config(bg='#25283c', fg='white')

        self.bg_rom.config(bg='#25283c')
        self.romBtn.config(bg='#25283c', fg='white')

        self.bg_sales.config(bg='#25283c')
        self.saleBtn.config(bg='#25283c', fg='white')

        self.bg_reports.config(bg='#008b8b')
        self.reportBtn.config(bg='#008b8b',fg='white')










    #======Functions=========

    def _clock_(self):
        self.hours=time.strftime('%I')
        self.minutes=time.strftime('%M')
        self.seconds=time.strftime('%S')
        self.state=time.strftime('%p')

        self.month=time.strftime('%m')
        self.day=time.strftime('%d')
        self.year=time.strftime('%Y')
        self.clock_lable.config(text=f'{self.hours}:{self.minutes}:{self.seconds} {self.state}')
        self.date_label.config(text=f'{self.day}/{self.month}/{self.year}')
        self.clock_lable.after(1000,self._clock_)

    # Devs
    def devs(self):
        Dev.developers()

    # exit func
    def Exit(self):
        ans=messagebox.askyesno('Confirm','Are You Sure To Exit?')
        if (ans):
            self.root.destroy()
        else:
            pass




    #======Logins=============
    # activate usernames
    def active(self,e):
        self.otp_random = random.randint(1000, 9999)
        self.username.config(state=NORMAL)
        self.username.delete(0, END)
        self.username.insert(0, self.admin_str.get())
        if self.username.get() == self.admins[0]:
            try:
                messagebox.showinfo('OTP', 'Check Your Number\nAnd Enter The OTP Verification')
                message = client.messages.create(to="+252615178163", from_="+17755264333",
                                                 body=f"DARUL-SHIFA HOSPITAL Your Verification Code is-\nOTP: {self.otp_random}")
            except Exception as err:
                time.sleep(2)
                messagebox.showerror('err',f'{err}')
                # messagebox.showerror('Network Error','No Internet Connection\n'
                #                                      'Turn On Your Internet')
                self.username.delete(0,END)
                self.admin_str.set('Select Your Username')
        self.username.config(state=DISABLED)


    # Login

    def Login(self):

        if self.username.get() == '' or self.pascode.get() == '':
            messagebox.showerror('Error', 'All Fields Required')
        elif self.username.get() not in self.admins:
            messagebox.showerror('UserError',f'Invalid Admin Name → {self.username.get()}\n'
                                             f'The Admin Must Be Active The Admins Combobox')
            self.username.delete(0,END)
            self.pascode.delete(0,END)
            self.username.focus()
        else:

            try:

                self.otp_input = int(self.pascode.get())
                if self.otp_input == self.otp_random:
                    time.sleep(0.8)
                    self.otp_random =True
                    self.log.iconify()
                    self._main_Dashboard()


                elif self.otp_random == True:
                    messagebox.showerror('ERR', f'OTP CODE Already Have Been Used  With {self.username.get()}')
                    self.pascode.delete(0, END)
                else:
                    messagebox.showerror('ERR', 'Incorrect OTP Code Please Try Again\n Or Click Re-send To Re-send Again')
                    self.pascode.delete(0, END)

        #
            except Exception as err:
                messagebox.showerror('ERR', f'INVALID OPT CODE PLZ USE NUMERIC')
                self.pascode.delete(0, END)

    # resending  OTP
    def _resend_(self):
        if self.username.get() not in self.admins:
            messagebox.showerror('UserError', f'Invalid Admin Name → {self.username.get()}\n'
                                              f'The Admin Must In The Admins Combobox')
        else:
            if self.username.get() == self.admins[0]:
                try:
                    messagebox.showinfo('Resending OTP..', 'Check Your Number\nAnd Enter The OTP Verification')
                    message = client.messages.create(to="+252 61 5178163", from_="+17755264333",
                                                     body=f"DARUL-SHIFA HOSPITAL Verification Code is-\nOTP: {self.otp_random}")
                except:
                    time.sleep(2)
                    messagebox.showerror('Network Error', 'No Internet Connection\n'
                                                          'Turn On Your Internet')
                    self.username.delete(0, END)
                    self.admin_str.set('Select Your Username')
                    try:
                        # self.otp_input = int(self.pascode.get())
                        if self.otp_input == self.otp_random:
                            time.sleep(0.09)
                            self.otp_random = True
                            self.log.iconify()
                            self._main_Dashboard()


                        elif self.otp_random == True:
                            messagebox.showerror('ERR', f'this Code Already Have Been  Used With {self.username.get()}')
                            self.pascode.delete(0, END)
                        else:
                            messagebox.showerror('ERR', 'Incorrect OTP Code Please Try Again\n Or Click Re-send To Re-send Again')
                            self.pascode.delete(0, END)


                    except Exception as err:
                        messagebox.showerror('ERR', f'Invalid OTP Use Numberic.')
                        self.pascode.delete(0, END)

    # event functions
    def quit(self,e):
        ans=messagebox.askyesno('Confirm','Are Your Sure To Exit?')
        if ans:
            self.root.destroy()
            # self.log()
        else:
            pass
    def dev_s(self,e):
        Dev.developers()

    def minimize(self,e):
        self.root.iconify()


    # hovers
    def __hover__(self,e):
        self.op_frame.config(bg='#cddeff')
        self.op_icon_label.config(bg='#cddeff')
        self.count_op_lbl.config(bg='#cddeff')
        self.text_op_label.config(bg='#cddeff')

        # ip
    def __leave__(self,e):
        self.op_frame.config(bg='#fff')
        self.op_icon_label.config(bg='#fff')
        self.count_op_lbl.config(bg='#fff')
        self.text_op_label.config(bg='#fff')

    def _ip_hover(self,e):
        self.ip_icon_lbl.config(bg='#cddeff')
        self.count_ip_label.config(bg='#cddeff')
        self.text_ip_label.config(bg='#cddeff')
        self.ip_frame.config(bg='#cddeff')

    def _ip_leave(self,e):
        self.ip_frame.config(bg='#fff')
        self.ip_icon_lbl.config(bg='#fff')
        self.count_ip_label.config(bg='#fff')
        self.text_ip_label.config(bg='#fff')

    # dr
    def _dr_hover(self,e):
        self.dr_frame.config(bg='#cddeff')
        self.count_dr.config(bg='#cddeff')
        self.text_dr.config(bg='#cddeff')
        self.dr_icon_lbl.config(bg='#cddeff')
    def _dr_leave_hover(self,e):
        self.dr_frame.config(bg='#fff')
        self.dr_icon_lbl.config(bg='#fff')
        self.count_dr.config(bg='#fff')
        self.text_dr.config(bg='#fff')

    # patient
    def _patient_hover_(self,e):
        self.p_frame.config(bg='#cddeff')
        self.count_p.config(bg='#cddeff')
        self.text_p.config(bg='#cddeff')
        self.p_icon_lbl.config(bg='#cddeff')
    def _patient_leave_hover_(self,e):
        self.p_frame.config(bg='#fff')
        self.p_icon_lbl.config(bg='#fff')
        self.count_p.config(bg='#fff')
        self.text_p.config(bg='#fff')

    # nurse
    def _nurse_hover_(self,e):
        self.nurse_frame.config(bg='#cddeff')
        self.count_nurse.config(bg='#cddeff')
        self.text_nurse.config(bg='#cddeff')
        self.nurse_icon.config(bg='#cddeff')
    def _nurse_leave_hover_(self,e):
        self.nurse_frame.config(bg='#fff')
        self.nurse_icon.config(bg='#fff')
        self.count_nurse.config(bg='#fff')
        self.text_nurse.config(bg='#fff')

    # pharma
    def _pharma_hover_(self,e):
        self.pharma_frame.config(bg='#cddeff')
        self.count_pharma.config(bg='#cddeff')
        self.text_pharma.config(bg='#cddeff')
        self.pharma_icon_lbl.config(bg='#cddeff')
    def _leave_pharma_hover(self,e):
        self.pharma_frame.config(bg='#fff')
        self.pharma_icon_lbl.config(bg='#fff')
        self.count_pharma.config(bg='#fff')
        self.text_pharma.config(bg='#fff')

    # medicine
    def _med_hover_(self,e):
        self.med_frame.config(bg='#cddeff')
        self.count_med.config(bg='#cddeff')
        self.text_med.config(bg='#cddeff')
        self.med_icon_lbl.config(bg='#cddeff')
    def _leave_med_hover(self,e):
        self.med_frame.config(bg='#fff')
        self.med_icon_lbl.config(bg='#fff')
        self.count_med.config(bg='#fff')
        self.text_med.config(bg='#fff')

    #roms
    def _roms_hover_(self,e):
        self.room_frame.config(bg='#cddeff')
        self.count_rom.config(bg='#cddeff')
        self.text_room.config(bg='#cddeff')
        self.rom_icon_lbl.config(bg='#cddeff')
    def _leave_rom_hover(self,e):
        self.room_frame.config(bg='#fff')
        self.rom_icon_lbl.config(bg='#fff')
        self.count_rom.config(bg='#fff')
        self.text_room.config(bg='#fff')

    # deprts
    def _departs_hover_(self,e):
        self.dep_frame.config(bg='#cddeff')
        self.count_dep.config(bg='#cddeff')
        self.text_dep.config(bg='#cddeff')
        self.dep_icon_lbl.config(bg='#cddeff')
    def _leave_departs_hover_(self,e):
        self.dep_frame.config(bg='#fff')
        self.dep_icon_lbl.config(bg='#fff')
        self.count_dep.config(bg='#fff')
        self.text_dep.config(bg='#fff')

    # purchse
    def _pur_hover_(self,e):
        self.pur_frame.config(bg='#cddeff')
        self.count_pur.config(bg='#cddeff')
        self.text_pur.config(bg='#cddeff')
        self.pur_icon_lbl.config(bg='#cddeff')
    def _leave_pur(self,e):
        self.pur_frame.config(bg='#fff')
        self.pur_icon_lbl.config(bg='#fff')
        self.count_pur.config(bg='#fff')
        self.text_pur.config(bg='#fff')

    # sales
    def _sales_hover_(self,e):
        self.sales.config(bg='#cddeff')
        self.count_sales_label.config(bg='#cddeff')
        self.text_sales_label.config(bg='#cddeff')
        self.sales_icon_label.config(bg='#cddeff')
    def _leave_sales_hover_(self,e):
        self.sales.config(bg='#fff')
        self.sales_icon_label.config(bg='#fff')
        self.count_sales_label.config(bg='#fff')
        self.text_sales_label.config(bg='#fff')

    # customer
    def _customer_hover_(self,e):
        self.customer.config(bg='#cddeff')
        self.count_customer_label.config(bg='#cddeff')
        self.text_customer_label.config(bg='#cddeff')
        self.customer_icon_label.config(bg='#cddeff')

    def _leave_customer_hover(self,e):
        self.customer.config(bg='#fff')
        self.customer_icon_label.config(bg='#fff')
        self.count_customer_label.config(bg='#fff')
        self.text_customer_label.config(bg='#fff')




    # ______________Departments_______________________
    def _deps_(self):
        self.screen = Toplevel()
        self.screen.focus_force()
        self.screen.geometry('500x470')
        self.screen.resizable(0, 0)
        self.screen.config(bg='white')
        self.screen.title('Departments')
        # LABELS
        Label(self.screen, text='Manage Departments', bg='#00008b', fg='white',
              font=('Verdana', 18, 'bold')).pack(fill=X)

        Label(self.screen, text='DepID', bg='white', fg='black', font=('Verdana', 16, 'bold')).place(x=20, y=60)
        # global depID,depName
        self.depID = Entry(self.screen, font=('Verdana', 16, 'bold'), bg='#f4f4f4', fg='black',
                           bd=3, relief='groove')
        self.depID.place(x=20, y=100, width=120)

        Label(self.screen, text='DepName', bg='white', fg='black', font=('Verdana', 16, 'bold')).place(x=220, y=60)
        self.depName = Entry(self.screen, font=('Verdana', 16, 'bold'), bg='#f4f4f4', fg='black',
                             bd=3, relief='groove')
        self.depName.place(x=220, y=100, width=150)

        self.addBtn = Button(self.screen, text='Add', bg='#189', fg='white', font=('Verdana', 16, 'bold'),
                             bd=3, relief='sunken', command=self.add_)
        self.addBtn.place(x=20, y=160)

        self.update = Button(self.screen, text='Update', bg='#189', fg='white', font=('Verdana', 16, 'bold'),
                             bd=3, relief='sunken',command=self._update)
        self.update.place(x=100, y=160)

        self.Delete = Button(self.screen, text='Delete', bg='#189', fg='white', font=('Verdana', 16, 'bold'),
                             bd=3, relief='sunken',command=self._deletion_)
        self.Delete.place(x=230, y=160)
        # ===========================END LABLS==============

        # TREEVIEW STYLES
        self.style = ttk.Style()
        # style.configure("Treeview")

        self.style.theme_use('clam')
        self.style.configure("Treeview", background='#f4f4f4', foreground='#fff', font=('Verdana', 10),
                             fieldbackground='#f4f4f4')
        self.data_frame = Frame(self.screen, bg='white', bd=3, relief='ridge', width=900, heigh=100)
        self.data_frame.place(x=40, y=230)

        self.scrollbar = Scrollbar(self.data_frame, orient=VERTICAL)

        # global  tree_data
        self.tree_data = ttk.Treeview(self.data_frame, columns=("DepartID", 'DepartName'),
                                      yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.tree_data.yview)
        self.scrollbar.pack(fill=Y, side=RIGHT)
        self.tree_data.column('#0', width=0, stretch=NO)
        self.tree_data.column("DepartID")
        self.tree_data.column("DepartName")
        self.tree_data.heading("DepartID", text='DepartID')
        self.tree_data.heading("DepartName", text='Depart-Name')
        self.tree_data.pack(fill=BOTH, expand=1)
        # event
        self.tree_data.bind('<ButtonRelease-1>',self.selection)

        self._fetch_()


        mainloop()

    # fetching data from departs
    def _fetch_(self):
        conn = pyodbc.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
            "Database=DaruShifa_Hospital;"
            "Trusted_Connection=yes;"
        )
        cursor = conn.cursor()
        cursor.execute('select *from departments')
        rows = cursor.fetchall()
        for row in rows:
            self.tree_data.insert('', END, values=(
                row[0], row[1]
            ))

    # selection
    def selection(self,e):
        item_selected=self.tree_data.focus()
        selection_item=self.tree_data.item(item_selected,'values')
        self.depID.delete(0,END)
        self.depName.delete(0,END)
        # insert
        self.depID.insert(0,selection_item[0])
        self.depName.insert(0,selection_item[1])

    # add data
    def add_(self):
        # hos = HOSPITAL_SYSTEM.DARUL_SHIFA_HOSPITAL()
        if self.depID.get() == '' or self.depName.get() == '':
            messagebox.showerror('DaruShifa_Hospital', 'All Fields Are required')
        else:
            try:
                conn = pyodbc.connect(
                    "Driver={SQL Server Native Client 11.0};"
                    "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
                    "Database=DaruShifa_Hospital;"
                    "Trusted_Connection=yes;"
                )
                cursor = conn.cursor()
                cursor.execute('INSERT INTO departments VALUES(?,?)', (self.depID.get(), self.depName.get()))
                conn.commit()
                messagebox.showinfo('TEST', f'Successful Added\nDepartment [{self.depName.get()}]')
                self.tree_data.delete(*self.tree_data.get_children())
                self._fetch_()
                self.show_counts()
            except Exception as err:
                messagebox.showerror('Error Occurred', f'Error Occurred Due\n{err.args}')
    # delete
    def _deletion_(self):
        if self.depID.get()=='' or self.depName.get()=='':
            messagebox.showerror('ERR','Plz Select The Depart\nYou Want To Delete')
        else:
            try:
                item=self.tree_data.focus()
                selected=self.tree_data.item(item,'values')
                conn = pyodbc.connect(
                    "Driver={SQL Server Native Client 11.0};"
                    "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
                    "Database=DaruShifa_Hospital;"
                    "Trusted_Connection=yes;"
                )
                cursor=conn.cursor()
                ans=messagebox.askyesno('Confirm',f'Are You Sure To Delete \nThe Department {self.depName.get()}')
                if ans:
                    cursor.execute(f'DELETE departments where departID={selected[0]}')
                    conn.commit()
                    messagebox.showinfo('DaruShifa Hospital','Department Was Deleted Successfully')
                    self.depID.delete(0,END)
                    self.depName.delete(0,END)
                    self.tree_data.delete(*self.tree_data.get_children())
                    self._fetch_()
                    self.show_counts()
                else:
                    pass
            except Exception as err:
                messagebox.showerror('Error Ocurred',f'Error Ocurred Due\n{err}')
    # UPDATE
    def _update(self):
        if self.depID.get()=='' or self.depName.get()=='':
            messagebox.showerror('ERR','Plz Select The Depart\nYou Want To Update')
        else:
            try:
                item=self.tree_data.focus()
                selected=self.tree_data.item(item,'values')
                conn = pyodbc.connect(
                    "Driver={SQL Server Native Client 11.0};"
                    "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
                    "Database=DaruShifa_Hospital;"
                    "Trusted_Connection=yes;"
                )
                cursor=conn.cursor()
                cursor.execute(f'UPDATE departments set departID=?,departName=?  where departID={selected[0]}',
                               (self.depID.get(),self.depName.get()))
                conn.commit()
                messagebox.showinfo('DaruShifa Hospital','Department Updated Successfully')
                self.depID.delete(0,END)
                self.depName.delete(0,END)
                self.tree_data.delete(*self.tree_data.get_children())
                self._fetch_()
            except Exception as err:
                messagebox.showerror('Error Ocurred',f'Error Ocurred Due\n{err}')




     #_____________END DEPARTMENTS_______________

    #_______________DOCTORS_________________
    def drs(self):
        self.drs = Toplevel()
        # self.product.geometry('1100x740+30+20')
        self.drs.state('zoomed')
        self.drs.focus_force()
        self.drs.title('drss')
        self.drs.resizable(0, 0)
        self.drs.config(bg='#fff')
        # self.product.iconbitmap('logo.ico')

        # product
        Label(self.drs, text='DARUL-SHIFA HOSPITAL | MANAGE DOCTORS', bg='#015', fg='white', bd=3,
              relief='flat',
              font=('Verdana', 20, 'bold'), height=2).pack(fill=X)
        self.clock = Label(self.drs, bg='#015', fg='white', bd=3, relief='flat',
                           font=('Verdana', 18, 'bold'), height=2)
        self.clock.place(x=0, y=0)
        # self.clock_()

        # image
        self.log = Image.open('icons/lg.png')
        self.resizing = self.log.resize((60, 60), Image.ANTIALIAS)
        self.new_icon = ImageTk.PhotoImage(self.resizing)
        self.lb = Label(self.drs, bg='#015', image=self.new_icon, bd=0)
        self.lb.place(x=330, y=5)

        Label(self.drs, text='DrID', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=10, y=100)
        self.drid = Entry(self.drs, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                          bd=4, relief='sunken', width=10)
        self.drid.place(x=10, y=150)

        # drs name
        Label(self.drs, text='Dr-Name', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=10, y=200)
        self.drname = Entry(self.drs, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                            bd=4, relief='sunken', width=15)
        self.drname.place(x=10, y=250)

        # price
        Label(self.drs, text='Age', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=10, y=300)
        self.age = Entry(self.drs, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                         bd=4, relief='sunken', width=15)
        self.age.place(x=10, y=350)

        # quantity
        Label(self.drs, text='Mobile', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=320, y=100)
        self.mobile = Entry(self.drs, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                            bd=4, relief='sunken', width=15)
        self.mobile.place(x=320, y=150)

        # address
        Label(self.drs, text='Address', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=650, y=100)
        self.address = Entry(self.drs, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                             bd=4, relief='sunken', width=10)
        self.address.place(x=650, y=150)

        # baner

        self.banner_img = Image.open('images/medicine-banner.png')
        self.res = self.banner_img.resize((550, 500), Image.ANTIALIAS)
        self.baner = ImageTk.PhotoImage(self.res)
        Label(self.drs, image=self.baner, bg='white', bd=0).place(x=1030, y=120)

        # shifts


        Label(self.drs, text='Shift', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=850, y=100)
        self.shift_var=StringVar()
        self.shift=[]
        self.fetch_shifts()
        self.shift_var.set('Select')
        self.shifts = ttk.Combobox(self.drs,  textvariable=self.shift_var,values=self.shift,
                                   font=('Verdana', 15, 'bold'), justify=CENTER)
        self.shifts.place(x=850, y=150, width=230)
        self.shifts['state'] = 'readonly'
        # self.fetch_shifts()


        # Date
        Label(self.drs, text='Email', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=320, y=200)
        self.email = Entry(self.drs, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                           bd=4, relief='sunken', width=15)
        self.email.place(x=320, y=250)

        # Departs
        Label(self.drs, text='Departs', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=850, y=200)
        self.dep_var = StringVar()
        self.dep_var.set('Select')
        self.depList = []
        self.fetch_departs()
        self.departs = ttk.Combobox(self.drs, value=self.depList, textvariable=self.dep_var,
                                    font=('Verdana', 15, 'bold'), justify=CENTER)
        self.departs.place(x=850, y=250, width=230)
        self.departs['state'] = 'readonly'

        # specialist
        Label(self.drs, text='Specialist', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=650, y=200)
        self.specialist = Entry(self.drs, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                                bd=4, relief='sunken', width=10)
        self.specialist.place(x=650, y=250)

        # sALARAY
        Label(self.drs, text='Salary', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=650, y=300)
        self.salary = Entry(self.drs, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                            bd=4, relief='sunken', width=10)
        self.salary.place(x=650, y=350)

        Label(self.drs, text='Gender', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=320, y=300)
        self.gender_var = StringVar()
        self.gender_var.set('Select Gender')
        self.gends=['MALE','FEMALE']
        self.gender_combo=ttk.Combobox(self.drs,textvariable=self.gender_var,values=self.gends,font=('Verdana',9,'bold'),
                                       )
        self.gender_combo['state']='readonly'
        self.gender_combo.place(x=320,y=350)


        # Buttons
        self.add_btn = Button(self.drs, text='Add', bg='#019', fg='white',
                              bd=7, relief='ridge', font=('Verdana', 18, 'bold'),
                              command=self.add_dr)
        self.add_btn.place(x=190, y=420)

        self.update_btn = Button(self.drs, text='Update', bg='#019', fg='white',
                                 bd=7, relief='ridge', font=('Verdana', 18, 'bold')
                                 ,command=self.update_drs)
        self.update_btn.place(x=290, y=420)

        self.dele = Button(self.drs, text='Delete', bg='#019', fg='white',
                           bd=7, relief='ridge', font=('Verdana', 18, 'bold'),command=self.delete_drs)

        self.dele.place(x=445, y=420)

        # self.search = Button(self.drs, text='Delete', bg='#019', fg='white',
        #                    bd=7, relief='ridge', font=('Verdana', 18, 'bold'), command=self.Delete)
        #
        # self.search.place(x=445, y=420)
        # self.sear_var=IntVar()
        self.search = Entry(self.drs,bg='#fff', fg='#019', font=('Verdana', 15, 'bold'),
                            bd=4, relief='ridge', width=15)
        self.search.place(x=1290, y=15)
        self.drs.bind('<Control-f>', self.find)
        self.search.bind('<Button-1>', self._find_)
        self.search.bind('<Return>', self._Return_)
        self.drid.focus()

        self.search.insert(0, 'Search DrID')
        self.search.config(state=DISABLED)

        # tree-view table

        self.frame_tree = Frame(self.drs, bg='white', width=1090, bd=3, relief='groove')
        self.frame_tree.place(x=5, y=600)
        scrollbar = Scrollbar(self.frame_tree, orient=VERTICAL)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.tree = ttk.Treeview(self.frame_tree, yscrollcommand=scrollbar.set,
                                 columns=(
                                 'DrID', 'Dr-Name', 'Age', 'Mobile', 'Email', 'Gender', 'Address', 'Specialist',
                                 'Salary', 'Shift', 'Depart'))
        self.tree.pack(fill=BOTH, expand=True)
        # self.tree.bind('<ButtonRelease-1>',self.select)
        scrollbar.config(command=self.tree.yview)
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("Treeview", background='#f4f4f4', foreground='#fff', font=('Verdana', 10),
                             fieldbackground='#f4f4f4')

        self.style2 = ttk.Style()
        self.style2.theme_use('winnative')
        self.style2.configure("Combobox", background='red', foreground='#fff', font=('Verdana', 10),
                              fieldbackground='#f4f4f4')
        self.tree.column('#0', width=0, stretch=NO)
        self.tree.column('DrID', width=80)
        self.tree.column('Dr-Name', width=220)
        self.tree.column('Age', width=90, anchor=CENTER)
        self.tree.column('Mobile', width=200, anchor=CENTER)
        self.tree.column('Email', width=160, anchor=CENTER)
        self.tree.column('Gender', width=120, anchor=CENTER)
        self.tree.column('Address', width=120, anchor=CENTER)
        self.tree.column('Specialist', width=120, anchor=CENTER)
        self.tree.column('Salary', width=130, anchor=CENTER)
        self.tree.column('Shift', width=100, anchor=CENTER)
        self.tree.column('Depart', width=130, anchor=CENTER)

        self.tree.heading('DrID', text='DrID')
        self.tree.heading('Dr-Name', text='Dr-Name')
        self.tree.heading('Age', text='Age')
        self.tree.heading('Mobile', text='Mobile')
        self.tree.heading('Email', text='Email')
        self.tree.heading('Gender', text='Gender')
        self.tree.heading('Address', text='Address')
        self.tree.heading('Specialist', text='Specialist')
        self.tree.heading('Salary', text='Salary')
        self.tree.heading('Shift', text='Shift')
        self.tree.heading('Depart', text='Depart')
        self.tree.bind('<ButtonRelease-1>',self.selection_)
        self._fetch_drs()


        mainloop()

    def _find_(self, e):
        self.search.config(state=NORMAL)
        self.search.delete(0, END)
        self.search.focus()

    def find(self, e):
        self.search.config(state=NORMAL)
        self.search.delete(0, END)
        self.search.focus()




    # database
    def _fetch_drs(self):
        conn = pyodbc.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
            "Database=DaruShifa_Hospital;"
            "Trusted_Connection=yes;"
        )
        cursor = conn.cursor()
        cursor.execute('select *from Doctors')
        rows = cursor.fetchall()
        for row in rows:
            self.tree.insert('', END, values=(
                row[0], row[1],row[2], row[3],row[4], row[5],row[6], row[7],row[8], row[9],row[10]
            ))
    def fetch_shifts(self):
        conn = pyodbc.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
            "Database=DaruShifa_Hospital;"
            "Trusted_Connection=yes;"
        )
        cursor=conn.cursor()
        cursor.execute('select *from Shifts')
        rows=cursor.fetchall()
        for row in rows:
            self.shift.append(row[0])

    def fetch_departs(self):
        conn = pyodbc.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
            "Database=DaruShifa_Hospital;"
            "Trusted_Connection=yes;"
        )
        cursor = conn.cursor()
        cursor.execute('select *from Departments')
        rows = cursor.fetchall()
        for row in rows:
            self.depList.append(row[0])


    def selection_(self, e):
        try:
            self.drid.delete(0,END)
            self.drname.delete(0,END)
            self.age.delete(0,END)
            self.mobile.delete(0,END)
            self.email.delete(0,END)
            self.address.delete(0,END)
            self.salary.delete(0,END)
            self.specialist.delete(0,END)
            self.gender_var.set('')
            self.shifts.set('')
            self.dep_var.set('')
            item_selected = self.tree.focus()
            selection_item = self.tree.item(item_selected, 'values')
            self.drid.insert(0, selection_item[0])
            self.drname.insert(0, selection_item[1])
            self.age.insert(0, selection_item[2])
            self.gender_var.set(str(selection_item[3]))
            self.mobile.insert(0, selection_item[4])
            self.email.insert(0, selection_item[5])
            self.address.insert(0, selection_item[6])
            self.specialist.insert(0, selection_item[7])
            self.salary.insert(0, selection_item[8])
            self.shifts.set(str(selection_item[9]))
            self.dep_var.set(str(selection_item[10]))
        except Exception as err:
            messagebox.showerror('Err',f'Error Ocurred Due\n{err}')

        # insert

    # clear function
    def _clear_drs(self):
        self.drid.delete(0,END)
        self.drname.delete(0,END)
        self.age.delete(0,END)
        self.mobile.delete(0,END)
        self.address.delete(0,END)
        self.salary.delete(0,END)
        self.specialist.delete(0,END)
        self.email.delete(0,END)
        self.gender_var.set('Select')
        self.shift_var.set('Select')
        self.dep_var.set('Select')
    # add
    def add_dr(self):
        # hos = HOSPITAL_SYSTEM.DARUL_SHIFA_HOSPITAL()
        if self.drid.get()=='' or self.drname.get()=='' or self.age.get()=='' or self.mobile.get()=='' or self.email.get()=='' or self.gender_var.get()=='Select Gender' or self.address.get()=='' or self.specialist.get()=='' or self.salary.get()=='' or self.shift_var.get()=='Select' or self.dep_var.get()=='Select':
            messagebox.showerror('DaruShifa_Hospital', 'All Fields Are required')
        else:
            try:
                conn = pyodbc.connect(
                    "Driver={SQL Server Native Client 11.0};"
                    "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
                    "Database=DaruShifa_Hospital;"
                    "Trusted_Connection=yes;"
                )
                cursor = conn.cursor()
                cursor.execute('INSERT INTO Doctors VALUES(?,?,?,?,?,?,?,?,?,?,?)',
                (
                    self.drid.get(),self.drname.get(),self.age.get(),self.gender_var.get(),
                    self.mobile.get(),self.email.get(),self.address.get(),self.specialist.get(),
                    self.salary.get(),self.shift_var.get(),self.dep_var.get()
                ))
                conn.commit()
                messagebox.showinfo('DaruShifa Hospital', f'Successful Added\nDoctor [{self.drname.get()}]')
                self.tree.delete(*self.tree.get_children())
                self._fetch_drs()
                self.show_counts()
            except pyodbc.Error as err:
                sqlstate=err.args[1]
                sqlstate=sqlstate.split('.')
                # if sqlstate=='23000':
                messagebox.showerror(f'Error Occurred Code | {err.args[0]}', f'{sqlstate[2],sqlstate[3],sqlstate[4]}')

    # start update
    def update_drs(self):
        if self.drid.get() == '' or self.drname.get() == '' or self.age.get() == '' or self.mobile.get() == '' or self.email.get() == '' or self.gender_var.get() == 'Select Gender' or self.address.get() == '' or self.specialist.get() == '' or self.salary.get() == '' or self.shift_var.get() == 'Select' or self.dep_var.get() == 'Select':
            messagebox.showerror('ERR', 'Plz Select The Doctor\nYou Want To Update')
        else:
            try:
                item = self.tree.focus()
                selected = self.tree.item(item, 'values')
                conn = pyodbc.connect(
                    "Driver={SQL Server Native Client 11.0};"
                    "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
                    "Database=DaruShifa_Hospital;"
                    "Trusted_Connection=yes;"
                )
                cursor = conn.cursor()
                cursor.execute(f'UPDATE Doctors set DrID=?,Drname=?,Age=?,Gender=?,Mobile=?, Email=?, Address=?,Specialist=?,Salary=?,ShiftID=?,DepartID=?  '
                               f'where DrID={selected[0]}',
                               (
                                   self.drid.get(),
                                   self.drname.get(),
                                   self.age.get(),
                                   self.gender_var.get(),
                                   self.mobile.get(),
                                   self.email.get(),
                                   self.address.get(),
                                   self.specialist.get(),
                                   self.salary.get(),
                                   self.shift_var.get(),
                                   self.dep_var.get(),

                               ))
                conn.commit()
                messagebox.showinfo('DaruShifa Hospital', 'Doctor Updated Successfully')
                self._clear_drs()
                self.tree.delete(*self.tree.get_children())
                self._fetch_drs()
            except pyodbc.Error as err:
                sqlstate = err.args[1]
                sqlstate = sqlstate.split('.')
                # if sqlstate=='23000':
                messagebox.showerror(f'Error Occurred Code | {err.args[0]}', f'{sqlstate[2], sqlstate[3]}')
    #end_update

    # start_delete
    def delete_drs(self):
        if self.drid.get() == '' or self.drname.get() == '' or self.age.get() == '' or self.mobile.get() == '' or self.email.get() == '' or self.gender_var.get() == 'Select Gender' or self.address.get() == '' or self.specialist.get() == '' or self.salary.get() == '' or self.shift_var.get() == 'Select' or self.dep_var.get() == 'Select':
            messagebox.showerror('ERR', 'Plz Select The Doctor\nYou Want To Delete')
        else:
            try:
                item = self.tree.focus()
                selected = self.tree.item(item, 'values')
                conn = pyodbc.connect(
                    "Driver={SQL Server Native Client 11.0};"
                    "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
                    "Database=DaruShifa_Hospital;"
                    "Trusted_Connection=yes;"
                )
                cursor = conn.cursor()
                ans = messagebox.askyesno('Confirm', f'Are You Sure To Delete \nThe Doctor {self.drname.get()}')
                if ans:
                    cursor.execute(f'DELETE Doctors where DrID={selected[0]}')
                    conn.commit()
                    messagebox.showinfo('DaruShifa Hospital', 'Doctor Was Deleted Successfully')
                    self._clear_drs()
                    self.tree.delete(*self.tree.get_children())
                    self._fetch_drs()
                    self.show_counts()
                else:
                    pass
            except pyodbc.Error as err:
                    sqlstate = err.args[1]
                    sqlstate = sqlstate.split('.')
                    # if sqlstate=='23000':
                    messagebox.showerror(f'Error Occurred Code | {err.args[0]}',
                                         f'{sqlstate[2], sqlstate[3], sqlstate[4]}')


    #__end_delete
    def return_def(self,e):
        self.search.focus()
    # search drs
    def _Return_(self, e):
        # self.search.delete(0,END)
        try:
            search=self.search.get()
            conn = pyodbc.connect(
                "Driver={SQL Server Native Client 11.0};"
                "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
                "Database=DaruShifa_Hospital;"
                "Trusted_Connection=yes;"
            )
            cursor = conn.cursor()
            cursor.execute(f'select *from Doctors where DrID=?',(search))
            row=cursor.fetchone()
            if row!=None:
                for x in self.tree.get_children():
                    self.tree.delete(x)
                self.tree.insert('',END,values=(
                    row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]
                ))
            else:
                messagebox.showerror('DaruShifa Hospital','No Record Was Found With that ID')

        except pyodbc.Error as err:
            sqlstate = err.args[1]
            sqlstate = sqlstate.split('.')
            # if sqlstate=='23000':
            messagebox.showerror(f'Error Occurred Code | {err.args[0]}', f'{sqlstate[1], sqlstate[2]}')

    # selection

        #_________END DOCTORS___________________

    #____START NURSES
    def nurse(self):
        # def products(self):
        self.Nurses = Toplevel()
        # self.product.geometry('1100x740+30+20')
        self.Nurses.state('zoomed')
        self.Nurses.focus_force()
        self.Nurses.title('Nursess')
        self.Nurses.resizable(0, 0)
        self.Nurses.config(bg='#fff')
        # self.Nurses.iconbitmap('logo.ico')

        # Nurses
        Label(self.Nurses, text='DARUL-SHIFA HOSPITAL | MANAGE NURSES', bg='#015', fg='white', bd=3, relief='flat',
              font=('Verdana', 20, 'bold'), height=2).pack(fill=X)
        self.clock = Label(self.Nurses, bg='#015', fg='white', bd=3, relief='flat',
                           font=('Verdana', 18, 'bold'), height=2)
        self.clock.place(x=0, y=0)
        self.clock_()

        # image
        self.log = Image.open('icons/lg.png')
        self.resizing = self.log.resize((60, 60), Image.ANTIALIAS)
        self.new_icon = ImageTk.PhotoImage(self.resizing)
        self.lb = Label(self.Nurses, bg='#015', image=self.new_icon, bd=0)
        self.lb.place(x=330, y=5)

        Label(self.Nurses, text='NurseID', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=10, y=100)
        self.nurid = Entry(self.Nurses, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                          bd=4, relief='sunken', width=10)
        self.nurid.place(x=10, y=150)

        # Nurses name
        Label(self.Nurses, text='Nurse-Name', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=10, y=200)
        self.nursname = Entry(self.Nurses, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                            bd=4, relief='sunken', width=15)
        self.nursname.place(x=10, y=250)

        # price
        Label(self.Nurses, text='Age', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=10, y=300)
        self._age = Entry(self.Nurses, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                         bd=4, relief='sunken', width=15)
        self._age.place(x=10, y=350)

        # quantity
        Label(self.Nurses, text='Mobile', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=320, y=100)
        self._mobile = Entry(self.Nurses, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                            bd=4, relief='sunken', width=15)
        self._mobile.place(x=320, y=150)

        # address
        Label(self.Nurses, text='Address', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=650, y=100)
        self._address = Entry(self.Nurses, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                             bd=4, relief='sunken', width=10)
        self._address.place(x=650, y=150)

        # baner

        self.banner_img = Image.open('images/female-nurse.jpg')
        self.res = self.banner_img.resize((650, 600), Image.ANTIALIAS)
        self.baner = ImageTk.PhotoImage(self.res)
        Label(self.Nurses, image=self.baner, bg='white', bd=0).place(x=980, y=120)

        # shifts
        Label(self.Nurses, text='Shift', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=850, y=100)
        self.shift_var_n = StringVar()
        self.shift_var_n.set('Select')
        self.lists_n = []
        self.fetch_shifts_nurse()
        self.shifts_n = ttk.Combobox(self.Nurses, value=self.lists_n, textvariable=self.shift_var_n,
                                   font=('Verdana', 15, 'bold'), justify=CENTER)
        self.shifts_n.place(x=850, y=150, width=230)
        self.shifts_n['state'] = 'readonly'
        # self.shifts.config(background='red')

        # Date
        Label(self.Nurses, text='Email', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=320, y=200)
        self._email = Entry(self.Nurses, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                           bd=4, relief='sunken', width=15)
        self._email.place(x=320, y=250)

        # Departs
        Label(self.Nurses, text='Departs', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=850, y=200)
        self.dep_var_n = StringVar()
        self.dep_var_n.set('Select')
        self.list_departs_n = []
        self.fetch_departs_nurse()
        self.departs_n = ttk.Combobox(self.Nurses, value=self.list_departs_n, textvariable=self.dep_var_n,
                                    font=('Verdana', 15, 'bold'), justify=CENTER)
        self.departs_n.place(x=850, y=250, width=230)
        self.departs_n['state'] = 'readonly'

        # specialist
        Label(self.Nurses, text='Salary', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=650, y=200)
        self.salary_n = Entry(self.Nurses, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                                bd=4, relief='sunken', width=10)
        self.salary_n.place(x=650, y=250)

        # sALARAY
        # Label(self.Nurses, text='Salary', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
        #       ).place(x=650, y=300)
        # self.salary_n = Entry(self.Nurses, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
        #                     bd=4, relief='sunken', width=10)
        # self.salary_n.place(x=650, y=350)

        #gender
        Label(self.Nurses, text='Gender', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=320, y=300)
        self.gender_var_n = StringVar()
        self.gender_var_n.set('Select Gender')
        self.gends_n=['MALE','FEMALE']
        self.gender_combo_n=ttk.Combobox(self.Nurses,textvariable=self.gender_var_n,values=self.gends_n,font=('Verdana',9,'bold'),
                                       )
        self.gender_combo_n['state']='readonly'
        self.gender_combo_n.place(x=320,y=350)
        # Buttons
        self._add_btn = Button(self.Nurses, text='Add', bg='#019', fg='white',
                              bd=7, relief='ridge', font=('Verdana', 18, 'bold'),
                              command=self.add_nurse)
        self._add_btn.place(x=190, y=420)

        self._update_btn = Button(self.Nurses, text='Update', bg='#019', fg='white',
                                 bd=7, relief='ridge', font=('Verdana', 18, 'bold')
                                 ,command=self._update_nurse)
        self._update_btn.place(x=290, y=420)

        self._dele = Button(self.Nurses, text='Delete', bg='#019', fg='white',
                           bd=7, relief='ridge', font=('Verdana', 18, 'bold')
                            ,command=self._deletion_nurse)

        self._dele.place(x=445, y=420)

        # self.search = Button(self.Nurses, text='Delete', bg='#019', fg='white',
        #                    bd=7, relief='ridge', font=('Verdana', 18, 'bold'), command=self.Delete)
        #
        # self.search.place(x=445, y=420)

        self.search_ = Entry(self.Nurses, bg='#fff', fg='#019', font=('Verdana', 15, 'bold'),
                            bd=4, relief='ridge', width=15)
        self.search_.place(x=1290, y=15)
        self.Nurses.bind('<Control-f>', self.find_nurse)
        self.search_.bind('<Button-1>', self._find_nurse)
        self.search_.bind('<Return>', self._Return_nurse)
        self.nurid.focus()

        self.search_.insert(0, 'Search NurseID')
        self.search_.config(state=DISABLED)

        # tree-view table

        self.frame_tree = Frame(self.Nurses, bg='white', width=1090, bd=3, relief='groove')
        self.frame_tree.place(x=5, y=600)
        scrollbar = Scrollbar(self.frame_tree, orient=VERTICAL)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.tree_nurse = ttk.Treeview(self.frame_tree, yscrollcommand=scrollbar.set,
                                 columns=(
                                 'NurseID', 'Nurse-Name', 'Age', 'Mobile', 'Email', 'Gender', 'Address', 'Salary',
                                 'Shift', 'Depart'))
        self.tree_nurse.pack(fill=BOTH, expand=True)
        # self.tree.bind('<ButtonRelease-1>',self.select)
        scrollbar.config(command=self.tree_nurse.yview)
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("Treeview", background='#f4f4f4', foreground='#fff', font=('Verdana', 10),
                             fieldbackground='#f4f4f4')

        self.style2 = ttk.Style()
        self.style2.theme_use('clam')
        self.style2.configure("Combobox", background='red', foreground='#fff', font=('Verdana', 10),
                              fieldbackground='#f4f4f4')
        self.tree_nurse.column('#0', width=0, stretch=NO)
        self.tree_nurse.column('NurseID', width=80)
        self.tree_nurse.column('Nurse-Name', width=220)
        self.tree_nurse.column('Age', width=90, anchor=CENTER)
        self.tree_nurse.column('Mobile', width=200, anchor=CENTER)
        self.tree_nurse.column('Email', width=240, anchor=CENTER)
        self.tree_nurse.column('Gender', width=120, anchor=CENTER)
        self.tree_nurse.column('Address', width=200, anchor=CENTER)
        self.tree_nurse.column('Salary', width=130, anchor=CENTER)
        self.tree_nurse.column('Shift', width=100, anchor=CENTER)
        self.tree_nurse.column('Depart', width=130, anchor=CENTER)

        self.tree_nurse.heading('NurseID', text='NurseID')
        self.tree_nurse.heading('Nurse-Name', text='Nurse-Name')
        self.tree_nurse.heading('Age', text='Age')
        self.tree_nurse.heading('Mobile', text='Mobile')
        self.tree_nurse.heading('Email', text='Email')
        self.tree_nurse.heading('Gender', text='Gender')
        self.tree_nurse.heading('Address', text='Address')
        self.tree_nurse.heading('Salary', text='Salary')
        self.tree_nurse.heading('Shift', text='Shift')
        self.tree_nurse.heading('Depart', text='Depart')
        self.tree_nurse.bind('<ButtonRelease-1>',self.selection_nurse)
        self._fetch_nurses()

        mainloop()

    # fetch nurse
    def _fetch_nurses(self):
        conn = pyodbc.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
            "Database=DaruShifa_Hospital;"
            "Trusted_Connection=yes;"
        )
        cursor = conn.cursor()
        cursor.execute('select *from Nursing')
        rows = cursor.fetchall()
        for row in rows:
            self.tree_nurse.insert('', END, values=(
                row[0], row[1],row[2], row[3],row[4], row[5],row[6], row[7],
                row[8], row[9]
            ))

    # fetching departs
    def fetch_departs_nurse(self):
        conn = pyodbc.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
            "Database=DaruShifa_Hospital;"
            "Trusted_Connection=yes;"
        )
        cursor = conn.cursor()
        cursor.execute('select *from Departments')
        rows = cursor.fetchall()
        for row in rows:
            self.list_departs_n.append(row[0])

    # fetch shifts nurse
    def fetch_shifts_nurse(self):
        conn = pyodbc.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
            "Database=DaruShifa_Hospital;"
            "Trusted_Connection=yes;"
        )
        cursor = conn.cursor()
        cursor.execute('select *from Shifts')
        rows = cursor.fetchall()
        for row in rows:
            self.lists_n.append(row[0])


    # clear function
    def clear_nurse(self):
        self.nurid.delete(0,END)
        self.nursname.delete(0,END)
        self._age.delete(0,END)
        self._mobile.delete(0,END)
        self._address.delete(0,END)
        self.salary_n.delete(0,END)
        # self.specialist_n.delete(0,END)
        self._email.delete(0,END)
        self.shift_var_n.set('Select')
        self.departs_n.set('Select')

    # selection
    def selection_nurse(self,e):
        item_selected=self.tree_nurse.focus()
        selection_item=self.tree_nurse.item(item_selected,'values')
        self.clear_nurse()
        # insert
        self.nurid.insert(0,selection_item[0])
        self.nursname.insert(0,selection_item[1])
        self._age.insert(0,selection_item[2])
        self.gender_var_n.set(str(selection_item[3]))
        self._mobile.insert(0,selection_item[4])
        self._email.insert(0,selection_item[5])
        self._address.insert(0,selection_item[6])
        self.salary_n.insert(0, selection_item[7])
        self.shift_var_n.set(str(selection_item[8]))
        self.departs_n.set(str(selection_item[9]))

    # ___add____nurse
    def add_nurse(self):
        # hos = HOSPITAL_SYSTEM.DARUL_SHIFA_HOSPITAL()
        if self.nurid.get()=='' or self.nursname.get()=='' or self._age.get()=='' or self._mobile.get()=='' or self._email.get()=='' or self.gender_var_n.get()=='Select Gender' or self._address.get()=='' or   self.salary_n.get()=='' or self.shift_var_n.get()=='Select' or self.dep_var_n.get()=='Select':
            messagebox.showerror('DaruShifa_Hospital', 'All Fields Are required')
        else:
            try:
                conn = pyodbc.connect(
                    "Driver={SQL Server Native Client 11.0};"
                    "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
                    "Database=DaruShifa_Hospital;"
                    "Trusted_Connection=yes;"
                )
                cursor = conn.cursor()
                cursor.execute("INSERT INTO Nursing Values(?,?,?,?,?,?,?,?,?,?)",(
                    self.nurid.get(),
                    self.nursname.get(),
                    self._age.get(),
                    self.gender_var_n.get(),
                    self._mobile.get(),
                    self._email.get(),
                    self._address.get(),
                    self.salary_n.get(),
                    self.shift_var_n.get(),
                    self.departs_n.get()

                ))
                conn.commit()
                messagebox.showinfo('DaruShifa Hospital', f'Successful Added\nNurse [{self.nursname.get()}]')
                self.tree_nurse.delete(*self.tree_nurse.get_children())
                self._fetch_nurses()
                self.show_counts()
            except pyodbc.Error as err:
                sqlstate=err.args[1]
                sqlstate=sqlstate.split('.')
                # if sqlstate=='23000':
                messagebox.showerror(f'Error Occurred', f'{sqlstate[2],sqlstate[3],sqlstate[4]}')



    #__end____

    #update
    def _update_nurse(self):
        if self.nurid.get() == '' or self.nursname.get() == '' or self._age.get() == '' or self._mobile.get() == '' or self._email.get() == '' or self.gender_var_n.get() == 'Select Gender' or self._address.get() == '' or self.salary_n.get() == '' or self.shift_var_n.get() == 'Select' or self.dep_var_n.get() == 'Select':
            messagebox.showerror('ERR', 'Plz Select The Nurse\nYou Want To Update')
        else:
            try:
                item = self.tree_nurse.focus()
                selected = self.tree_nurse.item(item, 'values')
                conn = pyodbc.connect(
                    "Driver={SQL Server Native Client 11.0};"
                    "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
                    "Database=DaruShifa_Hospital;"
                    "Trusted_Connection=yes;"
                )
                cursor = conn.cursor()
                cursor.execute(f'UPDATE Nursing set NurseID=?,NurseName=?,Age=?,gender=?,Mobile=?, Email=?, Address=?,Salary=?,'
                               f'ShiftID=?,DepartID=? where NurseID={selected[0]}',
                               (
                                   self.nurid.get(),
                                   self.nursname.get(),
                                   self._age.get(),
                                   self.gender_var_n.get(),
                                   self._mobile.get(),
                                   self._email.get(),
                                   self._address.get(),
                                   self.salary_n.get(),
                                   self.shift_var_n.get(),
                                   self.departs_n.get()
                               ))
                conn.commit()
                messagebox.showinfo('DaruShifa Hospital', 'Nurse Updated Successfully')
                self.clear_nurse()
                self.tree_nurse.delete(*self.tree_nurse.get_children())
                self._fetch_nurses()
            except pyodbc.Error as err:
                sqlstate = err.args[1]
                sqlstate = sqlstate.split('.')
                # if sqlstate=='23000':
                messagebox.showerror(f'Error Occurred', f'{sqlstate[2], sqlstate[3]}')

    #end update

    # delete
    def _deletion_nurse(self):
        if self.nurid.get() == '' or self.nursname.get() == '' or self._age.get() == '' or self._mobile.get() == '' or self._email.get() == '' or self.gender_var_n.get() == 'Select Gender' or self._address.get() == '' or self.salary_n.get() == '' or self.shift_var_n.get() == 'Select' or self.dep_var_n.get() == 'Select':
            messagebox.showerror('ERR', 'Plz Select The Nurse\nYou Want To Delete')
        else:
            try:
                item = self.tree_nurse.focus()
                selected = self.tree_nurse.item(item, 'values')
                conn = pyodbc.connect(
                    "Driver={SQL Server Native Client 11.0};"
                    "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
                    "Database=DaruShifa_Hospital;"
                    "Trusted_Connection=yes;"
                )
                cursor = conn.cursor()
                ans = messagebox.askyesno('Confirm', f'Are You Sure To Delete \nThe Nurse {self.nursname.get()}')
                if ans:
                    cursor.execute(f'DELETE Nursing where NurseID={selected[0]}')
                    conn.commit()
                    messagebox.showinfo('DaruShifa Hospital', 'Nurse Was Deleted Successfully')
                    self.clear_nurse()
                    self.tree_nurse.delete(*self.tree_nurse.get_children())
                    self._fetch_nurses()
                    self.show_counts()
                else:
                    pass
            except pyodbc.Error as err:
                sqlstate = err.args[1]
                sqlstate = sqlstate.split('.')
                # if sqlstate=='23000':
                messagebox.showerror(f'Error Occurred', f'{sqlstate[0], sqlstate[1]}')

    #end delete

    def find_nurse(self, e):
        self.search_.config(state=NORMAL)
        self.search_.delete(0, END)
        self.search_.focus()

    def _find_nurse(self, e):
        self.search_.config(state=NORMAL)
        self.search_.delete(0, END)
        self.search_.focus()

    def _Return_nurse(self, e):
        try:
            search=self.search_.get()
            conn = pyodbc.connect(
                "Driver={SQL Server Native Client 11.0};"
                "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
                "Database=DaruShifa_Hospital;"
                "Trusted_Connection=yes;"
            )
            cursor = conn.cursor()
            cursor.execute(f'select *from Nursing where NurseID=?',(search))
            row=cursor.fetchone()

            if row!=None:
                for x in self.tree_nurse.get_children():
                    self.tree_nurse.delete(x)
                self.tree_nurse.insert('',END,values=(
                    row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]
                ))
            else:
                messagebox.showerror('DaruShifa Hospital','No Record Was Found With that ID')

        except pyodbc.Error as err:
            sqlstate = err.args[1]
            sqlstate = sqlstate.split('.')
            # if sqlstate=='23000':
            messagebox.showerror(f'Error Occurred Code | {err.args[0]}', f'{sqlstate[1], sqlstate[2]}')



    def clock_(self):
        import time
        self.hour = time.strftime('%I')
        self.minutes = time.strftime('%M')
        self.secons = time.strftime('%S')
        self.satte = time.strftime('%p')
        self.clock.config(text=f'Time: {self.hour}:{self.minutes}:{self.secons} {self.satte}')
        self.clock.after(1000, self.clock_)


    #___END__NURSES

    # patients
    def manage_patient(self):

        self.patients = Toplevel()
        # self.patients.geometry('1100x740+30+20')
        self.patients.state('zoomed')
        self.patients.focus_force()
        self.patients.title('patientss')
        self.patients.resizable(0, 0)
        self.patients.config(bg='#fff')
        # self.patients.iconbitmap('logo.ico')

        # patients
        Label(self.patients, text='DARUL-SHIFA HOSPITAL | MANAGE PATIENTS', bg='#015', fg='white', bd=3,
              relief='flat',
              font=('Verdana', 20, 'bold'), height=2).pack(fill=X)
        self.clock = Label(self.patients, bg='#015', fg='white', bd=3, relief='flat',
                           font=('Verdana', 18, 'bold'), height=2)
        self.clock.place(x=0, y=0)
        self.clock_patient()

        # image
        self.log = Image.open('icons/lg.png')
        self.resizing = self.log.resize((60, 60), Image.ANTIALIAS)
        self.new_icon = ImageTk.PhotoImage(self.resizing)
        self.lb = Label(self.patients, bg='#015', image=self.new_icon, bd=0)
        self.lb.place(x=330, y=5)

        Label(self.patients, text='PatientID', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=10, y=100)
        self.pat_id = Entry(self.patients, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                          bd=4, relief='sunken', width=10)
        self.pat_id.place(x=10, y=150)

        # patients name
        Label(self.patients, text='PatientName', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=10, y=200)
        self.pat_name = Entry(self.patients, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                            bd=4, relief='sunken', width=15)
        self.pat_name.place(x=10, y=250)

        # age
        Label(self.patients, text='Age', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=10, y=300)
        self.age_pat = Entry(self.patients, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                         bd=4, relief='sunken', width=15)
        self.age_pat.place(x=10, y=350)

        # quantity
        Label(self.patients, text='Mobile', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=320, y=100)
        self.mobile_pat = Entry(self.patients, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                            bd=4, relief='sunken', width=15)
        self.mobile_pat.place(x=320, y=150)

        # address
        Label(self.patients, text='Address', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=320, y=200)
        self.address_pat = Entry(self.patients, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                             bd=4, relief='sunken', width=10)
        self.address_pat.place(x=320, y=250)

        # baner

        self.banner_img = Image.open('images/patient-banner.jpg')
        self.res = self.banner_img.resize((570, 530), Image.ANTIALIAS)
        self.baner = ImageTk.PhotoImage(self.res)
        Label(self.patients, image=self.baner, bg='white', bd=0).place(x=920, y=120)

        # shifts
        Label(self.patients, text='Blood-Type', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=650, y=100)
        self.blood_var_pat = StringVar()
        self.blood_var_pat.set('Select')
        self.blood_lists_pat = []
        self.fetch_blood_pat()
        self.bloods = ttk.Combobox(self.patients, value=self.blood_lists_pat, textvariable=self.blood_var_pat,
                                   font=('Verdana', 15, 'bold'), justify=CENTER)
        self.bloods.place(x=650, y=150, width=180)
        self.bloods['state'] = 'readonly'
        # self.shifts.config(background='red')

        # Date



        # Departs
        Label(self.patients, text='DrID', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=650, y=200)
        self.dr_var = StringVar()
        self.dr_var.set('Select DrID')
        self.dr_lists = []
        self.fetch_drs_pat()
        self.drid_pat = ttk.Combobox(self.patients, value=self.dr_lists, textvariable=self.dr_var,
                                    font=('Verdana', 15, 'bold'), justify=CENTER)
        self.drid_pat.place(x=650, y=250, width=190)
        self.drid_pat['state'] = 'readonly'

        Label(self.patients, text='Gender', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=320, y=300)
        self.gender_var_pat = StringVar()
        self.gender_var_pat.set('Select')
        self.gender_list=['Male','Female']
        self.gender_combo_pat = ttk.Combobox(self.patients, font=('Verdana', 13, 'bold'),
                                 textvariable=self.gender_var_pat,value=self.gender_list,width=10)
        self.gender_combo_pat.place(x=320, y=350)



        # Buttons
        self.add_btn = Button(self.patients, text='Add', bg='#019', fg='white',
                              bd=7, relief='ridge', font=('Verdana', 18, 'bold'),
                              command=self.add_pateint)
        self.add_btn.place(x=190, y=420)

        self.update_btn = Button(self.patients, text='Update', bg='#019', fg='white',
                                 bd=7, relief='ridge', font=('Verdana', 18, 'bold')
                                 ,command=self._update_patients)
        self.update_btn.place(x=290, y=420)

        self.dele = Button(self.patients, text='Delete', bg='#019', fg='white',
                           bd=7, relief='ridge', font=('Verdana', 18, 'bold'),command=self._deletion_patient)

        self.dele.place(x=445, y=420)

        # self.search = Button(self.patients, text='Delete', bg='#019', fg='white',
        #                    bd=7, relief='ridge', font=('Verdana', 18, 'bold'), command=self.Delete)
        #
        # self.search.place(x=445, y=420)

        self.search_pat = Entry(self.patients, bg='#fff', fg='#019', font=('Verdana', 15, 'bold'),
                            bd=4, relief='ridge', width=15)
        self.search_pat.place(x=1290, y=15)

        self.search_pat.insert(0, 'Search PatienID')
        self.search_pat.config(state=DISABLED)
        self.search_pat.bind('<Button-1>',self._find_patient)
        self.search_pat.bind('<Return>',self._Return_patient)

        # tree-view table

        self.frame_tree = Frame(self.patients, bg='white', width=1090, bd=3, relief='groove')
        self.frame_tree.place(x=5, y=600)
        scrollbar = Scrollbar(self.frame_tree, orient=VERTICAL)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.tree_patients = ttk.Treeview(self.frame_tree, yscrollcommand=scrollbar.set,
                                 columns=('PaID', 'Patient-Name', 'Age', 'Gender', 'Mobile', 'Address',
                                          'Blood-Type', 'DoctorID'))
        self.tree_patients.pack(fill=BOTH, expand=True)
        # self.tree.bind('<ButtonRelease-1>',self.select)
        scrollbar.config(command=self.tree_patients.yview)
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("Treeview", background='#f4f4f4', foreground='#fff', font=('Verdana', 10),
                             fieldbackground='#f4f4f4')

        self.style2 = ttk.Style()
        self.style2.theme_use('clam')
        self.style2.configure("Combobox", background='red', foreground='#fff', font=('Verdana', 10),
                              fieldbackground='#f4f4f4')
        self.tree_patients.column('#0', width=0, stretch=NO)
        self.tree_patients.column('PaID', width=80)
        self.tree_patients.column('Patient-Name', width=320)
        self.tree_patients.column('Age', width=90, anchor=CENTER)
        self.tree_patients.column('Gender', width=220, anchor=CENTER)
        self.tree_patients.column('Mobile', width=230, anchor=CENTER)
        self.tree_patients.column('Address', width=200, anchor=CENTER)
        self.tree_patients.column('Blood-Type', width=130, anchor=CENTER)
        self.tree_patients.column('DoctorID', width=210, anchor=CENTER)
        self._fetch_patients()

        # display headings
        self.tree_patients.heading('PaID', text='PtaientID')
        self.tree_patients.heading('Patient-Name', text='Patient-Name')
        self.tree_patients.heading('Age', text='Age')
        self.tree_patients.heading('Gender', text='Gender')
        self.tree_patients.heading('Mobile', text='Mobile')
        self.tree_patients.heading('Address', text='Address')
        self.tree_patients.heading('Blood-Type', text='Blood-Type')
        self.tree_patients.heading('DoctorID', text='DoctorID')
        self.tree_patients.bind('<ButtonRelease-1>',self.selection_patients)

        mainloop()


    def _find_patient(self, e):
        self.search_pat.config(state=NORMAL)
        self.search_pat.delete(0, END)
        self.search_pat.focus()

    def _Return_patient(self, e):
        if self.search_pat.get()=='':
            messagebox.showerror('Error','Enter The ID you Want To Search')
        else:
            try:
                search = self.search_pat.get()
                conn = pyodbc.connect(
                    "Driver={SQL Server Native Client 11.0};"
                    "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
                    "Database=DaruShifa_Hospital;"
                    "Trusted_Connection=yes;"
                )
                cursor = conn.cursor()
                cursor.execute(f'select *from Patients where PatientID=?', (search))
                row = cursor.fetchone()
                if row != None:
                    for x in self.tree_patients.get_children():
                        self.tree_patients.delete(x)
                    self.tree_patients.insert('', END, values=(
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]
                    ))
                else:
                    messagebox.showerror('DaruShifa Hospital', 'No Record Was Found With that ID')

            except pyodbc.Error as err:
                sqlstate = err.args[1]
                sqlstate = sqlstate.split('.')
                # if sqlstate=='23000':
                messagebox.showerror(f'Error Occurred Code | {err.args[0]}', f'{sqlstate[1], sqlstate[2]}')

    def clock_patient(self):
        import time
        self.hour = time.strftime('%I')
        self.minutes = time.strftime('%M')
        self.secons = time.strftime('%S')
        self.satte = time.strftime('%p')
        self.clock.config(text=f'Time: {self.hour}:{self.minutes}:{self.secons} {self.satte}')
        self.clock.after(1000, self.clock_patient)

    # fetching bloods
    def fetch_blood_pat(self):
        conn = pyodbc.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
            "Database=DaruShifa_Hospital;"
            "Trusted_Connection=yes;"
        )
        cursor = conn.cursor()
        cursor.execute('select *from Bloods')
        rows = cursor.fetchall()
        for row in rows:
            self.blood_lists_pat.append(row[0])

    # fetch dr pat
    def fetch_drs_pat(self):
        conn = pyodbc.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
            "Database=DaruShifa_Hospital;"
            "Trusted_Connection=yes;"
        )
        cursor = conn.cursor()
        cursor.execute('select *from Doctors')
        rows = cursor.fetchall()
        for row in rows:
            self.dr_lists.append(row[0])


    # fetching patients
    def _fetch_patients(self):
        conn = pyodbc.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
            "Database=DaruShifa_Hospital;"
            "Trusted_Connection=yes;"
        )
        cursor = conn.cursor()
        cursor.execute('select *from Patients')
        rows = cursor.fetchall()
        for row in rows:
            self.tree_patients.insert('', END, values=(
                row[0], row[1],row[2], row[3],row[4], row[5],
                row[6], row[7]
            ))

    # add patients
    def add_pateint(self):
        # hos = HOSPITAL_SYSTEM.DARUL_SHIFA_HOSPITAL()
        if self.pat_id.get()=='' or self.pat_name.get()=='' or self.age_pat.get()=='' or self.mobile_pat.get()==''  or self.gender_var_pat.get()=='Select' or self.address_pat.get()==''  or self.blood_var_pat.get()=='Select' or self.dr_var.get()=='Select':
            messagebox.showerror('DaruShifa_Hospital', 'All Fields Are required')
        else:
            try:
                conn = pyodbc.connect(
                    "Driver={SQL Server Native Client 11.0};"
                    "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
                    "Database=DaruShifa_Hospital;"
                    "Trusted_Connection=yes;"
                )
                cursor = conn.cursor()
                cursor.execute("INSERT INTO Patients Values(?,?,?,?,?,?,?,?)",(
                    self.pat_id.get(),
                    self.pat_name.get(),
                    self.age_pat.get(),
                    self.gender_var_pat.get(),
                    self.mobile_pat.get(),
                    self.address_pat.get(),
                    self.blood_var_pat.get(),
                    self.dr_var.get()

                ))
                conn.commit()
                messagebox.showinfo('DaruShifa Hospital', f'Successful Added\nPatient [{self.pat_name.get()}]')
                self.tree_patients.delete(*self.tree_patients.get_children())
                self._fetch_patients()
                self.show_counts()
            except pyodbc.Error as err:
                sqlstate=err.args[1]
                sqlstate=sqlstate.split('.')
                # if sqlstate=='23000':
                messagebox.showerror(f'Error Occurred', f'{sqlstate[2],sqlstate[3],sqlstate[4]}')

    # clear patients
    def clear_patients(self):
        self.pat_id.delete(0, END)
        self.pat_name.delete(0, END)
        self.age_pat.delete(0, END)
        self.mobile_pat.delete(0, END)
        self.address_pat.delete(0, END)
        self.blood_var_pat.set('Select')
        self.dr_var.set('Select')

    # selection
    def selection_patients(self, e):
        item_selected = self.tree_patients.focus()
        selection_item = self.tree_patients.item(item_selected, 'values')
        self.clear_patients()
        # insert
        self.pat_id.insert(0,selection_item[0])
        self.pat_name.insert(0,selection_item[1])
        self.age_pat.insert(0,selection_item[2])
        self.gender_var_pat.set(str(selection_item[3]))
        self.mobile_pat.insert(0,selection_item[4])
        self.address_pat.insert(0,selection_item[5])
        self.blood_var_pat.set(str(selection_item[6]))
        self.dr_var.set(str(selection_item[7]))

    # update patienrs
    def _update_patients(self):
        if self.pat_id.get() == '' or self.pat_name.get() == '' or self.age_pat.get() == '' or self.mobile_pat.get() == '' or self.gender_var_pat.get() == 'Select' or self.address_pat.get() == '' or self.blood_var_pat.get() == 'Select' or self.dr_var.get() == 'Select':
            messagebox.showerror('ERR', 'Plz Select The Patient\nYou Want To Update')
        else:
            try:
                item = self.tree_patients.focus()
                selected = self.tree_patients.item(item, 'values')
                conn = pyodbc.connect(
                    "Driver={SQL Server Native Client 11.0};"
                    "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
                    "Database=DaruShifa_Hospital;"
                    "Trusted_Connection=yes;"
                )
                cursor = conn.cursor()
                cursor.execute(
                    f'UPDATE Patients set PatientID=?,P_name=?,Age=?,gender=?,Mobile=?, Address=?,'
                    f'BloodID=?,DrID=? where PatientID={selected[0]}',
                    (
                        self.pat_id.get(),
                        self.pat_name.get(),
                        self.age_pat.get(),
                        self.gender_var_pat.get(),
                        self.mobile_pat.get(),
                        self.address_pat.get(),
                        self.blood_var_pat.get(),
                        self.dr_var.get()

                    ))
                conn.commit()
                messagebox.showinfo('DaruShifa Hospital', 'Patient Updated Successfully')
                self.clear_patients()
                self.tree_patients.delete(*self.tree_patients.get_children())
                self._fetch_patients()
            except pyodbc.Error as err:
                sqlstate = err.args[1]
                sqlstate = sqlstate.split('.')
                # if sqlstate=='23000':
                messagebox.showerror(f'Error Occurred', f'{sqlstate[2], sqlstate[3]}')

    # delete patients

    def _deletion_patient(self):
        if self.pat_id.get() == '' or self.pat_name.get() == '' or self.age_pat.get() == '' or self.mobile_pat.get() == '' or self.gender_var_pat.get() == 'Select' or self.address_pat.get() == '' or self.blood_var_pat.get() == 'Select' or self.dr_var.get() == 'Select':
            messagebox.showerror('ERR', 'Plz Select The Patient\nYou Want To Delete')
        else:
            try:
                item = self.tree_patients.focus()
                selected = self.tree_patients.item(item, 'values')
                conn = pyodbc.connect(
                    "Driver={SQL Server Native Client 11.0};"
                    "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
                    "Database=DaruShifa_Hospital;"
                    "Trusted_Connection=yes;"
                )
                cursor = conn.cursor()
                ans = messagebox.askyesno('Confirm', f'Are You Sure To Delete \nThe Patient {self.pat_name.get()}')
                if ans:
                    cursor.execute(f'DELETE Patients where PatientID={selected[0]}')
                    conn.commit()
                    messagebox.showinfo('DaruShifa Hospital', 'Patient Was Deleted Successfully')
                    self.clear_patients()
                    self.tree_patients.delete(*self.tree_patients.get_children())
                    self._fetch_patients()
                    self.show_counts()
                else:
                    pass
            except pyodbc.Error as err:
                sqlstate = err.args[1]
                sqlstate = sqlstate.split('.')
                # if sqlstate=='23000':
                messagebox.showerror(f'Error Occurred', f'{sqlstate[0], sqlstate[1]}')

    # end patients

    def pharmcits(self):
        self.Pharam = Toplevel()
        # self.product.geometry('1100x740+30+20')
        self.Pharam.state('zoomed')
        self.Pharam.focus_force()
        self.Pharam.title('Pharmacist')
        self.Pharam.resizable(0, 0)
        self.Pharam.config(bg='#fff')
        # self.Pharam.iconbitmap('logo.ico')

        # Pharam
        Label(self.Pharam, text='DARUL-SHIFA HOSPITAL | MANAGE PHARMACIST', bg='#015', fg='white', bd=3, relief='flat',
              font=('Verdana', 20, 'bold'), height=2).pack(fill=X)
        self.clock = Label(self.Pharam, bg='#015', fg='white', bd=3, relief='flat',
                           font=('Verdana', 18, 'bold'), height=2)
        self.clock.place(x=0, y=0)
        self.clock_()

        # image
        self.log = Image.open('icons/lg.png')
        self.resizing = self.log.resize((60, 60), Image.ANTIALIAS)
        self.new_icon = ImageTk.PhotoImage(self.resizing)
        self.lb = Label(self.Pharam, bg='#015', image=self.new_icon, bd=0)
        self.lb.place(x=330, y=5)

        Label(self.Pharam, text='PharmacistID', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=10, y=100)
        self.pharma_id = Entry(self.Pharam, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                          bd=4, relief='sunken', width=10)
        self.pharma_id.place(x=10, y=150)

        # Pharam name
        Label(self.Pharam, text='Pharmacist-Name', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=10, y=200)
        self.pharam_name = Entry(self.Pharam, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                            bd=4, relief='sunken', width=15)
        self.pharam_name.place(x=10, y=250)

        # price
        Label(self.Pharam, text='Age', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=10, y=300)
        self.age_pharama = Entry(self.Pharam, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                         bd=4, relief='sunken', width=15)
        self.age_pharama.place(x=10, y=350)

        # quantity
        Label(self.Pharam, text='Mobile', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=320, y=100)
        self.mobile_pharma = Entry(self.Pharam, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                            bd=4, relief='sunken', width=15)
        self.mobile_pharma.place(x=320, y=150)

        # address
        Label(self.Pharam, text='Address', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=650, y=100)
        self.address_pharma = Entry(self.Pharam, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                             bd=4, relief='sunken', width=10)
        self.address_pharma.place(x=650, y=150)

        # baner

        self.banner_img = Image.open('images/p-2.jpg')
        self.res = self.banner_img.resize((570, 530), Image.ANTIALIAS)
        self.baner = ImageTk.PhotoImage(self.res)
        Label(self.Pharam, image=self.baner, bg='white', bd=0).place(x=920, y=120)

        # Date
        Label(self.Pharam, text='Email', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=320, y=200)
        self.email_pharma = Entry(self.Pharam, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                           bd=4, relief='sunken', width=15)
        self.email_pharma.place(x=320, y=250)

        Label(self.Pharam, text='Gender', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=320, y=300)
        self.gender_var_pharma = StringVar()
        self.gender_var_pharma.set('Select')
        self.gender_pharma_list=['Male','Female']
        self.gender_list_phar = ttk.Combobox(self.Pharam, font=('Verdana', 14, 'bold'),
                                value=self.gender_pharma_list, width=10,textvariable=self.gender_var_pharma)
        self.gender_list_phar.place(x=320, y=350)
        self.gender_list_phar['state']='readonly'



        # Buttons
        self.add_btn = Button(self.Pharam, text='Add', bg='#019', fg='white',
                              bd=7, relief='ridge', font=('Verdana', 18, 'bold'),
                              command=self.add_pharma)
        self.add_btn.place(x=190, y=420)

        self.update_btn = Button(self.Pharam, text='Update', bg='#019', fg='white',
                                 bd=7, relief='ridge', font=('Verdana', 18, 'bold')
                                ,command=self._update_pharma )
        self.update_btn.place(x=290, y=420)

        self.dele = Button(self.Pharam, text='Delete', bg='#019', fg='white',
                           bd=7, relief='ridge', font=('Verdana', 18, 'bold'),
                           command=self._deletion_pharma)

        self.dele.place(x=445, y=420)

        # self.search = Button(self.Pharam, text='Delete', bg='#019', fg='white',
        #                    bd=7, relief='ridge', font=('Verdana', 18, 'bold'), command=self.Delete)
        #
        # self.search.place(x=445, y=420)

        self.search_pharma = Entry(self.Pharam, bg='#fff', fg='#019', font=('Verdana', 15, 'bold'),
                            bd=4, relief='ridge', width=15)
        self.search_pharma.place(x=1290, y=15)
        self.Pharam.bind('<Control-f>', self.find_pharama)
        self.search_pharma.bind('<Button-1>', self._find_pharma)
        self.search_pharma.bind('<Return>', self._Return_pharma)
        self.search_pharma.focus()

        self.search_pharma.insert(0, 'Search PharmaID')
        self.search_pharma.config(state=DISABLED)

        # tree-view table

        self.frame_tree = Frame(self.Pharam, bg='white', width=1090, bd=3, relief='groove')
        self.frame_tree.place(x=5, y=600)
        scrollbar = Scrollbar(self.frame_tree, orient=VERTICAL)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.tree_pharma = ttk.Treeview(self.frame_tree, yscrollcommand=scrollbar.set,
                                 columns=('PharmaID', 'Pharma-Name', 'Age', 'Gender','Mobile', 'Email', 'Address'))
        self.tree_pharma.pack(fill=BOTH, expand=True)
        # self.tree.bind('<ButtonRelease-1>',self.select)
        scrollbar.config(command=self.tree_pharma.yview)
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("Treeview", background='#f4f4f4', foreground='#fff', font=('Verdana', 10),
                             fieldbackground='#f4f4f4')

        #   ^ Configuration
        self.style2 = ttk.Style()
        self.style2.theme_use('clam')
        self.style2.configure("Combobox", background='red', foreground='#fff', font=('Verdana', 10),
                              fieldbackground='#f4f4f4')
        self.tree_pharma.column('#0', width=0, stretch=NO)
        self.tree_pharma.column('PharmaID', width=80)
        self.tree_pharma.column('Pharma-Name', width=320)
        self.tree_pharma.column('Age', width=110, anchor=CENTER)
        self.tree_pharma.column('Gender', width=200, anchor=CENTER)
        self.tree_pharma.column('Mobile', width=200, anchor=CENTER)
        self.tree_pharma.column('Email', width=280, anchor=CENTER)

        self.tree_pharma.column('Address', width=300, anchor=CENTER)

        self.tree_pharma.heading('PharmaID', text='PharmaID')
        self.tree_pharma.heading('Pharma-Name', text='Pharma-Name')
        self.tree_pharma.heading('Age', text='Age')
        self.tree_pharma.heading('Gender', text='Gender')
        self.tree_pharma.heading('Mobile', text='Mobile')
        self.tree_pharma.heading('Email', text='Email')

        self.tree_pharma.heading('Address', text='Address')
        self._fetch_pharma()
        self.tree_pharma.bind('<ButtonRelease-1>',self.selection_pharma)

        mainloop()


    def find_pharama(self, e):
        self.search_pharma.config(state=NORMAL)
        self.search_pharma.delete(0, END)
        self.search_pharma.focus()

    def _find_pharma(self, e):
        self.search_pharma.config(state=NORMAL)
        self.search_pharma.delete(0, END)
        self.search_pharma.focus()

    def _Return_pharma(self, e):
        if self.search_pharma.get()=="":
            messagebox.showerror('ERR','Enter the ID U Want To Search')
        else:
            try:
                search = self.search_pharma.get()
                conn = pyodbc.connect(
                    "Driver={SQL Server Native Client 11.0};"
                    "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
                    "Database=DaruShifa_Hospital;"
                    "Trusted_Connection=yes;"
                )
                cursor = conn.cursor()
                cursor.execute(f'select *from Pharmacist where PharmID=?', (search))
                row = cursor.fetchone()
                if row != None:
                    for x in self.tree_pharma.get_children():
                        self.tree_pharma.delete(x)
                    self.tree_pharma.insert('', END, values=(
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6]
                    ))
                else:
                    messagebox.showerror('DaruShifa Hospital', 'No Record Was Found With that ID')

            except pyodbc.Error as err:
                sqlstate = err.args[1]
                sqlstate = sqlstate.split('.')
                # if sqlstate=='23000':
                messagebox.showerror(f'Error Occurred Code | {err.args[0]}', f'{sqlstate[1], sqlstate[2]}\nEnter Numeric Value')
    def clock_pharma(self):
        import time
        self.hour = time.strftime('%I')
        self.minutes = time.strftime('%M')
        self.secons = time.strftime('%S')
        self.satte = time.strftime('%p')
        self.clock.config(text=f'Time: {self.hour}:{self.minutes}:{self.secons} {self.satte}')
        self.clock.after(1000, self.clock_)


    # fetching pharma
    def _fetch_pharma(self):
        conn = pyodbc.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
            "Database=DaruShifa_Hospital;"
            "Trusted_Connection=yes;"
        )
        cursor = conn.cursor()
        cursor.execute('select *from Pharmacist')
        rows = cursor.fetchall()
        for row in rows:
            self.tree_pharma.insert('', END, values=(
                row[0], row[1],row[2], row[3],row[4], row[5],row[6]
            ))

    # clear pharama
    def clear__pharma(self):
        self.pharma_id.delete(0, END)
        self.pharam_name.delete(0, END)
        self.age_pharama.delete(0, END)
        self.mobile_pharma.delete(0, END)
        self.address_pharma.delete(0, END)
        self.email_pharma.delete(0, END)
        self.gender_var_pharma.set('Select')


   # selction
    def selection_pharma(self, e):
        item_selected = self.tree_pharma.focus()
        selection_item = self.tree_pharma.item(item_selected, 'values')
        self.clear__pharma()
        # insert
        self.pharma_id.insert(0, selection_item[0])
        self.pharam_name.insert(0, selection_item[1])
        self.age_pharama.insert(0, selection_item[2])
        self.gender_var_pharma.set(str(selection_item[3]))
        self.mobile_pharma.insert(0, selection_item[4])
        self.email_pharma.insert(0, selection_item[5])
        self.address_pharma.insert(0, selection_item[6])
        # self.salary_n.insert(0, selection_item[7])
        # self.shift_var_n.set(str(selection_item[8]))
        # self.departs_n.set(str(selection_item[9]))


    # add
    def add_pharma(self):
        # hos = HOSPITAL_SYSTEM.DARUL_SHIFA_HOSPITAL()
        if self.pharma_id.get()=='' or self.pharam_name.get()=='' or self.age_pharama.get()=='' or self.mobile_pharma.get()=='' or self.email_pharma.get()=='' or self.gender_var_pharma.get()=='Select' or self.address_pharma.get()=='':
            messagebox.showerror('DaruShifa_Hospital', 'All Fields Are required')
        else:
            try:
                conn = pyodbc.connect(
                    "Driver={SQL Server Native Client 11.0};"
                    "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
                    "Database=DaruShifa_Hospital;"
                    "Trusted_Connection=yes;"
                )
                cursor = conn.cursor()
                cursor.execute("INSERT INTO Pharmacist Values(?,?,?,?,?,?,?)",(
                    self.pharma_id.get(),
                    self.pharam_name.get(),
                    self.age_pharama.get(),
                    self.gender_var_pharma.get(),
                    self.mobile_pharma.get(),
                    self.email_pharma.get(),
                    self.address_pharma.get(),


                ))
                conn.commit()
                messagebox.showinfo('DaruShifa Hospital', f'Successful Added\nPharmacist [{self.pharam_name.get()}]')
                self.tree_pharma.delete(*self.tree_pharma.get_children())
                self._fetch_pharma()
                self.show_counts()
            except pyodbc.Error as err:
                sqlstate=err.args[1]
                sqlstate=sqlstate.split('.')
                # if sqlstate=='23000':
                messagebox.showerror(f'Error Occurred', f'{sqlstate[2],sqlstate[3],sqlstate[4]}')


    # update
    def _update_pharma(self):
        if self.pharma_id.get()=='' or self.pharam_name.get()=='' or self.age_pharama.get()=='' or self.mobile_pharma.get()=='' or self.email_pharma.get()=='' or self.gender_var_pharma.get()=='Select' or self.address_pharma.get()=='':
            messagebox.showerror('ERR', 'Plz Select The Pharmacist\nYou Want To Update')
        else:
            try:
                item = self.tree_pharma.focus()
                selected = self.tree_pharma.item(item, 'values')
                conn = pyodbc.connect(
                    "Driver={SQL Server Native Client 11.0};"
                    "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
                    "Database=DaruShifa_Hospital;"
                    "Trusted_Connection=yes;"
                )
                cursor = conn.cursor()
                cursor.execute(f'UPDATE Pharmacist set PharmID=?,Name=?,age=?,gender=?,mobile=?, Email=?, Address=? '
                               f'where PharmID={selected[0]}',
                               (
                                   self.pharma_id.get(),
                                   self.pharam_name.get(),
                                   self.age_pharama.get(),
                                   self.gender_var_pharma.get(),
                                   self.mobile_pharma.get(),
                                   self.email_pharma.get(),
                                   self.address_pharma.get(),
                               ))
                conn.commit()
                messagebox.showinfo('DaruShifa Hospital', 'Pharmacist Updated Successfully')
                self.clear__pharma()
                self.tree_pharma.delete(*self.tree_pharma.get_children())
                self._fetch_pharma()
            except pyodbc.Error as err:
                sqlstate = err.args[1]
                sqlstate = sqlstate.split('.')
                # if sqlstate=='23000':
                messagebox.showerror(f'Error Occurred', f'{sqlstate[2],sqlstate[3]}')
   # delete
    def _deletion_pharma(self):
        if self.pharma_id.get()=='' or self.pharam_name.get()=='' or self.age_pharama.get()=='' or self.mobile_pharma.get()=='' or self.email_pharma.get()=='' or self.gender_var_pharma.get()=='Select' or self.address_pharma.get()=='':
            messagebox.showerror('ERR', 'Plz Select The Pharmacist\nYou Want To Delete')
        else:
            try:
                item = self.tree_pharma.focus()
                selected = self.tree_pharma.item(item, 'values')
                conn = pyodbc.connect(
                    "Driver={SQL Server Native Client 11.0};"
                    "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
                    "Database=DaruShifa_Hospital;"
                    "Trusted_Connection=yes;"
                )
                cursor = conn.cursor()
                ans = messagebox.askyesno('Confirm', f'Are You Sure To Delete \nThe Pharmacist {self.pharam_name.get()}')
                if ans:
                    cursor.execute(f'DELETE Pharmacist where PharmID={selected[0]}')
                    conn.commit()
                    messagebox.showinfo('DaruShifa Hospital', 'Pharmacist Was Deleted Successfully')
                    self.clear__pharma()
                    self.tree_pharma.delete(*self.tree_pharma.get_children())
                    self._fetch_pharma()
                    self.show_counts()
                else:
                    pass
            except pyodbc.Error as err:
                sqlstate = err.args[1]
                sqlstate = sqlstate.split('.')
                # if sqlstate=='23000':
                messagebox.showerror(f'Error Occurred', f'{sqlstate[0], sqlstate[1]}')


    # end pharmacist


    def medicine(self):
        self.medicine = Toplevel()
        # self.medicine.geometry('1100x740+30+20')
        self.medicine.state('zoomed')
        self.medicine.focus_force()
        self.medicine.title('Medicines | Darul-Shifa')
        self.medicine.resizable(0, 0)
        self.medicine.config(bg='#fff')
        # self.medicine.iconbitmap('logo.ico')

        # medicine
        Label(self.medicine, text='DARUL-SHIFA HOSPITAL | MANAGE MEDICINES', bg='#015', fg='white', bd=3, relief='flat',
              font=('Verdana', 20, 'bold'), height=2).pack(fill=X)
        self.clock = Label(self.medicine, bg='#015', fg='white', bd=3, relief='flat',
                           font=('Verdana', 18, 'bold'), height=2)
        self.clock.place(x=0, y=0)
        self.clock_()

        # image
        self.log = Image.open('icons/lg.png')
        self.resizing = self.log.resize((60, 60), Image.ANTIALIAS)
        self.new_icon = ImageTk.PhotoImage(self.resizing)
        self.lb = Label(self.medicine, bg='#015', image=self.new_icon, bd=0)
        self.lb.place(x=330, y=5)

        Label(self.medicine, text='MedID', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=10, y=100)
        self.medid = Entry(self.medicine, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                          bd=4, relief='sunken', width=10)
        self.medid.place(x=10, y=150)

        # medicine name
        Label(self.medicine, text='MED-Name', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=10, y=200)
        self.med_name = Entry(self.medicine, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                            bd=4, relief='sunken', width=15)
        self.med_name.place(x=10, y=250)

        # price
        Label(self.medicine, text='Company', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=10, y=300)
        self.co = Entry(self.medicine, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                         bd=4, relief='sunken', width=15)
        self.co.place(x=10, y=350)

        # quantity
        Label(self.medicine, text='Quantity', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=320, y=100)
        self.qtty = Entry(self.medicine, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                            bd=4, relief='sunken', width=15)
        self.qtty.place(x=320, y=150)

        # address
        Label(self.medicine, text='Price', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=650, y=100)
        self.price_ = Entry(self.medicine, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                             bd=4, relief='sunken', width=10)
        self.price_.place(x=650, y=150)

        # baner

        self.banner_img = Image.open('images/iso-metr.jpg')
        self.res = self.banner_img.resize((620, 560), Image.ANTIALIAS)
        self.baner = ImageTk.PhotoImage(self.res)
        Label(self.medicine, image=self.baner, bg='white', bd=0).place(x=920, y=120)

        # Date
        Label(self.medicine, text='Type', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=320, y=200)
        self.type = Entry(self.medicine, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                           bd=4, relief='sunken', width=15)
        self.type.place(x=320, y=250)

        # desc
        Label(self.medicine, text='Description', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=320, y=295)
        self.desc = Entry(self.medicine, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                          bd=4, relief='sunken', width=15)
        self.desc.place(x=320, y=350)

        # Buttons
        self.add_btn = Button(self.medicine, text='Add', bg='#019', fg='white',
                              bd=7, relief='ridge', font=('Verdana', 18, 'bold'),
                              command=self.add_med)
        self.add_btn.place(x=190, y=420)

        self.update_btn = Button(self.medicine, text='Update', bg='#019', fg='white',
                                 bd=7, relief='ridge', font=('Verdana', 18, 'bold')
                                 ,command=self._update_med)
        self.update_btn.place(x=290, y=420)

        self.dele = Button(self.medicine, text='Delete', bg='#019', fg='white',
                           bd=7, relief='ridge', font=('Verdana', 18, 'bold'),
                           command=self._deletion_med)

        self.dele.place(x=445, y=420)

        # self.search = Button(self.medicine, text='Delete', bg='#019', fg='white',
        #                    bd=7, relief='ridge', font=('Verdana', 18, 'bold'), command=self.Delete)
        #
        # self.search.place(x=445, y=420)

        self.search_med = Entry(self.medicine, bg='#fff', fg='#019', font=('Verdana', 15, 'bold'),
                            bd=4, relief='ridge', width=15)
        self.search_med.place(x=1290, y=15)
        self.medicine.bind('<Control-f>', self.find_med)
        self.search_med.bind('<Button-1>', self._find_med)
        self.search_med.bind('<Return>', self._Return_med)
        self.search_med.focus()

        self.search_med.insert(0, 'Search MedID')
        self.search_med.config(state=DISABLED)

        # tree-view table

        self.frame_tree = Frame(self.medicine, bg='white', width=1090, bd=3, relief='groove')
        self.frame_tree.place(x=5, y=600)
        scrollbar = Scrollbar(self.frame_tree, orient=VERTICAL)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.tree_med = ttk.Treeview(self.frame_tree, yscrollcommand=scrollbar.set,

                                 columns=('MedID', 'MED-Name', 'Company', 'Quantity', 'Price', 'Type', 'Description'))
        self.tree_med.pack(fill=BOTH, expand=True)
        # self.tree.bind('<ButtonRelease-1>',self.select)
        scrollbar.config(command=self.tree_med.yview)
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("Treeview", background='#f4f4f4', foreground='#fff', font=('Verdana', 10),
                             fieldbackground='#f4f4f4')

        self.style2 = ttk.Style()
        self.style2.theme_use('clam')
        self.style2.configure("Combobox", background='red', foreground='#fff', font=('Verdana', 10),
                              fieldbackground='#f4f4f4')
        self.tree_med.column('#0', width=0, stretch=NO)
        self.tree_med.column('MedID', width=80)
        self.tree_med.column('MED-Name', width=250)
        self.tree_med.column('Company', width=130, anchor=CENTER)
        self.tree_med.column('Quantity', width=200, anchor=CENTER)
        self.tree_med.column('Price', width=240, anchor=CENTER)
        self.tree_med.column('Type', width=120, anchor=CENTER)
        self.tree_med.column('Description', width=490, anchor=CENTER)

        self.tree_med.heading('MedID', text='MedID')
        self.tree_med.heading('MED-Name', text='MED-Name')
        self.tree_med.heading('Company', text='Company')
        self.tree_med.heading('Quantity', text='Quantity')
        self.tree_med.heading('Price', text='Price')
        self.tree_med.heading('Type', text='Type')
        self.tree_med.heading('Description', text='Description')
        self._fetch_med()
        self.tree_med.bind('<ButtonRelease-1>',self.selection_med)

        mainloop()

    def add(self):
        pass

    def find_med(self, e):
        self.search_med.config(state=NORMAL)
        self.search_med.delete(0, END)
        self.search_med.focus()

    def _find_med(self, e):
        self.search_med.config(state=NORMAL)
        self.search_med.delete(0, END)
        self.search_med.focus()

    def _Return_med(self, e):
        if self.search_med.get()=='':
            messagebox.showerror('ERR','Plz Enter The ')
        try:
            search = self.search_med.get()
            conn = pyodbc.connect(
                "Driver={SQL Server Native Client 11.0};"
                "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
                "Database=DaruShifa_Hospital;"
                "Trusted_Connection=yes;"
            )
            cursor = conn.cursor()
            cursor.execute(f'select *from medicines where MedID=?', (search))
            row = cursor.fetchone()
            if row != None:
                for x in self.tree_med.get_children():
                    self.tree_med.delete(x)
                self.tree_med.insert('', END, values=(
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6]
                ))
            else:
                messagebox.showerror('DaruShifa Hospital', 'No Record Was Found With that ID')

        except pyodbc.Error as err:
            sqlstate = err.args[1]
            sqlstate = sqlstate.split('.')
            # if sqlstate=='23000':
            messagebox.showerror(f'Error Occurred Code | {err.args[0]}', f'{sqlstate[1], sqlstate[2]}')

    def clock_med(self):
        import time
        self.hour = time.strftime('%I')
        self.minutes = time.strftime('%M')
        self.secons = time.strftime('%S')
        self.satte = time.strftime('%p')
        self.clock.config(text=f'Time: {self.hour}:{self.minutes}:{self.secons} {self.satte}')
        self.clock.after(1000, self.clock_)


    # fetching

    def _fetch_med(self):
        conn = pyodbc.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
            "Database=DaruShifa_Hospital;"
            "Trusted_Connection=yes;"
        )
        cursor = conn.cursor()
        cursor.execute('select *from medicines')
        rows = cursor.fetchall()
        for row in rows:
            self.tree_med.insert('', END, values=(
                row[0], row[1],row[2], row[3],row[4], row[5],row[6]
            ))
    # clear med
    def clear_med(self):
        self.medid.delete(0, END)
        self.med_name.delete(0, END)
        self.co.delete(0, END)
        self.qtty.delete(0, END)
        self.price_.delete(0, END)
        self.type.delete(0, END)
        # self.specialist_n.delete(0,END)
        self.desc.delete(0, END)

    # selection med
    def selection_med(self, e):
        item_selected = self.tree_med.focus()
        selection_item = self.tree_med.item(item_selected, 'values')
        # self.clear_nurse()
        self.clear_med()
        # insert
        self.medid.insert(0, selection_item[0])
        self.med_name.insert(0, selection_item[1])
        self.co.insert(0, selection_item[2])
        self.qtty.insert(0,selection_item[3])
        self.price_.insert(0, selection_item[4])
        self.type.insert(0, selection_item[5])
        self.desc.insert(0, selection_item[6])

    # add
    def add_med(self):
        # hos = HOSPITAL_SYSTEM.DARUL_SHIFA_HOSPITAL()
        if self.medid.get()=='' or self.med_name.get()=='' or self.co.get()=='' or self.qtty.get()=='' or self.price_.get()=='' or self.type.get()=='' or self.desc.get()=='':
            messagebox.showerror('DaruShifa_Hospital', 'All Fields Are required')
        else:
            try:
                conn = pyodbc.connect(
                    "Driver={SQL Server Native Client 11.0};"
                    "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
                    "Database=DaruShifa_Hospital;"
                    "Trusted_Connection=yes;"
                )
                cursor = conn.cursor()
                cursor.execute("INSERT INTO medicines Values(?,?,?,?,?,?,?)",(
                    self.medid.get(),
                    self.med_name.get(),
                    self.co.get(),
                    self.qtty.get(),
                    self.price_.get(),
                    self.type.get(),
                    self.desc.get()

                ))
                conn.commit()
                messagebox.showinfo('DaruShifa Hospital', f'Successful Added\nMedicine [{self.med_name.get()}]')
                self.clear_med()
                self.tree_med.delete(*self.tree_med
                                       .get_children())
                self._fetch_med()
                self.show_counts()
            except pyodbc.Error as err:
                sqlstate=err.args[1]
                sqlstate=sqlstate.split('.')
                # if sqlstate=='23000':
                messagebox.showerror(f'Error Occurred', f'{sqlstate[2],sqlstate[3],sqlstate[4]}')

    # update
    def _update_med(self):
        if self.medid.get() == '' or self.med_name.get() == '' or self.co.get() == '' or self.qtty.get() == '' or self.price_.get() == '' or self.type.get() == '' or self.desc.get() == '':
            messagebox.showerror('ERR', 'Plz Select The Medicine\nYou Want To Update')
        else:
            try:
                item = self.tree_med.focus()
                selected = self.tree_med.item(item, 'values')
                conn = pyodbc.connect(
                    "Driver={SQL Server Native Client 11.0};"
                    "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
                    "Database=DaruShifa_Hospital;"
                    "Trusted_Connection=yes;"
                )
                cursor = conn.cursor()
                cursor.execute(
                    f'UPDATE medicines set MedID=?,MedName=?,Company=?,Quantity=?,Price=?, type=?, Description=? where MedID={selected[0]}',
                    (
                        self.medid.get(),
                        self.med_name.get(),
                        self.co.get(),
                        self.qtty.get(),
                        self.price_.get(),
                        self.type.get(),
                        self.desc.get()
                    ))
                conn.commit()
                messagebox.showinfo('DaruShifa Hospital', 'Medicine Updated Successfully')
                self.clear_med()
                self.tree_med.delete(*self.tree_med.get_children())
                self._fetch_med()
            except pyodbc.Error as err:
                sqlstate = err.args[1]
                sqlstate = sqlstate.split('.')
                # if sqlstate=='23000':
                messagebox.showerror(f'Error Occurred', f'{sqlstate[2], sqlstate[3]}')

    # DELETE
    def _deletion_med(self):
        if self.medid.get() == '' or self.med_name.get() == '' or self.co.get() == '' or self.qtty.get() == '' or self.price_.get() == '' or self.type.get() == '' or self.desc.get() == '':
            messagebox.showerror('ERR', 'Plz Select The Medicine\nYou Want To Delete')
        else:
            try:
                item = self.tree_med.focus()
                selected = self.tree_med.item(item, 'values')
                conn = pyodbc.connect(
                    "Driver={SQL Server Native Client 11.0};"
                    "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
                    "Database=DaruShifa_Hospital;"
                    "Trusted_Connection=yes;"
                )
                cursor = conn.cursor()
                ans = messagebox.askyesno('Confirm', f'Are You Sure To Delete \nThe Medicine {self.med_name.get()}')
                if ans:
                    cursor.execute(f'DELETE medicines where MedID={selected[0]}')
                    conn.commit()
                    messagebox.showinfo('DaruShifa Hospital', 'Medicine Was Deleted Successfully')
                    self.clear_med()
                    self.tree_med.delete(*self.tree_med.get_children())
                    self._fetch_med()
                    self.show_counts()
                else:
                    pass
            except pyodbc.Error as err:
                sqlstate = err.args[1]
                sqlstate = sqlstate.split('.')
                # if sqlstate=='23000':
                messagebox.showerror(f'Error Occurred', f'{sqlstate[0], sqlstate[1]}')
    # end medine


    def rooms(self):
        self.screen = Tk()
        self.screen.focus_force()
        self.screen.geometry('590x480')
        self.screen.resizable(0, 0)
        self.screen.config(bg='white')
        self.screen.title('Rooms')
        # LABELS
        Label(self.screen, text='Manage Rooms', bg='#00008b', fg='white',
              font=('Verdana', 18, 'bold')).pack(fill=X)

        Label(self.screen, text='RoomID', bg='white', fg='black', font=('Verdana', 16, 'bold')).place(x=20, y=60)

        self.roomID = Entry(self.screen, font=('Verdana', 16, 'bold'), bg='#f4f4f4', fg='black',
                            bd=3, relief='groove')
        self.roomID.place(x=20, y=100, width=120)

        Label(self.screen, text='Room-Type', bg='white', fg='black', font=('Verdana', 16, 'bold')).place(x=220, y=60)
        self.RomType = Entry(self.screen, font=('Verdana', 16, 'bold'), bg='#f4f4f4', fg='black',
                             bd=3, relief='groove')
        self.RomType.place(x=220, y=100, width=150)

        Label(self.screen, text='Status', bg='white', fg='black', font=('Verdana', 16, 'bold')).place(x=420, y=60)
        self.Status = Entry(self.screen, font=('Verdana', 16, 'bold'), bg='#f4f4f4', fg='black',
                            bd=3, relief='groove')
        self.Status.place(x=420, y=100, width=150)

        self.addBtn = Button(self.screen, text='Add', bg='#189', fg='white', font=('Verdana', 16, 'bold'),
                             bd=3, relief='sunken',command=self.add_room)
        self.addBtn.place(x=20, y=160)

        self.update = Button(self.screen, text='Update', bg='#189', fg='white', font=('Verdana', 16, 'bold'),
                             bd=3, relief='sunken',command=self._update_rooms)
        self.update.place(x=100, y=160)

        self.Delete = Button(self.screen, text='Delete', bg='#189', fg='white', font=('Verdana', 16, 'bold'),
                             bd=3, relief='sunken',command=self._deletion_rooms)
        self.Delete.place(x=230, y=160)
        # ===========================END LABLS==============

        # TREEVIEW STYLES
        self.style = ttk.Style()
        # style.configure("Treeview")


        self.style.theme_use('vista')
        self.style.configure("Treeview", background='#f4f4f4', foreground='#fff', font=('Verdana', 10),
                             fieldbackground='#f4f4f4')
        self.data_frame = Frame(self.screen, bg='white', bd=3, relief='ridge', width=900, heigh=100)
        self.data_frame.place(x=0, y=230)

        self.scrollbar = Scrollbar(self.data_frame, orient=VERTICAL)


        self.tree_data = ttk.Treeview(self.data_frame, columns=("RoomID", 'Room-Type', 'Status'),
                                      yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.tree_data.yview)
        self.scrollbar.pack(fill=Y, side=RIGHT)
        self.tree_data.column('#0', width=0, stretch=NO)
        self.tree_data.column("RoomID", width=120)
        self.tree_data.column("Room-Type", width=200)
        self.tree_data.column("Status", width=240)
        self.tree_data.heading("RoomID", text='RoomID')
        self.tree_data.heading("Room-Type", text='Room-Type')
        self.tree_data.heading("Status", text='Status')
        self.tree_data.pack(fill=BOTH, expand=1)
        self._fetch_rooms()
        self.tree_data.bind('<ButtonRelease-1>',self.selection_rooms)


        # TREE-END========================
        # self.show()/

        mainloop()

    # fetching
    def _fetch_rooms(self):
        conn = pyodbc.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
            "Database=DaruShifa_Hospital;"
            "Trusted_Connection=yes;"
        )
        cursor = conn.cursor()
        cursor.execute('select *from Rooms')
        rows = cursor.fetchall()
        for row in rows:
            self.tree_data.insert('', END, values=(
                row[0], row[1],row[2]
            ))

    # clear
    def clear_rooms(self):
        self.roomID.delete(0, END)
        self.RomType.delete(0, END)
        self.Status.delete(0, END)

    def add_room(self):
        # hos = HOSPITAL_SYSTEM.DARUL_SHIFA_HOSPITAL()
        if self.roomID.get()=='' or self.RomType.get()=='' or self.Status.get()=='':
            messagebox.showerror('DaruShifa_Hospital', 'All Fields Are required')
        else:
            try:
                conn = pyodbc.connect(
                    "Driver={SQL Server Native Client 11.0};"
                    "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
                    "Database=DaruShifa_Hospital;"
                    "Trusted_Connection=yes;"
                )
                cursor = conn.cursor()
                cursor.execute("INSERT INTO Rooms Values(?,?,?)",(
                    self.roomID.get(),
                    self.RomType.get(),
                    self.Status.get(),

                ))
                conn.commit()
                messagebox.showinfo('DaruShifa Hospital', f'Successful Added\nRoom [{self.RomType.get()}]')
                self.clear_rooms()
                self.tree_data.delete(*self.tree_data.get_children())
                self._fetch_rooms()
                self.show_counts()
            except pyodbc.Error as err:
                sqlstate=err.args[1]
                sqlstate=sqlstate.split('.')
                # if sqlstate=='23000':
                messagebox.showerror(f'Error Occurred', f'{sqlstate[2],sqlstate[3],sqlstate[4]}')
    # sleection
    def selection_rooms(self, e):
        item_selected = self.tree_data.focus()
        selection_item = self.tree_data.item(item_selected, 'values')
        self.clear_rooms()
        # insert
        self.roomID.insert(0, selection_item[0])
        self.RomType.insert(0, selection_item[1])
        self.Status.insert(0, selection_item[2])

    # update rooms
    def _update_rooms(self):
        if self.roomID.get()=='' or self.RomType.get()=='' or self.Status.get()=='':
            messagebox.showerror('ERR', 'Plz Select The Room\nYou Want To Update')
        else:
            try:
                item = self.tree_data.focus()
                selected = self.tree_data.item(item, 'values')
                conn = pyodbc.connect(
                    "Driver={SQL Server Native Client 11.0};"
                    "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
                    "Database=DaruShifa_Hospital;"
                    "Trusted_Connection=yes;"
                )
                cursor = conn.cursor()
                cursor.execute(f'UPDATE Rooms set RoomID=?,RoomType=?,Status=?'
                               f' where RoomID={selected[0]}',
                               (
                                   self.roomID.get(),
                                   self.RomType.get(),
                                   self.Status.get(),

                               ))
                conn.commit()
                messagebox.showinfo('DaruShifa Hospital', 'Room Updated Successfully')
                self.clear_rooms()
                self.tree_data.delete(*self.tree_data.get_children())
                self._fetch_rooms()
            except pyodbc.Error as err:
                sqlstate = err.args[1]
                sqlstate = sqlstate.split('.')
                # if sqlstate=='23000':
                messagebox.showerror(f'Error Occurred', f'{sqlstate[2], sqlstate[3]}')

    # deletin
    def _deletion_rooms(self):
        if self.roomID.get()=='' or self.RomType.get()=='' or self.Status.get()=='':
            messagebox.showerror('ERR', 'Plz Select The Room\nYou Want To Delete')
        else:
            try:
                item = self.tree_data.focus()
                selected = self.tree_data.item(item, 'values')
                conn = pyodbc.connect(
                    "Driver={SQL Server Native Client 11.0};"
                    "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
                    "Database=DaruShifa_Hospital;"
                    "Trusted_Connection=yes;"
                )
                cursor = conn.cursor()
                ans = messagebox.askyesno('Confirm', f'Are You Sure To Delete \nThe Room {self.RomType.get()}')
                if ans:
                    cursor.execute(f'DELETE Rooms where RoomID={selected[0]}')
                    conn.commit()
                    messagebox.showinfo('DaruShifa Hospital', 'Room Was Deleted Successfully')
                    self.clear_rooms()
                    self.tree_data.delete(*self.tree_data.get_children())
                    self._fetch_rooms()
                    self.show_counts()
                else:
                    pass
            except pyodbc.Error as err:
                sqlstate = err.args[1]
                sqlstate = sqlstate.split('.')
                # if sqlstate=='23000':
                messagebox.showerror(f'Error Occurred', f'{sqlstate[0], sqlstate[1]}')


        #

    # PURCHASE
    def purchase(self):
        self.Purchase = Toplevel()
        # self.Purchase.geometry('1100x740+30+20')
        self.Purchase.state('zoomed')
        self.Purchase.focus_force()
        self.Purchase.title('Purchases')
        self.Purchase.resizable(0, 0)
        self.Purchase.config(bg='#fff')
        # self.Purchase.iconbitmap('logo.ico')

        # Purchase
        Label(self.Purchase, text='DARUL-SHIFA HOSPITAL | MANAGE PHARMACIST', bg='#015', fg='white', bd=3, relief='flat',
              font=('Verdana', 20, 'bold'), height=2).pack(fill=X)
        self.clock = Label(self.Purchase, bg='#015', fg='white', bd=3, relief='flat',
                           font=('Verdana', 18, 'bold'), height=2)
        self.clock.place(x=0, y=0)
        self.clock_()

        # image
        self.log = Image.open('icons/lg.png')
        self.resizing = self.log.resize((60, 60), Image.ANTIALIAS)
        self.new_icon = ImageTk.PhotoImage(self.resizing)
        self.lb = Label(self.Purchase, bg='#015', image=self.new_icon, bd=0)
        self.lb.place(x=330, y=5)

        Label(self.Purchase, text='PurchaseID', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=10, y=100)
        self.purID = Entry(self.Purchase, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                           bd=4, relief='sunken', width=10)
        self.purID.place(x=10, y=150)

        # Purchase name
        Label(self.Purchase, text='Company', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=10, y=200)
        self.company = Entry(self.Purchase, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                             bd=4, relief='sunken', width=15)
        self.company.place(x=10, y=250)

        # price
        Label(self.Purchase, text='MedName', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=10, y=300)
        self.medname = Entry(self.Purchase, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                             bd=4, relief='sunken', width=15)
        self.medname.place(x=10, y=350)

        # quantity
        Label(self.Purchase, text='Cost', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=320, y=100)
        self.cost = Entry(self.Purchase, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                          bd=4, relief='sunken', width=15)
        self.cost.place(x=320, y=150)

        # address
        Label(self.Purchase, text='Date', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=320, y=300)
        self.date = Entry(self.Purchase, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                          bd=4, relief='sunken', width=15)
        self.date.place(x=320, y=350)

        # baner

        self.banner_img = Image.open('images/sales.png')
        self.res = self.banner_img.resize((490, 480), Image.ANTIALIAS)
        self.baner = ImageTk.PhotoImage(self.res)
        Label(self.Purchase, image=self.baner, bg='white', bd=0).place(x=790, y=100)

        # Date
        Label(self.Purchase, text='Type', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=320, y=200)
        self.type = Entry(self.Purchase, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                          bd=4, relief='sunken', width=15)
        self.type.place(x=320, y=250)

        # Buttons
        self.add_btn = Button(self.Purchase, text='Add', bg='#019', fg='white',
                              bd=7, relief='ridge', font=('Verdana', 18, 'bold'),
                              command=self.add_purchase)
        self.add_btn.place(x=190, y=420)

        self.update_btn = Button(self.Purchase, text='Update', bg='#019', fg='white',
                                 bd=7, relief='ridge', font=('Verdana', 18, 'bold')
                                 ,command=self._update_pur)
        self.update_btn.place(x=290, y=420)

        self.dele = Button(self.Purchase, text='Delete', bg='#019', fg='white',
                           bd=7, relief='ridge', font=('Verdana', 18, 'bold'),command=self._deletion_purchase)

        self.dele.place(x=445, y=420)

        # self.search = Button(self.Purchase, text='Delete', bg='#019', fg='white',
        #                    bd=7, relief='ridge', font=('Verdana', 18, 'bold'), command=self.Delete)
        #
        # self.search.place(x=445, y=420)

        self.search_pur = Entry(self.Purchase, bg='#fff', fg='#019', font=('Verdana', 15, 'bold'),
                            bd=4, relief='ridge', width=15)
        self.search_pur.place(x=1290, y=15)
        self.Purchase.bind('<Control-f>', self.find_pur)
        self.search_pur.bind('<Button-1>', self._find__pur)
        self.search_pur.bind('<Return>', self._Return_pur)

        self.search_pur.insert(0, 'Search PurchID')
        self.search_pur.config(state=DISABLED)

        # tree-view table

        self.frame_tree = Frame(self.Purchase, bg='white', width=1090, bd=3, relief='groove')
        self.frame_tree.place(x=5, y=600)
        scrollbar = Scrollbar(self.frame_tree, orient=VERTICAL)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.tree_pur = ttk.Treeview(self.frame_tree, yscrollcommand=scrollbar.set,
                                 columns=('PurID', 'Company', 'Medname', 'Cost', 'Type', 'Date'))
        self.tree_pur.pack(fill=BOTH, expand=True)
        # self.tree.bind('<ButtonRelease-1>',self.select)
        scrollbar.config(command=self.tree_pur.yview)
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("Treeview", background='#f4f4f4', foreground='#fff', font=('Verdana', 10),
                             fieldbackground='#f4f4f4')

        self.style2 = ttk.Style()
        self.style2.theme_use('clam')
        self.style2.configure("Combobox", background='red', foreground='#fff', font=('Verdana', 10),
                              fieldbackground='#f4f4f4')
        self.tree_pur.column('#0', width=0, stretch=NO)
        self.tree_pur.column('PurID', width=100)
        self.tree_pur.column('Company', width=300)
        self.tree_pur.column('Medname', width=300, anchor=CENTER)
        self.tree_pur.column('Cost', width=200, anchor=CENTER)
        self.tree_pur.column('Type', width=290, anchor=CENTER)
        self.tree_pur.column('Date', width=300, anchor=CENTER)

        self.tree_pur.heading('PurID', text='PurchaseID')
        self.tree_pur.heading('Company', text='Company-Name')
        self.tree_pur.heading('Medname', text='Medicine-name')
        self.tree_pur.heading('Cost', text='Cost')
        self.tree_pur.heading('Type', text='Type')
        self.tree_pur.heading('Date', text='Date')
        self._fetch_purchase()
        self.tree_pur.bind('<ButtonRelease-1>',self.selection_pur)

        mainloop()


    def find_pur(self, e):
        self.search_pur.config(state=NORMAL)
        self.search_pur.delete(0, END)
        self.search_pur.focus()

    def _find__pur(self, e):
        self.search_pur.config(state=NORMAL)
        self.search_pur.delete(0, END)
        self.search_pur.focus()

    def _Return_pur(self, e):
      if self.search_pur.get()=='':
          messagebox.showerror('ERR','Enter The ID You Want To Search')
      else:
          try:
              search = self.search_pur.get()
              conn = pyodbc.connect(
                  "Driver={SQL Server Native Client 11.0};"
                  "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
                  "Database=DaruShifa_Hospital;"
                  "Trusted_Connection=yes;"
              )
              cursor = conn.cursor()
              cursor.execute(f'select *from Purchase where PurID=?', (search))
              row = cursor.fetchone()
              if row != None:
                  for x in self.tree_pur.get_children():
                      self.tree_pur.delete(x)
                  self.tree_pur.insert('', END, values=(
                      row[0], row[1], row[2], row[3], row[4], row[5]
                  ))
              else:
                  messagebox.showerror('DaruShifa Hospital', 'No Record Was Found With that ID')

          except pyodbc.Error as err:
              sqlstate = err.args[1]
              sqlstate = sqlstate.split('.')
              # if sqlstate=='23000':
              messagebox.showerror(f'Error Occurred Code | {err.args[0]}', f'{sqlstate[1], sqlstate[2]}')

    def clock_pur(self):
        import time
        self.hour = time.strftime('%I')
        self.minutes = time.strftime('%M')
        self.secons = time.strftime('%S')
        self.satte = time.strftime('%p')
        self.clock.config(text=f'Time: {self.hour}:{self.minutes}:{self.secons} {self.satte}')
        self.clock.after(1000, self.clock_)

    # fetch purchase
    def _fetch_purchase(self):
        conn = pyodbc.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
            "Database=DaruShifa_Hospital;"
            "Trusted_Connection=yes;"
        )
        cursor = conn.cursor()
        cursor.execute('select *from Purchase')
        rows = cursor.fetchall()
        for row in rows:
            self.tree_pur.insert('', END, values=(
                row[0], row[1],row[2], row[3],row[4],row[5]
            ))

    # clear
    def clear_pur(self):
        self.purID.delete(0, END)
        self.company.delete(0, END)
        self.medname.delete(0, END)
        self.cost.delete(0, END)
        self.type.delete(0, END)
        self.date.delete(0, END)

    # add
    def add_purchase(self):
        # hos = HOSPITAL_SYSTEM.DARUL_SHIFA_HOSPITAL()
        if self.purID.get()=='' or self.company.get()=='' or self.medname.get()=='' or self.cost.get()=='' or self.type.get()=='' or self.date.get()=='':
            messagebox.showerror('DaruShifa_Hospital', 'All Fields Are required')
        else:
            try:
                conn = pyodbc.connect(
                    "Driver={SQL Server Native Client 11.0};"
                    "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
                    "Database=DaruShifa_Hospital;"
                    "Trusted_Connection=yes;"
                )
                cursor = conn.cursor()
                cursor.execute("INSERT INTO Purchase Values(?,?,?,?,?,?)",(
                    self.purID.get(),
                    self.company.get(),
                    self.medname.get(),
                    self.cost.get(),
                    self.type.get(),
                    self.date.get(),

                ))
                conn.commit()
                messagebox.showinfo('DaruShifa Hospital', f'Successful Added')
                self.tree_pur.delete(*self.tree_pur.get_children())
                self._fetch_purchase()
                self.show_counts()
            except pyodbc.Error as err:
                sqlstate=err.args[1]
                sqlstate=sqlstate.split('.')
                # if sqlstate=='23000':
                messagebox.showerror(f'Error Occurred', f'{sqlstate[2],sqlstate[3],sqlstate[4]}')
        # selection
    def selection_pur(self, e):
        item_selected = self.tree_pur.focus()
        selection_item = self.tree_pur.item(item_selected, 'values')
        self.clear_pur()
        # insert
        self.purID.insert(0, selection_item[0])
        self.company.insert(0, selection_item[1])
        self.medname.insert(0, selection_item[2])
        self.cost.insert(0,selection_item[3])
        self.type.insert(0, selection_item[4])
        self.date.insert(0, selection_item[5])

    # update
    def _update_pur(self):
        if self.purID.get()=='' or self.company.get()=='' or self.medname.get()=='' or self.cost.get()=='' or self.type.get()=='' or self.date.get()=='':
            messagebox.showerror('ERR', 'Plz Select The Purchase\nYou Want To Update')
        else:
            try:
                item = self.tree_pur.focus()
                selected = self.tree_pur.item(item, 'values')
                conn = pyodbc.connect(
                    "Driver={SQL Server Native Client 11.0};"
                    "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
                    "Database=DaruShifa_Hospital;"
                    "Trusted_Connection=yes;"
                )
                cursor = conn.cursor()
                cursor.execute(f'UPDATE Purchase set PurID=?,CompanyName=?,MedName=?,Cost=?,Type=?, Date_=? where PurID={selected[0]}',
                               (
                                   self.purID.get(),
                                   self.company.get(),
                                   self.medname.get(),
                                   self.cost.get(),
                                   self.type.get(),
                                   self.date.get()

                               ))
                conn.commit()
                messagebox.showinfo('DaruShifa Hospital', 'Purchase Updated Successfully')
                self.clear_pur()
                self.tree_pur.delete(*self.tree_pur.get_children())
                self._fetch_purchase()
            except pyodbc.Error as err:

                sqlstate = err.args[1]
                sqlstate = sqlstate.split('.')
                # if sqlstate=='23000':
                messagebox.showerror(f'Error Occurred', f'{sqlstate[2], sqlstate[3]}')
    # deleet
    def _deletion_purchase(self):
        if self.purID.get()=='' or self.company.get()=='' or self.medname.get()=='' or self.cost.get()=='' or self.type.get()=='' or self.date.get()=='':
            messagebox.showerror('ERR', 'Plz Select The Purchase\nYou Want To Delete')
        else:
            try:
                item = self.tree_pur.focus()
                selected = self.tree_pur.item(item, 'values')
                conn = pyodbc.connect(
                    "Driver={SQL Server Native Client 11.0};"
                    "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
                    "Database=DaruShifa_Hospital;"
                    "Trusted_Connection=yes;"
                )
                cursor = conn.cursor()
                ans = messagebox.askyesno('Confirm', f'Are You Sure To Delete \nThe Purchase ID {self.purID.get()}')
                if ans:
                    cursor.execute(f'DELETE Purchase where PurID={selected[0]}')
                    conn.commit()
                    messagebox.showinfo('DaruShifa Hospital', 'Purchase Was Deleted Successfully')
                    self.clear_pur()
                    self.tree_pur.delete(*self.tree_pur.get_children())
                    self._fetch_purchase()
                    self.show_counts()
                else:
                    pass
            except pyodbc.Error as err:
                sqlstate = err.args[1]
                sqlstate = sqlstate.split('.')
                # if sqlstate=='23000':
                messagebox.showerror(f'Error Occurred', f'{sqlstate[0], sqlstate[1]}')


    # bloods
    def __bloods__(self):
        self.screen = Toplevel()
        self.screen.focus_force()
        self.screen.geometry('500x470')
        self.screen.resizable(0, 0)
        self.screen.config(bg='white')
        self.screen.title('Bloods')
        # LABELS
        Label(self.screen, text='Manage Bloods', bg='#00008b', fg='white',
              font=('Verdana', 18, 'bold')).pack(fill=X)

        Label(self.screen, text='BloodID', bg='white', fg='black', font=('Verdana', 16, 'bold')).place(x=20, y=60)

        self.blid = Entry(self.screen, font=('Verdana', 16, 'bold'), bg='#f4f4f4', fg='black',
                           bd=3, relief='groove')
        self.blid.place(x=20, y=100, width=120)

        Label(self.screen, text='Blood-Type', bg='white', fg='black', font=('Verdana', 16, 'bold')).place(x=220, y=60)
        self.bldType = Entry(self.screen, font=('Verdana', 16, 'bold'), bg='#f4f4f4', fg='black',
                             bd=3, relief='groove')
        self.bldType.place(x=220, y=100, width=150)

        self.addBtn = Button(self.screen, text='Add', bg='#189', fg='white', font=('Verdana', 16, 'bold'),
                             bd=3, relief='sunken',command=self.add_bloods)
        self.addBtn.place(x=20, y=160)

        self.update = Button(self.screen, text='Update', bg='#189', fg='white', font=('Verdana', 16, 'bold'),
                             bd=3, relief='sunken',command=self._update_bloods)
        self.update.place(x=100, y=160)

        self.Delete = Button(self.screen, text='Delete', bg='#189', fg='white', font=('Verdana', 16, 'bold'),
                             bd=3, relief='sunken',command=self._deletion_bloods)
        self.Delete.place(x=230, y=160)
        # ===========================END LABLS==============

        # TREEVIEW STYLES
        self.style = ttk.Style()
        # style.configure("Treeview")

        self.data = ['A+', 'B+', 'AB', 'AB+', '0+', '0-']
        self.style.theme_use('clam')
        self.style.configure("Treeview", background='#f4f4f4', foreground='#fff', font=('Verdana', 10),
                             fieldbackground='#f4f4f4')
        self.data_frame = Frame(self.screen, bg='white', bd=3, relief='ridge', width=900, heigh=100)
        self.data_frame.place(x=40, y=230)

        self.scrollbar = Scrollbar(self.data_frame, orient=VERTICAL)


        self.tree_blood = ttk.Treeview(self.data_frame, columns=("BloodID", 'Blood-type'),
                                      yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.tree_blood.yview)
        self.scrollbar.pack(fill=Y, side=RIGHT)
        self.tree_blood.column('#0', width=0, stretch=NO)
        self.tree_blood.column("BloodID")
        self.tree_blood.column("Blood-type")
        self.tree_blood.heading("BloodID", text='BloodID')
        self.tree_blood.heading("Blood-type", text='Blood-Type')
        self.tree_blood.pack(fill=BOTH, expand=1)
        self._fetch_blood()
        self.tree_blood.bind('<ButtonRelease-1>',self.selection_bloods)


        # TREE-END========================
        # self.show()/

        mainloop()


    # fetching

    def _fetch_blood(self):
        conn = pyodbc.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
            "Database=DaruShifa_Hospital;"
            "Trusted_Connection=yes;"
        )
        cursor = conn.cursor()
        cursor.execute('select *from Bloods')
        rows = cursor.fetchall()
        for row in rows:
            self.tree_blood.insert('', END, values=(
                row[0], row[1]
            ))

    # clear
    def clear_bloods(self):
        self.blid.delete(0, END)
        self.bldType.delete(0, END)

    # add
    def add_bloods(self):
        # hos = HOSPITAL_SYSTEM.DARUL_SHIFA_HOSPITAL()
        if self.blid.get()=='' or self.bldType.get()=='':
            messagebox.showerror('DaruShifa_Hospital', 'All Fields Are required')
        else:
            try:
                conn = pyodbc.connect(
                    "Driver={SQL Server Native Client 11.0};"
                    "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
                    "Database=DaruShifa_Hospital;"
                    "Trusted_Connection=yes;"
                )
                cursor = conn.cursor()
                cursor.execute("INSERT INTO Bloods Values(?,?)",(
                    self.blid.get(),
                    self.bldType.get(),

                ))
                conn.commit()
                messagebox.showinfo('DaruShifa Hospital', f'Successful Added\nBlood [{self.bldType.get()}]')
                self.tree_blood.delete(*self.tree_blood.get_children())
                self._fetch_blood()
                self.show_counts()
            except pyodbc.Error as err:
                sqlstate=err.args[1]
                sqlstate=sqlstate.split('.')
                # if sqlstate=='23000':
                messagebox.showerror(f'Error Occurred', f'{sqlstate[2],sqlstate[3],sqlstate[4]}')

    # selection
    def selection_bloods(self, e):
        item_selected = self.tree_blood.focus()
        selection_item = self.tree_blood.item(item_selected, 'values')
        self.clear_bloods()
        # insert
        self.blid.insert(0, selection_item[0])
        self.bldType.insert(0, selection_item[1])

    # update
    def _update_bloods(self):
        if self.blid.get()=='' or self.bldType.get()=='':
            messagebox.showerror('ERR', 'Plz Select The Blood\nYou Want To Update')
        else:
            try:
                item = self.tree_blood.focus()
                selected = self.tree_blood.item(item, 'values')
                conn = pyodbc.connect(
                    "Driver={SQL Server Native Client 11.0};"
                    "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
                    "Database=DaruShifa_Hospital;"
                    "Trusted_Connection=yes;"
                )
                cursor = conn.cursor()
                cursor.execute(f'UPDATE Bloods set BloodID=?,BloodType=? where BloodID={selected[0]}',
                               (
                                   self.blid.get(),
                                   self.bldType.get(),

                               ))
                conn.commit()
                messagebox.showinfo('DaruShifa Hospital', 'Blood Updated Successfully')
                self.clear_bloods()
                self.tree_blood.delete(*self.tree_blood.get_children())
                self._fetch_blood()
            except pyodbc.Error as err:
                sqlstate = err.args[1]
                sqlstate = sqlstate.split('.')
                # if sqlstate=='23000':
                messagebox.showerror(f'Error Occurred', f'{sqlstate[2], sqlstate[3]}')

    # delete
    def _deletion_bloods(self):
        if self.blid.get()=='' or self.bldType.get()=='':
            messagebox.showerror('ERR', 'Plz Select The Blood\nYou Want To Delete')
        else:
            try:
                item = self.tree_blood.focus()
                selected = self.tree_blood.item(item, 'values')
                conn = pyodbc.connect(
                    "Driver={SQL Server Native Client 11.0};"
                    "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
                    "Database=DaruShifa_Hospital;"
                    "Trusted_Connection=yes;"
                )
                cursor = conn.cursor()
                ans = messagebox.askyesno('Confirm', f'Are You Sure To Delete \nThe Blood {self.bldType.get()}')
                if ans:
                    cursor.execute(f'DELETE Bloods where BloodID={selected[0]}')
                    conn.commit()
                    messagebox.showinfo('DaruShifa Hospital', 'Blood Was Deleted Successfully')
                    self.clear_bloods()
                    self.tree_blood.delete(*self.tree_blood.get_children())
                    self._fetch_blood()
                    self.show_counts()
                else:
                    pass
            except pyodbc.Error as err:
                sqlstate = err.args[1]
                sqlstate = sqlstate.split('.')
                # if sqlstate=='23000':
                messagebox.showerror(f'Error Occurred', f'{sqlstate[0], sqlstate[1]}')

    # reports
    def __report__(self):
        self.screen = Toplevel()
        self.screen.focus_force()
        self.screen.geometry('590x480')
        self.screen.resizable(0, 0)
        self.screen.config(bg='white')
        self.screen.title('Rooms')
        # LABELS
        Label(self.screen, text='Manage Reports', bg='#00008b', fg='white',
              font=('Verdana', 18, 'bold')).pack(fill=X)

        Label(self.screen, text='ReportID', bg='white', fg='black', font=('Verdana', 16, 'bold')).place(x=20, y=60)

        self.rid = Entry(self.screen, font=('Verdana', 16, 'bold'), bg='#f4f4f4', fg='black',
                            bd=3, relief='groove')
        self.rid.place(x=20, y=100, width=120)

        Label(self.screen, text='PurID', bg='white', fg='black', font=('Verdana', 16, 'bold')).place(x=220, y=60)
        self.pur_lists=[]
        self.fetch_purid()
        self.pur_var=StringVar()
        self.pur_var.set('Select')
        self.purid = ttk.Combobox(self.screen,textvariable=self.pur_var,
                                  font=('Verdana', 13, 'bold'),
                             value=self.pur_lists)
        self.purid.place(x=220, y=100, width=100)
        self.purid['state']='readonly'

        Label(self.screen, text='Date', bg='white', fg='black', font=('Verdana', 16, 'bold')).place(x=420, y=60)
        self.date = Entry(self.screen, font=('Verdana', 16, 'bold'), bg='#f4f4f4', fg='black',
                            bd=3, relief='groove')
        self.date.place(x=420, y=100, width=150)

        self.addBtn = Button(self.screen, text='Add', bg='#189', fg='white', font=('Verdana', 16, 'bold'),
                             bd=3, relief='sunken',command=self.add_report)
        self.addBtn.place(x=20, y=160)

        self.update = Button(self.screen, text='Update', bg='#189', fg='white', font=('Verdana', 16, 'bold'),
                             bd=3, relief='sunken',command=self._update_reports)
        self.update.place(x=100, y=160)

        self.Delete = Button(self.screen, text='Delete', bg='#189', fg='white', font=('Verdana', 16, 'bold'),
                             bd=3, relief='sunken',command=self._deletion_report)
        self.Delete.place(x=230, y=160)
        # ===========================END LABLS==============

        # TREEVIEW STYLES
        self.style = ttk.Style()
        # style.configure("Treeview")


        self.style.theme_use('clam')
        self.style.configure("Treeview", background='#f4f4f4', foreground='#fff', font=('Verdana', 10),
                             fieldbackground='#f4f4f4')
        self.data_frame = Frame(self.screen, bg='white', bd=3, relief='ridge', width=900, heigh=100)
        self.data_frame.place(x=0, y=230)

        self.scrollbar = Scrollbar(self.data_frame, orient=VERTICAL)


        self.tree_report = ttk.Treeview(self.data_frame, columns=("ReportID", 'PurID', 'Date'),
                                      yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.tree_report.yview)
        self.scrollbar.pack(fill=Y, side=RIGHT)
        self.tree_report.column('#0', width=0, stretch=NO)
        self.tree_report.column("ReportID", width=120)
        self.tree_report.column("PurID", width=200)
        self.tree_report.column("Date", width=240)
        self.tree_report.heading("ReportID", text='ReportID')
        self.tree_report.heading("PurID", text='PurchaseID')
        self.tree_report.heading("Date", text='Date')
        self.tree_report.pack(fill=BOTH, expand=1)
        self._fetch__reports()
        self.tree_report.bind('<ButtonRelease-1>',self.selection_reports)
        # TREE-END========================
        # self.show()/

        mainloop()

    #fetching purid
    def fetch_purid(self):
        conn = pyodbc.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
            "Database=DaruShifa_Hospital;"
            "Trusted_Connection=yes;"
        )
        cursor = conn.cursor()
        cursor.execute('select *from Purchase')
        rows = cursor.fetchall()
        for row in rows:
            self.pur_lists.append(row[0])

    # fetching data
    def _fetch__reports(self):
        conn = pyodbc.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
            "Database=DaruShifa_Hospital;"
            "Trusted_Connection=yes;"
        )
        cursor = conn.cursor()
        cursor.execute('select *from Reports')
        rows = cursor.fetchall()
        for row in rows:
            self.tree_report.insert('', END, values=(
                row[0], row[1],row[2]
            ))

    # clera
    def clear_reports(self):
        self.rid.delete(0, END)
        self.pur_var.set('Select')
        self.date.delete(0, END)


    # add
    def add_report(self):
        # hos = HOSPITAL_SYSTEM.DARUL_SHIFA_HOSPITAL()
        if self.rid.get()=='' or self.pur_var.get()=='Select' or self.date.get()=='' :
            messagebox.showerror('DaruShifa_Hospital', 'All Fields Are required')
        else:
            try:
                conn = pyodbc.connect(
                    "Driver={SQL Server Native Client 11.0};"
                    "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
                    "Database=DaruShifa_Hospital;"
                    "Trusted_Connection=yes;"
                )
                cursor = conn.cursor()
                cursor.execute("INSERT INTO Reports Values(?,?,?)",(
                    self.rid.get(),
                    self.pur_var.get(),
                    self.date.get()


                ))
                conn.commit()
                messagebox.showinfo('DaruShifa Hospital', f'Successful Added\nReport')
                self.clear_reports()
                self.tree_report.delete(*self.tree_report.get_children())
                self._fetch__reports()
                self.show_counts()
            except pyodbc.Error as err:

                sqlstate=err.args[1]
                sqlstate=sqlstate.split('.')
                # if sqlstate=='23000':
                messagebox.showerror(f'Error Occurred', f'{sqlstate[2],sqlstate[3],sqlstate[4]}')

    # selection
    def selection_reports(self, e):
        item_selected = self.tree_report.focus()
        selection_item = self.tree_report.item(item_selected, 'values')
        self.clear_reports()
        # insert
        self.rid.insert(0, selection_item[0])
        self.pur_var.set(str(selection_item[1]))
        self.date.insert(0, selection_item[2])

      # updare
    def _update_reports(self):
        if self.rid.get()=='' or self.pur_var.get()=='Select' or self.date.get()=='' :
            messagebox.showerror('ERR', 'Plz Select The Reports\nYou Want To Update')
        else:
            try:
                item = self.tree_report.focus()
                selected = self.tree_report.item(item, 'values')
                conn = pyodbc.connect(
                    "Driver={SQL Server Native Client 11.0};"
                    "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
                    "Database=DaruShifa_Hospital;"
                    "Trusted_Connection=yes;"
                )
                cursor = conn.cursor()
                cursor.execute(f'UPDATE Reports set ReportID=?,PurID=?,Date_=?  where ReportID={selected[0]}',
                               (
                                   self.rid.get(),
                                   self.pur_var.get(),
                                   self.date.get(),

                               ))
                conn.commit()
                messagebox.showinfo('DaruShifa Hospital', 'Report Updated Successfully')
                self.clear_reports()
                self.tree_report.delete(*self.tree_report.get_children())
                self._fetch__reports()
            except pyodbc.Error as err:
                sqlstate = err.args[1]
                sqlstate = sqlstate.split('.')
                # if sqlstate=='23000':
                messagebox.showerror(f'Error Occurred', f'{sqlstate[2], sqlstate[3]}')

    # deletion
    def _deletion_report(self):
        if self.rid.get()=='' or self.pur_var.get()=='Select' or self.date.get()=='' :
            messagebox.showerror('ERR', 'Plz Select The Report\nYou Want To Delete')
        else:
            try:
                item = self.tree_report.focus()
                selected = self.tree_report.item(item, 'values')
                conn = pyodbc.connect(
                    "Driver={SQL Server Native Client 11.0};"
                    "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
                    "Database=DaruShifa_Hospital;"
                    "Trusted_Connection=yes;"
                )
                cursor = conn.cursor()
                ans = messagebox.askyesno('Confirm', f'Are You Sure To Delete This Report? ')
                if ans:
                    cursor.execute(f'DELETE Reports where ReportID={selected[0]}')
                    conn.commit()
                    messagebox.showinfo('DaruShifa Hospital', 'Report Was Deleted Successfully')
                    self.clear_reports()
                    self.tree_report.delete(*self.tree_report.get_children())
                    self._fetch__reports()
                    self.show_counts()
                else:
                    pass
            except pyodbc.Error as err:
                sqlstate = err.args[1]
                sqlstate = sqlstate.split('.')
                # if sqlstate=='23000':
                messagebox.showerror(f'Error Occurred', f'{sqlstate[0], sqlstate[1]}')


    # taking medicine
    def taking_medcine(self):
        self.TakMedicine = Toplevel()
        # self.TakMedicine.geometry('1100x740+30+20')
        self.TakMedicine.state('zoomed')
        self.TakMedicine.focus_force()
        self.TakMedicine.title('TakMedicines')
        self.TakMedicine.resizable(0, 0)
        self.TakMedicine.config(bg='#fff')
        # self.TakMedicine.iconbitmap('logo.ico')

        # TakMedicine
        Label(self.TakMedicine, text='DARUL-SHIFA HOSPITAL | MANAGE TAKING MEDICINES', bg='#015', fg='white', bd=3,
              relief='flat',
              font=('Verdana', 20, 'bold'), height=2).pack(fill=X)
        self.clock = Label(self.TakMedicine, bg='#015', fg='white', bd=3, relief='flat',
                           font=('Verdana', 18, 'bold'), height=2)
        self.clock.place(x=0, y=0)
        self.clock_()

        # image
        self.log = Image.open('icons/lg.png')
        self.resizing = self.log.resize((60, 60), Image.ANTIALIAS)
        self.new_icon = ImageTk.PhotoImage(self.resizing)
        self.lb = Label(self.TakMedicine, bg='#015', image=self.new_icon, bd=0)
        self.lb.place(x=330, y=5)

        Label(self.TakMedicine, text='TAKES_ID', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=10, y=100)
        self.takID = Entry(self.TakMedicine, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                           bd=4, relief='sunken', width=10)
        self.takID.place(x=10, y=150)

        # TakMedicine name
        Label(self.TakMedicine, text='MedID', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=10, y=200)

        self.medVar = StringVar()
        self.medVar.set('MedID')
        self.lists4 = ['Get', 'Normal', 'ITS']
        self.medID = ttk.Combobox(self.TakMedicine, value=self.lists4, textvariable=self.medVar,
                                  font=('Verdana', 15, 'bold'), justify=CENTER)
        self.medID.place(x=10, y=250, width=180)
        self.medID['state'] = 'readonly'

        # price
        Label(self.TakMedicine, text='PatID', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=10, y=300)
        self.patID_VAR = StringVar()
        self.patID_VAR.set('PatientID')
        self.lists3 = ['Get', 'Normal', 'ITS']
        self.patID = ttk.Combobox(self.TakMedicine, value=self.lists3, textvariable=self.patID_VAR,
                                  font=('Verdana', 15, 'bold'), justify=CENTER)
        self.patID.place(x=10, y=350, width=180)
        self.patID['state'] = 'readonly'

        # quantity
        Label(self.TakMedicine, text='Quantity', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=320, y=100)
        self.qttvar = IntVar()
        self.qty = Spinbox(self.TakMedicine, textvariable=self.qttvar, from_=1, to=100, bg='#c0b6ff', fg='black',
                           font=('Verdana', 15, 'bold'),
                           bd=4, relief='sunken', width=9)
        self.qty.place(x=320, y=150)

        # address
        Label(self.TakMedicine, text='Price', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=320, y=200)
        self.price = Entry(self.TakMedicine, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                           bd=4, relief='sunken', width=10)
        self.price.place(x=320, y=250)

        Label(self.TakMedicine, text='Date', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=320, y=300)
        self.date = Entry(self.TakMedicine, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                          bd=4, relief='sunken', width=10)
        self.date.place(x=320, y=350)

        # baner

        self.banner_img = Image.open('images/female-nurse.jpg')
        self.res = self.banner_img.resize((650, 600), Image.ANTIALIAS)
        self.baner = ImageTk.PhotoImage(self.res)
        Label(self.TakMedicine, image=self.baner, bg='white', bd=0).place(x=980, y=120)

        # shifts

        # Buttons
        self.add_btn = Button(self.TakMedicine, text='Add', bg='#019', fg='white',
                              bd=7, relief='ridge', font=('Verdana', 18, 'bold'),
                              )
        self.add_btn.place(x=190, y=420)

        self.update_btn = Button(self.TakMedicine, text='Update', bg='#019', fg='white',
                                 bd=7, relief='ridge', font=('Verdana', 18, 'bold')
                                 )
        self.update_btn.place(x=290, y=420)

        self.dele = Button(self.TakMedicine, text='Delete', bg='#019', fg='white',
                           bd=7, relief='ridge', font=('Verdana', 18, 'bold'))

        self.dele.place(x=445, y=420)


        self.search_takmed = Entry(self.TakMedicine, bg='#fff', fg='#019', font=('Verdana', 15, 'bold'),
                            bd=4, relief='ridge', width=15)
        self.search_takmed.place(x=1290, y=15)
        self.TakMedicine.bind('<Control-f>', self._find_tak)
        self.search_takmed.bind('<Button-1>', self._find_tak)
        self.search_takmed.bind('<Return>', self._Return_tak)
        self.takID.focus()

        self.search_takmed.insert(0, 'TakesID')
        self.search_takmed.config(state=DISABLED)

        # tree-view table

        self.frame_tree = Frame(self.TakMedicine, bg='white', width=1090, bd=3, relief='groove')
        self.frame_tree.place(x=5, y=600)
        scrollbar = Scrollbar(self.frame_tree, orient=VERTICAL)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.tree_takmed = ttk.Treeview(self.frame_tree, yscrollcommand=scrollbar.set,
                                 columns=('TakesID', 'MedID', 'PatientID', 'QTTY', 'Price', 'Date'))
        self.tree_takmed.pack(fill=BOTH, expand=True)
        # self.tree.bind('<ButtonRelease-1>',self.select)
        scrollbar.config(command=self.tree_takmed.yview)
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("Treeview", background='#f4f4f4', foreground='#fff', font=('Verdana', 10),
                             fieldbackground='#f4f4f4')

        self.style2 = ttk.Style()
        self.style2.theme_use('clam')
        self.style2.configure("Combobox", background='red', foreground='#fff', font=('Verdana', 10),
                              fieldbackground='#f4f4f4')
        self.tree_takmed.column('#0', width=0, stretch=NO)
        self.tree_takmed.column('TakesID', width=100)
        self.tree_takmed.column('MedID', width=240)
        self.tree_takmed.column('PatientID', width=210, anchor=CENTER)
        self.tree_takmed.column('QTTY', width=320, anchor=CENTER)
        self.tree_takmed.column('Price', width=240, anchor=CENTER)
        self.tree_takmed.column('Date', width=400, anchor=CENTER)

        self.tree_takmed.heading('TakesID', text='TakesID')
        self.tree_takmed.heading('MedID', text='MedID')
        self.tree_takmed.heading('PatientID', text='PatientID')
        self.tree_takmed.heading('QTTY', text='QTTY')
        self.tree_takmed.heading('Price', text='Price')
        self.tree_takmed.heading('Date', text='Date')

        mainloop()
        #
        # def add(self):
        #     self.tree.insert('',END,values=(self.drid.get(),self.drname.get(),self.age.get(),self.mobile.get(),self.email.get(),self.gender_var.get(),self.address.get(),self.specialist.get(),self.salary.get(),self.shift_var.get(),self.dep_var.get()))

    def find_tak(self, e):
        self.search_takmed.config(state=NORMAL)
        self.search_takmed.delete(0, END)
        self.search_takmed.focus()

    def _find_tak(self, e):
        self.search_takmed.config(state=NORMAL)
        self.search_takmed.delete(0, END)
        self.search_takmed.focus()

    def _Return_tak(self, e):

        messagebox.showinfo('INFO', f'QTY {self.search_takmed.get()}', parent=self.TakMedicine)

    def clock_tak(self):
        import time
        self.hour = time.strftime('%I')
        self.minutes = time.strftime('%M')
        self.secons = time.strftime('%S')
        self.satte = time.strftime('%p')
        self.clock.config(text=f'Time: {self.hour}:{self.minutes}:{self.secons} {self.satte}')
        self.clock.after(1000, self.clock_)


    # end taking mecine

    # lab diagnose
    def diagnose(self):
        self.Diagnose=Tk()
        # self.product.geometry('1100x740+30+20')
        # self.Diagnose.state('zoomed')
        self.Diagnose.geometry('1280x500')
        self.Diagnose.focus_force()
        self.Diagnose.title('Diagnoses')
        self.Diagnose.resizable(0,0)
        self.Diagnose.config(bg='#fff')
        # self.Diagnose.iconbitmap('logo.ico')




        # Diagnose
        Label(self.Diagnose,text='DARUL-SHIFA HOSPITAL | MANAGE DIAGNOSE',bg='#657',fg='white',bd=3,relief='flat',
              font=('Verdana',20,'bold'),height=2).pack(fill=X)


        Label(self.Diagnose,text='DiagnoseID',bg='white',fg='#6c63ff',font=('Verdana',19,'bold')
              ).place(x=10,y=100)
        self.diagID=Entry(self.Diagnose,bg='#c0b6ff',fg='black',font=('Verdana',15,'bold'),
                         bd=4,relief='sunken',width=10)
        self.diagID.place(x=10,y=150)

        # Diagnose name
        # 10 250/
        Label(self.Diagnose,text='PatienID',bg='white',fg='#6c63ff',font=('Verdana',19,'bold')
              ).place(x=10,y=200)
        self.pat_id_list = [1, 2, 3]
        self.pat_id_var_diag = StringVar()
        self.pat_id_var_diag.set('Select')
        self.pat_list = ttk.Combobox(self.Diagnose, textvariable=self.pat_id_var_diag,value=self.pat_id_list,
                                      font=('Verdana', 15, 'bold'), justify=CENTER)
        self.pat_list.place(x=10, y=250, width=130)
        # self.pat_id_var_diag.set('Select')
        self.pat_list['state']='readonly'


        # price

        Label(self.Diagnose,text='Test-Type',bg='white',fg='#6c63ff',font=('Verdana',19,'bold')
              ).place(x=10,y=300)
        self.test_type = Entry(self.Diagnose, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                          bd=4, relief='sunken', width=10)
        self.test_type.place(x=10, y=350)

        # quantity
        Label(self.Diagnose, text='Result', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=10, y=390)
        self.result = Entry(self.Diagnose, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                           bd=4, relief='sunken', width=10)
        self.result.place(x=10, y=440)


        # Buttons
        self.add_btn=Button(self.Diagnose,text='Add',bg='#019',fg='white',
                            bd=7,relief='flat',font=('Verdana',18,'bold'),
                            command=self.add_diagn)
        self.add_btn.place(x=400,y=430,width=120)

        self.update_btn = Button(self.Diagnose, text='Update', bg='#019', fg='white',
                              bd=7, relief='flat', font=('Verdana', 18, 'bold')
                                 )
        self.update_btn.place(x=540, y=430)

        self.dele = Button(self.Diagnose, text='Delete', bg='#019', fg='white',
                              bd=7, relief='flat', font=('Verdana', 18, 'bold'))

        self.dele.place(x=700, y=430)

        # self.search = Button(self.Diagnose, text='Delete', bg='#019', fg='white',
        #                    bd=7, relief='ridge', font=('Verdana', 18, 'bold'), command=self.Delete)
        #
        # self.search.place(x=445, y=420)

        self.search_diag = Entry(self.Diagnose, bg='#fff', fg='#019', font=('Verdana', 15, 'bold'),
                          bd=4, relief='ridge', width=14)
        self.search_diag.place(x=1060, y=15)
        # self.Diagnose.bind('<Control-f>',self.find)
        # self.Diagnose.bind('<Button-1>',self._find_)
        # self.Diagnose.bind('<Return>',self._Return_)
        # self.drid.focus()

        self.search_diag.insert(0,'Search')
        self.search_diag.config(state=DISABLED)




        # tree-view table


        self.frame_tree=Frame(self.Diagnose,bg='white',width=1090,bd=3,relief='groove')
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
    def add_diagn(self):
        pass
    #     self.tree.insert('',END,values=(self.drid.get(),self.drname.get(),self.age.get(),self.mobile.get(),self.email.get(),self.gender_var.get(),self.address.get(),self.specialist.get(),self.salary.get(),self.shift_var.get(),self.dep_var.get()))


    def find_diag(self,e):
        self.search_diag.config(state=NORMAL)
        self.search_diag.delete(0,END)
        self.search_diag.focus()

    def _find_diag(self, e):
        self.search_diag.config(state=NORMAL)
        self.search_diag.delete(0, END)
        self.search_diag.focus()

    def _Return_diag(self, e):
        messagebox.showinfo('INFO', f'You Write {self.search_diag.get()}', parent=self.Diagnose)




    # fetch labdiag


    # fetch patieID

    #clear

    # add

    # selection

    #update

    # delete




    # end diagnose


    # shifts
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

        self.shiftID=Entry(self.screen,font=('Verdana',16,'bold'),bg='#f4f4f4',fg='black',
                    bd=3,relief='groove')
        self.shiftID.place(x=20,y=100,width=120)

        Label(self.screen, text='ShiftType', bg='white', fg='black', font=('Verdana', 16, 'bold')).place(x=220, y=60)
        self.shiftType = Entry(self.screen, font=('Verdana', 16, 'bold'), bg='#f4f4f4', fg='black',
                      bd=3, relief='groove')
        self.shiftType.place(x=220, y=100, width=150)





        self.addBtn=Button(self.screen,text='Add',bg='#189',fg='white',font=('Verdana', 16, 'bold'),
                      bd=3,relief='sunken',command=self.add_shifts)
        self.addBtn.place(x=20,y=160)

        self.update=Button(self.screen,text='Update',bg='#189',fg='white',font=('Verdana', 16, 'bold'),
                      bd=3,relief='sunken',command=self._update_shift)
        self.update.place(x=100,y=160)

        self.Delete=Button(self.screen,text='Delete',bg='#189',fg='white',font=('Verdana', 16, 'bold'),
                      bd=3,relief='sunken',command=self._deletion_shifts)
        self.Delete.place(x=230,y=160)
        # ===========================END LABLS==============

        # TREEVIEW STYLES
        self.style=ttk.Style()
        # style.configure("Treeview")


        self.style.theme_use('clam')
        self.style.configure("Treeview", background='#f4f4f4', foreground='#fff', font=('Verdana', 10),
                        fieldbackground='#f4f4f4')
        self.data_frame=Frame(self.screen,bg='white',bd=3,relief='ridge',width=900,heigh=100)
        self.data_frame.place(x=0,y=230)

        self.scrollbar=Scrollbar(self.data_frame,orient=VERTICAL)


        self.tree_shifts=ttk.Treeview(self.data_frame,columns=("shiftID",'shiftType'),yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.tree_shifts.yview)
        self.scrollbar.pack(fill=Y,side=RIGHT)
        self.tree_shifts.column('#0',width=0,stretch=NO)
        self.tree_shifts.column("shiftID",width=120)
        self.tree_shifts.column("shiftType",width=266)

        self.tree_shifts.heading("shiftID",text='ShiftID')
        self.tree_shifts.heading("shiftType",text='ShiftType')

        self.tree_shifts.pack(fill=BOTH,expand=1)
        self.tree_shifts.bind('<ButtonRelease-1>',self.selection_shifts)
        self._fetch_shifts()




        mainloop()




    # fetching shifts
    def _fetch_shifts(self):
        conn = pyodbc.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
            "Database=DaruShifa_Hospital;"
            "Trusted_Connection=yes;"
        )
        cursor = conn.cursor()
        cursor.execute('select *from Shifts')
        rows = cursor.fetchall()
        for row in rows:
            self.tree_shifts.insert('', END, values=(
                row[0], row[1]
            ))

    # clear shifts
    def clear_shifts(self):
        self.shiftID.delete(0, END)
        self.shiftType.delete(0, END)



    # add Event
    def add_shifts(self):
        # hos = HOSPITAL_SYSTEM.DARUL_SHIFA_HOSPITAL()
        if self.shiftID.get()=='' or self.shiftType.get()=='':
            messagebox.showerror('DaruShifa_Hospital', 'All Fields Are required')
        else:
            try:
                conn = pyodbc.connect(
                    "Driver={SQL Server Native Client 11.0};"
                    "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
                    "Database=DaruShifa_Hospital;"
                    "Trusted_Connection=yes;"
                )
                cursor = conn.cursor()
                cursor.execute("INSERT INTO Shifts Values(?,?)",(
                    self.shiftID.get(),
                    self.shiftType.get(),

                ))
                conn.commit()
                messagebox.showinfo('DaruShifa Hospital', f'Successful Added\nShifts [{self.shiftType.get()}]')
                self.clear_shifts()
                self.tree_shifts.delete(*self.tree_shifts.get_children())
                self._fetch_shifts()
                self.show_counts()
            except pyodbc.Error as err:
                sqlstate=err.args[1]
                sqlstate=sqlstate.split('.')
                # if sqlstate=='23000':
                messagebox.showerror(f'Error Occurred', f'{sqlstate[2],sqlstate[3],sqlstate[4]}')
    # selection
    def selection_shifts(self, e):
        item_selected = self.tree_shifts.focus()
        selection_item = self.tree_shifts.item(item_selected, 'values')
        self.clear_shifts()
        # insert
        self.shiftID.insert(0, selection_item[0])
        self.shiftType.insert(0, selection_item[1])


    # update
    def _update_shift(self):
        if self.shiftID.get()=='' or self.shiftType.get()=='':
            messagebox.showerror('ERR', 'Plz Select The Shift\nYou Want To Update')
        else:
            try:
                item = self.tree_shifts.focus()
                selected = self.tree_shifts.item(item, 'values')
                conn = pyodbc.connect(

                    "Driver={SQL Server Native Client 11.0};"
                    "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
                    "Database=DaruShifa_Hospital;"
                    "Trusted_Connection=yes;"
                )
                cursor = conn.cursor()
                cursor.execute(f'UPDATE Shifts set ShiftID=?,ShiftType=? where ShiftID={selected[0]}',
                               (
                                   self.shiftID.get(),
                                   self.shiftType.get()

                               ))
                conn.commit()
                messagebox.showinfo('DaruShifa Hospital', 'Shift Updated Successfully')
                self.clear_shifts()
                self.tree_shifts.delete(*self.tree_shifts.get_children())
                self._fetch_shifts()
            except pyodbc.Error as err:
                sqlstate = err.args[1]
                sqlstate = sqlstate.split('.')
                # if sqlstate=='23000':
                messagebox.showerror(f'Error Occurred', f'{sqlstate[2], sqlstate[3]}')


    # delete
    def _deletion_shifts(self):
        if self.shiftID.get()=='' or self.shiftType.get()=='':
            messagebox.showerror('ERR', 'Plz Select The Shift\nYou Want To Delete')
        else:
            try:
                item = self.tree_shifts.focus()
                selected = self.tree_shifts.item(item, 'values')
                conn = pyodbc.connect(
                    "Driver={SQL Server Native Client 11.0};"
                    "Server= DESKTOP-N9PT8FH\SQLEXPRESS;"
                    "Database=DaruShifa_Hospital;"
                    "Trusted_Connection=yes;"
                )
                cursor = conn.cursor()
                ans = messagebox.askyesno('Confirm', f'Are You Sure To Delete This Shift')
                if ans:
                    cursor.execute(f'DELETE Shifts where ShiftID={selected[0]}')
                    conn.commit()
                    messagebox.showinfo('DaruShifa Hospital', 'Shift Was Deleted Successfully')
                    self.clear_shifts()
                    self.tree_shifts.delete(*self.tree_shifts.get_children())
                    self._fetch_shifts()
                    self.show_counts()
                else:
                    pass
            except pyodbc.Error as err:
                sqlstate = err.args[1]
                sqlstate = sqlstate.split('.')
                # if sqlstate=='23000':
                messagebox.showerror(f'Error Occurred', f'{sqlstate[0], sqlstate[1]}')

    #end shifts


    # inpatient
    def inpatient(self):
        self.IP = Toplevel()
        # self.product.geometry('1100x740+30+20')
        self.IP.state('zoomed')
        self.IP.focus_force()
        self.IP.title('InPatients')
        self.IP.resizable(0, 0)
        self.IP.config(bg='#fff')
        # self.IP.iconbitmap('logo.ico')

        # IP
        Label(self.IP, text='DARUL-SHIFA HOSPITAL | MANAGE IP', bg='#127', fg='white', bd=3, relief='flat',
              font=('Verdana',20, 'bold'), height=2).pack(fill=X)
        self.clock = Label(self.IP, bg='#127', fg='white', bd=3, relief='flat',
                           font=('Verdana', 18, 'bold'), height=2)
        self.clock.place(x=0, y=0)
        self.clock_()

        # image
        self.log = Image.open('icons/lg.png')
        self.resizing = self.log.resize((60, 60), Image.ANTIALIAS)
        self.new_icon = ImageTk.PhotoImage(self.resizing)
        self.lb = Label(self.IP, bg='#127', image=self.new_icon, bd=0)
        self.lb.place(x=330, y=5)

        Label(self.IP, text='IPID', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=10, y=100)
        self.ipID = Entry(self.IP, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                          bd=4, relief='sunken', width=10)
        self.ipID.place(x=10, y=150)

        # IP name
        self.pat_list_p = [1, 2]
        self.pat_var_p = StringVar()
        self.pat_var_p.set('Select')
        Label(self.IP, text='PatientID', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=10, y=200)
        self.pat_id = ttk.Combobox(self.IP, textvariable=self.pat_var_p, value=self.pat_list_p,
                                   font=('Verdana', 15, 'bold'), justify=CENTER)
        self.pat_id.place(x=10, y=250, width=130)
        self.pat_id['state'] = 'readonly'

        # price
        self.dag_list = [1, 2]
        self.diag_var = StringVar()
        self.diag_var.set('Select')
        Label(self.IP, text='DiagnoseID', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=10, y=300)
        self.diagid = ttk.Combobox(self.IP, textvariable=self.diag_var, value=self.dag_list,
                                   font=('Verdana', 15, 'bold'), justify=CENTER)
        self.diagid.place(x=10, y=350, width=130)
        self.diagid['state'] = 'readonly'

        # quantitys
        self.tak_list = [1, 2]
        self.tak_var = StringVar()
        self.tak_var.set('Select')
        Label(self.IP, text='TakeMedID', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=320, y=100)
        self.Takid = ttk.Combobox(self.IP, textvariable=self.tak_var, value=self.tak_list,
                                  font=('Verdana', 15, 'bold'), justify=CENTER)
        self.Takid.place(x=320, y=150, width=130)
        self.Takid['state'] = 'readonly'

        # baner

        self.banner_img = Image.open('images/female-nurse.jpg')
        self.res = self.banner_img.resize((650, 600), Image.ANTIALIAS)
        self.baner = ImageTk.PhotoImage(self.res)
        Label(self.IP, image=self.baner, bg='white', bd=0).place(x=980, y=120)

        # shifts
        Label(self.IP, text='Date Out', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=550, y=100)
        self.date_admin = Entry(self.IP, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                                bd=4, relief='sunken', width=10)
        self.date_admin.place(x=550, y=150)

        # self.shifts.config(background='red')

        # Date
        Label(self.IP, text='RoomID', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=320, y=200)
        self.r_list = [1, 2]
        self.r_var = StringVar()
        self.r_var.set('Select')
        self.rid = ttk.Combobox(self.IP, textvariable=self.r_var, value=self.r_list,
                                font=('Verdana', 15, 'bold'), justify=CENTER)
        self.rid.place(x=320, y=250, width=130)
        self.rid['state'] = 'readonly'

        # Departs
        Label(self.IP, text='No-OfDays', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=550, y=200)
        self.nodays = Entry(self.IP, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                            bd=4, relief='sunken', width=12)
        self.nodays.place(x=550, y=250)

        # sALARAY
        # Label(self.IP, text='Salary', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
        #       ).place(x=650, y=300)
        # self.salary = Entry(self.IP, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
        #                         bd=4, relief='sunken', width=10)
        # self.salary.place(x=650, y=350)

        Label(self.IP, text='Date Admis', bg='white', fg='#6c63ff', font=('Verdana', 19, 'bold')
              ).place(x=320, y=300)
        self.date_admin = Entry(self.IP, bg='#c0b6ff', fg='black', font=('Verdana', 15, 'bold'),
                                bd=4, relief='sunken', width=13)
        self.date_admin.place(x=320, y=350)

        # Buttons
        self.add_btn = Button(self.IP, text='Add', bg='#019', fg='white',
                              bd=7, relief='sunken', font=('Verdana', 18, 'bold'),
                              command=self.add)
        self.add_btn.place(x=190, y=420)

        self.update_btn = Button(self.IP, text='Update', bg='#019', fg='white',
                                 bd=7, relief='sunken', font=('Verdana', 18, 'bold')
                                 )
        self.update_btn.place(x=290, y=420)

        self.dele = Button(self.IP, text='Delete', bg='#019', fg='white',
                           bd=7, relief='sunken', font=('Verdana', 18, 'bold'))

        self.dele.place(x=445, y=420)

        # self.search = Button(self.IP, text='Delete', bg='#019', fg='white',
        #                    bd=7, relief='ridge', font=('Verdana', 18, 'bold'), command=self.Delete)
        #
        # self.search.place(x=445, y=420)

        self.search_ip = Entry(self.IP, bg='#fff', fg='#019', font=('Verdana', 15, 'bold'),
                            bd=4, relief='ridge', width=15)
        self.search_ip.place(x=1290, y=15)
        # self.IP.bind('<Control-f>',self.find)
        # self.IP.bind('<Button-1>',self._find_)
        # self.IP.bind('<Return>',self._Return_)
        # self.drid.focus()

        self.search_ip.insert(0, 'Search')
        self.search_ip.config(state=DISABLED)

        # tree-view table
        self.key_binding=[
            {
                "key_1" : "23AP",
                "key_2" : "25AD"
            }
        ]
        self.frame_tree = Frame(self.IP, bg='white', width=1090, bd=3, relief='groove')
        self.frame_tree.place(x=5, y=600)
        scrollbar = Scrollbar(self.frame_tree, orient=VERTICAL)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.tree_ip = ttk.Treeview(self.frame_tree, yscrollcommand=scrollbar.set,
                                    columns=(
                                    'IPID', 'PatientID', 'DiagnoseID', 'TakmedID', 'RoomID', 'DateAdmis', 'DateOut',
                                    'NoOfDays'))
        self.tree_ip.pack(fill=BOTH, expand=True)
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
        self.tree_ip.column('#0', width=0, stretch=NO)
        self.tree_ip.column('IPID', width=80)
        self.tree_ip.column('PatientID', width=220)
        self.tree_ip.column('DiagnoseID', width=90, anchor=CENTER)
        self.tree_ip.column('TakmedID', width=200, anchor=CENTER)
        self.tree_ip.column('RoomID', width=240, anchor=CENTER)
        self.tree_ip.column('DateAdmis', width=220, anchor=CENTER)
        self.tree_ip.column('DateOut', width=230, anchor=CENTER)
        self.tree_ip.column('NoOfDays', width=210, anchor=CENTER)

        self.tree_ip.heading('IPID', text='IPID')
        self.tree_ip.heading('PatientID', text='PatientID')
        self.tree_ip.heading('DiagnoseID', text='DiagnoseID')
        self.tree_ip.heading('TakmedID', text='TakmedID')
        self.tree_ip.heading('RoomID', text='RoomID')
        self.tree_ip.heading('DateAdmis', text='DateAdmis')
        self.tree_ip.heading('DateOut', text='DateOut')
        self.tree_ip.heading('NoOfDays', text='NoOfDays')

        mainloop()

    def add_ip(self):
        pass
        # / self.tree.insert('',END,values=(self.drid.get(),self.drname.get(),self.age.get(),self.mobile.get(),self.email.get(),self.gender_var.get(),self.address.get(),self.specialist.get(),self.salary.get(),self.shift_var.get(),self.dep_var.get()))

    def find_ip(self, e):
        self.search_ip.config(state=NORMAL)
        self.search_ip.delete(0, END)
        self.search_ip.focus()

    def _find_ip(self, e):
        self.search_ip.config(state=NORMAL)
        self.search_ip.delete(0, END)
        self.search_ip.focus()

    def _Return_ip(self, e):
        messagebox.showinfo('INFO', f'You Write {self.search_ip.get()}', parent=self.IP)

    def clock_ip(self):
        import time
        self.hour = time.strftime('%I')
        self.minutes = time.strftime('%M')
        self.secons = time.strftime('%S')
        self.satte = time.strftime('%p')
        self.clock.config(text=f'Time: {self.hour}:{self.minutes}:{self.secons} {self.satte}')
        self.clock.after(1000, self.clock_)

    # DATABASE FETCHING DATA COUNT

    def show_counts(self):
        conn = pyodbc.connect(
            "Driver={SQL Server Native Client 11.0};"
            "Server=DESKTOP-N9PT8FH\SQLEXPRESS;"
            "Database=DaruShifa_Hospital;"
            "Trusted_Connection=yes;"
        )
        # Departments
        cursor=conn.cursor()
        cursor.execute('select *from departments')
        rows=cursor.fetchall()
        self.count_dep.config(text=f'{len(rows)}')

        # doctors
        cursor.execute('select *from Doctors')
        rows_2 = cursor.fetchall()
        self.count_dr.config(text=f'{len(rows_2)}')

        #patients
        cursor.execute('select *from Patients')
        rows_3 = cursor.fetchall()
        self.count_p.config(text=f'{len(rows_3)}')

        # nursing
        cursor.execute('select *from Nursing')
        rows_4 = cursor.fetchall()
        self.count_nurse.config(text=f'{len(rows_4)}')

        #Pharma
        cursor.execute('select *from Pharmacist')
        rows_5= cursor.fetchall()
        self.count_pharma.config(text=f'{len(rows_5)}')

        # medicines
        cursor.execute('select *from Medicines')
        rows_6 = cursor.fetchall()
        self.count_med.config(text=f'{len(rows_6)}')

        # rooms
        cursor.execute('select *from Rooms')
        rows_7= cursor.fetchall()
        self.count_rom.config(text=f'{len(rows_7)}')

        # purchase
        cursor.execute('select *from Purchase')
        rows_8 = cursor.fetchall()
        self.count_pur.config(text=f'{len(rows_8)}')

        # reports
        cursor.execute('select *from Reports')
        rows_9 = cursor.fetchall()
        self.count_sales_label.config(text=f'{len(rows_9)}')

        # bloodsRow
        cursor.execute('select *from Bloods')
        rows_10 = cursor.fetchall()
        self.count_customer_label.config(text=f'{len(rows_10)}')

        # IpRow
        cursor.execute('select *from InPatient')
        rows_11 = cursor.fetchall()
        self.count_ip_label.config(text=f'{len(rows_11)}')

        # opRow
        cursor.execute('select *from OutPatient')
        rows_12 = cursor.fetchall()
        self.count_op_lbl.config(text=f'{len(rows_12)}')


    #_____________logout__________________
    def logout(self):
        ans = messagebox.askyesno('Confirm', 'Are You Sure To Logout?',parent=self.root)
        if (ans):
            self.root.destroy()
            self.log.deiconify()

        else:
            pass



#==object====
if __name__=="__main__":
    __app__=DARUL_SHIFA_HOSPITAL()
    __app__.login_page()