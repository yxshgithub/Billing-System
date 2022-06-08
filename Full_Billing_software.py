from tkinter import *
from tkinter.font import BOLD
import math, random, os
from openpyxl import Workbook
from tkinter import messagebox
import pandas as pd
import datetime
import time
from pandas.core.series import Series
import mysql.connector
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import plotly
import plotly.graph_objects as go



def main():
    win = Tk()
    app = login_window(win)
    win.mainloop()



class login_window:
    def __init__(self, root):
        self.root1 = root
        self.root1.title('Login')
        self.root1.geometry('1100x700+40+40')
        self.root1.resizable(FALSE,FALSE)

        self.bg = ImageTk.PhotoImage(file = r"C:\Users\swara\Documents\New folder (2)\imgbg.png")
        lbl_bg = Label(self.root1, image = self.bg )
        lbl_bg.place(x=0, y=0, relheight = 1, relwidth = 1)

        frame = Frame(self.root1, bg ='yellow')
        frame.place(x=400, y=150, height = 400, width = 300)

        # img1 = Image.open(r"C:\Users\swara\Downloads\New folder (2)\img.png")
        # img1 = img1.resize((100, 100),Image.ANTIALIAS)
        # self.photoimage1 = ImageTk.PhotoImage(img1)
        # lbl_img1 = Label(image=self.photoimage1, bg = 'black', borderwidth=0)
        # lbl_img1.place(x=400, y=80, height = 400, width = 100)
       
        lbl_login = Label(frame ,text= "Login Here", font= ('Times new Roman', 30,'bold'), bg = 'yellow' , fg= "red") 
        lbl_login.place(x = 50, y = 10)
        
        # =============username ico=================
        img1 = Image.open(r"C:\Users\swara\Documents\New folder (2)\img2.png")
        img1 = img1.resize((25, 25),Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lbl_img1 = Label(image=self.photoimage1, bg = 'yellow', borderwidth=0)
        lbl_img1.place(x=430, y=230, height = 20, width = 20)

        lbl_user = Label(frame ,text= "Username* ", font= ('Times new Roman',15), bg = 'yellow' , fg= "red") 
        lbl_user.place(x = 50, y = 80)

        self.user_text1=StringVar()
        self.Entry_user = Entry(frame ,textvariable=self.user_text1 , font= ('Times new Roman',15)) 
        self.Entry_user.place(x = 30, y = 110 , width = 220)

        # =============password ico=================
        img2 = Image.open(r"C:\Users\swara\Documents\New folder (2)\img3.png")
        img2 = img2.resize((25, 25),Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lbl_img2 = Label(image=self.photoimage2, bg = 'yellow', borderwidth=0)
        lbl_img2.place(x=430, y=305, height = 18, width = 18)

        lbl_pass = Label(frame ,text= "Password* ", font= ('Times new Roman',15), bg = 'yellow' , fg= "red") 
        lbl_pass.place(x = 50, y = 150)

        self.password_text1=StringVar()
        self.Entry_user = Entry(frame ,textvariable=self.password_text1, font= ('Times new Roman',15), show="*") 
        self.Entry_user.place(x = 30, y = 180 , width = 220)

        b1=Button(frame, text="Login" ,width=50  , command= self.login_database ,font="times 15",bd = 3 , relief= RIDGE, bg="red",fg= "white",
        activebackground= "red" ,  activeforeground="white")
        b1.place(x=80,y=230,width=130,height=30)

        lbl_user = Label(frame ,text=  "OR", font= ('Times new Roman',12 , "bold"), bg = 'yellow' , fg= "#Ac9c0e") 
        lbl_user.place(x = 120, y = 270)

        
        b2=Button(frame, text= " Forgot Password? " ,command=self.forgot_pass,  width=50  ,font="times 13 ",borderwidth= 0 ,fg= "blue", bg = 'yellow')
        b2.place(x=70,y=295,width=160)

        b3=Button(frame, text= "New-User Registeration" , command = self.register_win, width=50  ,font="times 15 ",borderwidth= 0 ,fg= "blue", bg = 'yellow')
        b3.place(x=0,y=350,width=250)


    def register_win(self):
        self.new_window = Toplevel(self.root1)
        self.app = Register_window(self.new_window)


    #==============================================backend for login butt-==================================================

    def login_database(self):
        if self.user_text1.get() == "" or self.password_text1.get() == "" :
            messagebox.showerror("Error" , "All fields are required to login ")
        else:
            conn = mysql.connector.connect(host='localhost',user='root',password='root',database='mydata')
            my_cur = conn.cursor()
            my_cur.execute("select * from register where username=%s and password=%s",(
                                                                                        self.user_text1.get(),
                                                                                        self.password_text1.get()
                                                                                        
                                                                                        ))
            row=my_cur.fetchone()
            if row==None:
                messagebox.showerror("Error", "Invalid credentials")
            else:
                open_main = messagebox.askyesno("Yesorno", " Access by employee ")
                if open_main>0:
                        self.new_window = Toplevel(self.root1)
                        self.app= BilL_App(self.new_window)

                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
    #===================================================backend for reset butt=========================================
    def rest_pass(self):
        if self.e6_combobox.get() == "select":
            messagebox.showerror("error","Please select a security question ", parent = self.root2)
        elif self.answer_text1.get() == "" or self.npass_text1.get() =="" or self.npass_textc.get() == "":
            messagebox.showerror("error","All fields are rquired", parrent = self.root2)
        elif self.npass_text1.get() != self.npass_textc.get():
            messagebox.showerror("error","Password and Confirm Password must be same ", parent = self.root2)
        else:
            conn = mysql.connector.connect(host='localhost',user='root',password='root',database='mydata')
            my_cur = conn.cursor()
            query=("select * from register where username=%s and securityQ=%s and securityA=%s")
            value=(self.user_text1.get(), self.e6_combobox.get(), self.answer_text1.get(),)
            my_cur.execute(query,value)
            row=my_cur.fetchone()
            if row== None:
                messagebox.showerror("error","Please enter correct answer")
            else:
                query=("update register set password=%s where username=%s")
                value=(self.npass_text1.get(),self.user_text1.get())
                my_cur.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info", "Your password has been Reset, Please login with new password.", parent = self.root2)
                self.root2.destroy()


    #===================================================backend for forgot butt=========================================
    def forgot_pass(self):
        if self.user_text1 == "":
            messagebox.showerror("Error", "Please enter a username")
        else:
            conn = mysql.connector.connect(host='localhost',user='root',password='root',database='mydata')
            my_cur = conn.cursor()
            query=("select * from register where username=%s")
            value=(self.user_text1.get(),)
            my_cur.execute(query,value)
            row=my_cur.fetchone()
            if row==None:
                messagebox.showerror('Error', 'Please enter a valid username')
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Reset Password")
                self.root2.geometry("350x470+610+170")
                for_lab = Label(self.root2, text="Forgot password" , font="times 20 bold", fg = "red")
                for_lab.place(x=0,y=10,relwidth=1)

                sec_que = Label(self.root2,text="Security questions*",font="times 14")
                sec_que.place(x=50,y=80)

                # global self.e6_combobox
                self.e6_combobox = ttk.Combobox(self.root2,  font="times 12", state= "readonly" )
                self.e6_combobox["values"]= ("Select","Your Pet Name " , "Your Birth place" ,"Your First Best friend")
                self.e6_combobox.place(x=50,y=110,width=250)
                self.e6_combobox.current(0)

                sec_ans = Label(self.root2,text="Security Answer*",font="times 14")
                sec_ans.place(x=50,y=150)

                # global self.answer_text1
                self.answer_text1 = StringVar()
                self.sec_ans = Entry(self.root2, textvariable=self.answer_text1, font="times 14")
                self.sec_ans.place(x = 50, y= 190)

                new_pass = Label(self.root2,text="New Password*",font="times 14")
                new_pass.place(x=50,y=230)

                # global self.npass_text1
                self.npass_text1 = StringVar()
                self.new_pass = Entry(self.root2, textvariable=self.npass_text1, font="times 14")
                self.new_pass.place(x = 50, y= 270)

                new_passc = Label(self.root2,text="Confirm New Password*",font="times 14")
                new_passc.place(x=50,y=310)

                # global self.npass_textc
                self.npass_textc = StringVar()
                self.new_passc = Entry(self.root2,textvariable = self.npass_textc ,  font="times 14")
                self.new_passc.place(x = 50, y= 350)

                but1=Button(self.root2, text="Reset Password", command= self.rest_pass, width=50 ,font="times 14 bold",  bg="green" , fg="white")
                but1.place(x=100,y=400,width=150)
                # command= rest_pass

class Register_window:
    def __init__(self, root):
        self.root = root
        self.root.title('Login')
        self.root.geometry('1100x700+40+40')
        self.root.resizable(FALSE,FALSE)

        self.bg = ImageTk.PhotoImage(file = r"C:\Users\swara\Documents\New folder (2)\imgbg.png")
        lbl_bg = Label(self.root, image = self.bg )
        lbl_bg.place(x=0, y=0, relheight = 1, relwidth = 1)

        frame1 =Frame (self.root , bg = "#f5d142")
        frame1.place(x=250, y=150, width=500, height=500 )

        lbl_reg= Label(self.root ,text= " Register Here ", font= ('Times new Roman',45,'bold'), fg= "red", bg= "#f5d142") 
        lbl_reg.place(x = 310, y = 120)

        #----------------------------------------------labels and entry --------------------------------------

        l1=Label(frame1,text="First Name*",font="times 15", bg = "#f5d142" , fg = "red")
        l1.place(x=30,y=60,width=130,height=25)

        self.name_text=StringVar()
        self.e1=Entry(frame1,textvariable=self.name_text)
        self.e1.place(x=40,y=90,width=180,height=25)

        l2=Label(frame1,text="User-email*",font="times 15", bg = "#f5d142" , fg = "red")
        l2.place(x=10,y=130,width=160,height=25)

        self.email_text=StringVar()
        self.e2=Entry(frame1,textvariable=self.email_text)
        self.e2.place(x=40,y=160,width=180,height=25)

        l3=Label(frame1,text="Password*",font="times 15", bg = "#f5d142" , fg = "red")
        l3.place(x=20,y=200,width=130,height=25)

        self.password_text=StringVar()
        self.e3=Entry(frame1,textvariable=self.password_text)
        self.e3.place(x=40,y=230,width=180,height=25)

        l5 = Label(frame1,text="Confirm Password*",font="times 15", bg = "#f5d142" , fg = "red")
        l5.place(x=20,y=270,width=190,height=25)
            
        self.password_textC=StringVar()
        self.e4=Entry(frame1,textvariable= self.password_textC)
        self.e4.place(x=40,y=300,width=180,height=25)

        l10 = Label(frame1,text= " Please select your Gender",font="times 14", bg = "#f5d142" , fg = "red")
        l10.place(x=35,y=340,width=200,height=25)

        self.gender_text=StringVar()
        e10_combobox = ttk.Combobox(frame1, textvariable = self.gender_text, font="times 12", state= "readonly" )
        e10_combobox["values"]= ("Select"," Male " , "Female" ,"Other")
        e10_combobox.place(x=40,y=370,width=190,height=25)
        e10_combobox.current(0)
        
        l8 = Label(frame1,text="Last Name ",font="times 15", bg = "#f5d142" , fg = "red")
        l8.place(x=250,y=60,width=150,height=25)

        self.last_name = StringVar()
        self.e8 = Entry(frame1, textvariable=self.last_name)
        self.e8.place(x=270,y=90,width=190,height=25)

        l6 = Label(frame1,text="Username*",font="times 15", bg = "#f5d142" , fg = "red")
        l6.place(x=230,y=130,width=190,height=25)

        self.User_name = StringVar()
        self.e9 = Entry(frame1, textvariable=self.User_name)
        self.e9.place(x=270,y=160,width=190,height=25)

        l7 = Label(frame1,text="Security questions*",font="times 14", bg = "#f5d142" , fg = "red")
        l7.place(x=270,y=200,width=150,height=25)

        self.question_text=StringVar()
        self.e6_combobox = ttk.Combobox(frame1, textvariable = self.question_text, font="times 13", state= "readonly" )
        self.e6_combobox["values"]= ("Select","Your Pet Name " , "Your Birth place" ,"Your First Best friend")
        self.e6_combobox.place(x=270,y=230,width=190,height=25)
        self.e6_combobox.current(0)

        l9 = Label(frame1,text="Security Answer*",font="times 14", bg = "#f5d142" , fg = "red")
        l9.place(x=270,y=270,width=150,height=25)

        self.answer_text1 = StringVar()
        self.e7 = Entry(frame1, textvariable = self.answer_text1)
        self.e7.place(x = 270, y= 300, width=180,height=25)

        # checkbutton
        self.var_check = IntVar()
        self.chckbtn = Checkbutton(frame1, variable=self.var_check, text = "I Agree to the Terms & Conditions",font="times 12 bold italic",bg="#f5d142", activebackground= "#f5d142", onvalue=1,offvalue=0)
        self.chckbtn.place(x=130,y=420,width= 250)

        
        b1=Button(self.root, text="Register" ,width=50 ,command= self.signup_database ,  font="times 16 ", bg="#D05748" , bd = 4 , relief= RIDGE)
        b1.place(x=300,y=630,width=150,height=40)

        b1=Button(self.root, text="Login Now" ,width=50 , command= self.login_win ,  font="times 16", bg="#5959BC" , bd = 4 , relief= RIDGE)
        b1.place(x=540,y=630,width=150,height=40)
    
    def signup_database(self):

        if self.e1.get() == "" or self.e2.get() == "" or self.e3.get() == "" or self.e4.get() == "" or self.e6_combobox == "select" or self.e7 =="":
            messagebox.showerror("Error","All fields are Required for Registration")
        elif self.e3.get() != self.e4.get():
            messagebox.showerror("Error", "Password and Confirm Password must be same")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree to our terms and conditions")
        else:
            conn = mysql.connector.connect(host='localhost',user='root',password='root',database='mydata')
            my_cur = conn.cursor()
            query=(" select * from register where email = %s")
            value = (self.email_text.get(),)
            my_cur.execute(query, value)    
            row=my_cur.fetchone()
            if row!= None:
                messagebox.showerror("error", "User already exists, please try another email")
            else:
                my_cur.execute("insert into register values(%s, %s, %s,%s,%s,%s,%s)",(
                                                                                        self.name_text.get(),
                                                                                        self.User_name.get(),
                                                                                        self.email_text.get(),
                                                                                        self.User_name.get(),
                                                                                        self.password_text.get(),
                                                                                        self.question_text.get(),
                                                                                        self.answer_text1.get()

                                                                                            ))
            conn.commit()
            conn.close()
            messagebox.showinfo("success" ,"Register successfully")

    def login_win(self):
        self.root.destroy()



class BilL_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+10+10")
        self.root.resizable(FALSE,FALSE)
        self.root.title("Billing Software")
        bg_color = "red"
        title = Label(self.root, text="McDonald's", bd=12, relief=GROOVE, bg=bg_color, fg="gold",
                      font=("Mclawsuit", 30, "bold"), pady=2).pack(fill=X)

        # =============Variables======================================
        # ==========Menu card variables==========
        self.aloo_tikki = IntVar()
        self.mc_veg = IntVar()
        self.mc_Maharaja = IntVar()
        self.french_fries = IntVar()
        self.coke_float = IntVar()
        self.chicken_wrap = IntVar()
        self.mc_spicy_veg = IntVar()
        self.mc_non_veg = IntVar()
        self.chicken_keebab = IntVar()
        self.mc_supreme = IntVar()
        self.veg_happy_meal = IntVar()
        self.chicken_strips = IntVar()
        self.fountain_coke = IntVar()
        self.chip_muffin = IntVar()
        self.masala_wedges = IntVar()
        self.pizza_puff = IntVar()
        self.flat_white = IntVar()
        self.green_tea = IntVar()

        # ==================================Total Price and Tax===================================
        self.total_price = StringVar()
        self.gst_tax = StringVar()

        # ==================================Customer details========================================
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()

        self.this = datetime.datetime.now()
        self.current_time = self.this.strftime("%H:%M %p")
        self.current_date = self.this.strftime("%d/%b/%Y")

        # =====customer details Frame

        F1 = LabelFrame(self.root, text="Customer Details", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),fg="gold", bg=bg_color)
        F1.place(x=0, y=80, relwidth=1)

        cname_lbl = Label(F1, text="Customer Name", bg=bg_color, fg="white", font=("times new roman", 17, "bold")).grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, font="arial 15", bd=7, textvariable=self.c_name, relief=SUNKEN).grid(row=0,
                                                                                                             column=1,
                                                                                                             pady=5,
                                                                                                             padx=5)

        cphn_lbl = Label(F1, text="Phone No", bg=bg_color, fg="white", font=("times new roman", 17, "bold")).grid(row=0,
                                                                                                                  column=2,
                                                                                                                  padx=10,
                                                                                                                  pady=5)
        cphn_txt = Entry(F1, width=15, font="arial 15", bd=7, textvariable=self.c_phone, relief=SUNKEN).grid(row=0,
                                                                                                             column=3,
                                                                                                             pady=5,
                                                                                                             padx=5)

        c_bill_lbl = Label(F1, text="Bill Number", bg=bg_color, fg="white", font=("times new roman", 17, "bold")).grid(
            row=0, column=4, padx=10, pady=5)
        c_bill_lbl_txt = Entry(F1, width=10, font="arial 15", bd=7, textvariable=self.search_bill, relief=SUNKEN).grid(
            row=0, column=5, pady=5, padx=10)

        bill_btn = Button(F1, text="Search", width=10, bd=7, command=self.find_bill, font="arial 12 bold").grid(row=0,
                                                                                                                column=6,
                                                                                                                padx=10,
                                                                                                                pady=10)
        
        excel_btn = Button(F1, text="Save into Excel", width=15, bd=7,  command=self.Excel_app,  font="arial 11 bold").grid(row=0,column=7,padx=10,pady=10)

        # ===========MENU CARD FRAME 1============================================

        F2 = LabelFrame(self.root, text="MENU CARD", bd=10, relief=GROOVE,
                        font=("timesAT+CMGS=\"+919867235486\"\r new roman", 15, "bold"), fg="gold", bg=bg_color)
        F2.place(x=5, y=180, width=330, height=380)

        Aloo_Tiki_lbl = Label(F2, text="Aloo Tikki", font=("times new roman", 16, "bold"), bg=bg_color,
                              fg="white").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        Aloo_Tiki_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"), bd=5, textvariable=self.aloo_tikki,
                              relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        Mc_Veg_lbl = Label(F2, text="Mc Veg", font=("times new roman", 16, "bold"), bg=bg_color, fg="white").grid(row=1,
                                                                                                                  column=0,
                                                                                                                  padx=10,
                                                                                                                  pady=10,
                                                                                                                  sticky="w")
        Mc_Veg_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"), bd=5, textvariable=self.mc_veg,
                           relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        Mc_Maharaja_lbl = Label(F2, text="Mc Maharaja", font=("times new roman", 16, "bold"), bg=bg_color,
                                fg="white").grid(row=2, column=0, padx=10, pady=1, sticky="w")
        Mc_Maharaja_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"), bd=5, textvariable=self.mc_Maharaja,
                                relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        French_fries_lbl = Label(F2, text="French Fries", font=("times new roman", 16, "bold"), bg=bg_color,
                                 fg="white").grid(row=3, column=0, padx=10, pady=1, sticky="w")
        French_fries_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"), bd=5,
                                 textvariable=self.french_fries, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        Coke_Float_lbl = Label(F2, text="Coke Float", font=("times new roman", 16, "bold"), bg=bg_color,
                               fg="white").grid(row=4, column=0, padx=10, pady=1, sticky="w")
        Coke_Float_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"), bd=5, textvariable=self.coke_float,
                               relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        Chicken_wrap_lbl = Label(F2, text="Chicken Wrap", font=("times new roman", 16, "bold"), bg=bg_color,
                                 fg="white").grid(row=5, column=0, padx=10, pady=1, sticky="w")
        Chicken_wrap_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"), bd=5,
                                 textvariable=self.chicken_wrap, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # ===========MENU CARD FRAME 2============================================

        F3 = LabelFrame(self.root, bd=10, relief=GROOVE, font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F3.place(x=340, y=180, width=325, height=380)

        Mc_Spicy_lbl = Label(F3, text=" Mc Spicy Veg", font=("times new roman", 16, "bold"), bg=bg_color,
                             fg="white").grid(row=0, column=0, padx=10, pady=22, sticky="w")
        Mc_Spicy_txt = Entry(F3, width=9, font=("times new roman", 16, "bold"), bd=5, textvariable=self.mc_spicy_veg,
                             relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        Mc_Non_Veg_lbl = Label(F3, text="Mc Non Veg", font=("times new roman", 16, "bold"), bg=bg_color,
                               fg="white").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        Mc_Non_Veg_txt = Entry(F3, width=9, font=("times new roman", 16, "bold"), bd=5, textvariable=self.mc_non_veg,
                               relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        Chicken_keebab_lbl = Label(F3, text="Chicken kebab", font=("times new roman", 16, "bold"), bg=bg_color,
                                   fg="white").grid(row=2, column=0, padx=10, pady=1, sticky="w")
        Chicken_keebab_txt = Entry(F3, width=9, font=("times new roman", 16, "bold"), bd=5,
                                   textvariable=self.chicken_keebab, relief=SUNKEN).grid(row=2, column=1, padx=10,
                                                                                         pady=10)

        Mc_Supreme_lbl = Label(F3, text="Mc Supreme", font=("times new roman", 16, "bold"), bg=bg_color,
                               fg="white").grid(row=3, column=0, padx=10, pady=1, sticky="w")
        Mc_Supreme_txt = Entry(F3, width=9, font=("times new roman", 16, "bold"), bd=5, textvariable=self.mc_supreme,
                               relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        Veg_Happymeal_lbl = Label(F3, text="Veg Happy Meal", font=("times new roman", 16, "bold"), bg=bg_color,
                                  fg="white").grid(row=4, column=0, padx=10, pady=1, sticky="w")
        Veg_Happymeal_txt = Entry(F3, width=9, font=("times new roman", 16, "bold"), bd=5,
                                  textvariable=self.veg_happy_meal, relief=SUNKEN).grid(row=4, column=1, padx=10,
                                                                                        pady=10)

        Chicken_Strips_lbl = Label(F3, text="Chicken Strips", font=("times new roman", 16, "bold"), bg=bg_color,
                                   fg="white").grid(row=5, column=0, padx=10, pady=1, sticky="w")
        Chicken_Strips_txt = Entry(F3, width=9, font=("times new roman", 16, "bold"), bd=5,
                                   textvariable=self.chicken_strips, relief=SUNKEN).grid(row=5, column=1, padx=10,
                                                                                         pady=10)

        # ===========MENU CARD FRAME 3============================================

        F4 = LabelFrame(self.root, bd=10, relief=GROOVE, font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F4.place(x=670, y=180, width=325, height=380)

        Fountain_Coke_lbl = Label(F4, text="Fountain Coke", font=("times new roman", 16, "bold"), bg=bg_color,
                                  fg="white").grid(row=0, column=0, padx=10, pady=22, sticky="w")
        Fountain_Coke_txt = Entry(F4, width=9, font=("times new roman", 16, "bold"), bd=5,
                                  textvariable=self.fountain_coke, relief=SUNKEN).grid(row=0, column=1, padx=10,
                                                                                       pady=10)

        Chip_Muffin_lbl = Label(F4, text="Chip Muffin", font=("times new roman", 16, "bold"), bg=bg_color,
                                fg="white").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        Chip_Muffin_txt = Entry(F4, width=9, font=("times new roman", 16, "bold"), bd=5, textvariable=self.chip_muffin,
                                relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        Masala_Wedges_lbl = Label(F4, text="Masala Wedges", font=("times new roman", 16, "bold"), bg=bg_color,
                                  fg="white").grid(row=2, column=0, padx=10, pady=1, sticky="w")
        Masala_Wedges_txt = Entry(F4, width=9, font=("times new roman", 16, "bold"), bd=5,
                                  textvariable=self.masala_wedges, relief=SUNKEN).grid(row=2, column=1, padx=10,
                                                                                       pady=10)

        Pizza_Puff_lbl = Label(F4, text="Pizza Puff", font=("times new roman", 16, "bold"), bg=bg_color,
                               fg="white").grid(row=3, column=0, padx=10, pady=1, sticky="w")
        Pizza_Puff_txt = Entry(F4, width=9, font=("times new roman", 16, "bold"), bd=5, textvariable=self.pizza_puff,
                               relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        Flat_White_lbl = Label(F4, text="Flat White", font=("times new roman", 16, "bold"), bg=bg_color,
                               fg="white").grid(row=4, column=0, padx=10, pady=1, sticky="w")
        Flat_White_txt = Entry(F4, width=9, font=("times new roman", 16, "bold"), bd=5, textvariable=self.flat_white,
                               relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        Green_Tea_lbl = Label(F4, text="Green Tea", font=("times new roman", 16, "bold"), bg=bg_color, fg="white").grid(
            row=5, column=0, padx=10, pady=1, sticky="w")
        Green_Tea_txt = Entry(F4, width=9, font=("times new roman", 16, "bold"), bd=5, textvariable=self.green_tea,
                              relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # ================================BILL AREA==========================================================================
        F5 = LabelFrame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1002, y=180, width=345, height=500)
        Bill_title = Label(F5, text="Bill Generated", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        Scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=Scroll_y.set)
        Scroll_y.pack(side=RIGHT, fill=Y)
        Scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        # =========================Button Frame=========================
        F6 = LabelFrame(self.root, text="Bill Card", bd=10, relief=GROOVE, font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=140)

        m1_lbl = Label(F6, text="Total Price", bg=bg_color, height=3, fg="gold",
                       font=("times new roman", 14, "bold")).grid(row=0, column=0, padx=10, pady=1, sticky="w")
        m1_txt = Entry(F6, width=18, font="arial 10 bold", bd=7, textvariable=self.total_price, relief=SUNKEN).grid(
            row=0, column=1, padx=10, pady=1)

        m2_lbl = Label(F6, text="G.S.T Tax", bg=bg_color, fg="gold", font=("times new roman", 14, "bold")).grid(row=0,
                                                                                                                 column=2,
                                                                                                                 padx=10,
                                                                                                                 pady=1,
                                                                                                                 sticky="w")
        m2_txt = Entry(F6, width=18, font="arial 10 bold", textvariable=self.gst_tax, bd=7, relief=SUNKEN).grid(row=0,
                                                                                                                column=3,
                                                                                                                padx=10,
                                                                                                                pady=1)

        btn_F = Frame(F6, bd=7, relief=GROOVE, bg="red")
        btn_F.place(x=600, width=720, height=100)

        Total_btn = Button(btn_F, text="Total", command=self.total, bg="red", fg="gold", width=13,
                           font="arial 14 bold",bd=2).grid(row=0, column=0, padx=5)
        GBill_btn = Button(btn_F, text="Generate Bill", command=self.bill_area, bg="red", fg="gold", width=13,
                           font="arial 14 bold",bd=2).grid(row=0, column=1, padx=5)
        Clear_btn = Button(btn_F, text="Clear", bg="red", command=self.clear_data, fg="gold", width=13,
                           font="arial 14 bold",bd=2).grid(row=0, column=2, padx=5)
        Exit_btn = Button(btn_F, text="Exit", bg="red", command=self.Exit_app, fg="gold", width=13,
                          font="arial 14 bold",bd=2).grid(row=0, column=3, padx=5)
        Graph_btn = Button(btn_F, text="Graph", bg="red", command=self.Plot_graph, fg="gold", width=7,
                          font="arial 14 bold",bd=2).grid(row=1, column=1,pady= 5)
        self.welcome_bill()

    def total(self):
        self.a_tki = self.aloo_tikki.get() * 40
        self.mc_vg = self.mc_veg.get() * 103
        self.mc_mhraja = self.mc_Maharaja.get() * 204
        self.frnch_fries = self.french_fries.get() * 57
        self.cok_flot = self.coke_float.get() * 82
        self.chckn_wrp = self.chicken_wrap.get() * 204
        self.mc_spcy_vg = self.mc_spicy_veg.get() * 163
        self.mc_n_vg = self.mc_non_veg.get() * 100
        self.chckn_kebaab = self.chicken_keebab.get() * 80
        self.mc_sup = self.mc_supreme.get() * 135
        self.vg_hppy = self.veg_happy_meal.get() * 220
        self.chkn_strip = self.chicken_strips.get() * 78
        self.futn_cok = self.fountain_coke.get() * 75
        self.chp_muff = self.chip_muffin.get() * 113
        self.msla_wdg = self.masala_wedges.get() * 44
        self.piz_puf = self.pizza_puff.get() * 42
        self.flt_wht = self.flat_white.get() * 80
        self.grn_t = self.green_tea.get() * 70
        self.total_show_price = float(
            self.a_tki +
            self.mc_vg +
            self.mc_mhraja +
            self.frnch_fries +
            self.cok_flot +
            self.chckn_wrp +
            self.mc_spcy_vg +
            self.mc_n_vg +
            self.chckn_kebaab +
            self.mc_sup +
            self.vg_hppy +
            self.chkn_strip +
            self.futn_cok +
            self.chp_muff +
            self.msla_wdg +
            self.piz_puf +
            self.flt_wht +
            self.grn_t
        )

        self.total_price.set("Rs. " + str(self.total_show_price))
        self.g_tax = round((self.total_show_price * 0.18), 2)
        self.gst_tax.set("Rs. " + str(self.g_tax))
        self.t_bill = round((self.total_show_price + self.g_tax), 2)
        self.Total_Bill = float(self.t_bill)

    # =======================Bill area ==============================================
    def welcome_bill(self):

        self.my_label = Label(self.root ,text='', font=("Times", 20), fg="Yellow", bg="red")
        self.my_label.place(x=80, y=20)
        self.my_label1 = Label(self.root, text='Time:', font=("Times", 20), fg="Yellow", bg="red")
        self.my_label1.place(x=15, y=20)

        self.my_label2 = Label(self.root, text=f'Date: {self.current_date}', font= ("Times", 20),  fg = "Yellow", bg="red" )
        self.my_label2.place(x=1120, y=20)

        def clock():
            this = datetime.datetime.now()
            hours = this.strftime("%H")
            minutes = this.strftime("%M")
            seconds = this.strftime("%S")

            self.my_label.config(text=hours + ":" + minutes + ":" + seconds)
            self.my_label.after(1000, clock)

        clock()

        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\t Welcome to Mcdonald's\n")
        self.txtarea.insert(END, f"\n Date: {self.current_date} Time: {self.current_time}")
        self.txtarea.insert(END, f"\n Bill Number:   {self.bill_no.get()}")
        self.txtarea.insert(END, f"\n Customer Name: {self.c_name.get()}")
        self.txtarea.insert(END, f"\n Phone Number:  {self.c_phone.get()}")
        self.txtarea.insert(END, f"\n======================================")
        self.txtarea.insert(END, f"\n Products\t\tQty\t\tPrice")
        self.txtarea.insert(END, f"\n======================================")

    def bill_area(self):
        if self.c_name.get() == "" or self.c_phone.get() == "":
            messagebox.showerror("Error", "Customer Details are empty",parent= self.root)
        elif self.total_price.get() == "Rs. 0.0":
            messagebox.showerror("Error", "No items purchased" ,parent= self.root)
        else:
            self.welcome_bill()
            if self.aloo_tikki.get() != 0:
                self.txtarea.insert(END, f"\n Aloo Tikki\t\t {self.aloo_tikki.get()}\t\t {self.a_tki}")
            if self.mc_veg.get() != 0:
                self.txtarea.insert(END, f"\n Mc Veg\t\t {self.mc_veg.get()}\t\t {self.mc_vg}")
            if self.mc_Maharaja.get() != 0:
                self.txtarea.insert(END, f"\n Mc Maharaja\t\t {self.mc_Maharaja.get()}\t\t {self.mc_mhraja}")
            if self.french_fries.get() != 0:
                self.txtarea.insert(END, f"\n French Fries\t\t {self.french_fries.get()}\t\t {self.frnch_fries}")
            if self.coke_float.get() != 0:
                self.txtarea.insert(END, f"\n Coke Float\t\t {self.coke_float.get()}\t\t {self.cok_flot}")
            if self.chicken_wrap.get() != 0:
                self.txtarea.insert(END, f"\n Chicken Wrap\t\t {self.chicken_wrap.get()}\t\t {self.chckn_wrp}")
            if self.mc_spicy_veg.get() != 0:
                self.txtarea.insert(END, f"\n Mc Spicy Veg\t\t {self.mc_spicy_veg.get()}\t\t {self.mc_spcy_vg}")
            if self.mc_non_veg.get() != 0:
                self.txtarea.insert(END, f"\n Mc Non Veg\t\t {self.mc_non_veg.get()}\t\t {self.mc_n_vg}")
            if self.chicken_keebab.get() != 0:
                self.txtarea.insert(END, f"\n Chicken Kebab\t\t {self.chicken_keebab.get()}\t\t {self.chckn_kebaab}")
            if self.mc_supreme.get() != 0:
                self.txtarea.insert(END, f"\n Mc Supreme\t\t {self.mc_supreme.get()}\t\t {self.mc_sup}")
            if self.veg_happy_meal.get() != 0:
                self.txtarea.insert(END, f"\n Veg Happy Meal\t\t {self.veg_happy_meal.get()}\t\t {self.vg_hppy}")
            if self.chicken_strips.get() != 0:
                self.txtarea.insert(END, f"\n Chicken Strips\t\t {self.chicken_strips.get()}\t\t {self.chkn_strip}")
            if self.fountain_coke.get() != 0:
                self.txtarea.insert(END, f"\n Fountain Coke\t\t {self.fountain_coke.get()}\t\t {self.futn_cok}")
            if self.chip_muffin.get() != 0:
                self.txtarea.insert(END, f"\n Chip Muffin\t\t {self.chip_muffin.get()}\t\t {self.chp_muff}")
            if self.masala_wedges.get() != 0:
                self.txtarea.insert(END, f"\n Masala Wedges\t\t {self.masala_wedges.get()}\t\t {self.msla_wdg}")
            if self.pizza_puff.get() != 0:
                self.txtarea.insert(END, f"\n Pizza Puff\t\t {self.pizza_puff.get()}\t\t {self.piz_puf}")
            if self.flat_white.get() != 0:
                self.txtarea.insert(END, f"\n Flat White\t\t {self.flat_white.get()}\t\t {self.flt_wht}")
            if self.green_tea.get() != 0:
                self.txtarea.insert(END, f"\n Green Tea\t\t {self.green_tea.get()}\t\t {self.grn_t}")

            self.txtarea.insert(END, f"\n--------------------------------------")
            if self.gst_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\n G.S.T Tax  :\t\t\t   {self.gst_tax.get()}")
                self.txtarea.insert(END, f"\n Total Bill :\t\t\t   Rs. {self.Total_Bill}")
            self.txtarea.insert(END, f"\n--------------------------------------")
            self.save_bill()
            # self.Excel_app()

    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the Bill?" ,parent= self.root)
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open("Bills/" + str(self.bill_no.get()) + ".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved", f"Bill no: {self.bill_no.get()} saved Succssfully" ,parent= self.root)
        else:
            return

    def Excel_app(self):
        path = 'Data2.xlsx'
        df1 = pd.read_excel(path)
        SeriesA = df1['Customer_name']
        SeriesB = df1['Customer_phone_no']
        SeriesC = df1['Bill_no']
        SeriesD = df1['GST_TAX']
        SeriesE = df1['Total_Bill']
        SeriesF = df1['DATE']
        SeriesG = df1['TIME']
        A = pd.Series(self.c_name.get())
        B = pd.Series(self.c_phone.get())
        C = pd.Series(self.bill_no.get())
        D = pd.Series(self.gst_tax.get())
        E = pd.Series(self.total_price.get())
        F = pd.Series(self.current_date)
        G = pd.Series(self.current_time)
        SeriesA = SeriesA.append(A)
        SeriesB = SeriesB.append(B)
        SeriesC = SeriesC.append(C)
        SeriesD = SeriesD.append(D)
        SeriesE = SeriesE.append(E)
        SeriesF = SeriesF.append(F)
        SeriesG = SeriesG.append(G)
        df2 = pd.DataFrame(
            {"Customer_name": SeriesA, "Customer_phone_no": SeriesB, "Bill_no": SeriesC, "GST_TAX": SeriesD,
             "Total_Bill": SeriesE, "DATE": SeriesF, "TIME": SeriesG})
        df2.to_excel(path, index=False)
        messagebox.showinfo("Saved", f"Bill no: {self.bill_no.get()} saved Succssfully into the Excel File" ,parent= self.root)

    def find_bill(self):
        present = "No"
        for i in os.listdir("Bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"Bills/{i}", "r")
                self.txtarea.delete('1.0', END)
                for d in f1:
                    self.txtarea.insert(END, d)
                f1.close()
                present = "Yes"
        if present == "No":
            messagebox.showerror("Error", "Invalid Bill No.",parent= self.root)

    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to clear data?",parent= self.root)
        if op > 0:
            self.aloo_tikki.set(0)
            self.mc_veg.set(0)
            self.mc_Maharaja.set(0)
            self.french_fries.set(0)
            self.coke_float.set(0)
            self.chicken_wrap.set(0)
            self.mc_spicy_veg.set(0)
            self.mc_non_veg.set(0)
            self.chicken_keebab.set(0)
            self.mc_supreme.set(0)
            self.veg_happy_meal.set(0)
            self.chicken_strips.set(0)
            self.fountain_coke.set(0)
            self.chip_muffin.set(0)
            self.masala_wedges.set(0)
            self.pizza_puff.set(0)
            self.flat_white.set(0)
            self.green_tea.set(0)
            # ==================================Total Price and Tax===================================
            self.total_price.set("")
            self.gst_tax.set("")

            # ==================================Customer details========================================
            self.c_name.set("")
            self.c_phone.set("")
            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.this = datetime.datetime.now()
            self.current_time = self.this.strftime("%H:%M %p")
            self.current_date = self.this.strftime("%d/%b/%Y")
            self.welcome_bill()


    def Plot_graph(self):
        excel_file = 'Data2.xlsx'
        df = pd.read_excel(excel_file)
        # print(df)
        data = [go.Scatter(x=df['DATE'], y=df['Total_Bill'])]
        fig = go.Figure(data)
        # fig.show()
        plotly.offline.plot(fig, filename="salesreport.html")

    def Exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?" ,parent= self.root)
        if op > 0:
            self.root.destroy()
        else:
            return



if __name__ == "__main__":
    main()
