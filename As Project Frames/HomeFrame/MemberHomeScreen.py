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
from time import strftime
from datetime import date, datetime,timedelta
import datetime
from PIL import Image, ImageTk

i = 0

class MemberHomeScreenContent:

	def __init__(self, mainScreen):
		self.MemberHome = mainScreen


	def generateMemberHomeScreenContnt(self, FinalUsername):

		def time():
			string = strftime('%H:%M:%S %p')
			clock.config(text=string)
			clock.after(1000, time)


		def start():
			global i, show
			if i >= (len(images)-1):
				i = 0
				slide_image.config(image=images[i])
			else:
				i = i + 1
				slide_image.configure(image=images[i])
			show = slide_image.after(2000, start)


		def findfirstandsurname():
			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
			c = conn.cursor()

			c.execute("SELECT * FROM member WHERE username=:memberusername", {
				"memberusername": FinalUsername
			})
			items = c.fetchone()
			labelusername = items[2] + ' ' + items[3]

			return labelusername

		def AllCalendarSelection(cal, event=None):
			AllChangeSelection = False

			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
			c = conn.cursor()

			print(cal.get_date)

			coachdate = cal.get_date()
			coachdate=str(coachdate).split('/')
			newcoachddate=coachdate[0],coachdate[1],coachdate[2]
			newcoach_a_date = datetime.date(int('20'+newcoachddate[2]),int(newcoachddate[0]), int(newcoachddate[1]))

			string_date = newcoach_a_date.strftime("%d/%m/%Y")

			c.execute("SELECT * From coachSessionDetails WHERE date=?", (string_date,))
			items = c.fetchone()

			print(items)
			print('got here')

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
				"memberusername": FinalUsername
			})
			singles_competition_array = c.fetchall()

			print(singles_competition_array)

			singlescompetitiondate = cal.get_date()
			singlescompetitiondate=str(singlescompetitiondate).split('/')
			newsinglescompetitiondate=singlescompetitiondate[0],singlescompetitiondate[1],singlescompetitiondate[2]
			newsinglescompetitiondatea_date = datetime.date(int('20'+newsinglescompetitiondate[2]),int(newsinglescompetitiondate[0]), int(newsinglescompetitiondate[1]))
			newsinglescompetitiondatea_date.strftime('%Y-%m-%d')

			singles_current_day=str(newsinglescompetitiondatea_date).split('-')

			for i in singles_competition_array:
				singlesstart=str(i[2]).split('/')
				singlesend=str(i[3]).split('/')

				if singles_current_day[1] == singlesstart[1] and singles_current_day[2] >= singlesstart[0] and singles_current_day[2] <= singlesend[0]:
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
				"memberusername": FinalUsername
			})
			doubles_competition_array = c.fetchall()

			doublescompetitiondate = cal.get_date()
			doublescompetitiondate=str(doublescompetitiondate).split('/')
			newdoublescompetitiondate=doublescompetitiondate[0],doublescompetitiondate[1],doublescompetitiondate[2]
			newdoublescompetitiondatea_date = datetime.date(int('20'+newdoublescompetitiondate[2]),int(newdoublescompetitiondate[0]), int(newdoublescompetitiondate[1]))
			newdoublescompetitiondatea_date.strftime('%Y-%m-%d')

			doubles_current_day=str(newdoublescompetitiondatea_date).split('-')

			for i in doubles_competition_array:
				doublesstart=str(i[4]).split('/')
				doublesend=str(i[5]).split('/')

				if doubles_current_day[1] == doublesstart[1] and doubles_current_day[2] >= doublesstart[0] and doubles_current_day[2] <= doublesend[0]:
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
				messagebox.showinfo('Error', "There is currently no event for " + FinalUsername + " on the date selected", icon='error')


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
				"memberusername": FinalUsername
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
				"memberusername": FinalUsername
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



		username_label = tkinter.Label(self.MemberHome, text="Main Menu: Member", font=('Tahoma', 15, 'bold','underline'), fg='black', bg='white')
		username_label.place(rely=0.14, relx=0.5, anchor='center')

		calendar_label =Label(self.MemberHome, text = "All of " + findfirstandsurname() + "'s Events", fg ='black',bg='white',font=('Tahoma',11,'bold'), bd=2, relief="ridge", padx=10, pady=3)
		calendar_label.place(rely=0.448,relx=0.68,anchor=CENTER)
		today = date.today()
		cal = Calendar(self.MemberHome, font="Tahoma 20", selectmode='day', cursor="tcross", year=today.year, month=today.month, day=today.day)
		cal.place(rely=0.72, relx=0.68, anchor='center')
		cal.bind("<<CalendarSelected>>", partial(AllCalendarSelection, cal))

		clock_label = tkinter.Label(self.MemberHome, text="Current Time:", font=('Tahoma', 17, 'bold'), fg='black', bg='white')
		clock_label.place(rely=0.229, relx=0.12, anchor='center')
		clock = Label(self.MemberHome, font=('Tahoma', 20, 'bold'), fg='black', bg='white', bd=5, relief='sunken')
		clock.place(rely=0.23, relx=0.31, anchor='center')

		img1 = Image.open('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Images/MemberImageSlider4.png')
		img1.thumbnail((300, 300))
		img2 = Image.open('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Images/MemberImageSlider1.png')
		img2.thumbnail((300, 300))
		img3 = Image.open('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Images/MemberImageSlider2.png')
		img3.thumbnail((300, 300))
		img4 = Image.open('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Images/MemberImageSlider5.png')
		img4.thumbnail((300, 300))
		img5 = Image.open('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Images/MemberImageSlider3.png')
		img5.thumbnail((300, 300))
		img6 = Image.open('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Images/MemberImageSlider6.png')
		img6.thumbnail((300, 300))

		image1 = ImageTk.PhotoImage(img1)
		image2 = ImageTk.PhotoImage(img2)
		image3 = ImageTk.PhotoImage(img3)
		image4 = ImageTk.PhotoImage(img4)
		image5 = ImageTk.PhotoImage(img5)
		image6 = ImageTk.PhotoImage(img6)

		images = [image1, image2, image3, image4, image5, image6]

		i = 0
		slide_image = Label(self.MemberHome, image=images[i], bd=10, relief='ridge', bg='grey')
		slide_image.place(rely=0.71, relx=0.19, anchor='center')



		start()
		time()
		changeCalendarColour(cal)
		SinglesChangeCalendarColour(cal)
		DoublesChangeCalendarColour(cal)