# Coach Details Screen

from tkinter import ttk
from tkinter import messagebox
import tkinter.simpledialog
from tkinter.messagebox import showinfo
from tkinter.messagebox import askyesno
import sqlite3
from tkinter import simpledialog
from tkinter import *
from functools import partial
from tkcalendar import Calendar
from MainScreens.StakeholderEmail import Email
from CoachFrame.coachWordDocument import buildCoachDocument
import datetime
import Pmw



# Coach Details Class
class CoachContent:

	# Initiates main screen window
	# Initiates Lisburn Racquets Club Database
	# Initiates Filepath
	def __init__(self, mainScreen, filepath):
		self.coach = mainScreen
		self.conn = sqlite3.connect(filepath + '\\_databases_images_doc\\Databases\\LisburnRacquetsDatabase.db')
		self.c = self.conn.cursor()
		self.filepath = filepath


	# Generate coach details content
	def generateCoachContnt(self):

		# Select the date of birth of the coach
		def dateEntryCheck(dob):
			def assign_dob():
				dateOfBirth.set(cal.get_date())
				top.withdraw()

			today = datetime.date.today()
			top = Toplevel(self.coach)

			cal = Calendar(top, date_pattern='dd/mm/yyyy', font="serif 16", selectmode='day', cursor="tcross", day=today.day, month=today.month, year=today.year)
			cal.pack(fill="both", expand=True)
			ttk.Button(top, text="Select", command=assign_dob).pack()


		# Ensures username entered is not empty
		# Ensures username entered contains a @ symbol
		# Ensures the username entered contains a .
		# Ensures the username entered is not over 25 characters long
		def validate_username(value, label):
			conn = sqlite3.connect(self.filepath + '\\_databases_images_doc\\Databases\\LisburnRacquetsDatabase.db')
			c = conn.cursor()

			if (value == ''):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The username field cannot be empty", icon='error')
				return False
			if (value == 'e.g. sooney@gmail.com'):
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
		# Ensures password is not under 8 characters long
		# Ensures password is not over 15 characters long
		def validate_password(value, label):
			if (value == ''):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The password field cannot be empty", icon='error')
				return False
			if (value == 'e.g. Ch12ch12'):
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


		# Ensures first name entered is not empty
		# Ensures first name entered is not numerical
		# Ensures first name entered is not over 15 characters long
		def validate_firstname(value, label):
			if (value == ""):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The firstname field cannot be empty", icon='error')
				return False
			if (value == "e.g. Connor"):
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
		# Ensures surname entered is not over 15 characters long
		def validate_surname(value, label):
			if (value == ""):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The surname field cannot be empty", icon='error')
				return False
			if (value == "e.g. Blair"):
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


		# Ensures address entered is not empty
		def validate_address(value, label):
			if (value == ''):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The address field cannot be empty", icon='error')
				return False
			if (value == 'e.g. 47 star street'):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The address field cannot be empty", icon='error')
				return False

			label.config(fg="SpringGreen3")
			return True


		# Ensures at least 1 working day has been selected for the coach
		def validate_all_availability(value, value2, value3, value4, value5, value6, value7):
			if (value ==0 and value2 ==0 and value3 ==0 and value4 ==0 and value5 ==0 and value6 ==0 and value7 ==0):
				messagebox.showinfo("Validation Error", "One availability should be selected", icon='error')
				return False

			return True


		# Ensures monday availability does not have an start time greater than the end time
		def validate_monday_availability(value, value2, label):
			if (mondayAvaliability.get() ==0):
				label.config(fg="SpringGreen3")
				return True
			else:
				if (float(value) >= float(value2)):
					label.config(fg="red")
					messagebox.showinfo("Validation Error", "Monday start time must be before the end time", icon='error')
					return False

				label.config(fg="SpringGreen3")
				return True


		# Ensures tuesday availability does not have an start time greater than the end time
		def validate_tuesday_availability(value, value2, label):
			if (tuesdayAvaliability.get() ==0):
				label.config(fg="SpringGreen3")
				return True
			else:
				if (float(value) >= float(value2)):
					label.config(fg="red")
					messagebox.showinfo("Validation Error", "Tuesday start time must be before the end time", icon='error')
					return False

				label.config(fg="SpringGreen3")
				return True


		# Ensures wednesday availability does not have an start time greater than the end time
		def validate_wednesday_availability(value, value2, label):
			if (wednesdayAvaliability.get() ==0):
				label.config(fg="SpringGreen3")
				return True
			else:
				if (float(value) >= float(value2)):
					label.config(fg="red")
					messagebox.showinfo("Validation Error", "Wednesday start time must be before the end time", icon='error')
					return False

				label.config(fg="SpringGreen3")
				return True


		# Ensures thursday availability does not have an start time greater than the end time
		def validate_thursday_availability(value, value2, label):
			if (thursdayAvaliability.get() ==0):
				label.config(fg="SpringGreen3")
				return True
			else:
				if (float(value) >= float(value2)):
					label.config(fg="red")
					messagebox.showinfo("Validation Error", "Thursday start time must be before the end time", icon='error')
					return False

				label.config(fg="SpringGreen3")
				return True


		# Ensures friday availability does not have an start time greater than the end time
		def validate_friday_availability(value, value2, label):
			if (fridayAvaliability.get() ==0):
				label.config(fg="SpringGreen3")
				return True
			else:
				if (float(value) >= float(value2)):
					label.config(fg="red")
					messagebox.showinfo("Validation Error", "Friday start time must be before the end time", icon='error')
					return False

				label.config(fg="SpringGreen3")
				return True


		# Ensures saturday availability does not have an start time greater than the end time
		def validate_saturday_availability(value, value2, label):
			if (saturdayAvaliability.get() ==0):
				label.config(fg="SpringGreen3")
				return True
			else:
				if (float(value) >= float(value2)):
					label.config(fg="red")
					messagebox.showinfo("Validation Error", "Saturday start time must be before the end time", icon='error')
					return False

				label.config(fg="SpringGreen3")
				return True


		# Ensures sunday availability does not have an start time greater than the end time
		def validate_sunday_availability(value, value2, label):
			if (sundayAvaliability.get() ==0):
				label.config(fg="SpringGreen3")
				return True
			else:
				if (float(value) >= float(value2)):
					label.config(fg="red")
					messagebox.showinfo("Validation Error", "Sunday start time must be before the end time", icon='error')
					return False

				label.config(fg="SpringGreen3")
				return True


		# Ensures gender selected conforms to the rules (Will always conform to the rules)
		def validate_gender(label):
			label.config(fg="SpringGreen3")
			return True


		# Ensures date of birth selected is not empty
		# Ensures date of birth selected is not after the current day
		def validate_DOB(value, label):
			if (value == ''):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The date of birth cannot be empty", icon='error')
				return False

			presentDate = datetime.datetime.now()
			date_formated = presentDate.strftime("%d/%m/%Y")

			d1 = datetime.datetime.strptime(value, "%d/%m/%Y").date()
			d2 = datetime.datetime.strptime(str(date_formated), "%d/%m/%Y").date()

			if d1>d2:
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The date of birth selected cannot be after the current date", icon='error')
				return False

			label.config(fg="SpringGreen3")
			return True


		# Ensures at least one availability is selected
		def validate_new_availability(value, value2, value3, value4, value5, value6, value7):
			if (value ==0 and value2 ==0 and value3 ==0 and value4 ==0 and value5 ==0 and value6 ==0 and value7 ==0):
				messagebox.showinfo("Validation Error", "One availability day should be selected", icon='error')
				return False

			return True


		# Removes the ability to resize all tree views
		def treeviewresizedisable(treeview, event):
			if treeview.identify_region(event.x, event.y) == "separator":
				return "break"


		# Clears coach details tree view data
		def clearTv():
			record=coach_search_Tv.get_children()
			for elements in record:
				coach_search_Tv.delete(elements)


		# Clears coach timetable tree view data
		def clearTimesTv():
			record=coach_times_search_Tv.get_children()
			for elements in record:
				coach_times_search_Tv.delete(elements)


		# Coach details tree view populate based on details in the coach database
		def treeviewPopulate():
			clearTv()

			conn = sqlite3.connect(self.filepath + '\\_databases_images_doc\\Databases\\LisburnRacquetsDatabase.db')
			c = conn.cursor()

			c.execute("SELECT * From coach")
			items = c.fetchall()
			conn.commit()

			count=0
			for row in items:
				if row == []:
					pass
				else:
					if count%2==0:
						coach_search_Tv.insert('','end',text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
					else:
						coach_search_Tv.insert('','end',text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
					count+=1


		# Coach timetable populate based on the details in the coachTimetable database
		def timestreeviewPopulate():
			clearTimesTv()

			conn = sqlite3.connect(self.filepath + '\\_databases_images_doc\\Databases\\LisburnRacquetsDatabase.db')
			c = conn.cursor()

			c.execute("SELECT * From coachTimetable")
			items = c.fetchall()
			conn.commit()

			count=0
			for row in items:
				if row == []:
					pass
				else:
					if count%2==0:
						coach_times_search_Tv.insert('','end',text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
					else:
						coach_times_search_Tv.insert('','end',text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
					count+=1


		# Will add and remove placeholder text in the username name entry box
		def username_click(event):
			if username_entry.get() == 'e.g. sooney@gmail.com':
				username_entry.delete(0, "end")
				username_entry.insert(0, '')
				username_entry.config(fg='black')

		def username_unclick(event):
			if username_entry.get() == '':
				username_entry.insert(0, 'e.g. sooney@gmail.com')
				username_entry.config(fg='grey')


		# Will add and remove placeholder text in the password name entry box
		def password_click(event):
			if password_entry.get() == 'e.g. Ch12ch12':
				password_entry.delete(0, "end")
				password_entry.insert(0, '')
				password_entry.config(fg='black')
				password_entry.config(show="*")

		def password_unclick(event):
			if password_entry.get() == '':
				password_entry.config(show="")
				password_entry.insert(0, 'e.g. Ch12ch12')
				password_entry.config(fg='grey')


		# Will add and remove placeholder text in the first name name entry box
		def firstname_click(event):
			if firstname_entry.get() == 'e.g. Connor':
				firstname_entry.delete(0, "end")
				firstname_entry.insert(0, '')
				firstname_entry.config(fg='black')

		def firstname_unclick(event):
			if firstname_entry.get() == '':
				firstname_entry.insert(0, 'e.g. Connor')
				firstname_entry.config(fg='grey')


		# Will add and remove placeholder text in the surname name entry box
		def surname_click(event):
			if surname_entry.get() == 'e.g. Blair':
				surname_entry.delete(0, "end")
				surname_entry.insert(0, '')
				surname_entry.config(fg='black')

		def surname_unclick(event):
			if surname_entry.get() == '':
				surname_entry.insert(0, 'e.g. Blair')
				surname_entry.config(fg='grey')


		# Will add and remove placeholder text in the address name entry box
		def address_click(event):
			if address_entry.get() == 'e.g. 47 star street':
				address_entry.delete(0, "end")
				address_entry.insert(0, '')
				address_entry.config(fg='black')

		def address_unclick(event):
			if address_entry.get() == '':
				address_entry.insert(0, 'e.g. 47 star street')
				address_entry.config(fg='grey')


		# Returns black colouring to all labels (from green) when updating availability
		def returnColourUpdate(mondayReturn, tuesdayReturn, wednesdayReturn, thursdayReturn, fridayReturn, saturdayReturn, sundayReturn):
			mondayReturn.config(fg="black")
			tuesdayReturn.config(fg="black")
			wednesdayReturn.config(fg="black")
			thursdayReturn.config(fg="black")
			fridayReturn.config(fg="black")
			saturdayReturn.config(fg="black")
			sundayReturn.config(fg="black")

		# Returns black colouring to all labels (from green)
		def returnColour(usernameReturn, passwordReturn, firstnameReturn, surnameReturn, genderReturn, DOBReturn, addressReturn, mondayReturn, tuesdayReturn, wednesdayReturn, thursdayReturn, fridayReturn, saturdayReturn, sundayReturn):
			usernameReturn.config(fg="black")
			passwordReturn.config(fg="black")
			firstnameReturn.config(fg="black")
			surnameReturn.config(fg="black")
			genderReturn.config(fg="black")
			DOBReturn.config(fg="black")
			addressReturn.config(fg="black")
			mondayReturn.config(fg="black")
			tuesdayReturn.config(fg="black")
			wednesdayReturn.config(fg="black")
			thursdayReturn.config(fg="black")
			fridayReturn.config(fg="black")
			saturdayReturn.config(fg="black")
			sundayReturn.config(fg="black")


		# Activates & deactivates functionality of monday work hours based on if the checkbox is active or not active
		def check_monday_checkbox(value):
			if (value.get() == 0):
				monday_from_combobox.config(state="disable")
				monday_to_combobox.config(state="disable")
				monday_from_combobox.current(0)
				monday_to_combobox.current(0)
			else:
				monday_from_combobox.config(state="readonly")
				monday_to_combobox.config(state="readonly")


		# Activates & deactivates functionality of tuesday work hours based on if the checkbox is active or not active
		def check_tuesday_checkbox(value):
			if (value.get() == 0):
				tuesday_from_combobox.config(state="disable")
				tuesday_to_combobox.config(state="disable")
				tuesday_from_combobox.current(0)
				tuesday_to_combobox.current(0)
			else:
				tuesday_from_combobox.config(state="readonly")
				tuesday_to_combobox.config(state="readonly")


		# Activates & deactivates functionality of wednesday work hours based on if the checkbox is active or not active
		def check_wednesday_checkbox(value):
			if (value.get() == 0):
				wednesday_from_combobox.config(state="disable")
				wednesday_to_combobox.config(state="disable")
				wednesday_from_combobox.current(0)
				wednesday_to_combobox.current(0)
			else:
				wednesday_from_combobox.config(state="readonly")
				wednesday_to_combobox.config(state="readonly")


		# Activates & deactivates functionality of thursday work hours based on if the checkbox is active or not active
		def check_thursday_checkbox(value):
			if (value.get() == 0):
				thursday_from_combobox.config(state="disable")
				thursday_to_combobox.config(state="disable")
				thursday_from_combobox.current(0)
				thursday_to_combobox.current(0)
			else:
				thursday_from_combobox.config(state="readonly")
				thursday_to_combobox.config(state="readonly")


		# Activates & deactivates functionality of friday work hours based on if the checkbox is active or not active
		def check_friday_checkbox(value):
			if (value.get() == 0):
				friday_from_combobox.config(state="disable")
				friday_to_combobox.config(state="disable")
				friday_from_combobox.current(0)
				friday_to_combobox.current(0)
			else:
				friday_from_combobox.config(state="readonly")
				friday_to_combobox.config(state="readonly")


		# Activates & deactivates functionality of saturday work hours based on if the checkbox is active or not active
		def check_saturday_checkbox(value):
			if (value.get() == 0):
				saturday_from_combobox.config(state="disable")
				saturday_to_combobox.config(state="disable")
				saturday_from_combobox.current(0)
				saturday_to_combobox.current(0)
			else:
				saturday_from_combobox.config(state="readonly")
				saturday_to_combobox.config(state="readonly")


		# Activates & deactivates functionality of sunday work hours based on if the checkbox is active or not active
		def check_sunday_checkbox(value):
			if (value.get() == 0):
				sunday_from_combobox.config(state="disable")
				sunday_to_combobox.config(state="disable")
				sunday_from_combobox.current(0)
				sunday_to_combobox.current(0)
			else:
				sunday_from_combobox.config(state="readonly")
				sunday_to_combobox.config(state="readonly")


		# Updates coaches details, such as: address and availability
		# Pop-up will allow manager to select which update he wants to perform
		def updateCoachDetails(self, value, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11, value12, value13, value14, value15, value16, value17, value18, value19):
			response = askyesno("Question", "Do you want to update a coach's details?", icon='question')
			if response == False:
				messagebox.showinfo("Info", "Update cancelled", icon='info')

			else:

				updateCoach=Toplevel(bg="white")

				title_label =Label(updateCoach,text = 'Update Coach' , fg ='SpringGreen3',bg='white',font=('serif',15,'bold'))
				title_label.place(rely=0.13,relx=0.5,anchor=CENTER)

				update_address=Button(updateCoach,text = 'Update Address', command = lambda : update_coach_address(updateCoach), fg ='white', bg='black', relief= 'groove', font = ('serif',10,'bold'), padx =20, pady =8)
				update_address.place(rely=0.43,relx=0.5,anchor=CENTER)
				ToolTips.bind(update_address, "Update the coach's address")

				update_availiability=Button(updateCoach,text = 'Update Availability', command = lambda : update_coach_availability(updateCoach, value, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11, value12, value13, value14, value15, value16, value17, value18, value19), fg ='white', bg='black', relief= 'groove', font = ('serif',10,'bold'), padx =20, pady =8)
				update_availiability.place(rely=0.75,relx=0.5,anchor=CENTER)
				ToolTips.bind(update_availiability, "Update the coach's availiability")


		# Updates coaches address based on the username entered by the manager
		# Username must be valid and in the database
		def update_coach_address(frame):
			conn = sqlite3.connect(self.filepath + '\\_databases_images_doc\\Databases\\LisburnRacquetsDatabase.db')
			c = conn.cursor()

			frame.withdraw()

			coachUsername = simpledialog.askstring("Response", "Enter the username of the coach you want to update")
			if coachUsername != '' and len(coachUsername) <25 and '@' in coachUsername and '.' in coachUsername:
				c.execute(f"SELECT * FROM coach WHERE username=?", (coachUsername,))
				data = c.fetchone()
				if not data:
					messagebox.showinfo("Error", "The username entered was not found in the database", icon='error')

				else:

					new_address = simpledialog.askstring("Response", "Enter your new Address")

					if new_address != '' and len(new_address) < 30:

						c.execute("""UPDATE coach SET address=:new_address WHERE username=:username""", {
							"new_address": str(new_address),
							"username": coachUsername
						})

						messagebox.showinfo("Info", "The coach's address is now "+new_address, icon='info')

					else:

						messagebox.showinfo("Error", "The address entered does not meet the rules", icon='error')

			else:

				messagebox.showinfo("Error", "The username entered does not meet the rules", icon='error')

			conn.commit()
			conn.close()

			treeviewPopulate()


		# This will remove all other entry boxes, etc. in order for the manager to update availability of a coach
		def update_coach_availability(frame, value, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11, value12, value13, value14, value15, value16, value17, value18, value19):
			conn = sqlite3.connect(self.filepath + '\\_databases_images_doc\\Databases\\LisburnRacquetsDatabase.db')
			c = conn.cursor()

			frame.withdraw()

			coachUsername = simpledialog.askstring("Response", "Enter the username of the coach you want to update")
			if coachUsername != '' and len(coachUsername) <25 and '@' in coachUsername and '.' in coachUsername:
				c.execute(f"SELECT * FROM coach WHERE username=?", (coachUsername,))
				data = c.fetchone()
				if not data:
					messagebox.showinfo("Error", "The username entered was not found in the database", icon='error')

				else:

					returnColour(username_label, password_label, firstname_label, surname_label, gender_label, DOB_label, address_label, monday_label, tuesday_label, wednesday_label, thursday_label, friday_label, saturday_label, sunday_label)

					value.place_forget()
					value2.place_forget()
					value3.place_forget()
					value4.place_forget()
					value5.place_forget()
					value6.place_forget()
					value7.place_forget()
					value8.place_forget()
					value9.place_forget()
					value10.place_forget()
					value11.place_forget()
					value12.place_forget()
					value13.place_forget()
					value14.place_forget()
					value15.place_forget()
					value16.place_forget()
					value17.place_forget()
					value18.place_forget()
					value19.place_forget()

					username.set('')
					password.set('')
					firstname.set('')
					surname.set('')
					gender.set('1')
					address.set('')
					mondayAvaliability.set('0')
					tuesdayAvaliability.set('0')
					wednesdayAvaliability.set('0')
					thursdayAvaliability.set('0')
					fridayAvaliability.set('0')
					saturdayAvaliability.set('0')
					sundayAvaliability.set('0')
					check_monday_checkbox(mondayAvaliability)
					check_tuesday_checkbox(tuesdayAvaliability)
					check_wednesday_checkbox(wednesdayAvaliability)
					check_thursday_checkbox(thursdayAvaliability)
					check_friday_checkbox(fridayAvaliability)
					check_saturday_checkbox(saturdayAvaliability)
					check_sunday_checkbox(sundayAvaliability)

					update_availability_button = tkinter.Button(self.coach, cursor="tcross",text="Update Availability", command=lambda : availableUpdate(coachUsername, update_availability_button, value, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11, value12, value13, value14, value15, value16, value17, value18, value19), fg='white', bg='black', bd=4, relief='ridge', font=('serif', 10, 'bold'), padx=30)
					update_availability_button.place(rely=0.95, relx=0.77, anchor='center')
					ToolTips.bind(update_availability_button, 'Update availability of a coach')

			conn.close()


		# Updates coaches availability based on the username entered
		# Username and all availabilities must be validated correctly in order for the update to authenticate
		def availableUpdate(username, button, value, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11, value12, value13, value14, value15, value16, value17, value18, value19):
			conn = sqlite3.connect(self.filepath + '\\_databases_images_doc\\Databases\\LisburnRacquetsDatabase.db')
			c = conn.cursor()

			isValid = True
			isValid = isValid and validate_new_availability(mondayAvaliability.get(), tuesdayAvaliability.get(), wednesdayAvaliability.get(), thursdayAvaliability.get(), fridayAvaliability.get(), saturdayAvaliability.get(), sundayAvaliability.get())
			isValid = isValid and validate_monday_availability(monday_from_combobox.get(),monday_to_combobox.get(), monday_label)
			isValid = isValid and validate_tuesday_availability(tuesday_from_combobox.get(),tuesday_to_combobox.get(), tuesday_label)
			isValid = isValid and validate_wednesday_availability(wednesday_from_combobox.get(),wednesday_to_combobox.get(), wednesday_label)
			isValid = isValid and validate_thursday_availability(thursday_from_combobox.get(),thursday_to_combobox.get(), thursday_label)
			isValid = isValid and validate_friday_availability(friday_from_combobox.get(),friday_to_combobox.get(), friday_label)
			isValid = isValid and validate_saturday_availability(saturday_from_combobox.get(),saturday_to_combobox.get(), saturday_label)
			isValid = isValid and validate_sunday_availability(sunday_from_combobox.get(),sunday_to_combobox.get(), sunday_label)

			if isValid:

				AllAvaliability = [mondayAvaliability.get(),tuesdayAvaliability.get(),wednesdayAvaliability.get(),thursdayAvaliability.get(),fridayAvaliability.get(),saturdayAvaliability.get(),sundayAvaliability.get()]
				AllFinalAvaliability = ['monday, ','tuesday, ','wednesday, ','thursday, ','friday, ','saturday, ','sunday, ']

				new_final_avaliability = ''

				for index in range(len(AllAvaliability)):
					item = AllAvaliability[index]
					if item == 1:
						new_final_avaliability = new_final_avaliability + AllFinalAvaliability[index]

				new_final_avaliability = new_final_avaliability[:-2]


				mondayFinalAvaliability = ""
				tuesdayFinalAvaliability = ""
				wednesdayFinalAvaliability = ""
				thursdayFinalAvaliability = ""
				fridayFinalAvaliability = ""
				saturdayFinalAvaliability = ""
				sundayFinalAvaliability = ""

				AllTimes = [mondayAvaliability.get(),tuesdayAvaliability.get(),wednesdayAvaliability.get(),thursdayAvaliability.get(),fridayAvaliability.get(),saturdayAvaliability.get(),sundayAvaliability.get()]
				WeekdaysAvailaiblity = [mondayFinalAvaliability,tuesdayFinalAvaliability,wednesdayFinalAvaliability,thursdayFinalAvaliability,fridayFinalAvaliability,saturdayFinalAvaliability,sundayFinalAvaliability]

				AllFinalTimes = [monday_from_combobox.get(),monday_to_combobox.get(),tuesday_from_combobox.get(),
								 tuesday_to_combobox.get(), wednesday_from_combobox.get(), wednesday_to_combobox.get(),
								 thursday_from_combobox.get(), thursday_to_combobox.get(), friday_from_combobox.get(),
								 friday_to_combobox.get(), saturday_from_combobox.get(), saturday_to_combobox.get(),
								 sunday_from_combobox.get(), sunday_to_combobox.get()]

				finalvaluedates = []

				for rows in AllTimes:
					index = AllTimes.index(rows)
					if rows == 1:
						fromindex = index * 2
						toindex = fromindex + 1
						WeekdaysAvailaiblity[index] = AllFinalTimes[fromindex] + "-" + AllFinalTimes[toindex]
						finalvaluedates.append(WeekdaysAvailaiblity[index])
					else:
						WeekdaysAvailaiblity[index] = 'n/a'
						finalvaluedates.append(WeekdaysAvailaiblity[index])


				c.execute("UPDATE coach SET availability = :new_availability WHERE username=:username", {
					"new_availability": str(new_final_avaliability),
					"username": username
				})

				c.execute("UPDATE coachTimetable SET Monday=:monday, Tuesday=:tuesday, Wednesday=:wednesday, Thursday=:thursday, Friday=:friday, Saturday=:saturday, Sunday=:sunday WHERE username=:username",
						  {
							  "monday": finalvaluedates[0],
							  "tuesday": finalvaluedates[1],
							  "wednesday": finalvaluedates[2],
							  "thursday": finalvaluedates[3],
							  "friday": finalvaluedates[4],
							  "saturday": finalvaluedates[5],
							  "sunday": finalvaluedates[6],
							  "username": username
						  })

				conn.commit()
				conn.close()

				messagebox.showinfo("Info", "The coach's availability is now "+new_final_avaliability, icon='info')

				value.place(rely=0.13, relx=0.09, anchor='center')
				value2.place(rely=0.133, relx=0.25, anchor='center')
				value3.place(rely=0.2, relx=0.09, anchor='center')
				value4.place(rely=0.203, relx=0.25, anchor='center')
				value5.place(rely=0.27, relx=0.09, anchor='center')
				value6.place(rely=0.273, relx=0.25, anchor='center')
				value7.place(rely=0.34, relx=0.09, anchor='center')
				value8.place(rely=0.343, relx=0.25, anchor='center')
				value9.place(rely=0.415, relx=0.09, anchor='center')
				value10.place(rely=0.418, relx=0.2, anchor='center')
				value11.place(rely=0.418, relx=0.3, anchor='center')
				value12.place(rely=0.495, relx=0.09, anchor='center')
				value13.place(rely=0.498, relx=0.25, anchor='center')
				value14.place(rely=0.57, relx=0.09, anchor='center')
				value15.place(rely=0.573, relx=0.25, anchor='center')
				value16.place(rely=0.95, relx=0.49, anchor='center')
				value17.place(rely=0.95, relx=0.77, anchor='center')
				value18.place(rely=0.95, relx=0.63, anchor='center')
				value19.place(rely=0.95, relx=0.91, anchor='center')

				button.place_forget()

			mondayAvaliability.set('0')
			tuesdayAvaliability.set('0')
			wednesdayAvaliability.set('0')
			thursdayAvaliability.set('0')
			fridayAvaliability.set('0')
			saturdayAvaliability.set('0')
			sundayAvaliability.set('0')
			check_monday_checkbox(mondayAvaliability)
			check_tuesday_checkbox(tuesdayAvaliability)
			check_wednesday_checkbox(wednesdayAvaliability)
			check_thursday_checkbox(thursdayAvaliability)
			check_friday_checkbox(fridayAvaliability)
			check_saturday_checkbox(saturdayAvaliability)
			check_sunday_checkbox(sundayAvaliability)

			returnColourUpdate(monday_label, tuesday_label, wednesday_label, thursday_label, friday_label, saturday_label, sunday_label)

			treeviewPopulate()
			timestreeviewPopulate()


		# Delete coaches details from coach and coachTimetable database tables based on the username entered by the manager
		# All associated details of the coach will be deleted as well, including their login
		def deleteCoachDetails(event):
			conn = sqlite3.connect(self.filepath + '\\_databases_images_doc\\Databases\\LisburnRacquetsDatabase.db')
			c = conn.cursor()

			response = askyesno("Question", "Do you want to delete a coach?", icon='question')
			if response == False:
				showinfo("Info", "Deletion cancelled", icon='info')

			else:

				coachUsername = simpledialog.askstring("Response", "Enter the username of the coach you want to delete")

				if coachUsername !='' and len(coachUsername) <25 and '@' in coachUsername and '.' in coachUsername:

					c.execute(f"SELECT * FROM coach WHERE username =?", (coachUsername,))
					data = c.fetchone()
					if not data:
						messagebox.showinfo("Error", "The username entered was not found in the database", icon='error')

					else:

						c.execute(f"DELETE FROM coach WHERE username =?", (coachUsername,))
						c.execute(f"DELETE FROM coachTimetable WHERE username =?", (coachUsername,))
						c.execute(f"DELETE FROM account WHERE username =?", (coachUsername,))
						c.execute(f"DELETE FROM coachSessionDetails WHERE username =?", (coachUsername,))
						messagebox.showinfo("Info", "The coach with username "+coachUsername+" has been deleted from the database", icon='info')

				else:

					messagebox.showinfo("Error", "The username entered does not meet the rules", icon='error')

			conn.commit()
			conn.close()

			treeviewPopulate()
			timestreeviewPopulate()


		# Search coaches details from coach and coachTimetable database tables based on the username entered by the manager
		# A message box will show all the specific details of the coach searched
		def searchCoachDetails():
			conn = sqlite3.connect(self.filepath + '\\_databases_images_doc\\Databases\\LisburnRacquetsDatabase.db')
			c = conn.cursor()

			response = askyesno("Question", "Do you want to search a coach's details?", icon='question')
			if response == False:
				showinfo("Info", "Search cancelled", icon='info')

			else:

				coachUsername = simpledialog.askstring("Response", "Enter the username of the coach you want to see information for")
				if coachUsername != '' and len(coachUsername) <25 and '@' in coachUsername and '.' in coachUsername:
					coachDetails1 = c.execute(f"SELECT * FROM coach WHERE username=?", (coachUsername,))
					data = coachDetails1.fetchone()
					coachDetails2 = c.execute(f"SELECT * FROM coachTimetable WHERE username=?", (coachUsername,))
					data2 = coachDetails2.fetchone()
					if not data:
						messagebox.showinfo("Error", "The username entered was not found in the database", icon='error')
					else:
						messagebox.showinfo("Info", "The coach's details are listed below" + "\n\n" + "Username: " + str(data[0]) + "\n" + "Password: " + str(data[1]) + "\n" + "Firstname: " + str(data[2]) + "\n" + "Surname: " + str(data[3]) + "\n" + "Gender: " + str(data[4]) + "\n" + "DOB: " + str(data[5]) + "\n" + "Address: " + str(data[6]) + "\n" + "Availability: " + str(data[7]), icon='info')
						messagebox.showinfo("Info", "The coach's Timetable is listed below" + "\n\n" + "Username: " + str(data2[0]) + "\n" + "Monday: " + str(data2[1]) + "\n" + "Tuesday: " + str(data2[2]) + "\n" + "Wednesday: " + str(data2[3]) + "\n" + "Thursday: " + str(data2[4]) + "\n" + "Friday: " + str(data2[5]) + "\n" + "Saturday: " + str(data2[6]) + "\n" + "Sunday: " + str(data2[7]), icon='info')

				else:

					messagebox.showinfo("Error", "The username entered does not meet the rules", icon='error')

			conn.close()

			treeviewPopulate()
			timestreeviewPopulate()


		# Submit coaches details to the coach and coachTimetable databases
		# Will generate a document containing all details stored about the coach
		# This will subsequently be sent to the coach's email address
		# The coach will also have a login account created in order to login to the system
		def SubmitCoachDetails():
			conn = sqlite3.connect(self.filepath + '\\_databases_images_doc\\Databases\\LisburnRacquetsDatabase.db')
			c = conn.cursor()

			isValid = True
			isValid = isValid and validate_username(username.get(), username_label)
			isValid = isValid and validate_password(password.get(), password_label)
			isValid = isValid and validate_firstname(firstname.get(), firstname_label)
			isValid = isValid and validate_surname(surname.get(), surname_label)
			isValid = isValid and validate_gender(gender_label)
			isValid = isValid and validate_DOB(dateOfBirth.get(), DOB_label)
			isValid = isValid and validate_address(address.get(), address_label)
			isValid = isValid and validate_all_availability(mondayAvaliability.get(), tuesdayAvaliability.get(), wednesdayAvaliability.get(), thursdayAvaliability.get(), fridayAvaliability.get(), saturdayAvaliability.get(), sundayAvaliability.get())
			isValid = isValid and validate_monday_availability(monday_from_combobox.get(),monday_to_combobox.get(), monday_label)
			isValid = isValid and validate_tuesday_availability(tuesday_from_combobox.get(),tuesday_to_combobox.get(), tuesday_label)
			isValid = isValid and validate_wednesday_availability(wednesday_from_combobox.get(),wednesday_to_combobox.get(), wednesday_label)
			isValid = isValid and validate_thursday_availability(thursday_from_combobox.get(),thursday_to_combobox.get(), thursday_label)
			isValid = isValid and validate_friday_availability(friday_from_combobox.get(),friday_to_combobox.get(), friday_label)
			isValid = isValid and validate_saturday_availability(saturday_from_combobox.get(),saturday_to_combobox.get(), saturday_label)
			isValid = isValid and validate_sunday_availability(sunday_from_combobox.get(),sunday_to_combobox.get(), sunday_label)

			if isValid:
				coach_username = username.get()
				coach_password = password.get()
				coach_firstname = firstname.get()
				coach_surname = surname.get()
				coach_gender = gender.get()
				coach_DOB = dateOfBirth.get()
				coach_address = address.get()

				if (coach_gender == 1):
					final_coach_gender = 'Male'
				else:
					final_coach_gender = 'Female'

				AllAvaliability = [mondayAvaliability.get(),tuesdayAvaliability.get(),wednesdayAvaliability.get(),thursdayAvaliability.get(),fridayAvaliability.get(),saturdayAvaliability.get(),sundayAvaliability.get()]
				AllFinalAvaliability = ['monday, ','tuesday, ','wednesday, ','thursday, ','friday, ','saturday, ','sunday, ']

				new_final_avaliability = ''

				for index in range(len(AllAvaliability)):
					item = AllAvaliability[index]
					if item == 1:
						new_final_avaliability = new_final_avaliability + AllFinalAvaliability[index]

				new_final_avaliability = new_final_avaliability[:-2]


				mondayFinalAvaliability = ""
				tuesdayFinalAvaliability = ""
				wednesdayFinalAvaliability = ""
				thursdayFinalAvaliability = ""
				fridayFinalAvaliability = ""
				saturdayFinalAvaliability = ""
				sundayFinalAvaliability = ""

				AllTimes = [mondayAvaliability.get(),tuesdayAvaliability.get(),wednesdayAvaliability.get(),thursdayAvaliability.get(),fridayAvaliability.get(),saturdayAvaliability.get(),sundayAvaliability.get()]
				WeekdaysAvailaiblity = [mondayFinalAvaliability,tuesdayFinalAvaliability,wednesdayFinalAvaliability,thursdayFinalAvaliability,fridayFinalAvaliability,saturdayFinalAvaliability,sundayFinalAvaliability]

				AllFinalTimes = [monday_from_combobox.get(),monday_to_combobox.get(),tuesday_from_combobox.get(),
								 tuesday_to_combobox.get(), wednesday_from_combobox.get(), wednesday_to_combobox.get(),
								 thursday_from_combobox.get(), thursday_to_combobox.get(), friday_from_combobox.get(),
								 friday_to_combobox.get(), saturday_from_combobox.get(), saturday_to_combobox.get(),
								 sunday_from_combobox.get(), sunday_to_combobox.get()]

				finalvaluedates = []

				for rows in AllTimes:
					index = AllTimes.index(rows)
					if rows == 1:
						fromindex = index * 2
						toindex = fromindex + 1
						WeekdaysAvailaiblity[index] = AllFinalTimes[fromindex] + "-" + AllFinalTimes[toindex]
						finalvaluedates.append(WeekdaysAvailaiblity[index])
					else:
						WeekdaysAvailaiblity[index] = 'n/a'
						finalvaluedates.append(WeekdaysAvailaiblity[index])


				response = askyesno("Question", "Are you sure that all information above is correct?", icon='question')
				if response == False:
					showinfo("Info", "submition cancelled", icon='info')

				else:

					doc = buildCoachDocument(coach_username, coach_password, coach_firstname, coach_surname, final_coach_gender, coach_DOB, coach_address, mondayFinalAvaliability, tuesdayFinalAvaliability, wednesdayFinalAvaliability, thursdayFinalAvaliability, fridayFinalAvaliability, saturdayFinalAvaliability, sundayFinalAvaliability)
					found = Email("Lisburn Racquets Coach Added", "Good work on securing a coach position at Lisburn Racquets Club" + "\n" + "Your details can be found in the document below." + "\n\n" + "Thanks for choosing Lisburn Racquets Club", coach_username, doc, username_label, 'Coach_Account_Details.docx')
					if found:

						c.execute("INSERT INTO coach VALUES (:username, :password, :firstname, :surname, :gender, :DOB, :address, :availabilty)",
								  {
									  'username': coach_username,
									  'password': coach_password,
									  'firstname': coach_firstname,
									  'surname': coach_surname,
									  'gender': final_coach_gender,
									  'DOB': coach_DOB,
									  'address': coach_address,
									  'availabilty': new_final_avaliability,
								  })

						c.execute("INSERT INTO coachTimetable VALUES (:username, :monday, :tuesday, :wednesday, :thursday, :friday, :saturday, :sunday)",
								  {
									  'username': coach_username,
									  'monday': finalvaluedates[0],
									  'tuesday': finalvaluedates[1],
									  'wednesday': finalvaluedates[2],
									  'thursday': finalvaluedates[3],
									  'friday': finalvaluedates[4],
									  'saturday': finalvaluedates[5],
									  'sunday': finalvaluedates[6],
								  })

						c.execute("INSERT INTO account VALUES (:username, :password, :status)",
								   {
									   'username': coach_username,
									   'password': coach_password,
									   'status': 'coach',
								   })

						username.set('')
						password.set('')
						firstname.set('')
						surname.set('')
						gender.set('1')
						address.set('')
						mondayAvaliability.set('0')
						tuesdayAvaliability.set('0')
						wednesdayAvaliability.set('0')
						thursdayAvaliability.set('0')
						fridayAvaliability.set('0')
						saturdayAvaliability.set('0')
						sundayAvaliability.set('0')
						check_monday_checkbox(mondayAvaliability)
						check_tuesday_checkbox(tuesdayAvaliability)
						check_wednesday_checkbox(wednesdayAvaliability)
						check_thursday_checkbox(thursdayAvaliability)
						check_friday_checkbox(fridayAvaliability)
						check_saturday_checkbox(saturdayAvaliability)
						check_sunday_checkbox(sundayAvaliability)

						returnColour(username_label, password_label, firstname_label, surname_label, gender_label, DOB_label, address_label, monday_label, tuesday_label, wednesday_label, thursday_label, friday_label, saturday_label, sunday_label)


				conn.commit()
				conn.close()

				treeviewPopulate()
				timestreeviewPopulate()



		# Variables Used
		username = StringVar()
		password = StringVar()
		firstname=StringVar()
		surname=StringVar()
		gender=IntVar()
		dateOfBirth=StringVar()
		address=StringVar()
		mondayAvaliability=IntVar()
		tuesdayAvaliability=IntVar()
		wednesdayAvaliability=IntVar()
		thursdayAvaliability=IntVar()
		fridayAvaliability=IntVar()
		saturdayAvaliability=IntVar()
		sundayAvaliability=IntVar()

		# Times array
		monday_from_Avaliability_times = ["9.00","10.00","11.00","12.00","13.00","14.00","15.00","16.00","17.00","18.00","19.00","20.00","21.00"]
		tuesday_from_Avaliability_times = ["9.00","10.00","11.00","12.00","13.00","14.00","15.00","16.00","17.00","18.00","19.00","20.00","21.00"]
		wednesday_from_Avaliability_times = ["9.00","10.00","11.00","12.00","13.00","14.00","15.00","16.00","17.00","18.00","19.00","20.00","21.00"]
		thursday_from_Avaliability_times = ["9.00","10.00","11.00","12.00","13.00","14.00","15.00","16.00","17.00","18.00","19.00","20.00","21.00"]
		friday_from_Avaliability_times = ["9.00","10.00","11.00","12.00","13.00","14.00","15.00","16.00","17.00","18.00","19.00","20.00","21.00"]
		saturday_from_Avaliability_times = ["9.00","10.00","11.00","12.00","13.00","14.00","15.00","16.00","17.00","18.00","19.00"]
		sunday_from_Avaliability_times = ["9.00","10.00","11.00","12.00","13.00","14.00","15.00","16.00","17.00"]

		monday_to_Avaliability_times = ["9.00","10.00","11.00","12.00","13.00","14.00","15.00","16.00","17.00","18.00","19.00","20.00","21.00","22.00"]
		tuesday_to_Avaliability_times = ["9.00","10.00","11.00","12.00","13.00","14.00","15.00","16.00","17.00","18.00","19.00","20.00","21.00","22.00"]
		wednesday_to_Avaliability_times = ["9.00","10.00","11.00","12.00","13.00","14.00","15.00","16.00","17.00","18.00","19.00","20.00","21.00","22.00"]
		thursday_to_Avaliability_times = ["9.00","10.00","11.00","12.00","13.00","14.00","15.00","16.00","17.00","18.00","19.00","20.00","21.00","22.00"]
		friday_to_Avaliability_times = ["9.00","10.00","11.00","12.00","13.00","14.00","15.00","16.00","17.00","18.00","19.00","20.00","21.00","22.00"]
		saturday_to_Avaliability_times = ["9.00","10.00","11.00","12.00","13.00","14.00","15.00","16.00","17.00","18.00","19.00","20.00"]
		sunday_to_Avaliability_times = ["9.00","10.00","11.00","12.00","13.00","14.00","15.00","16.00","17.00","18.00"]


		ToolTips = Pmw.Balloon()


		# Tkinter labels, entry boxes, buttons, tree views, etc.
		username_label = tkinter.Label(self.coach, text="Username:", font=('serif', 14, 'bold'), fg='black', bg='white')
		username_label.place(rely=0.13, relx=0.09, anchor='center')

		password_label = tkinter.Label(self.coach, text="Password:", font=('serif', 14, 'bold'), fg='black', bg='white')
		password_label.place(rely=0.2, relx=0.09, anchor='center')

		firstname_label = tkinter.Label(self.coach, text="Firstname:", font=('serif', 14, 'bold'), fg='black', bg='white')
		firstname_label.place(rely=0.27, relx=0.09, anchor='center')

		surname_label = tkinter.Label(self.coach, text="Surname:", font=('serif', 14, 'bold'), fg='black', bg='white')
		surname_label.place(rely=0.34, relx=0.09, anchor='center')

		gender_label = tkinter.Label(self.coach, text="Gender:", font=('serif', 14, 'bold'), fg='black', bg='white')
		gender_label.place(rely=0.415, relx=0.09, anchor='center')

		DOB_label = tkinter.Label(self.coach, text="DOB:", font=('serif', 14, 'bold'), fg='black', bg='white')
		DOB_label.place(rely=0.495, relx=0.09, anchor='center')

		address_label = tkinter.Label(self.coach, text="Address:", font=('serif', 14, 'bold'), fg='black', bg='white')
		address_label.place(rely=0.57, relx=0.09, anchor='center')


		username_entry = tkinter.Entry(self.coach, width=25, textvariable=username, bd=3, relief='ridge', cursor="tcross")
		username_entry.place(rely=0.133, relx=0.25, anchor='center')
		username_entry.insert(0, 'e.g. sooney@gmail.com')
		username_entry.bind('<FocusIn>', username_click)
		username_entry.bind('<FocusOut>', username_unclick)
		username_entry.config(fg='grey')

		password_entry = tkinter.Entry(self.coach, width=15, textvariable=password, bd=3, relief='ridge', cursor="tcross")
		password_entry.place(rely=0.203, relx=0.25, anchor='center')
		password_entry.insert(0, 'e.g. Ch12ch12')
		password_entry.bind('<FocusIn>', password_click)
		password_entry.bind('<FocusOut>', password_unclick)
		password_entry.config(fg='grey')

		firstname_entry = tkinter.Entry(self.coach, width=15, textvariable=firstname, bd=3, relief='ridge', cursor="tcross")
		firstname_entry.place(rely=0.273, relx=0.25, anchor='center')
		firstname_entry.insert(0, 'e.g. Connor')
		firstname_entry.bind('<FocusIn>', firstname_click)
		firstname_entry.bind('<FocusOut>', firstname_unclick)
		firstname_entry.config(fg='grey')

		surname_entry = tkinter.Entry(self.coach, width=15, textvariable=surname, bd=3, relief='ridge', cursor="tcross")
		surname_entry.place(rely=0.343, relx=0.25, anchor='center')
		surname_entry.insert(0, 'e.g. Blair')
		surname_entry.bind('<FocusIn>', surname_click)
		surname_entry.bind('<FocusOut>', surname_unclick)
		surname_entry.config(fg='grey')

		male_radiobutton = Radiobutton(self.coach, text="Male", variable=gender, value=1, font=("serif",9, 'bold'), cursor="tcross", bg="white", bd=2, relief="ridge")
		male_radiobutton.place(rely=0.418, relx=0.2, anchor='center')

		female_radiobutton = Radiobutton(self.coach, text="Female", variable=gender, value=2, font=("serif",9, 'bold'), cursor="tcross", bg="white", bd=2, relief="ridge")
		female_radiobutton.place(rely=0.418, relx=0.3, anchor='center')
		gender.set("1")

		DOB_button = Button(self.coach, text='Select DOB',font=("serif",10, 'bold'), cursor="tcross",command=lambda : dateEntryCheck(dateOfBirth), padx=10, bd=4, relief="ridge")
		DOB_button.place(rely=0.498, relx=0.25, anchor='center')
		ToolTips.bind(DOB_button, "Select the coaches Date Of Birth")

		address_entry = tkinter.Entry(self.coach, width=25, textvariable=address, bd=3, relief='ridge', cursor="tcross")
		address_entry.place(rely=0.573, relx=0.25, anchor='center')
		address_entry.insert(0, 'e.g. 47 star street')
		address_entry.bind('<FocusIn>', address_click)
		address_entry.bind('<FocusOut>', address_unclick)
		address_entry.config(fg='grey')


		line = Canvas(self.coach, width=360, height=1)
		line.config(bg='black')
		line.create_line(3, 0, 200, 100000)
		line.place(rely=0.61462, relx=0.18, anchor='center')


		monday_label = tkinter.Label(self.coach, text="Monday:", font=('serif', 10, 'bold'), fg='black', bg='white')
		monday_label.place(rely=0.66, relx=0.05, anchor='center')

		monday_checkbox = Checkbutton(self.coach, cursor="tcross", command=lambda : check_monday_checkbox(mondayAvaliability), variable=mondayAvaliability,bg="white",bd=2, relief="groove", font=('serif', 6,'bold'),onvalue=1, offvalue=0)
		monday_checkbox.place(rely=0.662, relx=0.11, anchor='center')

		monday_from_label = tkinter.Label(self.coach, text="From:", font=('serif', 10, 'bold'), fg='black', bg='white')
		monday_from_label.place(rely=0.66, relx=0.18, anchor='center')

		monday_from_combobox = ttk.Combobox(self.coach, value=monday_from_Avaliability_times,font=('serif', 8, 'bold'), width=5)
		monday_from_combobox.place(rely=0.661, relx=0.24, anchor='center')
		monday_from_combobox.current(0)
		monday_from_combobox.config(state="disable")

		monday_to_label = tkinter.Label(self.coach, text="To:", font=('serif', 10, 'bold'), fg='black', bg='white')
		monday_to_label.place(rely=0.66, relx=0.32, anchor='center')

		monday_to_combobox = ttk.Combobox(self.coach, value=monday_to_Avaliability_times, font=('serif', 8, 'bold'), width=5)
		monday_to_combobox.place(rely=0.661, relx=0.37, anchor='center')
		monday_to_combobox.current(0)
		monday_to_combobox.config(state="disable")


		tuesday_label = tkinter.Label(self.coach, text="Tuesday:", font=('serif', 10, 'bold'), fg='black', bg='white')
		tuesday_label.place(rely=0.73, relx=0.05, anchor='center')

		tuesday_checkbox = Checkbutton(self.coach, cursor="tcross", command=lambda : check_tuesday_checkbox(tuesdayAvaliability), variable=tuesdayAvaliability,bg="white",bd=2, relief="groove", font=('serif', 6,'bold'),onvalue=1, offvalue=0)
		tuesday_checkbox.place(rely=0.732, relx=0.11, anchor='center')

		tuesday_from_label = tkinter.Label(self.coach, text="From:", font=('serif', 10, 'bold'), fg='black', bg='white')
		tuesday_from_label.place(rely=0.73, relx=0.18, anchor='center')

		tuesday_from_combobox = ttk.Combobox(self.coach, value=tuesday_from_Avaliability_times, font=('serif', 8, 'bold'), width=5)
		tuesday_from_combobox.place(rely=0.731, relx=0.24, anchor='center')
		tuesday_from_combobox.current(0)
		tuesday_from_combobox.config(state="disable")

		tuesday_to_label = tkinter.Label(self.coach, text="To:", font=('serif', 10, 'bold'), fg='black', bg='white')
		tuesday_to_label.place(rely=0.73, relx=0.32, anchor='center')

		tuesday_to_combobox = ttk.Combobox(self.coach, value=tuesday_to_Avaliability_times, font=('serif', 8, 'bold'), width=5)
		tuesday_to_combobox.place(rely=0.731, relx=0.37, anchor='center')
		tuesday_to_combobox.current(0)
		tuesday_to_combobox.config(state="disable")


		wednesday_label = tkinter.Label(self.coach, text="Wednesday:", font=('serif', 10, 'bold'), fg='black', bg='white')
		wednesday_label.place(rely=0.8, relx=0.05, anchor='center')

		wednesday_checkbox = Checkbutton(self.coach, cursor="tcross", command=lambda : check_wednesday_checkbox(wednesdayAvaliability), variable=wednesdayAvaliability,bg="white",bd=2, relief="groove", font=('serif', 6,'bold'),onvalue=1, offvalue=0)
		wednesday_checkbox.place(rely=0.802, relx=0.11, anchor='center')

		wednesday_from_label = tkinter.Label(self.coach, text="From:", font=('serif', 10, 'bold'), fg='black', bg='white')
		wednesday_from_label.place(rely=0.8, relx=0.18, anchor='center')

		wednesday_from_combobox = ttk.Combobox(self.coach, value=wednesday_from_Avaliability_times, font=('serif', 8, 'bold'), width=5)
		wednesday_from_combobox.place(rely=0.801, relx=0.24, anchor='center')
		wednesday_from_combobox.current(0)
		wednesday_from_combobox.config(state="disable")

		wednesday_to_label = tkinter.Label(self.coach, text="To:", font=('serif', 10, 'bold'), fg='black', bg='white')
		wednesday_to_label.place(rely=0.8, relx=0.32, anchor='center')

		wednesday_to_combobox = ttk.Combobox(self.coach, value=wednesday_to_Avaliability_times, font=('serif', 8, 'bold'), width=5)
		wednesday_to_combobox.place(rely=0.801, relx=0.37, anchor='center')
		wednesday_to_combobox.current(0)
		wednesday_to_combobox.config(state="disable")


		thursday_label = tkinter.Label(self.coach, text="Thursday:", font=('serif', 10, 'bold'), fg='black', bg='white')
		thursday_label.place(rely=0.87, relx=0.05, anchor='center')

		thursday_checkbox = Checkbutton(self.coach, cursor="tcross", command=lambda : check_thursday_checkbox(thursdayAvaliability), variable=thursdayAvaliability,bg="white",bd=2, relief="groove", font=('serif', 6,'bold'),onvalue=1, offvalue=0)
		thursday_checkbox.place(rely=0.872, relx=0.11, anchor='center')

		thursday_from_label = tkinter.Label(self.coach, text="From:", font=('serif', 10, 'bold'), fg='black', bg='white')
		thursday_from_label.place(rely=0.87, relx=0.18, anchor='center')

		thursday_from_combobox = ttk.Combobox(self.coach, value=thursday_from_Avaliability_times, font=('serif', 8, 'bold'), width=5)
		thursday_from_combobox.place(rely=0.871, relx=0.24, anchor='center')
		thursday_from_combobox.current(0)
		thursday_from_combobox.config(state="disable")

		thursday_to_label = tkinter.Label(self.coach, text="To:", font=('serif', 10, 'bold'), fg='black', bg='white')
		thursday_to_label.place(rely=0.87, relx=0.32, anchor='center')

		thursday_to_combobox = ttk.Combobox(self.coach, value=thursday_to_Avaliability_times, font=('serif', 8, 'bold'), width=5)
		thursday_to_combobox.place(rely=0.871, relx=0.37, anchor='center')
		thursday_to_combobox.current(0)
		thursday_to_combobox.config(state="disable")


		friday_label = tkinter.Label(self.coach, text="Friday:", font=('serif', 10, 'bold'), fg='black', bg='white')
		friday_label.place(rely=0.94, relx=0.05, anchor='center')

		friday_checkbox = Checkbutton(self.coach, cursor="tcross", command=lambda : check_friday_checkbox(fridayAvaliability), variable=fridayAvaliability,bg="white",bd=2, relief="groove", font=('serif', 6,'bold'),onvalue=1, offvalue=0)
		friday_checkbox.place(rely=0.942, relx=0.11, anchor='center')

		friday_from_label = tkinter.Label(self.coach, text="From:", font=('serif', 10, 'bold'), fg='black', bg='white')
		friday_from_label.place(rely=0.94, relx=0.18, anchor='center')

		friday_from_combobox = ttk.Combobox(self.coach, value=friday_from_Avaliability_times, font=('serif', 8, 'bold'), width=5)
		friday_from_combobox.place(rely=0.941, relx=0.24, anchor='center')
		friday_from_combobox.current(0)
		friday_from_combobox.config(state="disable")

		friday_to_label = tkinter.Label(self.coach, text="To:", font=('serif', 10, 'bold'), fg='black', bg='white')
		friday_to_label.place(rely=0.94, relx=0.32, anchor='center')

		friday_to_combobox = ttk.Combobox(self.coach, value=friday_to_Avaliability_times, font=('serif', 8, 'bold'), width=5)
		friday_to_combobox.place(rely=0.941, relx=0.37, anchor='center')
		friday_to_combobox.current(0)
		friday_to_combobox.config(state="disable")


		saturday_label = tkinter.Label(self.coach, text="Saturday:", font=('serif', 10, 'bold'), fg='black', bg='white')
		saturday_label.place(rely=0.825, relx=0.52, anchor='center')

		saturday_checkbox = Checkbutton(self.coach, cursor="tcross", command=lambda : check_saturday_checkbox(saturdayAvaliability), variable=saturdayAvaliability,bg="white",bd=2, relief="groove", font=('serif', 6,'bold'),onvalue=1, offvalue=0)
		saturday_checkbox.place(rely=0.827, relx=0.58, anchor='center')

		saturday_from_label = tkinter.Label(self.coach, text="From:", font=('serif', 10, 'bold'), fg='black', bg='white')
		saturday_from_label.place(rely=0.825, relx=0.65, anchor='center')

		saturday_from_combobox = ttk.Combobox(self.coach, value=saturday_from_Avaliability_times,font=('serif', 8, 'bold'), width=5)
		saturday_from_combobox.place(rely=0.826, relx=0.71, anchor='center')
		saturday_from_combobox.current(0)
		saturday_from_combobox.config(state="disable")


		saturday_to_label = tkinter.Label(self.coach, text="To:", font=('serif', 10, 'bold'), fg='black', bg='white')
		saturday_to_label.place(rely=0.825, relx=0.79, anchor='center')

		saturday_to_combobox = ttk.Combobox(self.coach, value=saturday_to_Avaliability_times, font=('serif', 8, 'bold'), width=5)
		saturday_to_combobox.place(rely=0.826, relx=0.84, anchor='center')
		saturday_to_combobox.current(0)
		saturday_to_combobox.config(state="disable")


		sunday_label = tkinter.Label(self.coach, text="Sunday:", font=('serif', 10, 'bold'), fg='black', bg='white')
		sunday_label.place(rely=0.885, relx=0.52, anchor='center')

		sunday_checkbox = Checkbutton(self.coach, cursor="tcross", command=lambda : check_sunday_checkbox(sundayAvaliability), variable=sundayAvaliability,bg="white",bd=2, relief="groove", font=('serif', 6,'bold'),onvalue=1, offvalue=0)
		sunday_checkbox.place(rely=0.887, relx=0.58, anchor='center')

		sunday_from_label = tkinter.Label(self.coach, text="From:", font=('serif', 10, 'bold'), fg='black', bg='white')
		sunday_from_label.place(rely=0.885, relx=0.65, anchor='center')

		sunday_from_combobox = ttk.Combobox(self.coach, value=sunday_from_Avaliability_times, font=('serif', 8, 'bold'), width=5)
		sunday_from_combobox.place(rely=0.886, relx=0.71, anchor='center')
		sunday_from_combobox.current(0)
		sunday_from_combobox.config(state="disable")

		sunday_to_label = tkinter.Label(self.coach, text="To:", font=('serif', 10, 'bold'), fg='black', bg='white')
		sunday_to_label.place(rely=0.885, relx=0.79, anchor='center')

		sunday_to_combobox = ttk.Combobox(self.coach, value=sunday_to_Avaliability_times, font=('serif', 8, 'bold'), width=5)
		sunday_to_combobox.place(rely=0.886, relx=0.84, anchor='center')
		sunday_to_combobox.current(0)
		sunday_to_combobox.config(state="disable")


		submit_button = tkinter.Button(self.coach, cursor="tcross",text="Submit", command=SubmitCoachDetails, fg='white', bg='black', bd=4, relief='ridge', font=('serif', 10, 'bold'), padx=30)
		submit_button.place(rely=0.95, relx=0.49, anchor='center')
		ToolTips.bind(submit_button, 'Submit coach details entered into database')

		search_button = tkinter.Button(self.coach, cursor="tcross",text="Search", command=searchCoachDetails, fg='white', bg='black', bd=4, relief='ridge', font=('serif', 10, 'bold'), padx=32.4)
		search_button.place(rely=0.95, relx=0.63, anchor='center')
		ToolTips.bind(search_button, 'Search a coach from database')

		update_button = tkinter.Button(self.coach, cursor="tcross",text="Update", command=lambda : updateCoachDetails(self, username_label, username_entry, password_label, password_entry, firstname_label, firstname_entry, surname_label, surname_entry, gender_label, male_radiobutton, female_radiobutton, DOB_label, DOB_button, address_label, address_entry, submit_button, update_button, search_button, delete_button), fg='white', bg='black', bd=4, relief='ridge', font=('serif', 10, 'bold'), padx=30)
		update_button.place(rely=0.95, relx=0.77, anchor='center')
		ToolTips.bind(update_button, 'Update details of a coach in the database')

		delete_button = tkinter.Button(self.coach, cursor="tcross",text="Delete", command=lambda : deleteCoachDetails(self), fg='white', bg='black', bd=4, relief='ridge', font=('serif', 10, 'bold'), padx=33.2)
		delete_button.place(rely=0.95, relx=0.91, anchor='center')
		ToolTips.bind(delete_button, 'Delete a coach from the database')


		coach_search_Tv=ttk.Treeview(self.coach,height=15,columns=('Password','Firstname','Surname','Gender','DOB','Address','Availability'))
		coach_search_Tv.place(relx=0.665,rely=0.365,anchor=CENTER)

		coach_search_Tv.heading("#0",text='Username')
		coach_search_Tv.column("#0",minwidth=0,width=100)
		coach_search_Tv.heading("#1",text='Password')
		coach_search_Tv.column("#1",minwidth=0,width=70)
		coach_search_Tv.heading("#2",text='Firstname')
		coach_search_Tv.column("#2",minwidth=0,width=80)
		coach_search_Tv.heading("#3",text='Surname')
		coach_search_Tv.column("#3",minwidth=0,width=80)
		coach_search_Tv.heading("#4",text='Gender')
		coach_search_Tv.column("#4",minwidth=0,width=70)
		coach_search_Tv.heading("#5",text='DOB')
		coach_search_Tv.column("#5",minwidth=0,width=80)
		coach_search_Tv.heading("#6",text='Address')
		coach_search_Tv.column("#6",minwidth=0,width=70)
		coach_search_Tv.heading("#7",text='Days')
		coach_search_Tv.column("#7",minwidth=0,width=70)
		coach_search_Tv.bind('<Button-1>', partial(treeviewresizedisable, coach_search_Tv))

		coach_ysearch_scrollbar = Scrollbar(self.coach, orient = 'vertical', command = coach_search_Tv.yview, cursor="tcross")
		coach_ysearch_scrollbar.place(relx=0.985,rely=0.365,anchor='center',height=327)
		coach_search_Tv.configure(yscrollcommand=coach_ysearch_scrollbar.set)


		coach_times_search_Tv=ttk.Treeview(self.coach,height=4,columns=('Mon','Tues','Wed','Thur','Fri','Sat','Sun'))
		coach_times_search_Tv.place(relx=0.695,rely=0.713,anchor=CENTER)

		coach_times_search_Tv.heading("#0",text='Username')
		coach_times_search_Tv.column("#0",minwidth=0,width=100)
		coach_times_search_Tv.heading("#1",text='Mon')
		coach_times_search_Tv.column("#1",minwidth=0,width=67)
		coach_times_search_Tv.heading("#2",text='Tues')
		coach_times_search_Tv.column("#2",minwidth=0,width=67)
		coach_times_search_Tv.heading("#3",text='Wed')
		coach_times_search_Tv.column("#3",minwidth=0,width=67)
		coach_times_search_Tv.heading("#4",text='Thur')
		coach_times_search_Tv.column("#4",minwidth=0,width=67)
		coach_times_search_Tv.heading("#5",text='Fri')
		coach_times_search_Tv.column("#5",minwidth=0,width=67)
		coach_times_search_Tv.heading("#6",text='Sat')
		coach_times_search_Tv.column("#6",minwidth=0,width=67)
		coach_times_search_Tv.heading("#7",text='Sun')
		coach_times_search_Tv.column("#7",minwidth=0,width=67)
		coach_times_search_Tv.bind('<Button-1>', partial(treeviewresizedisable, coach_times_search_Tv))

		coach_times_ysearch_scrollbar = Scrollbar(self.coach, orient = 'vertical', command = coach_times_search_Tv.yview, cursor="tcross")
		coach_times_ysearch_scrollbar.place(relx=0.99,rely=0.713,anchor='center',height=106)
		coach_times_search_Tv.configure(yscrollcommand=coach_times_ysearch_scrollbar.set)


		treeviewPopulate()
		timestreeviewPopulate()


		# A pop-up will be produced if a user right-clicks the coach details or coach timetable tree view
		# This allows them to update/delete that coaches details
		def onTreeviewPopup(tvPopup, event=None):
			try:
				rowItem = coach_search_Tv.identify_row(event.y)
				tvPopup.selection = coach_search_Tv.set(rowItem)

				coach_search_Tv.selection_set(rowItem)
				coach_search_Tv.focus(rowItem)
				tvPopup.post(event.x_root, event.y_root)
			finally:
				tvPopup.grab_release()

		tvPopup = Menu(self.coach, tearoff = 0)
		tvPopup.add_command(label = "Update", command = partial(updateCoachDetails, True))
		tvPopup.add_separator()
		tvPopup.add_command(label = "Delete", command = partial(deleteCoachDetails,True))

		coach_search_Tv.bind("<Button-3>", partial(onTreeviewPopup, tvPopup))
