from tkinter import ttk
from tkinter import messagebox
import tkinter.simpledialog
from tkinter.messagebox import showinfo
from tkinter.messagebox import askyesno
import sqlite3
from tkinter import simpledialog
from tkinter import *
import math
from Common.ScreenHeader import getHeader
from functools import partial

from CustomerFrame.member_email import memberEmail
from CustomerFrame.memberWordDocument import buildMemberDocument

member = Tk()
member.geometry('900x600')

header = getHeader(member)
content = Frame(member, bg='white')

member.columnconfigure(0, weight=1)

member.rowconfigure(0, weight=1)
member.rowconfigure(1, weight=9)

header.grid(row=0, sticky="nsew")
content.grid(row=1, sticky="nsew")

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

def raise_frame(frame_name):
	frame_name.tkraise()

def memberOpen():
	member.mainloop()


def validate_password(value, fieldname, label):
	if (value == ''):
		label.config(fg="red")
		messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " Can Not Be Empty")
		return False
	if (len(value) < 8):
		label.config(fg="red")
		messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " Must have between 8 and 15 characters")
		return False
	if (len(value) > 15):
		label.config(fg="red")
		messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " Must have between 8 and 15 characters")
		return False

	label.config(fg="SpringGreen3")
	return True


def validate_username(value, fieldname, label):
	if (value == ''):
		label.config(fg="red")
		messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " Can Not Be empty")
		return False

	if ('@' not in value):
		label.config(fg="red")
		messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " must contain @")
		return False

	if ('.' not in value):
		label.config(fg="red")
		messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " must contain a .")
		return False

	label.config(fg="SpringGreen3")
	return True

def validate_not_empty_string(value, fieldname, label):
	if (value == ""):
		label.config(fg="red")
		messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " Can Not Be Empty")
		return False

	if (value.isdigit()):
		label.config(fg="red")
		messagebox.showinfo("Validation Error", "The Value for Field " + fieldname + " Can not Contain Whole Numbers")
		return False

	if (len(value) >15):
		label.config(fg="red")
		messagebox.showinfo("Validation Error", "The Value for Field " + fieldname + " Can only Contain a max of 15 characters")
		return False

	label.config(fg="SpringGreen3")
	return True

def validate_empty(value, fieldname, label):
	if (value == ''):
		label.config(fg="red")
		messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " Can Not Be Empty")
		return False

	label.config(fg="SpringGreen3")
	return True

def validate_age(value, fieldname, label):
	if (int(value) >100):
		label.config(fg="red")
		messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " Can Not Be over 100")
		return False

	if (value ==''):
		label.config(fg="red")
		messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " Can Not Be empty")
		return False

	label.config(fg="SpringGreen3")
	return True


def ageToGroup(value):
	return math.ceil(value.get()/5)


def clearTv():
	record=member_search_Tv.get_children()
	for elements in record:
		member_search_Tv.delete(elements)


def treeviewPopulate():
	clearTv()

	conn = sqlite3.connect('Badmington_club.db')

	c = conn.cursor()

	c.execute("SELECT * From member")
	items = c.fetchall()
	conn.commit()
	conn.close()

	member_search_Tv.tag_configure("even",background="green")
	member_search_Tv.tag_configure("odd",background="red")

	count=0
	for row in items:
		if row == []:
			pass
		else:
			if count%2==0:
				member_search_Tv.insert('','end',text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7]),tags=["even"])
			else:
				member_search_Tv.insert('','end',text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7]),tags=["odd"])
			count+=1



def destroyAddMemberFrame():
	username_label.destroy()
	password_label.destroy()
	firstname_label.destroy()






def returnColour(usernameReturn, passwordReturn, firstnameReturn, surnameReturn, addressReturn, postcodeReturn, ageReturn):
	usernameReturn.config(fg="black")
	passwordReturn.config(fg="black")
	firstnameReturn.config(fg="black")
	surnameReturn.config(fg="black")
	addressReturn.config(fg="black")
	postcodeReturn.config(fg="black")
	ageReturn.config(fg="black")


