from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk,ImageGrab
import mysql.connector as sqlcon
import tkinter.messagebox as mb
from googletrans import Translator
from datetime import datetime,date
import random
import os

# Initialising google trans module
translator = Translator()

# Adding Mysql to program
mycon=sqlcon.connect(host='localhost',
                    user='root',
                    passwd='9@5Pra524',
                    database='BLO')
mycur=mycon.cursor()

# GUI window
root=Tk()
root.geometry('850x600')
root.resizable(0,0)
root.title('BLO Desktop')
#root.iconbitmap("E:/Python/BLO/directory/BLO_img.xbm")

#Importing all images
root_bg=PhotoImage(file="E:\Python\BLO\directory\Images\window_bg.png")
home_bg_img=PhotoImage(file="E:\Python\BLO\directory\Images\home_bg.png")
username_img=PhotoImage(file="E:\Python\BLO\directory\Images\\username.png")
password_img=PhotoImage(file="E:\Python\BLO\directory\Images\passwd.png")
verify_img=PhotoImage(file="E:\Python\BLO\directory\Images\confirm.png")
part_img=PhotoImage(file="E:\Python\BLO\directory\Images\part.png")
name_img=PhotoImage(file="E:\Python\BLO\directory\Images\\name.png")
profile_img=PhotoImage(file="E:\Python\BLO\directory\Images\profile.png")
eci_img=PhotoImage(file="E:\Python\BLO\directory\Images\eci.png")
satya_img=PhotoImage(file="E:\Python\BLO\directory\Images\satya.png")
card_bg=PhotoImage(file="E:\Python\BLO\directory\Images\card_bg_img.png")
gov_img=PhotoImage(file="E:\Python\BLO\directory\Images\gov_img.png")

# Storing details of users
new_credentials=()
verify_credentials=()

#Defining all functions
def new_account():
    global login1,number_new,password_new,part_num,name
    login1=Frame(root,width=420,height=370,bg='white')
    login1.place(x=212,y=130)
    label=Label(login1,text='Create your account',font=('Calibri','24'),bg='white')
    label.place(x=80,y=5)
    label=Label(login1,text='Number',font=('Calibri','18'),bg='white')
    label.place(x=73,y=75)
    label=Label(login1,text='Password',font=('Calibri','18'),bg='white')
    label.place(x=73,y=140)
    label=Label(login1,text='Part no.',font=('Calibri','18'),bg='white')
    label.place(x=73,y=200)
    label=Label(login1,text='Name',font=('Calibri','18'),bg='white')
    label.place(x=73,y=254)
    img_label=Label(login1,image=username_img,bg='white')
    img_label.place(x=5,y=60)
    img_label=Label(login1,image=password_img,bg='white')
    img_label.place(x=5,y=123)
    img_label=Label(login1,image=part_img,bg='white')
    img_label.place(x=5,y=184)
    img_label=Label(login1,image=name_img,bg='white')
    img_label.place(x=5,y=242)
    number_new=Entry(login1,width=18,font=('Calibri','14'))
    number_new.place(x=197,y=82)
    password_new=Entry(login1,width=18,font=('Calibri','14'))
    password_new.place(x=197,y=146)
    part_num=Entry(login1,width=18,font=('Calibri','14'))
    part_num.place(x=197,y=208)
    name=Entry(login1,width=18,font=('Calibri','14'))
    name.place(x=197,y=262)
    proceed_btn=Button(login1,text='PROCEED',command=new_register,font="calibri",fg="white",bg="#002076",border=0,padx=10,pady=5)
    proceed_btn.place(x=180,y=300) 

def new_register():
    global new_credentials
    a,b,c,d=number_new.get(),password_new.get(),part_num.get(),name.get()
    new_credentials=(int(a),str(b),int(c),str(d))
    num,passwd,part_numer,naam=new_credentials
    try:
        mycur.execute("INSERT INTO blo_cred(number,password,part_number,name) VALUES({},'{}',{},'{}')".format(num,passwd,part_numer,naam))
        mycon.commit()
        mb.showinfo('Success','Registered successful\nPlease login with same details to continue')
    except sqlcon.errors.IntegrityError:
        mb.showerror('Error','Phone number already registered\nLogin to your account')
    login1.destroy()

