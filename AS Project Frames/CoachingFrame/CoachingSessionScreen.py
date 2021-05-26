from tkinter import ttk
from tkinter import messagebox
import tkinter.simpledialog
from tkinter.messagebox import showinfo
from tkinter.messagebox import askyesno
import sqlite3
from tkinter import simpledialog
from tkinter import *
import math
from functools import partial

from CustomerFrame.member_email import memberEmail
from CustomerFrame.memberWordDocument import buildMemberDocument

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

def coachingSession():
	pass



coaching_session_button = tkinter.Button(header, text="Coaching Session", command=coachingSession, fg='white', bg='black', bd=4, relief='ridge', font=('Segoe UI Black', 12, 'bold'), padx=10)
coaching_session_button.place(rely=0.5, relx=0.3, anchor='center')

add_member_button = tkinter.Button(header, text="Add Member", command=coachingSession, fg='white', bg='black', bd=4, relief='ridge', font=('Segoe UI Black', 12, 'bold'), padx=10)
add_member_button.place(rely=0.5, relx=0.1, anchor='center')









CoachName=StringVar()
timeStart=StringVar()
timeEnd=StringVar()
date=StringVar()
people=StringVar()
level=StringVar()
hourlyRate=StringVar()
notes=StringVar()


name_label = tkinter.Label(member, text="Full Name:", font=('Tahoma', 14, 'bold'), fg='black', bg='white')
name_label.place(rely=0.3, relx=0.1, anchor='center')

starttime_label = tkinter.Label(member, text="Start Time:", font=('Tahoma', 14, 'bold'), fg='black', bg='white')
starttime_label.place(rely=0.38, relx=0.1, anchor='center')

endtime_label = tkinter.Label(member, text="End Time:", font=('Tahoma', 14, 'bold'), fg='black', bg='white')
endtime_label.place(rely=0.46, relx=0.1, anchor='center')

date_label = tkinter.Label(member, text="Session Date:", font=('Tahoma', 14, 'bold'), fg='black', bg='white')
date_label.place(rely=0.54, relx=0.1, anchor='center')

nopeople_label = tkinter.Label(member, text="No. Members:", font=('Tahoma', 14, 'bold'), fg='black', bg='white')
nopeople_label.place(rely=0.62, relx=0.1, anchor='center')

level_label = tkinter.Label(member, text="Group Level:", font=('Tahoma', 14, 'bold'), fg='black', bg='white')
level_label.place(rely=0.7, relx=0.1, anchor='center')

hourlyrate_label = tkinter.Label(member, text="Hourly Rate:", font=('Tahoma', 14, 'bold'), fg='black', bg='white')
hourlyrate_label.place(rely=0.78, relx=0.1, anchor='center')

notes_label = tkinter.Label(member, text="Extra Notes:", font=('Tahoma', 14, 'bold'), fg='black', bg='white')
notes_label.place(rely=0.86, relx=0.1, anchor='center')

# dot_label = tkinter.Label(member, text=".", font=('Tahoma', 14, 'bold'), fg='black', bg='white')
# dot_label.place(rely=0.231, relx=0.85, anchor='center')
#
# # canvas = Canvas(member, width=550, height=820)
# # canvas.place(rely=0.5, relx=0.5, anchor='center')
# #
# # png = PhotoImage(file = 'rectangle.png') # Just an example
# # canvas.create_image(0, 0, image = png, anchor = "nw")
# #
# # a = canvas.create_rectangle(50, 0, 50, 0, fill='red')
# # canvas.move(a, 20, 20)


name_entry = tkinter.Entry(member, width=30, textvariable=CoachName, bd=2, relief='ridge')
name_entry.place(rely=0.153, relx=0.25, anchor='center')

starttime_entry = tkinter.Entry(member, width=15, textvariable=timeStart, show='*', bd=2, relief='ridge')
starttime_entry.place(rely=0.233, relx=0.217, anchor='center')

endtime_entry = tkinter.Entry(member, width=15, textvariable=timeEnd, bd=2, relief='ridge')
endtime_entry.place(rely=0.155, relx=0.56, anchor='center')

date_entry = tkinter.Entry(member, width=15, textvariable=date, bd=2, relief='ridge')
date_entry.place(rely=0.235, relx=0.483, anchor='center')

nopeople_entry = tkinter.Entry(member, width=25, textvariable=people, bd=2, relief='ridge')
nopeople_entry.place(rely=0.155, relx=0.85, anchor='center')

level_entry = tkinter.Entry(member, width=10, textvariable=level, bd=2, relief='ridge')
level_entry.place(rely=0.234, relx=0.743, anchor='center')

hourlyrate_entry = tkinter.Entry(member, width=4, textvariable=hourlyRate, bd=2, relief='ridge')
hourlyrate_entry.place(rely=0.233, relx=0.905, anchor='center')

notes_entry = tkinter.Entry(member, width=4, textvariable=notes, bd=2, relief='ridge')
notes_entry.place(rely=0.233, relx=0.905, anchor='center')

#
# delete_button = tkinter.Button(member, text="Delete Member", command=deleteAccountDetails, fg='white', bg='black', bd=4, relief='ridge', font=('Segoe UI Black', 10, 'bold'), padx=50)
# delete_button.place(rely=0.41, relx=0.23, anchor='center')
#
# update_button = tkinter.Button(member, text="Update Member", command=updateAccountDetails, fg='white', bg='black', bd=4, relief='ridge', font=('Segoe UI Black', 10, 'bold'), padx=50)
# update_button.place(rely=0.33, relx=0.23, anchor='center')
#
# clear_button = tkinter.Button(member, text="Search Details", command=searchAccountDetails, fg='white', bg='black', bd=4, relief='ridge', font=('Segoe UI Black', 10, 'bold'), padx=50)
# clear_button.place(rely=0.41, relx=0.77, anchor='center')
#
# create_button = tkinter.Button(member, text="Save Member", command=saveAccountDetails, fg='white', bg='black', bd=4, relief='ridge', font=('Segoe UI Black', 10, 'bold'), padx=50)
# create_button.place(rely=0.33, relx=0.77, anchor='center')



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
