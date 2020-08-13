from tkinter import *
def ogsignlerf():
    from tkinter.font import Font
    import sqlite3,os,sys

    enter=Tk()
    enter.attributes('-fullscreen', True)

    def close():
        enter.destroy()

    def imgbinary11():
        global imgdata
        with open("111.png", "rb") as f:
            imgdata = f.read()
    def imgbinary22():
        global imgdata
        with open("158.png", "rb") as f:
            imgdata = f.read()
    def imgbinary33():
        global imgdata
        with open("175.png", "rb") as f:
            imgdata = f.read()
    def imgbinary44():
        global imgdata
        with open("186.png", "rb") as f:
            imgdata = f.read()
    def imgbinary55():
        global imgdata
        with open("153.png", "rb") as f:
            imgdata = f.read()
    def imgbinary66():
        global imgdata
        with open("136.png", "rb") as f:
            imgdata = f.read()

    def dtbssign():
        global naam
        naam=sign11.get()
        print(naam)
        if len(sign33.get())>=8 and len(sign44.get())>=8:
            if sign33.get()==sign44.get():
                conn = sqlite3.connect("pybox-db.db", isolation_level=None)
                cursor = conn.execute("Insert into accounts values(?,?,?,?)",(naam, sign22.get(), sign33.get(),imgdata))
                print("data sent.")
                conn.close()
                print(naam)
                f=open("userella.txt","w")
                f.write(naam)
                enter.destroy()
                os.system("python player.py")
            else:
                print("alag.")
        else:
            print("8.")

    def dtbslog():
        global naam,letter
        naam=log11.get()
        letter=log22.get()
        print(naam,letter)
        conn = sqlite3.connect("pybox-db.db", isolation_level=None)
        cursor = conn.execute('SELECT * from accounts WHERE username="{}" AND password="{}"'.format(naam,letter))
        if cursor.fetchone() is not None:
            print("welcome")
            print(naam)
            f = open("userella.txt", "w")
            f.write(naam)
            f.close()
            enter.destroy()
            os.system("python player.py")
        else:
            print("Hatt!")
            log11.set("")
            log22.set("")
        conn.close()


    clsbtn=Button(enter,command=close,border=0,bg="white")
    calc=PhotoImage(file="cross.png").subsample(3,3)
    clsbtn.config(image=calc,width="30",height="30")
    clsbtn.place(x=1325,y=10)
    photo=PhotoImage(file="F:\projects\pybox-tk\head.png").subsample(2,2)
    fontl=Font(size=20,family="Fixedsys")
    fontr=Font(size=16,family="System")
    brcanva=Canvas(enter,height=2,width=1150,bg="white",background="black",bd=0,highlightthickness=0,relief='ridge').place(x=100,y=390)
    imgcnv=Canvas(enter,height=100,width=100,bg="white",bd=0,highlightthickness=0,relief='ridge')
    imgcnv.create_image(50,50,image=photo)
    imgcnv.place(x=50,y=0)
    frmlog=Frame(enter,height=200,width=600,bg="white").place(x=375,y=150)
    sgnfrm=Frame(enter,height=350,width=1100,bg="white").place(x=125,y=400)
    #dp=PhotoImage(file="user.png").subsample(3,3)
    imgcnv=Canvas(enter,height=100,width=100,bg="white",bd=0,highlightthickness=0,relief='ridge')
    imgcnv.create_image(50,50,image=photo)
    imgcnv.place(x=1000,y=200)

    #frmlog
    loghead=Label(frmlog,text="Login",font=fontl,bg="white").place(x=380,y=155)
    userlogin=Label(frmlog,text="Username",font=fontr,bg="white").place(x=440,y=210)
    pwdlogin=Label(frmlog,text="Password",font=fontr,bg="white").place(x=440,y=270)
    login=Button(sgnfrm,text="Log In",font=fontr,command=dtbslog).place(x=600,y=330)
    log11=StringVar()
    log22=StringVar()
    log1=Entry(frmlog,font=fontr,textvariable=log11,bg="white",validate="focusout").place(x=580,y=210)
    log2=Entry(frmlog,font=fontr,textvariable=log22,bg="white").place(x=580,y=270)

    #sgnfrm
    sgnhead=Label(sgnfrm,text="Sign-Up",font=fontl,bg="white").place(x=130,y=405)
    user=Label(sgnfrm,text="Create Username",font=fontr,bg="white").place(x=190,y=460)
    email=Label(sgnfrm,text="Enter E-Mail",font=fontr,bg="white").place(x=190,y=520)
    pwd=Label(sgnfrm,text="Create Password",font=fontr,bg="white").place(x=190,y=580)
    repwd=Label(sgnfrm,text="Re-Enter Password",font=fontr,bg="white").place(x=190,y=640)
    imager=Label(sgnfrm,text="Select You Profile Picture",font=fontr,bg="white").place(x=600,y=460)
    signup=Button(sgnfrm,text="Sign Up",font=fontr,command=dtbssign).place(x=450,y=700)
    sign11=StringVar()
    sign22=StringVar()
    sign33=StringVar()
    sign44=StringVar()
    sign1=Entry(sgnfrm,textvariable=sign11,font=fontr,bg="white").place(x=330,y=460)
    sign2=Entry(sgnfrm,textvariable=sign22,font=fontr,bg="white").place(x=330,y=520)
    sign3=Entry(sgnfrm,textvariable=sign33,font=fontr,bg="white").place(x=330,y=580)
    sign4=Entry(sgnfrm,textvariable=sign44,font=fontr,bg="white").place(x=330,y=640)
    img11=PhotoImage(file="111.png").zoom(2,2)
    img11btn=Button(sgnfrm,border=0,command=imgbinary11,bg="white",relief=FLAT)
    img11btn.config(image=img11,width="100",height="100")
    img11btn.place(x=600,y=500)
    img22=PhotoImage(file="158.png").zoom(2,2)
    img22btn=Button(sgnfrm,border=0,command=imgbinary22,bg="white",relief=FLAT)
    img22btn.config(image=img22,width="100",height="100")
    img22btn.place(x=700,y=500)
    img33=PhotoImage(file="175.png").zoom(2,2)
    img33btn=Button(sgnfrm,border=0,command=imgbinary33,bg="white",relief=FLAT)
    img33btn.config(image=img33,width="100",height="100")
    img33btn.place(x=800,y=500)
    img44=PhotoImage(file="186.png").zoom(2,2)
    img44btn=Button(sgnfrm,border=0,command=imgbinary44,bg="white",relief=FLAT)
    img44btn.config(image=img44,width="100",height="100")
    img44btn.place(x=900,y=500)
    img55=PhotoImage(file="153.png").zoom(2,2)
    img55btn=Button(sgnfrm,border=0,command=imgbinary55,bg="white",relief=FLAT)
    img55btn.config(image=img55,width="100",height="100")
    img55btn.place(x=1000,y=500)
    img66=PhotoImage(file="136.png").zoom(2,2)
    img66btn=Button(sgnfrm,border=0,command=imgbinary66,bg="white",relief=FLAT)
    img66btn.config(image=img66,width="100",height="100")
    img66btn.place(x=1100,y=500)


    enter.configure(background='white')
    enter.mainloop()

if __name__=="__main__":
    ogsignlerf()