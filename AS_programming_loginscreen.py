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
c.execute("""CREATE TABLE users (
				username text,
				password text
				)""")
'''

update_frame = tkinter.Frame(root, bg ="white", width =500, height =500)

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


def forgot_system():

    conn = sqlite3.connect('Badmington_club.db')

    c = conn.cursor()

    forgot_username = simpledialog.askstring("Info", "Enter your username")
    forgot_password = simpledialog.askstring("Info", "Enter your old password")

    isValid = True
    isValid = isValid and validate_username(forgot_username, "Username")
    isValid = isValid and validate_not_empty(forgot_password, "Password")

    if isValid:
        user_email.sendEmail("hello","from joe","josnoble113@gmail.com")

    conn.commit()
    conn.close()

def open_update_frame():
    raise_frame(update_frame)

def login_update():
    conn = sqlite3.connect('Badmington_club.db')

    c = conn.cursor()

    open_update_frame()
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

def show_password(bruh):
    password_entry.config(show="")

def dont_show_password(bruh):
    password_entry.config(show="*")

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

login_button = tkinter.Button(root, text="Login", command=login_submit, fg='white', bg='black', relief='groove', font=('Segoe UI Black', 14, 'bold'), padx=30)
login_button.place(rely=0.9, relx=0.2, anchor='center')

update_button = tkinter.Button(root, text="Update", command=login_update, fg='white', bg='black', relief='groove', font=('Segoe UI Black', 14, 'bold'), padx=30)
update_button.place(rely=0.9, relx=0.5, anchor='center')

clear_button = tkinter.Button(root, text="Clear", command=login_clear, fg='white', bg='black', relief='groove', font=('Segoe UI Black', 14, 'bold'), padx=30)
clear_button.place(rely=0.9, relx=0.8, anchor='center')

root.mainloop()
