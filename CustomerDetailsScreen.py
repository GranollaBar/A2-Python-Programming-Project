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
from functools import partial

customer = Tk()
customer.geometry('600x600')

header = Frame(customer, bg='green')
content = Frame(customer, bg='red')

customer.columnconfigure(0, weight=1)

customer.rowconfigure(0, weight=2)
customer.rowconfigure(1, weight=8)

header.grid(row=0, sticky="nsew")
content.grid(row=1, sticky="nsew")



root = tkinter.Tk()
root.title('Lisburn Raquets Club')
root.geometry('500x550')
root.configure(bg='white')

conn = sqlite3.connect('Badmington_club.db')

c = conn.cursor()


c.execute("""CREATE TABLE member (
            username text,
            password text,
            user_type text
            )""")


def createAccount():
	global account_password_entry
	global account_password2_entry

	username = StringVar()
	password = StringVar()
	repassword = StringVar()
	user_ending=StringVar()

	raise_frame(createAccountFrame)
	title_label = tkinter.Label(createAccountFrame, text="Create Racquets Account", font=('Verdana', 24, 'underline', 'bold'), fg='red', bg='white')
	title_label.place(rely=0.08, relx=0.5, anchor='center')

	username_label = tkinter.Label(createAccountFrame, text="Username:", font=('Georgia', 20, 'bold'), fg='black', bg='white')
	username_label.place(rely=0.25, relx=0.26, anchor='center')

	password_label = tkinter.Label(createAccountFrame, text="Password:", font=('Georgia', 20, 'bold'), fg='black', bg='white')
	password_label.place(rely=0.4, relx=0.265, anchor='center')

	password2_label = tkinter.Label(createAccountFrame, text="RePassword:", font=('Georgia', 20, 'bold'), fg='black', bg='white')
	password2_label.place(rely=0.55, relx=0.27, anchor='center')

	user_type_label = tkinter.Label(createAccountFrame, text="Type of User:", font=('Georgia', 20, 'bold'), fg='black', bg='white')
	user_type_label.place(rely=0.7, relx=0.265, anchor='center')

	account_username_entry = tkinter.Entry(createAccountFrame, width=25, borderwidth=2, textvariable=username)
	account_username_entry.place(rely=0.256, relx=0.66, anchor='center')

	account_password_entry = tkinter.Entry(createAccountFrame, width=25, show="*", borderwidth=2, textvariable=password)
	account_password_entry.place(rely=0.406, relx=0.66, anchor='center')

	account_password2_entry = tkinter.Entry(createAccountFrame, width=25, show="*", borderwidth=2, textvariable=repassword)
	account_password2_entry.place(rely=0.556, relx=0.66, anchor='center')

	user_choice =['Member','Coach','Organiser']
	user_ending.set('Member')
	popmenu_email = OptionMenu(createAccountFrame,user_ending,*user_choice)
	popmenu_email.config(width=20)
	popmenu_email.place(rely=0.706, relx=0.66, anchor='center')

	def completeAccount():
		saveAccountDetails(username.get(), password.get(), repassword.get(), user_ending.get())

	create_account_button = tkinter.Button(createAccountFrame, text="Save Details", command=completeAccount, fg='white', bg='black', relief='groove', font=('Segoe UI Black', 14, 'bold'), padx=40)
	create_account_button.place(rely=0.9, relx=0.5, anchor='center')



def saveAccountDetails(account_username_entry, account_password_entry, account_password2_entry, user_ending):
	conn = sqlite3.connect('Badmington_club.db')

	c = conn.cursor()

	isValid = True
	isValid = isValid and validate_username(account_username_entry, "Username")
	isValid = isValid and validate_not_empty(account_password_entry, "Password")
	isValid = isValid and validate_repassword(account_password2_entry, "RePassword", account_password_entry)

	if isValid:
		account_user_username = account_username_entry
		account_user_password = account_password_entry
		account_user_ending = user_ending


		response = askyesno("Are you sure?", "Are you sure that all information above is correct?")
		if response == False:
			showinfo("Info", "submition cancelled")

		else:

			c.execute("INSERT INTO account VALUES (:username, :password, :User_Type)",
					  {
						  'username': account_user_username,
						  'password': account_user_password,
						  'User_Type': account_user_ending
					  })

			messagebox.showinfo("info", "Details have been saved successfully")
			messagebox.showinfo("info", "Details are shown below" + "\n" + "\n" + "Username: " + account_user_username + "\n" + "Password: " + account_user_password+ "\n" + "User Type: " + account_user_ending)

		'''
          account_username_entry.set('')
          account_password_entry.setText("")
          account_password2_entry.setText("")
          user_ending.setText("")
          '''

		conn.commit()
		conn.close()


title_label = tkinter.Label(root, text="", font=('Verdana', 20, 'underline', 'bold'), fg='black', bg='white')
title_label.place(rely=0.06, relx=0.5, anchor='center')

customer.mainloop()

