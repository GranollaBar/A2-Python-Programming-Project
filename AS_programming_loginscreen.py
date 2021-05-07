import tkinter
from tkinter import ttk
from tkinter import messagebox, END
import csv
import random
import tkinter.simpledialog
import math
import datetime
import string
import time
from tkinter.messagebox import showinfo
from tkinter.messagebox import askyesno
import sqlite3
from tkinter.ttk import Combobox
from tkinter import simpledialog
from tkcalendar import Calendar, DateEntry
import tkinter as tk
from tkinter import *

import user_email

root = tkinter.Tk()
root.title('Lisburn Raquets Club')
root.geometry('500x500')
root.configure(bg='white')

conn = sqlite3.connect('Badmington_club.db')

c = conn.cursor()

def raise_frame(frame_name):
    frame_name.tkraise()

'''
c.execute("""CREATE TABLE account (
				username text,
				password text,
				password_hint text
				)""")
'''

createAccountFrame = tkinter.Frame(root, bg ="white", width =500, height =500)

update_frame = tkinter.Frame(root, bg ="white", width =500, height =500)

for frame in(createAccountFrame,update_frame):
    frame.grid(row = 0 , column=0,sticky='nesw')

username = tkinter.StringVar()
password = tkinter.StringVar()

def validate_not_empty(value, fieldname):
    if (value == ''):
        messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " Can Not Be Empty")
        return False

    return True


def validate_username(value, fieldname):
    if ('@gmail.com' not in value):
        messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " must contain @gmail.com")
        return False
    if (value.isdigit()):
        messagebox.showinfo("Validation Error", "The Value for Field " + fieldname + " Can not Contain Whole Numbers")
        return False
    if (value == ''):
        messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " Can Not Be empty")

    return True

def validate_repassword(value, fieldname):
    if (value != account_password_entry):
        messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " must be the same as first password")
        return False
    if (value.isdigit()):
        messagebox.showinfo("Validation Error", "The Value for Field " + fieldname + " Can not Contain Whole Numbers")
        return False
    if (value == ''):
        messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " Can Not Be empty")

    return True

def forgot_system():

    conn = sqlite3.connect('Badmington_club.db')

    c = conn.cursor()

    verificationCode = random.randint(100000,999999)

    recipient = tkinter.simpledialog.askstring("Info","Enter the username of the password you want to change")
    if recipient == '' or recipient.isnumeric() == True or len(recipient) >30:
        messagebox.showinfo("Info","The recipient email entered did not comply with the rules", icon="error")

    else:
        found = user_email.sendEmail("Lisburn Racquets Verification code","\n" + "This is an automated message sent from Lisburn Racquet's Club" + "\n" + "The verification code to change passwords is " + "\n\n" + str(verificationCode) + "\n\n" + "Please do not respond to this email",recipient)
        if found:

            forgot_password=Toplevel(bg="white")

            title_label = tkinter.Label(forgot_password, text="Forgot Password System", font=('Verdana', 14, 'underline', 'bold'), fg='red', bg='white')
            title_label.place(rely=0.08, relx=0.5, anchor='center')

            verification_label = Label(forgot_password,text = 'Verification Code:', fg ='black', bg='white', font = ('Verdana',10,'bold'))
            verification_label.place(rely=0.3,relx=0.25,anchor=CENTER)

            newpassword_label = Label(forgot_password,text = 'New password:', fg ='black', bg='white', font = ('Verdana',10,'bold'))
            newpassword_label.place(rely=0.5,relx=0.3,anchor=CENTER)

            newpassword2_label = Label(forgot_password,text = 'Re New password:', fg ='black', bg='white', font = ('Verdana',10,'bold'))
            newpassword2_label.place(rely=0.7,relx=0.25,anchor=CENTER)

            newpassword_entry = Entry(forgot_password,width=15, borderwidth=2)
            newpassword_entry.place(rely=0.225,relx=0.7,anchor=CENTER)

            username_entry = tkinter.Entry(root, width=30, borderwidth=2)
            username_entry.place(rely=0.306, relx=0.66, anchor='center')

            newpassword_button=Button(forgot_password,text = 'Update Password', command = newPasswordUpdate, fg ='white', bg='black', relief= 'groove', font = ('Verdana',10,'bold'), padx =20)
            newpassword_button.place(rely=0.9,relx=0.5,anchor=CENTER)



    conn.commit()
    conn.close()

def newPasswordUpdate():
    pass


