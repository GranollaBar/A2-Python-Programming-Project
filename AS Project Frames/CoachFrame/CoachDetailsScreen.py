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
from tkcalendar import Calendar, DateEntry

from CoachFrame.coachEmail import coachEmail
from CoachFrame.coachWordDocument import buildCoachDocument


class CoachContent:

	def __init__(self, mainScreen):
		self.coach = mainScreen
		self.conn = sqlite3.connect('CoachDetails.db')
		self.c = self.conn.cursor()


		'''
		self.c.execute("""CREATE TABLE coach (
					username text,
					password text,
					firstname text,
					surname text,
					gender text,
					DOB text,
					postcode text,
					availability text
					)""")
		'''


	def generateCoachContnt(self):

		def dateEntryCheck(dob):
			def assign_dob():
				dateOfBirth.set(cal.selection_get())
				top.withdraw()

			top = Toplevel(self.coach)

			cal = Calendar(top, font="Tahoma 16", selectmode='day', cursor="tcross", day=29, month=5, year=2021)
			cal.pack(fill="both", expand=True)
			ttk.Button(top, text="Select", command=assign_dob).pack()


		def validate_password(value, fieldname, label):
			if (value == ''):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " Can Not Be Empty")
				return False
			if (len(value) < 8):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " Must contain more than 8 characters")
				return False
			if (len(value) > 15):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " Must contain less than 15 characters")
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


		def validate_availability(value, value2, value3, value4, value5, value6, value7, fieldname, label):
			if (value ==0 and value2 ==0 and value3 ==0 and value4 ==0 and value5 ==0 and value6 ==0 and value7 ==0):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " must have one selected")
				return False

			label.config(fg="SpringGreen3")
			return True


		def validate_gender(label):
			label.config(fg="SpringGreen3")
			return True


		def validate_DOB(label):
			label.config(fg="SpringGreen3")
			return True


		def validate_new_availability(value, value2, value3, value4, value5, value6, value7, fieldname):
			if (value ==0 and value2 ==0 and value3 ==0 and value4 ==0 and value5 ==0 and value6 ==0 and value7 ==0):
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " must have one selected")
				return False

			return True


		def clearTv():
			record=coach_search_Tv.get_children()
			for elements in record:
				coach_search_Tv.delete(elements)


		def treeviewPopulate():
			clearTv()

			conn = sqlite3.connect('CoachDetails.db')
			c = conn.cursor()

			c.execute("SELECT * From coach")
			items = c.fetchall()
			conn.commit()
			conn.close()

			coach_search_Tv.tag_configure("even",background="green")
			coach_search_Tv.tag_configure("odd",background="red")

			count=0
			for row in items:
				if row == []:
					pass
				else:
					if count%2==0:
						coach_search_Tv.insert('','end',text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7]),tags=["even"])
					else:
						coach_search_Tv.insert('','end',text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7]),tags=["odd"])
					count+=1


		def returnColour(usernameReturn, passwordReturn, firstnameReturn, surnameReturn, genderReturn, DOBReturn, postcodeReturn, availabilityReturn):
			usernameReturn.config(fg="black")
			passwordReturn.config(fg="black")
			firstnameReturn.config(fg="black")
			surnameReturn.config(fg="black")
			genderReturn.config(fg="black")
			DOBReturn.config(fg="black")
			postcodeReturn.config(fg="black")
			availabilityReturn.config(fg="black")


		def updateCoachDetails():
			response = askyesno("Are you sure?", "Do you want to update a coach's details")
			if response == False:
				showinfo("Info", "Update cancelled")

			else:

				updateCoach=Toplevel(bg="white")

				title_label =Label(updateCoach,text = 'Update Coach' , fg ='SpringGreen3',bg='white',font=('Verdana',15,'bold'))
				title_label.place(rely=0.13,relx=0.5,anchor=CENTER)

				update_postcode=Button(updateCoach,text = 'Update Postcode', command = lambda : update_coach_postcode(updateCoach), fg ='white', bg='black', relief= 'groove', font = ('Verdana',10,'bold'), padx =20, pady =8)
				update_postcode.place(rely=0.43,relx=0.5,anchor=CENTER)

				update_availiability=Button(updateCoach,text = 'Update Availability', command = lambda : update_coach_availability(updateCoach), fg ='white', bg='black', relief= 'groove', font = ('Verdana',10,'bold'), padx =20, pady =8)
				update_availiability.place(rely=0.75,relx=0.5,anchor=CENTER)





		def update_coach_postcode(frame):
			conn = sqlite3.connect('CoachDetails.db')
			c = conn.cursor()

			frame.withdraw()

			coachUsername = simpledialog.askstring("info", "Enter the username of the coach you want to update")
			if coachUsername != '' and len(coachUsername) <25 and '@' in coachUsername and '.' in coachUsername:
				c.execute(f"SELECT * FROM coach WHERE username=?", (coachUsername,))
				data = c.fetchone()
				if not data:
					messagebox.showinfo("Warning", "The username entered was not found in the database", icon='error')

				else:

					new_postcode = simpledialog.askstring("info", "Enter your new postcode")

					if new_postcode != '' and len(new_postcode) < 9 and ' ' in new_postcode:

						c.execute("""UPDATE coach SET postcode = :new_postcode""", {'new_postcode': new_postcode})
						messagebox.showinfo("info", "The coach's postcode is now "+new_postcode)

					else:

						messagebox.showinfo("Warning", "The postcode entered does not meet the rules", icon='error')

			else:

				messagebox.showinfo("Warning", "The username entered does not meet the rules", icon='error')

			conn.commit()
			conn.close()

			treeviewPopulate()


		def update_coach_availability(frame):
			conn = sqlite3.connect('CoachDetails.db')
			c = conn.cursor()

			frame.withdraw()

			coachUsername = simpledialog.askstring("info", "Enter the username of the coach you want to update")
			if coachUsername != '' and len(coachUsername) <25 and '@' in coachUsername and '.' in coachUsername:
				c.execute(f"SELECT * FROM coach WHERE username=?", (coachUsername,))
				data = c.fetchone()
				if not data:
					messagebox.showinfo("Warning", "The username entered was not found in the database", icon='error')

				else:

					updateAvailiability=Toplevel(bg="white")
					updateAvailiability.geometry('200x200')

					title_label =Label(updateAvailiability,text ="Select Available Days" , fg ='SpringGreen3',bg='white',font=('Verdana',9,'bold','underline'))
					title_label.place(rely=0.1,relx=0.5,anchor=CENTER)

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

					avaliability_saturday = Checkbutton(updateAvailiability, cursor="tcross",text="Saturday", variable=satrudayNewAvaliability,bg="white",bd=2, relief="sunken", font=('Segoe UI Black', 8,'bold'),onvalue=1, offvalue=0)
					avaliability_saturday.place(rely=0.6, relx=0.72, anchor='center')

					avaliability_sunday = Checkbutton(updateAvailiability, cursor="tcross",text="Sunday", variable=sundayNewAvaliability,bg="white",bd=2, relief="sunken", font=('Segoe UI Black', 8,'bold'),onvalue=1, offvalue=0)
					avaliability_sunday.place(rely=0.75, relx=0.5, anchor='center')

					availiable_update_button=Button(updateAvailiability,text = 'Confirm Update', command = lambda : availableUpdate(updateAvailiability), fg ='white', bg='black', relief= 'groove', font = ('Verdana',11,'bold'), padx =30)
					availiable_update_button.place(rely=0.93,relx=0.5,anchor=CENTER)

			conn.commit()
			conn.close()


		def availableUpdate(frame):
			conn = sqlite3.connect('CoachDetails.db')
			c = conn.cursor()

			frame.withdraw()

			isValid = True
			isValid = isValid and validate_new_availability(mondayNewAvaliability.get(), tuesdayNewAvaliability.get(), wednesdayNewAvaliability.get(), thursdayNewAvaliability.get(), fridayNewAvaliability.get(), satrudayNewAvaliability.get(), sundayNewAvaliability.get(), "Availability")

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
				if (satrudayNewAvaliability.get() ==1):
					new_final_avaliability = new_final_avaliability + 'saturday, '
				if (sundayNewAvaliability.get() ==1):
					new_final_avaliability = new_final_avaliability + 'sunday'

				c.execute("""UPDATE coach SET availability = :new_availabilty""", {'new_availabilty': new_final_avaliability})
				messagebox.showinfo("info", "The coach's avaliability is now "+new_final_avaliability)



			conn.commit()
			conn.close()

			treeviewPopulate()


		def deleteCoachDetails():
			conn = sqlite3.connect('CoachDetails.db')
			c = conn.cursor()

			response = askyesno("Are you sure?", "Do you want to delete a coach")
			if response == False:
				showinfo("Info", "Deletion cancelled")

			else:

				coachUsername = simpledialog.askstring("Info", "Enter the username of the coach you want to delete")

				if coachUsername !='' and len(coachUsername) <25 and '@' in coachUsername and '.' in coachUsername:

					c.execute(f"SELECT * FROM coach WHERE username =?", (coachUsername,))
					data = c.fetchone()
					if not data:
						messagebox.showinfo("Warning", "The username entered was not found in the database", icon='error')

					else:

						c.execute(f"DELETE FROM coach WHERE username =?", (coachUsername,))
						messagebox.showinfo("info", "The coach with username "+coachUsername+" has been deleted from the database")

				else:

					messagebox.showinfo("Warning", "The username entered does not meet the rules", icon='error')

			conn.commit()
			conn.close()

			treeviewPopulate()


		def searchCoachDetails():
			conn = sqlite3.connect('CoachDetails.db')
			c = conn.cursor()

			response = askyesno("Are you sure?", "Do you want to search a coach's details")
			if response == False:
				showinfo("Info", "Search cancelled")

			else:

				coachUsername = simpledialog.askstring("info", "Enter the username of the coach you want to see information for")
				if coachUsername != '' and len(coachUsername) <25 and '@' in coachUsername and '.' in coachUsername:
					c.execute(f"SELECT * FROM coach WHERE username=?", (coachUsername,))
					data = c.fetchone()
					if not data:
						messagebox.showinfo("Warning", "The username entered was not found in the database", icon='error')
					else:

						messagebox.showinfo("info", "The coach's details are listed below" + "\n\n" + "Username: " + str(data[0]) + "\n" + "Password: " + str(data[1]) + "\n" + "Firstname: " + str(data[2]) + "\n" + "Surname: " + str(data[3]) + "\n" + "Gender: " + str(data[4]) + "\n" + "DOB: " + str(data[5]) + "\n" + "Postcode: " + str(data[6]) + "\n" + "Availability: " + str(data[7]))

				else:

					messagebox.showinfo("Warning", "The username entered does not meet the rules", icon='error')

			conn.commit()
			conn.close()

			treeviewPopulate()


		def saveCoachDetails():
			conn = sqlite3.connect('CoachDetails.db')
			c = conn.cursor()

			isValid = True
			isValid = isValid and validate_username(username.get(), "Username", username_label)
			isValid = isValid and validate_password(password.get(), "Password", password_label)
			isValid = isValid and validate_not_empty_string(firstname.get(), "Firstname", firstname_label)
			isValid = isValid and validate_not_empty_string(surname.get(), "Surname", surname_label)
			isValid = isValid and validate_gender(gender_label)
			isValid = isValid and validate_DOB(DOB_label)
			isValid = isValid and validate_empty(postcode.get(), "Postcode", postcode_label)
			isValid = isValid and validate_availability(mondayAvaliability.get(), tuesdayAvaliability.get(), wednesdayAvaliability.get(), thursdayAvaliability.get(), fridayAvaliability.get(), satrudayAvaliability.get(), sundayAvaliability.get(),"Availability", avaliability_label)


			if isValid:
				coach_username = username.get()
				coach_password = password.get()
				coach_firstname = firstname.get()
				coach_surname = surname.get()
				coach_gender = gender.get()
				coach_DOB = dateOfBirth.get()
				coach_postcode = postcode.get()

				if (coach_gender == 1):
					final_coach_gender = 'Male'
				else:
					final_coach_gender = 'Female'

				final_avaliability = ""
				if (mondayAvaliability.get() ==1):
					final_avaliability = final_avaliability + 'monday, '
				if (tuesdayAvaliability.get() ==1):
					final_avaliability = final_avaliability +  'tuesday, '
				if (wednesdayAvaliability.get() ==1):
					final_avaliability = final_avaliability + 'wednesday, '
				if (thursdayAvaliability.get() ==1):
					final_avaliability = final_avaliability + 'thursday, '
				if (fridayAvaliability.get() ==1):
					final_avaliability = final_avaliability + 'friday, '
				if (satrudayAvaliability.get() ==1):
					final_avaliability = final_avaliability + 'saturday, '
				if (sundayAvaliability.get() ==1):
					final_avaliability = final_avaliability + 'sunday'

				response = askyesno("Are you sure?", "Are you sure that all information above is correct?")
				if response == False:
					showinfo("Info", "submition cancelled")

				else:

					doc = buildCoachDocument(coach_username, coach_password, coach_firstname, coach_surname, final_coach_gender, coach_DOB, coach_postcode, final_avaliability)
					found = coachEmail("Lisburn Racquets Coach Added", "Good work on securing a coach position at Lisburn Racquets Club" + "\n" + "Your details can be found in the document below." + "\n\n" + "Thanks for choosing Lisburn Racquets Club", coach_username, doc, username_label)
					if found:

						c.execute("INSERT INTO coach VALUES (:username, :password, :firstname, :surname, :gender, :DOB, :postcode, :availabilty)",
								  {
									  'username': coach_username,
									  'password': coach_password,
									  'firstname': coach_firstname,
									  'surname': coach_surname,
									  'gender': final_coach_gender,
									  'DOB': coach_DOB,
									  'postcode': coach_postcode,
									  'availabilty': final_avaliability,
								  })

						username.set('')
						password.set('')
						firstname.set('')
						surname.set('')
						gender.set('1')
						postcode.set('')
						mondayAvaliability.set('0')
						tuesdayAvaliability.set('0')
						wednesdayAvaliability.set('0')
						thursdayAvaliability.set('0')
						fridayAvaliability.set('0')
						satrudayAvaliability.set('0')
						sundayAvaliability.set('0')

						returnColour(username_label, password_label, firstname_label, surname_label, gender_label, DOB_label, postcode_label, avaliability_label)


				conn.commit()
				conn.close()

				treeviewPopulate()



		username = StringVar()
		password = StringVar()
		firstname=StringVar()
		surname=StringVar()
		gender=IntVar()
		dateOfBirth=StringVar()
		postcode=StringVar()
		mondayAvaliability=IntVar()
		tuesdayAvaliability=IntVar()
		wednesdayAvaliability=IntVar()
		thursdayAvaliability=IntVar()
		fridayAvaliability=IntVar()
		satrudayAvaliability=IntVar()
		sundayAvaliability=IntVar()

		mondayNewAvaliability=IntVar()
		tuesdayNewAvaliability=IntVar()
		wednesdayNewAvaliability=IntVar()
		thursdayNewAvaliability=IntVar()
		fridayNewAvaliability=IntVar()
		satrudayNewAvaliability=IntVar()
		sundayNewAvaliability=IntVar()





		username_label = tkinter.Label(self.coach, text="Username:", font=('Segoe UI Black', 14, 'bold'), fg='black', bg='white')
		username_label.place(rely=0.15, relx=0.09, anchor='center')

		password_label = tkinter.Label(self.coach, text="Password:", font=('Segoe UI Black', 14, 'bold'), fg='black', bg='white')
		password_label.place(rely=0.23, relx=0.09, anchor='center')

		firstname_label = tkinter.Label(self.coach, text="Firstname:", font=('Segoe UI Black', 14, 'bold'), fg='black', bg='white')
		firstname_label.place(rely=0.31, relx=0.09, anchor='center')

		surname_label = tkinter.Label(self.coach, text="Surname:", font=('Segoe UI Black', 14, 'bold'), fg='black', bg='white')
		surname_label.place(rely=0.39, relx=0.09, anchor='center')

		gender_label = tkinter.Label(self.coach, text="Gender:", font=('Segoe UI Black', 14, 'bold'), fg='black', bg='white')
		gender_label.place(rely=0.47, relx=0.09, anchor='center')

		DOB_label = tkinter.Label(self.coach, text="DOB:", font=('Segoe UI Black', 14, 'bold'), fg='black', bg='white')
		DOB_label.place(rely=0.55, relx=0.09, anchor='center')

		postcode_label = tkinter.Label(self.coach, text="Postcode:", font=('Segoe UI Black', 14, 'bold'), fg='black', bg='white')
		postcode_label.place(rely=0.63, relx=0.09, anchor='center')

		avaliability_label = tkinter.Label(self.coach, text="Avaliability:", font=('Segoe UI Black', 14, 'bold'), fg='black', bg='white')
		avaliability_label.place(rely=0.77, relx=0.09, anchor='center')


		username_entry = tkinter.Entry(self.coach, width=25, textvariable=username, bd=3, relief='ridge', cursor="tcross")
		username_entry.place(rely=0.153, relx=0.25, anchor='center')

		password_entry = tkinter.Entry(self.coach, width=15, textvariable=password, show='*', bd=3, relief='ridge', cursor="tcross")
		password_entry.place(rely=0.233, relx=0.25, anchor='center')

		firstname_entry = tkinter.Entry(self.coach, width=15, textvariable=firstname, bd=3, relief='ridge', cursor="tcross")
		firstname_entry.place(rely=0.313, relx=0.25, anchor='center')

		surname_entry = tkinter.Entry(self.coach, width=15, textvariable=surname, bd=3, relief='ridge', cursor="tcross")
		surname_entry.place(rely=0.393, relx=0.25, anchor='center')

		male_radiobutton = Radiobutton(self.coach, text="Male", variable=gender, value=1, font=("Segoe UI Black",9, 'bold'), cursor="tcross", bg="white", bd=2, relief="ridge")
		male_radiobutton.place(rely=0.47, relx=0.2, anchor='center')

		female_radiobutton = Radiobutton(self.coach, text="Female", variable=gender, value=2, font=("Segoe UI Black",9, 'bold'), cursor="tcross", bg="white", bd=2, relief="ridge")
		female_radiobutton.place(rely=0.47, relx=0.3, anchor='center')
		gender.set("1")

		DOB_button = Button(self.coach, text='Select DOB',font=("Tahoma",10, 'bold'), cursor="tcross",command=lambda : dateEntryCheck(dateOfBirth), padx=10, bd=4, relief="ridge")
		DOB_button.place(rely=0.553, relx=0.25, anchor='center')

		postcode_entry = tkinter.Entry(self.coach, width=10, textvariable=postcode, bd=3, relief='ridge', cursor="tcross")
		postcode_entry.place(rely=0.633, relx=0.25, anchor='center')

		avaliability_monday = Checkbutton(self.coach, cursor="tcross",text="Monday", variable=mondayAvaliability,bg="white",bd=2, relief="sunken", font=('Segoe UI Black', 9,'bold'),onvalue=1, offvalue=0)
		avaliability_monday.place(rely=0.7, relx=0.21, anchor='center')

		avaliability_tuesday = Checkbutton(self.coach, cursor="tcross",text="Tuesday", variable=tuesdayAvaliability,bg="white",bd=2, relief="sunken", font=('Segoe UI Black', 9,'bold'),onvalue=1, offvalue=0)
		avaliability_tuesday.place(rely=0.7, relx=0.31, anchor='center')

		avaliability_wednesday = Checkbutton(self.coach, cursor="tcross",text="Wednesday", variable=wednesdayAvaliability,bg="white",bd=2, relief="sunken", font=('Segoe UI Black', 9,'bold'),onvalue=1, offvalue=0)
		avaliability_wednesday.place(rely=0.75, relx=0.205, anchor='center')

		avaliability_thursday = Checkbutton(self.coach, cursor="tcross",text="Thursday", variable=thursdayAvaliability,bg="white",bd=2, relief="sunken", font=('Segoe UI Black', 9,'bold'),onvalue=1, offvalue=0)
		avaliability_thursday.place(rely=0.75, relx=0.32, anchor='center')

		avaliability_friday = Checkbutton(self.coach, cursor="tcross",text="Friday", variable=fridayAvaliability,bg="white",bd=2, relief="sunken", font=('Segoe UI Black', 9,'bold'),onvalue=1, offvalue=0)
		avaliability_friday.place(rely=0.8, relx=0.21, anchor='center')

		avaliability_saturday = Checkbutton(self.coach, cursor="tcross",text="Saturday", variable=satrudayAvaliability,bg="white",bd=2, relief="sunken", font=('Segoe UI Black', 9,'bold'),onvalue=1, offvalue=0)
		avaliability_saturday.place(rely=0.8, relx=0.31, anchor='center')

		avaliability_sunday = Checkbutton(self.coach, cursor="tcross",text="Sunday", variable=sundayAvaliability,bg="white",bd=2, relief="sunken", font=('Segoe UI Black', 9,'bold'),onvalue=1, offvalue=0)
		avaliability_sunday.place(rely=0.85, relx=0.26, anchor='center')

		background_entry_canvas = Canvas(self.coach,width=500, height=227, bg = "white")
		background_entry_canvas.place(rely=0.8,relx=0.7,anchor=CENTER)

		background_entry_image = PhotoImage(file = "kids_racquets.png")

		background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
		background_entry_canvas.background_entry_image = background_entry_image

		delete_button = tkinter.Button(self.coach, cursor="tcross",text="Delete", command=deleteCoachDetails, fg='white', bg='black', bd=4, relief='ridge', font=('Segoe UI Black', 11, 'bold'), padx=10)
		delete_button.place(rely=0.95, relx=0.058, anchor='center')

		update_button = tkinter.Button(self.coach, cursor="tcross",text="Update", command=updateCoachDetails, fg='white', bg='black', bd=4, relief='ridge', font=('Segoe UI Black', 11, 'bold'), padx=10)
		update_button.place(rely=0.95, relx=0.16, anchor='center')

		search_button = tkinter.Button(self.coach, cursor="tcross",text="Search", command=searchCoachDetails, fg='white', bg='black', bd=4, relief='ridge', font=('Segoe UI Black', 11, 'bold'), padx=10)
		search_button.place(rely=0.95, relx=0.264, anchor='center')

		create_button = tkinter.Button(self.coach, cursor="tcross",text="Submit", command=saveCoachDetails, fg='white', bg='black', bd=4, relief='ridge', font=('Segoe UI Black', 11, 'bold'), padx=10)
		create_button.place(rely=0.95, relx=0.368, anchor='center')


		coach_search_Tv=ttk.Treeview(self.coach,height=14,columns=('Password','Firstname','Surname','Gender','DOB','Postcode','Availability'))
		coach_search_Tv.place(relx=0.665,rely=0.35,anchor=CENTER)


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
		coach_search_Tv.heading("#6",text='Postcode')
		coach_search_Tv.column("#6",minwidth=0,width=70)
		coach_search_Tv.heading("#7",text='Days')
		coach_search_Tv.column("#7",minwidth=0,width=70)

		coach_ysearch_scrollbar = Scrollbar(self.coach, orient = 'vertical', command = coach_search_Tv.yview, cursor="tcross")
		coach_ysearch_scrollbar.place(relx=0.98,rely=0.35,anchor='center',height=307)
		coach_search_Tv.configure(yscrollcommand=coach_ysearch_scrollbar.set)


		treeviewPopulate()


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
