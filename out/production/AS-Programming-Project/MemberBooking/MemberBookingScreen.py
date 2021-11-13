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
import datetime
from tkinter import PhotoImage
import tkinter as tk

class BookingContent:

	def __init__(self, mainScreen):
		self.booking = mainScreen
		self.conn = sqlite3.connect('BadmintonClub.db')
		self.c = self.conn.cursor()
		self.conn2 = sqlite3.connect('BadmintonClub.db')
		self.c2 = self.conn2.cursor()


		# self.c.execute("""CREATE TABLE booking (
		# 			username text,
		# 			username2 text,
		# 			date text,
		# 			time text,
		# 			court text,
		# 			bookingID integer
		# 			)""")


	def generateBookingContnt(self):

		def validate_time(value, fieldname, label):
			if (value ==0):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " must have at least 1 selected")
				return False

			label.config(fg="SpringGreen3")
			return True


		def validate_court(value, fieldname, label):
			if (value ==0):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " must have at least 1 selected")
				return False

			label.config(fg="SpringGreen3")
			return True


		def validate_member(value, fieldname, label):
			if (value == ""):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " must have at least 1 selected")
				return False

			label.config(fg="SpringGreen3")
			return True


		def returnColour(label):
			label.config(fg="black")


		def returnColour2(label, label2):
			label.config(fg="black")
			label2.config(fg="black")



		def clearTv():
			record=booking_TV.get_children()
			for elements in record:
				booking_TV.delete(elements)


		def treeviewPopulate():
			clearTv()

			conn = sqlite3.connect('BadmintonClub.db')
			c = conn.cursor()

			c.execute("SELECT * From booking")
			items = c.fetchall()

			conn.commit()
			conn.close()

			count=0
			for row in items:
				if row == []:
					pass
				else:
					if count%2==0:
						booking_TV.insert('','end',text=row[0],values=(row[1],row[2],row[3],row[4]))
					else:
						booking_TV.insert('','end',text=row[0],values=(row[1],row[2],row[3],row[4]))
					count+=1


		def newTreeviewPopulate():
			clearTv()

			conn = sqlite3.connect('BadmintonClub.db')
			c = conn.cursor()

			c.execute("SELECT * From booking")
			items = c.fetchall()

			conn.commit()
			conn.close()

			count=0
			for row in items:
				if row == [] or row[1] == "" or row[2] == "":
					pass
				else:
					if count%2==0:
						booking_TV.insert('','end',text=row[0],values=(row[1],row[2],row[3],row[4]))
					else:
						booking_TV.insert('','end',text=row[0],values=(row[1],row[2],row[3],row[4]))
					count+=1



		def dateSelectionleft():
			currentDateSelected = date_label.cget("text")

			today = datetime.date.today()
			oneDay = datetime.date.today() + datetime.timedelta(days=1)
			twoDay = datetime.date.today() + datetime.timedelta(days=2)
			threeDay = datetime.date.today() + datetime.timedelta(days=3)
			fourDay = datetime.date.today() + datetime.timedelta(days=4)
			fiveDay = datetime.date.today() + datetime.timedelta(days=5)
			sixDay = datetime.date.today() + datetime.timedelta(days=6)
			sevenDay = datetime.date.today() + datetime.timedelta(days=7)

			todaysWordDate = today.strftime("%B %d, %Y")
			oneDayWordDate = oneDay.strftime("%B %d, %Y")
			twoDayWordDate = twoDay.strftime("%B %d, %Y")
			threeDayWordDate = threeDay.strftime("%B %d, %Y")
			fourDayWordDate = fourDay.strftime("%B %d, %Y")
			fiveDayWordDate = fiveDay.strftime("%B %d, %Y")
			sixDayWordDate = sixDay.strftime("%B %d, %Y")
			sevenDayWordDate = sevenDay.strftime("%B %d, %Y")

			if (currentDateSelected == oneDayWordDate):
				date_label.config(text=todaysWordDate)
				previous_date_button.place_forget()
			if (currentDateSelected == twoDayWordDate):
				date_label.config(text=oneDayWordDate)
			if (currentDateSelected == threeDayWordDate):
				date_label.config(text=twoDayWordDate)
			if (currentDateSelected == fourDayWordDate):
				date_label.config(text=threeDayWordDate)
			if (currentDateSelected == fiveDayWordDate):
				date_label.config(text=fourDayWordDate)
			if (currentDateSelected == sixDayWordDate):
				date_label.config(text=fiveDayWordDate)
			if (currentDateSelected == sevenDayWordDate):
				date_label.config(text=sixDayWordDate)
				next_date_button.place(rely=0.643, relx=0.535, anchor='center')


		def dateSelectionRight():
			currentDateSelected = date_label.cget("text")

			today = datetime.date.today()
			oneDay = datetime.date.today() + datetime.timedelta(days=1)
			twoDay = datetime.date.today() + datetime.timedelta(days=2)
			threeDay = datetime.date.today() + datetime.timedelta(days=3)
			fourDay = datetime.date.today() + datetime.timedelta(days=4)
			fiveDay = datetime.date.today() + datetime.timedelta(days=5)
			sixDay = datetime.date.today() + datetime.timedelta(days=6)
			sevenDay = datetime.date.today() + datetime.timedelta(days=7)

			todaysWordDate = today.strftime("%B %d, %Y")
			oneDayWordDate = oneDay.strftime("%B %d, %Y")
			twoDayWordDate = twoDay.strftime("%B %d, %Y")
			threeDayWordDate = threeDay.strftime("%B %d, %Y")
			fourDayWordDate = fourDay.strftime("%B %d, %Y")
			fiveDayWordDate = fiveDay.strftime("%B %d, %Y")
			sixDayWordDate = sixDay.strftime("%B %d, %Y")
			sevenDayWordDate = sevenDay.strftime("%B %d, %Y")

			if (currentDateSelected == todaysWordDate):
				date_label.config(text=oneDayWordDate)
				previous_date_button.place(rely=0.643, relx=0.085, anchor='center')
			if (currentDateSelected == oneDayWordDate):
				date_label.config(text=twoDayWordDate)
			if (currentDateSelected == twoDayWordDate):
				date_label.config(text=threeDayWordDate)
			if (currentDateSelected == threeDayWordDate):
				date_label.config(text=fourDayWordDate)
			if (currentDateSelected == fourDayWordDate):
				date_label.config(text=fiveDayWordDate)
			if (currentDateSelected == fiveDayWordDate):
				date_label.config(text=sixDayWordDate)
			if (currentDateSelected == sixDayWordDate):
				date_label.config(text=sevenDayWordDate)
				next_date_button.place_forget()


		def firstTime():
			pass


		def AutoFillButton():
			conn = sqlite3.connect('BadmintonClub.db')
			c = conn.cursor()

			isValid = True
			isValid = isValid and validate_time(time.get(), "Time", title_label)
			isValid = isValid and validate_court(court.get(), "Court", title_label)

			if isValid:
				if (time.get() ==1):
					final_time = '9-10am'
				if (time.get() ==2):
					final_time = '10-11am'
				if (time.get() ==3):
					final_time = '11-12am'
				if (time.get() ==4):
					final_time = '12-1pm'
				if (time.get() ==5):
					final_time = '1-2pm'
				if (time.get() ==6):
					final_time = '2-3pm'
				if (time.get() ==7):
					final_time = '3-4pm'
				if (time.get() ==8):
					final_time = '4-5pm'
				if (time.get() ==9):
					final_time = '5-6pm'
				if (time.get() ==10):
					final_time = '6-7pm'
				if (time.get() ==11):
					final_time = '7-8pm'
				if (time.get() ==12):
					final_time = '8-9pm'
				if (time.get() ==13):
					final_time = '9-10pm'
				if (time.get() ==14):
					final_time = '10-11pm'

				if (court.get() ==1):
					final_court = '1'
				if (court.get() ==2):
					final_court = '2'
				if (court.get() ==3):
					final_court = '3'
				if (court.get() ==4):
					final_court = '4'
				if (court.get() ==5):
					final_court = '5'
				if (court.get() ==6):
					final_court = '6'
				if (court.get() ==7):
					final_court = '7'
				if (court.get() ==8):
					final_court = '8'
				if (court.get() ==9):
					final_court = '9'
				if (court.get() ==10):
					final_court = '10'
				if (court.get() ==11):
					final_court = '11'
				if (court.get() ==12):
					final_court = '12'

				currentDateSelected = date_label.cget("text")

				response = askyesno("Are you sure?", "Are you sure that the details selected are correct?")
				if response == False:
					returnColour(title_label)
					showinfo("Info", "submition cancelled")

				else:
					c.execute("SELECT * FROM booking")
					booking_array = c.fetchall()

					newId = len(booking_array) + 1

					c.execute("INSERT INTO booking VALUES(?, ?, ?, ?, ?, ?)", (
						"","",currentDateSelected,final_time,final_court,newId

					))

					messagebox.showinfo("info", "User's has been successfully stored for the competition")

				today = datetime.date.today()
				todaysWordDate = today.strftime("%B %d, %Y")
				date_label.config(text=todaysWordDate)
				time.set("1")
				court.set("1")

				returnColour(title_label)

			conn.commit()
			conn.close()

			treeviewPopulate()


		def confirmBooking():
			conn = sqlite3.connect('BadmintonClub.db')
			c = conn.cursor()

			isValid = True
			isValid = isValid and validate_member(self.memberNamesAndPasswords.get(), "Member 1", member_label)
			isValid = isValid and validate_member(self.memberNamesAndPasswords2.get(), "Member 2", member2_label)

			if isValid:
				finalMember = self.memberNamesAndPasswords.get()
				finalMember2 = self.memberNamesAndPasswords2.get()

				response = askyesno("Are you sure?", "Are you sure that the members selected are correct?")
				if response == False:
					returnColour2(member_label, member2_label)
					showinfo("Info", "submition cancelled")

				else:
					response2 = askyesno("Are you sure?", "These new members will update the latest booking added, is this okay?")
					if response2 == False:
						returnColour2(member_label, member2_label)
						showinfo("Info", "submition cancelled")

					else:

						c.execute("SELECT * FROM booking")
						competition_array = c.fetchall()

						BookingID = len(competition_array)

						c.execute("""UPDATE booking SET username = :username WHERE bookingID=:bookingID""", {
							"username": finalMember,
							"bookingID": BookingID
						})

						c.execute("""UPDATE booking SET username2 = :username2 WHERE bookingID=:bookingID""", {
							"username2": finalMember2,
							"bookingID": BookingID
						})

					returnColour2(member_label, member2_label)
					messagebox.showinfo("info", "Booking has been completed")

			conn.commit()
			conn.close()

			treeviewPopulate()



		time=IntVar()
		court=IntVar()



		line1 = Canvas(self.booking, width=3, height=190)
		line1.config(bg='black')
		line1.create_line(3, 0, 200, 100000)
		line1.place(rely=0.86, relx=0.566, anchor='center')

		background_entry_canvas = Canvas(self.booking,width=900, height=400, bg = "white")
		background_entry_canvas.place(rely=0.41,relx=0.5,anchor=CENTER)

		background_entry_image = PhotoImage(file ="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images/Images/BookingTable.png")

		background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
		background_entry_canvas.background_entry_image = background_entry_image


		title_label = tkinter.Label(self.booking, text="Member Booking Table", font=('Tahoma', 21, 'bold', 'underline'), fg='black', bg='white')
		title_label.place(rely=0.16, relx=0.5, anchor='center')

		firstTimeButton = Radiobutton(self.booking, text="9-10am", cursor="tcross", variable=time, value=1, fg='black', bg='white', bd=5, relief='sunken', font=('Tahoma', 8, 'bold'), padx=10, pady=5)
		firstTimeButton.place(rely=0.26, relx=0.13, anchor='center')

		secondTimeButton = Radiobutton(self.booking, text="10-11am", cursor="tcross", variable=time, value=2, fg='black', bg='white', bd=5, relief='sunken', font=('Tahoma', 8, 'bold'), padx=10, pady=5)
		secondTimeButton.place(rely=0.26, relx=0.25, anchor='center')

		thirdTimeButton = Radiobutton(self.booking, text="11-12am", cursor="tcross", variable=time, value=3, fg='black', bg='white', bd=5, relief='sunken', font=('Tahoma', 8, 'bold'), padx=10, pady=5)
		thirdTimeButton.place(rely=0.26, relx=0.37, anchor='center')

		fourthTimeButton = Radiobutton(self.booking, text="12-1pm", cursor="tcross", variable=time, value=4, fg='black', bg='white', bd=5, relief='sunken', font=('Tahoma', 8, 'bold'), padx=10, pady=5)
		fourthTimeButton.place(rely=0.26, relx=0.49, anchor='center')

		fifthTimeButton = Radiobutton(self.booking, text="1-2pm", cursor="tcross", variable=time, value=5, fg='black', bg='white', bd=5, relief='sunken', font=('Tahoma', 8, 'bold'), padx=10, pady=5)
		fifthTimeButton.place(rely=0.35, relx=0.13, anchor='center')

		sixthTimeButton = Radiobutton(self.booking, text="2-3pm", cursor="tcross", variable=time, value=6, fg='black', bg='white', bd=5, relief='sunken', font=('Tahoma', 8, 'bold'), padx=10, pady=5)
		sixthTimeButton.place(rely=0.35, relx=0.25, anchor='center')

		seventhTimeButton = Radiobutton(self.booking, text="3-4pm", cursor="tcross", variable=time, value=7, fg='black', bg='white', bd=5, relief='sunken', font=('Tahoma', 8, 'bold'), padx=10, pady=5)
		seventhTimeButton.place(rely=0.35, relx=0.37, anchor='center')

		eigthTimeButton = Radiobutton(self.booking, text="4-5pm", cursor="tcross", variable=time, value=8, fg='black', bg='white', bd=5, relief='sunken', font=('Tahoma', 8, 'bold'), padx=10, pady=5)
		eigthTimeButton.place(rely=0.35, relx=0.49, anchor='center')

		ninthTimeButton = Radiobutton(self.booking, text="5-6pm", cursor="tcross", variable=time, value=9, fg='black', bg='white', bd=5, relief='sunken', font=('Tahoma', 8, 'bold'), padx=10, pady=5)
		ninthTimeButton.place(rely=0.44, relx=0.13, anchor='center')

		tenthTimeButton = Radiobutton(self.booking, text="6-7pm", cursor="tcross", variable=time, value=10, fg='black', bg='white', bd=5, relief='sunken', font=('Tahoma', 8, 'bold'), padx=10, pady=5)
		tenthTimeButton.place(rely=0.44, relx=0.25, anchor='center')

		eleventhTimeButton = Radiobutton(self.booking, text="7-8pm", cursor="tcross", variable=time, value=11, fg='black', bg='white', bd=5, relief='sunken', font=('Tahoma', 8, 'bold'), padx=10, pady=5)
		eleventhTimeButton.place(rely=0.44, relx=0.37, anchor='center')

		twelthTimeButton = Radiobutton(self.booking, text="8-9pm", cursor="tcross", variable=time, value=12, fg='black', bg='white', bd=5, relief='sunken', font=('Tahoma', 8, 'bold'), padx=10, pady=5)
		twelthTimeButton.place(rely=0.44, relx=0.49, anchor='center')

		thirteenthTimeButton = Radiobutton(self.booking, text="9-10pm", cursor="tcross", variable=time, value=13, fg='black', bg='white', bd=5, relief='sunken', font=('Tahoma', 8, 'bold'), padx=10, pady=5)
		thirteenthTimeButton.place(rely=0.52, relx=0.25, anchor='center')

		fourteenthTimeButton = Radiobutton(self.booking, text="10-11pm", cursor="tcross", variable=time, value=14, fg='black', bg='white', bd=5, relief='sunken', font=('Tahoma', 8, 'bold'), padx=10, pady=5)
		fourteenthTimeButton.place(rely=0.52, relx=0.37, anchor='center')
		time.set("1")


		firstCourtButton = Radiobutton(self.booking, text="Court 1", cursor="tcross", variable=court, value=1, fg='black', bg='white', bd=5, relief='sunken', font=('Tahoma', 8, 'bold'), padx=10, pady=5)
		firstCourtButton.place(rely=0.26, relx=0.635, anchor='center')

		secondCourtButton = Radiobutton(self.booking, text="Court 2", cursor="tcross", variable=court, value=2, fg='black', bg='white', bd=5, relief='sunken', font=('Tahoma', 8, 'bold'), padx=10, pady=5)
		secondCourtButton.place(rely=0.26, relx=0.755, anchor='center')

		thirdCourtButton = Radiobutton(self.booking, text="Court 3", cursor="tcross", variable=court, value=3, fg='black', bg='white', bd=5, relief='sunken', font=('Tahoma', 8, 'bold'), padx=10, pady=5)
		thirdCourtButton.place(rely=0.26, relx=0.875, anchor='center')

		fourthCourtButton = Radiobutton(self.booking, text="Court 4", cursor="tcross", variable=court, value=4, fg='black', bg='white', bd=5, relief='sunken', font=('Tahoma', 8, 'bold'), padx=10, pady=5)
		fourthCourtButton.place(rely=0.35, relx=0.635, anchor='center')

		fifthCourtButton = Radiobutton(self.booking, text="Court 5", cursor="tcross", variable=court, value=5, fg='black', bg='white', bd=5, relief='sunken', font=('Tahoma', 8, 'bold'), padx=10, pady=5)
		fifthCourtButton.place(rely=0.35, relx=0.755, anchor='center')

		sixthCourtButton = Radiobutton(self.booking, text="Court 6", cursor="tcross", variable=court, value=6, fg='black', bg='white', bd=5, relief='sunken', font=('Tahoma', 8, 'bold'), padx=10, pady=5)
		sixthCourtButton.place(rely=0.35, relx=0.875, anchor='center')

		seventhCourtButton = Radiobutton(self.booking, text="Court 7", cursor="tcross", variable=court, value=7, fg='black', bg='white', bd=5, relief='sunken', font=('Tahoma', 8, 'bold'), padx=10, pady=5)
		seventhCourtButton.place(rely=0.44, relx=0.635, anchor='center')

		eigthCourtButton = Radiobutton(self.booking, text="Court 8", cursor="tcross", variable=court, value=8, fg='black', bg='white', bd=5, relief='sunken', font=('Tahoma', 8, 'bold'), padx=10, pady=5)
		eigthCourtButton.place(rely=0.44, relx=0.755, anchor='center')

		ninthCourtButton = Radiobutton(self.booking, text="Court 9", cursor="tcross", variable=court, value=9, fg='black', bg='white', bd=5, relief='sunken', font=('Tahoma', 8, 'bold'), padx=10, pady=5)
		ninthCourtButton.place(rely=0.44, relx=0.875, anchor='center')

		tenthCourtButton = Radiobutton(self.booking, text="Court 10", cursor="tcross", variable=court, value=10, fg='black', bg='white', bd=5, relief='sunken', font=('Tahoma', 8, 'bold'), padx=10, pady=5)
		tenthCourtButton.place(rely=0.53, relx=0.635, anchor='center')

		eleventhCourtButton = Radiobutton(self.booking, text="Court 11", cursor="tcross", variable=court, value=11, fg='black', bg='white', bd=5, relief='sunken', font=('Tahoma', 8, 'bold'), padx=10, pady=5)
		eleventhCourtButton.place(rely=0.53, relx=0.755, anchor='center')

		twelthCourtButton = Radiobutton(self.booking, text="Court 12", cursor="tcross", variable=court, value=12, fg='black', bg='white', bd=5, relief='sunken', font=('Tahoma', 8, 'bold'), padx=10, pady=5)
		twelthCourtButton.place(rely=0.53, relx=0.875, anchor='center')
		court.set("1")


		today = datetime.date.today()
		todaysWordDate = today.strftime("%B %d, %Y")
		date_label = tk.Label(self.booking, text=todaysWordDate, font=('Tahoma', 20, 'bold'), fg='black', bg='white')
		date_label.place(rely=0.64, relx=0.313, anchor='center')


		left_date_photo = PhotoImage(file="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images/Images/ArrowLeft.png")
		previous_date_button = Button(self.booking, image=left_date_photo, command=dateSelectionleft, borderwidth=0, cursor="tcross")
		previous_date_button.image = left_date_photo
		previous_date_button.place(rely=0.643, relx=0.085, anchor='center')
		previous_date_button.place_forget()

		right_date_photo = PhotoImage(file="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images/Images/ArrowRight.png")
		next_date_button = Button(self.booking, image=right_date_photo, command=dateSelectionRight, borderwidth=0, cursor="tcross")
		next_date_button.image = right_date_photo
		next_date_button.place(rely=0.643, relx=0.535, anchor='center')


		autofill_booking_button = tkinter.Button(self.booking, cursor="tcross",text="Auto-Fill Booking", command=AutoFillButton, fg='black', bg='white', bd=5, relief='ridge', font=('Tahoma', 14, 'bold'), padx=25, pady=3)
		autofill_booking_button.place(rely=0.64, relx=0.755, anchor='center')


		member_label = tkinter.Label(self.booking, text="Member 1:", font=('Tahoma', 15, 'bold'), fg='black', bg='white')
		member_label.place(rely=0.775, relx=0.66, anchor='center')

		member2_label = tkinter.Label(self.booking, text="Member 2:", font=('Tahoma', 15, 'bold'), fg='black', bg='white')
		member2_label.place(rely=0.845, relx=0.66, anchor='center')


		booking_submit_button = tkinter.Button(self.booking, cursor="tcross",text="Confirm Booking", command=confirmBooking, fg='white', bg='black', bd=5, relief='ridge', font=('Tahoma', 14, 'bold'), padx=15)
		booking_submit_button.place(rely=0.94, relx=0.755, anchor='center')


		booking_TV=ttk.Treeview(self.booking,height=7,columns=('Member2','Date','Time','Court'))
		booking_TV.place(relx=0.278,rely=0.86, anchor=CENTER)

		booking_TV.heading("#0",text='Member1')
		booking_TV.column("#0",minwidth=0,width=155)
		booking_TV.heading("#1",text='Member2')
		booking_TV.column("#1",minwidth=0,width=155)
		booking_TV.heading("#2",text='Date')
		booking_TV.column("#2",minwidth=0,width=125)
		booking_TV.heading("#3",text='Time')
		booking_TV.column("#3",minwidth=0,width=55)
		booking_TV.heading("#4",text='Court')
		booking_TV.column("#4",minwidth=0,width=40)

		booking_ysearch_scrollbar = Scrollbar(self.booking, orient = 'vertical', command = booking_TV.yview, cursor="tcross")
		booking_ysearch_scrollbar.place(relx=0.554,rely=0.861,anchor='center',height=168)
		booking_TV.configure(yscrollcommand=booking_ysearch_scrollbar.set)


		treeviewPopulate()



	def memberSelection(self):
		self.memberNamesAndPasswords = StringVar()
		self.memberNamesAndPasswords2 = StringVar()

		member_name_choices = self.get_member_details()
		if (len(member_name_choices) > 0) :
			member_selection_dropdown = OptionMenu(self.booking, self.memberNamesAndPasswords, *member_name_choices)
			member_selection_dropdown.place(rely=0.779, relx=0.84, anchor='center')

			member2_selection_dropdown = OptionMenu(self.booking, self.memberNamesAndPasswords2, *member_name_choices)
			member2_selection_dropdown.place(rely=0.849, relx=0.84, anchor='center')


	def get_member_details(self):
		conn = sqlite3.connect('BadmintonClub.db')
		c = conn.cursor()

		member_name_list = []

		c.execute("SELECT * From member")
		items = c.fetchall()

		for row in items:
			if row == []:
				pass
			else:
				member_name = row[0]
				member_name_list.append(member_name)

		conn.commit()
		conn.close()

		return member_name_list