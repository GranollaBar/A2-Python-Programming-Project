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
import math
import member_email
import memberWordDocument

member = Tk()
member.geometry('900x600')

header = Frame(member, bg='pale green')
content = Frame(member, bg='white')

member.columnconfigure(0, weight=1)

member.rowconfigure(0, weight=1)
member.rowconfigure(1, weight=9)

header.grid(row=0, sticky="nsew")
content.grid(row=1, sticky="nsew")

conn = sqlite3.connect('Badmington_club.db')

c = conn.cursor()

'''
c.execute("""CREATE TABLE member (
            username text,
            password text,
            firstname text,
            surname text,
            address text,
            postcode text,
            age integer,
            member_group integer
            )""")
'''

def validate_password(value, fieldname):
	if (value == ''):
		messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " Can Not Be Empty")
		return False
	if (len(value) < 8):
		messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " Must have between 8 and 15 characters")
		return False
	if (len(value) > 15):
		messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " Must have between 8 and 15 characters")
		return False

	return True


def validate_username(value, fieldname):
	if (value == ''):
		messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " Can Not Be empty")
		return False
	if ('@' not in value):
		messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " must contain @")
		return False
	if ('.' not in value):
		messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " must contain a .")
		return False

	return True

def validate_not_empty_string(value, fieldname):
	if (value == ""):
		messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " Can Not Be Empty")
		return False
	if (value.isdigit()):
		messagebox.showinfo("Validation Error", "The Value for Field " + fieldname + " Can not Contain Whole Numbers")
		return False
	if (len(value) >15):
		messagebox.showinfo("Validation Error", "The Value for Field " + fieldname + " Can only Contain a max of 15 characters")
		return False

	return True

def validate_empty(value, fieldname):
	if (value == ''):
		messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " Can Not Be Empty")
		return False

	return True

def validate_age(value, fieldname):
	if (int(value) >100):
		messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " Can Not Be over 100")
		return False
	if (value ==''):
		messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " Can Not Be empty")
		return False

	return True

def ageToGroup(value):
	return math.ceil(value.get()/5)

def treeviewPopulate():
	pass

def deleteAccountDetails():
	pass


def updateAccountDetails():
	pass

def searchAccountDetails():
	pass



def saveAccountDetails():
	conn = sqlite3.connect('Badmington_club.db')

	c = conn.cursor()

	isValid = True
	isValid = isValid and validate_username(username.get(), "Username")
	isValid = isValid and validate_password(password.get(), "Password")
	isValid = isValid and validate_not_empty_string(firstname.get(), "Firstname")
	isValid = isValid and validate_not_empty_string(surname.get(), "Surname")
	isValid = isValid and validate_empty(address.get(), "Address")
	isValid = isValid and validate_empty(postcode.get(), "Postcode")
	isValid = isValid and validate_age(age.get(), "Age")

	if isValid:
		account_username = username.get()
		account_password = password.get()
		account_firstname = firstname.get()
		account_surname = surname.get()
		account_address = address.get()
		account_postcode = postcode.get()
		account_age = age.get()

		account_group = ageToGroup(age)

		response = askyesno("Are you sure?", "Are you sure that all information above is correct?")
		if response == False:
			showinfo("Info", "submition cancelled")

		else:

			memberWordDocument.sendMemberDocument(account_username,account_password,account_firstname,account_surname,account_address,account_postcode,account_age,account_group)
			found = member_email("Lisburn Racquets Account Added","You have been accepted into Lisburn Raquets Club." + "\n" + "Your details can be found in the document below." + "\n\n" + "Thanks for choosing Lisburn Racquets Club", account_username)
			if found:

				c.execute("INSERT INTO member VALUES (:username, :password, :firstname, :surname, :address, :postcode, :age, :member_group)",
						  {
							  'username': account_username,
							  'password': account_password,
							  'firstname': account_firstname,
							  'surname': account_surname,
							  'address': account_address,
							  'postcode': account_postcode,
							  'age': account_age,
							  'member_group': account_group,
						  })

				username.set('')
				password.set('')
				firstname.set('')
				surname.set('')
				address.set('')
				postcode.set('')
				age.set('')


		conn.commit()
		conn.close()







def selection():
	pass

global account_password_entry
global account_password2_entry

username = StringVar()
password = StringVar()
firstname=StringVar()
surname=StringVar()
address=StringVar()
postcode=StringVar()
age=IntVar()


username_label = tkinter.Label(member, text="Username:", font=('Georgia', 14, 'bold'), fg='black', bg='white')
username_label.place(rely=0.15, relx=0.09, anchor='center')

password_label = tkinter.Label(member, text="Password:", font=('Georgia', 14, 'bold'), fg='black', bg='white')
password_label.place(rely=0.23, relx=0.09, anchor='center')