def updateAccountDetails():
	response = askyesno("Are you sure?", "Do you want to update a students details")
	if response == False:
		showinfo("Info", "Update cancelled")

	else:

		update_member=Toplevel(bg="white")

		title_label =Label(update_member,text = 'Update Member' , fg ='SpringGreen3',bg='white',font=('Verdana',15,'bold'))
		title_label.place(rely=0.13,relx=0.5,anchor=CENTER)

		update_address=Button(update_member,text = 'Update Address', command = update_member_address, fg ='white', bg='black', relief= 'groove', font = ('Verdana',10,'bold'), padx =20, pady =10)
		update_address.place(rely=0.43,relx=0.5,anchor=CENTER)

		update_postcode=Button(update_member,text = 'Update Postcode', command = update_member_postcode, fg ='white', bg='black', relief= 'groove', font = ('Verdana',10,'bold'), padx =20, pady =10)
		update_postcode.place(rely=0.75,relx=0.5,anchor=CENTER)



def update_member_address():
	conn = sqlite3.connect('Badmington_club.db')

	c = conn.cursor()

	memberUsername = simpledialog.askstring("info", "Enter the username of the member you want to see information for")
	if memberUsername != '' and len(memberUsername) <25:
		c.execute(f"SELECT * FROM member WHERE username=?", (memberUsername,))
		data = c.fetchone()
		if not data:
			messagebox.showinfo("Warning", "The username entered was not found in the database", icon='error')

		else:

			new_address = simpledialog.askstring("info", "Enter the new address of the member")

			if new_address != '' and len(new_address) < 30:

				c.execute("""UPDATE member SET address = :new_address""", {'new_address': new_address})
				messagebox.showinfo("info", "The members address is now "+new_address)

			else:

				messagebox.showinfo("Warning", "The address entered does not meet the rules", icon='error')

	else:

		messagebox.showinfo("Warning", "The username entered does not meet the rules", icon='error')

	conn.commit()
	conn.close()

	treeviewPopulate()


def update_member_postcode():
	conn = sqlite3.connect('Badmington_club.db')

	c = conn.cursor()

	memberUsername = simpledialog.askstring("info", "Enter the username of the member you want to see information for")
	if memberUsername != '' and len(memberUsername) <25:
		c.execute(f"SELECT * FROM member WHERE username=?", (memberUsername,))
		data = c.fetchone()
		if not data:
			messagebox.showinfo("Warning", "The username entered was not found in the database", icon='error')

		else:

			new_postcode = simpledialog.askstring("info", "Enter the new postcode of the member")

			if new_postcode != '' and len(new_postcode) < 9:

				c.execute("""UPDATE member SET postcode = :new_postcode""", {'new_postcode': new_postcode})
				messagebox.showinfo("info", "The members postcode is now "+new_postcode)

			else:

				messagebox.showinfo("Warning", "The postcode entered does not meet the rules", icon='error')

	else:

		messagebox.showinfo("Warning", "The username entered does not meet the rules", icon='error')

	conn.commit()
	conn.close()

	treeviewPopulate()


def deleteAccountDetails():
	conn = sqlite3.connect('Badmington_club.db')

	c = conn.cursor()

	response = askyesno("Are you sure?", "Do you want to delete a member")
	if response == False:
		showinfo("Info", "Deletion cancelled")

	else:

		accountUsername = simpledialog.askstring("Info", "Enter the username of the member you want to delete")

		if accountUsername !='' and len(accountUsername) <25:

			c.execute(f"SELECT * FROM member WHERE username =?", (accountUsername,))
			data = c.fetchone()
			if not data:
				messagebox.showinfo("Warning", "The username entered was not found in the database", icon='error')

			else:

				c.execute(f"DELETE FROM member WHERE username =?", (accountUsername,))
				messagebox.showinfo("info", "The member with username "+accountUsername+" has been deleted from the database")

		else:

			messagebox.showinfo("Warning", "The username entered does not meet the rules", icon='error')

	conn.commit()
	conn.close()

	treeviewPopulate()


def searchAccountDetails():
	conn = sqlite3.connect('Badmington_club.db')

	c = conn.cursor()

	response = askyesno("Are you sure?", "Do you want to search a members details")
	if response == False:
		showinfo("Info", "Search cancelled")

	else:

		memberUsername = simpledialog.askstring("info", "Enter the username of the member you want to see information for")
		if memberUsername != '' and len(memberUsername) <25:
			c.execute(f"SELECT * FROM member WHERE username=?", (memberUsername,))
			data = c.fetchone()
			if not data:
				messagebox.showinfo("Warning", "The username entered was not found in the database", icon='error')
			else:

				messagebox.showinfo("info", "The members details are listed below" + "\n\n" + "Username: " + str(data[0]) + "\n" + "Password: " + str(data[1]) + "\n" + "Firstname: " + str(data[2]) + "\n" + "Surname: " + str(data[3]) + "\n" + "Address: " + str(data[4]) + "\n" + "Postcode: " + str(data[5]) + "\n" + "Age: " + str(data[6]) + "\n" + "Group: " + str(data[7]))

		else:

			messagebox.showinfo("Warning", "The username entered does not meet the rules", icon='error')

	conn.commit()
	conn.close()

	treeviewPopulate()