def createAccount():
    conn = sqlite3.connect('Badmington_club.db')
    c = conn.cursor()

    global account_username_entry
    global account_password_entry
    global account_password2_entry
    global account_password_hint_entry

    raise_frame(createAccountFrame)
    title_label = tkinter.Label(createAccountFrame, text="Create Racquets Account", font=('Verdana', 24, 'underline', 'bold'), fg='red', bg='white')
    title_label.place(rely=0.08, relx=0.5, anchor='center')

    username_label = tkinter.Label(createAccountFrame, text="Username:", font=('Georgia', 20, 'bold'), fg='black', bg='white')
    username_label.place(rely=0.3, relx=0.26, anchor='center')

    password_label = tkinter.Label(createAccountFrame, text="Password:", font=('Georgia', 20, 'bold'), fg='black', bg='white')
    password_label.place(rely=0.45, relx=0.265, anchor='center')

    password2_label = tkinter.Label(createAccountFrame, text="RePassword:", font=('Georgia', 20, 'bold'), fg='black', bg='white')
    password2_label.place(rely=0.6, relx=0.27, anchor='center')

    password_hint_label = tkinter.Label(createAccountFrame, text="Password Hint:", font=('Georgia', 20, 'bold'), fg='black', bg='white')
    password_hint_label.place(rely=0.75, relx=0.265, anchor='center')

    account_username_entry = tkinter.Entry(createAccountFrame, width=25, borderwidth=2)
    account_username_entry.place(rely=0.306, relx=0.66, anchor='center')

    account_password_entry = tkinter.Entry(createAccountFrame, width=25, show="*", borderwidth=2)
    account_password_entry.place(rely=0.456, relx=0.66, anchor='center')

    account_password2_entry = tkinter.Entry(createAccountFrame, width=25, show="*", borderwidth=2)
    account_password2_entry.place(rely=0.606, relx=0.66, anchor='center')

    account_password_hint_entry = tkinter.Entry(createAccountFrame, width=25, borderwidth=2)
    account_password_hint_entry.place(rely=0.756, relx=0.66, anchor='center')

    accountpassword_button_image = PhotoImage(file='eye.png')
    accountimage_label = Label(image=accountpassword_button_image)

    password_button = Button(createAccountFrame, image=accountpassword_button_image, borderwidth=3)
    password_button.place(rely=0.606, relx=0.885, anchor='center')
    password_button.bind("<ButtonRelease-1>", show_2password)

    accountnotpassword_button_image = PhotoImage(file='noteye.png')
    accountnotimage_label = Label(image=accountnotpassword_button_image)

    notpassword_button = Button(createAccountFrame, image=accountnotpassword_button_image, borderwidth=3)
    notpassword_button.place(rely=0.606, relx=0.955, anchor='center')
    notpassword_button.bind("<ButtonRelease-1>", dont_show_2password)

    create_account_button = tkinter.Button(createAccountFrame, text="Save Details", command=saveAccountDetails, fg='white', bg='black', relief='groove', font=('Segoe UI Black', 14, 'bold'), padx=40)
    create_account_button.place(rely=0.9, relx=0.5, anchor='center')


    conn.commit()
    conn.close()

def saveAccountDetails():
    conn = sqlite3.connect('Badmington_club.db')

    c = conn.cursor()

    isValid = True
    isValid = isValid and validate_username(account_username_entry.get(), "Username")
    isValid = isValid and validate_not_empty(account_password_entry.get(), "Password")
    isValid = isValid and validate_repassword(account_password2_entry.get(), "RePassword")
    isValid = isValid and validate_not_empty(account_password_hint_entry.get(), "Password Hint")

    if isValid:
        account_user_username = account_username_entry.get()
        account_user_password = account_password_entry.get()
        account_user_hint_password = account_password_hint_entry.get()

        response = askyesno("Are you sure?", "Are you sure that all information above is correct?")
        if response == False:
            showinfo("Info", "submition cancelled")

        else:

            c.execute("INSERT INTO users VALUES (:username, :password, :Password Hint)",
                      {
                          'username': account_user_username,
                          'password': account_user_password,
                          'Password Hint': account_user_hint_password
                      })

            messagebox.showinfo("info", "Details have been saved successfully")
            messagebox.showinfo("info", "Details are shown below" + "\n" + "\n" + "Username: " + account_user_username + "\n" + "Password: " + account_user_password+ "\n" + "Password Hint: " + account_user_hint_password)

        conn.commit()
        conn.close()

        username_entry.delete(0, END)
        password_entry.delete(0, END)



