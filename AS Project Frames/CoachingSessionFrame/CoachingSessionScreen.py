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
from CoachingSessionFrame.CoachingSessionEmail import SessionEmail
from PIL import ImageTk,Image
import Pmw


GroupFinder=0
CourtsTrue = False
GroupTrue = False


class CoachingSessionContent:

	def __init__(self, mainScreen):
		self.coachSession = mainScreen
		self.conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
		self.c = self.conn.cursor()


		# self.c.execute("""CREATE TABLE coachSessionDetails (
		# 			username text,
		# 			startTime text,
		# 			endTime text,
		# 			date text,
		# 			courts text,
		# 			membergroup integer,
		# 			people text,
		# 			technique text,
		# 			sessionID text
		# 			)""")


	def generateCoachSessionContnt(self):

		def validate_username(value, label):
			if (value == ''):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The username field cannot be empty", icon='error')
				return False

			label.config(fg="SpringGreen3")
			return True


		def validate_start_time(value, value2, label):
			if (float(value) <8.00):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The start time cannot be before 8am", icon='error')
				return False
			if (float(value) >22.00):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The start time cannot be past 10pm", icon='error')
				return False
			if (float(value) >= float(value2)):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The start time cannot be higher than the end time", icon='error')
				return False

			label.config(fg="SpringGreen3")
			return True


		def validate_end_time(value, label):
			if (float(value) <9.00):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The end time cannot be before 9am", icon='error')
				return False
			if (float(value) >23.00):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The end time cannot be after 11pm", icon='error')
				return False

			label.config(fg="SpringGreen3")
			return True


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

			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
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


		def validate_courts(value, label):
			if (value != True):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The courts must have at least 1 selected", icon='error')
				return False

			label.config(fg="SpringGreen3")
			return True


		def validate_entry_group(value):
			if value is None:
				return False
			if (value == ''):
				messagebox.showinfo("Validation Error", "The group cannot be empty", icon='error')
				return False
			if (value.isnumeric==False):
				messagebox.showinfo("Validation Error", "The group can only contain numbers", icon='error')
				return False
			if (int(value)>20):
				messagebox.showinfo("Validation Error", "The group cannot be over 20, as it doesn't exist", icon='error')
				return False
			if (int(value)<0):
				messagebox.showinfo("Validation Error", "The group cannot be below 0, as it doesn't exist", icon='error')
				return False

			return True


		def validate_group(value, label):
			GroupExistsCounter = 0

			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
			c = conn.cursor()

			c.execute("SELECT * From member")
			items = c.fetchall()

			if (value != True):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "A group must be selected", icon='error')
				return False

			for records in items:
				if (str(records[7]) != str(GroupFinder) or records == []):
					GroupExistsCounter += 1
					pass
					if (GroupExistsCounter == len(items)):
						group_label.config(fg='red')
						messagebox.showinfo('Validation Error', 'There are no members in group ' + str(GroupFinder) + '. You must choose a group with members in order to create a valid coaching session', icon='error')
						return False

			label.config(fg="SpringGreen3")
			return True


		def validate_techniques(label):
			label.config(fg="SpringGreen3")
			return True


		def validate_new_start_time(value, value2):
			if (float(value) <8.00):
				messagebox.showinfo("Validation Error", "The start time cannot be before 8am", icon='error')
				return False
			if (float(value) >22.00):
				messagebox.showinfo("Validation Error", "The start time cannot be after 10pm", icon='error')
				return False
			if (float(value) > float(value2)):
				messagebox.showinfo("Validation Error", "The start time cannot be higher than the end time", icon='error')
				return False

			return True


		def validate_new_end_time(value, value2):
			if (float(value2) <9.00):
				messagebox.showinfo("Validation Error", "The end time cannot be before 9am", icon='error')
				return False
			if (float(value2) >23.00):
				messagebox.showinfo("Validation Error", "The end time cannot be after 11pm", icon='error')
				return False
			if (float(value) == float(value2)):
				messagebox.showinfo("Validation Error", "The start and end time cannot equal each other", icon='error')
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

			today = datetime.date.today()
			top = Toplevel(self.coachSession)

			cal = Calendar(top, font="serif 16", date_pattern='dd/mm/yyyy',selectmode='day', cursor="tcross", year=today.year, month=today.month, day=today.day)
			cal.pack(fill="both", expand=True)
			ttk.Button(top, text="ok", command=assign_dob).pack()


		def ClickedCourt(courtvalue):
			if (courtvalue.cget('bg') == 'black'):
				courtvalue.config(bg='SpringGreen3')
			else:
				courtvalue.config(bg='black')


		def courtsRequired():
			courts = Toplevel(self.coachSession, bg="white")
			courts.geometry('500x500')

			title_label =Label(courts, cursor="tcross",text = 'Select the Number of Courts Required', fg ='black',bg='white',font=('serif',11,'bold'), bd=2, relief="ridge", padx=10, pady=3)
			title_label.place(rely=0.027,relx=0.5,anchor=CENTER)


			CourtsImage = PhotoImage(file="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Images/courts.png")


			Court1label =Label(courts, text = 'Court 1', fg ='black',bg='white',font=('serif',7,'bold'), bd=2, relief="ridge", padx=10, pady=3)
			Court1label.place(rely=0.155,relx=0.15,anchor=CENTER)
			Court1Button = Button(courts, text='1', cursor="tcross", image=CourtsImage, width=95, height=53, command=lambda : ClickedCourt(Court1Button), bg="black", highlightthickness=5, activebackground="grey")
			Court1Button.place(rely=0.24,relx=0.15,anchor=CENTER)
			Court1Button.image = CourtsImage


			Court2label =Label(courts, text = 'Court 2', fg ='black',bg='white',font=('serif',7,'bold'), bd=2, relief="ridge", padx=10, pady=3)
			Court2label.place(rely=0.375,relx=0.15,anchor=CENTER)
			Court2Button = Button(courts, text='2', cursor="tcross", image=CourtsImage, width=95, height=53, command=lambda : ClickedCourt(Court2Button), bg="black", highlightthickness=5, activebackground="grey")
			Court2Button.place(rely=0.46,relx=0.15,anchor=CENTER)
			Court2Button.image = CourtsImage


			Court3label =Label(courts, text = 'Court 3', fg ='black',bg='white',font=('serif',7,'bold'), bd=2, relief="ridge", padx=10, pady=3)
			Court3label.place(rely=0.595,relx=0.15,anchor=CENTER)
			Court3Button = Button(courts, text='3', cursor="tcross", image=CourtsImage, width=95, height=53, command=lambda : ClickedCourt(Court3Button), bg="black", highlightthickness=5, activebackground="grey")
			Court3Button.place(rely=0.68,relx=0.15,anchor=CENTER)
			Court3Button.image = CourtsImage


			Court4label =Label(courts, text = 'Court 4', fg ='black',bg='white',font=('serif',7,'bold'), bd=2, relief="ridge", padx=10, pady=3)
			Court4label.place(rely=0.815,relx=0.15,anchor=CENTER)
			Court4Button = Button(courts, text='4', cursor="tcross", image=CourtsImage, width=95, height=53, command=lambda : ClickedCourt(Court4Button), bg="black", highlightthickness=5, activebackground="grey")
			Court4Button.place(rely=0.9,relx=0.15,anchor=CENTER)
			Court4Button.image = CourtsImage


			Court5label =Label(courts, text = 'Court 5', fg ='black',bg='white',font=('serif',7,'bold'), bd=2, relief="ridge", padx=10, pady=3)
			Court5label.place(rely=0.155,relx=0.5,anchor=CENTER)
			Court5Button = Button(courts, text='5', cursor="tcross", image=CourtsImage, width=95, height=53, command=lambda : ClickedCourt(Court5Button), bg="black", highlightthickness=5, activebackground="grey")
			Court5Button.place(rely=0.24,relx=0.5,anchor=CENTER)
			Court5Button.image = CourtsImage


			Court6label =Label(courts, text = 'Court 6', fg ='black',bg='white',font=('serif',7,'bold'), bd=2, relief="ridge", padx=10, pady=3)
			Court6label.place(rely=0.375,relx=0.5,anchor=CENTER)
			Court6Button = Button(courts, text='6', cursor="tcross", image=CourtsImage, width=95, height=53, command=lambda : ClickedCourt(Court6Button), bg="black", highlightthickness=5, activebackground="grey")
			Court6Button.place(rely=0.46,relx=0.5,anchor=CENTER)
			Court6Button.image = CourtsImage


			Court7label =Label(courts, text = 'Court 7', fg ='black',bg='white',font=('serif',7,'bold'), bd=2, relief="ridge", padx=10, pady=3)
			Court7label.place(rely=0.595,relx=0.5,anchor=CENTER)
			Court7Button = Button(courts, text='7', cursor="tcross", image=CourtsImage, width=95, height=53, command=lambda : ClickedCourt(Court7Button), bg="black", highlightthickness=5, activebackground="grey")
			Court7Button.place(rely=0.68,relx=0.5,anchor=CENTER)
			Court7Button.image = CourtsImage


			Court8label =Label(courts, text = 'Court 8', fg ='black',bg='white',font=('serif',7,'bold'), bd=2, relief="ridge", padx=10, pady=3)
			Court8label.place(rely=0.815,relx=0.5,anchor=CENTER)
			Court8Button = Button(courts, text='8', cursor="tcross", image=CourtsImage, width=95, height=53, command=lambda : ClickedCourt(Court8Button), bg="black", highlightthickness=5, activebackground="grey")
			Court8Button.place(rely=0.9,relx=0.5,anchor=CENTER)
			Court8Button.image = CourtsImage


			Court9label =Label(courts, text = 'Court 9', fg ='black',bg='white',font=('serif',7,'bold'), bd=2, relief="ridge", padx=10, pady=3)
			Court9label.place(rely=0.155,relx=0.85,anchor=CENTER)
			Court9Button = Button(courts, text='9', cursor="tcross", image=CourtsImage, width=95, height=53, command=lambda : ClickedCourt(Court9Button), bg="black", highlightthickness=5, activebackground="grey")
			Court9Button.place(rely=0.24,relx=0.85,anchor=CENTER)
			Court9Button.image = CourtsImage


			Court10label =Label(courts, text = 'Court 10', fg ='black',bg='white',font=('serif',7,'bold'), bd=2, relief="ridge", padx=10, pady=3)
			Court10label.place(rely=0.375,relx=0.85,anchor=CENTER)
			Court10Button = Button(courts, text='10', cursor="tcross", image=CourtsImage, width=95, height=53, command=lambda : ClickedCourt(Court10Button), bg="black", highlightthickness=5, activebackground="grey")
			Court10Button.place(rely=0.46,relx=0.85,anchor=CENTER)
			Court10Button.image = CourtsImage


			Court11label =Label(courts, text = 'Court 11', fg ='black',bg='white',font=('serif',7,'bold'), bd=2, relief="ridge", padx=10, pady=3)
			Court11label.place(rely=0.595,relx=0.85,anchor=CENTER)
			Court11Button = Button(courts, text='11', cursor="tcross", image=CourtsImage, width=95, height=53, command=lambda : ClickedCourt(Court11Button), bg="black", highlightthickness=5, activebackground="grey")
			Court11Button.place(rely=0.68,relx=0.85,anchor=CENTER)
			Court11Button.image = CourtsImage


			Court12label =Label(courts, text = 'Court 12', fg ='black',bg='white',font=('serif',7,'bold'), bd=2, relief="ridge", padx=10, pady=3)
			Court12label.place(rely=0.815,relx=0.85,anchor=CENTER)
			Court12Button = Button(courts, text='12', cursor="tcross", image=CourtsImage, width=95, height=53, command=lambda : ClickedCourt(Court12Button), bg="black", highlightthickness=5, activebackground="grey")
			Court12Button.place(rely=0.9,relx=0.85,anchor=CENTER)
			Court12Button.image = CourtsImage


			SelectCourtsButton=Button(courts, cursor="tcross",text = 'Select Courts', command = lambda : ChangeCourtsColour(courts,Court1Button, Court2Button, Court3Button, Court4Button, Court5Button, Court6Button, Court7Button, Court8Button, Court9Button, Court10Button, Court11Button, Court12Button), fg ='white', bg='black', relief= 'groove', font = ('serif',8,'bold'), padx =15)
			SelectCourtsButton.place(rely=0.095,relx=0.5,anchor=CENTER)
			ToolTips.bind(SelectCourtsButton, 'Pick the courts required for the coaching session')



		def ChangeCourtsColour(frame, courtvalue, courtvalue2, courtvalue3, courtvalue4, courtvalue5, courtvalue6, courtvalue7, courtvalue8, courtvalue9, courtvalue10, courtvalue11, courtvalue12):
			global FinalSelectedCourts
			global CourtsTrue

			counter = 1
			SelectedCourts = []

			courts = [courtvalue, courtvalue2, courtvalue3, courtvalue4, courtvalue5, courtvalue6,
					  courtvalue7, courtvalue8, courtvalue9, courtvalue10, courtvalue11, courtvalue12]

			if (courtvalue.cget('bg') != 'SpringGreen3' and courtvalue2.cget('bg') != 'SpringGreen3' and courtvalue3.cget('bg') != 'SpringGreen3' and courtvalue4.cget('bg') != 'SpringGreen3' and courtvalue5.cget('bg') != 'SpringGreen3' and courtvalue6.cget('bg') != 'SpringGreen3' and courtvalue7.cget('bg') != 'SpringGreen3' and courtvalue8.cget('bg') != 'SpringGreen3' and courtvalue9.cget('bg') != 'SpringGreen3' and courtvalue10.cget('bg') != 'SpringGreen3' and courtvalue11.cget('bg') != 'SpringGreen3' and courtvalue12.cget('bg') != 'SpringGreen3'):
				messagebox.showinfo('Error', 'Please select a court to continue', icon='error')

			else:
				CourtsTrue = True
				frame.withdraw()
				for court in courts:
					if (str(counter) == court.cget('text') and court.cget('bg') == 'SpringGreen3'):
						FinalCourt = str(counter)
						SelectedCourts.append(FinalCourt)

					counter += 1

				FinalSelectedCourts = ''
				for court in SelectedCourts:
					FinalSelectedCourts = FinalSelectedCourts + court + ", "

				FinalSelectedCourts = FinalSelectedCourts[0: len(FinalSelectedCourts) - 2]

				return FinalSelectedCourts


		def groupRequired():
			global GroupFinder
			global GroupTrue

			groupNumber = tkinter.simpledialog.askstring("Response","Enter the group number that you want the coaching session for (1-20)")

			isValid = True
			isValid = isValid and validate_entry_group(groupNumber)

			if isValid:
				GroupTrue = True
				GroupFinder = groupNumber

				return GroupFinder


		def findMembers():
			global PeopleCounter
			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
			c = conn.cursor()

			PeopleCounter = 0

			c.execute("SELECT * From member")
			items = c.fetchall()

			for row in items:
				if row[7] != GroupFinder or row == []:
					pass
				else:
					PeopleCounter += 1

			conn.commit()

			return PeopleCounter


		def updateCoachSessionDate(frame):
			def new_assign_dob(username):
				conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
				c = conn.cursor()

				newEventDate.set(newcal.get_date())
				top.withdraw()

				newCoachSessionDate = newEventDate.get()

				c.execute("""UPDATE coachSessionDetails SET date = :newDate WHERE username=:username""", {
					"newDate": str(newCoachSessionDate),
					"username": username
				})

				messagebox.showinfo("Info", "The coach's session date is now " + newCoachSessionDate, icon='info')

				conn.commit()
				conn.close()

				treeviewPopulate()
				changeCalendarColour()

			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
			c = conn.cursor()

			frame.withdraw()

			coachUsername = simpledialog.askstring("Response", "Enter the username of the coach you want to update")
			if coachUsername != '' and len(coachUsername) <25 and '@' in coachUsername and '.' in coachUsername:
				c.execute(f"SELECT * FROM coachSessionDetails WHERE username=?", (coachUsername,))
				data = c.fetchone()
				if not data:
					messagebox.showinfo("Error", "The username entered was not found in the database", icon='error')

				else:

					top = Toplevel(self.coachSession)

					newcal = Calendar(top, font="serif 16", date_pattern='dd/mm/yyyy',selectmode='day', cursor="tcross", year=today.year, month=today.month, day=today.day)
					newcal.pack(fill="both", expand=True)
					ttk.Button(top, text="Update", command= lambda : new_assign_dob(coachUsername)).pack()


		def clearTv():
			record=coachsession_search_Tv.get_children()
			for elements in record:
				coachsession_search_Tv.delete(elements)


		def treeviewPopulate():
			clearTv()

			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
			c = conn.cursor()

			c.execute("SELECT * From coachSessionDetails")
			items = c.fetchall()
			conn.commit()
			conn.close()

			count=0
			for row in items:
				if row == []:
					pass
				else:
					if count%2==0:
						coachsession_search_Tv.insert('','end',text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
					else:
						coachsession_search_Tv.insert('','end',text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
					count+=1


		def treeviewresizedisable(treeview, event):
			if treeview.identify_region(event.x, event.y) == "separator":
				return "break"


		def returnColour(usernameReturn, startTimeReturn, endTimeReturn, dateReturn, courtReturn, groupReturn, techniqueReturn):
			usernameReturn.config(fg="black")
			startTimeReturn.config(fg="black")
			endTimeReturn.config(fg="black")
			dateReturn.config(fg="black")
			courtReturn.config(fg="black")
			groupReturn.config(fg="black")
			techniqueReturn.config(fg="black")


		def updateCoachSessionDetails(self):
			response = askyesno("Question", "Do you want to update a coach's session?", icon='question')
			if response == False:
				showinfo("Info", "Update cancelled", icon='info')

			else:

				updateCoachSession=Toplevel(bg="white")

				title_label =Label(updateCoachSession, cursor="tcross",text = 'Update Session' , fg ='SpringGreen3',bg='white',font=('serif',15,'bold'))
				title_label.place(rely=0.1,relx=0.5,anchor=CENTER)

				update_time=Button(updateCoachSession, cursor="tcross",text = 'Update Time', command = lambda : updateCoachSessionTime(updateCoachSession), fg ='white', bg='black', relief= 'groove', font = ('serif',9,'bold'), padx =20)
				update_time.place(rely=0.27,relx=0.5,anchor=CENTER)
				ToolTips.bind(update_time, 'Update the coaching session time')

				update_date=Button(updateCoachSession, cursor="tcross", text = 'Update Date', command = lambda : updateCoachSessionDate(updateCoachSession), fg ='white', bg='black', relief= 'groove', font = ('serif',9,'bold'), padx =20)
				update_date.place(rely=0.47,relx=0.5,anchor=CENTER)
				ToolTips.bind(update_date, 'Update the date of the coaching session')

				update_courts=Button(updateCoachSession, cursor="tcross",text = 'Update Courts', command = lambda : updateCoachSessionCourts(updateCoachSession), fg ='white', bg='black', relief= 'groove', font = ('serif',9,'bold'), padx =20)
				update_courts.place(rely=0.67,relx=0.5,anchor=CENTER)
				ToolTips.bind(update_courts, 'Update the court of the competition')

				update_technique=Button(updateCoachSession, cursor="tcross",text = 'Update Technique', command = lambda : updateCoachSessionTechnique(updateCoachSession), fg ='white', bg='black', relief= 'groove', font = ('serif',9,'bold'), padx =20)
				update_technique.place(rely=0.87,relx=0.5,anchor=CENTER)
				ToolTips.bind(update_technique, 'Update the technique used for the coaching session')


		def updateCoachSessionTime(frame):
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

					updateTimes=Toplevel(bg="white")
					updateTimes.geometry('200x200')

					title_label =Label(updateTimes,text ="Select New Times", fg ='SpringGreen3',bg='white',font=('serif',13,'bold','underline'))
					title_label.place(rely=0.1,relx=0.5,anchor=CENTER)

					update_starttime_label =Label(updateTimes,text ="New Start Time:", fg ='black',bg='white',font=('serif',9,'bold'))
					update_starttime_label.place(rely=0.35,relx=0.3,anchor=CENTER)

					update_endtime_label =Label(updateTimes,text ="New End Time:", fg ='black',bg='white',font=('serif',9,'bold'))
					update_endtime_label.place(rely=0.55,relx=0.3,anchor=CENTER)

					update_starttime_spinbox = Spinbox(updateTimes, width=7,font=("serif",8, 'bold'), bd=3, relief='ridge', cursor="tcross",textvariable=new_start_time, values=('8.00', '8.15', '8.30', '8.45', '9.00', '9.15', '9.30', '9.45', '10.00', '10.15', '10.30', '10.45', '11.00', '11.15', '11.30', '11.45', '12.00', '12.15','12.30','12.45','13.00','13.15','13.30','13.45','14.00','14.15','14.30','14.45','15.00','15.15','15.30','15.45','16.00','16.15','16.30','16.45','17.00','17.15','17.30','17.45','18.00','18.15','18.30','18.45','19.00','19.15','19.30','19.45','20.00','20.15','20.30','20.45','21.00','21.15','21.30','21.45','22.00'))
					update_starttime_spinbox.place(rely=0.353, relx=0.79, anchor='center')

					update_endtime_spinbox = Spinbox(updateTimes, width=7,font=("serif",8, 'bold'), bd=3, relief='ridge', cursor="tcross", textvariable=new_end_time, values=('9.00', '9.15', '9.30', '9.45', '10.00', '10.15', '10.30', '10.45', '11.00', '11.15', '11.30', '11.45', '12.00', '12.15','12.30','12.45','13.00','13.15','13.30','13.45','14.00','14.15','14.30','14.45','15.00','15.15','15.30','15.45','16.00','16.15','16.30','16.45','17.00','17.15','17.30','17.45','18.00','18.15','18.30','18.45','19.00','19.15','19.30','19.45','20.00','20.15','20.30','20.45','21.00','21.15','21.30','21.45','22.00','22.15','22.30','22.45','23.00'))
					update_endtime_spinbox.place(rely=0.553, relx=0.79, anchor='center')

					update_time_button = Button(updateTimes, text='Confirm Update',font=("serif",10, 'bold'), fg='white', bg='black',cursor="tcross",command=lambda : confirmNewTimes(updateTimes, coachUsername), padx=10, bd=4, relief="ridge")
					update_time_button.place(rely=0.85, relx=0.5, anchor='center')
					ToolTips.bind(update_time_button, 'Confirm new time')

			conn.commit()
			conn.close()

			treeviewPopulate()


		def confirmNewTimes(frame, username):
			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
			c = conn.cursor()

			frame.withdraw()

			isValid = True
			isValid = isValid and validate_new_start_time(new_start_time.get(), new_end_time.get())
			isValid = isValid and validate_new_end_time(new_start_time.get(), new_end_time.get())

			if isValid:
				newCoachSessionStartTime = new_start_time.get()
				newCoachSessionEndTime = new_end_time.get()

				c.execute("""UPDATE coachSessionDetails SET startTime = :new_start_time WHERE username=:username""", {
					"new_start_time": str(new_start_time.get()),
					"username": username
				})
				c.execute("""UPDATE coachSessionDetails SET endTime = :new_end_time WHERE username=:username""", {
					"new_end_time": str(new_end_time.get()),
					"username": username
				})

				messagebox.showinfo("Info", "The coach's new session start time is: "+newCoachSessionStartTime, icon='info')
				messagebox.showinfo("Info", "The coach's new session end time is: "+newCoachSessionEndTime, icon='info')

			conn.commit()
			conn.close()

			treeviewPopulate()


		def updateCoachSessionCourts(frame):
			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
			c = conn.cursor()

			frame.withdraw()

			coachUsername = simpledialog.askstring("Response", "Enter the username of the coach you want to update")
			if coachUsername != '' and len(coachUsername) <25 and '@' in coachUsername and '.' in coachUsername:
				c.execute(f"SELECT * FROM coachSessionDetails WHERE username=?", (coachUsername,))
				data = c.fetchone()
				if not data:
					messagebox.showinfo("Error", "The username entered was not found in the database", icon='error')

				else:
					courts = Toplevel(self.coachSession, bg="white")
					courts.geometry('500x500')

					title_label =Label(courts, cursor="tcross",text = 'Update the Number of Courts Required', fg ='black',bg='white',font=('serif',11,'bold'), bd=2, relief="ridge", padx=10, pady=3)
					title_label.place(rely=0.027,relx=0.5,anchor=CENTER)

					CourtsImage = PhotoImage(file="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Images/courts.png")


					Court1label =Label(courts, text = 'Court 1', fg ='black',bg='white',font=('serif',7,'bold'), bd=2, relief="ridge", padx=10, pady=3)
					Court1label.place(rely=0.155,relx=0.15,anchor=CENTER)
					Court1Button = Button(courts, text='1', cursor="tcross", image=CourtsImage, width=95, height=53, command=lambda : ClickedCourt(Court1Button), bg="black", highlightthickness=5, activebackground="grey")
					Court1Button.place(rely=0.24,relx=0.15,anchor=CENTER)
					Court1Button.image = CourtsImage


					Court2label =Label(courts, text = 'Court 2', fg ='black',bg='white',font=('serif',7,'bold'), bd=2, relief="ridge", padx=10, pady=3)
					Court2label.place(rely=0.375,relx=0.15,anchor=CENTER)
					Court2Button = Button(courts, text='2', cursor="tcross", image=CourtsImage, width=95, height=53, command=lambda : ClickedCourt(Court2Button), bg="black", highlightthickness=5, activebackground="grey")
					Court2Button.place(rely=0.46,relx=0.15,anchor=CENTER)
					Court2Button.image = CourtsImage


					Court3label =Label(courts, text = 'Court 3', fg ='black',bg='white',font=('serif',7,'bold'), bd=2, relief="ridge", padx=10, pady=3)
					Court3label.place(rely=0.595,relx=0.15,anchor=CENTER)
					Court3Button = Button(courts, text='3', cursor="tcross", image=CourtsImage, width=95, height=53, command=lambda : ClickedCourt(Court3Button), bg="black", highlightthickness=5, activebackground="grey")
					Court3Button.place(rely=0.68,relx=0.15,anchor=CENTER)
					Court3Button.image = CourtsImage


					Court4label =Label(courts, text = 'Court 4', fg ='black',bg='white',font=('serif',7,'bold'), bd=2, relief="ridge", padx=10, pady=3)
					Court4label.place(rely=0.815,relx=0.15,anchor=CENTER)
					Court4Button = Button(courts, text='4', cursor="tcross", image=CourtsImage, width=95, height=53, command=lambda : ClickedCourt(Court4Button), bg="black", highlightthickness=5, activebackground="grey")
					Court4Button.place(rely=0.9,relx=0.15,anchor=CENTER)
					Court4Button.image = CourtsImage


					Court5label =Label(courts, text = 'Court 5', fg ='black',bg='white',font=('serif',7,'bold'), bd=2, relief="ridge", padx=10, pady=3)
					Court5label.place(rely=0.155,relx=0.5,anchor=CENTER)
					Court5Button = Button(courts, text='5', cursor="tcross", image=CourtsImage, width=95, height=53, command=lambda : ClickedCourt(Court5Button), bg="black", highlightthickness=5, activebackground="grey")
					Court5Button.place(rely=0.24,relx=0.5,anchor=CENTER)
					Court5Button.image = CourtsImage


					Court6label =Label(courts, text = 'Court 6', fg ='black',bg='white',font=('serif',7,'bold'), bd=2, relief="ridge", padx=10, pady=3)
					Court6label.place(rely=0.375,relx=0.5,anchor=CENTER)
					Court6Button = Button(courts, text='6', cursor="tcross", image=CourtsImage, width=95, height=53, command=lambda : ClickedCourt(Court6Button), bg="black", highlightthickness=5, activebackground="grey")
					Court6Button.place(rely=0.46,relx=0.5,anchor=CENTER)
					Court6Button.image = CourtsImage


					Court7label =Label(courts, text = 'Court 7', fg ='black',bg='white',font=('serif',7,'bold'), bd=2, relief="ridge", padx=10, pady=3)
					Court7label.place(rely=0.595,relx=0.5,anchor=CENTER)
					Court7Button = Button(courts, text='7', cursor="tcross", image=CourtsImage, width=95, height=53, command=lambda : ClickedCourt(Court7Button), bg="black", highlightthickness=5, activebackground="grey")
					Court7Button.place(rely=0.68,relx=0.5,anchor=CENTER)
					Court7Button.image = CourtsImage


					Court8label =Label(courts, text = 'Court 8', fg ='black',bg='white',font=('serif',7,'bold'), bd=2, relief="ridge", padx=10, pady=3)
					Court8label.place(rely=0.815,relx=0.5,anchor=CENTER)
					Court8Button = Button(courts, text='8', cursor="tcross", image=CourtsImage, width=95, height=53, command=lambda : ClickedCourt(Court8Button), bg="black", highlightthickness=5, activebackground="grey")
					Court8Button.place(rely=0.9,relx=0.5,anchor=CENTER)
					Court8Button.image = CourtsImage


					Court9label =Label(courts, text = 'Court 9', fg ='black',bg='white',font=('serif',7,'bold'), bd=2, relief="ridge", padx=10, pady=3)
					Court9label.place(rely=0.155,relx=0.85,anchor=CENTER)
					Court9Button = Button(courts, text='9', cursor="tcross", image=CourtsImage, width=95, height=53, command=lambda : ClickedCourt(Court9Button), bg="black", highlightthickness=5, activebackground="grey")
					Court9Button.place(rely=0.24,relx=0.85,anchor=CENTER)
					Court9Button.image = CourtsImage


					Court10label =Label(courts, text = 'Court 10', fg ='black',bg='white',font=('serif',7,'bold'), bd=2, relief="ridge", padx=10, pady=3)
					Court10label.place(rely=0.375,relx=0.85,anchor=CENTER)
					Court10Button = Button(courts, text='10', cursor="tcross", image=CourtsImage, width=95, height=53, command=lambda : ClickedCourt(Court10Button), bg="black", highlightthickness=5, activebackground="grey")
					Court10Button.place(rely=0.46,relx=0.85,anchor=CENTER)
					Court10Button.image = CourtsImage


					Court11label =Label(courts, text = 'Court 11', fg ='black',bg='white',font=('serif',7,'bold'), bd=2, relief="ridge", padx=10, pady=3)
					Court11label.place(rely=0.595,relx=0.85,anchor=CENTER)
					Court11Button = Button(courts, text='11', cursor="tcross", image=CourtsImage, width=95, height=53, command=lambda : ClickedCourt(Court11Button), bg="black", highlightthickness=5, activebackground="grey")
					Court11Button.place(rely=0.68,relx=0.85,anchor=CENTER)
					Court11Button.image = CourtsImage


					Court12label =Label(courts, text = 'Court 12', fg ='black',bg='white',font=('serif',7,'bold'), bd=2, relief="ridge", padx=10, pady=3)
					Court12label.place(rely=0.815,relx=0.85,anchor=CENTER)
					Court12Button = Button(courts, text='12', cursor="tcross", image=CourtsImage, width=95, height=53, command=lambda : ClickedCourt(Court12Button), bg="black", highlightthickness=5, activebackground="grey")
					Court12Button.place(rely=0.9,relx=0.85,anchor=CENTER)
					Court12Button.image = CourtsImage


					SelectCourtsButton=Button(courts, cursor="tcross",text = 'Select Courts', command = lambda : updateCourts(courts, coachUsername, Court1Button, Court2Button, Court3Button, Court4Button, Court5Button, Court6Button, Court7Button, Court8Button, Court9Button, Court10Button, Court11Button, Court12Button), fg ='white', bg='black', relief= 'groove', font = ('serif',8,'bold'), padx =15)
					SelectCourtsButton.place(rely=0.095,relx=0.5,anchor=CENTER)
					ToolTips.bind(SelectCourtsButton, 'Pick the courts required for the coaching session')


		def updateCourts(frame, username, courtvalue, courtvalue2, courtvalue3, courtvalue4, courtvalue5, courtvalue6, courtvalue7, courtvalue8, courtvalue9, courtvalue10, courtvalue11, courtvalue12):

			counter = 1
			SelectedCourts = []

			courts = [courtvalue, courtvalue2, courtvalue3, courtvalue4, courtvalue5, courtvalue6,
					  courtvalue7, courtvalue8, courtvalue9, courtvalue10, courtvalue11, courtvalue12]

			if (courtvalue.cget('bg') != 'SpringGreen3' and courtvalue2.cget('bg') != 'SpringGreen3' and courtvalue3.cget('bg') != 'SpringGreen3' and courtvalue4.cget('bg') != 'SpringGreen3' and courtvalue5.cget('bg') != 'SpringGreen3' and courtvalue6.cget('bg') != 'SpringGreen3' and courtvalue7.cget('bg') != 'SpringGreen3' and courtvalue8.cget('bg') != 'SpringGreen3' and courtvalue9.cget('bg') != 'SpringGreen3' and courtvalue10.cget('bg') != 'SpringGreen3' and courtvalue11.cget('bg') != 'SpringGreen3' and courtvalue12.cget('bg') != 'SpringGreen3'):
				messagebox.showinfo('Error', 'Please select a court to continue', icon='error')

			else:
				frame.withdraw()

				for court in courts:
					if (str(counter) == court.cget('text') and court.cget('bg') == 'SpringGreen3'):
						FinalCourt = str(counter)
						SelectedCourts.append(FinalCourt)

					counter += 1

				FinalSelectedCourts = ''
				for court in SelectedCourts:
					FinalSelectedCourts = FinalSelectedCourts + court + ", "

				FinalSelectedCourts = FinalSelectedCourts[0: len(FinalSelectedCourts) - 2]

				c.execute("UPDATE coachSessionDetails SET courts = :newCourts WHERE username=:username", {
					"newCourts": FinalSelectedCourts,
					"username": username
				})

				messagebox.showinfo("Info", "The session's new courts are now "+FinalSelectedCourts, icon='info')

			conn.commit()
			conn.close()

			treeviewPopulate()


		def updateCoachSessionTechnique(frame):
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

					updateTechnique=Toplevel(bg="white")
					updateTechnique.geometry('200x200')

					title_label =Label(updateTechnique,text ="Select New Technique" , fg ='SpringGreen3',bg='white',font=('serif',10,'bold','underline'))
					title_label.place(rely=0.055,relx=0.5,anchor=CENTER)

					technique1_radiobutton = Radiobutton(updateTechnique, text="Net Play", variable=newtechnique, value=1, font=("serif",9, 'bold'), cursor="tcross", bg="white", bd=2, relief="ridge")
					technique1_radiobutton.place(rely=0.225, relx=0.5, anchor='center')

					technique2_radiobutton = Radiobutton(updateTechnique, text="Smash", variable=newtechnique, value=2, font=("serif",9, 'bold'), cursor="tcross", bg="white", bd=2, relief="ridge")
					technique2_radiobutton.place(rely=0.39, relx=0.5, anchor='center')

					technique3_radiobutton = Radiobutton(updateTechnique, text="Rally", variable=newtechnique, value=3, font=("serif",9, 'bold'), cursor="tcross", bg="white", bd=2, relief="ridge")
					technique3_radiobutton.place(rely=0.55, relx=0.5, anchor='center')

					technique4_radiobutton = Radiobutton(updateTechnique, text="Back Court", variable=newtechnique, value=4, font=("serif",9, 'bold'), cursor="tcross", bg="white", bd=2, relief="ridge")
					technique4_radiobutton.place(rely=0.715, relx=0.5, anchor='center')

					technique_update_button=Button(updateTechnique,text = 'Confirm Update', command = lambda : techniqueUpdate(updateTechnique, coachUsername), fg ='white', bg='black', relief= 'groove', font = ('serif',10,'bold'), padx =10)
					technique_update_button.place(rely=0.9,relx=0.5,anchor=CENTER)
					ToolTips.bind(technique_update_button, 'Confirm new technique')

			conn.commit()
			conn.close()


		def techniqueUpdate(frame, username):
			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
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

				c.execute("""UPDATE coachSessionDetails SET technique = :newTechnique WHERE username=:username""", {
					"newTechnique": str(final_technique),
					"username": username
				})

				messagebox.showinfo("Info", "The session's new technique is now "+ str(final_technique), icon='info')

			conn.commit()
			conn.close()

			treeviewPopulate()


		def deleteCoachSessionDetails(self):
			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
			c = conn.cursor()

			response = askyesno("Question", "Do you want to delete a coach session?", icon='question')
			if response == False:
				showinfo("Info", "Deletion cancelled", icon='info')

			else:

				coachUsername = simpledialog.askstring("Response", "Enter the username of the coach you want to delete")

				if coachUsername !='' and len(coachUsername) <25 and '@' in coachUsername and '.' in coachUsername:

					c.execute(f"SELECT * FROM coachSessionDetails WHERE username =?", (coachUsername,))
					data = c.fetchone()
					if not data:
						messagebox.showinfo("Error", "The username entered was not found in the database", icon='error')

					else:

						c.execute(f"DELETE FROM coachSessionDetails WHERE username =?", (coachUsername,))
						messagebox.showinfo("Info", "The coach session associated with username "+coachUsername+" has been deleted from the database", icon='info')

				else:

					messagebox.showinfo("Error", "The username entered does not meet the rules", icon='error')

			conn.commit()
			conn.close()

			treeviewPopulate()


		def searchCoachSessionDetails():
			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
			c = conn.cursor()

			response = askyesno("Question", "Do you want to search a coach's session?", icon='question')
			if response == False:
				showinfo("Info", "Search cancelled", icon='info')

			else:

				coachUsername = simpledialog.askstring("Response", "Enter the username of the coach you want to find the session on")
				if coachUsername != '' and len(coachUsername) <25 and '@' in coachUsername and '.' in coachUsername:
					c.execute(f"SELECT * FROM coachSessionDetails WHERE username=?", (coachUsername,))
					data = c.fetchone()
					if not data:
						messagebox.showinfo("Error", "The username entered was not found in the database", icon='error')
					else:

						messagebox.showinfo("Info", "The session's details are listed below" + "\n\n" + "Username: " + str(data[0]) + "\n" + "Start Time: " + str(data[1]) + "\n" + "End Time: " + str(data[2]) + "\n" + "Date: " + str(data[3]) + "\n" + "Courts: " + str(data[4]) + "\n" + "Group: " + str(data[5]) + "\n" + "People: " + str(data[6]) + "\n" + "Technique: " + str(data[7]), icon='info')

				else:

					messagebox.showinfo("Error", "The username entered does not meet the rules", icon='error')

			conn.commit()
			conn.close()

			treeviewPopulate()


		def submitCoachSession():
			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
			c = conn.cursor()

			AllEmailsComplete = 0

			isValid = True
			isValid = isValid and validate_username(self.coachNamesAndPasswords.get(), username_label)
			isValid = isValid and validate_start_time(timeStart.get(), timeEnd.get(), starttime_label)
			isValid = isValid and validate_end_time(timeEnd.get(), endtime_label)
			isValid = isValid and validate_date(eventDate.get(), date_label)
			isValid = isValid and validate_courts(CourtsTrue, courts_needed_label)
			isValid = isValid and validate_group(GroupTrue, group_label)
			isValid = isValid and validate_techniques(techniques_label)


			if isValid:
				c.execute("SELECT * From coachSessionDetails")
				rows = c.fetchall()

				coachsession_username = self.coachNamesAndPasswords.get()
				coachsession_starttime= timeStart.get()
				coachsession_endtime= timeEnd.get()
				coachsession_date = eventDate.get()
				coachID = len(rows)+1

				final_coach_starttime = format(float(coachsession_starttime), '.2f')
				final_coach_endtime = format(float(coachsession_endtime), '.2f')

				if (technique.get() ==1):
					final_technique = 'Net Play'
				if (technique.get() ==2):
					final_technique = 'Smash'
				if (technique.get() ==3):
					final_technique = 'Rally'
				if (technique.get() ==4):
					final_technique = 'Clears'


				response = askyesno("Question", "Are you sure that all information above is correct?", icon='question')
				if response == False:
					showinfo("Info", "submition cancelled", icon='info')

				else:
					findMembers()

					c.execute("SELECT * From member")
					items = c.fetchall()

					for row in items:
						if str(row[7]) != str(GroupFinder) or row == []:
							pass
							AllEmailsComplete += 1
						else:
							member_name = row[0]
							SessionEmail("Coaching Session Date Set", "A coach at Lisburn Racquets Club has set up a new coaching session. The date and time of the session is listed below:" + "\n\n" + "Date: " + coachsession_date + "\n\n" + "From: " + coachsession_starttime + "\n" + "To: " + coachsession_endtime + "\n\n" + "Thanks for choosing Lisburn Racquets Club", member_name, username_label)
							AllEmailsComplete += 1
							if (AllEmailsComplete == len(items)):
								messagebox.showinfo('Info', 'All members in group ' + str(GroupFinder) + ' have been sent information on the new coaching session', icon='info')

					conn2 = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
					c2 = conn2.cursor()
					c2.execute("INSERT INTO coachSessionDetails VALUES (:username, :startTime, :endTime, :date, :courts, :membergroup, :people, :technique, :sessionID)",
							{
								'username': coachsession_username,
								'startTime': final_coach_starttime,
								'endTime': final_coach_endtime,
								'date': coachsession_date,
								'courts': FinalSelectedCourts,
								'membergroup': GroupFinder,
								'people': PeopleCounter,
								'technique': final_technique,
								'sessionID': coachID,
							})

					conn.commit()
					conn.close()

					conn2.commit()
					conn2.close()

					changeCalendarColour()

					self.coachNamesAndPasswords.set('')
					timeStart.set('8.00')
					timeEnd.set('9.00')
					technique.set('1')

					returnColour(username_label, starttime_label, endtime_label, date_label, courts_needed_label, group_label, techniques_label)
					messagebox.showinfo("Info", "Details have been successfully stored", icon='info')

			treeviewPopulate()


		def CalendarSelection(event):
			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
			c = conn.cursor()

			date = cal.get_date()
			date=str(date).split('/')
			newdate=date[0],date[1],date[2]
			a_date = datetime.date(int('20'+newdate[2]),int(newdate[0]), int(newdate[1]))

			string_date = a_date.strftime("%d/%m/%Y")

			c.execute("SELECT * From coachSessionDetails WHERE date=?", (string_date,))
			items = c.fetchone()
			if not items:
				messagebox.showinfo("Error", "There is no coaching session on this date", icon='error')

			else:

				messagebox.showinfo("info", "There is a coaching session on this date" + "\n" +
				"The details are listed below:" + "\n\n"
				+ "Coach: " + items[0] + "\n"
				+ "Start Time: " + str(items[1]) + "\n"
				+ "End Time: " + str(items[2]) + "\n"
				+ "Court(s): " + items[4] + "\n"
				+ "Group: " + str(items[5]) + "\n"
				+ "No. People: " + str(items[6]) + "\n"
			    + "Technique: " + items[7])

			conn.commit()
			conn.close()


		def changeCalendarColour():
			cal.calevent_remove("all")
			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
			c = conn.cursor()

			c.execute("SELECT * FROM coachSessionDetails")
			session_array = c.fetchall()

			for row in session_array:
				cal.calevent_create(datetime.date(int(row[3][6:10]), int(row[3][3:5]), int(row[3][0:2])),"View Coaching Session Details","message")

			cal.tag_config("message", background="SpringGreen3", foreground="black")

			conn.commit()
			conn.close()



		presentDate = datetime.datetime.now()
		current_date = presentDate.strftime("%d/%m/%Y")

		conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
		c = conn.cursor()

		c.execute("SELECT * From coachSessionDetails")
		items = c.fetchall()

		for row in items:
			rowsplitdate = str(row[3]).split('/')
			currentdatesplit = current_date.split('/')

			if rowsplitdate[2] < currentdatesplit[2]:
				c.execute('DELETE FROM coachSessionDetails WHERE sessionID=:ID', {
					"ID": row[8]
				})
			else:
				if rowsplitdate[2] >= currentdatesplit[2] and rowsplitdate[1] < currentdatesplit[1]:
					c.execute('DELETE FROM coachSessionDetails WHERE sessionID=:ID', {
						"ID": row[8]
					})
				else:
					if rowsplitdate[2] >= currentdatesplit[2] and rowsplitdate[1] >= currentdatesplit[1] and rowsplitdate[0] < currentdatesplit[0]:
						c.execute('DELETE FROM coachSessionDetails WHERE sessionID=:ID', {
							"ID": row[8]
						})
					else:
						pass



		timeStart=StringVar()
		timeEnd=StringVar()
		eventDate=StringVar()
		technique=IntVar()

		new_start_time = StringVar()
		new_end_time = StringVar()
		newEventDate=StringVar()

		newtechnique=IntVar()


		ToolTips = Pmw.Balloon()


		username_label = tkinter.Label(self.coachSession, text="Username:", font=('serif', 14, 'bold'), fg='black', bg='white')
		username_label.place(rely=0.36, relx=0.12, anchor='center')

		starttime_label = tkinter.Label(self.coachSession, text="Start Time:", font=('serif', 14, 'bold'), fg='black', bg='white')
		starttime_label.place(rely=0.44, relx=0.12, anchor='center')

		endtime_label = tkinter.Label(self.coachSession, text="End Time:", font=('serif', 14, 'bold'), fg='black', bg='white')
		endtime_label.place(rely=0.52, relx=0.12, anchor='center')

		date_label = tkinter.Label(self.coachSession, text="Session Date:", font=('serif', 14, 'bold'), fg='black', bg='white')
		date_label.place(rely=0.6, relx=0.12, anchor='center')

		courts_needed_label = tkinter.Label(self.coachSession, text="Courts Required:", font=('serif', 14, 'bold'), fg='black', bg='white')
		courts_needed_label.place(rely=0.68, relx=0.12, anchor='center')

		group_label = tkinter.Label(self.coachSession, text="Group Level:", font=('serif', 14, 'bold'), fg='black', bg='white')
		group_label.place(rely=0.76, relx=0.12, anchor='center')

		techniques_label = tkinter.Label(self.coachSession, text="Technique:", font=('serif', 14, 'bold'), fg='black', bg='white')
		techniques_label.place(rely=0.84, relx=0.12, anchor='center')


		starttime_spinbox = Spinbox(self.coachSession, width=7,font=("serif",12, 'bold'), bd=3, relief='ridge', cursor="tcross",textvariable=timeStart, values=('8.00', '8.15', '8.30', '8.45', '9.00', '9.15', '9.30', '9.45', '10.00', '10.15', '10.30', '10.45', '11.00', '11.15', '11.30', '11.45', '12.00', '12.15','12.30','12.45','13.00','13.15','13.30','13.45','14.00','14.15','14.30','14.45','15.00','15.15','15.30','15.45','16.00','16.15','16.30','16.45','17.00','17.15','17.30','17.45','18.00','18.15','18.30','18.45','19.00','19.15','19.30','19.45','20.00','20.15','20.30','20.45','21.00','21.15','21.30','21.45','22.00'))
		starttime_spinbox.place(rely=0.4425, relx=0.3, anchor='center')
		starttime_spinbox.config(state='readonly')

		endtime_spinbox = Spinbox(self.coachSession, width=7,font=("serif",12, 'bold'), bd=3, relief='ridge', cursor="tcross", textvariable=timeEnd, values=('9.00', '9.15', '9.30', '9.45', '10.00', '10.15', '10.30', '10.45', '11.00', '11.15', '11.30', '11.45', '12.00', '12.15','12.30','12.45','13.00','13.15','13.30','13.45','14.00','14.15','14.30','14.45','15.00','15.15','15.30','15.45','16.00','16.15','16.30','16.45','17.00','17.15','17.30','17.45','18.00','18.15','18.30','18.45','19.00','19.15','19.30','19.45','20.00','20.15','20.30','20.45','21.00','21.15','21.30','21.45','22.00','22.15','22.30','22.45','23.00'))
		endtime_spinbox.place(rely=0.5225, relx=0.3, anchor='center')
		endtime_spinbox.config(state='readonly')

		date_entry = Button(self.coachSession, text='Select Date',font=("serif",10, 'bold'), cursor="tcross",command=lambda : dateEntryCheck(eventDate), padx=10, bd=4, relief="ridge")
		date_entry.place(rely=0.603, relx=0.3, anchor='center')
		ToolTips.bind(date_entry, 'Select the date of the coaching session')

		courts_needed_button = Button(self.coachSession, text='Select Courts',font=("serif",10, 'bold'), cursor="tcross",command=courtsRequired, padx=10, bd=4, relief="ridge")
		courts_needed_button.place(rely=0.683, relx=0.3, anchor='center')
		ToolTips.bind(courts_needed_button, 'Select the courts needed for the coaching session')

		group_needed_button = Button(self.coachSession, text='Select Group',font=("serif",10, 'bold'), cursor="tcross",command=groupRequired, padx=10, bd=4, relief="ridge")
		group_needed_button.place(rely=0.763, relx=0.3, anchor='center')
		ToolTips.bind(group_needed_button, 'Select the group needed for the coaching session')

		technique1_radiobutton = Radiobutton(self.coachSession, text="Net Play", variable=technique, value=1, font=("serif",9, 'bold'), cursor="tcross", bg="white", bd=2, relief="ridge")
		technique1_radiobutton.place(rely=0.82, relx=0.25, anchor='center')

		technique2_radiobutton = Radiobutton(self.coachSession, text="Smash", variable=technique, value=2, font=("serif",9, 'bold'), cursor="tcross", bg="white", bd=2, relief="ridge")
		technique2_radiobutton.place(rely=0.87, relx=0.25, anchor='center')

		technique3_radiobutton = Radiobutton(self.coachSession, text="Rally", variable=technique, value=3, font=("serif",9, 'bold'), cursor="tcross", bg="white", bd=2, relief="ridge")
		technique3_radiobutton.place(rely=0.82, relx=0.35, anchor='center')

		technique4_radiobutton = Radiobutton(self.coachSession, text="Clears", variable=technique, value=4, font=("serif",9, 'bold'), cursor="tcross", bg="white", bd=2, relief="ridge")
		technique4_radiobutton.place(rely=0.87, relx=0.355, anchor='center')
		technique.set("1")


		delete_button = tkinter.Button(self.coachSession, cursor="tcross",text="Delete", command=lambda : deleteCoachSessionDetails(self), fg='white', bg='black', bd=4, relief='ridge', font=('serif', 12, 'bold'), padx=10, pady=5)
		delete_button.place(rely=0.95, relx=0.058, anchor='center')
		ToolTips.bind(delete_button, 'Delete coaching session from database')

		update_button = tkinter.Button(self.coachSession, cursor="tcross",text="Update", command=lambda : updateCoachSessionDetails(self), fg='white', bg='black', bd=4, relief='ridge', font=('serif', 12, 'bold'), padx=10, pady=5)
		update_button.place(rely=0.95, relx=0.168, anchor='center')
		ToolTips.bind(update_button, 'Update data inside coaching session database')

		search_button = tkinter.Button(self.coachSession, cursor="tcross",text="Search", command=searchCoachSessionDetails, fg='white', bg='black', bd=4, relief='ridge', font=('serif', 12, 'bold'), padx=10, pady=5)
		search_button.place(rely=0.95, relx=0.276, anchor='center')
		ToolTips.bind(search_button, 'Search data inside coaching session database')

		create_button = tkinter.Button(self.coachSession, cursor="tcross",text="Submit", command=submitCoachSession, fg='white', bg='black', bd=4, relief='ridge', font=('serif', 12, 'bold'), padx=10, pady=5)
		create_button.place(rely=0.95, relx=0.384, anchor='center')
		ToolTips.bind(create_button, 'Creates a new coaching session')


		coachsession_search_Tv=ttk.Treeview(self.coachSession,height=4,columns=('Start Time','End Time','Date','Courts','Group','No. People','Technique'))
		coachsession_search_Tv.place(relx=0.5,rely=0.22,anchor=CENTER)

		coachsession_search_Tv.heading("#0",text='Username')
		coachsession_search_Tv.column("#0",minwidth=0,width=180)
		coachsession_search_Tv.heading("#1",text='Start Time')
		coachsession_search_Tv.column("#1",minwidth=0,width=90)
		coachsession_search_Tv.heading("#2",text='End Time')
		coachsession_search_Tv.column("#2",minwidth=0,width=90)
		coachsession_search_Tv.heading("#3",text='Date')
		coachsession_search_Tv.column("#3",minwidth=0,width=100)
		coachsession_search_Tv.heading("#4",text='Court(s)')
		coachsession_search_Tv.column("#4",minwidth=0,width=120)
		coachsession_search_Tv.heading("#5",text='Group')
		coachsession_search_Tv.column("#5",minwidth=0,width=120)
		coachsession_search_Tv.heading("#6",text='No. People')
		coachsession_search_Tv.column("#6",minwidth=0,width=80)
		coachsession_search_Tv.heading("#7",text='Technique')
		coachsession_search_Tv.column("#7",minwidth=0,width=100)
		coachsession_search_Tv.bind('<Button-1>', partial(treeviewresizedisable, coachsession_search_Tv))

		coachsession_ysearch_scrollbar = Scrollbar(self.coachSession, orient = 'vertical', command = coachsession_search_Tv.yview, cursor="tcross")
		coachsession_ysearch_scrollbar.place(relx=0.95,rely=0.22,anchor='center',height=109)
		coachsession_search_Tv.configure(yscrollcommand=coachsession_ysearch_scrollbar.set)

		calendar_label =Label(self.coachSession, text = 'Coaching Session Dates', fg ='black',bg='white',font=('serif',13,'bold'), bd=2, relief="ridge", padx=10, pady=3)
		calendar_label.place(rely=0.405,relx=0.715,anchor=CENTER)
		today = datetime.date.today()
		cal = Calendar(self.coachSession, font="serif 21", selectmode='day', cursor="tcross", year=today.year, month=today.month, day=today.day)
		cal.place(rely=0.67, relx=0.715, anchor='center')

		cal.bind("<<CalendarSelected>>", CalendarSelection)


		treeviewPopulate()
		changeCalendarColour()
		findMembers()


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
			coach_selection_dropdown = ttk.Combobox(self.coachSession, value=coach_name_choices, textvariable=self.coachNamesAndPasswords ,font=('serif', 8, 'bold'), width=25)
			coach_selection_dropdown.place(rely=0.362, relx=0.305, anchor='center')
			coach_selection_dropdown.config(state='readonly')


	def get_coach_details(self):
		conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
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