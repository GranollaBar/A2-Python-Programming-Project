from tkinter import ttk
from tkinter import messagebox
import tkinter.simpledialog
from tkinter.messagebox import showinfo
from tkinter.messagebox import askyesno
import sqlite3
from tkinter import simpledialog
from tkinter import *
from functools import partial
import datetime
from tkcalendar import Calendar

MemberCounter=0

class CoachingSessionContent:

	def __init__(self, mainScreen):
		self.coachSession = mainScreen
		self.conn = sqlite3.connect('CoachDetails.db')
		self.c = self.conn.cursor()


		# self.c.execute("""CREATE TABLE coachSession (
		# 			username text,
		# 			startTime text,
		# 			endTime text,
		# 			date text,
		# 			courts text,
		# 			groups text,
		# 			people text,
		# 			technique text
		# 			)""")


	def generateCoachSessionContnt(self):


		def courtsRequired():
			if (court1.get() ==1):
				court1.set('1')
			if (court2.get() ==1):
				court2.set('1')
			if (court3.get() ==1):
				court3.set('1')
			if (court4.get() ==1):
				court4.set('1')
			if (court5.get() ==1):
				court5.set('1')
			if (court6.get() ==1):
				court6.set('1')
			if (court7.get() ==1):
				court7.set('1')
			if (court8.get() ==1):
				court8.set('1')
			if (court9.get() ==1):
				court9.set('1')
			if (court10.get() ==1):
				court10.set('1')
			if (court11.get() ==1):
				court11.set('1')
			if (court12.get() ==1):
				court12.set('1')

			courts = Toplevel(self.coachSession, bg="white")
			courts.geometry('500x500')

			title_label = tkinter.Label(courts, text="Check the No. Courts Needed For The Session", font=('Tahoma', 16, 'underline', 'bold'), fg='black', bg='white')
			title_label.place(rely=0.03, relx=0.5, anchor='center')

			confirm_button = tkinter.Button(courts, text="Confirm Selection", command=lambda : confirmSelection(courts), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 10, 'bold'), padx=35, cursor="tcross")
			confirm_button.place(rely=0.112, relx=0.5, anchor='center')

			all_button = tkinter.Button(courts, text="Select All", command=lambda : addAllCourts(court1, court2, court3, court4, court5, court6, court7, court8, court9, court10, court11, court12), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 8, 'bold'), padx=10, cursor="tcross")
			all_button.place(rely=0.112, relx=0.15, anchor='center')

			clear_button = tkinter.Button(courts, text="Clear All", command=lambda : clearAllCourts(court1, court2, court3, court4, court5, court6, court7, court8, court9, court10, court11, court12), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 8, 'bold'), padx=10, cursor="tcross")
			clear_button.place(rely=0.112, relx=0.85, anchor='center')


			confirm_court1 = Checkbutton(courts, cursor="tcross",text="Court 1  V", variable=court1,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_court1.place(rely=0.2, relx=0.15, anchor='center')

			confirm_court2 = Checkbutton(courts, cursor="tcross",text="Court 2  V", variable=court2,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_court2.place(rely=0.4, relx=0.15, anchor='center')

			confirm_court3 = Checkbutton(courts, cursor="tcross",text="Court 3  V", variable=court3,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_court3.place(rely=0.6, relx=0.15, anchor='center')

			confirm_court4 = Checkbutton(courts, cursor="tcross",text="Court 4  V", variable=court4,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_court4.place(rely=0.8, relx=0.15, anchor='center')

			confirm_court5 = Checkbutton(courts, cursor="tcross",text="Court 5  V", variable=court5,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_court5.place(rely=0.2, relx=0.5, anchor='center')

			confirm_court6 = Checkbutton(courts, cursor="tcross",text="Court 6  V", variable=court6,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_court6.place(rely=0.4, relx=0.5, anchor='center')

			confirm_court7 = Checkbutton(courts, cursor="tcross",text="Court 7  V", variable=court7,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_court7.place(rely=0.6, relx=0.5, anchor='center')

			confirm_court8 = Checkbutton(courts, cursor="tcross",text="Court 8  V", variable=court8,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_court8.place(rely=0.8, relx=0.5, anchor='center')

			confirm_court9 = Checkbutton(courts, cursor="tcross",text="Court 9  V", variable=court9,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_court9.place(rely=0.2, relx=0.85, anchor='center')

			confirm_court10 = Checkbutton(courts, cursor="tcross",text="Court 10  V", variable=court10,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_court10.place(rely=0.4, relx=0.85, anchor='center')

			confirm_court11 = Checkbutton(courts, cursor="tcross",text="Court 11 V", variable=court11,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_court11.place(rely=0.6, relx=0.85, anchor='center')

			confirm_court12 = Checkbutton(courts, cursor="tcross",text="Court 12 V", variable=court12,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_court12.place(rely=0.8, relx=0.85, anchor='center')


			background_entry_canvas = Canvas(courts,width=100, height=58, bg = "white")
			background_entry_canvas.place(rely=0.3,relx=0.15,anchor=CENTER)

			background_entry_image = PhotoImage(file ="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images/Images/courts.png")

			background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
			background_entry_canvas.background_entry_image = background_entry_image


			background_entry_canvas = Canvas(courts,width=100, height=58, bg = "white")
			background_entry_canvas.place(rely=0.5,relx=0.15,anchor=CENTER)

			background_entry_image = PhotoImage(file ="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images/Images/courts.png")

			background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
			background_entry_canvas.background_entry_image = background_entry_image


			background_entry_canvas = Canvas(courts,width=100, height=58, bg = "white")
			background_entry_canvas.place(rely=0.7,relx=0.15,anchor=CENTER)

			background_entry_image = PhotoImage(file ="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images/Images/courts.png")

			background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
			background_entry_canvas.background_entry_image = background_entry_image


			background_entry_canvas = Canvas(courts,width=100, height=58, bg = "white")
			background_entry_canvas.place(rely=0.9,relx=0.15,anchor=CENTER)

			background_entry_image = PhotoImage(file ="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images/Images/courts.png")

			background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
			background_entry_canvas.background_entry_image = background_entry_image


			background_entry_canvas = Canvas(courts,width=100, height=58, bg = "white")
			background_entry_canvas.place(rely=0.3,relx=0.5,anchor=CENTER)

			background_entry_image = PhotoImage(file ="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images/Images/courts.png")

			background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
			background_entry_canvas.background_entry_image = background_entry_image


			background_entry_canvas = Canvas(courts,width=100, height=58, bg = "white")
			background_entry_canvas.place(rely=0.5,relx=0.5,anchor=CENTER)

			background_entry_image = PhotoImage(file ="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images/Images/courts.png")

			background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
			background_entry_canvas.background_entry_image = background_entry_image


			background_entry_canvas = Canvas(courts,width=100, height=58, bg = "white")
			background_entry_canvas.place(rely=0.7,relx=0.5,anchor=CENTER)

			background_entry_image = PhotoImage(file ="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images/Images/courts.png")

			background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
			background_entry_canvas.background_entry_image = background_entry_image


			background_entry_canvas = Canvas(courts,width=100, height=58, bg = "white")
			background_entry_canvas.place(rely=0.9,relx=0.5,anchor=CENTER)

			background_entry_image = PhotoImage(file ="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images/Images/courts.png")

			background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
			background_entry_canvas.background_entry_image = background_entry_image


			background_entry_canvas = Canvas(courts,width=100, height=58, bg = "white")
			background_entry_canvas.place(rely=0.3,relx=0.85,anchor=CENTER)

			background_entry_image = PhotoImage(file ="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images/Images/courts.png")

			background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
			background_entry_canvas.background_entry_image = background_entry_image


			background_entry_canvas = Canvas(courts,width=100, height=58, bg = "white")
			background_entry_canvas.place(rely=0.5,relx=0.85,anchor=CENTER)

			background_entry_image = PhotoImage(file ="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images/Images/courts.png")

			background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
			background_entry_canvas.background_entry_image = background_entry_image


			background_entry_canvas = Canvas(courts,width=100, height=58, bg = "white")
			background_entry_canvas.place(rely=0.7,relx=0.85,anchor=CENTER)

			background_entry_image = PhotoImage(file ="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images/Images/courts.png")

			background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
			background_entry_canvas.background_entry_image = background_entry_image


			background_entry_canvas = Canvas(courts,width=100, height=58, bg = "white")
			background_entry_canvas.place(rely=0.9,relx=0.85,anchor=CENTER)

			background_entry_image = PhotoImage(file ="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images/Images/courts.png")

			background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
			background_entry_canvas.background_entry_image = background_entry_image



		def confirmSelection(frame):
			frame.withdraw()


		def groupsRequired():
			if (group1.get() ==1):
				group1.set('1')
			if (group2.get() ==1):
				group2.set('1')
			if (group3.get() ==1):
				group3.set('1')
			if (group4.get() ==1):
				group4.set('1')
			if (group5.get() ==1):
				group5.set('1')
			if (group6.get() ==1):
				group6.set('1')
			if (group7.get() ==1):
				group7.set('1')
			if (group8.get() ==1):
				group8.set('1')
			if (group9.get() ==1):
				group9.set('1')
			if (group10.get() ==1):
				group10.set('1')
			if (group11.get() ==1):
				group11.set('1')
			if (group12.get() ==1):
				group12.set('1')
			if (group13.get() ==1):
				group13.set('1')
			if (group14.get() ==1):
				group14.set('1')
			if (group15.get() ==1):
				group15.set('1')
			if (group16.get() ==1):
				group16.set('1')
			if (group17.get() ==1):
				group17.set('1')
			if (group18.get() ==1):
				group18.set('1')
			if (group19.get() ==1):
				group19.set('1')
			if (group20.get() ==1):
				group20.set('1')

			groups = Toplevel(self.coachSession, bg="white")
			groups.geometry('450x350')

			title_label = tkinter.Label(groups, text="Check the No. Groups Needed For The Session", font=('Tahoma', 13, 'underline', 'bold'), fg='black', bg='white')
			title_label.place(rely=0.03, relx=0.5, anchor='center')

			confirm_button = tkinter.Button(groups, text="Confirm Selection", command=lambda : confirmSelection2(groups), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 9, 'bold'), padx=35, cursor="tcross")
			confirm_button.place(rely=0.15, relx=0.5, anchor='center')

			all_button = tkinter.Button(groups, text="Select All", command=lambda : addAllGroups(group1, group2, group3, group4, group5, group6, group7, group8, group9, group10, group11, group12, group13, group14, group15, group16, group17, group18, group19, group20), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 8, 'bold'), padx=10, cursor="tcross")
			all_button.place(rely=0.15, relx=0.15, anchor='center')

			clear_button = tkinter.Button(groups, text="Clear All", command=lambda : clearAllGroups(group1, group2, group3, group4, group5, group6, group7, group8, group9, group10, group11, group12, group13, group14, group15, group16, group17, group18, group19, group20), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 8, 'bold'), padx=10, cursor="tcross")
			clear_button.place(rely=0.15, relx=0.85, anchor='center')


			confirm_group1 = Checkbutton(groups, cursor="tcross",text="Group 1", variable=group1,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_group1.place(rely=0.3, relx=0.15, anchor='center')

			confirm_group2 = Checkbutton(groups, cursor="tcross",text="Group 2", variable=group2,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_group2.place(rely=0.3, relx=0.38, anchor='center')

			confirm_group3 = Checkbutton(groups, cursor="tcross",text="Group 3", variable=group3,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_group3.place(rely=0.3, relx=0.61, anchor='center')

			confirm_group4 = Checkbutton(groups, cursor="tcross",text="Group 4", variable=group4,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_group4.place(rely=0.3, relx=0.84, anchor='center')

			confirm_group5 = Checkbutton(groups, cursor="tcross",text="Group 5", variable=group5,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_group5.place(rely=0.45, relx=0.15, anchor='center')

			confirm_group6 = Checkbutton(groups, cursor="tcross",text="Group 6", variable=group6,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_group6.place(rely=0.45, relx=0.38, anchor='center')

			confirm_group7 = Checkbutton(groups, cursor="tcross",text="Group 7", variable=group7,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_group7.place(rely=0.45, relx=0.61, anchor='center')

			confirm_group8 = Checkbutton(groups, cursor="tcross",text="Group 8", variable=group8,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_group8.place(rely=0.45, relx=0.84, anchor='center')

			confirm_group9 = Checkbutton(groups, cursor="tcross",text="Group 9", variable=group9,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_group9.place(rely=0.6, relx=0.15, anchor='center')

			confirm_group10 = Checkbutton(groups, cursor="tcross",text="Group 10", variable=group10,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_group10.place(rely=0.6, relx=0.38, anchor='center')

			confirm_group11 = Checkbutton(groups, cursor="tcross",text="Group 11", variable=group11,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_group11.place(rely=0.6, relx=0.61, anchor='center')

			confirm_group12 = Checkbutton(groups, cursor="tcross",text="Group 12", variable=group12,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_group12.place(rely=0.6, relx=0.84, anchor='center')

			confirm_group13 = Checkbutton(groups, cursor="tcross",text="Group 13", variable=group13,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_group13.place(rely=0.75, relx=0.15, anchor='center')

			confirm_group14 = Checkbutton(groups, cursor="tcross",text="Group 14", variable=group14,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_group14.place(rely=0.75, relx=0.38, anchor='center')

			confirm_group15 = Checkbutton(groups, cursor="tcross",text="Group 15", variable=group15,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_group15.place(rely=0.75, relx=0.61, anchor='center')

			confirm_group16 = Checkbutton(groups, cursor="tcross",text="Group 16", variable=group16,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_group16.place(rely=0.75, relx=0.84, anchor='center')

			confirm_group17 = Checkbutton(groups, cursor="tcross",text="Group 17", variable=group17,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_group17.place(rely=0.9, relx=0.15, anchor='center')

			confirm_group18 = Checkbutton(groups, cursor="tcross",text="Group 18", variable=group18,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_group18.place(rely=0.9, relx=0.38, anchor='center')

			confirm_group19 = Checkbutton(groups, cursor="tcross",text="Group 19", variable=group19,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_group19.place(rely=0.9, relx=0.61, anchor='center')

			confirm_group20 = Checkbutton(groups, cursor="tcross",text="Group 20", variable=group20,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_group20.place(rely=0.9, relx=0.84, anchor='center')


		def confirmSelection2(frame):
			frame.withdraw()


		def addAllCourts(value1, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11, value12):
			value1.set("1")
			value2.set("1")
			value3.set("1")
			value4.set("1")
			value5.set("1")
			value6.set("1")
			value7.set("1")
			value8.set("1")
			value9.set("1")
			value10.set("1")
			value11.set("1")
			value12.set("1")


		def clearAllCourts(value1, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11, value12):
			value1.set("0")
			value2.set("0")
			value3.set("0")
			value4.set("0")
			value5.set("0")
			value6.set("0")
			value7.set("0")
			value8.set("0")
			value9.set("0")
			value10.set("0")
			value11.set("0")
			value12.set("0")


		def addAllGroups(value1, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11, value12, value13, value14, value15, value16, value17, value18, value19, value20):
			value1.set("1")
			value2.set("1")
			value3.set("1")
			value4.set("1")
			value5.set("1")
			value6.set("1")
			value7.set("1")
			value8.set("1")
			value9.set("1")
			value10.set("1")
			value11.set("1")
			value12.set("1")
			value13.set("1")
			value14.set("1")
			value15.set("1")
			value16.set("1")
			value17.set("1")
			value18.set("1")
			value19.set("1")
			value20.set("1")


		def clearAllGroups(value1, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11, value12, value13, value14, value15, value16, value17, value18, value19, value20):
			value1.set("0")
			value2.set("0")
			value3.set("0")
			value4.set("0")
			value5.set("0")
			value6.set("0")
			value7.set("0")
			value8.set("0")
			value9.set("0")
			value10.set("0")
			value11.set("0")
			value12.set("0")
			value13.set("0")
			value14.set("0")
			value15.set("0")
			value16.set("0")
			value17.set("0")
			value18.set("0")
			value19.set("0")
			value20.set("0")


		def validate_username(value, fieldname, label):
			if (value == ''):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " Can Not Be empty")
				return False

			label.config(fg="SpringGreen3")
			return True


		def validate_start_time(value, value2, fieldname, label):
			if (float(value) <8.00):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " Can Not Be before 8am")
				return False
			if (float(value) >22.00):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " Can Not Be past 10pm")
				return False
			if (float(value) >= float(value2)):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " Can Not Be higher than the end time")
				return False

			label.config(fg="SpringGreen3")
			return True


		def validate_end_time(value, fieldname, label):
			if (float(value) <9.00):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " Can Not Be before 9am")
				return False
			if (float(value) >23.00):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " Can Not Be past 11pm")
				return False

			label.config(fg="SpringGreen3")
			return True


		def validate_date(value, fieldname, label):
			presentDate = datetime.datetime.now()
			date_formated = presentDate.strftime("%d/%m/%Y")

			d1 = datetime.datetime.strptime(value, "%d/%m/%Y").date()
			d2 = datetime.datetime.strptime(str(date_formated), "%d/%m/%Y").date()

			if d2>d1:
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " Can Not Be before the current date")
				return False

			label.config(fg="SpringGreen3")
			return True


		def validate_courts(value, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11, value12, fieldname, label):
			if (value ==0 and value2 ==0 and value3 ==0 and value4 ==0 and value5 ==0 and value6 ==0 and value7 ==0 and value8 ==0 and value9 ==0 and value10 ==0 and value11 ==0 and value12 ==0):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " must have at least 1 selected")
				return False

			label.config(fg="SpringGreen3")
			return True


		def validate_groups(value, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11, value12, value13, value14, value15, value16, value17, value18, value19, value20, fieldname, label):
			if (value ==0 and value2 ==0 and value3 ==0 and value4 ==0 and value5 ==0 and value6 ==0 and value7 ==0 and value8 ==0 and value9 ==0 and value10 ==0 and value11 ==0 and value12 ==0 and value13 ==0 and value14 ==0 and value15 ==0 and value16 ==0 and value17 ==0 and value18 ==0 and value19 ==0 and value20 ==0):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " must have at least 1 selected")
				return False

			label.config(fg="SpringGreen3")
			return True


		def validate_techniques(label):
			label.config(fg="SpringGreen3")
			return True


		def validate_new_start_time(value, value2, fieldname):
			if (float(value) <8.00):
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " Can Not Be before 8am")
				return False
			if (float(value) >22.00):
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " Can Not Be past 10pm")
				return False
			if (float(value) > float(value2)):
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " Can Not Be higher than the end time")
				return False

			return True


		def validate_new_end_time(value, fieldname):
			if (float(value) <9.00):
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " Can Not Be empty")
				return False
			if (float(value) >23.00):
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " Can Not Be empty")
				return False

			return True


		def validate_new_courts(value, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11, value12, fieldname):
			if (value ==0 and value2 ==0 and value3 ==0 and value4 ==0 and value5 ==0 and value6 ==0 and value7 ==0 and value8 ==0 and value9 ==0 and value10 ==0 and value11 ==0 and value12 ==0):
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " must have at least 1 selected")
				return False

			return True


		def validate_new_groups(value, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11, value12, value13, value14, value15, value16, value17, value18, value19, value20, fieldname):
			if (value ==0 and value2 ==0 and value3 ==0 and value4 ==0 and value5 ==0 and value6 ==0 and value7 ==0 and value8 ==0 and value9 ==0 and value10 ==0 and value11 ==0 and value12 ==0 and value13 ==0 and value14 ==0 and value15 ==0 and value16 ==0 and value17 ==0 and value18 ==0 and value19 ==0 and value20 ==0):
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " must have at least 1 selected")
				return False

			return True


		def validate_new_techniques(value, fieldname):
			if (value ==0):
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " must have at least 1 selected")
				return False

			return True


		def dateEntryCheck(dob):
			def assign_dob():
				eventDate.set(cal.get_date())
				top.withdraw()

			top = Toplevel(self.coachSession)

			cal = Calendar(top, font="Tahoma 16", date_pattern='dd/mm/yyyy',selectmode='day', cursor="tcross", year=2021, month=5, day=29)
			cal.pack(fill="both", expand=True)
			ttk.Button(top, text="ok", command=assign_dob).pack()


		def PeopleCounter():
			conn = sqlite3.connect('BadmintonClub.db')
			c = conn.cursor()

			c.execute("SELECT member_group From member")
			items = c.fetchall()

			if items =='':
				pass

			else:

				MemberCounter = 0
				if '1' in str(items) and group1.get() ==1:
					MemberCounter = MemberCounter + 1
				if '2' in str(items) and group2.get() ==1:
					MemberCounter = MemberCounter + 1
				if '3' in str(items) and group3.get() ==1:
					MemberCounter = MemberCounter + 1
				if '4' in str(items) and group4.get() ==1:
					MemberCounter = MemberCounter + 1
				if '5' in str(items) and group5.get() ==1:
					MemberCounter = MemberCounter + 1
				if '6' in str(items) and group6.get() ==1:
					MemberCounter = MemberCounter + 1
				if '7' in str(items) and group7.get() ==1:
					MemberCounter = MemberCounter + 1
				if '8' in str(items) and group8.get() ==1:
					MemberCounter = MemberCounter + 1
				if '9' in str(items) and group9.get() ==1:
					MemberCounter = MemberCounter + 1
				if '10' in str(items) and group10.get() ==1:
					MemberCounter = MemberCounter + 1
				if '11' in str(items) and group11.get() ==1:
					MemberCounter = MemberCounter + 1
				if '12' in str(items) and group12.get() ==1:
					MemberCounter = MemberCounter + 1
				if '13' in str(items) and group13.get() ==1:
					MemberCounter = MemberCounter + 1
				if '14' in str(items) and group14.get() ==1:
					MemberCounter = MemberCounter + 1
				if '15' in str(items) and group15.get() ==1:
					MemberCounter = MemberCounter + 1
				if '16' in str(items) and group16.get() ==1:
					MemberCounter = MemberCounter + 1
				if '17' in str(items) and group17.get() ==1:
					MemberCounter = MemberCounter + 1
				if '18' in str(items) and group18.get() ==1:
					MemberCounter = MemberCounter + 1
				if '19' in str(items) and group19.get() ==1:
					MemberCounter = MemberCounter + 1
				if '20' in str(items) and group20.get() ==1:
					MemberCounter = MemberCounter + 1

			conn.commit()
			conn.close()

			return MemberCounter

		def updateCoachSessionDate(newDate, frame):
			def new_assign_dob(username):
				conn = sqlite3.connect('CoachDetails.db')
				c = conn.cursor()

				newEventDate.set(newcal.get_date())
				top.withdraw()

				newCoachSessionDate = newEventDate.get()

				c.execute("""UPDATE coachSession SET date = :newDate WHERE username=:username""", {
					"newDate": str(newCoachSessionDate),
					"username": username
				})

				messagebox.showinfo("info", "The coach's session date is now " + newCoachSessionDate)

				conn.commit()
				conn.close()

				treeviewPopulate()

			conn = sqlite3.connect('CoachDetails.db')
			c = conn.cursor()

			frame.withdraw()

			coachUsername = simpledialog.askstring("info", "Enter the username of the coach you want to update")
			if coachUsername != '' and len(coachUsername) <25 and '@' in coachUsername and '.' in coachUsername:
				c.execute(f"SELECT * FROM coachSession WHERE username=?", (coachUsername,))
				data = c.fetchone()
				if not data:
					messagebox.showinfo("Warning", "The username entered was not found in the database", icon='error')

				else:

					top = Toplevel(self.coachSession)

					newcal = Calendar(top, font="Tahoma 16", selectmode='day', cursor="tcross", year=2021, month=5, day=29)
					newcal.pack(fill="both", expand=True)
					ttk.Button(top, text="Update", command= lambda : new_assign_dob(coachUsername)).pack()


		def clearTv():
			record=coachsession_search_Tv.get_children()
			for elements in record:
				coachsession_search_Tv.delete(elements)


		def treeviewPopulate():
			clearTv()

			conn = sqlite3.connect('CoachDetails.db')
			c = conn.cursor()

			c.execute("SELECT * From coachSession")
			items = c.fetchall()
			conn.commit()
			conn.close()

			coachsession_search_Tv.tag_configure("even",background="green")
			coachsession_search_Tv.tag_configure("odd",background="red")

			count=0
			for row in items:
				if row == []:
					pass
				else:
					if count%2==0:
						coachsession_search_Tv.insert('','end',text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7]),tags=["even"])
					else:
						coachsession_search_Tv.insert('','end',text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7]),tags=["odd"])
					count+=1


		def returnColour(usernameReturn, startTimeReturn, endTimeReturn, dateReturn, courtReturn, groupsReturn, techniqueReturn):
			usernameReturn.config(fg="black")
			startTimeReturn.config(fg="black")
			endTimeReturn.config(fg="black")
			dateReturn.config(fg="black")
			courtReturn.config(fg="black")
			groupsReturn.config(fg="black")
			techniqueReturn.config(fg="black")


		def updateCoachSessionDetails(self):
			response = askyesno("Are you sure?", "Do you want to update a coach's session")
			if response == False:
				showinfo("Info", "Update cancelled")

			else:

				updateCoachSession=Toplevel(bg="white")

				title_label =Label(updateCoachSession, cursor="tcross",text = 'Update Session' , fg ='SpringGreen3',bg='white',font=('Verdana',15,'bold'))
				title_label.place(rely=0.1,relx=0.5,anchor=CENTER)

				update_time=Button(updateCoachSession, cursor="tcross",text = 'Update Time', command = lambda : updateCoachSessionTime(updateCoachSession), fg ='white', bg='black', relief= 'groove', font = ('Verdana',9,'bold'), padx =20)
				update_time.place(rely=0.25,relx=0.5,anchor=CENTER)

				update_date=Button(updateCoachSession, cursor="tcross", text = 'Update Date', command = lambda : updateCoachSessionDate(newEventDate, updateCoachSession), fg ='white', bg='black', relief= 'groove', font = ('Verdana',9,'bold'), padx =20)
				update_date.place(rely=0.4,relx=0.5,anchor=CENTER)

				update_courts=Button(updateCoachSession, cursor="tcross",text = 'Update Courts', command = lambda : updateCoachSessionCourts(updateCoachSession), fg ='white', bg='black', relief= 'groove', font = ('Verdana',9,'bold'), padx =20)
				update_courts.place(rely=0.55,relx=0.5,anchor=CENTER)

				update_groups=Button(updateCoachSession, cursor="tcross",text = 'Update Groups', command = lambda : updateCoachSessionGroups(updateCoachSession), fg ='white', bg='black', relief= 'groove', font = ('Verdana',9,'bold'), padx =20)
				update_groups.place(rely=0.7,relx=0.5,anchor=CENTER)

				update_technique=Button(updateCoachSession, cursor="tcross",text = 'Update Technique', command = lambda : updateCoachSessionTechnique(updateCoachSession), fg ='white', bg='black', relief= 'groove', font = ('Verdana',9,'bold'), padx =20)
				update_technique.place(rely=0.85,relx=0.5,anchor=CENTER)



		def updateCoachSessionTime(frame):
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

					updateTimes=Toplevel(bg="white")
					updateTimes.geometry('200x200')

					title_label =Label(updateTimes,text ="Select New Times", fg ='SpringGreen3',bg='white',font=('Verdana',13,'bold','underline'))
					title_label.place(rely=0.1,relx=0.5,anchor=CENTER)

					update_starttime_label =Label(updateTimes,text ="New Start Time:", fg ='black',bg='white',font=('Verdana',9,'bold'))
					update_starttime_label.place(rely=0.35,relx=0.3,anchor=CENTER)

					update_endtime_label =Label(updateTimes,text ="New End Time:", fg ='black',bg='white',font=('Verdana',9,'bold'))
					update_endtime_label.place(rely=0.55,relx=0.3,anchor=CENTER)

					update_starttime_spinbox = Spinbox(updateTimes, width=7,font=("Tahoma",8, 'bold'), bd=3, relief='ridge', cursor="tcross",textvariable=new_start_time, values=('8.00', '8.15', '8.30', '8.45', '9.00', '9.15', '9.30', '9.45', '10.00', '10.15', '10.30', '10.45', '11.00', '11.15', '11.30', '11.45', '12.00', '12.15','12.30','12.45','13.00','13.15','13.30','13.45','14.00','14.15','14.30','14.45','15.00','15.15','15.30','15.45','16.00','16.15','16.30','16.45','17.00','17.15','17.30','17.45','18.00','18.15','18.30','18.45','19.00','19.15','19.30','19.45','20.00','20.15','20.30','20.45','21.00','21.15','21.30','21.45','22.00'))
					update_starttime_spinbox.place(rely=0.353, relx=0.79, anchor='center')

					update_endtime_spinbox = Spinbox(updateTimes, width=7,font=("Tahoma",8, 'bold'), bd=3, relief='ridge', cursor="tcross", textvariable=new_end_time, values=('9.00', '9.15', '9.30', '9.45', '10.00', '10.15', '10.30', '10.45', '11.00', '11.15', '11.30', '11.45', '12.00', '12.15','12.30','12.45','13.00','13.15','13.30','13.45','14.00','14.15','14.30','14.45','15.00','15.15','15.30','15.45','16.00','16.15','16.30','16.45','17.00','17.15','17.30','17.45','18.00','18.15','18.30','18.45','19.00','19.15','19.30','19.45','20.00','20.15','20.30','20.45','21.00','21.15','21.30','21.45','22.00','22.15','22.30','22.45','23.00'))
					update_endtime_spinbox.place(rely=0.553, relx=0.79, anchor='center')

					update_time_button = Button(updateTimes, text='Confirm Update',font=("Tahoma",10, 'bold'), fg='white', bg='black',cursor="tcross",command=lambda : confirmNewTimes(updateTimes, coachUsername), padx=10, bd=4, relief="ridge")
					update_time_button.place(rely=0.85, relx=0.5, anchor='center')

			conn.commit()
			conn.close()

			treeviewPopulate()


		def confirmNewTimes(frame, username):
			conn = sqlite3.connect('CoachDetails.db')
			c = conn.cursor()

			frame.withdraw()

			isValid = True
			isValid = isValid and validate_new_start_time(new_start_time.get(), new_end_time.get(), "Start Time")
			isValid = isValid and validate_new_end_time(new_end_time.get(), "End Time")

			if isValid:
				newCoachSessionStartTime = new_start_time.get()
				newCoachSessionEndTime = new_end_time.get()

				c.execute("""UPDATE coachSession SET startTime = :new_start_time WHERE username=:username""", {
					"new_start_time": str(new_start_time.get()),
					"username": username
				})
				c.execute("""UPDATE coachSession SET endTime = :new_end_time WHERE username=:username""", {
					"new_end_time": str(new_end_time.get()),
					"username": username
				})

				messagebox.showinfo("info", "The coach's new session start time is now "+newCoachSessionStartTime)
				messagebox.showinfo("info", "The coach's new session end time is now "+newCoachSessionEndTime)

			conn.commit()
			conn.close()

			treeviewPopulate()


		def updateCoachSessionCourts(frame):
			conn = sqlite3.connect('CoachDetails.db')
			c = conn.cursor()

			frame.withdraw()

			coachUsername = simpledialog.askstring("info", "Enter the username of the coach you want to update")
			if coachUsername != '' and len(coachUsername) <25 and '@' in coachUsername and '.' in coachUsername:
				c.execute(f"SELECT * FROM coachSession WHERE username=?", (coachUsername,))
				data = c.fetchone()
				if not data:
					messagebox.showinfo("Warning", "The username entered was not found in the database", icon='error')

				else:

					newcourts = Toplevel(self.coachSession, bg="white")
					newcourts.geometry('500x500')

					title_label = tkinter.Label(newcourts, text="Update the No. Courts Needed For The Session", font=('Tahoma', 15, 'underline', 'bold'), fg='SpringGreen3', bg='white')
					title_label.place(rely=0.03, relx=0.5, anchor='center')

					confirm_button = tkinter.Button(newcourts, text="Confirm Selection", command=lambda : updateCourts(newcourts, coachUsername), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 10, 'bold'), padx=35, cursor="tcross")
					confirm_button.place(rely=0.112, relx=0.5, anchor='center')

					all_button = tkinter.Button(newcourts, text="Select All", command=lambda : addAllCourts(newcourt1, newcourt2, newcourt3, newcourt4, newcourt5, newcourt6, newcourt7, newcourt8, newcourt9, newcourt10, newcourt11, newcourt12), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 8, 'bold'), padx=10, cursor="tcross")
					all_button.place(rely=0.112, relx=0.15, anchor='center')

					clear_button = tkinter.Button(newcourts, text="Clear All", command=lambda : clearAllCourts(newcourt1, newcourt2, newcourt3, newcourt4, newcourt5, newcourt6, newcourt7, newcourt8, newcourt9, newcourt10, newcourt11, newcourt12), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 8, 'bold'), padx=10, cursor="tcross")
					clear_button.place(rely=0.112, relx=0.85, anchor='center')


					confirm_court1 = Checkbutton(newcourts, cursor="tcross",text="Court 1  V", variable=newcourt1,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
					confirm_court1.place(rely=0.2, relx=0.15, anchor='center')

					confirm_court2 = Checkbutton(newcourts, cursor="tcross",text="Court 2  V", variable=newcourt2,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
					confirm_court2.place(rely=0.4, relx=0.15, anchor='center')

					confirm_court3 = Checkbutton(newcourts, cursor="tcross",text="Court 3  V", variable=newcourt3,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
					confirm_court3.place(rely=0.6, relx=0.15, anchor='center')

					confirm_court4 = Checkbutton(newcourts, cursor="tcross",text="Court 4  V", variable=newcourt4,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
					confirm_court4.place(rely=0.8, relx=0.15, anchor='center')

					confirm_court5 = Checkbutton(newcourts, cursor="tcross",text="Court 5  V", variable=newcourt5,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
					confirm_court5.place(rely=0.2, relx=0.5, anchor='center')

					confirm_court6 = Checkbutton(newcourts, cursor="tcross",text="Court 6  V", variable=newcourt6,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
					confirm_court6.place(rely=0.4, relx=0.5, anchor='center')

					confirm_court7 = Checkbutton(newcourts, cursor="tcross",text="Court 7  V", variable=newcourt7,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
					confirm_court7.place(rely=0.6, relx=0.5, anchor='center')

					confirm_court8 = Checkbutton(newcourts, cursor="tcross",text="Court 8  V", variable=newcourt8,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
					confirm_court8.place(rely=0.8, relx=0.5, anchor='center')

					confirm_court9 = Checkbutton(newcourts, cursor="tcross",text="Court 9  V", variable=newcourt9,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
					confirm_court9.place(rely=0.2, relx=0.85, anchor='center')

					confirm_court10 = Checkbutton(newcourts, cursor="tcross",text="Court 10  V", variable=newcourt10,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
					confirm_court10.place(rely=0.4, relx=0.85, anchor='center')

					confirm_court11 = Checkbutton(newcourts, cursor="tcross",text="Court 11 V", variable=newcourt11,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
					confirm_court11.place(rely=0.6, relx=0.85, anchor='center')

					confirm_court12 = Checkbutton(newcourts, cursor="tcross",text="Court 12 V", variable=newcourt12,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
					confirm_court12.place(rely=0.8, relx=0.85, anchor='center')


					background_entry_canvas = Canvas(newcourts,width=100, height=58, bg = "white")
					background_entry_canvas.place(rely=0.3,relx=0.15,anchor=CENTER)

					background_entry_image = PhotoImage(file ="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images/Images/courts.png")

					background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
					background_entry_canvas.background_entry_image = background_entry_image


					background_entry_canvas = Canvas(newcourts,width=100, height=58, bg = "white")
					background_entry_canvas.place(rely=0.5,relx=0.15,anchor=CENTER)

					background_entry_image = PhotoImage(file ="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images/Images/courts.png")

					background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
					background_entry_canvas.background_entry_image = background_entry_image


					background_entry_canvas = Canvas(newcourts,width=100, height=58, bg = "white")
					background_entry_canvas.place(rely=0.7,relx=0.15,anchor=CENTER)

					background_entry_image = PhotoImage(file ="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images/Images/courts.png")

					background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
					background_entry_canvas.background_entry_image = background_entry_image


					background_entry_canvas = Canvas(newcourts,width=100, height=58, bg = "white")
					background_entry_canvas.place(rely=0.9,relx=0.15,anchor=CENTER)

					background_entry_image = PhotoImage(file ="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images/Images/courts.png")

					background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
					background_entry_canvas.background_entry_image = background_entry_image


					background_entry_canvas = Canvas(newcourts,width=100, height=58, bg = "white")
					background_entry_canvas.place(rely=0.3,relx=0.5,anchor=CENTER)

					background_entry_image = PhotoImage(file ="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images/Images/courts.png")

					background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
					background_entry_canvas.background_entry_image = background_entry_image


					background_entry_canvas = Canvas(newcourts,width=100, height=58, bg = "white")
					background_entry_canvas.place(rely=0.5,relx=0.5,anchor=CENTER)

					background_entry_image = PhotoImage(file ="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images/Images/courts.png")

					background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
					background_entry_canvas.background_entry_image = background_entry_image


					background_entry_canvas = Canvas(newcourts,width=100, height=58, bg = "white")
					background_entry_canvas.place(rely=0.7,relx=0.5,anchor=CENTER)

					background_entry_image = PhotoImage(file ="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images/Images/courts.png")

					background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
					background_entry_canvas.background_entry_image = background_entry_image


					background_entry_canvas = Canvas(newcourts,width=100, height=58, bg = "white")
					background_entry_canvas.place(rely=0.9,relx=0.5,anchor=CENTER)

					background_entry_image = PhotoImage(file ="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images/Images/courts.png")

					background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
					background_entry_canvas.background_entry_image = background_entry_image


					background_entry_canvas = Canvas(newcourts,width=100, height=58, bg = "white")
					background_entry_canvas.place(rely=0.3,relx=0.85,anchor=CENTER)

					background_entry_image = PhotoImage(file ="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images/Images/courts.png")

					background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
					background_entry_canvas.background_entry_image = background_entry_image


					background_entry_canvas = Canvas(newcourts,width=100, height=58, bg = "white")
					background_entry_canvas.place(rely=0.5,relx=0.85,anchor=CENTER)

					background_entry_image = PhotoImage(file ="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images/Images/courts.png")

					background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
					background_entry_canvas.background_entry_image = background_entry_image


					background_entry_canvas = Canvas(newcourts,width=100, height=58, bg = "white")
					background_entry_canvas.place(rely=0.7,relx=0.85,anchor=CENTER)

					background_entry_image = PhotoImage(file ="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images/Images/courts.png")

					background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
					background_entry_canvas.background_entry_image = background_entry_image


					background_entry_canvas = Canvas(newcourts,width=100, height=58, bg = "white")
					background_entry_canvas.place(rely=0.9,relx=0.85,anchor=CENTER)

					background_entry_image = PhotoImage(file ="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images/Images/courts.png")

					background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
					background_entry_canvas.background_entry_image = background_entry_image

			conn.commit()
			conn.close()


		def updateCourts(frame, username):
			conn = sqlite3.connect('CoachDetails.db')
			c = conn.cursor()

			frame.withdraw()

			isValid = True
			isValid = isValid and validate_new_courts(newcourt1.get(), newcourt2.get(), newcourt3.get(), newcourt4.get(), newcourt5.get(), newcourt6.get(), newcourt7.get(), newcourt8.get(), newcourt9.get(), newcourt10.get(), newcourt11.get(), newcourt12.get(), "Court")

			if isValid:
				final_courts = ""
				if (newcourt1.get() ==1):
					final_courts = final_courts + '1, '
				if (newcourt2.get() ==1):
					final_courts = final_courts + '2, '
				if (newcourt3.get() ==1):
					final_courts = final_courts + '3, '
				if (newcourt4.get() ==1):
					final_courts = final_courts + '4, '
				if (newcourt5.get() ==1):
					final_courts = final_courts + '5, '
				if (newcourt6.get() ==1):
					final_courts = final_courts + '6, '
				if (newcourt7.get() ==1):
					final_courts = final_courts + '7, '
				if (newcourt8.get() ==1):
					final_courts = final_courts + '8, '
				if (newcourt9.get() ==1):
					final_courts = final_courts + '9, '
				if (newcourt10.get() ==1):
					final_courts = final_courts + '10, '
				if (newcourt11.get() ==1):
					final_courts = final_courts + '11, '
				if (newcourt12.get() ==1):
					final_courts = final_courts + '12'

				c.execute("""UPDATE coachSession SET courts = :newCourts WHERE username=:username""", {
					"newCourts": str(final_courts),
					"username": username
				})

				messagebox.showinfo("info", "The session's new courts are now "+final_courts)

			conn.commit()
			conn.close()

			treeviewPopulate()


		def updateCoachSessionGroups(frame):
			conn = sqlite3.connect('CoachDetails.db')
			c = conn.cursor()

			frame.withdraw()

			coachUsername = simpledialog.askstring("info", "Enter the username of the coach you want to update")
			if coachUsername != '' and len(coachUsername) <25 and '@' in coachUsername and '.' in coachUsername:
				c.execute(f"SELECT * FROM coachSession WHERE username=?", (coachUsername,))
				data = c.fetchone()
				if not data:
					messagebox.showinfo("Warning", "The username entered was not found in the database", icon='error')

				else:

					groups = Toplevel(self.coachSession, bg="white")
					groups.geometry('450x350')

					title_label = tkinter.Label(groups, text="Update the No. Groups Needed For The Session", font=('Tahoma', 12, 'underline', 'bold'), fg='SpringGreen3', bg='white')
					title_label.place(rely=0.03, relx=0.5, anchor='center')

					confirm_button = tkinter.Button(groups, text="Confirm Selection", command=lambda : updateGroups(groups, coachUsername), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 9, 'bold'), padx=35, cursor="tcross")
					confirm_button.place(rely=0.15, relx=0.5, anchor='center')

					all_button = tkinter.Button(groups, text="Select All", command=lambda : addAllGroups(newgroup1, newgroup2, newgroup3, newgroup4, newgroup5, newgroup6, newgroup7, newgroup8, newgroup9, newgroup10, newgroup11, newgroup12, newgroup13, newgroup14, newgroup15, newgroup16, newgroup17, newgroup18, newgroup19, newgroup20), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 8, 'bold'), padx=10, cursor="tcross")
					all_button.place(rely=0.15, relx=0.15, anchor='center')

					clear_button = tkinter.Button(groups, text="Clear All", command=lambda : clearAllGroups(newgroup1, newgroup2, newgroup3, newgroup4, newgroup5, newgroup6, newgroup7, newgroup8, newgroup9, newgroup10, newgroup11, newgroup12, newgroup13, newgroup14, newgroup15, newgroup16, newgroup17, newgroup18, newgroup19, newgroup20), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 8, 'bold'), padx=10, cursor="tcross")
					clear_button.place(rely=0.15, relx=0.85, anchor='center')


					confirm_group1 = Checkbutton(groups, cursor="tcross",text="Group 1", variable=newgroup1,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
					confirm_group1.place(rely=0.3, relx=0.15, anchor='center')

					confirm_group2 = Checkbutton(groups, cursor="tcross",text="Group 2", variable=newgroup2,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
					confirm_group2.place(rely=0.3, relx=0.38, anchor='center')

					confirm_group3 = Checkbutton(groups, cursor="tcross",text="Group 3", variable=newgroup3,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
					confirm_group3.place(rely=0.3, relx=0.61, anchor='center')

					confirm_group4 = Checkbutton(groups, cursor="tcross",text="Group 4", variable=newgroup4,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
					confirm_group4.place(rely=0.3, relx=0.84, anchor='center')

					confirm_group5 = Checkbutton(groups, cursor="tcross",text="Group 5", variable=newgroup5,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
					confirm_group5.place(rely=0.45, relx=0.15, anchor='center')

					confirm_group6 = Checkbutton(groups, cursor="tcross",text="Group 6", variable=newgroup6,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
					confirm_group6.place(rely=0.45, relx=0.38, anchor='center')

					confirm_group7 = Checkbutton(groups, cursor="tcross",text="Group 7", variable=newgroup7,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
					confirm_group7.place(rely=0.45, relx=0.61, anchor='center')

					confirm_group8 = Checkbutton(groups, cursor="tcross",text="Group 8", variable=newgroup8,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
					confirm_group8.place(rely=0.45, relx=0.84, anchor='center')

					confirm_group9 = Checkbutton(groups, cursor="tcross",text="Group 9", variable=newgroup9,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
					confirm_group9.place(rely=0.6, relx=0.15, anchor='center')

					confirm_group10 = Checkbutton(groups, cursor="tcross",text="Group 10", variable=newgroup10,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
					confirm_group10.place(rely=0.6, relx=0.38, anchor='center')

					confirm_group11 = Checkbutton(groups, cursor="tcross",text="Group 11", variable=newgroup11,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
					confirm_group11.place(rely=0.6, relx=0.61, anchor='center')

					confirm_group12 = Checkbutton(groups, cursor="tcross",text="Group 12", variable=newgroup12,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
					confirm_group12.place(rely=0.6, relx=0.84, anchor='center')

					confirm_group13 = Checkbutton(groups, cursor="tcross",text="Group 13", variable=newgroup13,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
					confirm_group13.place(rely=0.75, relx=0.15, anchor='center')

					confirm_group14 = Checkbutton(groups, cursor="tcross",text="Group 14", variable=newgroup14,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
					confirm_group14.place(rely=0.75, relx=0.38, anchor='center')

					confirm_group15 = Checkbutton(groups, cursor="tcross",text="Group 15", variable=newgroup15,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
					confirm_group15.place(rely=0.75, relx=0.61, anchor='center')

					confirm_group16 = Checkbutton(groups, cursor="tcross",text="Group 16", variable=newgroup16,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
					confirm_group16.place(rely=0.75, relx=0.84, anchor='center')

					confirm_group17 = Checkbutton(groups, cursor="tcross",text="Group 17", variable=newgroup17,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
					confirm_group17.place(rely=0.9, relx=0.15, anchor='center')

					confirm_group18 = Checkbutton(groups, cursor="tcross",text="Group 18", variable=newgroup18,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
					confirm_group18.place(rely=0.9, relx=0.38, anchor='center')

					confirm_group19 = Checkbutton(groups, cursor="tcross",text="Group 19", variable=newgroup19,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
					confirm_group19.place(rely=0.9, relx=0.61, anchor='center')

					confirm_group20 = Checkbutton(groups, cursor="tcross",text="Group 20", variable=newgroup20,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
					confirm_group20.place(rely=0.9, relx=0.84, anchor='center')

			conn.commit()
			conn.close()


		def updateGroups(frame, username):
			conn = sqlite3.connect('CoachDetails.db')
			c = conn.cursor()

			frame.withdraw()

			isValid = True
			isValid = isValid and validate_new_groups(newgroup1.get(), newgroup2.get(), newgroup3.get(), newgroup4.get(), newgroup5.get(), newgroup6.get(), newgroup7.get(), newgroup8.get(), newgroup9.get(), newgroup10.get(), newgroup11.get(), newgroup12.get(), newgroup13.get(), newgroup14.get(), newgroup15.get(), newgroup16.get(), newgroup17.get(), newgroup18.get(), newgroup19.get(), newgroup20.get(), "Group")

			if isValid:
				final_groups = ""
				if (newgroup1.get() ==1):
					final_groups = final_groups + '1, '
				if (newgroup2.get() ==1):
					final_groups = final_groups + '2, '
				if (newgroup3.get() ==1):
					final_groups = final_groups + '3, '
				if (newgroup4.get() ==1):
					final_groups = final_groups + '4, '
				if (newgroup5.get() ==1):
					final_groups = final_groups + '5, '
				if (newgroup6.get() ==1):
					final_groups = final_groups + '6, '
				if (newgroup7.get() ==1):
					final_groups = final_groups + '7, '
				if (newgroup8.get() ==1):
					final_groups = final_groups + '8, '
				if (newgroup9.get() ==1):
					final_groups = final_groups + '9, '
				if (newgroup10.get() ==1):
					final_groups = final_groups + '10, '
				if (newgroup11.get() ==1):
					final_groups = final_groups + '11, '
				if (newgroup12.get() ==1):
					final_groups = final_groups + '12, '
				if (newgroup13.get() ==1):
					final_groups = final_groups + '13, '
				if (newgroup14.get() ==1):
					final_groups = final_groups + '14, '
				if (newgroup15.get() ==1):
					final_groups = final_groups + '15, '
				if (newgroup16.get() ==1):
					final_groups = final_groups + '16, '
				if (newgroup17.get() ==1):
					final_groups = final_groups + '17, '
				if (newgroup18.get() ==1):
					final_groups = final_groups + '18, '
				if (newgroup19.get() ==1):
					final_groups = final_groups + '19, '
				if (newgroup20.get() ==1):
					final_groups = final_groups + '20'

				c.execute("""UPDATE coachSession SET groups = :newGroups WHERE username=:username""", {
					"newGroups": str(final_groups),
					"username": username
				})

				messagebox.showinfo("info", "The session's new groups are now "+final_groups)

			conn.commit()
			conn.close()

			treeviewPopulate()


		def updateCoachSessionTechnique(frame):
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

					updateTechnique=Toplevel(bg="white")
					updateTechnique.geometry('200x200')

					title_label =Label(updateTechnique,text ="Select New Technique" , fg ='SpringGreen3',bg='white',font=('Verdana',11,'bold','underline'))
					title_label.place(rely=0.06,relx=0.5,anchor=CENTER)

					technique1_radiobutton = Radiobutton(updateTechnique, text="Net Play", variable=newtechnique, value=1, font=("Tahoma",9, 'bold'), cursor="tcross", bg="white", bd=2, relief="ridge")
					technique1_radiobutton.place(rely=0.22, relx=0.5, anchor='center')

					technique2_radiobutton = Radiobutton(updateTechnique, text="Smash", variable=newtechnique, value=2, font=("Tahoma",9, 'bold'), cursor="tcross", bg="white", bd=2, relief="ridge")
					technique2_radiobutton.place(rely=0.4, relx=0.5, anchor='center')

					technique3_radiobutton = Radiobutton(updateTechnique, text="Rally", variable=newtechnique, value=3, font=("Tahoma",9, 'bold'), cursor="tcross", bg="white", bd=2, relief="ridge")
					technique3_radiobutton.place(rely=0.58, relx=0.5, anchor='center')

					technique4_radiobutton = Radiobutton(updateTechnique, text="Back Court", variable=newtechnique, value=4, font=("Tahoma",9, 'bold'), cursor="tcross", bg="white", bd=2, relief="ridge")
					technique4_radiobutton.place(rely=0.76, relx=0.5, anchor='center')

					technique_update_button=Button(updateTechnique,text = 'Confirm Update', command = lambda : techniqueUpdate(updateTechnique, coachUsername), fg ='white', bg='black', relief= 'groove', font = ('Verdana',11,'bold'), padx =30)
					technique_update_button.place(rely=0.93,relx=0.5,anchor=CENTER)

			conn.commit()
			conn.close()


		def techniqueUpdate(frame, username):
			conn = sqlite3.connect('CoachDetails.db')
			c = conn.cursor()

			frame.withdraw()

			isValid = True
			isValid = isValid and validate_new_techniques(newtechnique.get(), "Technique")

			if isValid:
				if (newtechnique.get() ==1):
					final_technique = 'Net Play'
				if (newtechnique.get() ==2):
					final_technique = 'Smash'
				if (newtechnique.get() ==3):
					final_technique = 'Rally'
				if (newtechnique.get() ==4):
					final_technique = 'Back Court'

				c.execute("""UPDATE coachSession SET technique = :newTechnique WHERE username=:username""", {
					"newTechnique": str(final_technique),
					"username": username
				})

				messagebox.showinfo("info", "The session's new technique is now "+ final_technique)

			conn.commit()
			conn.close()

			treeviewPopulate()


		def deleteCoachSessionDetails(self):
			conn = sqlite3.connect('CoachDetails.db')
			c = conn.cursor()

			response = askyesno("Are you sure?", "Do you want to delete a coach session")
			if response == False:
				showinfo("Info", "Deletion cancelled")

			else:

				coachUsername = simpledialog.askstring("Info", "Enter the username of the coach you want to delete")

				if coachUsername !='' and len(coachUsername) <25 and '@' in coachUsername and '.' in coachUsername:

					c.execute(f"SELECT * FROM coachSession WHERE username =?", (coachUsername,))
					data = c.fetchone()
					if not data:
						messagebox.showinfo("Warning", "The username entered was not found in the database", icon='error')

					else:

						c.execute(f"DELETE FROM coachSession WHERE username =?", (coachUsername,))
						messagebox.showinfo("info", "The coach session associated with username "+coachUsername+" has been deleted from the database")

				else:

					messagebox.showinfo("Warning", "The username entered does not meet the rules", icon='error')

			conn.commit()
			conn.close()

			treeviewPopulate()


		def searchCoachSessionDetails():
			conn = sqlite3.connect('CoachDetails.db')
			c = conn.cursor()

			response = askyesno("Are you sure?", "Do you want to search a coach's session")
			if response == False:
				showinfo("Info", "Search cancelled")

			else:

				coachUsername = simpledialog.askstring("info", "Enter the username of the coach you want to find the session on")
				if coachUsername != '' and len(coachUsername) <25 and '@' in coachUsername and '.' in coachUsername:
					c.execute(f"SELECT * FROM coachSession WHERE username=?", (coachUsername,))
					data = c.fetchone()
					if not data:
						messagebox.showinfo("Warning", "The username entered was not found in the database", icon='error')
					else:

						messagebox.showinfo("info", "The session's details are listed below" + "\n\n" + "Username: " + str(data[0]) + "\n" + "Start Time: " + str(data[1]) + "\n" + "End Time: " + str(data[2]) + "\n" + "Date: " + str(data[3]) + "\n" + "Courts: " + str(data[4]) + "\n" + "Groups: " + str(data[5]) + "\n" + "People: " + str(data[6]) + "\n" + "Technique: " + str(data[7]))

				else:

					messagebox.showinfo("Warning", "The username entered does not meet the rules", icon='error')

			conn.commit()
			conn.close()

			treeviewPopulate()


		def submitCoachSession():
			isValid = True
			isValid = isValid and validate_username(self.coachNamesAndPasswords.get(), "Username", username_label)
			isValid = isValid and validate_start_time(timeStart.get(), timeEnd.get(),"Start Time", starttime_label)
			isValid = isValid and validate_end_time(timeEnd.get(), "End Time", endtime_label)
			isValid = isValid and validate_date(eventDate.get(), "Date", date_label)
			isValid = isValid and validate_courts(court1.get(), court2.get(),court3.get(), court4.get(), court5.get(), court6.get(), court7.get(), court8.get(), court9.get(), court10.get(), court11.get(), court12.get(),  "Court", courts_needed_label)
			isValid = isValid and validate_groups(group1.get(), group2.get(), group3.get(), group4.get(), group5.get(), group6.get(), group7.get(), group8.get(), group9.get(), group10.get(), group11.get(), group12.get(), group13.get(), group14.get(), group15.get(), group16.get(), group17.get(), group18.get(), group19.get(), group20.get(), "Group", groups_label)
			isValid = isValid and validate_techniques(techniques_label)


			if isValid:
				coachsession_username = self.coachNamesAndPasswords.get()
				coachsession_starttime= timeStart.get()
				coachsession_endtime= timeEnd.get()
				coachsession_date = eventDate.get()

				final_courts = ""
				if (court1.get() ==1):
					final_courts = final_courts + '1, '
				if (court2.get() ==1):
					final_courts = final_courts + '2, '
				if (court3.get() ==1):
					final_courts = final_courts + '3, '
				if (court4.get() ==1):
					final_courts = final_courts + '4, '
				if (court5.get() ==1):
					final_courts = final_courts + '5, '
				if (court6.get() ==1):
					final_courts = final_courts + '6, '
				if (court7.get() ==1):
					final_courts = final_courts + '7, '
				if (court8.get() ==1):
					final_courts = final_courts + '8, '
				if (court9.get() ==1):
					final_courts = final_courts + '9, '
				if (court10.get() ==1):
					final_courts = final_courts + '10, '
				if (court11.get() ==1):
					final_courts = final_courts + '11, '
				if (court12.get() ==1):
					final_courts = final_courts + '12'

				final_groups = ""
				if (group1.get() ==1):
					final_groups = final_groups + '1, '
				if (group2.get() ==1):
					final_groups = final_groups + '2, '
				if (group3.get() ==1):
					final_groups = final_groups + '3, '
				if (group4.get() ==1):
					final_groups = final_groups + '4, '
				if (group5.get() ==1):
					final_groups = final_groups + '5, '
				if (group6.get() ==1):
					final_groups = final_groups + '6, '
				if (group7.get() ==1):
					final_groups = final_groups + '7, '
				if (group8.get() ==1):
					final_groups = final_groups + '8, '
				if (group9.get() ==1):
					final_groups = final_groups + '9, '
				if (group10.get() ==1):
					final_groups = final_groups + '10, '
				if (group11.get() ==1):
					final_groups = final_groups + '11, '
				if (group12.get() ==1):
					final_groups = final_groups + '12, '
				if (group13.get() ==1):
					final_groups = final_groups + '13, '
				if (group14.get() ==1):
					final_groups = final_groups + '14, '
				if (group15.get() ==1):
					final_groups = final_groups + '15, '
				if (group16.get() ==1):
					final_groups = final_groups + '16, '
				if (group17.get() ==1):
					final_groups = final_groups + '17, '
				if (group18.get() ==1):
					final_groups = final_groups + '18, '
				if (group19.get() ==1):
					final_groups = final_groups + '19, '
				if (group20.get() ==1):
					final_groups = final_groups + '20'

				if (technique.get() ==1):
					final_technique = 'Net Play'
				if (technique.get() ==2):
					final_technique = 'Smash'
				if (technique.get() ==3):
					final_technique = 'Rally'
				if (technique.get() ==4):
					final_technique = 'Back Court'


				final_coach_starttime = format(float(coachsession_starttime), '.2f')
				final_coach_endtime = format(float(coachsession_endtime), '.2f')

				MemberCounter = PeopleCounter()

				response = askyesno("Are you sure?", "Are you sure that all information above is correct?")
				if response == False:
					showinfo("Info", "submition cancelled")

				else:
					conn = sqlite3.connect('CoachDetails.db')
					c = conn.cursor()
					c.execute("INSERT INTO coachSession VALUES (:username, :startTime, :endTime, :date, :courts, :groups, :people, :technique)",
							{
								'username': coachsession_username,
								'startTime': final_coach_starttime,
								'endTime': final_coach_endtime,
								'date': coachsession_date,
								'courts': final_courts,
								'groups': final_groups,
								'people': MemberCounter,
								'technique': final_technique,
							})
					conn.commit()
					conn.close()

					changeCalendarColour()

					self.coachNamesAndPasswords.set('')
					timeStart.set('8.00')
					timeEnd.set('9.00')
					technique.set('1')

					court1.set("0")
					court2.set("0")
					court3.set("0")
					court4.set("0")
					court5.set("0")
					court6.set("0")
					court7.set("0")
					court8.set("0")
					court9.set("0")
					court10.set("0")
					court11.set("0")
					court12.set("0")

					group1.set("0")
					group2.set("0")
					group3.set("0")
					group4.set("0")
					group5.set("0")
					group6.set("0")
					group7.set("0")
					group8.set("0")
					group9.set("0")
					group10.set("0")
					group11.set("0")
					group12.set("0")
					group13.set("0")
					group14.set("0")
					group15.set("0")
					group16.set("0")
					group17.set("0")
					group18.set("0")
					group19.set("0")
					group20.set("0")

					returnColour(username_label, starttime_label, endtime_label, date_label, courts_needed_label, groups_label, techniques_label)
					messagebox.showinfo("info", "Details have been successfully stored")

			treeviewPopulate()


		def CalendarSelection(event):
			conn = sqlite3.connect('CoachDetails.db')
			c = conn.cursor()

			date = cal.get_date()
			date=str(date).split('/')
			newdate=date[0],date[1],date[2]
			a_date = datetime.date(int('20'+newdate[2]),int(newdate[0]), int(newdate[1]))

			string_date = a_date.strftime("%d/%m/%Y")

			c.execute("SELECT * From coachSession WHERE date=?", (string_date,))
			items = c.fetchone()
			if not items:
				messagebox.showinfo("info", "There is no coaching session on this date")

			else:

				messagebox.showinfo("info", "There is a coaching session on this date" + "\n" +
				"The details are listed below:" + "\n\n"
				+ "Coach: " + items[0] + "\n"
				+ "Start Time: " + str(items[1]) + "\n"
				+ "End Time: " + str(items[2]) + "\n"
				+ "Court(s): " + items[4] + "\n"
				+ "Group(s): " + items[5] + "\n"
				+ "No. People: " + str(items[6]) + "\n"
			    + "Technique: " + items[7])

			conn.commit()
			conn.close()


		def changeCalendarColour():
			cal.calevent_remove("all")
			conn = sqlite3.connect('CoachDetails.db')
			c = conn.cursor()

			c.execute("SELECT * FROM coachSession")
			session_array = c.fetchall()

			for row in session_array:
				cal.calevent_create(datetime.date(int(row[3][6:10]), int(row[3][3:5]), int(row[3][0:2])),"View Coaching Session Details","message")

			cal.tag_config("message", background="red", foreground="black")

			conn.commit()
			conn.close()




		timeStart=StringVar()
		timeEnd=StringVar()
		eventDate=StringVar()
		technique=IntVar()

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

		group1=IntVar()
		group2=IntVar()
		group3=IntVar()
		group4=IntVar()
		group5=IntVar()
		group6=IntVar()
		group7=IntVar()
		group8=IntVar()
		group9=IntVar()
		group10=IntVar()
		group11=IntVar()
		group12=IntVar()
		group13=IntVar()
		group14=IntVar()
		group15=IntVar()
		group16=IntVar()
		group17=IntVar()
		group18=IntVar()
		group19=IntVar()
		group20=IntVar()


		new_start_time = StringVar()
		new_end_time = StringVar()
		newEventDate=StringVar()

		newcourt1=IntVar()
		newcourt2=IntVar()
		newcourt3=IntVar()
		newcourt4=IntVar()
		newcourt5=IntVar()
		newcourt6=IntVar()
		newcourt7=IntVar()
		newcourt8=IntVar()
		newcourt9=IntVar()
		newcourt10=IntVar()
		newcourt11=IntVar()
		newcourt12=IntVar()

		newgroup1=IntVar()
		newgroup2=IntVar()
		newgroup3=IntVar()
		newgroup4=IntVar()
		newgroup5=IntVar()
		newgroup6=IntVar()
		newgroup7=IntVar()
		newgroup8=IntVar()
		newgroup9=IntVar()
		newgroup10=IntVar()
		newgroup11=IntVar()
		newgroup12=IntVar()
		newgroup13=IntVar()
		newgroup14=IntVar()
		newgroup15=IntVar()
		newgroup16=IntVar()
		newgroup17=IntVar()
		newgroup18=IntVar()
		newgroup19=IntVar()
		newgroup20=IntVar()

		newtechnique=IntVar()



		username_label = tkinter.Label(self.coachSession, text="Username:", font=('Tahoma', 14, 'bold'), fg='black', bg='white')
		username_label.place(rely=0.36, relx=0.12, anchor='center')

		starttime_label = tkinter.Label(self.coachSession, text="Start Time:", font=('Tahoma', 14, 'bold'), fg='black', bg='white')
		starttime_label.place(rely=0.44, relx=0.12, anchor='center')

		endtime_label = tkinter.Label(self.coachSession, text="End Time:", font=('Tahoma', 14, 'bold'), fg='black', bg='white')
		endtime_label.place(rely=0.52, relx=0.12, anchor='center')

		date_label = tkinter.Label(self.coachSession, text="Session Date:", font=('Tahoma', 14, 'bold'), fg='black', bg='white')
		date_label.place(rely=0.6, relx=0.12, anchor='center')

		courts_needed_label = tkinter.Label(self.coachSession, text="Courts Required:", font=('Tahoma', 14, 'bold'), fg='black', bg='white')
		courts_needed_label.place(rely=0.68, relx=0.12, anchor='center')

		groups_label = tkinter.Label(self.coachSession, text="Group Level:", font=('Tahoma', 14, 'bold'), fg='black', bg='white')
		groups_label.place(rely=0.76, relx=0.12, anchor='center')

		techniques_label = tkinter.Label(self.coachSession, text="Techniques:", font=('Tahoma', 14, 'bold'), fg='black', bg='white')
		techniques_label.place(rely=0.84, relx=0.12, anchor='center')


		starttime_spinbox = Spinbox(self.coachSession, width=7,font=("Tahoma",12, 'bold'), bd=3, relief='ridge', cursor="tcross",textvariable=timeStart, values=('8.00', '8.15', '8.30', '8.45', '9.00', '9.15', '9.30', '9.45', '10.00', '10.15', '10.30', '10.45', '11.00', '11.15', '11.30', '11.45', '12.00', '12.15','12.30','12.45','13.00','13.15','13.30','13.45','14.00','14.15','14.30','14.45','15.00','15.15','15.30','15.45','16.00','16.15','16.30','16.45','17.00','17.15','17.30','17.45','18.00','18.15','18.30','18.45','19.00','19.15','19.30','19.45','20.00','20.15','20.30','20.45','21.00','21.15','21.30','21.45','22.00'))
		starttime_spinbox.place(rely=0.4425, relx=0.3, anchor='center')

		endtime_spinbox = Spinbox(self.coachSession, width=7,font=("Tahoma",12, 'bold'), bd=3, relief='ridge', cursor="tcross", textvariable=timeEnd, values=('9.00', '9.15', '9.30', '9.45', '10.00', '10.15', '10.30', '10.45', '11.00', '11.15', '11.30', '11.45', '12.00', '12.15','12.30','12.45','13.00','13.15','13.30','13.45','14.00','14.15','14.30','14.45','15.00','15.15','15.30','15.45','16.00','16.15','16.30','16.45','17.00','17.15','17.30','17.45','18.00','18.15','18.30','18.45','19.00','19.15','19.30','19.45','20.00','20.15','20.30','20.45','21.00','21.15','21.30','21.45','22.00','22.15','22.30','22.45','23.00'))
		endtime_spinbox.place(rely=0.5225, relx=0.3, anchor='center')

		date_entry = Button(self.coachSession, text='Select Date',font=("Tahoma",10, 'bold'), cursor="tcross",command=lambda : dateEntryCheck(eventDate), padx=10, bd=4, relief="ridge")
		date_entry.place(rely=0.603, relx=0.3, anchor='center')

		courts_needed_button = Button(self.coachSession, text='Select Courts',font=("Tahoma",10, 'bold'), cursor="tcross",command=lambda : courtsRequired(), padx=10, bd=4, relief="ridge")
		courts_needed_button.place(rely=0.683, relx=0.3, anchor='center')

		groups_needed_button = Button(self.coachSession, text='Select Groups',font=("Tahoma",10, 'bold'), cursor="tcross",command=lambda : groupsRequired(), padx=10, bd=4, relief="ridge")
		groups_needed_button.place(rely=0.763, relx=0.3, anchor='center')

		technique1_radiobutton = Radiobutton(self.coachSession, text="Net Play", variable=technique, value=1, font=("Tahoma",9, 'bold'), cursor="tcross", bg="white", bd=2, relief="ridge")
		technique1_radiobutton.place(rely=0.82, relx=0.25, anchor='center')

		technique2_radiobutton = Radiobutton(self.coachSession, text="Smash", variable=technique, value=2, font=("Tahoma",9, 'bold'), cursor="tcross", bg="white", bd=2, relief="ridge")
		technique2_radiobutton.place(rely=0.87, relx=0.25, anchor='center')

		technique3_radiobutton = Radiobutton(self.coachSession, text="Rally", variable=technique, value=3, font=("Tahoma",9, 'bold'), cursor="tcross", bg="white", bd=2, relief="ridge")
		technique3_radiobutton.place(rely=0.82, relx=0.35, anchor='center')

		technique4_radiobutton = Radiobutton(self.coachSession, text="Back Court", variable=technique, value=4, font=("Tahoma",9, 'bold'), cursor="tcross", bg="white", bd=2, relief="ridge")
		technique4_radiobutton.place(rely=0.87, relx=0.355, anchor='center')
		technique.set("1")


		delete_button = tkinter.Button(self.coachSession, cursor="tcross",text="Delete", command=lambda : deleteCoachSessionDetails(self), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 12, 'bold'), padx=10, pady=5)
		delete_button.place(rely=0.95, relx=0.058, anchor='center')

		update_button = tkinter.Button(self.coachSession, cursor="tcross",text="Update", command=lambda : updateCoachSessionDetails(self), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 12, 'bold'), padx=10, pady=5)
		update_button.place(rely=0.95, relx=0.168, anchor='center')

		search_button = tkinter.Button(self.coachSession, cursor="tcross",text="Search", command=searchCoachSessionDetails, fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 12, 'bold'), padx=10, pady=5)
		search_button.place(rely=0.95, relx=0.276, anchor='center')

		create_button = tkinter.Button(self.coachSession, cursor="tcross",text="Submit", command=submitCoachSession, fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 12, 'bold'), padx=10, pady=5)
		create_button.place(rely=0.95, relx=0.384, anchor='center')


		coachsession_search_Tv=ttk.Treeview(self.coachSession,height=4,columns=('Start Time','End Time','Date','Courts','Groups','No. People','Technique'))
		coachsession_search_Tv.place(relx=0.5,rely=0.22,anchor=CENTER)

		coachsession_search_Tv.heading("#0",text='Username')
		coachsession_search_Tv.column("#0",minwidth=0,width=180)
		coachsession_search_Tv.heading("#1",text='Start Time')
		coachsession_search_Tv.column("#1",minwidth=0,width=90)
		coachsession_search_Tv.heading("#2",text='End Time')
		coachsession_search_Tv.column("#2",minwidth=0,width=90)
		coachsession_search_Tv.heading("#3",text='Date')
		coachsession_search_Tv.column("#3",minwidth=0,width=100)
		coachsession_search_Tv.heading("#4",text='Courts')
		coachsession_search_Tv.column("#4",minwidth=0,width=120)
		coachsession_search_Tv.heading("#5",text='Groups')
		coachsession_search_Tv.column("#5",minwidth=0,width=120)
		coachsession_search_Tv.heading("#6",text='No. People')
		coachsession_search_Tv.column("#6",minwidth=0,width=80)
		coachsession_search_Tv.heading("#7",text='Technique')
		coachsession_search_Tv.column("#7",minwidth=0,width=100)

		coachsession_ysearch_scrollbar = Scrollbar(self.coachSession, orient = 'vertical', command = coachsession_search_Tv.yview, cursor="tcross")
		coachsession_ysearch_scrollbar.place(relx=0.95,rely=0.22,anchor='center',height=109)
		coachsession_search_Tv.configure(yscrollcommand=coachsession_ysearch_scrollbar.set)

		cal = Calendar(self.coachSession, font="Tahoma 21", selectmode='day', cursor="tcross", year=2021, month=5, day=29)
		cal.place(rely=0.62, relx=0.71, anchor='center')

		cal.bind("<<CalendarSelected>>", CalendarSelection)


		treeviewPopulate()
		changeCalendarColour()


		def onTreeviewPopup(tvPopup, event=None):
			try:
				rowItem = coachsession_search_Tv.identify_row(event.y)
				tvPopup.selection = coachsession_search_Tv.set(rowItem)

				coachsession_search_Tv.selection_set(rowItem)
				coachsession_search_Tv.focus(rowItem)
				tvPopup.post(event.x_root, event.y_root)
			finally:
				tvPopup.grab_release()

		tvPopup = Menu(self.coachSession, tearoff = 0)
		tvPopup.add_command(label = "Update", command = partial(updateCoachSessionDetails, True))
		tvPopup.add_separator()
		tvPopup.add_command(label = "Delete", command = partial(deleteCoachSessionDetails,True))

		coachsession_search_Tv.bind("<Button-3>", partial(onTreeviewPopup, tvPopup))


	def coachSelection(self):
		self.coachNamesAndPasswords = StringVar()

		coach_name_choices = self.get_coach_details()
		if (len(coach_name_choices) > 0) :
			coach_selection_dropdown = OptionMenu(self.coachSession, self.coachNamesAndPasswords, *coach_name_choices)
			coach_selection_dropdown.place(rely=0.365, relx=0.305, anchor='center')


	def get_coach_details(self):
		conn = sqlite3.connect('coachDetails.db')
		c = conn.cursor()

		coach_name_list = []

		c.execute("SELECT * From coach")
		items = c.fetchall()

		for row in items:
			if row == []:
				pass
			else:
				coach_name = row[0]
				coach_name_list.append(coach_name)

		conn.commit()
		conn.close()

		return coach_name_list