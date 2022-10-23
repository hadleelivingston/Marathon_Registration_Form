from cgitb import text
from ctypes import alignment, sizeof
import tkinter
from tkinter import END, StringVar, ttk
from tkinter import messagebox
from turtle import color
window=tkinter.Tk()
window.title('Marathon Registration Form')
window.geometry('500x600')
window.resizable(False,False)
window['bg']='#C6ECCF'

def submitted():
    first_Name=first_name_info.get()
    last_name=last_name_info.get()
    Email=email_info.get()
    phone=phone_info.get()
    DOB=dob_info.get()
    gender=gender_info.get()
    distance=distance_info.get()

    if first_Name=='':
        messagebox.showerror('Error','Please Enter your Full Name')
    elif last_name=='':
        messagebox.showerror('Error','Please Enter your Full Name')
    elif Email=='':
        messagebox.showerror('Error','Please Enter  valid E-mail Adress')
    elif phone=='':
        messagebox.showerror('Error','Please Enter your Phone Number')
    elif DOB=='':
        messagebox.showerror('Error','Please Enter your Date of Birth')
    elif gender=='':
        messagebox.showerror('Error','Please Select your Gender')
    elif distance=='':
        messagebox.showerror('Error','Please Select the Marathon Categorie')


    with open(first_Name+'.txt','w') as f:
        f.write('Name : '+ first_Name + last_name + '\n')
        f.write('E-mail : '+ Email + '\n')
        f.write('Phone No : '+ phone + '\n')
        f.write('DOB : '+ DOB + '\n')
        if gender=='Male':
            f.write('Gender : ' + 'Male' + '\n')
        elif gender=='Female':
            f.write('Gender : ' + 'Female' + '\n')
        else:
            f.write('Gender : ' + 'Other' + '\n')
        f.write('Distance : ' + distance )



def cleared():
    name_e1.delete(0,END)
    name_e2.delete(0,END)
    phone_e1.delete(0,END)
    dob_e1.delete(0,END)
    distance_cb1.delete(0,END)
    email_e1.delete(0,END)
space_1=tkinter.Label(window,text='     ',font='Arial 8',bg='#C6ECCF')
space_1.pack()
img_marathon=tkinter.PhotoImage(file=r"C:\Users\hp\Downloads\Marathon.png").subsample(5,5)
img_1=tkinter.Label(window,image=img_marathon)
img_1.pack()
space_2=tkinter.Label(window,text='     ',font='Arial 8',bg='#C6ECCF')
space_2.pack()
heading=tkinter.Label(window,text='MARATHON REGISTRATION FORM',font='Constantia 15 bold')
heading.pack()
# def variable 
first_name_info=StringVar()
last_name_info=StringVar()
email_info=StringVar()
phone_info=StringVar()
dob_info=StringVar()
gender_info=StringVar()
distance_info=StringVar()
#Name
name_l1=tkinter.Label(window,text='Name',font='Lora 10 bold')
name_l1.place(x=50,y=200)
name_l2=tkinter.Label(window,text='*',fg='red')
name_l2.place(x=90,y=200)
name_e1=tkinter.Entry(window,width=30,bd=4,textvariable=first_name_info)
name_e1.place(x=50,y=230)
name_e2=tkinter.Entry(window,width=30,bd=4,textvariable=last_name_info)
name_e2.place(x=250,y=230)
name_l3=tkinter.Label(window,text='First Name',font='Arial 7')
name_l3.place(x=50,y=260)
name_l4=tkinter.Label(window,text='Last Name',font='Arial 7')
name_l4.place(x=250,y=260)
#E-mail
email_l1=tkinter.Label(window,text='Email',font='Lora 10 bold')
email_l1.place(x=50,y=290)
email_l2=tkinter.Label(window,text='*',fg='red')
email_l2.place(x=90,y=290)
email_e1=tkinter.Entry(window,width=30,bd=4,textvariable=email_info)
email_e1.place(x=50,y=320)
email_l3=tkinter.Label(window,text='example@example.com',font='Arial 7')
email_l3.place(x=50,y=350)
#Phone Number
phone_l1=tkinter.Label(window,text='Phone No',font='Lora 10 bold')
phone_l1.place(x=250,y=290)
phone_l2=tkinter.Label(window,text='*',fg='red')
phone_l2.place(x=315,y=290)
phone_e1=tkinter.Entry(window,width=30,bd=4,textvariable=phone_info)
phone_e1.place(x=250,y=320)
phone_l3=tkinter.Label(window,text='Please Enter a valid Phone Number',font='Arial 7')
phone_l3.place(x=250,y=350)
#DOB
dob_l1=tkinter.Label(window,text='Date',font='Lora 10 bold')
dob_l1.place(x=50,y=380)
dob_l2=tkinter.Label(window,text='*',fg='red')
dob_l2.place(x=85,y=380)
dob_e1=tkinter.Entry(window,width=30,bd=4,textvariable=dob_info)
dob_e1.place(x=50,y=410)
dob_l3=tkinter.Label(window,text='DD-MM-YYYY',font='Arial 7')
dob_l3.place(x=50,y=440)
#gender
gender_l1=tkinter.Label(window,text='Gender',font='Lora 10 bold')
gender_l1.place(x=250,y=380)
gender_l2=tkinter.Label(window,text='*',fg='red')
gender_l2.place(x=300,y=380)
gender_rb1=tkinter.Radiobutton(window,text='Male',value='Male',bd=3,variable=gender_info)
gender_rb1.place(x=250,y=410)
gender_rb2=tkinter.Radiobutton(window,text='Female',value='Female',bd=3,variable=gender_info)
gender_rb2.place(x=310,y=410)
gender_rb3=tkinter.Radiobutton(window,text='Other',value='Other',bd=3,variable=gender_info)
gender_rb3.place(x=380,y=410)

#marathon distance
distance_l1=tkinter.Label(window,text='Marathon Distance',font='Lora 10 bold')
distance_l1.place(x=50,y=470)
distance_cb1=ttk.Combobox(window,width=20,textvariable=distance_info)
distance_cb1['values']=('5 Km','10 Km','21 Km','42 Km')
distance_cb1.current(2)
distance_cb1.place(x=50,y=500)
#submit and clear
submit_b1=tkinter.Button(window,text='Submit',font='Lora 11 bold',width=9,bd=4,command=submitted)
submit_b1.place(x=250,y=490)
clear_b1=tkinter.Button(window,text='Clear',font='Lora 11 bold',width=6,bd=4,command=cleared)
clear_b1.place(x=380,y=490)
window.mainloop()