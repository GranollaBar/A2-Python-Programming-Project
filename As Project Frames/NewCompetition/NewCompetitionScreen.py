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
from CoachingSessionFrame.CoachingSessionEmail import SessionEmail
import time
from datetime import date, timedelta


CourtsTrue = False


class NewCompetitionContent:

	def __init__(self, mainScreen):
		self.competition = mainScreen
		self.conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
		self.c = self.conn.cursor()


		# self.c.execute("""CREATE TABLE SinglesCompetition (
		# 			username text,
		# 			username2 text,
		# 			start_date text,
		# 			end_date text,
		# 			court text,
		# 			singlescompetitionID integer
		# 			)""")
		#
		# self.c.execute("""CREATE TABLE DoublesCompetition (
		# 			username text,
		# 			username2 text,
		# 			username3 text,
		# 			username4 text,
		# 			start_date text,
		# 			end_date text,
		# 			team1 text,
		# 			team2 text,
		# 			doublescompetitionID integer
		# 			)""")


	def generateCompetitionContnt(self):

		def startDateCheck(dob):
			def assign_start_date():
				startDate.set(start_cal.get_date())
				startDateTop.withdraw()

			today = datetime.date.today()
			startDateTop = Toplevel(self.competition)

			start_cal = Calendar(startDateTop, font="Tahoma 16", date_pattern='dd/mm/yyyy',selectmode='day', cursor="tcross", year=today.year, month=today.month, day=today.day)
			start_cal.pack(fill="both", expand=True)
			ttk.Button(startDateTop, text="ok", command=assign_start_date).pack()


		def endDateCheck(dob):
			def assign_end_date():
				endDate.set(end_cal.get_date())
				endDateTop.withdraw()

			today = datetime.date.today()
			endDateTop = Toplevel(self.competition)

			end_cal = Calendar(endDateTop, font="Tahoma 16", date_pattern='dd/mm/yyyy',selectmode='day', cursor="tcross", year=today.year, month=today.month, day=today.day)
			end_cal.pack(fill="both", expand=True)
			ttk.Button(endDateTop, text="ok", command=assign_end_date).pack()


		def validate_competition_start_date(value, fieldname, label):
			if (value == ''):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " not not be empty")
				return False

			presentDate = datetime.datetime.now()
			date_formated = presentDate.strftime("%d/%m/%Y")

			d1 = datetime.datetime.strptime(value, "%d/%m/%Y").date()
			d2 = datetime.datetime.strptime(str(date_formated), "%d/%m/%Y").date()

			if d2>d1:
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " Can Not Be before the current date")
				return False

			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
			c = conn.cursor()

			c.execute("SELECT * FROM SinglesCompetition")
			singles_competition_array = c.fetchall()

			ColourDates = []

			for i in singles_competition_array:
				date_1 = datetime.datetime.strptime(i[2], "%d/%m/%Y")
				stringdate = date_1.date()
				ColourDates.append(i[2])
				ColourDates.append(i[3])

				while stringdate != i[3]:
					stringdateadd = stringdate + datetime.timedelta(days=1)
					finaldate=str(stringdateadd).split('-')
					finalnewdate=finaldate[0],finaldate[1],finaldate[2]
					a_date = datetime.date(int(finalnewdate[0]),int(finalnewdate[1]), int(finalnewdate[2]))

					date_2 = a_date.strftime("%d/%m/%Y")
					ColourDates.append(date_2)
					break

			for row in ColourDates:
				if value == row:
					label.config(fg="red")
					messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " can not be the same as a competition already created")
					return False
				else:
					pass

			conn.commit()
			conn.close()

			label.config(fg="SpringGreen3")
			return True


		def validate_competition_end_date(value, value2, fieldname, fieldname2, label2):
			if (value2 == ''):
				label2.config(fg="red")
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname2 + " can not be empty")
				return False
			if (value > value2):
				label2.config(fg="red")
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname2 + " can not be cannot be before the " + fieldname)
				return False
			if (value == value2):
				label2.config(fg="red")
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname2 + " can not be cannot be the same as the " + fieldname)
				return False

			date = value
			date=str(date).split('/')
			newdate=date[1],date[0],date[2]
			a_date = datetime.date(int(newdate[2]),int(newdate[0]), int(newdate[1]))

			date2 = value2
			date2=str(date2).split('/')
			newdate2=date2[1],date2[0],date2[2]
			a_date2 = datetime.date(int(newdate2[2]),int(newdate2[0]), int(newdate2[1]))

			numberdate = ((a_date2-a_date).days)

			if (numberdate >= 3):
				label2.config(fg='red')
				messagebox.showinfo("Validation Error", "The competition can only be ran for three days total")
				return False
			else:
				pass

			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
			c = conn.cursor()

			c.execute("SELECT * FROM SinglesCompetition")
			singles_competition_array = c.fetchall()

			ColourDates = []

			for i in singles_competition_array:
				date_1 = datetime.datetime.strptime(i[2], "%d/%m/%Y")
				stringdate = date_1.date()
				ColourDates.append(i[2])
				ColourDates.append(i[3])

				while stringdate != i[3]:
					stringdateadd = stringdate + datetime.timedelta(days=1)
					finaldate=str(stringdateadd).split('-')
					finalnewdate=finaldate[0],finaldate[1],finaldate[2]
					a_date = datetime.date(int(finalnewdate[0]),int(finalnewdate[1]), int(finalnewdate[2]))

					date_2 = a_date.strftime("%d/%m/%Y")
					ColourDates.append(date_2)
					break

			for row in ColourDates:
				if value2 == row:
					label2.config(fg="red")
					messagebox.showinfo("Validation Error", "The Value For Field " + fieldname2 + " can not be the same as a competition already created")
					return False
				else:
					pass

			conn.commit()
			conn.close()

			label2.config(fg="SpringGreen3")
			return True


		def validate_first_member(value, fieldname, label):
			if (value == ''):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " Can Not Be empty")
				return False

			label.config(fg="SpringGreen3")
			return True


		def validate_second_member(value, value2, fieldname, fieldname3, label, label2):
			if (value2 == ''):
				label2.config(fg="red")
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname3 + " Can Not Be empty")
				return False
			if (value == value2):
				label.config(fg="red")
				label2.config(fg="red")
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " Can not have the same username")
				return False

			label.config(fg="SpringGreen3")
			label2.config(fg="SpringGreen3")
			return True


		def validate_court(value, fieldname, label):
			if (value != True):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " must have at least 1 selected")
				return False

			label.config(fg="SpringGreen3")
			return True


		def clearTv(treeview):
			record=treeview.get_children()
			for elements in record:
				treeview.delete(elements)


		def treeviewPopulate(treeview):
			clearTv(treeview)

			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
			c = conn.cursor()

			c.execute("SELECT * From SinglesCompetition")
			items = c.fetchall()

			conn.commit()
			conn.close()

			count=0
			for row in items:
				if row == []:
					pass
				else:
					if count%2==0:
						treeview.insert('','end',text=row[0],values=(row[1],row[2],row[3],row[4],row[5]))
					else:
						treeview.insert('','end',text=row[0],values=(row[1],row[2],row[3],row[4],row[5]))
					count+=1


		def returnColour(usernameReturn, username2Return, startDateReturn, endDateReturn, CourtReturn):
			usernameReturn.config(fg="black")
			username2Return.config(fg="black")
			startDateReturn.config(fg="black")
			endDateReturn.config(fg="black")
			CourtReturn.config(fg="black")


		def ClickedCourt(courtvalue):
			if (courtvalue.cget('bg') == 'black'):
				courtvalue.config(bg='SpringGreen3')
			else:
				courtvalue.config(bg='black')


		def courtRequired():
			courts = Toplevel(self.competition, bg="white")
			courts.geometry('500x500')
			courts.attributes('-topmost', 1)

			title_label =Label(courts, cursor="tcross",text = 'Select the Number of Courts Required', fg ='black',bg='white',font=('Tahoma',11,'bold'), bd=2, relief="ridge", padx=10, pady=3)
			title_label.place(rely=0.027,relx=0.5,anchor=CENTER)


			CourtsImage = PhotoImage(file="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Images/courts.png")


			Court1label =Label(courts, text = 'Court 1', fg ='black',bg='white',font=('Tahoma',7,'bold'), bd=2, relief="ridge", padx=10, pady=3)
			Court1label.place(rely=0.155,relx=0.15,anchor=CENTER)
			Court1Button = Button(courts, text='1', cursor="tcross", image=CourtsImage, width=95, height=53, command=lambda : ClickedCourt(Court1Button), bg="black", highlightthickness=5, activebackground="grey")
			Court1Button.place(rely=0.24,relx=0.15,anchor=CENTER)
			Court1Button.image = CourtsImage


			Court2label =Label(courts, text = 'Court 2', fg ='black',bg='white',font=('Tahoma',7,'bold'), bd=2, relief="ridge", padx=10, pady=3)
			Court2label.place(rely=0.375,relx=0.15,anchor=CENTER)
			Court2Button = Button(courts, text='2', cursor="tcross", image=CourtsImage, width=95, height=53, command=lambda : ClickedCourt(Court2Button), bg="black", highlightthickness=5, activebackground="grey")
			Court2Button.place(rely=0.46,relx=0.15,anchor=CENTER)
			Court2Button.image = CourtsImage


			Court3label =Label(courts, text = 'Court 3', fg ='black',bg='white',font=('Tahoma',7,'bold'), bd=2, relief="ridge", padx=10, pady=3)
			Court3label.place(rely=0.595,relx=0.15,anchor=CENTER)
			Court3Button = Button(courts, text='3', cursor="tcross", image=CourtsImage, width=95, height=53, command=lambda : ClickedCourt(Court3Button), bg="black", highlightthickness=5, activebackground="grey")
			Court3Button.place(rely=0.68,relx=0.15,anchor=CENTER)
			Court3Button.image = CourtsImage


			Court4label =Label(courts, text = 'Court 4', fg ='black',bg='white',font=('Tahoma',7,'bold'), bd=2, relief="ridge", padx=10, pady=3)
			Court4label.place(rely=0.815,relx=0.15,anchor=CENTER)
			Court4Button = Button(courts, text='4', cursor="tcross", image=CourtsImage, width=95, height=53, command=lambda : ClickedCourt(Court4Button), bg="black", highlightthickness=5, activebackground="grey")
			Court4Button.place(rely=0.9,relx=0.15,anchor=CENTER)
			Court4Button.image = CourtsImage


			Court5label =Label(courts, text = 'Court 5', fg ='black',bg='white',font=('Tahoma',7,'bold'), bd=2, relief="ridge", padx=10, pady=3)
			Court5label.place(rely=0.155,relx=0.5,anchor=CENTER)
			Court5Button = Button(courts, text='5', cursor="tcross", image=CourtsImage, width=95, height=53, command=lambda : ClickedCourt(Court5Button), bg="black", highlightthickness=5, activebackground="grey")
			Court5Button.place(rely=0.24,relx=0.5,anchor=CENTER)
			Court5Button.image = CourtsImage


			Court6label =Label(courts, text = 'Court 6', fg ='black',bg='white',font=('Tahoma',7,'bold'), bd=2, relief="ridge", padx=10, pady=3)
			Court6label.place(rely=0.375,relx=0.5,anchor=CENTER)
			Court6Button = Button(courts, text='6', cursor="tcross", image=CourtsImage, width=95, height=53, command=lambda : ClickedCourt(Court6Button), bg="black", highlightthickness=5, activebackground="grey")
			Court6Button.place(rely=0.46,relx=0.5,anchor=CENTER)
			Court6Button.image = CourtsImage


			Court7label =Label(courts, text = 'Court 7', fg ='black',bg='white',font=('Tahoma',7,'bold'), bd=2, relief="ridge", padx=10, pady=3)
			Court7label.place(rely=0.595,relx=0.5,anchor=CENTER)
			Court7Button = Button(courts, text='7', cursor="tcross", image=CourtsImage, width=95, height=53, command=lambda : ClickedCourt(Court7Button), bg="black", highlightthickness=5, activebackground="grey")
			Court7Button.place(rely=0.68,relx=0.5,anchor=CENTER)
			Court7Button.image = CourtsImage


			Court8label =Label(courts, text = 'Court 8', fg ='black',bg='white',font=('Tahoma',7,'bold'), bd=2, relief="ridge", padx=10, pady=3)
			Court8label.place(rely=0.815,relx=0.5,anchor=CENTER)
			Court8Button = Button(courts, text='8', cursor="tcross", image=CourtsImage, width=95, height=53, command=lambda : ClickedCourt(Court8Button), bg="black", highlightthickness=5, activebackground="grey")
			Court8Button.place(rely=0.9,relx=0.5,anchor=CENTER)
			Court8Button.image = CourtsImage


			Court9label =Label(courts, text = 'Court 9', fg ='black',bg='white',font=('Tahoma',7,'bold'), bd=2, relief="ridge", padx=10, pady=3)
			Court9label.place(rely=0.155,relx=0.85,anchor=CENTER)
			Court9Button = Button(courts, text='9', cursor="tcross", image=CourtsImage, width=95, height=53, command=lambda : ClickedCourt(Court9Button), bg="black", highlightthickness=5, activebackground="grey")
			Court9Button.place(rely=0.24,relx=0.85,anchor=CENTER)
			Court9Button.image = CourtsImage


			Court10label =Label(courts, text = 'Court 10', fg ='black',bg='white',font=('Tahoma',7,'bold'), bd=2, relief="ridge", padx=10, pady=3)
			Court10label.place(rely=0.375,relx=0.85,anchor=CENTER)
			Court10Button = Button(courts, text='10', cursor="tcross", image=CourtsImage, width=95, height=53, command=lambda : ClickedCourt(Court10Button), bg="black", highlightthickness=5, activebackground="grey")
			Court10Button.place(rely=0.46,relx=0.85,anchor=CENTER)
			Court10Button.image = CourtsImage


			Court11label =Label(courts, text = 'Court 11', fg ='black',bg='white',font=('Tahoma',7,'bold'), bd=2, relief="ridge", padx=10, pady=3)
			Court11label.place(rely=0.595,relx=0.85,anchor=CENTER)
			Court11Button = Button(courts, text='11', cursor="tcross", image=CourtsImage, width=95, height=53, command=lambda : ClickedCourt(Court11Button), bg="black", highlightthickness=5, activebackground="grey")
			Court11Button.place(rely=0.68,relx=0.85,anchor=CENTER)
			Court11Button.image = CourtsImage


			Court12label =Label(courts, text = 'Court 12', fg ='black',bg='white',font=('Tahoma',7,'bold'), bd=2, relief="ridge", padx=10, pady=3)
			Court12label.place(rely=0.815,relx=0.85,anchor=CENTER)
			Court12Button = Button(courts, text='12', cursor="tcross", image=CourtsImage, width=95, height=53, command=lambda : ClickedCourt(Court12Button), bg="black", highlightthickness=5, activebackground="grey")
			Court12Button.place(rely=0.9,relx=0.85,anchor=CENTER)
			Court12Button.image = CourtsImage


			SelectCourtsButton=Button(courts, cursor="tcross",text = 'Select Courts', command = lambda : ChangeCourtsColour(courts,Court1Button, Court2Button, Court3Button, Court4Button, Court5Button, Court6Button, Court7Button, Court8Button, Court9Button, Court10Button, Court11Button, Court12Button), fg ='white', bg='black', relief= 'groove', font = ('Verdana',8,'bold'), padx =15)
			SelectCourtsButton.place(rely=0.095,relx=0.5,anchor=CENTER)


		def ChangeCourtsColour(frame, courtvalue, courtvalue2, courtvalue3, courtvalue4, courtvalue5, courtvalue6, courtvalue7, courtvalue8, courtvalue9, courtvalue10, courtvalue11, courtvalue12):
			global FinalSelectedCourts
			global CourtsTrue

			counter = 1
			SelectedCourts = []

			courts = [courtvalue, courtvalue2, courtvalue3, courtvalue4, courtvalue5, courtvalue6,
					  courtvalue7, courtvalue8, courtvalue9, courtvalue10, courtvalue11, courtvalue12]

			if (courtvalue.cget('bg') != 'SpringGreen3' and courtvalue2.cget('bg') != 'SpringGreen3' and courtvalue3.cget('bg') != 'SpringGreen3' and courtvalue4.cget('bg') != 'SpringGreen3' and courtvalue5.cget('bg') != 'SpringGreen3' and courtvalue6.cget('bg') != 'SpringGreen3' and courtvalue7.cget('bg') != 'SpringGreen3' and courtvalue8.cget('bg') != 'SpringGreen3' and courtvalue9.cget('bg') != 'SpringGreen3' and courtvalue10.cget('bg') != 'SpringGreen3' and courtvalue11.cget('bg') != 'SpringGreen3' and courtvalue12.cget('bg') != 'SpringGreen3'):
				messagebox.showinfo('Info', 'Please select a court to continue')

			else:

				for court in courts:
					if (str(counter) == court.cget('text') and court.cget('bg') == 'SpringGreen3'):
						FinalCourt = str(counter)
						SelectedCourts.append(FinalCourt)

					counter += 1

				if (len(SelectedCourts) > 1):
					messagebox.showinfo('Info', 'Only one court can be selected per competition')
					courtvalue.config(bg='black')
					courtvalue2.config(bg='black')
					courtvalue3.config(bg='black')
					courtvalue4.config(bg='black')
					courtvalue5.config(bg='black')
					courtvalue6.config(bg='black')
					courtvalue7.config(bg='black')
					courtvalue8.config(bg='black')
					courtvalue9.config(bg='black')
					courtvalue10.config(bg='black')
					courtvalue11.config(bg='black')
					courtvalue12.config(bg='black')

				else:
					CourtsTrue = True
					frame.withdraw()

					FinalSelectedCourts = ''
					for court in SelectedCourts:
						FinalSelectedCourts = FinalSelectedCourts + court + ", "

					FinalSelectedCourts = FinalSelectedCourts[0: len(FinalSelectedCourts) - 2]

					return FinalSelectedCourts


		def CalendarSelection(cal, event=None):
			ListComplete = False
			AllListComplete = 0

			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
			c = conn.cursor()

			c.execute("SELECT * FROM SinglesCompetition")
			singles_competition_array = c.fetchall()

			date = cal.get_date()
			date=str(date).split('/')
			newdate=date[0],date[1],date[2]
			a_date = datetime.date(int('20'+newdate[2]),int(newdate[0]), int(newdate[1]))
			a_date.strftime('%Y-%m-%d')

			current_day=str(a_date).split('-')

			for i in singles_competition_array:
				start=str(i[2]).split('/')
				end=str(i[3]).split('/')
				AllListComplete += 1

				if current_day[1] == start[1] and current_day[2] >= start[0] and current_day[2] <= end[0]:
					ListComplete = True
					messagebox.showinfo("info", "There is a singles competition on these dates" + "\n" +
																	"The details are listed below:" + "\n\n"
																	+ "Member 1: " + str(i[0]) + "\n"
																	+ "Member 2: " + str(i[1]) + "\n"
																	+ "Start Date: " + str(i[2]) + "\n"
																	+ "End Date: " + str(i[3]) + "\n"
																	+ "Court: " + str(i[4]) + "\n")

				if (ListComplete == False and AllListComplete == len(singles_competition_array)):
					messagebox.showinfo("info", "There is no competition on this date")


		def changeCalendarColour(cal):
			cal.calevent_remove("all")
			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
			c = conn.cursor()

			c.execute("SELECT * FROM SinglesCompetition")
			singles_competition_array = c.fetchall()

			ColourDates = []

			for i in singles_competition_array:
				date_1 = datetime.datetime.strptime(i[2], "%d/%m/%Y")
				stringdate = date_1.date()
				ColourDates.append(i[2])
				ColourDates.append(i[3])

				while stringdate != i[3]:
					stringdateadd = stringdate + datetime.timedelta(days=1)
					finaldate=str(stringdateadd).split('-')
					finalnewdate=finaldate[0],finaldate[1],finaldate[2]
					a_date = datetime.date(int(finalnewdate[0]),int(finalnewdate[1]), int(finalnewdate[2]))

					date_2 = a_date.strftime("%d/%m/%Y")
					ColourDates.append(date_2)
					break

			for row in ColourDates:
				finalfinaldate=str(row).split('/')
				cal.calevent_create(datetime.date(int(finalfinaldate[2]), int(finalfinaldate[1]), int(finalfinaldate[0])),"View Coaching Session Details","message")

			cal.tag_config("message", background="SpringGreen3", foreground="black")

			conn.commit()
			conn.close()


		def SearchNewSingles():
			pass


		def SubmitNewSingles(label1, label2, label3, label4, label5, cal, treeview):
			AllEmailsComplete = 0

			isValid = True
			isValid = isValid and validate_first_member(memberNamesAndPasswords.get(), "Member", label1)
			isValid = isValid and validate_second_member(memberNamesAndPasswords.get(), memberNamesAndPasswords2.get(), "Members", "Member2", label1, label2)
			isValid = isValid and validate_competition_start_date(startDate.get(), "Start Date", label3)
			isValid = isValid and validate_competition_end_date(startDate.get(), endDate.get(), "Start Date", "End Date", label4)
			isValid = isValid and validate_court(CourtsTrue, "Court", label5)

			if isValid:
				FinalMember1 = memberNamesAndPasswords.get()
				FinalMember2 = memberNamesAndPasswords2.get()
				FinalStartDate = startDate.get()
				FinalEndDate = endDate.get()
				FinalCourt = FinalSelectedCourts

				response = askyesno("Are you sure?", "Are you sure that all information above is correct?")
				if response == False:
					showinfo("Info", "submition cancelled")

				else:
					conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
					c = conn.cursor()

					c.execute("SELECT * From member")
					items = c.fetchall()

					for row in items:
						if str(row[0]) != str(memberNamesAndPasswords.get()) or str(row[0]) != str(memberNamesAndPasswords2.get()):
							pass
							AllEmailsComplete += 1
						else:
							member_name = row[0]
							SessionEmail("New Singles Competition Date Set", "A coach at Lisburn Racquets Club has set up a new singles competition. The start and end date of the competition is listed below:" + "\n\n" + "Start Date: " + FinalStartDate + "\n" + "End Date: " + FinalEndDate + "\n\n" + "Court: " + FinalCourt + "\n\n" + "Check the opening and closing times of the club as you will need to complete the competition between them" + "\n" + "Thanks for choosing Lisburn Racquets Club", member_name, label1)
							AllEmailsComplete += 1
							if (AllEmailsComplete == len(items)):
								messagebox.showinfo('Info', 'All members involved have been sent information about the upcoming competition')

					c.execute("SELECT * FROM competition")
					competition_array = c.fetchall()
					newId = len(competition_array) + 1

					c.execute("INSERT INTO SinglesCompetition VALUES (:member1, :member2, :startDate, :endDate, :court, :singlescompetitionID)",
							   {
								   'member1': FinalMember1,
								   'member2': FinalMember2,
								   'startDate': FinalStartDate,
								   'endDate': FinalEndDate,
								   'court': FinalSelectedCourts,
								   'singlescompetitionID': newId,
							   })

					conn.commit()
					conn.close()

					changeCalendarColour(cal)

					memberNamesAndPasswords.set('')
					memberNamesAndPasswords2.set('')

					returnColour(label1, label2, label3, label4, label5)
					messagebox.showinfo("info", "Details have been successfully stored")

			treeviewPopulate(treeview)


		def MatchTypeConfirmation(value, value2, value3, value4):
			value.config(fg='grey')
			value2.config(state='disabled')
			value3.config(state='disabled')
			value4.config(state='disabled')

			competition_status_label = tkinter.Label(self.competition, text="Competition Status:", font=('Tahoma', 12, 'bold'), fg='black', bg='white')
			competition_status_label.place(rely=0.198, relx=0.14, anchor='center')

			competition_status_new = Radiobutton(self.competition, text="Create New", variable=CompetitionStatus, value=1, font=("Tahoma",9, 'bold'), cursor="tcross", bg="white", bd=2, relief="ridge")
			competition_status_new.place(rely=0.2, relx=0.294, anchor='center')

			competition_status_join = Radiobutton(self.competition, text="Join Existing", variable=CompetitionStatus, value=2, font=("Tahoma",9, 'bold'), cursor="tcross", bg="white", bd=2, relief="ridge")
			competition_status_join.place(rely=0.2, relx=0.43, anchor='center')

			competition_status_update = Radiobutton(self.competition, text="Update Existing", variable=CompetitionStatus, value=3, font=("Tahoma",9, 'bold'), cursor="tcross", bg="white", bd=2, relief="ridge")
			competition_status_update.place(rely=0.2, relx=0.577, anchor='center')

			competition_status_delete = Radiobutton(self.competition, text="Delete Existing", variable=CompetitionStatus, value=4, font=("Tahoma",9, 'bold'), cursor="tcross", bg="white", bd=2, relief="ridge")
			competition_status_delete.place(rely=0.2, relx=0.73, anchor='center')
			CompetitionStatus.set("1")

			competition_status_button = tkinter.Button(self.competition, cursor="tcross",text="Select Status", command= lambda : CompetitionStatusConfirmation(value, value2, value3, value4, competition_status_label, competition_status_new, competition_status_join, competition_status_update, competition_status_delete, competition_status_button), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 9, 'bold'), padx=2)
			competition_status_button.place(rely=0.1995, relx=0.87, anchor='center')

			competition_status_line = Canvas(self.competition, width=1000, height=2)
			competition_status_line.config(bg='black')
			competition_status_line.create_line(3, 0, 200, 100000)
			competition_status_line.place(rely=0.233, relx=0.5, anchor='center')


		def CompetitionStatusConfirmation(value, value2, value3, value4, value5, value6, value7, value8, value9, value10):
			value5.config(fg='grey')
			value6.config(state='disabled')
			value7.config(state='disabled')
			value8.config(state='disabled')
			value9.config(state='disabled')
			value10.config(state='disabled')

			if (MatchType.get() == 1 and CompetitionStatus.get() == 1):
				username_label = tkinter.Label(self.competition, text="Member 1:", font=('Tahoma', 15, 'bold'), fg='black', bg='white')
				username_label.place(rely=0.29, relx=0.09, anchor='center')

				username2_label = tkinter.Label(self.competition, text="Member 2:", font=('Tahoma', 15, 'bold'), fg='black', bg='white')
				username2_label.place(rely=0.37, relx=0.09, anchor='center')


				conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
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

				member_name_choices = member_name_list

				coach_selection_dropdown = ttk.Combobox(self.competition, value=member_name_choices, textvariable=memberNamesAndPasswords ,font=('Tahoma', 9, 'bold'), width=25)
				coach_selection_dropdown.place(rely=0.293, relx=0.277, anchor='center')
				coach_selection_dropdown.config(state='readonly')

				coach_selection_dropdown2 = ttk.Combobox(self.competition, value=member_name_choices, textvariable=memberNamesAndPasswords2 ,font=('Tahoma', 9, 'bold'), width=25)
				coach_selection_dropdown2.place(rely=0.373, relx=0.277, anchor='center')
				coach_selection_dropdown2.config(state='readonly')


				start_date_label = tkinter.Label(self.competition, text="Start Date:", font=('Tahoma', 15, 'bold'), fg='black', bg='white')
				start_date_label.place(rely=0.45, relx=0.09, anchor='center')

				end_date_label = tkinter.Label(self.competition, text="End Date:", font=('Tahoma', 15, 'bold'), fg='black', bg='white')
				end_date_label.place(rely=0.53, relx=0.09, anchor='center')

				start_date_entry = Button(self.competition, text='Select Start Date',font=("Tahoma",10, 'bold'), cursor="tcross",command=lambda : startDateCheck(startDate), padx=10, bd=4, relief="ridge")
				start_date_entry.place(rely=0.453, relx=0.277, anchor='center')

				end_date_entry = Button(self.competition, text='Select End Date',font=("Tahoma",10, 'bold'), cursor="tcross",command=lambda : endDateCheck(endDate), padx=10, bd=4, relief="ridge")
				end_date_entry.place(rely=0.533, relx=0.277, anchor='center')

				court_label = tkinter.Label(self.competition, text="Court:", font=('Tahoma', 15, 'bold'), fg='black', bg='white')
				court_label.place(rely=0.61, relx=0.09, anchor='center')

				court_button = Button(self.competition, text='Select Court',font=("Tahoma",10, 'bold'), cursor="tcross",command=courtRequired, padx=10, bd=4, relief="ridge")
				court_button.place(rely=0.613, relx=0.277, anchor='center')


				calendar_label =Label(self.competition, text = 'Competition Dates', fg ='black',bg='white',font=('Tahoma',11,'bold'), bd=2, relief="ridge", padx=10, pady=3)
				calendar_label.place(rely=0.286,relx=0.67,anchor=CENTER)
				today = datetime.date.today()
				cal = Calendar(self.competition, font="Tahoma 16", selectmode='day', cursor="tcross", year=today.year, month=today.month, day=today.day)
				cal.place(rely=0.51, relx=0.67, anchor='center')
				cal.bind("<<CalendarSelected>>", partial(CalendarSelection, cal))


				singles_competition_treeview=ttk.Treeview(self.competition,height=6,columns=('Member 2','Start Date','End Date','Court'))
				singles_competition_treeview.place(relx=0.5,rely=0.86,anchor=CENTER)

				singles_competition_treeview.heading("#0",text='Member 1')
				singles_competition_treeview.column("#0",minwidth=0,width=250)
				singles_competition_treeview.heading("#1",text='Member 2')
				singles_competition_treeview.column("#1",minwidth=0,width=250)
				singles_competition_treeview.heading("#2",text='Start Date')
				singles_competition_treeview.column("#2",minwidth=0,width=145)
				singles_competition_treeview.heading("#3",text='End Date')
				singles_competition_treeview.column("#3",minwidth=0,width=145)
				singles_competition_treeview.heading("#4",text='Court')
				singles_competition_treeview.column("#4",minwidth=0,width=145)

				singles_competition_ysearch_scrollbar = Scrollbar(self.competition, orient = 'vertical', command = singles_competition_treeview.yview, cursor="tcross")
				singles_competition_ysearch_scrollbar.place(relx=0.98,rely=0.86,anchor='center',height=147)
				singles_competition_treeview.configure(yscrollcommand=singles_competition_ysearch_scrollbar.set)

				treeviewPopulate(singles_competition_treeview)
				changeCalendarColour(cal)

				search_new_singles_button = tkinter.Button(self.competition, cursor="tcross",text="Search", command=SearchNewSingles, fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 11, 'bold'), padx=30, pady=2)
				search_new_singles_button.place(rely=0.695, relx=0.12, anchor='center')

				submit_new_singles_button = tkinter.Button(self.competition, cursor="tcross",text="Submit", command=lambda : SubmitNewSingles(username_label, username2_label, start_date_label, end_date_label, court_label, cal, singles_competition_treeview), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 11, 'bold'), padx=30, pady=2)
				submit_new_singles_button.place(rely=0.695, relx=0.28, anchor='center')


			if (MatchType.get() == 2 and CompetitionStatus.get() == 1):
				pass



			if (MatchType.get() == 1 and CompetitionStatus.get() == 2):
				group_selection_label = tkinter.Label(self.competition, text="Which Competition Do You Want to Join:", font=('Tahoma', 12, 'bold'), fg='black', bg='white')
				group_selection_label.place(rely=0.268, relx=0.317, anchor='center')

				group_selection_dropdown = ttk.Combobox(self.competition, value='1',font=('Tahoma', 11, 'bold'), width=4)
				group_selection_dropdown.place(rely=0.27, relx=0.542, anchor='center')
				group_selection_dropdown.config(state='readonly')

				group_selection_button = tkinter.Button(self.competition, cursor="tcross",text="Select Group", command=first, fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 9, 'bold'), padx=2)
				group_selection_button.place(rely=0.2695, relx=0.654, anchor='center')

				group_selection_line = Canvas(self.competition, width=1000, height=2)
				group_selection_line.config(bg='black')
				group_selection_line.create_line(3, 0, 200, 100000)
				group_selection_line.place(rely=0.303, relx=0.5, anchor='center')


				doubles_competition_treeview=ttk.Treeview(self.competition,height=5,columns=('Member 2','Member 3','Member 4','Start Date','End Date','Team 1','Team 2'))
				doubles_competition_treeview.place(relx=0.5,rely=0.86,anchor=CENTER)

				doubles_competition_treeview.heading("#0",text='Member 1')
				doubles_competition_treeview.column("#0",minwidth=0,width=120)
				doubles_competition_treeview.heading("#1",text='Member 2')
				doubles_competition_treeview.column("#1",minwidth=0,width=120)
				doubles_competition_treeview.heading("#2",text='Member 3')
				doubles_competition_treeview.column("#2",minwidth=0,width=120)
				doubles_competition_treeview.heading("#3",text='Member 4')
				doubles_competition_treeview.column("#3",minwidth=0,width=120)
				doubles_competition_treeview.heading("#4",text='Start Date')
				doubles_competition_treeview.column("#4",minwidth=0,width=80)
				doubles_competition_treeview.heading("#5",text='End Date')
				doubles_competition_treeview.column("#5",minwidth=0,width=80)
				doubles_competition_treeview.heading("#6",text='Team 1')
				doubles_competition_treeview.column("#6",minwidth=0,width=150)
				doubles_competition_treeview.heading("#7",text='Team 2')
				doubles_competition_treeview.column("#7",minwidth=0,width=150)

				doubles_competition_ysearch_scrollbar = Scrollbar(self.competition, orient = 'vertical', command = doubles_competition_treeview.yview, cursor="tcross")
				doubles_competition_ysearch_scrollbar.place(relx=0.976,rely=0.86,anchor='center',height=127)
				doubles_competition_treeview.configure(yscrollcommand=doubles_competition_ysearch_scrollbar.set)


			if (MatchType.get() == 2 and CompetitionStatus.get() == 2):
				group_selection_label = tkinter.Label(self.competition, text="Which Competition Do You Want to Join:", font=('Tahoma', 12, 'bold'), fg='black', bg='white')
				group_selection_label.place(rely=0.268, relx=0.317, anchor='center')

				group_selection_dropdown = ttk.Combobox(self.competition, value='1',font=('Tahoma', 11, 'bold'), width=4)
				group_selection_dropdown.place(rely=0.27, relx=0.542, anchor='center')
				group_selection_dropdown.config(state='readonly')

				group_selection_button = tkinter.Button(self.competition, cursor="tcross",text="Select Group", command=first, fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 9, 'bold'), padx=2)
				group_selection_button.place(rely=0.2695, relx=0.654, anchor='center')

				group_selection_line = Canvas(self.competition, width=1000, height=2)
				group_selection_line.config(bg='black')
				group_selection_line.create_line(3, 0, 200, 100000)
				group_selection_line.place(rely=0.303, relx=0.5, anchor='center')




		MatchType=IntVar()
		CompetitionStatus=IntVar()

		memberNamesAndPasswords = StringVar()
		memberNamesAndPasswords2 = StringVar()
		startDate=StringVar()
		endDate=StringVar()


		match_type_label = tkinter.Label(self.competition, text="Type of Match:", font=('Tahoma', 12, 'bold'), fg='black', bg='white')
		match_type_label.place(rely=0.128, relx=0.33, anchor='center')

		match_type_singles = Radiobutton(self.competition, text="Singles", variable=MatchType, value=1, font=("Tahoma",9, 'bold'), cursor="tcross", bg="white", bd=2, relief="ridge")
		match_type_singles.place(rely=0.13, relx=0.45, anchor='center')

		match_type_doubles = Radiobutton(self.competition, text="Doubles", variable=MatchType, value=2, font=("Tahoma",9, 'bold'), cursor="tcross", bg="white", bd=2, relief="ridge")
		match_type_doubles.place(rely=0.13, relx=0.55, anchor='center')
		MatchType.set("1")

		match_type_button = tkinter.Button(self.competition, cursor="tcross",text="Select Match Type", command=lambda : MatchTypeConfirmation(match_type_label, match_type_singles, match_type_doubles, match_type_button), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 9, 'bold'), padx=2)
		match_type_button.place(rely=0.1295, relx=0.685, anchor='center')

		match_type_line = Canvas(self.competition, width=1000, height=2)
		match_type_line.config(bg='black')
		match_type_line.create_line(3, 0, 200, 100000)
		match_type_line.place(rely=0.163, relx=0.5, anchor='center')