def saveAccountDetails():
	conn = sqlite3.connect('Badmington_club.db')

	c = conn.cursor()

	isValid = True
	isValid = isValid and validate_username(username.get(), "Username", username_label)
	isValid = isValid and validate_password(password.get(), "Password", password_label)
	isValid = isValid and validate_not_empty_string(firstname.get(), "Firstname", firstname_label)
	isValid = isValid and validate_not_empty_string(surname.get(), "Surname", surname_label)
	isValid = isValid and validate_empty(address.get(), "Address", address_label)
	isValid = isValid and validate_empty(postcode.get(), "Postcode", postcode_label)
	isValid = isValid and validate_age(age.get(), "Age", age_label)

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

			doc = buildMemberDocument(account_username, account_password, account_firstname, account_surname, account_address, account_postcode, account_age, account_group)
			found = memberEmail("Lisburn Racquets Account Added", "You have been accepted into Lisburn Raquets Club." + "\n" + "Your details can be found in the document below." + "\n\n" + "Thanks for choosing Lisburn Racquets Club", account_username, doc, username_label)
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

				returnColour(username_label, password_label, firstname_label, surname_label, address_label, postcode_label, age_label)


		conn.commit()
		conn.close()

		treeviewPopulate()


def selection():
	pass













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

password_entry = tkinter.Entry(member, width=15, textvariable=password, show='*', bd=2, relief='ridge')
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


#background_entry_canvas = Canvas(member,width=131, height=78, bg = "white")
#background_entry_canvas.place(rely=0.367,relx=0.5,anchor=CENTER)

#background_entry_image = PhotoImage(file = "rsz_lisburnraquetsclub_60.png")

#background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
#background_entry_canvas.background_entry_image = background_entry_image

delete_button = tkinter.Button(member, text="Delete Member", command=deleteAccountDetails, fg='white', bg='black', bd=4, relief='ridge', font=('Segoe UI Black', 10, 'bold'), padx=50)
delete_button.place(rely=0.41, relx=0.23, anchor='center')

update_button = tkinter.Button(member, text="Update Member", command=updateAccountDetails, fg='white', bg='black', bd=4, relief='ridge', font=('Segoe UI Black', 10, 'bold'), padx=50)
update_button.place(rely=0.33, relx=0.23, anchor='center')

clear_button = tkinter.Button(member, text="Search Details", command=searchAccountDetails, fg='white', bg='black', bd=4, relief='ridge', font=('Segoe UI Black', 10, 'bold'), padx=50)
clear_button.place(rely=0.41, relx=0.77, anchor='center')

create_button = tkinter.Button(member, text="Save Member", command=saveAccountDetails, fg='white', bg='black', bd=4, relief='ridge', font=('Segoe UI Black', 10, 'bold'), padx=50)
create_button.place(rely=0.33, relx=0.77, anchor='center')


member_search_Tv=ttk.Treeview(member,height=14,columns=('Password','Firstname','Surname','Address','Postcode','Age','Group'))
member_search_Tv.place(relx=0.5,rely=0.71,anchor=CENTER)


member_search_Tv.heading("#0",text='Username')
member_search_Tv.column("#0",minwidth=0,width=190)
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
student_ysearch_scrollbar.place(relx=0.96,rely=0.71,anchor='center',height=307)
member_search_Tv.configure(yscrollcommand=student_ysearch_scrollbar.set)




treeviewPopulate()
member.mainloop()

'''
def onTreeviewPopup(event):
	try:
		rowItem = member_search_Tv.treeview.identify_row(event.y)
		tvPopup.selection = member_search_Tv.treeview.set(rowItem)

		member_search_Tv.treeview.selection_set(rowItem)
		member_search_Tv.treeview.focus(rowItem)
		tvPopup.post(event.x_root, event.y_root)
	finally:
		tvPopup.grab_release()


tvPopup = Menu(member, tearoff = 0)
tvPopup.add_command(label = "Update", command = partial(updateAccountDetails, True))
tvPopup.add_separator()
tvPopup.add_command(label = "Delete", command = partial(deleteAccountDetails,True))
'''
