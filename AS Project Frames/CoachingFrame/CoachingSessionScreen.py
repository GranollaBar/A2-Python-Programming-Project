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
import datetime
from tkcalendar import Calendar, DateEntry

from CustomerFrame.member_email import memberEmail
from CustomerFrame.memberWordDocument import buildMemberDocument

from CustomerFrame import CustomerDetailsScreen

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



def dateEntryCheck(dob):
	def assign_dob():
		eventDate.set(cal.selection_get())

	top = Toplevel(member)

	cal = Calendar(top,
				   font="Tahoma 16", selectmode='day',
				   cursor="tcross", year=2021, month=4, day=29)
	cal.pack(fill="both", expand=True)
	ttk.Button(top, text="ok", command=assign_dob).pack()


court1=IntVar()
court2=IntVar()
court3=IntVar()
court4=IntVar()
court5=IntVar()
court6=IntVar()
court7=IntVar()
court8=IntVar()
court9=IntVar()
court10=IntVar()
court11=IntVar()
court12=IntVar()


def courtsRequired():
	courts = Toplevel(member, bg="white")
	courts.geometry('500x500')

	title_label = tkinter.Label(courts, text="Check the No. Courts Needed For The Session", font=('Tahoma', 16, 'underline', 'bold'), fg='black', bg='white')
	title_label.place(rely=0.03, relx=0.5, anchor='center')

	confirm_button = tkinter.Button(courts, text="Confirm Selection", command=lambda : confirmSelection(courts), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 10, 'bold'), padx=35, cursor="tcross")
	confirm_button.place(rely=0.112, relx=0.5, anchor='center')

	confirm_court1 = Checkbutton(courts, cursor="tcross",text="Court 1  V", variable=court1,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'))
	confirm_court1.place(rely=0.2, relx=0.15, anchor='center')

	confirm_court2 = Checkbutton(courts, cursor="tcross",text="Court 2  V", variable=court2,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'))
	confirm_court2.place(rely=0.4, relx=0.15, anchor='center')

	confirm_court3 = Checkbutton(courts, cursor="tcross",text="Court 3  V", variable=court3,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'))
	confirm_court3.place(rely=0.6, relx=0.15, anchor='center')

	confirm_court4 = Checkbutton(courts, cursor="tcross",text="Court 4  V", variable=court4,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'))
	confirm_court4.place(rely=0.8, relx=0.15, anchor='center')

	confirm_court5 = Checkbutton(courts, cursor="tcross",text="Court 5  V", variable=court5,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'))
	confirm_court5.place(rely=0.2, relx=0.5, anchor='center')

	confirm_court6 = Checkbutton(courts, cursor="tcross",text="Court 6  V", variable=court6,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'))
	confirm_court6.place(rely=0.4, relx=0.5, anchor='center')

	confirm_court7 = Checkbutton(courts, cursor="tcross",text="Court 7  V", variable=court7,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'))
	confirm_court7.place(rely=0.6, relx=0.5, anchor='center')

	confirm_court8 = Checkbutton(courts, cursor="tcross",text="Court 8  V", variable=court8,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'))
	confirm_court8.place(rely=0.8, relx=0.5, anchor='center')

	confirm_court9 = Checkbutton(courts, cursor="tcross",text="Court 9  V", variable=court9,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'))
	confirm_court9.place(rely=0.2, relx=0.85, anchor='center')

	confirm_court10 = Checkbutton(courts, cursor="tcross",text="Court 10  V", variable=court10,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'))
	confirm_court10.place(rely=0.4, relx=0.85, anchor='center')

	confirm_court11 = Checkbutton(courts, cursor="tcross",text="Court 11 V", variable=court11,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'))
	confirm_court11.place(rely=0.6, relx=0.85, anchor='center')

	confirm_court12 = Checkbutton(courts, cursor="tcross",text="Court 12 V", variable=court12,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'))
	confirm_court12.place(rely=0.8, relx=0.85, anchor='center')


	background_entry_canvas = Canvas(courts,width=100, height=58, bg = "white")
	background_entry_canvas.place(rely=0.3,relx=0.15,anchor=CENTER)

	background_entry_image = PhotoImage(file ="blueRectangle_100x58.png")

	background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
	background_entry_canvas.background_entry_image = background_entry_image


	background_entry_canvas = Canvas(courts,width=100, height=58, bg = "white")
	background_entry_canvas.place(rely=0.5,relx=0.15,anchor=CENTER)

	background_entry_image = PhotoImage(file ="blueRectangle_100x58.png")

	background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
	background_entry_canvas.background_entry_image = background_entry_image


	background_entry_canvas = Canvas(courts,width=100, height=58, bg = "white")
	background_entry_canvas.place(rely=0.7,relx=0.15,anchor=CENTER)

	background_entry_image = PhotoImage(file ="blueRectangle_100x58.png")

	background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
	background_entry_canvas.background_entry_image = background_entry_image


	background_entry_canvas = Canvas(courts,width=100, height=58, bg = "white")
	background_entry_canvas.place(rely=0.9,relx=0.15,anchor=CENTER)

	background_entry_image = PhotoImage(file ="blueRectangle_100x58.png")

	background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
	background_entry_canvas.background_entry_image = background_entry_image


	background_entry_canvas = Canvas(courts,width=100, height=58, bg = "white")
	background_entry_canvas.place(rely=0.3,relx=0.5,anchor=CENTER)

	background_entry_image = PhotoImage(file ="blueRectangle_100x58.png")

	background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
	background_entry_canvas.background_entry_image = background_entry_image


	background_entry_canvas = Canvas(courts,width=100, height=58, bg = "white")
	background_entry_canvas.place(rely=0.5,relx=0.5,anchor=CENTER)

	background_entry_image = PhotoImage(file ="blueRectangle_100x58.png")

	background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
	background_entry_canvas.background_entry_image = background_entry_image


	background_entry_canvas = Canvas(courts,width=100, height=58, bg = "white")
	background_entry_canvas.place(rely=0.7,relx=0.5,anchor=CENTER)

	background_entry_image = PhotoImage(file ="blueRectangle_100x58.png")

	background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
	background_entry_canvas.background_entry_image = background_entry_image


	background_entry_canvas = Canvas(courts,width=100, height=58, bg = "white")
	background_entry_canvas.place(rely=0.9,relx=0.5,anchor=CENTER)

	background_entry_image = PhotoImage(file ="blueRectangle_100x58.png")

	background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
	background_entry_canvas.background_entry_image = background_entry_image


	background_entry_canvas = Canvas(courts,width=100, height=58, bg = "white")
	background_entry_canvas.place(rely=0.3,relx=0.85,anchor=CENTER)

	background_entry_image = PhotoImage(file ="blueRectangle_100x58.png")

	background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
	background_entry_canvas.background_entry_image = background_entry_image


	background_entry_canvas = Canvas(courts,width=100, height=58, bg = "white")
	background_entry_canvas.place(rely=0.5,relx=0.85,anchor=CENTER)

	background_entry_image = PhotoImage(file ="blueRectangle_100x58.png")

	background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
	background_entry_canvas.background_entry_image = background_entry_image


	background_entry_canvas = Canvas(courts,width=100, height=58, bg = "white")
	background_entry_canvas.place(rely=0.7,relx=0.85,anchor=CENTER)

	background_entry_image = PhotoImage(file ="blueRectangle_100x58.png")

	background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
	background_entry_canvas.background_entry_image = background_entry_image


	background_entry_canvas = Canvas(courts,width=100, height=58, bg = "white")
	background_entry_canvas.place(rely=0.9,relx=0.85,anchor=CENTER)

	background_entry_image = PhotoImage(file ="blueRectangle_100x58.png")

	background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
	background_entry_canvas.background_entry_image = background_entry_image



def confirmSelection(frame):
	frame.withdraw()


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



def showCoachingScreen():
	name_label.place(rely=0.32, relx=0.12, anchor='center')




coaching_session_button = tkinter.Button(header, text="Coaching Session", command=coachingSession, fg='white', bg='black', bd=4, relief='ridge', font=('Segoe UI Black', 12, 'bold'), padx=10)
coaching_session_button.place(rely=0.5, relx=0.3, anchor='center')

add_member_button = tkinter.Button(header, text="Add Member", command=coachingSession, fg='white', bg='black', bd=4, relief='ridge', font=('Segoe UI Black', 12, 'bold'), padx=10)
add_member_button.place(rely=0.5, relx=0.1, anchor='center')









CoachName=StringVar()
timeStart=StringVar()
timeEnd=StringVar()
eventDate=StringVar()
people=StringVar()
level=StringVar()
hourlyRate=StringVar()
notes=StringVar()


name_label = tkinter.Label(member, text="Full Name:", font=('Tahoma', 14, 'bold'), fg='black', bg='white')
name_label.place(rely=0.32, relx=0.12, anchor='center')

starttime_label = tkinter.Label(member, text="Start Time:", font=('Tahoma', 14, 'bold'), fg='black', bg='white')
starttime_label.place(rely=0.4, relx=0.12, anchor='center')

endtime_label = tkinter.Label(member, text="End Time:", font=('Tahoma', 14, 'bold'), fg='black', bg='white')
endtime_label.place(rely=0.48, relx=0.12, anchor='center')

date_label = tkinter.Label(member, text="Session Date:", font=('Tahoma', 14, 'bold'), fg='black', bg='white')
date_label.place(rely=0.56, relx=0.12, anchor='center')

courts_needed_label = tkinter.Label(member, text="Courts Required:", font=('Tahoma', 14, 'bold'), fg='black', bg='white')
courts_needed_label.place(rely=0.64, relx=0.12, anchor='center')

level_label = tkinter.Label(member, text="Group Level:", font=('Tahoma', 14, 'bold'), fg='black', bg='white')
level_label.place(rely=0.72, relx=0.12, anchor='center')

hourlyrate_label = tkinter.Label(member, text="Hourly Rate:", font=('Tahoma', 14, 'bold'), fg='black', bg='white')
hourlyrate_label.place(rely=0.8, relx=0.12, anchor='center')

notes_label = tkinter.Label(member, text="Extra Notes:", font=('Tahoma', 14, 'bold'), fg='black', bg='white')
notes_label.place(rely=0.88, relx=0.12, anchor='center')


name_entry = tkinter.Entry(member, width=30, textvariable=CoachName, bd=3, relief='ridge', cursor="tcross")
name_entry.place(rely=0.323, relx=0.3, anchor='center')

starttime_spinbox_hours = Spinbox(member, width=7,font=("Tahoma",12, 'bold'), bd=3, relief='ridge', cursor="tcross",textvariable=timeStart, values=('8.00', '8.15', '8.30', '8.45', '9.00', '9.15', '9.30', '9.45', '10.00', '10.15', '10.30', '10.45', '11.00', '11.15', '11.30', '11.45', '12.00', '12.15','12.30','12.45','13.00','13.15','13.30','13.45','14.00','14.15','14.30','14.45','15.00','15.15','15.30','15.45','16.00','16.15','16.30','16.45','17.00','17.15','17.30','17.45','18.00','18.15','18.30','18.45','19.00','19.15','19.30','19.45','20.00','20.15','20.30','20.45','21.00','21.15','21.30','21.45','22.00'))
starttime_spinbox_hours.place(rely=0.4025, relx=0.3, anchor='center')

starttime_spinbox_hours = Spinbox(member, width=7,font=("Tahoma",12, 'bold'), bd=3, relief='ridge', cursor="tcross", textvariable=timeEnd, values=('9.00', '9.15', '9.30', '9.45', '10.00', '10.15', '10.30', '10.45', '11.00', '11.15', '11.30', '11.45', '12.00', '12.15','12.30','12.45','13.00','13.15','13.30','13.45','14.00','14.15','14.30','14.45','15.00','15.15','15.30','15.45','16.00','16.15','16.30','16.45','17.00','17.15','17.30','17.45','18.00','18.15','18.30','18.45','19.00','19.15','19.30','19.45','20.00','20.15','20.30','20.45','21.00','21.15','21.30','21.45','22.00','22.15','22.30','22.45','23.00'))
starttime_spinbox_hours.place(rely=0.4825, relx=0.3, anchor='center')

date_entry = Button(member, text='Select Date',font=("Tahoma",11, 'bold'), cursor="tcross",command=lambda : dateEntryCheck(eventDate), padx=10, bd=4, relief="ridge")
date_entry.place(rely=0.565, relx=0.3, anchor='center')

Courts_needed_button = Button(member, text='Select Courts',font=("Tahoma",11, 'bold'), cursor="tcross",command=lambda : courtsRequired(), padx=10, bd=4, relief="ridge")
Courts_needed_button.place(rely=0.645, relx=0.3, anchor='center')

level_entry = tkinter.Entry(member, width=10, textvariable=level, bd=3, relief='ridge', cursor="tcross")
level_entry.place(rely=0.723, relx=0.3, anchor='center')

hourlyrate_entry = tkinter.Entry(member, width=4, textvariable=hourlyRate, bd=3, relief='ridge', cursor="tcross")
hourlyrate_entry.place(rely=0.803, relx=0.3, anchor='center')

notes_entry = tkinter.Entry(member, width=4, textvariable=notes, bd=3, relief='ridge', cursor="tcross")
notes_entry.place(rely=0.883, relx=0.3, anchor='center', width=100, height=50)

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