def login_win():
    global login, label1,label2,label3,label4,label5, img_label1,img_label2,img_label3, number, password, captcha, login_btn1,login_btn2,captcha_store,code
    window_bg_img=Label(root,image=root_bg)
    window_bg_img.place(relwidth=1,relheight=1)
    login=Frame(root,width=420,height=370,bg='white')
    login.place(x=212,y=130)
    label1=Label(login,text='Verify your account',font=('Calibri','24'),bg='white')
    label1.place(x=80,y=5)
    label2=Label(login,text='Number',font=('Calibri','18'),bg='white')
    label2.place(x=73,y=75)
    label3=Label(login,text='Password',font=('Calibri','18'),bg='white')
    label3.place(x=73,y=140)
    label4=Label(login,text='Captcha',font=('Calibri','18'),bg='white')
    label4.place(x=73,y=200)
    img_label1=Label(login,image=username_img,bg='white')
    img_label1.place(x=5,y=60)
    img_label2=Label(login,image=password_img,bg='white')
    img_label2.place(x=5,y=123)
    img_label3=Label(login,image=verify_img,bg='white')
    img_label3.place(x=5,y=190)
    number=Entry(login,width=18,font=('Calibri','14'))
    number.place(x=197,y=82)
    password=Entry(login,width=18,font=('Calibri','14'))
    password.place(x=197,y=146)
    captcha=Entry(login,width=18,font=('Calibri','14'))
    captcha.place(x=197,y=208)
    captcha_store=captcha.get()
    code=random.randint(111111,999999)
    label5=Label(login,text=code,font=('Calibri','18'),bg='white')
    label5.place(x=227,y=230)
    login_btn1=Button(login,text='LOGIN',command=store_log_cred,font="calibri",fg="white",bg="#002076",border=0,padx=10,pady=5)
    login_btn1.place(x=180,y=270)
    login_btn2=Button(login,text='CREATE AN ACCOUNT',command=new_account,font="calibri",fg="white",bg="#002076",border=0,padx=10,pady=5)
    login_btn2.place(x=128,y=315)

def chng_geo_bg():
    #root.geometry('350x350')
    bg_label=Label(root,image=home_bg_img)
    bg_label.place(relwidth=1,relheight=1)

def store_log_cred():
    global user_name
    a,b=number.get(),password.get()
    query11="SELECT * FROM blo_cred WHERE number=%s AND password=%s"
    mycur.execute(query11,(a,b))
    result=mycur.fetchone()
    user_number,user_password,user_partno,user_name=result
    if result:
        mb.showinfo('Authentication','Authentication successful')
        main_menu()
    else:
        mb.showerror('Authentication','Authentication failed')
        login.destroy()
        login_win()

