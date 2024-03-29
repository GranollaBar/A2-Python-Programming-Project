# Member Details Screen

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
from MainScreens.StakeholderEmail import Email
from MemberFrame.memberWordDocument import buildMemberDocument
import Pmw



# Member Details Class
class MemberContent:

	# Initiates main screen window
	# Initiates Lisburn Racquets Club Database
	# Initiates Filepath
	def __init__(self, mainScreen, filepath):
		self.member = mainScreen
		self.conn = sqlite3.connect(filepath + '\\_databases_images_doc\\Databases\\LisburnRacquetsDatabase.db')
		self.c = self.conn.cursor()
		self.filepath = filepath


	# Generate member details content
	def generateMemberContnt(self):

		# Ensures username entered is not empty
		# Ensures username entered contains an @ symbol
		# Ensures username entered contains a .
		# Ensures username entered is less than 25 characters
		# Ensures username entered does not exists in the system already
		def validate_username(value, label):
			conn = sqlite3.connect(self.filepath + '\\_databases_images_doc\\Databases\\LisburnRacquetsDatabase.db')
			c = conn.cursor()

			if (value == ''):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The username field cannot be empty", icon='error')
				return False
			if (value == 'e.g. bobby564@gmail.com'):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The username field cannot be empty", icon='error')
				return False
			if ('@' not in value):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The username field must contain @", icon='error')
				return False
			if ('.' not in value):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The username field must contain a .", icon='error')
				return False
			if (len(value) > 25):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The username field cannot have more than 25 characters", icon='error')
				return False

			c.execute(f"SELECT * FROM member WHERE username=?", (value,))
			data = c.fetchone()
			c.execute(f"SELECT * FROM coach WHERE username=?", (value,))
			data2 = c.fetchone()
			c.execute(f"SELECT * FROM manager WHERE username=?", (value,))
			data3 = c.fetchone()
			if data or data2 or data3:
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The username entered already exists in the database", icon='error')
				return False


			label.config(fg="SpringGreen3")
			return True


		# Ensures password entered is not empty
		# Ensures password entered does not have less than 8 characters
		# Ensures password entered does not contain more than 15 characters
		def validate_password(value, label):
			if (value == ''):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The password field cannot be empty", icon='error')
				return False
			if (value == 'e.g. RossBob24'):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The password field cannot be empty", icon='error')
				return False
			if (len(value) < 8):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The password field cannot contain less than 8 characters", icon='error')
				return False
			if (len(value) > 15):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The password field must contain less than 16 characters", icon='error')
				return False

			label.config(fg="SpringGreen3")
			return True


		# Ensures telephone entered is not empty
		# Ensures telephone entered is not less than 11 characters
		# Ensures telephone entered is not more than 11 characters
		def validate_telephone(value, label):
			if (value == ''):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The telephone field cannot be empty", icon='error')
				return False
			if (value == 'e.g. 03358629462'):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The telephone field cannot be empty", icon='error')
				return False
			if (len(value) < 11):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The telephone field cannot contain less than 11 numbers", icon='error')
				return False
			if (len(value) > 11):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The telephone field cannot contain more than 11 numbers", icon='error')
				return False

			label.config(fg="SpringGreen3")
			return True


		# Ensures first name entered is not empty
		# Ensures first name entered is not numerical
		# Ensures first name entered is not more than 15 characters
		def validate_firstname(value, label):
			if (value == ""):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The firstname field cannot be empty", icon='error')
				return False
			if (value == 'e.g. Johhny'):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The firstname field cannot be empty", icon='error')
				return False
			if (any(char.isdigit() for char in value) == True):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The firstname field can only contain letters", icon='error')
				return False
			if (len(value) >15):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The firstname field can only contain 15 characters", icon='error')
				return False

			label.config(fg="SpringGreen3")
			return True


		# Ensures surname entered is not empty
		# Ensures surname entered is not numerical
		# Ensures surname entered is not more than 15 characters
		def validate_surname(value, label):
			if (value == ""):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The surname field cannot be empty", icon='error')
				return False
			if (value == 'e.g. Synders'):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The surname field cannot be empty", icon='error')
				return False
			if (any(char.isdigit() for char in value) == True):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The surname field can only contain letters", icon='error')
				return False
			if (len(value) >15):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The surname field can only contain 15 characters", icon='error')
				return False

			label.config(fg="SpringGreen3")
			return True


		# Ensures postcode entered is not empty
		# Ensures postcode entered is not more than 9 characters
		def validate_postcode(value, label):
			if (value == ''):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The postcode field cannot be empty", icon='error')
				return False
			if (value == 'e.g. BT12 4RF'):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The postcode field cannot be empty", icon='error')
				return False
			if (len(value) > 9):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The postcode field cannot have more than 9 characters", icon='error')
				return False

			label.config(fg="SpringGreen3")
			return True


		# Ensures age entered is not empty
		# Ensures age entered is not over 100
		def validate_age(value, label):
			if (str(value) ==''):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The age field cannot be empty", icon='error')
				return False
			if (value == 'e.g. 27'):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The age field cannot be empty", icon='error')
				return False
			if (int(value) >100):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The age field cannot be over 100", icon='error')
				return False

			label.config(fg="SpringGreen3")
			return True


		# Calculates the correct group for the member by using DIV
		def ageToGroup(value):
			return math.ceil(int(value.get())//5)


		# Will add and remove placeholder text in the username name entry box
		def username_click(event):
			if username_entry.get() == 'e.g. bobby564@gmail.com':
				username_entry.delete(0, "end")
				username_entry.insert(0, '')
				username_entry.config(fg='black')

		def username_unclick(event):
			if username_entry.get() == '':
				username_entry.insert(0, 'e.g. bobby564@gmail.com')
				username_entry.config(fg='grey')


		# Will add and remove placeholder text in the password name entry box
		def password_click(event):
			if password_entry.get() == 'e.g. RossBob24':
				password_entry.delete(0, "end")
				password_entry.insert(0, '')
				password_entry.config(fg='black')
				password_entry.config(show="*")

		def password_unclick(event):
			if password_entry.get() == '':
				password_entry.config(show="")
				password_entry.insert(0, 'e.g. RossBob24')
				password_entry.config(fg='grey')


		# Will add and remove placeholder text in the first name name entry box
		def firstname_click(event):
			if firstname_entry.get() == 'e.g. Johhny':
				firstname_entry.delete(0, "end")
				firstname_entry.insert(0, '')
				firstname_entry.config(fg='black')

		def firstname_unclick(event):
			if firstname_entry.get() == '':
				firstname_entry.insert(0, 'e.g. Johhny')
				firstname_entry.config(fg='grey')


		# Will add and remove placeholder text in the surname name entry box
		def surname_click(event):
			if surname_entry.get() == 'e.g. Synders':
				surname_entry.delete(0, "end")
				surname_entry.insert(0, '')
				surname_entry.config(fg='black')

		def surname_unclick(event):
			if surname_entry.get() == '':
				surname_entry.insert(0, 'e.g. Synders')
				surname_entry.config(fg='grey')


		# Will add and remove placeholder text in the telephone name entry box
		def telephone_click(event):
			if telephone_entry.get() == 'e.g. 03358629462':
				telephone_entry.delete(0, "end")
				telephone_entry.insert(0, '')
				telephone_entry.config(fg='black')

		def telephone_unclick(event):
			if telephone_entry.get() == '':
				telephone_entry.insert(0, 'e.g. 03358629462')
				telephone_entry.config(fg='grey')


		# Will add and remove placeholder text in the postcode name entry box
		def postcode_click(event):
			if postcode_entry.get() == 'e.g. BT12 4RF':
				postcode_entry.delete(0, "end")
				postcode_entry.insert(0, '')
				postcode_entry.config(fg='black')

		def postcode_unclick(event):
			if postcode_entry.get() == '':
				postcode_entry.insert(0, 'e.g. BT12 4RF')
				postcode_entry.config(fg='grey')


		# Ensures age entered conforms to the rules
		def age_click(event):
			if age_entry.get() == 'e.g. 27':
				age_entry.delete(0, "end")
				age_entry.insert(0, '')
				age_entry.config(fg='black')


		def age_unclick(event):
			if age_entry.get() == '':
				age_entry.insert(0, 'e.g. 27')
				age_entry.config(fg='grey')


		# Clears member details tree view data
		def clearTv():
			record=member_search_Tv.get_children()
			for elements in record:
				member_search_Tv.delete(elements)


		# Member details tree view populate based on the data in the member dtaabase table
		def treeviewPopulate():
			clearTv()

			conn = sqlite3.connect(self.filepath + '\\_databases_images_doc\\Databases\\LisburnRacquetsDatabase.db')
			c = conn.cursor()

			c.execute("SELECT * From member")
			items = c.fetchall()

			conn.commit()
			conn.close()

			count=0
			for row in items:
				if row == []:
					pass
				else:
					if count%2==0:
						member_search_Tv.insert('','end',text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
					else:
						member_search_Tv.insert('','end',text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
					count+=1


		# Removes the ability to resize all tree views
		def treeviewresizedisable(treeview, event):
			if treeview.identify_region(event.x, event.y) == "separator":
				return "break"


		# Returns black colouring to all labels
		def returnColour(usernameReturn, passwordReturn, firstnameReturn, surnameReturn, telephoneReturn, postcodeReturn, ageReturn):
			usernameReturn.config(fg="black")
			passwordReturn.config(fg="black")
			firstnameReturn.config(fg="black")
			surnameReturn.config(fg="black")
			telephoneReturn.config(fg="black")
			postcodeReturn.config(fg="black")
			ageReturn.config(fg="black")


		# Updates member details, such as: telephone and postcode based on the username entered
		def updateAccountDetails(event):
			response = askyesno("Question", "Do you want to update a students details?", icon='question')
			if response == False:
				showinfo("Info", "Update cancelled", icon='info')

			else:

				update_member=Toplevel(bg="white")

				title_label =Label(update_member,text = 'Update Member' , fg ='SpringGreen3',bg='white',font=('serif',15,'bold'))
				title_label.place(rely=0.13,relx=0.5,anchor=CENTER)

				update_telephone=Button(update_member,text = 'Update Telephone', command = lambda : update_member_telephone(update_member), fg ='white', bg='black', relief= 'groove', font = ('serif',10,'bold'), padx =20, pady =10)
				update_telephone.place(rely=0.43,relx=0.5,anchor=CENTER)
				ToolTips.bind(update_telephone, "Update the member's telephone")

				update_postcode=Button(update_member,text = 'Update Postcode', command = lambda : update_member_postcode(update_member), fg ='white', bg='black', relief= 'groove', font = ('serif',10,'bold'), padx =20, pady =10)
				update_postcode.place(rely=0.75,relx=0.5,anchor=CENTER)
				ToolTips.bind(update_postcode, "Update the member's postcode")


		# Updates member's telephone based on the username entered by the coach
		def update_member_telephone(frame):
			frame.withdraw()

			conn = sqlite3.connect(self.filepath + '\\_databases_images_doc\\Databases\\LisburnRacquetsDatabase.db')
			c = conn.cursor()

			memberUsername = simpledialog.askstring("Response", "Enter the username of the member you want to update")
			if memberUsername != '' and len(memberUsername) <25 and '@' in memberUsername and '.' in memberUsername:
				c.execute(f"SELECT * FROM member WHERE username=?", (memberUsername,))
				data = c.fetchone()
				if not data:
					messagebox.showinfo("Error", "The username entered was not found in the database", icon='error')

				else:

					new_telephone = simpledialog.askstring("Response", "Enter the new telephone number of the member")

					if new_telephone != '' and len(new_telephone) == 11:

						c.execute("""UPDATE member SET telephone = :new_telephone WHERE username=:username""", {
							"new_telephone": str(new_telephone),
							"username": memberUsername
						})

						messagebox.showinfo("Info", "The members telephone number is now "+new_telephone, icon='info')

					else:

						messagebox.showinfo("Error", "The telephone number entered does not meet the rules", icon='error')

			else:

				messagebox.showinfo("Error", "The username entered does not meet the rules", icon='error')

			conn.commit()
			conn.close()

			treeviewPopulate()


		# Updates member's postcode based on the username entered by the coach
		def update_member_postcode(frame):
			frame.withdraw()

			conn = sqlite3.connect(self.filepath + '\\_databases_images_doc\\Databases\\LisburnRacquetsDatabase.db')
			c = conn.cursor()

			memberUsername = simpledialog.askstring("Response", "Enter the username of the member you want to update")
			if memberUsername != '' and len(memberUsername) <25 and '@' in memberUsername and '.' in memberUsername:
				c.execute(f"SELECT * FROM member WHERE username=?", (memberUsername,))
				data = c.fetchone()
				if not data:
					messagebox.showinfo("Error", "The username entered was not found in the database", icon='error')

				else:

					new_postcode = simpledialog.askstring("Response", "Enter the new postcode of the member")

					if new_postcode != '' and len(new_postcode) < 9:

						c.execute("""UPDATE member SET postcode = :new_postcode WHERE username=:username""", {
							"new_postcode": str(new_postcode),
							"username": memberUsername
						})

						messagebox.showinfo("Info", "The members postcode is now "+new_postcode, icon='info')

					else:

						messagebox.showinfo("Error", "The postcode entered does not meet the rules", icon='error')

			else:

				messagebox.showinfo("Error", "The username entered does not meet the rules", icon='error')

			conn.commit()
			conn.close()

			treeviewPopulate()


		# Delete member details from member database table based on the username entered
		# This will simultaneously delete all information stored about that user, includng their login account
		def deleteAccountDetails(event):
			conn = sqlite3.connect(self.filepath + '\\_databases_images_doc\\Databases\\LisburnRacquetsDatabase.db')
			c = conn.cursor()

			response = askyesno("Question", "Do you want to delete a member?", icon='question')
			if response == False:
				showinfo("Info", "Deletion cancelled", icon='info')

			else:

				accountUsername = simpledialog.askstring("Response", "Enter the username of the member you want to delete")

				if accountUsername !='' and len(accountUsername) <25:

					c.execute(f"SELECT * FROM member WHERE username =?", (accountUsername,))
					data = c.fetchone()
					if not data:
						messagebox.showinfo("Error", "The username entered was not found in the database", icon='error')

					else:

						c.execute(f"DELETE FROM member WHERE username =?", (accountUsername,))
						c.execute(f"DELETE FROM account WHERE username =?", (accountUsername,))
						c.execute(f"DELETE FROM fees WHERE username =?", (accountUsername,))
						c.execute(f"DELETE FROM MemberBooking WHERE username =?", (accountUsername,))
						c.execute(f"DELETE FROM SinglesCompetition WHERE username=:username OR username2=:username", {
							"username": accountUsername
						})
						c.execute(f"DELETE FROM DoublesCompetition WHERE username=:username OR username2=:username OR username3=:username OR username4=:username", {
							"username": accountUsername
						})
						messagebox.showinfo("info", "The member with username "+accountUsername+" has been deleted from the system")

				else:

					messagebox.showinfo("Error", "The username entered does not meet the rules", icon='error')

			conn.commit()
			conn.close()

			treeviewPopulate()


		# Search member details from member database table based on the username entered by the coach
		def searchAccountDetails():
			conn = sqlite3.connect(self.filepath + '\\_databases_images_doc\\Databases\\LisburnRacquetsDatabase.db')
			c = conn.cursor()

			response = askyesno("Question", "Do you want to search a members details?", icon='question')
			if response == False:
				showinfo("Info", "Search cancelled", icon='info')

			else:

				memberUsername = simpledialog.askstring("Response", "Enter the username of the member you want to see information for")
				if memberUsername != '' and len(memberUsername) <25:
					c.execute(f"SELECT * FROM member WHERE username=?", (memberUsername,))
					data = c.fetchone()
					if not data:
						messagebox.showinfo("Error", "The username entered was not found in the database", icon='error')
					else:

						messagebox.showinfo("Info", "The members details are listed below" + "\n\n" + "Username: " + str(data[0]) + "\n" + "Password: " + str(data[1]) + "\n" + "Firstname: " + str(data[2]) + "\n" + "Surname: " + str(data[3]) + "\n" + "Telephone: " + str(data[4]) + "\n" + "Postcode: " + str(data[5]) + "\n" + "Age: " + str(data[6]) + "\n" + "Group: " + str(data[7]), icon='info')

				else:

					messagebox.showinfo("Error", "The username entered does not meet the rules", icon='error')

			conn.commit()
			conn.close()

			treeviewPopulate()


		# Submit member details
		# Will generate a document containing all details stored about the member
		# This will subsequently be sent to the member's email
		# Will create a login account for the member entered
		def SubmitAccountDetails():
			conn = sqlite3.connect(self.filepath + '\\_databases_images_doc\\Databases\\LisburnRacquetsDatabase.db')
			c = conn.cursor()

			isValid = True
			isValid = isValid and validate_username(username.get(), username_label)
			isValid = isValid and validate_password(password.get(), password_label)
			isValid = isValid and validate_firstname(firstname.get(), firstname_label)
			isValid = isValid and validate_surname(surname.get(), surname_label)
			isValid = isValid and validate_telephone(number.get(), telephone_label)
			isValid = isValid and validate_postcode(postcode.get(), postcode_label)
			isValid = isValid and validate_age(age.get(), age_label)

			if isValid:
				account_username = username.get()
				account_password = password.get()
				account_firstname = firstname.get()
				account_surname = surname.get()
				account_telephone = number.get()
				account_postcode = postcode.get()
				account_age = age.get()

				account_group = ageToGroup(age)

				CompetitionConfirmation = messagebox.askquestion('Question','Are you comfortable with doing competitions', icon='question')
				if CompetitionConfirmation == 'yes':
					finalCompetition = 'yes'
				else:
					finalCompetition = 'no'

				if isValid:
					response = askyesno("Question", "Are you sure that all information above is correct?", icon='question')
					if response == False:
						showinfo("Info", "submition cancelled", icon='info')

					else:

						doc = buildMemberDocument(account_username, account_password, account_firstname, account_surname, account_telephone, account_postcode, account_age, account_group, self.filepath)
						found = Email("Lisburn Racquets Account Added", "You have been accepted into Lisburn Raquets Club." + "\n" + "Your details can be found in the document below." + "\n\n" + "Thanks for choosing Lisburn Racquets Club", account_username, doc, username_label, 'Member_Account_Details.docx')
						if found:

							c.execute("INSERT INTO member VALUES (:username, :password, :firstname, :surname, :telephone, :postcode, :age, :member_group, :competitions)",
									  {
										  'username': account_username,
										  'password': account_password,
										  'firstname': account_firstname,
										  'surname': account_surname,
										  'telephone': account_telephone,
										  'postcode': account_postcode,
										  'age': account_age,
										  'member_group': account_group,
										  'competitions': finalCompetition,
									  })

							c.execute("INSERT INTO account VALUES (:username, :password, :status)",
									  {
										  'username': account_username,
										  'password': account_password,
										  'status': 'member',
									  })

							messagebox.showinfo("Info","The member has been assigned to group " + str(account_group) + " because he/she is " + str(account_age) + " years old", icon='info')

							username.set('')
							password.set('')
							firstname.set('')
							surname.set('')
							number.set('')
							postcode.set('')
							age.set('')

							returnColour(username_label, password_label, firstname_label, surname_label, telephone_label, postcode_label, age_label)

				conn.commit()
				conn.close()

				treeviewPopulate()



		# Variables Used
		username = StringVar()
		password = StringVar()
		firstname=StringVar()
		surname=StringVar()
		number=StringVar()
		postcode=StringVar()
		age=StringVar()


		ToolTips = Pmw.Balloon()


		# Tkinter labels, entry boxes, buttons, tree views, etc.
		username_label = tkinter.Label(self.member, text="Username:", font=('serif', 14, 'bold'), fg='black', bg='white')
		username_label.place(rely=0.15, relx=0.09, anchor='center')

		password_label = tkinter.Label(self.member, text="Password:", font=('serif', 14, 'bold'), fg='black', bg='white')
		password_label.place(rely=0.23, relx=0.09, anchor='center')

		firstname_label = tkinter.Label(self.member, text="Firstname:", font=('serif', 14, 'bold'), fg='black', bg='white')
		firstname_label.place(rely=0.152, relx=0.43, anchor='center')

		surname_label = tkinter.Label(self.member, text="Surname:", font=('serif', 14, 'bold'), fg='black', bg='white')
		surname_label.place(rely=0.231, relx=0.36, anchor='center')

		telephone_label = tkinter.Label(self.member, text="Telephone:", font=('serif', 14, 'bold'), fg='black', bg='white')
		telephone_label.place(rely=0.152, relx=0.7, anchor='center')

		postcode_label = tkinter.Label(self.member, text="Postcode:", font=('serif', 14, 'bold'), fg='black', bg='white')
		postcode_label.place(rely=0.231, relx=0.64, anchor='center')

		age_label = tkinter.Label(self.member, text="Age:", font=('serif', 14, 'bold'), fg='black', bg='white')
		age_label.place(rely=0.231, relx=0.85, anchor='center')


		username_entry = tkinter.Entry(self.member, width=25, textvariable=username, bd=3, relief='ridge', cursor="tcross")
		username_entry.place(rely=0.153, relx=0.25, anchor='center')
		username_entry.insert(0, 'e.g. bobby564@gmail.com')
		username_entry.bind('<FocusIn>', username_click)
		username_entry.bind('<FocusOut>', username_unclick)
		username_entry.config(fg='grey')

		password_entry = tkinter.Entry(self.member, width=15, textvariable=password, bd=3, relief='ridge', cursor="tcross")
		password_entry.place(rely=0.233, relx=0.217, anchor='center')
		password_entry.insert(0, 'e.g. RossBob24')
		password_entry.bind('<FocusIn>', password_click)
		password_entry.bind('<FocusOut>', password_unclick)
		password_entry.config(fg='grey')

		firstname_entry = tkinter.Entry(self.member, width=15, textvariable=firstname, bd=3, relief='ridge', cursor="tcross")
		firstname_entry.place(rely=0.15, relx=0.56, anchor='center')
		firstname_entry.insert(0, 'e.g. Johhny')
		firstname_entry.bind('<FocusIn>', firstname_click)
		firstname_entry.bind('<FocusOut>', firstname_unclick)
		firstname_entry.config(fg='grey')

		surname_entry = tkinter.Entry(self.member, width=15, textvariable=surname, bd=3, relief='ridge', cursor="tcross")
		surname_entry.place(rely=0.23, relx=0.483, anchor='center')
		surname_entry.insert(0, 'e.g. Synders')
		surname_entry.bind('<FocusIn>', surname_click)
		surname_entry.bind('<FocusOut>', surname_unclick)
		surname_entry.config(fg='grey')

		telephone_entry = tkinter.Entry(self.member, width=25, textvariable=number, bd=3, relief='ridge', cursor="tcross")
		telephone_entry.place(rely=0.15, relx=0.85, anchor='center')
		telephone_entry.insert(0, 'e.g. 03358629462')
		telephone_entry.bind('<FocusIn>', telephone_click)
		telephone_entry.bind('<FocusOut>', telephone_unclick)
		telephone_entry.config(fg='grey')

		postcode_entry = tkinter.Entry(self.member, width=12, textvariable=postcode, bd=3, relief='ridge', cursor="tcross")
		postcode_entry.place(rely=0.23, relx=0.743, anchor='center')
		postcode_entry.insert(0, 'e.g. BT12 4RF')
		postcode_entry.bind('<FocusIn>', postcode_click)
		postcode_entry.bind('<FocusOut>', postcode_unclick)
		postcode_entry.config(fg='grey')

		age_entry = tkinter.Entry(self.member, width=7, textvariable=age, bd=3, relief='ridge', cursor="tcross")
		age_entry.place(rely=0.23, relx=0.905, anchor='center')
		age.set('')
		age_entry.insert(0, 'e.g. 27')
		age_entry.bind('<FocusIn>', age_click)
		age_entry.bind('<FocusOut>', age_unclick)
		age_entry.config(fg='grey')



		delete_button = tkinter.Button(self.member, cursor="tcross",text="Delete Member", command=lambda : deleteAccountDetails(self), fg='white', bg='black', bd=4, relief='ridge', font=('serif', 10, 'bold'), padx=50)
		delete_button.place(rely=0.41, relx=0.37, anchor='center')
		ToolTips.bind(delete_button, 'Delete a member from database')

		update_button = tkinter.Button(self.member, cursor="tcross",text="Update Member", command=lambda : updateAccountDetails(self), fg='white', bg='black', bd=4, relief='ridge', font=('serif', 10, 'bold'), padx=50)
		update_button.place(rely=0.33, relx=0.37, anchor='center')
		ToolTips.bind(update_button, 'Update a member in database')

		search_button = tkinter.Button(self.member, cursor="tcross",text="Search Details", command=searchAccountDetails, fg='white', bg='black', bd=4, relief='ridge', font=('serif', 10, 'bold'), padx=50)
		search_button.place(rely=0.41, relx=0.63, anchor='center')
		ToolTips.bind(search_button, 'Search for a user in the database')

		create_button = tkinter.Button(self.member, cursor="tcross",text="Save Member", command=SubmitAccountDetails, fg='white', bg='black', bd=4, relief='ridge', font=('serif', 10, 'bold'), padx=50)
		create_button.place(rely=0.33, relx=0.63, anchor='center')
		ToolTips.bind(create_button, 'Create new member with data inputted')


		member_search_Tv=ttk.Treeview(self.member,height=14,columns=('Password','Firstname','Surname','Telephone','Postcode','Age','Group'))
		member_search_Tv.place(relx=0.5,rely=0.71,anchor=CENTER)

		member_search_Tv.heading("#0",text='Username')
		member_search_Tv.column("#0",minwidth=0,width=190)
		member_search_Tv.heading("#1",text='Password')
		member_search_Tv.column("#1",minwidth=0,width=90)
		member_search_Tv.heading("#2",text='Firstname')
		member_search_Tv.column("#2",minwidth=0,width=100)
		member_search_Tv.heading("#3",text='Surname')
		member_search_Tv.column("#3",minwidth=0,width=100)
		member_search_Tv.heading("#4",text='Telephone')
		member_search_Tv.column("#4",minwidth=0,width=140)
		member_search_Tv.heading("#5",text='Postcode')
		member_search_Tv.column("#5",minwidth=0,width=90)
		member_search_Tv.heading("#6",text='Age')
		member_search_Tv.column("#6",minwidth=0,width=50)
		member_search_Tv.heading("#7",text='Group')
		member_search_Tv.column("#7",minwidth=0,width=80)
		member_search_Tv.bind('<Button-1>', partial(treeviewresizedisable, member_search_Tv))

		student_ysearch_scrollbar = Scrollbar(self.member, orient = 'vertical', command = member_search_Tv.yview, cursor="tcross")
		student_ysearch_scrollbar.place(relx=0.93,rely=0.71,anchor='center',height=307)
		member_search_Tv.configure(yscrollcommand=student_ysearch_scrollbar.set)


		treeviewPopulate()



		# A pop-up will be produced if a user right-clicks the member details tree view
		# This allows them to update/delete that member's details
		def onTreeviewPopup(tvPopup, event=None):
			try:
				rowItem = member_search_Tv.identify_row(event.y)
				tvPopup.selection = member_search_Tv.set(rowItem)

				member_search_Tv.selection_set(rowItem)
				member_search_Tv.focus(rowItem)
				tvPopup.post(event.x_root, event.y_root)
			finally:
				tvPopup.grab_release()

		tvPopup = Menu(self.member, tearoff = 0)
		tvPopup.add_command(label = "Update", command = partial(updateAccountDetails, True))
		tvPopup.add_separator()
		tvPopup.add_command(label = "Delete", command = partial(deleteAccountDetails,True))

		member_search_Tv.bind("<Button-3>", partial(onTreeviewPopup, tvPopup))