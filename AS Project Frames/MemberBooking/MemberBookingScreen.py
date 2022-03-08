# Member Booking Screen

from tkinter import ttk
from tkinter import messagebox
import tkinter.simpledialog
from tkinter.messagebox import showinfo
from tkinter.messagebox import askyesno
import sqlite3
from tkinter import *
from functools import partial
from tkcalendar import Calendar
import datetime
import Pmw
from MemberBooking.BookingEmail import BookingEmail
from PIL import Image, ImageTk
from io import BytesIO



# Member Booking Class
class BookingContent:

	previous = ''
	courts = False

	# Initiates main screen window
	def __init__(self, mainScreen, filepath):
		self.booking = mainScreen
		self.conn = sqlite3.connect(filepath + '\\_databases_images_doc\\Databases\\LisburnRacquetsDatabase.db')
		self.c = self.conn.cursor()
		self.filepath = filepath


		# Creates MemberBooking database table if it does not exist
		self.c.execute("""CREATE TABLE IF NOT EXISTS MemberBooking (
					image BlOB,
					username text,
					type text,
					date text,
					court text,
					bookingID integer
					)""")


	# Generate member booking content
	def generateBookingContnt(self):

		# Select the date of the booking
		def dateEntryCheck(dob):
			def assign_dob():
				eventDate.set(cal.get_date())
				top.withdraw()

			today = datetime.date.today()
			top = Toplevel(self.booking)

			cal = Calendar(top, font="serif 16", date_pattern='dd/mm/yyyy',selectmode='day', cursor="tcross", year=today.year, month=today.month, day=today.day)
			cal.pack(fill="both", expand=True)
			ttk.Button(top, text="ok", command=assign_dob).pack()


		# Ensures username entered conforms to the rules
		def validate_username(value, label):
			if (value == ''):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The username field cannot be empty", icon='error')
				return False

			label.config(fg="SpringGreen3")
			return True


		# Ensures date selected conforms to the rules
		def validate_date(value, label):
			if (value == ''):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The date cannot be empty", icon='error')
				return False

			presentDate = datetime.datetime.now()
			date_formated = presentDate.strftime("%d/%m/%Y")

			d1 = datetime.datetime.strptime(value, "%d/%m/%Y").date()
			d2 = datetime.datetime.strptime(str(date_formated), "%d/%m/%Y").date()

			if d2>d1:
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The start date cannot be before the current date", icon='error')
				return False

			conn = sqlite3.connect(self.filepath + '\\_databases_images_doc\\Databases\\LisburnRacquetsDatabase.db')
			c = conn.cursor()

			c.execute("SELECT * From coachSessionDetails")
			items = c.fetchall()

			for SessionDates in items:
				if (value == SessionDates[3]):
					date_label.config(fg='red')
					messagebox.showinfo('Validation Error', 'There is already a coaching session on ' + str(value) + '. There can only be one coaching session per day', icon='error')
					return False
				else:
					pass


			label.config(fg="SpringGreen3")
			return True


		# Courts selected will change background colour to SpringGreen3 or black
		def ClickedCourt(courtvalue):
			if (courtvalue.cget('bg') == 'black'):
				courtvalue.config(bg='SpringGreen3')
			else:
				courtvalue.config(bg='black')


		# Removes the ability to resize all tree views
		def treeviewresizedisable(treeview, event):
			if treeview.identify_region(event.x, event.y) == "separator":
				return "break"


		# Returns the photo based on the member's chose of competition selected
		def ConvertPic():
			if RacquetType_combobox.get() == 'Badminton':
				filename = self.filepath + '\\_databases_images_doc\\Images\\Badmintonblob.png'
				with open(filename, 'rb') as file:
					photo = file.read()
				return photo

			if RacquetType_combobox.get() == 'Tennis':
				filename = self.filepath + '\\_databases_images_doc\\Images\\Tennisblob.png'
				with open(filename, 'rb') as file:
					photo = file.read()
				return photo

			if RacquetType_combobox.get() == 'Squash':
				filename = self.filepath + '\\_databases_images_doc\\Images\\Squashblob.png'
				with open(filename, 'rb') as file:
					photo = file.read()
				return photo


		# Clears member booking tree view data
		def clearTv():
			record=member_booking_Tv.get_children()
			for elements in record:
				member_booking_Tv.delete(elements)


		# Member Booking tree view populate
		def BookingPopulate():
			clearTv()

			conn = sqlite3.connect(self.filepath + '\\_databases_images_doc\\Databases\\LisburnRacquetsDatabase.db')
			c = conn.cursor()

			c.execute("SELECT * From MemberBooking")
			items = c.fetchall()
			conn.commit()
			conn.close()

			count=0
			for row in items:
				if row == []:
					pass
				else:
					if count%2==0:
						member_booking_Tv.insert('','end', text=row[1], values=(row[2],row[3],row[4],row[5]))
					else:
						member_booking_Tv.insert('','end', text=row[1], values=(row[2],row[3],row[4],row[5]))
					count+=1


		# If you double click a certain user, an image of that user's selected sport will be presented within a canvas below the tree view
		def GetInformation(imageviewer2, event):
			conn = sqlite3.connect(self.filepath + '\\_databases_images_doc\\Databases\\LisburnRacquetsDatabase.db')
			c = conn.cursor()

			items = member_booking_Tv.selection()
			memberdata = []

			for i in items:
				memberdata.append(member_booking_Tv.item(i)['values'])

			if len(memberdata) > 0:
				imageviewer2.place_forget()

				c.execute(f"SELECT image FROM MemberBooking WHERE bookingID=?", (memberdata[0][3],))
				data = c.fetchone()

				render = Image.open(BytesIO(data[0]))
				newimage = ImageTk.PhotoImage(render)
				imageviewer = Button(self.booking, width=95, height=95, borderwidth=0, activebackground="white", bd=3)
				imageviewer.place(rely=0.433,relx=0.76,anchor=CENTER)
				imageviewer.config(image=newimage)
				imageviewer['command'] = 0
				imageviewer['relief'] = 'sunken'
				imageviewer.image = newimage


		# Presents a different no. courts based on the users chose between: badminton, tennis and squash
		def RacquetSportSelect(badminton1, badminton2, badminton3, badminton4, badminton5, badminton6, badminton7, badminton8, badminton9, badminton10, badminton11, badminton12, tennis1, tennis2, tennis3, tennis4, squash1, squash2, badminton1l, badminton2l, badminton3l, badminton4l, badminton5l, badminton6l, badminton7l, badminton8l, badminton9l, badminton10l, badminton11l, badminton12l, tennis1l, tennis2l, tennis3l, tennis4l, squash1l, squash2l):
			if RacquetType_combobox.get() == 'Badminton' and self.previous == '':
				self.previous = 'Badminton'

				BadmintonFloorPlanPhoto = PhotoImage(file=self.filepath + '\\_databases_images_doc\\Images\\badmintonRacquetsFloor.png')

				BadmintonFloorPlan = Button(self.booking, image=BadmintonFloorPlanPhoto, width=350, height=292, borderwidth=0, activebackground="white")
				BadmintonFloorPlan.place(rely=0.75,relx=0.76,anchor=CENTER)
				BadmintonFloorPlan.image = BadmintonFloorPlanPhoto
				BadmintonFloorPlan['command'] = 0
				BadmintonFloorPlan['relief'] = 'sunken'


				badminton1.place(rely=0.48,relx=0.09,anchor=CENTER)
				badminton1l.place(rely=0.42,relx=0.09,anchor=CENTER)

				badminton2.place(rely=0.48,relx=0.21,anchor=CENTER)
				badminton2l.place(rely=0.42,relx=0.21,anchor=CENTER)

				badminton3.place(rely=0.48,relx=0.33,anchor=CENTER)
				badminton3l.place(rely=0.42,relx=0.33,anchor=CENTER)

				badminton4.place(rely=0.48,relx=0.45,anchor=CENTER)
				badminton4l.place(rely=0.42,relx=0.45,anchor=CENTER)

				badminton5.place(rely=0.66,relx=0.09,anchor=CENTER)
				badminton5l.place(rely=0.6,relx=0.09,anchor=CENTER)

				badminton6.place(rely=0.66,relx=0.21,anchor=CENTER)
				badminton6l.place(rely=0.6,relx=0.21,anchor=CENTER)

				badminton7.place(rely=0.66,relx=0.33,anchor=CENTER)
				badminton7l.place(rely=0.6,relx=0.33,anchor=CENTER)

				badminton8.place(rely=0.66,relx=0.45,anchor=CENTER)
				badminton8l.place(rely=0.6,relx=0.45,anchor=CENTER)

				badminton9.place(rely=0.84,relx=0.09,anchor=CENTER)
				badminton9l.place(rely=0.78,relx=0.09,anchor=CENTER)

				badminton10.place(rely=0.84,relx=0.21,anchor=CENTER)
				badminton10l.place(rely=0.78,relx=0.21,anchor=CENTER)

				badminton11.place(rely=0.84,relx=0.33,anchor=CENTER)
				badminton11l.place(rely=0.78,relx=0.33,anchor=CENTER)

				badminton12.place(rely=0.84,relx=0.45,anchor=CENTER)
				badminton12l.place(rely=0.78,relx=0.45,anchor=CENTER)


			if RacquetType_combobox.get() == 'Tennis' and self.previous == '':
				self.previous = 'Tennis'

				TennisFloorPlanPhoto = PhotoImage(file=self.filepath + '\\_databases_images_doc\\Images\\tennisRacquetsFloor.png')

				TennisFloorPlan = Button(self.booking, image=TennisFloorPlanPhoto, width=350, height=292, borderwidth=0, activebackground="white")
				TennisFloorPlan.place(rely=0.75,relx=0.76,anchor=CENTER)
				TennisFloorPlan.image = TennisFloorPlanPhoto
				TennisFloorPlan['command'] = 0
				TennisFloorPlan['relief'] = 'sunken'


				tennis1.place(rely=0.54,relx=0.15,anchor=CENTER)
				tennis1l.place(rely=0.44,relx=0.15,anchor=CENTER)

				tennis2.place(rely=0.54,relx=0.39,anchor=CENTER)
				tennis2l.place(rely=0.44,relx=0.39,anchor=CENTER)

				tennis3.place(rely=0.78,relx=0.15,anchor=CENTER)
				tennis3l.place(rely=0.68,relx=0.15,anchor=CENTER)

				tennis4.place(rely=0.78,relx=0.39,anchor=CENTER)
				tennis4l.place(rely=0.68,relx=0.39,anchor=CENTER)


			if RacquetType_combobox.get() == 'Squash' and self.previous == '':
				self.previous = 'Squash'

				SquashFloorPlanPhoto = PhotoImage(file=self.filepath + '\\_databases_images_doc\\Images\\squashRacquetsFloor.png')

				SquashFloorPlan = Button(self.booking, image=SquashFloorPlanPhoto, width=350, height=292, borderwidth=0, activebackground="white")
				SquashFloorPlan.place(rely=0.75,relx=0.76,anchor=CENTER)
				SquashFloorPlan.image = SquashFloorPlanPhoto
				SquashFloorPlan['command'] = 0
				SquashFloorPlan['relief'] = 'sunken'


				squash1.place(rely=0.67,relx=0.15,anchor=CENTER)
				squash1l.place(rely=0.44,relx=0.15,anchor=CENTER)

				squash2.place(rely=0.67,relx=0.39,anchor=CENTER)
				squash2l.place(rely=0.44,relx=0.39,anchor=CENTER)


			if RacquetType_combobox.get() == 'Badminton' and self.previous == 'Badminton':
				pass


			if RacquetType_combobox.get() == 'Badminton' and self.previous == 'Tennis':
				self.previous = 'Badminton'

				BadmintonFloorPlanPhoto = PhotoImage(file=self.filepath + '\\_databases_images_doc\\Images\\badmintonRacquetsFloor.png')

				BadmintonFloorPlan = Button(self.booking, image=BadmintonFloorPlanPhoto, width=350, height=292, borderwidth=0, activebackground="white")
				BadmintonFloorPlan.place(rely=0.75,relx=0.76,anchor=CENTER)
				BadmintonFloorPlan.image = BadmintonFloorPlanPhoto
				BadmintonFloorPlan['command'] = 0
				BadmintonFloorPlan['relief'] = 'sunken'


				tennis1.config(bg='black')
				tennis2.config(bg='black')
				tennis3.config(bg='black')
				tennis4.config(bg='black')

				tennis1.place_forget()
				tennis1l.place_forget()
				tennis2.place_forget()
				tennis2l.place_forget()
				tennis3.place_forget()
				tennis3l.place_forget()
				tennis4.place_forget()
				tennis4l.place_forget()


				badminton1.place(rely=0.48,relx=0.09,anchor=CENTER)
				badminton1l.place(rely=0.42,relx=0.09,anchor=CENTER)

				badminton2.place(rely=0.48,relx=0.21,anchor=CENTER)
				badminton2l.place(rely=0.42,relx=0.21,anchor=CENTER)

				badminton3.place(rely=0.48,relx=0.33,anchor=CENTER)
				badminton3l.place(rely=0.42,relx=0.33,anchor=CENTER)

				badminton4.place(rely=0.48,relx=0.45,anchor=CENTER)
				badminton4l.place(rely=0.42,relx=0.45,anchor=CENTER)

				badminton5.place(rely=0.66,relx=0.09,anchor=CENTER)
				badminton5l.place(rely=0.6,relx=0.09,anchor=CENTER)

				badminton6.place(rely=0.66,relx=0.21,anchor=CENTER)
				badminton6l.place(rely=0.6,relx=0.21,anchor=CENTER)

				badminton7.place(rely=0.66,relx=0.33,anchor=CENTER)
				badminton7l.place(rely=0.6,relx=0.33,anchor=CENTER)

				badminton8.place(rely=0.66,relx=0.45,anchor=CENTER)
				badminton8l.place(rely=0.6,relx=0.45,anchor=CENTER)

				badminton9.place(rely=0.84,relx=0.09,anchor=CENTER)
				badminton9l.place(rely=0.78,relx=0.09,anchor=CENTER)

				badminton10.place(rely=0.84,relx=0.21,anchor=CENTER)
				badminton10l.place(rely=0.78,relx=0.21,anchor=CENTER)

				badminton11.place(rely=0.84,relx=0.33,anchor=CENTER)
				badminton11l.place(rely=0.78,relx=0.33,anchor=CENTER)

				badminton12.place(rely=0.84,relx=0.45,anchor=CENTER)
				badminton12l.place(rely=0.78,relx=0.45,anchor=CENTER)


			if RacquetType_combobox.get() == 'Badminton' and self.previous == 'Squash':
				self.previous = 'Badminton'

				BadmintonFloorPlanPhoto = PhotoImage(file=self.filepath + '\\_databases_images_doc\\Images\\badmintonRacquetsFloor.png')

				BadmintonFloorPlan = Button(self.booking, image=BadmintonFloorPlanPhoto, width=350, height=292, borderwidth=0, activebackground="white")
				BadmintonFloorPlan.place(rely=0.75,relx=0.76,anchor=CENTER)
				BadmintonFloorPlan.image = BadmintonFloorPlanPhoto
				BadmintonFloorPlan['command'] = 0
				BadmintonFloorPlan['relief'] = 'sunken'


				squash1.config(bg='black')
				squash2.config(bg='black')

				squash1.place_forget()
				squash1l.place_forget()
				squash2.place_forget()
				squash2l.place_forget()


				badminton1.place(rely=0.48,relx=0.09,anchor=CENTER)
				badminton1l.place(rely=0.42,relx=0.09,anchor=CENTER)

				badminton2.place(rely=0.48,relx=0.21,anchor=CENTER)
				badminton2l.place(rely=0.42,relx=0.21,anchor=CENTER)

				badminton3.place(rely=0.48,relx=0.33,anchor=CENTER)
				badminton3l.place(rely=0.42,relx=0.33,anchor=CENTER)

				badminton4.place(rely=0.48,relx=0.45,anchor=CENTER)
				badminton4l.place(rely=0.42,relx=0.45,anchor=CENTER)

				badminton5.place(rely=0.66,relx=0.09,anchor=CENTER)
				badminton5l.place(rely=0.6,relx=0.09,anchor=CENTER)

				badminton6.place(rely=0.66,relx=0.21,anchor=CENTER)
				badminton6l.place(rely=0.6,relx=0.21,anchor=CENTER)

				badminton7.place(rely=0.66,relx=0.33,anchor=CENTER)
				badminton7l.place(rely=0.6,relx=0.33,anchor=CENTER)

				badminton8.place(rely=0.66,relx=0.45,anchor=CENTER)
				badminton8l.place(rely=0.6,relx=0.45,anchor=CENTER)

				badminton9.place(rely=0.84,relx=0.09,anchor=CENTER)
				badminton9l.place(rely=0.78,relx=0.09,anchor=CENTER)

				badminton10.place(rely=0.84,relx=0.21,anchor=CENTER)
				badminton10l.place(rely=0.78,relx=0.21,anchor=CENTER)

				badminton11.place(rely=0.84,relx=0.33,anchor=CENTER)
				badminton11l.place(rely=0.78,relx=0.33,anchor=CENTER)

				badminton12.place(rely=0.84,relx=0.45,anchor=CENTER)
				badminton12l.place(rely=0.78,relx=0.45,anchor=CENTER)


			if RacquetType_combobox.get() == 'Tennis' and self.previous == 'Tennis':
				pass


			if RacquetType_combobox.get() == 'Tennis' and self.previous == 'Badminton':
				self.previous = 'Tennis'

				TennisFloorPlanPhoto = PhotoImage(file=self.filepath + '\\_databases_images_doc\\Images\\tennisRacquetsFloor.png')

				TennisFloorPlan = Button(self.booking, image=TennisFloorPlanPhoto, width=350, height=292, borderwidth=0, activebackground="white")
				TennisFloorPlan.place(rely=0.75,relx=0.76,anchor=CENTER)
				TennisFloorPlan.image = TennisFloorPlanPhoto
				TennisFloorPlan['command'] = 0
				TennisFloorPlan['relief'] = 'sunken'


				badminton1.config(bg='black')
				badminton2.config(bg='black')
				badminton3.config(bg='black')
				badminton4.config(bg='black')
				badminton5.config(bg='black')
				badminton6.config(bg='black')
				badminton7.config(bg='black')
				badminton8.config(bg='black')
				badminton9.config(bg='black')
				badminton10.config(bg='black')
				badminton11.config(bg='black')
				badminton12.config(bg='black')

				badminton1.place_forget()
				badminton1l.place_forget()
				badminton2.place_forget()
				badminton2l.place_forget()
				badminton3.place_forget()
				badminton3l.place_forget()
				badminton4.place_forget()
				badminton4l.place_forget()
				badminton5.place_forget()
				badminton5l.place_forget()
				badminton6.place_forget()
				badminton6l.place_forget()
				badminton7.place_forget()
				badminton7l.place_forget()
				badminton8.place_forget()
				badminton8l.place_forget()
				badminton9.place_forget()
				badminton9l.place_forget()
				badminton10.place_forget()
				badminton10l.place_forget()
				badminton11.place_forget()
				badminton11l.place_forget()
				badminton12.place_forget()
				badminton12l.place_forget()


				tennis1.place(rely=0.54,relx=0.15,anchor=CENTER)
				tennis1l.place(rely=0.44,relx=0.15,anchor=CENTER)

				tennis2.place(rely=0.54,relx=0.39,anchor=CENTER)
				tennis2l.place(rely=0.44,relx=0.39,anchor=CENTER)

				tennis3.place(rely=0.78,relx=0.15,anchor=CENTER)
				tennis3l.place(rely=0.68,relx=0.15,anchor=CENTER)

				tennis4.place(rely=0.78,relx=0.39,anchor=CENTER)
				tennis4l.place(rely=0.68,relx=0.39,anchor=CENTER)


			if RacquetType_combobox.get() == 'Tennis' and self.previous == 'Squash':
				self.previous = 'Tennis'

				TennisFloorPlanPhoto = PhotoImage(file=self.filepath + '\\_databases_images_doc\\Images\\tennisRacquetsFloor.png')

				TennisFloorPlan = Button(self.booking, image=TennisFloorPlanPhoto, width=350, height=292, borderwidth=0, activebackground="white")
				TennisFloorPlan.place(rely=0.75,relx=0.76,anchor=CENTER)
				TennisFloorPlan.image = TennisFloorPlanPhoto
				TennisFloorPlan['command'] = 0
				TennisFloorPlan['relief'] = 'sunken'


				squash1.config(bg='black')
				squash2.config(bg='black')

				squash1.place_forget()
				squash1l.place_forget()
				squash2.place_forget()
				squash2l.place_forget()


				tennis1.place(rely=0.54,relx=0.15,anchor=CENTER)
				tennis1l.place(rely=0.44,relx=0.15,anchor=CENTER)

				tennis2.place(rely=0.54,relx=0.39,anchor=CENTER)
				tennis2l.place(rely=0.44,relx=0.39,anchor=CENTER)

				tennis3.place(rely=0.78,relx=0.15,anchor=CENTER)
				tennis3l.place(rely=0.68,relx=0.15,anchor=CENTER)

				tennis4.place(rely=0.78,relx=0.39,anchor=CENTER)
				tennis4l.place(rely=0.68,relx=0.39,anchor=CENTER)


			if RacquetType_combobox.get() == 'Squash' and self.previous == 'Squash':
				pass


			if RacquetType_combobox.get() == 'Squash' and self.previous == 'Badminton':
				self.previous = 'Squash'

				SquashFloorPlanPhoto = PhotoImage(file=self.filepath + '\\_databases_images_doc\\Images\\squashRacquetsFloor.png')

				SquashFloorPlan = Button(self.booking, image=SquashFloorPlanPhoto, width=350, height=292, borderwidth=0, activebackground="white")
				SquashFloorPlan.place(rely=0.75,relx=0.76,anchor=CENTER)
				SquashFloorPlan.image = SquashFloorPlanPhoto
				SquashFloorPlan['command'] = 0
				SquashFloorPlan['relief'] = 'sunken'


				badminton1.config(bg='black')
				badminton2.config(bg='black')
				badminton3.config(bg='black')
				badminton4.config(bg='black')
				badminton5.config(bg='black')
				badminton6.config(bg='black')
				badminton7.config(bg='black')
				badminton8.config(bg='black')
				badminton9.config(bg='black')
				badminton10.config(bg='black')
				badminton11.config(bg='black')
				badminton12.config(bg='black')

				badminton1.place_forget()
				badminton1l.place_forget()
				badminton2.place_forget()
				badminton2l.place_forget()
				badminton3.place_forget()
				badminton3l.place_forget()
				badminton4.place_forget()
				badminton4l.place_forget()
				badminton5.place_forget()
				badminton5l.place_forget()
				badminton6.place_forget()
				badminton6l.place_forget()
				badminton7.place_forget()
				badminton7l.place_forget()
				badminton8.place_forget()
				badminton8l.place_forget()
				badminton9.place_forget()
				badminton9l.place_forget()
				badminton10.place_forget()
				badminton10l.place_forget()
				badminton11.place_forget()
				badminton11l.place_forget()
				badminton12.place_forget()
				badminton12l.place_forget()


				squash1.place(rely=0.67,relx=0.15,anchor=CENTER)
				squash1l.place(rely=0.44,relx=0.15,anchor=CENTER)

				squash2.place(rely=0.67,relx=0.39,anchor=CENTER)
				squash2l.place(rely=0.44,relx=0.39,anchor=CENTER)


			if RacquetType_combobox.get() == 'Squash' and self.previous == 'Tennis':
				self.previous = 'Squash'

				SquashFloorPlanPhoto = PhotoImage(file=self.filepath + '\\_databases_images_doc\\Images\\squashRacquetsFloor.png')

				SquashFloorPlan = Button(self.booking, image=SquashFloorPlanPhoto, width=350, height=292, borderwidth=0, activebackground="white")
				SquashFloorPlan.place(rely=0.75,relx=0.76,anchor=CENTER)
				SquashFloorPlan.image = SquashFloorPlanPhoto
				SquashFloorPlan['command'] = 0
				SquashFloorPlan['relief'] = 'sunken'


				tennis1.config(bg='black')
				tennis2.config(bg='black')
				tennis3.config(bg='black')
				tennis4.config(bg='black')

				tennis1.place_forget()
				tennis1l.place_forget()
				tennis2.place_forget()
				tennis2l.place_forget()
				tennis3.place_forget()
				tennis3l.place_forget()
				tennis4.place_forget()
				tennis4l.place_forget()


				squash1.place(rely=0.67,relx=0.15,anchor=CENTER)
				squash1l.place(rely=0.44,relx=0.15,anchor=CENTER)

				squash2.place(rely=0.67,relx=0.39,anchor=CENTER)
				squash2l.place(rely=0.44,relx=0.39,anchor=CENTER)


		# Ensures court entered conforms to the rules
		def validate_courts(badminton1, badminton2, badminton3, badminton4, badminton5, badminton6, badminton7, badminton8, badminton9, badminton10, badminton11, badminton12, tennis1, tennis2, tennis3, tennis4, squash1, squash2, racquet_sport_label):
			if RacquetType_combobox.get() == 'Badminton':
				badmintoncounter = 1
				badmintonselectedcourts = []

				badmintoncourts = [badminton1, badminton2, badminton3, badminton4, badminton5, badminton6,
								   badminton7, badminton8, badminton9, badminton10, badminton11, badminton12]

				if (badminton1.cget('bg') != 'SpringGreen3' and badminton2.cget('bg') != 'SpringGreen3' and badminton3.cget('bg') != 'SpringGreen3' and badminton4.cget('bg') != 'SpringGreen3' and badminton5.cget('bg') != 'SpringGreen3' and badminton6.cget('bg') != 'SpringGreen3' and badminton7.cget('bg') != 'SpringGreen3' and badminton8.cget('bg') != 'SpringGreen3' and badminton9.cget('bg') != 'SpringGreen3' and badminton10.cget('bg') != 'SpringGreen3' and badminton11.cget('bg') != 'SpringGreen3' and badminton12.cget('bg') != 'SpringGreen3'):
					racquet_sport_label.config(fg='red')
					messagebox.showinfo('Error', 'Please select a court', icon='error')

				else:

					for court in badmintoncourts:
						if (str(badmintoncounter) == court.cget('text') and court.cget('bg') == 'SpringGreen3'):
							FinalCourt = str(badmintoncounter)
							badmintonselectedcourts.append(FinalCourt)

						badmintoncounter += 1

					if (len(badmintonselectedcourts) > 1):
						racquet_sport_label.config(fg='red')
						messagebox.showinfo('Info', 'Only one court can be selected per booking')
						badminton1.config(bg='black')
						badminton2.config(bg='black')
						badminton3.config(bg='black')
						badminton4.config(bg='black')
						badminton5.config(bg='black')
						badminton6.config(bg='black')
						badminton7.config(bg='black')
						badminton8.config(bg='black')
						badminton9.config(bg='black')
						badminton10.config(bg='black')
						badminton11.config(bg='black')
						badminton12.config(bg='black')

					else:
						self.courts = True
						racquet_sport_label.config(fg='SpringGreen3')
						return badmintonselectedcourts[0]

			if RacquetType_combobox.get() == 'Tennis':
				tenniscounter = 1
				tennisselectedcourts = []

				tenniscourts = [tennis1, tennis2, tennis3, tennis4]

				if (tennis1.cget('bg') != 'SpringGreen3' and tennis2.cget('bg') != 'SpringGreen3' and tennis3.cget('bg') != 'SpringGreen3' and tennis4.cget('bg') != 'SpringGreen3'):
					racquet_sport_label.config(fg='red')
					messagebox.showinfo('Error', 'Please select a court', icon='error')

				else:

					for court in tenniscourts:
						if (str(tenniscounter) == court.cget('text') and court.cget('bg') == 'SpringGreen3'):
							FinalCourt = str(tenniscounter)
							tennisselectedcourts.append(FinalCourt)

						tenniscounter += 1

					if (len(tennisselectedcourts) > 1):
						racquet_sport_label.config(fg='red')
						messagebox.showinfo('Info', 'Only one court can be selected per booking')
						tennis1.config(bg='black')
						tennis2.config(bg='black')
						tennis3.config(bg='black')
						tennis4.config(bg='black')

					else:
						self.courts = True
						racquet_sport_label.config(fg='SpringGreen3')
						return tennisselectedcourts[0]

			if RacquetType_combobox.get() == 'Squash':
				squashcounter = 1
				squashselectedcourts = []

				squashcourts = [squash1, squash2]

				if (squash1.cget('bg') != 'SpringGreen3' and squash2.cget('bg') != 'SpringGreen3'):
					racquet_sport_label.config(fg='red')
					messagebox.showinfo('Error', 'Please select a court', icon='error')

				else:

					for court in squashcourts:
						if (str(squashcounter) == court.cget('text') and court.cget('bg') == 'SpringGreen3'):
							FinalCourt = str(squashcounter)
							squashselectedcourts.append(FinalCourt)

						squashcounter += 1

					if (len(squashselectedcourts) > 1):
						racquet_sport_label.config(fg='red')
						messagebox.showinfo('Info', 'Only one court can be selected per booking')
						squash1.config(bg='black')
						squash2.config(bg='black')

					else:
						self.courts = True
						racquet_sport_label.config(fg='SpringGreen3')
						return squashselectedcourts[0]


		# Submits member booking
		# Will generate a document containing all details stored about the member
		# This will subsequently be sent to the member who made the booking
		def SubmitBooking(badminton1, badminton2, badminton3, badminton4, badminton5, badminton6, badminton7, badminton8, badminton9, badminton10, badminton11, badminton12, tennis1, tennis2, tennis3, tennis4, squash1, squash2, badminton1l, badminton2l, badminton3l, badminton4l, badminton5l, badminton6l, badminton7l, badminton8l, badminton9l, badminton10l, badminton11l, badminton12l, tennis1l, tennis2l, tennis3l, tennis4l, squash1l, squash2l, floorplan):

			conn = sqlite3.connect(self.filepath + '\\_databases_images_doc\\Databases\\LisburnRacquetsDatabase.db')
			c = conn.cursor()

			isValid = True
			isValid = isValid and validate_username(self.memberNamesAndPasswords.get(), username_label)
			isValid = isValid and validate_date(eventDate.get(), date_label)

			if isValid:
				courtnumber = validate_courts(badminton1, badminton2, badminton3, badminton4, badminton5, badminton6, badminton7, badminton8, badminton9, badminton10, badminton11, badminton12, tennis1, tennis2, tennis3, tennis4, squash1, squash2, racquet_sport_label)

			if isValid == True and self.courts == True:
				c.execute("SELECT * FROM MemberBooking")
				row = c.fetchall()

				finalusername = self.memberNamesAndPasswords.get()
				finaltype = RacquetType_combobox.get()
				finaldate = eventDate.get()
				finalimage = ConvertPic()
				finalID = len(row)+1

				response = askyesno("Question", "Are you sure that all information above is correct?", icon='question')
				if response == False:
					showinfo("Info", "submition cancelled", icon='info')

				else:
					found = BookingEmail("Member Booking Successful", "The booking you have just made has been successfully stored within the Lisburn Racquets Club system" + "\n\n" + "The details of the booking have been listed below:" + "\n" + "Date: " + finaldate + "\n" + "Court No: " + courtnumber + "\n" + "Racquet Sport: " + finaltype + " (Shown in image attached)" + "\n\n" + "Thanks for choosing Lisburn Racquets Club", finalusername, username_label, RacquetType_combobox.get())
					if found:

						c.execute("INSERT INTO MemberBooking VALUES (:image, :username, :type, :date, :court, :bookingID)",
								  {
									  'image': finalimage,
									  'username': finalusername,
									  'type': finaltype,
									  'date': finaldate,
									  'court': courtnumber,
									  'bookingID': finalID,
								  })

						c.execute("INSERT INTO fees VALUES (:username, :coachingsessionfee, :memberbookingfee)",
								  {
									  'username': finalusername,
									  'coachingsessionfee': '',
									  'memberbookingfee': '£3.00',
								  })

						conn.commit()
						conn.close()

						self.memberNamesAndPasswords.set('')

						if RacquetType_combobox.get() == 'Badminton':
							badminton1.place_forget()
							badminton1l.place_forget()
							badminton2.place_forget()
							badminton2l.place_forget()
							badminton3.place_forget()
							badminton3l.place_forget()
							badminton4.place_forget()
							badminton4l.place_forget()
							badminton5.place_forget()
							badminton5l.place_forget()
							badminton6.place_forget()
							badminton6l.place_forget()
							badminton7.place_forget()
							badminton7l.place_forget()
							badminton8.place_forget()
							badminton8l.place_forget()
							badminton9.place_forget()
							badminton9l.place_forget()
							badminton10.place_forget()
							badminton10l.place_forget()
							badminton11.place_forget()
							badminton11l.place_forget()
							badminton12.place_forget()
							badminton12l.place_forget()

						if RacquetType_combobox.get() == 'Tennis':
							tennis1.place_forget()
							tennis1l.place_forget()
							tennis2.place_forget()
							tennis2l.place_forget()
							tennis3.place_forget()
							tennis3l.place_forget()
							tennis4.place_forget()
							tennis4l.place_forget()

						if RacquetType_combobox.get() == 'Squash':
							squash1.place_forget()
							squash1l.place_forget()
							squash2.place_forget()
							squash2l.place_forget()

						RacquetType_combobox.set('Badminton')
						floorplan.place(rely=0.75,relx=0.76,anchor=CENTER)

						username_label.config(fg='black')
						date_label.config(fg='black')
						racquet_sport_label.config(fg='black')

						BookingPopulate()


		# Variables Used
		eventDate=StringVar()
		court = StringVar()

		RacqutType = ['Badminton','Tennis','Squash']


		ToolTips = Pmw.Balloon()


		# Tkinter labels, entry boxes, buttons, tree views, etc.
		username_label = tkinter.Label(self.booking, text="Username:", font=('serif', 14, 'bold'), fg='black', bg='white')
		username_label.place(rely=0.15, relx=0.1, anchor='center')

		date_label = tkinter.Label(self.booking, text="Booking Date:", font=('serif', 14, 'bold'), fg='black', bg='white')
		date_label.place(rely=0.24, relx=0.1, anchor='center')

		date_entry = Button(self.booking, text='Select Date',font=("serif",10, 'bold'), cursor="tcross",command=lambda : dateEntryCheck(eventDate), padx=10, bd=4, relief="ridge")
		date_entry.place(rely=0.243, relx=0.27, anchor='center')
		ToolTips.bind(date_entry, 'Select the date of the booking')

		racquet_sport_label = tkinter.Label(self.booking, text="Racquet Sport:", font=('serif', 14, 'bold'), fg='black', bg='white')
		racquet_sport_label.place(rely=0.33, relx=0.1, anchor='center')

		RacquetType_combobox = ttk.Combobox(self.booking, value=RacqutType, font=('serif', 11, 'bold'), width=11)
		RacquetType_combobox.place(rely=0.333, relx=0.27, anchor='center')
		RacquetType_combobox.current(0)
		RacquetType_combobox.config(state="readonly")


		BlankFloorPlanPhoto = PhotoImage(file=self.filepath + '\\_databases_images_doc\\Images\\blankRacquetsFloor.png')

		BlankFloorPlan = Button(self.booking, image=BlankFloorPlanPhoto, width=350, height=292, borderwidth=0, activebackground="white")
		BlankFloorPlan.place(rely=0.75,relx=0.76,anchor=CENTER)
		BlankFloorPlan.image = BlankFloorPlanPhoto
		BlankFloorPlan['command'] = 0
		BlankFloorPlan['relief'] = 'sunken'


		box =Label(self.booking, text = "blank", fg ='white',bg='white',font=('serif',8,'bold'), bd=2, relief="sunken", padx=230, pady=160)
		box.place(rely=0.65,relx=0.27,anchor=CENTER)



		CourtsImage = PhotoImage(file=self.filepath + '\\_databases_images_doc\\Images\\courts.png')
		CourtsImage2 = PhotoImage(file=self.filepath + '\\_databases_images_doc\\Images\\bigcourts.png')
		CourtsImage3 = PhotoImage(file=self.filepath + '\\_databases_images_doc\\Images\\biggestcourts.png')


		badmintonCourt1label =Label(self.booking, text = 'Court 1', fg ='black',bg='white',font=('serif',7,'bold'), bd=2, relief="ridge", padx=10, pady=3)
		badmintonCourt1label.place(rely=0.42,relx=0.09,anchor=CENTER)
		badmintonCourt1Button = Button(self.booking, text='1', cursor="tcross", image=CourtsImage, width=95, height=53, command=lambda : ClickedCourt(badmintonCourt1Button), bg="black", highlightthickness=4, activebackground="grey")
		badmintonCourt1Button.place(rely=0.48,relx=0.09,anchor=CENTER)
		badmintonCourt1Button.image = CourtsImage

		badmintonCourt2label =Label(self.booking, text = 'Court 2', fg ='black',bg='white',font=('serif',7,'bold'), bd=2, relief="ridge", padx=10, pady=3)
		badmintonCourt2label.place(rely=0.42,relx=0.21,anchor=CENTER)
		badmintonCourt2Button = Button(self.booking, text='2', cursor="tcross", image=CourtsImage, width=95, height=53, command=lambda : ClickedCourt(badmintonCourt2Button), bg="black", highlightthickness=4, activebackground="grey")
		badmintonCourt2Button.place(rely=0.48,relx=0.21,anchor=CENTER)
		badmintonCourt2Button.image = CourtsImage

		badmintonCourt3label =Label(self.booking, text = 'Court 3', fg ='black',bg='white',font=('serif',7,'bold'), bd=2, relief="ridge", padx=10, pady=3)
		badmintonCourt3label.place(rely=0.42,relx=0.33,anchor=CENTER)
		badmintonCourt3Button = Button(self.booking, text='3', cursor="tcross", image=CourtsImage, width=95, height=53, command=lambda : ClickedCourt(badmintonCourt3Button), bg="black", highlightthickness=4, activebackground="grey")
		badmintonCourt3Button.place(rely=0.48,relx=0.33,anchor=CENTER)
		badmintonCourt3Button.image = CourtsImage

		badmintonCourt4label =Label(self.booking, text = 'Court 4', fg ='black',bg='white',font=('serif',7,'bold'), bd=2, relief="ridge", padx=10, pady=3)
		badmintonCourt4label.place(rely=0.42,relx=0.45,anchor=CENTER)
		badmintonCourt4Button = Button(self.booking, text='4', cursor="tcross", image=CourtsImage, width=95, height=53, command=lambda : ClickedCourt(badmintonCourt4Button), bg="black", highlightthickness=4, activebackground="grey")
		badmintonCourt4Button.place(rely=0.48,relx=0.45,anchor=CENTER)
		badmintonCourt4Button.image = CourtsImage

		badmintonCourt5label =Label(self.booking, text = 'Court 5', fg ='black',bg='white',font=('serif',7,'bold'), bd=2, relief="ridge", padx=10, pady=3)
		badmintonCourt5label.place(rely=0.6,relx=0.09,anchor=CENTER)
		badmintonCourt5Button = Button(self.booking, text='5', cursor="tcross", image=CourtsImage, width=95, height=53, command=lambda : ClickedCourt(badmintonCourt5Button), bg="black", highlightthickness=5, activebackground="grey")
		badmintonCourt5Button.place(rely=0.66,relx=0.09,anchor=CENTER)
		badmintonCourt5Button.image = CourtsImage

		badmintonCourt6label =Label(self.booking, text = 'Court 6', fg ='black',bg='white',font=('serif',7,'bold'), bd=2, relief="ridge", padx=10, pady=3)
		badmintonCourt6label.place(rely=0.6,relx=0.21,anchor=CENTER)
		badmintonCourt6Button = Button(self.booking, text='6', cursor="tcross", image=CourtsImage, width=95, height=53, command=lambda : ClickedCourt(badmintonCourt6Button), bg="black", highlightthickness=5, activebackground="grey")
		badmintonCourt6Button.place(rely=0.66,relx=0.21,anchor=CENTER)
		badmintonCourt6Button.image = CourtsImage

		badmintonCourt7label =Label(self.booking, text = 'Court 7', fg ='black',bg='white',font=('serif',7,'bold'), bd=2, relief="ridge", padx=10, pady=3)
		badmintonCourt7label.place(rely=0.6,relx=0.33,anchor=CENTER)
		badmintonCourt7Button = Button(self.booking, text='7', cursor="tcross", image=CourtsImage, width=95, height=53, command=lambda : ClickedCourt(badmintonCourt7Button), bg="black", highlightthickness=5, activebackground="grey")
		badmintonCourt7Button.place(rely=0.66,relx=0.33,anchor=CENTER)
		badmintonCourt7Button.image = CourtsImage

		badmintonCourt8label =Label(self.booking, text = 'Court 8', fg ='black',bg='white',font=('serif',7,'bold'), bd=2, relief="ridge", padx=10, pady=3)
		badmintonCourt8label.place(rely=0.6,relx=0.45,anchor=CENTER)
		badmintonCourt8Button = Button(self.booking, text='8', cursor="tcross", image=CourtsImage, width=95, height=53, command=lambda : ClickedCourt(badmintonCourt8Button), bg="black", highlightthickness=5, activebackground="grey")
		badmintonCourt8Button.place(rely=0.66,relx=0.45,anchor=CENTER)
		badmintonCourt8Button.image = CourtsImage

		badmintonCourt9label =Label(self.booking, text = 'Court 9', fg ='black',bg='white',font=('serif',7,'bold'), bd=2, relief="ridge", padx=10, pady=3)
		badmintonCourt9label.place(rely=0.78,relx=0.09,anchor=CENTER)
		badmintonCourt9Button = Button(self.booking, text='9', cursor="tcross", image=CourtsImage, width=95, height=53, command=lambda : ClickedCourt(badmintonCourt9Button), bg="black", highlightthickness=5, activebackground="grey")
		badmintonCourt9Button.place(rely=0.84,relx=0.09,anchor=CENTER)
		badmintonCourt9Button.image = CourtsImage

		badmintonCourt10label =Label(self.booking, text = 'Court 10', fg ='black',bg='white',font=('serif',7,'bold'), bd=2, relief="ridge", padx=10, pady=3)
		badmintonCourt10label.place(rely=0.78,relx=0.21,anchor=CENTER)
		badmintonCourt10Button = Button(self.booking, text='10', cursor="tcross", image=CourtsImage, width=95, height=53, command=lambda : ClickedCourt(badmintonCourt10Button), bg="black", highlightthickness=5, activebackground="grey")
		badmintonCourt10Button.place(rely=0.84,relx=0.21,anchor=CENTER)
		badmintonCourt10Button.image = CourtsImage

		badmintonCourt11label =Label(self.booking, text = 'Court 11', fg ='black',bg='white',font=('serif',7,'bold'), bd=2, relief="ridge", padx=10, pady=3)
		badmintonCourt11label.place(rely=0.78,relx=0.33,anchor=CENTER)
		badmintonCourt11Button = Button(self.booking, text='11', cursor="tcross", image=CourtsImage, width=95, height=53, command=lambda : ClickedCourt(badmintonCourt11Button), bg="black", highlightthickness=5, activebackground="grey")
		badmintonCourt11Button.place(rely=0.84,relx=0.33,anchor=CENTER)
		badmintonCourt11Button.image = CourtsImage

		badmintonCourt12label =Label(self.booking, text = 'Court 12', fg ='black',bg='white',font=('serif',7,'bold'), bd=2, relief="ridge", padx=10, pady=3)
		badmintonCourt12label.place(rely=0.78,relx=0.45,anchor=CENTER)
		badmintonCourt12Button = Button(self.booking, text='12', cursor="tcross", image=CourtsImage, width=95, height=53, command=lambda : ClickedCourt(badmintonCourt12Button), bg="black", highlightthickness=5, activebackground="grey")
		badmintonCourt12Button.place(rely=0.84,relx=0.45,anchor=CENTER)
		badmintonCourt12Button.image = CourtsImage


		tennisCourt1label =Label(self.booking, text = 'Court 1', fg ='black',bg='white',font=('serif',9,'bold'), bd=2, relief="ridge", padx=10, pady=3)
		tennisCourt1label.place(rely=0.44,relx=0.15,anchor=CENTER)
		tennisCourt1Button = Button(self.booking, text='1', cursor="tcross", image=CourtsImage2, width=170, height=97, command=lambda : ClickedCourt(tennisCourt1Button), bg="black", highlightthickness=4, activebackground="grey")
		tennisCourt1Button.place(rely=0.54,relx=0.15,anchor=CENTER)
		tennisCourt1Button.image = CourtsImage2

		tennisCourt2label =Label(self.booking, text = 'Court 2', fg ='black',bg='white',font=('serif',9,'bold'), bd=2, relief="ridge", padx=10, pady=3)
		tennisCourt2label.place(rely=0.44,relx=0.39,anchor=CENTER)
		tennisCourt2Button = Button(self.booking, text='2', cursor="tcross", image=CourtsImage2, width=170, height=97, command=lambda : ClickedCourt(tennisCourt2Button), bg="black", highlightthickness=4, activebackground="grey")
		tennisCourt2Button.place(rely=0.54,relx=0.39,anchor=CENTER)
		tennisCourt2Button.image = CourtsImage2

		tennisCourt3label =Label(self.booking, text = 'Court 3', fg ='black',bg='white',font=('serif',9,'bold'), bd=2, relief="ridge", padx=10, pady=3)
		tennisCourt3label.place(rely=0.68,relx=0.15,anchor=CENTER)
		tennisCourt3Button = Button(self.booking, text='3', cursor="tcross", image=CourtsImage2, width=170, height=97, command=lambda : ClickedCourt(tennisCourt3Button), bg="black", highlightthickness=4, activebackground="grey")
		tennisCourt3Button.place(rely=0.78,relx=0.15,anchor=CENTER)
		tennisCourt3Button.image = CourtsImage2

		tennisCourt4label =Label(self.booking, text = 'Court 4', fg ='black',bg='white',font=('serif',9,'bold'), bd=2, relief="ridge", padx=10, pady=3)
		tennisCourt4label.place(rely=0.68,relx=0.39,anchor=CENTER)
		tennisCourt4Button = Button(self.booking, text='4', cursor="tcross", image=CourtsImage2, width=170, height=97, command=lambda : ClickedCourt(tennisCourt4Button), bg="black", highlightthickness=4, activebackground="grey")
		tennisCourt4Button.place(rely=0.78,relx=0.39,anchor=CENTER)
		tennisCourt4Button.image = CourtsImage2


		squashCourt1label =Label(self.booking, text = 'Court 1', fg ='black',bg='white',font=('serif',11,'bold'), bd=2, relief="ridge", padx=10, pady=3)
		squashCourt1label.place(rely=0.44,relx=0.15,anchor=CENTER)
		squashCourt1Button = Button(self.booking, text='1', cursor="tcross", image=CourtsImage3, width=155, height=270, command=lambda : ClickedCourt(squashCourt1Button), bg="black", highlightthickness=4, activebackground="grey")
		squashCourt1Button.place(rely=0.67,relx=0.15,anchor=CENTER)
		squashCourt1Button.image = CourtsImage3

		squashCourt2label =Label(self.booking, text = 'Court 2', fg ='black',bg='white',font=('serif',11,'bold'), bd=2, relief="ridge", padx=10, pady=3)
		squashCourt2label.place(rely=0.44,relx=0.39,anchor=CENTER)
		squashCourt2Button = Button(self.booking, textvariable=court,text='2', cursor="tcross", image=CourtsImage3, width=155, height=270, command=lambda : ClickedCourt(squashCourt2Button), bg="black", highlightthickness=4, activebackground="grey")
		squashCourt2Button.place(rely=0.67,relx=0.39,anchor=CENTER)
		squashCourt2Button.image = CourtsImage3



		badmintonCourt1label.place_forget()
		badmintonCourt1Button.place_forget()
		badmintonCourt2label.place_forget()
		badmintonCourt2Button.place_forget()
		badmintonCourt3label.place_forget()
		badmintonCourt3Button.place_forget()
		badmintonCourt4label.place_forget()
		badmintonCourt4Button.place_forget()
		badmintonCourt5label.place_forget()
		badmintonCourt5Button.place_forget()
		badmintonCourt6label.place_forget()
		badmintonCourt6Button.place_forget()
		badmintonCourt7label.place_forget()
		badmintonCourt7Button.place_forget()
		badmintonCourt8label.place_forget()
		badmintonCourt8Button.place_forget()
		badmintonCourt9label.place_forget()
		badmintonCourt9Button.place_forget()
		badmintonCourt10label.place_forget()
		badmintonCourt10Button.place_forget()
		badmintonCourt11label.place_forget()
		badmintonCourt11Button.place_forget()
		badmintonCourt12label.place_forget()
		badmintonCourt12Button.place_forget()

		tennisCourt1label.place_forget()
		tennisCourt1Button.place_forget()
		tennisCourt2label.place_forget()
		tennisCourt2Button.place_forget()
		tennisCourt3label.place_forget()
		tennisCourt3Button.place_forget()
		tennisCourt4label.place_forget()
		tennisCourt4Button.place_forget()

		squashCourt1label.place_forget()
		squashCourt1Button.place_forget()
		squashCourt2label.place_forget()
		squashCourt2Button.place_forget()



		select_competition_button = tkinter.Button(self.booking, cursor="tcross",text="Choose", command=lambda : RacquetSportSelect(badmintonCourt1Button, badmintonCourt2Button, badmintonCourt3Button, badmintonCourt4Button, badmintonCourt5Button, badmintonCourt6Button, badmintonCourt7Button, badmintonCourt8Button, badmintonCourt9Button, badmintonCourt10Button, badmintonCourt11Button, badmintonCourt12Button, tennisCourt1Button, tennisCourt2Button, tennisCourt3Button, tennisCourt4Button, squashCourt1Button, squashCourt2Button, badmintonCourt1label, badmintonCourt2label, badmintonCourt3label, badmintonCourt4label, badmintonCourt5label, badmintonCourt6label, badmintonCourt7label, badmintonCourt8label, badmintonCourt9label, badmintonCourt10label, badmintonCourt11label, badmintonCourt12label, tennisCourt1label, tennisCourt2label, tennisCourt3label, tennisCourt4label, squashCourt1label, squashCourt2label), fg='white', bg='black', bd=2, relief='ridge', font=('serif', 10, 'bold'), padx=5)
		select_competition_button.place(rely=0.333, relx=0.4, anchor='center')
		ToolTips.bind(select_competition_button, 'Confirm ID and competition type')

		submit_button = tkinter.Button(self.booking, cursor="tcross",text="Submit Booking", command=lambda : SubmitBooking(badmintonCourt1Button, badmintonCourt2Button, badmintonCourt3Button, badmintonCourt4Button, badmintonCourt5Button, badmintonCourt6Button, badmintonCourt7Button, badmintonCourt8Button, badmintonCourt9Button, badmintonCourt10Button, badmintonCourt11Button, badmintonCourt12Button, tennisCourt1Button, tennisCourt2Button, tennisCourt3Button, tennisCourt4Button, squashCourt1Button, squashCourt2Button, badmintonCourt1label, badmintonCourt2label, badmintonCourt3label, badmintonCourt4label, badmintonCourt5label, badmintonCourt6label, badmintonCourt7label, badmintonCourt8label, badmintonCourt9label, badmintonCourt10label, badmintonCourt11label, badmintonCourt12label, tennisCourt1label, tennisCourt2label, tennisCourt3label, tennisCourt4label, squashCourt1label, squashCourt2label, BlankFloorPlan), fg='white', bg='black', bd=4, relief='ridge', font=('serif', 11, 'bold'), padx=20)
		submit_button.place(rely=0.955, relx=0.26, anchor='center')
		ToolTips.bind(submit_button, 'Submit booking details into database')

		transparentimage = PhotoImage(file=self.filepath + '\\_databases_images_doc\\Images\\white.png')
		imageviewer2 = Button(self.booking, image=transparentimage, width=90, height=90, borderwidth=0, activebackground="white", bd=3)
		imageviewer2.place(rely=0.433,relx=0.76,anchor=CENTER)
		imageviewer2.image = transparentimage
		imageviewer2['command'] = 0
		imageviewer2['relief'] = 'sunken'


		member_booking_Tv=ttk.Treeview(self.booking,columns=('Type','Date','Court','ID'), height=5)
		member_booking_Tv.place(relx=0.725,rely=0.24,anchor=CENTER)

		member_booking_Tv.heading("#0",text='Username')
		member_booking_Tv.column("#0",minwidth=0,width=180)
		member_booking_Tv.heading("#1",text='Type')
		member_booking_Tv.column("#1",minwidth=0,width=90)
		member_booking_Tv.heading("#2",text='Date')
		member_booking_Tv.column("#2",minwidth=0,width=90)
		member_booking_Tv.heading("#3",text='Court')
		member_booking_Tv.column("#3",minwidth=0,width=70)
		member_booking_Tv.heading("#4",text='ID')
		member_booking_Tv.column("#4",minwidth=0,width=50)
		member_booking_Tv.bind('<Button-1>', partial(treeviewresizedisable, member_booking_Tv))
		member_booking_Tv.bind("<Button-1>", partial(GetInformation, imageviewer2))

		member_booking_ysearch_scrollbar = Scrollbar(self.booking, orient = 'vertical', command = member_booking_Tv.yview, cursor="tcross")
		member_booking_ysearch_scrollbar.place(relx=0.969,rely=0.24,anchor='center',height=127)
		member_booking_Tv.configure(yscrollcommand=member_booking_ysearch_scrollbar.set)


		BookingPopulate()




	# Stores all usernames collected into a selectable username drop-down box
	def memberSelection(self):
		self.memberNamesAndPasswords = StringVar()

		member_name_choices = self.get_member_details()
		if (len(member_name_choices) > 0) :
			member_selection_dropdown = ttk.Combobox(self.booking, value=member_name_choices, textvariable=self.memberNamesAndPasswords ,font=('serif', 8, 'bold'), width=25)
			member_selection_dropdown.place(rely=0.152, relx=0.27, anchor='center')
			member_selection_dropdown.config(state='readonly')


	# Fetches all usernames within the member database table
	def get_member_details(self):
		conn = sqlite3.connect(self.filepath + '\\_databases_images_doc\\Databases\\LisburnRacquetsDatabase.db')
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