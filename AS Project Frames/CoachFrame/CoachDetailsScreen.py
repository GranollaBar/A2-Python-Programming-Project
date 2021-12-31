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


class CoachContent:

	def __init__(self, mainScreen):
		self.coach = mainScreen
		self.conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
		self.c = self.conn.cursor()


		# self.c.execute("""CREATE TABLE coach (
		# 			username text,
		# 			password text,
		# 			firstname text,
		# 			surname text,
		# 			gender text,
		# 			DOB text,
		# 			address text,
		# 			availability text
		# 			)""")
		#
		# self.c.execute("""CREATE TABLE coachTimetable (
		# 			username text,
		# 			Monday text,
		# 			Tuesday text,
		# 			Wednesday text,
		# 			Thursday text,
		# 			Friday text,
		# 			Saturday text,
		# 			Sunday text
		# 			)""")


	def generateCoachContnt(self):

		def dateEntryCheck(dob):
			def assign_dob():
				dateOfBirth.set(cal.get_date())
				top.withdraw()

			today = datetime.date.today()
			top = Toplevel(self.coach)

			cal = Calendar(top, date_pattern='dd/mm/yyyy', font="Tahoma 16", selectmode='day', cursor="tcross", day=today.day, month=today.month, year=today.year)
			cal.pack(fill="both", expand=True)
			ttk.Button(top, text="Select", command=assign_dob).pack()


		def validate_username(value, label):
			if (value == ''):
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

			label.config(fg="SpringGreen3")
			return True


		def validate_password(value, label):
			if (value == ''):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The password field cannot be empty", icon='error')
				return False
			if (len(value) < 8):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The password field must contain more than 7 characters", icon='error')
				return False
			if (len(value) > 15):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The password field must contain less than 16 characters", icon='error')
				return False

			label.config(fg="SpringGreen3")
			return True


		def validate_firstname(value, label):
			if (value == ""):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The firstname field cannot be empty", icon='error')
				return False
			if (value.isdigit()):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The firstname field can only contain letters", icon='error')
				return False
			if (len(value) >15):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The firstname field can only contain 15 characters", icon='error')
				return False

			label.config(fg="SpringGreen3")
			return True


		def validate_surname(value, label):
			if (value == ""):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The firstname field cannot be empty", icon='error')
				return False
			if (value.isdigit()):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The firstname field can only contain letters", icon='error')
				return False
			if (len(value) >15):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The firstname field can only contain 15 characters", icon='error')
				return False

			label.config(fg="SpringGreen3")
			return True



		def validate_address(value, label):
			if (value == ''):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The address field cannot be empty", icon='error')
				return False

			label.config(fg="SpringGreen3")
			return True


		def validate_all_availability(value, value2, value3, value4, value5, value6, value7):
			if (value ==0 and value2 ==0 and value3 ==0 and value4 ==0 and value5 ==0 and value6 ==0 and value7 ==0):
				messagebox.showinfo("Validation Error", "One availability should be selected", icon='error')
				return False

			return True


		def validate_monday_availability(value, value2, label):
			if (float(value) >= float(value2)):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "Monday start time must be before the end time", icon='error')
				return False

			label.config(fg="SpringGreen3")
			return True


		def validate_tuesday_availability(value, value2, label):
			if (float(value) >= float(value2)):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "Tuesday start time must be before the end time", icon='error')
				return False

			label.config(fg="SpringGreen3")
			return True


		def validate_wednesday_availability(value, value2, label):
			if (float(value) >= float(value2)):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "Wednesday start time must be before the end time", icon='error')
				return False

			label.config(fg="SpringGreen3")
			return True

		def validate_thursday_availability(value, value2, label):
			if (float(value) >= float(value2)):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "Thursday start time must be before the end time", icon='error')
				return False

			label.config(fg="SpringGreen3")
			return True


		def validate_friday_availability(value, value2, label):
			if (float(value) >= float(value2)):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "Friday start time must be before the end time", icon='error')
				return False

			label.config(fg="SpringGreen3")
			return True


		def validate_saturday_availability(value, value2, label):
			if (float(value) >= float(value2)):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "Saturday start time must be before the end time", icon='error')
				return False

			label.config(fg="SpringGreen3")
			return True


		def validate_sunday_availability(value, value2, label):
			if (float(value) >= float(value2)):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "Sunday start time must be before the end time", icon='error')
				return False

			label.config(fg="SpringGreen3")
			return True


		def validate_gender(label):
			label.config(fg="SpringGreen3")
			return True


		def validate_DOB(value, label):
			presentDate = datetime.datetime.now()
			date_formated = presentDate.strftime("%d/%m/%Y")

			d1 = datetime.datetime.strptime(value, "%d/%m/%Y").date()
			d2 = datetime.datetime.strptime(str(date_formated), "%d/%m/%Y").date()

			if d1>d2:
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The date selected cannot be after the current date", icon='error')
				return False

			label.config(fg="SpringGreen3")
			return True


		def validate_new_availability(value, value2, value3, value4, value5, value6, value7):
			if (value ==0 and value2 ==0 and value3 ==0 and value4 ==0 and value5 ==0 and value6 ==0 and value7 ==0):
				messagebox.showinfo("Validation Error", "One avaliablity day should be selected", icon='error')
				return False

			return True


		def clearTv():
			record=coach_search_Tv.get_children()
			for elements in record:
				coach_search_Tv.delete(elements)

		def clearTimesTv():
			record=coach_times_search_Tv.get_children()
			for elements in record:
				coach_times_search_Tv.delete(elements)


		def treeviewPopulate():
			clearTv()

			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
			c = conn.cursor()

			c.execute("SELECT * From coach")
			items = c.fetchall()
			conn.commit()
			conn.close()

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


		def treeviewresizedisable(treeview, event):
			if treeview.identify_region(event.x, event.y) == "separator":
				return "break"


		def timestreeviewPopulate():
			clearTimesTv()

			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
			c = conn.cursor()

			c.execute("SELECT * From coachTimetable")
			items = c.fetchall()
			conn.commit()
			conn.close()

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


		def check_monday_checkbox(value):
			if (value.get() == 0):
				monday_from_combobox.config(state="disable")
				monday_to_combobox.config(state="disable")
				monday_from_combobox.current(0)
				monday_to_combobox.current(0)
			else:
				monday_from_combobox.config(state="readonly")
				monday_to_combobox.config(state="readonly")


		def check_tuesday_checkbox(value):
			if (value.get() == 0):
				tuesday_from_combobox.config(state="disable")
				tuesday_to_combobox.config(state="disable")
				tuesday_from_combobox.current(0)
				tuesday_to_combobox.current(0)
			else:
				tuesday_from_combobox.config(state="readonly")
				tuesday_to_combobox.config(state="readonly")


		def check_wednesday_checkbox(value):
			if (value.get() == 0):
				wednesday_from_combobox.config(state="disable")
				wednesday_to_combobox.config(state="disable")
				wednesday_from_combobox.current(0)
				wednesday_to_combobox.current(0)
			else:
				wednesday_from_combobox.config(state="readonly")
				wednesday_to_combobox.config(state="readonly")


		def check_thursday_checkbox(value):
			if (value.get() == 0):
				thursday_from_combobox.config(state="disable")
				thursday_to_combobox.config(state="disable")
				thursday_from_combobox.current(0)
				thursday_to_combobox.current(0)
			else:
				thursday_from_combobox.config(state="readonly")
				thursday_to_combobox.config(state="readonly")


		def check_friday_checkbox(value):
			if (value.get() == 0):
				friday_from_combobox.config(state="disable")
				friday_to_combobox.config(state="disable")
				friday_from_combobox.current(0)
				friday_to_combobox.current(0)
			else:
				friday_from_combobox.config(state="readonly")
				friday_to_combobox.config(state="readonly")


		def check_saturday_checkbox(value):
			if (value.get() == 0):
				saturday_from_combobox.config(state="disable")
				saturday_to_combobox.config(state="disable")
				saturday_from_combobox.current(0)
				saturday_to_combobox.current(0)
			else:
				saturday_from_combobox.config(state="readonly")
				saturday_to_combobox.config(state="readonly")


		def check_sunday_checkbox(value):
			if (value.get() == 0):
				sunday_from_combobox.config(state="disable")
				sunday_to_combobox.config(state="disable")
				sunday_from_combobox.current(0)
				sunday_to_combobox.current(0)
			else:
				sunday_from_combobox.config(state="readonly")
				sunday_to_combobox.config(state="readonly")


		def updateCoachDetails(self):
			response = askyesno("Question", "Do you want to update a coach's details?", icon='question')
			if response == False:
				showinfo("Info", "Update cancelled", icon='info')

			else:

				updateCoach=Toplevel(bg="white")

				title_label =Label(updateCoach,text = 'Update Coach' , fg ='SpringGreen3',bg='white',font=('Verdana',15,'bold'))
				title_label.place(rely=0.13,relx=0.5,anchor=CENTER)

				update_postcode=Button(updateCoach,text = 'Update Postcode', command = lambda : update_coach_postcode(updateCoach), fg ='white', bg='black', relief= 'groove', font = ('Verdana',10,'bold'), padx =20, pady =8)
				update_postcode.place(rely=0.43,relx=0.5,anchor=CENTER)

				update_availiability=Button(updateCoach,text = 'Update Availability', command = lambda : update_coach_availability(updateCoach), fg ='white', bg='black', relief= 'groove', font = ('Verdana',10,'bold'), padx =20, pady =8)
				update_availiability.place(rely=0.75,relx=0.5,anchor=CENTER)


		def update_coach_postcode(frame):
			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
			c = conn.cursor()

			frame.withdraw()

			coachUsername = simpledialog.askstring("Response", "Enter the username of the coach you want to update")
			if coachUsername != '' and len(coachUsername) <25 and '@' in coachUsername and '.' in coachUsername:
				c.execute(f"SELECT * FROM coach WHERE username=?", (coachUsername,))
				data = c.fetchone()
				if not data:
					messagebox.showinfo("Error", "The username entered was not found in the database", icon='error')

				else:

					new_postcode = simpledialog.askstring("Response", "Enter your new postcode")

					if new_postcode != '' and len(new_postcode) < 9 and ' ' in new_postcode:

						c.execute("""UPDATE coach SET postcode = :new_postcode WHERE username=:username""", {
							"new_postcode": str(new_postcode),
							"username": coachUsername
						})

						messagebox.showinfo("Info", "The coach's postcode is now "+new_postcode, icon='info')

					else:

						messagebox.showinfo("Error", "The postcode entered does not meet the rules", icon='error')

			else:

				messagebox.showinfo("Error", "The username entered does not meet the rules", icon='error')

			conn.commit()
			conn.close()

			treeviewPopulate()


		def update_coach_availability(frame):
			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
			c = conn.cursor()

			frame.withdraw()

			coachUsername = simpledialog.askstring("Response", "Enter the username of the coach you want to update")
			if coachUsername != '' and len(coachUsername) <25 and '@' in coachUsername and '.' in coachUsername:
				c.execute(f"SELECT * FROM coach WHERE username=?", (coachUsername,))
				data = c.fetchone()
				if not data:
					messagebox.showinfo("Error", "The username entered was not found in the database", icon='error')

				else:

					updateAvailiability=Toplevel(bg="white")
					updateAvailiability.geometry('200x200')

					title_label =Label(updateAvailiability,text ="Select Available Days" , fg ='SpringGreen3',bg='white',font=('Verdana',11,'bold','underline'))
					title_label.place(rely=0.07,relx=0.5,anchor=CENTER)

					avaliability_monday = Checkbutton(updateAvailiability, cursor="tcross",text="Monday", variable=mondayNewAvaliability,bg="white",bd=2, relief="sunken", font=('Segoe UI Black', 8,'bold'),onvalue=1, offvalue=0)
					avaliability_monday.place(rely=0.3, relx=0.28, anchor='center')

					avaliability_tuesday = Checkbutton(updateAvailiability, cursor="tcross",text="Tuesday", variable=tuesdayNewAvaliability,bg="white",bd=2, relief="sunken", font=('Segoe UI Black', 8,'bold'),onvalue=1, offvalue=0)
					avaliability_tuesday.place(rely=0.3, relx=0.72, anchor='center')

					avaliability_wednesday = Checkbutton(updateAvailiability, cursor="tcross",text="Wednesday", variable=wednesdayNewAvaliability,bg="white",bd=2, relief="sunken", font=('Segoe UI Black', 8,'bold'),onvalue=1, offvalue=0)
					avaliability_wednesday.place(rely=0.45, relx=0.25, anchor='center')

					avaliability_thursday = Checkbutton(updateAvailiability, cursor="tcross",text="Thursday", variable=thursdayNewAvaliability,bg="white",bd=2, relief="sunken", font=('Segoe UI Black', 8,'bold'),onvalue=1, offvalue=0)
					avaliability_thursday.place(rely=0.45, relx=0.75, anchor='center')

					avaliability_friday = Checkbutton(updateAvailiability, cursor="tcross",text="Friday", variable=fridayNewAvaliability,bg="white",bd=2, relief="sunken", font=('Segoe UI Black', 8,'bold'),onvalue=1, offvalue=0)
					avaliability_friday.place(rely=0.6, relx=0.28, anchor='center')

					avaliability_saturday = Checkbutton(updateAvailiability, cursor="tcross",text="Saturday", variable=saturdayNewAvaliability,bg="white",bd=2, relief="sunken", font=('Segoe UI Black', 8,'bold'),onvalue=1, offvalue=0)
					avaliability_saturday.place(rely=0.6, relx=0.72, anchor='center')

					avaliability_sunday = Checkbutton(updateAvailiability, cursor="tcross",text="Sunday", variable=sundayNewAvaliability,bg="white",bd=2, relief="sunken", font=('Segoe UI Black', 8,'bold'),onvalue=1, offvalue=0)
					avaliability_sunday.place(rely=0.75, relx=0.5, anchor='center')

					availiable_update_button=Button(updateAvailiability,text = 'Confirm Update', command = lambda : availableUpdate(updateAvailiability, coachUsername), fg ='white', bg='black', relief= 'groove', font = ('Verdana',11,'bold'), padx =30)
					availiable_update_button.place(rely=0.93,relx=0.5,anchor=CENTER)

			conn.commit()
			conn.close()


		def availableUpdate(frame, username):
			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
			c = conn.cursor()

			frame.withdraw()

			isValid = True
			isValid = isValid and validate_new_availability(mondayNewAvaliability.get(), tuesdayNewAvaliability.get(), wednesdayNewAvaliability.get(), thursdayNewAvaliability.get(), fridayNewAvaliability.get(), saturdayNewAvaliability.get(), sundayNewAvaliability.get(), "Availability")

			if isValid:
				new_final_avaliability = ""
				if (mondayNewAvaliability.get() ==1):
					new_final_avaliability = new_final_avaliability + 'monday, '
				if (tuesdayNewAvaliability.get() ==1):
					new_final_avaliability = new_final_avaliability +  'tuesday, '
				if (wednesdayNewAvaliability.get() ==1):
					new_final_avaliability = new_final_avaliability + 'wednesday, '
				if (thursdayNewAvaliability.get() ==1):
					new_final_avaliability = new_final_avaliability + 'thursday, '
				if (fridayNewAvaliability.get() ==1):
					new_final_avaliability = new_final_avaliability + 'friday, '
				if (saturdayNewAvaliability.get() ==1):
					new_final_avaliability = new_final_avaliability + 'saturday, '
				if (sundayNewAvaliability.get() ==1):
					new_final_avaliability = new_final_avaliability + 'sunday'

				c.execute("""UPDATE coach SET availability = :new_availability WHERE username=:username""", {
					"new_availability": str(new_final_avaliability),
					"username": username
				})

				messagebox.showinfo("Info", "The coach's availability is now "+new_final_avaliability, icon='info')



			conn.commit()
			conn.close()

			treeviewPopulate()
			timestreeviewPopulate()


		def deleteCoachDetails(self):
			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
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
						messagebox.showinfo("Info", "The coach with username "+coachUsername+" has been deleted from the database", icon='info')

				else:

					messagebox.showinfo("Error", "The username entered does not meet the rules", icon='error')

			conn.commit()
			conn.close()

			treeviewPopulate()
			timestreeviewPopulate()


		def searchCoachDetails():
			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
			c = conn.cursor()

			response = askyesno("Question", "Do you want to search a coach's details?", icon='question')
			if response == False:
				showinfo("Info", "Search cancelled", icon='info')

			else:

				coachUsername = simpledialog.askstring("Response", "Enter the username of the coach you want to see information for")
				if coachUsername != '' and len(coachUsername) <25 and '@' in coachUsername and '.' in coachUsername:
					coachDetails1 = c.execute(f"SELECT * FROM coach WHERE username=?", (coachUsername,))
					coachDetails2 = c.execute(f"SELECT * FROM coachTimetable WHERE username=?", (coachUsername,))
					data = coachDetails1.fetchone()
					data2 = coachDetails2.fetchone()
					if not data:
						messagebox.showinfo("Error", "The username entered was not found in the database", icon='error')
					else:

						messagebox.showinfo("Info", "The coach's details are listed below" + "\n\n" + "Username: " + str(data[0]) + "\n" + "Password: " + str(data[1]) + "\n" + "Firstname: " + str(data[2]) + "\n" + "Surname: " + str(data[3]) + "\n" + "Gender: " + str(data[4]) + "\n" + "DOB: " + str(data[5]) + "\n" + "Address: " + str(data[6]) + "\n" + "Availability: " + str(data[7]), icon='info')
						messagebox.showinfo("Info", "The coach's Timetable is listed below" + "\n\n" + "Username: " + str(data2[0]) + "\n" + "Monday: " + str(data2[1]) + "\n" + "Tuesday: " + str(data2[2]) + "\n" + "Wednesday: " + str(data2[3]) + "\n" + "Thursday: " + str(data2[4]) + "\n" + "Friday: " + str(data2[5]) + "\n" + "Saturday: " + str(data2[6]) + "\n" + "Sunday: " + str(data2[7]), icon='info')

				else:

					messagebox.showinfo("Error", "The username entered does not meet the rules", icon='error')

			conn.commit()
			conn.close()

			treeviewPopulate()
			timestreeviewPopulate()


		def saveCoachDetails():
			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
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
			if (mondayAvaliability.get() ==1):
				isValid = isValid and validate_monday_availability(monday_from_combobox.get(),monday_to_combobox.get(), monday_label)
			if (tuesdayAvaliability.get() ==1):
				isValid = isValid and validate_tuesday_availability(tuesday_from_combobox.get(),tuesday_to_combobox.get(), tuesday_label)
			if (wednesdayAvaliability.get() ==1):
				isValid = isValid and validate_wednesday_availability(wednesday_from_combobox.get(),wednesday_to_combobox.get(), wednesday_label)
			if (thursdayAvaliability.get() ==1):
				isValid = isValid and validate_thursday_availability(thursday_from_combobox.get(),thursday_to_combobox.get(), thursday_label)
			if (fridayAvaliability.get() ==1):
				isValid = isValid and validate_friday_availability(friday_from_combobox.get(),friday_to_combobox.get(), friday_label)
			if (saturdayAvaliability.get() ==1):
				isValid = isValid and validate_saturday_availability(saturday_from_combobox.get(),saturday_to_combobox.get(), saturday_label)
			if (sundayAvaliability.get() ==1):
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

				final_avaliability = ""
				if (mondayAvaliability.get() ==1):
					final_avaliability = final_avaliability + 'monday, '
				if (tuesdayAvaliability.get() ==1):
					final_avaliability = final_avaliability + 'tuesday, '
				if (wednesdayAvaliability.get() ==1):
					final_avaliability = final_avaliability + 'wednesday, '
				if (thursdayAvaliability.get() ==1):
					final_avaliability = final_avaliability + 'thursday, '
				if (fridayAvaliability.get() ==1):
					final_avaliability = final_avaliability + 'friday, '
				if (saturdayAvaliability.get() ==1):
					final_avaliability = final_avaliability + 'saturday, '
				if (sundayAvaliability.get() ==1):
					final_avaliability = final_avaliability + 'sunday'

				mondayFinalAvaliability = ""
				tuesdayFinalAvaliability = ""
				wednesdayFinalAvaliability = ""
				thursdayFinalAvaliability = ""
				fridayFinalAvaliability = ""
				saturdayFinalAvaliability = ""
				sundayFinalAvaliability = ""
				if (mondayAvaliability.get() ==0):
					mondayFinalAvaliability = "n/a"
				if (mondayAvaliability.get() ==1):
					mondayFinalAvaliability = monday_from_combobox.get() + "-" + monday_to_combobox.get()
				if (tuesdayAvaliability.get() ==0):
					tuesdayFinalAvaliability = "n/a"
				if (tuesdayAvaliability.get() ==1):
					tuesdayFinalAvaliability = tuesday_from_combobox.get() + "-" + tuesday_to_combobox.get()
				if (wednesdayAvaliability.get() ==0):
					wednesdayFinalAvaliability = "n/a"
				if (wednesdayAvaliability.get() ==1):
					wednesdayFinalAvaliability = wednesday_from_combobox.get() + "-" + wednesday_to_combobox.get()
				if (thursdayAvaliability.get() ==0):
					thursdayFinalAvaliability = "n/a"
				if (thursdayAvaliability.get() ==1):
					thursdayFinalAvaliability = thursday_from_combobox.get() + "-" + thursday_to_combobox.get()
				if (fridayAvaliability.get() ==0):
					fridayFinalAvaliability = "n/a"
				if (fridayAvaliability.get() ==1):
					fridayFinalAvaliability = friday_from_combobox.get() + "-" + friday_to_combobox.get()
				if (saturdayAvaliability.get() ==0):
					saturdayFinalAvaliability = "n/a"
				if (saturdayAvaliability.get() ==1):
					saturdayFinalAvaliability = saturday_from_combobox.get() + "-" + saturday_to_combobox.get()
				if (sundayAvaliability.get() ==0):
					sundayFinalAvaliability = "n/a"
				if (sundayAvaliability.get() ==1):
					sundayFinalAvaliability = sunday_from_combobox.get() + "-" + sunday_to_combobox.get()


				response = askyesno("Question", "Are you sure that all information above is correct?", icon='question')
				if response == False:
					showinfo("Info", "submition cancelled", icon='info')

				else:

					doc = buildCoachDocument(coach_username, coach_password, coach_firstname, coach_surname, final_coach_gender, coach_DOB, coach_address, mondayFinalAvaliability, tuesdayFinalAvaliability, wednesdayFinalAvaliability, thursdayFinalAvaliability, fridayFinalAvaliability, saturdayFinalAvaliability, sundayFinalAvaliability)
					found = Email("Lisburn Racquets Coach Added", "Good work on securing a coach position at Lisburn Racquets Club" + "\n" + "Your details can be found in the document below." + "\n\n" + "Thanks for choosing Lisburn Racquets Club", coach_username, doc, username_label)
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
									  'availabilty': final_avaliability,
								  })

						c.execute("INSERT INTO coachTimetable VALUES (:username, :monday, :tuesday, :wednesday, :thursday, :friday, :saturday, :sunday)",
								  {
									  'username': coach_username,
									  'monday': mondayFinalAvaliability,
									  'tuesday': tuesdayFinalAvaliability,
									  'wednesday': wednesdayFinalAvaliability,
									  'thursday': thursdayFinalAvaliability,
									  'friday': fridayFinalAvaliability,
									  'saturday': saturdayFinalAvaliability,
									  'sunday': sundayFinalAvaliability,
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

		mondayNewAvaliability=IntVar()
		tuesdayNewAvaliability=IntVar()
		wednesdayNewAvaliability=IntVar()
		thursdayNewAvaliability=IntVar()
		fridayNewAvaliability=IntVar()
		saturdayNewAvaliability=IntVar()
		sundayNewAvaliability=IntVar()

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



		username_label = tkinter.Label(self.coach, text="Username:", font=('Tahoma', 14, 'bold'), fg='black', bg='white')
		username_label.place(rely=0.13, relx=0.09, anchor='center')

		password_label = tkinter.Label(self.coach, text="Password:", font=('Tahoma', 14, 'bold'), fg='black', bg='white')
		password_label.place(rely=0.2, relx=0.09, anchor='center')

		firstname_label = tkinter.Label(self.coach, text="Firstname:", font=('Tahoma', 14, 'bold'), fg='black', bg='white')
		firstname_label.place(rely=0.27, relx=0.09, anchor='center')

		surname_label = tkinter.Label(self.coach, text="Surname:", font=('Tahoma', 14, 'bold'), fg='black', bg='white')
		surname_label.place(rely=0.34, relx=0.09, anchor='center')

		gender_label = tkinter.Label(self.coach, text="Gender:", font=('Tahoma', 14, 'bold'), fg='black', bg='white')
		gender_label.place(rely=0.415, relx=0.09, anchor='center')

		DOB_label = tkinter.Label(self.coach, text="DOB:", font=('Tahoma', 14, 'bold'), fg='black', bg='white')
		DOB_label.place(rely=0.495, relx=0.09, anchor='center')

		address_label = tkinter.Label(self.coach, text="Address:", font=('Tahoma', 14, 'bold'), fg='black', bg='white')
		address_label.place(rely=0.57, relx=0.09, anchor='center')


		username_entry = tkinter.Entry(self.coach, width=25, textvariable=username, bd=3, relief='ridge', cursor="tcross")
		username_entry.place(rely=0.133, relx=0.25, anchor='center')

		password_entry = tkinter.Entry(self.coach, width=15, textvariable=password, show='*', bd=3, relief='ridge', cursor="tcross")
		password_entry.place(rely=0.203, relx=0.25, anchor='center')

		firstname_entry = tkinter.Entry(self.coach, width=15, textvariable=firstname, bd=3, relief='ridge', cursor="tcross")
		firstname_entry.place(rely=0.273, relx=0.25, anchor='center')

		surname_entry = tkinter.Entry(self.coach, width=15, textvariable=surname, bd=3, relief='ridge', cursor="tcross")
		surname_entry.place(rely=0.343, relx=0.25, anchor='center')

		male_radiobutton = Radiobutton(self.coach, text="Male", variable=gender, value=1, font=("Segoe UI Black",9, 'bold'), cursor="tcross", bg="white", bd=2, relief="ridge")
		male_radiobutton.place(rely=0.418, relx=0.2, anchor='center')

		female_radiobutton = Radiobutton(self.coach, text="Female", variable=gender, value=2, font=("Segoe UI Black",9, 'bold'), cursor="tcross", bg="white", bd=2, relief="ridge")
		female_radiobutton.place(rely=0.418, relx=0.3, anchor='center')
		gender.set("1")

		DOB_button = Button(self.coach, text='Select DOB',font=("Tahoma",10, 'bold'), cursor="tcross",command=lambda : dateEntryCheck(dateOfBirth), padx=10, bd=4, relief="ridge")
		DOB_button.place(rely=0.498, relx=0.25, anchor='center')

		address_entry = tkinter.Entry(self.coach, width=25, textvariable=address, bd=3, relief='ridge', cursor="tcross")
		address_entry.place(rely=0.573, relx=0.25, anchor='center')


		line = Canvas(self.coach, width=360, height=1)
		line.config(bg='black')
		line.create_line(3, 0, 200, 100000)
		line.place(rely=0.61462, relx=0.18, anchor='center')


		monday_label = tkinter.Label(self.coach, text="Monday:", font=('Tahoma', 10, 'bold'), fg='black', bg='white')
		monday_label.place(rely=0.66, relx=0.05, anchor='center')

		monday_checkbox = Checkbutton(self.coach, cursor="tcross", command=lambda : check_monday_checkbox(mondayAvaliability), variable=mondayAvaliability,bg="white",bd=2, relief="groove", font=('Segoe UI Black', 6,'bold'),onvalue=1, offvalue=0)
		monday_checkbox.place(rely=0.662, relx=0.11, anchor='center')

		monday_from_label = tkinter.Label(self.coach, text="From:", font=('Tahoma', 10, 'bold'), fg='black', bg='white')
		monday_from_label.place(rely=0.66, relx=0.18, anchor='center')

		monday_from_combobox = ttk.Combobox(self.coach, value=monday_from_Avaliability_times,font=('Tahoma', 8, 'bold'), width=5)
		monday_from_combobox.place(rely=0.661, relx=0.24, anchor='center')
		monday_from_combobox.current(0)
		monday_from_combobox.config(state="disable")

		monday_to_label = tkinter.Label(self.coach, text="To:", font=('Tahoma', 10, 'bold'), fg='black', bg='white')
		monday_to_label.place(rely=0.66, relx=0.32, anchor='center')

		monday_to_combobox = ttk.Combobox(self.coach, value=monday_to_Avaliability_times, font=('Tahoma', 8, 'bold'), width=5)
		monday_to_combobox.place(rely=0.661, relx=0.37, anchor='center')
		monday_to_combobox.current(0)
		monday_to_combobox.config(state="disable")


		tuesday_label = tkinter.Label(self.coach, text="Tuesday:", font=('Tahoma', 10, 'bold'), fg='black', bg='white')
		tuesday_label.place(rely=0.73, relx=0.05, anchor='center')

		tuesday_checkbox = Checkbutton(self.coach, cursor="tcross", command=lambda : check_tuesday_checkbox(tuesdayAvaliability), variable=tuesdayAvaliability,bg="white",bd=2, relief="groove", font=('Segoe UI Black', 6,'bold'),onvalue=1, offvalue=0)
		tuesday_checkbox.place(rely=0.732, relx=0.11, anchor='center')

		tuesday_from_label = tkinter.Label(self.coach, text="From:", font=('Tahoma', 10, 'bold'), fg='black', bg='white')
		tuesday_from_label.place(rely=0.73, relx=0.18, anchor='center')

		tuesday_from_combobox = ttk.Combobox(self.coach, value=tuesday_from_Avaliability_times, font=('Tahoma', 8, 'bold'), width=5)
		tuesday_from_combobox.place(rely=0.731, relx=0.24, anchor='center')
		tuesday_from_combobox.current(0)
		tuesday_from_combobox.config(state="disable")

		tuesday_to_label = tkinter.Label(self.coach, text="To:", font=('Tahoma', 10, 'bold'), fg='black', bg='white')
		tuesday_to_label.place(rely=0.73, relx=0.32, anchor='center')

		tuesday_to_combobox = ttk.Combobox(self.coach, value=tuesday_to_Avaliability_times, font=('Tahoma', 8, 'bold'), width=5)
		tuesday_to_combobox.place(rely=0.731, relx=0.37, anchor='center')
		tuesday_to_combobox.current(0)
		tuesday_to_combobox.config(state="disable")


		wednesday_label = tkinter.Label(self.coach, text="Wednesday:", font=('Tahoma', 10, 'bold'), fg='black', bg='white')
		wednesday_label.place(rely=0.8, relx=0.05, anchor='center')

		wednesday_checkbox = Checkbutton(self.coach, cursor="tcross", command=lambda : check_wednesday_checkbox(wednesdayAvaliability), variable=wednesdayAvaliability,bg="white",bd=2, relief="groove", font=('Segoe UI Black', 6,'bold'),onvalue=1, offvalue=0)
		wednesday_checkbox.place(rely=0.802, relx=0.11, anchor='center')

		wednesday_from_label = tkinter.Label(self.coach, text="From:", font=('Tahoma', 10, 'bold'), fg='black', bg='white')
		wednesday_from_label.place(rely=0.8, relx=0.18, anchor='center')

		wednesday_from_combobox = ttk.Combobox(self.coach, value=wednesday_from_Avaliability_times, font=('Tahoma', 8, 'bold'), width=5)
		wednesday_from_combobox.place(rely=0.801, relx=0.24, anchor='center')
		wednesday_from_combobox.current(0)
		wednesday_from_combobox.config(state="disable")

		wednesday_to_label = tkinter.Label(self.coach, text="To:", font=('Tahoma', 10, 'bold'), fg='black', bg='white')
		wednesday_to_label.place(rely=0.8, relx=0.32, anchor='center')

		wednesday_to_combobox = ttk.Combobox(self.coach, value=wednesday_to_Avaliability_times, font=('Tahoma', 8, 'bold'), width=5)
		wednesday_to_combobox.place(rely=0.801, relx=0.37, anchor='center')
		wednesday_to_combobox.current(0)
		wednesday_to_combobox.config(state="disable")


		thursday_label = tkinter.Label(self.coach, text="Thursday:", font=('Tahoma', 10, 'bold'), fg='black', bg='white')
		thursday_label.place(rely=0.87, relx=0.05, anchor='center')

		thursday_checkbox = Checkbutton(self.coach, cursor="tcross", command=lambda : check_thursday_checkbox(thursdayAvaliability), variable=thursdayAvaliability,bg="white",bd=2, relief="groove", font=('Segoe UI Black', 6,'bold'),onvalue=1, offvalue=0)
		thursday_checkbox.place(rely=0.872, relx=0.11, anchor='center')

		thursday_from_label = tkinter.Label(self.coach, text="From:", font=('Tahoma', 10, 'bold'), fg='black', bg='white')
		thursday_from_label.place(rely=0.87, relx=0.18, anchor='center')

		thursday_from_combobox = ttk.Combobox(self.coach, value=thursday_from_Avaliability_times, font=('Tahoma', 8, 'bold'), width=5)
		thursday_from_combobox.place(rely=0.871, relx=0.24, anchor='center')
		thursday_from_combobox.current(0)
		thursday_from_combobox.config(state="disable")

		thursday_to_label = tkinter.Label(self.coach, text="To:", font=('Tahoma', 10, 'bold'), fg='black', bg='white')
		thursday_to_label.place(rely=0.87, relx=0.32, anchor='center')

		thursday_to_combobox = ttk.Combobox(self.coach, value=thursday_to_Avaliability_times, font=('Tahoma', 8, 'bold'), width=5)
		thursday_to_combobox.place(rely=0.871, relx=0.37, anchor='center')
		thursday_to_combobox.current(0)
		thursday_to_combobox.config(state="disable")


		friday_label = tkinter.Label(self.coach, text="Friday:", font=('Tahoma', 10, 'bold'), fg='black', bg='white')
		friday_label.place(rely=0.94, relx=0.05, anchor='center')

		friday_checkbox = Checkbutton(self.coach, cursor="tcross", command=lambda : check_friday_checkbox(fridayAvaliability), variable=fridayAvaliability,bg="white",bd=2, relief="groove", font=('Segoe UI Black', 6,'bold'),onvalue=1, offvalue=0)
		friday_checkbox.place(rely=0.942, relx=0.11, anchor='center')

		friday_from_label = tkinter.Label(self.coach, text="From:", font=('Tahoma', 10, 'bold'), fg='black', bg='white')
		friday_from_label.place(rely=0.94, relx=0.18, anchor='center')

		friday_from_combobox = ttk.Combobox(self.coach, value=friday_from_Avaliability_times, font=('Tahoma', 8, 'bold'), width=5)
		friday_from_combobox.place(rely=0.941, relx=0.24, anchor='center')
		friday_from_combobox.current(0)
		friday_from_combobox.config(state="disable")

		friday_to_label = tkinter.Label(self.coach, text="To:", font=('Tahoma', 10, 'bold'), fg='black', bg='white')
		friday_to_label.place(rely=0.94, relx=0.32, anchor='center')

		friday_to_combobox = ttk.Combobox(self.coach, value=friday_to_Avaliability_times, font=('Tahoma', 8, 'bold'), width=5)
		friday_to_combobox.place(rely=0.941, relx=0.37, anchor='center')
		friday_to_combobox.current(0)
		friday_to_combobox.config(state="disable")


		saturday_label = tkinter.Label(self.coach, text="Saturday:", font=('Tahoma', 10, 'bold'), fg='black', bg='white')
		saturday_label.place(rely=0.825, relx=0.52, anchor='center')

		saturday_checkbox = Checkbutton(self.coach, cursor="tcross", command=lambda : check_saturday_checkbox(saturdayAvaliability), variable=saturdayAvaliability,bg="white",bd=2, relief="groove", font=('Segoe UI Black', 6,'bold'),onvalue=1, offvalue=0)
		saturday_checkbox.place(rely=0.827, relx=0.58, anchor='center')

		saturday_from_label = tkinter.Label(self.coach, text="From:", font=('Tahoma', 10, 'bold'), fg='black', bg='white')
		saturday_from_label.place(rely=0.825, relx=0.65, anchor='center')

		saturday_from_combobox = ttk.Combobox(self.coach, value=saturday_from_Avaliability_times,font=('Tahoma', 8, 'bold'), width=5)
		saturday_from_combobox.place(rely=0.826, relx=0.71, anchor='center')
		saturday_from_combobox.current(0)
		saturday_from_combobox.config(state="disable")


		saturday_to_label = tkinter.Label(self.coach, text="To:", font=('Tahoma', 10, 'bold'), fg='black', bg='white')
		saturday_to_label.place(rely=0.825, relx=0.79, anchor='center')

		saturday_to_combobox = ttk.Combobox(self.coach, value=saturday_to_Avaliability_times, font=('Tahoma', 8, 'bold'), width=5)
		saturday_to_combobox.place(rely=0.826, relx=0.84, anchor='center')
		saturday_to_combobox.current(0)
		saturday_to_combobox.config(state="disable")


		sunday_label = tkinter.Label(self.coach, text="Sunday:", font=('Tahoma', 10, 'bold'), fg='black', bg='white')
		sunday_label.place(rely=0.885, relx=0.52, anchor='center')

		sunday_checkbox = Checkbutton(self.coach, cursor="tcross", command=lambda : check_sunday_checkbox(sundayAvaliability), variable=sundayAvaliability,bg="white",bd=2, relief="groove", font=('Segoe UI Black', 6,'bold'),onvalue=1, offvalue=0)
		sunday_checkbox.place(rely=0.887, relx=0.58, anchor='center')

		sunday_from_label = tkinter.Label(self.coach, text="From:", font=('Tahoma', 10, 'bold'), fg='black', bg='white')
		sunday_from_label.place(rely=0.885, relx=0.65, anchor='center')

		sunday_from_combobox = ttk.Combobox(self.coach, value=sunday_from_Avaliability_times, font=('Tahoma', 8, 'bold'), width=5)
		sunday_from_combobox.place(rely=0.886, relx=0.71, anchor='center')
		sunday_from_combobox.current(0)
		sunday_from_combobox.config(state="disable")

		sunday_to_label = tkinter.Label(self.coach, text="To:", font=('Tahoma', 10, 'bold'), fg='black', bg='white')
		sunday_to_label.place(rely=0.885, relx=0.79, anchor='center')

		sunday_to_combobox = ttk.Combobox(self.coach, value=sunday_to_Avaliability_times, font=('Tahoma', 8, 'bold'), width=5)
		sunday_to_combobox.place(rely=0.886, relx=0.84, anchor='center')
		sunday_to_combobox.current(0)
		sunday_to_combobox.config(state="disable")


		submit_button = tkinter.Button(self.coach, cursor="tcross",text="Submit", command=saveCoachDetails, fg='white', bg='black', bd=4, relief='ridge', font=('Segoe UI Black', 10, 'bold'), padx=30)
		submit_button.place(rely=0.95, relx=0.49, anchor='center')

		search_button = tkinter.Button(self.coach, cursor="tcross",text="Search", command=searchCoachDetails, fg='white', bg='black', bd=4, relief='ridge', font=('Segoe UI Black', 10, 'bold'), padx=32.4)
		search_button.place(rely=0.95, relx=0.63, anchor='center')

		update_button = tkinter.Button(self.coach, cursor="tcross",text="Update", command=lambda : updateCoachDetails(self), fg='white', bg='black', bd=4, relief='ridge', font=('Segoe UI Black', 10, 'bold'), padx=30)
		update_button.place(rely=0.95, relx=0.77, anchor='center')

		delete_button = tkinter.Button(self.coach, cursor="tcross",text="Delete", command=lambda : deleteCoachDetails(self), fg='white', bg='black', bd=4, relief='ridge', font=('Segoe UI Black', 10, 'bold'), padx=33.2)
		delete_button.place(rely=0.95, relx=0.91, anchor='center')


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