firstname_label = tkinter.Label(member, text="Firstname:", font=('Georgia', 14, 'bold'), fg='black', bg='white')
firstname_label.place(rely=0.152, relx=0.43, anchor='center')

surname_label = tkinter.Label(member, text="Surname:", font=('Georgia', 14, 'bold'), fg='black', bg='white')
surname_label.place(rely=0.231, relx=0.36, anchor='center')

address_label = tkinter.Label(member, text="Address:", font=('Georgia', 14, 'bold'), fg='black', bg='white')
address_label.place(rely=0.152, relx=0.7, anchor='center')

postcode_label = tkinter.Label(member, text="Postcode:", font=('Georgia', 14, 'bold'), fg='black', bg='white')
postcode_label.place(rely=0.231, relx=0.64, anchor='center')

age_label = tkinter.Label(member, text="Age:", font=('Georgia', 14, 'bold'), fg='black', bg='white')
age_label.place(rely=0.231, relx=0.85, anchor='center')

username_entry = tkinter.Entry(member, width=25, textvariable=username, bd=2, relief='ridge')
username_entry.place(rely=0.153, relx=0.25, anchor='center')

password_entry = tkinter.Entry(member, width=15, textvariable=password, bd=2, relief='ridge')
password_entry.place(rely=0.233, relx=0.217, anchor='center')

firstname_entry = tkinter.Entry(member, width=15, textvariable=firstname, bd=2, relief='ridge')
firstname_entry.place(rely=0.155, relx=0.56, anchor='center')

surname_entry = tkinter.Entry(member, width=15, textvariable=surname, bd=2, relief='ridge')
surname_entry.place(rely=0.235, relx=0.483, anchor='center')

address_entry = tkinter.Entry(member, width=25, textvariable=address, bd=2, relief='ridge')
address_entry.place(rely=0.155, relx=0.85, anchor='center')

postcode_entry = tkinter.Entry(member, width=10, textvariable=postcode, bd=2, relief='ridge')
postcode_entry.place(rely=0.234, relx=0.743, anchor='center')

age_entry = tkinter.Entry(member, width=4, textvariable=age, bd=2, relief='ridge')
age_entry.place(rely=0.233, relx=0.905, anchor='center')
age.set('')

delete_button = tkinter.Button(member, text="Delete Member", command=deleteAccountDetails, fg='white', bg='black', bd=4, relief='ridge', font=('Segoe UI Black', 11, 'bold'), padx=20)
delete_button.place(rely=0.35, relx=0.15, anchor='center')

update_button = tkinter.Button(member, text="Update Member", command=updateAccountDetails, fg='white', bg='black', bd=4, relief='ridge', font=('Segoe UI Black', 11, 'bold'), padx=20)
update_button.place(rely=0.35, relx=0.39, anchor='center')

clear_button = tkinter.Button(member, text="Clear Details", command=searchAccountDetails, fg='white', bg='black', bd=4, relief='ridge', font=('Segoe UI Black', 11, 'bold'), padx=20)
clear_button.place(rely=0.35, relx=0.625, anchor='center')

create_button = tkinter.Button(member, text="Save Member", command=saveAccountDetails, fg='white', bg='black', bd=4, relief='ridge', font=('Segoe UI Black', 11, 'bold'), padx=20)
create_button.place(rely=0.35, relx=0.85, anchor='center')


member_search_Tv=ttk.Treeview(member,height=14,columns=('Password','Firstname','Surname','Address','Postcode','Age','Group'))
member_search_Tv.place(relx=0.5,rely=0.69,anchor=CENTER)


member_search_Tv.heading("#0",text='Username')
member_search_Tv.column("#0",minwidth=0,width=140)
member_search_Tv.heading("#1",text='Password')
member_search_Tv.column("#1",minwidth=0,width=90)
member_search_Tv.heading("#2",text='Firstname')
member_search_Tv.column("#2",minwidth=0,width=100)
member_search_Tv.heading("#3",text='Surname')
member_search_Tv.column("#3",minwidth=0,width=100)
member_search_Tv.heading("#4",text='Address')
member_search_Tv.column("#4",minwidth=0,width=140)
member_search_Tv.heading("#5",text='Postcode')
member_search_Tv.column("#5",minwidth=0,width=90)
member_search_Tv.heading("#6",text='Age')
member_search_Tv.column("#6",minwidth=0,width=50)
member_search_Tv.heading("#7",text='Group')
member_search_Tv.column("#7",minwidth=0,width=80)

student_ysearch_scrollbar = Scrollbar(member, orient = 'vertical', command = member_search_Tv.yview)
student_ysearch_scrollbar.place(relx=0.94,rely=0.69,anchor='center',height=307)
member_search_Tv.configure(yscrollcommand=student_ysearch_scrollbar.set)

member_search_Tv.bind("<ButtonRelease-1>", selection)



member.mainloop()