def login_update():
    conn = sqlite3.connect('Badmington_club.db')

    c = conn.cursor()

    raise_frame(update_frame)
    print('hello')

    conn.commit()
    conn.close()

def login_submit():
    conn = sqlite3.connect('Badmington_club.db')

    c = conn.cursor()

    isValid = True
    isValid = isValid and validate_username(username_entry.get(), "Username")
    isValid = isValid and validate_not_empty(password_entry.get(), "Password")

    if isValid:
        user_username = username_entry.get()
        user_password = password_entry.get()

        response = askyesno("Are you sure?", "Are you sure that all information above is correct?")
        if response == False:
            showinfo("Info", "submition cancelled")

        else:

            c.execute("INSERT INTO users VALUES (:username, :password)",
                      {
                          'username': user_username,
                          'password': user_password
                      })

            messagebox.showinfo("info", "Details have been saved successfully")
            messagebox.showinfo("info", "Details are shown below" + "\n" + "\n" + "Username: " + user_username + "\n" + "Password: " + user_password)

        conn.commit()
        conn.close()

        username_entry.delete(0, END)
        password_entry.delete(0, END)


def login_clear():
    response = askyesno("Are you sure?", "Do you want to clear all details entered so far")
    if response == False:
        showinfo("Info", "clearance cancelled")

    else:

        username_entry.delete(0, END)
        password_entry.delete(0, END)

def show_password(self):
    password_entry.config(show="")

def dont_show_password(self):
    password_entry.config(show="*")


def show_2password(self):
    account_password_entry.config(show="")
    account_password2_entry.config(show="")

def dont_show_2password(self):
    account_password_entry.config(show="*")
    account_password2_entry.config(show="*")

title_label = tkinter.Label(root, text="Racquets Club Login", font=('Verdana', 24, 'underline', 'bold'), fg='red', bg='white')
title_label.place(rely=0.08, relx=0.5, anchor='center')

username_label = tkinter.Label(root, text="Username:", font=('Georgia', 20, 'bold'), fg='black', bg='white')
username_label.place(rely=0.3, relx=0.295, anchor='center')

password_label = tkinter.Label(root, text="Password:", font=('Georgia', 20, 'bold'), fg='black', bg='white')
password_label.place(rely=0.45, relx=0.3, anchor='center')

username_entry = tkinter.Entry(root, width=30, borderwidth=2)
username_entry.place(rely=0.306, relx=0.66, anchor='center')

password_entry = tkinter.Entry(root, width=30, show="*", borderwidth=2)
password_entry.place(rely=0.456, relx=0.66, anchor='center')


password_button_image = PhotoImage(file='eye.png')
image_label = Label(image=password_button_image)

password_button = Button(root, image=password_button_image, borderwidth=3)
password_button.place(rely=0.454, relx=0.885, anchor='center')
password_button.bind("<ButtonRelease-1>", show_password)

notpassword_button_image = PhotoImage(file='noteye.png')
notimage_label = Label(image=notpassword_button_image)

notpassword_button = Button(root, image=notpassword_button_image, borderwidth=3)
notpassword_button.place(rely=0.454, relx=0.955, anchor='center')
notpassword_button.bind("<ButtonRelease-1>", dont_show_password)


forgot_password_button = tkinter.Button(root, text="Forgot Password", command=forgot_system, fg='white', bg='black', relief='groove', font=('Segoe UI Black', 11, 'bold'), padx=10)
forgot_password_button.place(rely=0.6, relx=0.5, anchor='center')

create_account_button = tkinter.Button(root, text="Create Account", command=createAccount, fg='white', bg='black', relief='groove', font=('Segoe UI Black', 11, 'bold'), padx=10)
create_account_button.place(rely=0.7, relx=0.5, anchor='center')

login_button = tkinter.Button(root, text="Login", command=login_submit, fg='white', bg='black', relief='groove', font=('Segoe UI Black', 14, 'bold'), padx=30)
login_button.place(rely=0.9, relx=0.2, anchor='center')

update_button = tkinter.Button(root, text="Update", command=login_update, fg='white', bg='black', relief='groove', font=('Segoe UI Black', 14, 'bold'), padx=30)
update_button.place(rely=0.9, relx=0.5, anchor='center')

clear_button = tkinter.Button(root, text="Clear", command=login_clear, fg='white', bg='black', relief='groove', font=('Segoe UI Black', 14, 'bold'), padx=30)
clear_button.place(rely=0.9, relx=0.8, anchor='center')

root.mainloop()