def form6i():
    global form_frame, preview_image,disp_us
    form_frame=Frame(root,width=610,height=555,bg='#cef3f5')
    form_frame.place(x=20,y=27)
    photo_frame=Frame(form_frame,width=130,height=140)
    photo_frame.place(x=352,y=353)
    file_path=None

    def open_image():
        global chosen_image
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.gif")])
        if file_path:
            chosen_image=Image.open(file_path)
            chosen_image=chosen_image.resize((130,140))
            photo=ImageTk.PhotoImage(chosen_image)
            label=Label(form_frame,text=os.path.basename(file_path),font=('Calibri','13'),bg='#cef3f5',fg='Black')
            label.place(x=432,y=331)
            preview_image.config(image=photo)
            preview_image.image=photo
    preview_image=Label(photo_frame,bg='#cef3f5')
    preview_image.pack()
    img_open_btn=Button(form_frame,text='Choose image',command=open_image,font="calibri",fg="White",bg="#002076",border=0,padx=10,pady=5)
    img_open_btn.place(x=352,y=285)

    labela=Label(form_frame,text='Get your virtual card',font=('Calibri','24'),bg='#cef3f5',fg='Black')
    labela.place(x=135,y=5)
    label1=Label(form_frame,text='Name *',font=('Calibri','14'),bg='#cef3f5',fg='Black')
    label1.place(x=15,y=52)
    text1=Entry(form_frame,width=18,font=('Calibri','14'),bg='#cef3f5',fg='Black')
    text1.place(x=15,y=82)
    label2=Label(form_frame,text='Father name *',font=('Calibri','14'),bg='#cef3f5',fg='Black')
    label2.place(x=15,y=112)
    text2=Entry(form_frame,width=18,font=('Calibri','14'),bg='#cef3f5',fg='Black')
    text2.place(x=15,y=142)
    label3=Label(form_frame,text='Mobile number *',font=('Calibri','14'),bg='#cef3f5',fg='Black')
    label3.place(x=15,y=172)
    text3=Entry(form_frame,width=18,font=('Calibri','14'),bg='#cef3f5',fg='Black')
    text3.place(x=15,y=202)
    label4=Label(form_frame,text='Aadhar number *',font=('Calibri','14'),bg='#cef3f5',fg='Black')
    label4.place(x=15,y=232)
    text4=Entry(form_frame,width=18,font=('Calibri','14'),bg='#cef3f5',fg='Black')
    text4.place(x=15,y=262)
    label5=Label(form_frame,text='Date Of Birth *',font=('Calibri','14'),bg='#cef3f5',fg='Black')
    label5.place(x=15,y=292)
    text5=Entry(form_frame,width=18,font=('Calibri','14'),bg='#cef3f5',fg='Black')
    text5.place(x=15,y=325)
    label6=Label(form_frame,text='House/Apartment/\nbuilding number *',font=('Calibri','14'),bg='#cef3f5',fg='Black')
    label6.place(x=15,y=352)
    text6=Entry(form_frame,width=18,font=('Calibri','14'),bg='#cef3f5',fg='Black')
    text6.place(x=15,y=403)
    label7=Label(form_frame,text='Area/locality name *',font=('Calibri','14'),bg='#cef3f5',fg='Black')
    label7.place(x=15,y=433)
    text7=Entry(form_frame,width=18,font=('Calibri','14'),bg='#cef3f5',fg='Black')
    text7.place(x=15,y=463)
    label8=Label(form_frame,text='Gender *.',font=('Calibri','14'),bg='#cef3f5',fg='Black')
    label8.place(x=15,y=493)
    text8=Entry(form_frame,width=18,font=('Calibri','14'),bg='#cef3f5',fg='Black')
    text8.place(x=15,y=523)
    label9=Label(form_frame,text='City *',font=('Calibri','14'),bg='#cef3f5',fg='Black')
    label9.place(x=352,y=55)
    text9=Entry(form_frame,width=18,font=('Calibri','14'),bg='#cef3f5',fg='Black')
    text9.place(x=352,y=85)
    label10=Label(form_frame,text='District *',font=('Calibri','14'),bg='#cef3f5',fg='Black')
    label10.place(x=352,y=115)
    text10=Entry(form_frame,width=18,font=('Calibri','14'),bg='#cef3f5',fg='Black')
    text10.place(x=352,y=145)
    label11=Label(form_frame,text='State *',font=('Calibri','14'),bg='#cef3f5',fg='Black')
    label11.place(x=352,y=175)
    text11=Entry(form_frame,width=18,font=('Calibri','14'),bg='#cef3f5',fg='Black')
    text11.place(x=352,y=205)
    label12=Label(form_frame,text="Applicant's passport size\nphoto (well cropped) *",font=('Calibri','14'),bg='#cef3f5',fg='Black')
    label12.place(x=352,y=235)
    label13=Label(form_frame,text="Preview:",font=('Calibri','14'),bg='#cef3f5',fg='Black')
    label13.place(x=352,y=330)
       
    def exxit():
        main_menu()
        global form6i
        form_frame.destroy()
 
    def get_it():
        global chosen_image,form_frame,front_card_frame,back_card_frame,disp_us
        front_card_frame=Frame(root,width=450,height=256,bg='#15A5FD')
        front_card_frame.place(x=220,y=50)
        back_card_frame=Frame(root,width=450,height=250,bg='#15A5FD')
        back_card_frame.place(x=220,y=325)
        photo_frame=Frame(front_card_frame,width=120,height=130,bg='#15A5FD')
        photo_frame.place(x=11,y=79)   

        if chosen_image:
            chosen_image_resized=chosen_image.resize((120,130))
            photo=ImageTk.PhotoImage(chosen_image_resized)
            chosen_image_label=Label(photo_frame,image=photo)
            chosen_image_label.image=photo
            chosen_image_label.pack()
        preview_image=Label(photo_frame,bg='#15A5FD')
        preview_image.pack()
        img_label1=Label(front_card_frame,image=eci_img,bg='#15A5FD')
        img_label1.place(x=385,y=13)
        img_label2=Label(front_card_frame,image=satya_img,bg='#15A5FD')
        img_label2.place(x=15,y=8)
        epic_number_generate=str(random.randint(111111,999999))

        #Front card fillings
        label1=Label(front_card_frame,text='ELECTION COMMISSION OF INDIA',font=('Calibri','14','bold'),bg='#15A5FD',fg='Black')
        label1.place(x=85,y=28)
        label2=Label(front_card_frame,text='_______भारत निर्वाचन आयोग________',font=('Calibri','12','bold'),bg='#15A5FD',fg='Black')
        label2.place(x=85,y=8)
        epic_number=Label(front_card_frame,text='ACM'+epic_number_generate,font=('Calibri','11','bold'),bg='#15A5FD',fg='Black')
        epic_number.place(x=335,y=64)
        h_name=Label(front_card_frame,text='नाम:',font=('Calibri','11','bold'),bg='#15A5FD',fg='Black')
        h_name.place(x=140,y=75)
        e_name=Label(front_card_frame,text='Name:',font=('Calibri','13','bold'),bg='#15A5FD',fg='Black')
        e_name.place(x=140,y=93)
        h_fname=Label(front_card_frame,text='पिता का नाम:',font=('Calibri','11','bold'),bg='#15A5FD',fg='Black')
        h_fname.place(x=140,y=120)
        e_fname=Label(front_card_frame,text="Father's Name:",font=('Calibri','13','bold'),bg='#15A5FD',fg='Black')
        e_fname.place(x=140,y=138)
        eh_gen=Label(front_card_frame,text='लिंग / Gender: ',font=('Calibri','12','bold'),bg='#15A5FD',fg='Black')
        eh_gen.place(x=140,y=163)
        e_dob=Label(front_card_frame,text='Date Of Birth:',font=('Calibri','13','bold'),bg='#15A5FD',fg='Black')
        e_dob.place(x=140,y=185)
        e_label=Label(front_card_frame,text='e-Electors Photo Identity Card',font=('Calibri','12'),bg='#15A5FD',fg='Black')
        e_label.place(x=56,y=232)
        h_label=Label(front_card_frame,text='ई-मतदाता पहचान पत्र',font=('Calibri','10'),bg='#15A5FD',fg='Black')
        h_label.place(x=255,y=236)

        name_fetch=str(text1.get())
        name_translated = translator.translate(name_fetch, src='en', dest='hi').text

        fname_fetch=str(text2.get())
        fname_translated=translator.translate(fname_fetch,src='en',dest='hi').text

        gender_fetch=str(text9.get())
        gender_translated=translator.translate(gender_fetch,src='en',dest='hi').text

        dob_fetch=str(text5.get())
        dob_translated=translator.translate(dob_fetch, src='en', dest='hi').text

        place_ename=Label(front_card_frame,text=name_fetch,font=('Calibri','13'),bg='#15A5FD',fg='Black')
        place_ename.place(x=188,y=93)
        place_hname=Label(front_card_frame,text=name_translated,font=('Calibri','11'),bg='#15A5FD',fg='Black')
        place_hname.place(x=176,y=75)
        place_e_fname=Label(front_card_frame,text=fname_fetch,font=('Calibri','13'),bg='#15A5FD',fg='Black')
        place_e_fname.place(x=255,y=138)
        place_h_fname=Label(front_card_frame,text=fname_translated,font=('Calibri','11'),bg='#15A5FD',fg='Black')
        place_h_fname.place(x=234,y=120)
        place_gender=Label(front_card_frame,text=gender_fetch,font=('Calibri','13'),bg='#15A5FD',fg='Black')
        place_gender.place(x=242,y=163)
        place_dob=Label(front_card_frame,text=dob_fetch,font=('Calibri','12'),bg='#15A5FD',fg='Black')
        place_dob.place(x=240,y=187)

        #Back side fillings
        label1=Label(back_card_frame,text='पता:',font=('Calibri','11','bold'),bg='#15A5FD',fg='Black')
        label1.place(x=11,y=15)
        label2=Label(back_card_frame,text='Address:',font=('Calibri','13','bold'),bg='#15A5FD',fg='Black')
        label2.place(x=11,y=49)
        label3=Label(back_card_frame,text='Date of Generation:',font=('Calibri','13','bold'),bg='#15A5FD',fg='Black')
        label3.place(x=11,y=120)
        epic_number=Label(back_card_frame,text='EPIC number:',font=('Calibri','13','bold'),bg='#15A5FD',fg='Black')
        epic_number.place(x=11,y=91)

        add_fetch=str(text6.get())+', '+str(text7.get())+', '+str(text9.get())+', '+str(text10.get())+', '+str(text11.get())
        add_translated=translator.translate(add_fetch, src='en', dest='hi').text

        date_fetch=date.today()
        #date_translated = translator.translate(date_fetch, src='en', dest='hi').text

        place_h_address=Label(back_card_frame,text=add_translated,wraplength=500,justify='left',font=('Calibri','11'),bg='#15A5FD',fg='Black')
        place_h_address.place(x=45,y=15)
        place_e_address=Label(back_card_frame,text=add_fetch,wraplength=500,justify='left',font=('Calibri','13'),bg='#15A5FD',fg='Black')
        place_e_address.place(x=76,y=49)
        place_date=Label(back_card_frame,text=date_fetch,font=('Calibri','13'),bg='#15A5FD',fg='Black')
        place_date.place(x=156,y=120)
        place_epic_number=Label(back_card_frame,text='ACM'+epic_number_generate,font=('Calibri','13'),bg='#15A5FD',fg='Black')
        place_epic_number.place(x=110,y=91)        

        def home():
            global get_it
            front_card_frame.destroy()
            back_card_frame.destroy()
            save_card_btn.destroy()
            home_btn.destroy()
            exit_btn.destroy()
            main_menu()

        def close():
            global get_it
            front_card_frame.destroy()
            back_card_frame.destroy()
            save_card_btn.destroy()
            home_btn.destroy()
            exit_btn.destroy()
            mb.showinfo('Bye','Thanks for using,\nExiting....')
            root.destroy()

        def save_front_card_as_image():
            time=datetime.now()

            x,y,width,height=front_card_frame.winfo_rootx(),front_card_frame.winfo_rooty(),front_card_frame.winfo_width(),front_card_frame.winfo_height()
            screenshot=ImageGrab.grab(bbox=(x,y,x+width,y+height))
            time_now=time.strftime('front_%H_%M_%S.png')
            file_name=time_now
            screenshot.save(file_name)
            mb.showinfo('Image Saved',f'Front side card image is saved as {file_name}')

            x,y,width,height=back_card_frame.winfo_rootx(),back_card_frame.winfo_rooty(),back_card_frame.winfo_width(),back_card_frame.winfo_height()
            screenshot=ImageGrab.grab(bbox=(x,y,x+width,y+height))
            time_now=time.strftime('back_%H_%M_%S.png')
            file_name=time_now
            screenshot.save(file_name)
            mb.showinfo('Image Saved',f'Back side card image is saved as {file_name}')
            
        save_card_btn=Button(root,text='Save',command=save_front_card_as_image,font=('Calibri','14'),bg='#002076',fg='White',border=0,width=9)
        save_card_btn.place(x=700,y=250)
        home_btn=Button(root,text='Home',command=home,font=('Calibri','14'),bg='#002076',fg='White',border=0,width=9)
        home_btn.place(x=700,y=295)
        exit_btn=Button(root,text='Exit',command=close,font=('Calibri','14'),bg='#002076',fg='White',border=0,width=9)
        exit_btn.place(x=700,y=340)
            
        global form6i
        form_frame.destroy()
        destroy_main_screen()
        
    save_btn=Button(form_frame,text="Get it",command=get_it,font=('Calibri','14'),bg='#002076',fg='White',border=0,padx=7)
    save_btn.place(x=425,y=515)
    exit_btn=Button(form_frame,text="Exit",command=exxit,font=('Calibri','14'),bg='#002076',fg='White',border=0,padx=7)
    exit_btn.place(x=352,y=515)

    def destroy_main_screen():
        global main_menu
        f8_btn.destroy()
        disp_us.destroy()
        logout_btn.destroy()
        profile_pic_image.destroy()
    destroy_main_screen()
    
