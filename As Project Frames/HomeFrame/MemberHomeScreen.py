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
from CoachingSessionFrame.CoachingSessionEmail import SessionEmail
import time
from datetime import date, datetime,timedelta
import datetime
from LoginFrame.AS_programming_loginscreen import loginUsername


class MemberHomeContent:

	def __init__(self, mainScreen):
		self.MemberHome = mainScreen


	def generateMemberHomeContnt(self):

		def AllCalendarSelection(event):
			AllChangeSelection = False

			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
			c = conn.cursor()

			date = cal.get_date()
			date=str(date).split('/')
			newdate=date[0],date[1],date[2]
			a_date = datetime.date(int('20'+newdate[2]),int(newdate[0]), int(newdate[1]))

			string_date = a_date.strftime("%d/%m/%Y")

			c.execute("SELECT * From coachSessionDetails WHERE date=?", (string_date,))
			items = c.fetchone()

			if items:
				AllChangeSelection = True
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


			c.execute("SELECT * FROM SinglesCompetition WHERE username=:memberusername OR username2=:memberusername", {
				"memberusername": loginUsername.get()
			})
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

				if current_day[1] == start[1] and current_day[2] >= start[0] and current_day[2] <= end[0]:
					AllChangeSelection = True
					messagebox.showinfo("Info", "There is a singles competition on these dates" + "\n" +
										"The details are listed below:" + "\n\n"
										+ "Member 1: " + str(i[0]) + "\n"
										+ "Member 2: " + str(i[1]) + "\n"
										+ "Start Date: " + str(i[2]) + "\n"
										+ "End Date: " + str(i[3]) + "\n"
										+ "Court: " + str(i[4]) + "\n"
										, icon='info')

			conn.commit()


			c.execute("SELECT * FROM DoublesCompetition WHERE username=:memberusername OR username2=:memberusername OR username3=:memberusername OR username4=:memberusername", {
				"memberusername": loginUsername.get()
			})
			doubles_competition_array = c.fetchall()

			date = cal.get_date()
			date=str(date).split('/')
			newdate=date[0],date[1],date[2]
			a_date = datetime.date(int('20'+newdate[2]),int(newdate[0]), int(newdate[1]))
			a_date.strftime('%Y-%m-%d')

			current_day=str(a_date).split('-')

			for i in doubles_competition_array:
				start=str(i[4]).split('/')
				end=str(i[5]).split('/')

				if current_day[1] == start[1] and current_day[2] >= start[0] and current_day[2] <= end[0]:
					AllChangeSelection = True
					messagebox.showinfo("Info", "There is a doubles competition on these dates" + "\n" +
										"The details are listed below:" + "\n\n"
										+ "Member 1: " + str(i[0]) + "\n"
										+ "Member 2: " + str(i[1]) + "\n"
										+ "Member 3: " + str(i[2]) + "\n"
										+ "Member 4: " + str(i[3]) + "\n"
										+ "Start Date: " + str(i[4]) + "\n"
										+ "End Date: " + str(i[5]) + "\n"
										+ "Court: " + str(i[6]) + "\n"
										+ "Team 1: " + str(i[7]) + "\n"
										+ "Team 2: " + str(i[8]) + "\n"
										, icon='info')

			conn.commit()
			conn.close()


			if (AllChangeSelection == False):
				messagebox.showinfo('Error', 'There is currently no event for you on the date selected', icon='error')


		def changeCalendarColour(cal):
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


		def SinglesChangeCalendarColour(cal):
			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
			c = conn.cursor()

			c.execute("SELECT * FROM SinglesCompetition WHERE username=:memberusername OR username2=:memberusername", {
				"memberusername": loginUsername.get()
			})
			singles_competition_array = c.fetchall()

			for dates in singles_competition_array:
				start_date = dates[2]
				end_date = dates[3]

				d1=start_date.split('/')
				d2=end_date.split('/')

				d1= datetime.datetime(int(d1[2]),int(d1[1]),int(d1[0]))
				d2= datetime.datetime(int(d2[2]),int(d2[1]),int(d2[0]))

				length_inbetween=str(d2-d1).strip(' days, 0:00:00')

				d1=start_date.split('/')
				d1= datetime.datetime(int(d1[2]),int(d1[1]),int(d1[0]))

				all_days_inbetween=[]

				for i in range(0,int(length_inbetween)+1):
					add=str(d1+timedelta(days=i)).strip('datetime.date(')
					add=str(d1+timedelta(days=i)).strip(') 00:00:00')
					add=add.split('-')
					add=add[2].strip(',')+'/'+add[1].strip(',')+'/'+add[0].strip(',')
					all_days_inbetween.append(add)

				if end_date not in all_days_inbetween:
					all_days_inbetween.append(end_date)

				for finaldates in all_days_inbetween:
					finalfinaldate=str(finaldates).split('/')
					cal.calevent_create(datetime.date(int(finalfinaldate[2]), int(finalfinaldate[1]), int(finalfinaldate[0])),"View Coaching Session Details","message")

				cal.tag_config("message", background="SpringGreen3", foreground="black")

			conn.close()


		def DoublesChangeCalendarColour(cal):
			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
			c = conn.cursor()

			c.execute("SELECT * FROM DoublesCompetition WHERE username=:memberusername OR username2=:memberusername OR username3=:memberusername OR username4=:memberusername", {
				"memberusername": loginUsername.get()
			})
			doubles_competition_array = c.fetchall()

			for dates in doubles_competition_array:
				start_date = dates[4]
				end_date = dates[5]

				d1=start_date.split('/')
				d2=end_date.split('/')

				d1= datetime.datetime(int(d1[2]),int(d1[1]),int(d1[0]))
				d2= datetime.datetime(int(d2[2]),int(d2[1]),int(d2[0]))

				length_inbetween=str(d2-d1).strip(' days, 0:00:00')

				d1=start_date.split('/')
				d1= datetime.datetime(int(d1[2]),int(d1[1]),int(d1[0]))

				all_days_inbetween=[]

				for i in range(0,int(length_inbetween)+1):
					add=str(d1+timedelta(days=i)).strip('datetime.date(')
					add=str(d1+timedelta(days=i)).strip(') 00:00:00')
					add=add.split('-')
					add=add[2].strip(',')+'/'+add[1].strip(',')+'/'+add[0].strip(',')
					all_days_inbetween.append(add)

				if end_date not in all_days_inbetween:
					all_days_inbetween.append(end_date)

				for finaldates in all_days_inbetween:
					finalfinaldate=str(finaldates).split('/')
					cal.calevent_create(datetime.date(int(finalfinaldate[2]), int(finalfinaldate[1]), int(finalfinaldate[0])),"View Coaching Session Details","message")

				cal.tag_config("message", background="SpringGreen3", foreground="black")

			conn.close()



		username_label = tkinter.Label(self.MemberHome, text="Main Menu: Member", font=('Tahoma', 15, 'bold'), fg='black', bg='white')
		username_label.place(rely=0.14, relx=0.5, anchor='center')

		calendar_label =Label(self.MemberHome, text = 'All Member Events', fg ='black',bg='white',font=('Tahoma',11,'bold'), bd=2, relief="ridge", padx=10, pady=3)
		calendar_label.place(rely=0.378,relx=0.5,anchor=CENTER)
		today = date.today()
		cal = Calendar(self.MemberHome, font="Tahoma 16", selectmode='day', cursor="tcross", year=today.year, month=today.month, day=today.day)
		cal.place(rely=0.6, relx=0.5, anchor='center')
		cal.bind("<<CalendarSelected>>", partial(AllCalendarSelection, cal))


		changeCalendarColour(cal)
		SinglesChangeCalendarColour(cal)
		DoublesChangeCalendarColour(cal)