def destroy_main_screen():
    global main_menu
    f8_btn.destroy()
    disp_us.destroy()
    label.destroy()
    logout_btn.destroy()
    profile_pic_image.destroy()

def logout():
    login_win()
    destroy_main_screen()

def main_menu():
    global f6_btn,f7_btn,f8_btn,logout_btn,label,profile_pic_image
    chng_geo_bg()
    logout_btn=Button(root,text="Logout",command=logout,font=('Calibri','14'),bg='#e9bc42',bd=0)
    logout_btn.place(x=735,y=15)
    profile_pic_image=Label(root,image=profile_img,bg='#9d822e')
    profile_pic_image.place(x=3,y=3)
    disp_us=Label(root,text=user_name,font=('Calibri','15','bold'),bg='#9d822e')
    disp_us.place(x=53,y=16)
    footer=Label(root,text='Designed & Developed by XII',font=('Calibri','10','bold'),bg='#b86e31')
    footer.place(x=686,y=581)

    f8_btn=Button(root,text="Form 6i: Get instant virtual\n   voter card",command=form6i,font=('Calibri','14'),bg="#fad483",bd=0,width=21)
    f8_btn.place(x=425,y=240)

    def destroy_login():
        global login_win
        login.destroy()
    destroy_login()

login_win()
root.mainloop()
mycon.close()