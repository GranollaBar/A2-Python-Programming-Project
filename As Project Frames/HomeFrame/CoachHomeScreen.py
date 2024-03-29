# Coach Home Screen

from tkinter import ttk
from tkinter import messagebox
import tkinter.simpledialog
import sqlite3
from tkinter import *
from functools import partial
from tkcalendar import Calendar
from time import strftime
from datetime import date, datetime,timedelta
import datetime
from PIL import Image, ImageTk
import webbrowser



# Coach Home Class
class CoachHomeScreenContent:

	# Instance variables
	i = 0
	PassedLogin = False

	# Initiates main screen window
	# Initiates Lisburn Racquets Club Database
	# Initiates Filepath
	def __init__(self, mainScreen, filepath):
		self.CoachHome = mainScreen
		self.conn = sqlite3.connect(filepath + '\\_databases_images_doc\\Databases\\LisburnRacquetsDatabase.db')
		self.c = self.conn.cursor()
		self.filepath = filepath


		# Creates PastEvents database table if it does not exist
		self.c.execute("""CREATE TABLE IF NOT EXISTS PastEvents (
							username text,
							event text,
							date text,
							status text
							)""")


	# Generate coach home content
	def generateCoachHomeScreenContnt(self, FinalUsername, main):

		# Showcases the Lisburn Racquets Club badminton, tennis and squash facilities with an image slider
		# There are a total of 6 images all taken around Lisburn Racquets Club
		def ImageSlider():
			if self.i >= (len(images)-1):
				self.i = 0
				slide_image.config(image=images[self.i])
			else:
				self.i = self.i + 1
				slide_image.configure(image=images[self.i])
			show = slide_image.after(3000, ImageSlider)


		# Find coach's first name and surname and returns the value
		# Based on the coach entered into the system
		def findfirstandsurname():
			conn = sqlite3.connect(self.filepath + '\\_databases_images_doc\\Databases\\LisburnRacquetsDatabase.db')
			c = conn.cursor()

			c.execute("SELECT * FROM coach WHERE username=:coachusername", {
				"coachusername": FinalUsername
			})
			items = c.fetchone()
			labelusername = items[2] + ' ' + items[3]

			return labelusername


		# Will present a message box of any coaching session or competition which hasn't been completed yet
		# Details of the competition/coaching session will be shown to the coach
		# An error will be presented if an invalid date has been selected
		def AllCalendarSelection(cal, event=None):
			AllChangeSelection = False

			conn = sqlite3.connect(self.filepath + '\\_databases_images_doc\\Databases\\LisburnRacquetsDatabase.db')
			c = conn.cursor()

			coachdate = cal.get_date()
			coachdate=str(coachdate).split('/')
			newcoachddate=coachdate[0],coachdate[1],coachdate[2]
			newcoach_a_date = datetime.date(int('20'+newcoachddate[2]),int(newcoachddate[0]), int(newcoachddate[1]))

			string_date = newcoach_a_date.strftime("%d/%m/%Y")

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


			c.execute("SELECT * FROM SinglesCompetition WHERE username=:memberusername OR username2=:memberusername", {
				"memberusername": FinalUsername
			})
			singles_competition_array = c.fetchall()

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

			conn.close()

			if (AllChangeSelection == False):
				messagebox.showinfo('Error', "There is currently no event for " + FinalUsername + " on the date selected", icon='error')


		# Will change the calendar's colour from black to green
		# This is based on all the dates in the coachSessionDetails database table
		def changeCalendarColour(cal):
			conn = sqlite3.connect(self.filepath + '\\_databases_images_doc\\Databases\\LisburnRacquetsDatabase.db')
			c = conn.cursor()

			c.execute("SELECT * FROM coachSessionDetails")
			row = c.fetchall()

			for values in row:
				cal.calevent_create(datetime.date(int(values[3][6:10]), int(values[3][3:5]), int(values[3][0:2])),"View Coaching Session Details","message")

			cal.tag_config("message", background="SpringGreen3", foreground="black")

			conn.close()


		# Will change the calendar's colour from black to green
		# This is based on all the dates in the SinglesCompetition database table
		def SinglesChangeCalendarColour(cal):
			conn = sqlite3.connect(self.filepath + '\\_databases_images_doc\\Databases\\LisburnRacquetsDatabase.db')
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
				if length_inbetween == '':
					length_inbetween = '1'
				else:
					int(length_inbetween)+1

				d3=start_date.split('/')
				d3= datetime.datetime(int(d3[2]),int(d3[1]),int(d3[0]))

				all_days_inbetween=[]

				for i in range(0,int(length_inbetween)):
					add=str(d3+timedelta(days=i)).strip('datetime.date(')
					add=str(d3+timedelta(days=i)).strip('00:00:00')
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


		# Will change the calendar's colour from black to green
		# This is based on all the dates in the DoublesCompetition database table
		def DoublesChangeCalendarColour(cal):
			conn = sqlite3.connect(self.filepath + '\\_databases_images_doc\\Databases\\LisburnRacquetsDatabase.db')
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
				if length_inbetween == '':
					length_inbetween = '1'
				else:
					int(length_inbetween)+1

				d3=start_date.split('/')
				d3= datetime.datetime(int(d3[2]),int(d3[1]),int(d3[0]))

				all_days_inbetween=[]

				for i in range(0,int(length_inbetween)+1):
					add=str(d3+timedelta(days=i)).strip('datetime.date(')
					add=str(d3+timedelta(days=i)).strip('00:00:00')
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


		# Will calculate the current week day for the coach and place it inside a label
		def GetCurrentWeeday():
			Weekday = datetime.datetime.today().strftime('%A')
			weekday.config(text=Weekday)


		# Shows the start and end of the coaches shift time (i.e. time on the system)
		# Once this time has reached its capacity, the coach will be logged out of the system
		def CoachShiftTime():
			Weekday = datetime.datetime.today().strftime('%A')

			conn = sqlite3.connect(self.filepath + '\\_databases_images_doc\\Databases\\LisburnRacquetsDatabase.db')
			c = conn.cursor()

			c.execute("SELECT " + str(Weekday) + " FROM coachTimetable WHERE username=:username", {
				"username":FinalUsername
			})
			WeedayTime = c.fetchone()
			StrippedWeedayTime = [i.strip(',') for i in WeedayTime]

			if 'n/a' in StrippedWeedayTime:
				messagebox.showinfo('Error', 'Coach ' + findfirstandsurname() + ' cannot enter the system at this time. You will now be returned to the login screen', icon='error')
				main.destroy()
				import LoginMainScreen
			else:
				time = str(StrippedWeedayTime[0])
				strippedTime = time.split('-')

				if float(strippedTime[0]) < 12.00 and float(strippedTime[1]) >= 12.00:
					from_time.config(text=strippedTime[0] + 'am')
					to_time.config(text=strippedTime[1] + 'pm')

				elif float(strippedTime[0]) < 12.00 and float(strippedTime[1]) < 12.00:
					from_time.config(text=strippedTime[0] + 'am')
					to_time.config(text=strippedTime[1] + 'am')

				elif float(strippedTime[0]) >= 12.00 and float(strippedTime[1]) >= 12.00:
					from_time.config(text=strippedTime[0] + 'pm')
					to_time.config(text=strippedTime[1] + 'pm')


		# Shows a countdown for when the coach will be logged out of the system
		# This is based on the weekday and the start and end time selected by the manager when creating the coach
		# Once countdown reaches 0, the coach will be forcibly logged out of the system
		def countdown():
			Weekday = datetime.datetime.today().strftime('%A')

			conn = sqlite3.connect(self.filepath + '\\_databases_images_doc\\Databases\\LisburnRacquetsDatabase.db')
			c = conn.cursor()

			c.execute("SELECT " + str(Weekday) + " FROM coachTimetable WHERE username=:username", {
				"username":FinalUsername
			})
			WeedayTime = c.fetchone()
			StrippedWeedayTime = [i.strip(',') for i in WeedayTime]

			if 'n/a' in StrippedWeedayTime:
				messagebox.showinfo('Error', 'Coach ' + findfirstandsurname() + ' cannot enter the system at this time. You will now be returned to the login screen', icon='error')
				main.destroy()
				import LoginMainScreen
			else:
				self.PassedLogin = True

				time = str(StrippedWeedayTime[0])
				strippedTime = time.split('-')

				string = strftime('%H:%M')
				newstring = string.split(':')
				finalstring = newstring[0] + '.' + newstring[1]

				formattedTime1 = format(float(strippedTime[0]), '.2f')
				formattedTime2 = format(float(strippedTime[1]), '.2f')
				formattedTime3 = format(float(finalstring), '.2f')

				if float(formattedTime3) > float(formattedTime1) and float(formattedTime3) < float(formattedTime2):
					redosplit = formattedTime2.split('.')
					finalredosplit = redosplit[0] + ':' + redosplit[1] + ':00'
					currenttime = strftime('%H:%M:%S')

					realfinal1 = datetime.datetime.strptime(finalredosplit, '%H:%M:%S').time()
					realfinal2 = datetime.datetime.strptime(currenttime, '%H:%M:%S').time()

					date = datetime.date(1, 1, 1)
					datetime1 = datetime.datetime.combine(date, realfinal1)
					datetime2 = datetime.datetime.combine(date, realfinal2)
					time_elapsed = datetime1 - datetime2
					timer_label.config(text=time_elapsed)
					timer_label.after(1000, countdown)


		# Opens a link to the specific google maps location of Lisburn Racquets Club
		def GoogleMapsLocation():
			webbrowser.open("https://www.google.com/maps/place/Lisburn+Racquets+Club/@54.5173416,-6.0428075,15z/data=!4m5!3m4!1s0x4861044f4e4d451b:0x9a328c6b732d12eb!8m2!3d54.5173416!4d-6.0340528")


		# Removes the ability to resize all tree views
		def treeviewresizedisable(treeview, event):
			if treeview.identify_region(event.x, event.y) == "separator":
				return "break"


		# Clears past events tree view data
		def clearTv(treeview):
			record=treeview.get_children()
			for elements in record:
				treeview.delete(elements)


		# Past events tree view populate based on the data inside the PastEvents database table
		def treeviewPopulate(treeview):
			clearTv(treeview)

			conn = sqlite3.connect(self.filepath + '\\_databases_images_doc\\Databases\\LisburnRacquetsDatabase.db')
			c = conn.cursor()

			c.execute("SELECT * From PastEvents")
			items = c.fetchall()
			conn.commit()
			conn.close()

			count=0
			for row in items:
				if row == [] or row[3] == 'member':
					pass
				else:
					if count%2==0:
						treeview.insert('','end',text=row[0],values=(row[1],row[2]))
					else:
						treeview.insert('','end',text=row[0],values=(row[1],row[2]))
					count+=1



		# Tkinter labels, entry boxes, buttons, tree views, etc.
		title_label = tkinter.Label(self.CoachHome, text="Main Menu: Coach", font=('serif', 18, 'bold','underline'), fg='black', bg='white', bd=4, relief='groove', padx=10, pady=4)
		title_label.place(rely=0.16, relx=0.17, anchor='center')

		calendar_label =Label(self.CoachHome, text = findfirstandsurname() + "'s Live Events", fg ='black',bg='white',font=('serif',8,'bold'), bd=2, relief="ridge", padx=5, pady=2)
		calendar_label.place(rely=0.14,relx=0.495,anchor=CENTER)
		today = date.today()
		cal = Calendar(self.CoachHome, font="serif 10", selectmode='day', cursor="tcross", year=today.year, month=today.month, day=today.day)
		cal.place(rely=0.305, relx=0.495, anchor='center')
		cal.bind("<<CalendarSelected>>", partial(AllCalendarSelection, cal))

		weekday_label = tkinter.Label(self.CoachHome, text="Current Weekday:", font=('serif', 14, 'bold'), fg='black', bg='white')
		weekday_label.place(rely=0.25, relx=0.11, anchor='center')
		weekday = Label(self.CoachHome, font=('serif', 14, 'bold'), fg='black', bg='white', bd=3, relief='sunken', padx=3, pady=1)
		weekday.place(rely=0.253, relx=0.26, anchor='center')

		from_label = tkinter.Label(self.CoachHome, text="From:", font=('serif', 14, 'bold'), fg='black', bg='white')
		from_label.place(rely=0.3425, relx=0.04, anchor='center')
		from_time = tkinter.Label(self.CoachHome, font=('serif', 14, 'bold'), fg='black', bg='white', bd=3, relief='sunken', padx=3, pady=1)
		from_time.place(rely=0.3455, relx=0.13, anchor='center')
		to_label = tkinter.Label(self.CoachHome, text="To:", font=('serif', 14, 'bold'), fg='black', bg='white')
		to_label.place(rely=0.3425, relx=0.23, anchor='center')
		to_time = tkinter.Label(self.CoachHome, font=('serif', 14, 'bold'), fg='black', bg='white', bd=3, relief='sunken', padx=3, pady=1)
		to_time.place(rely=0.3455, relx=0.31, anchor='center')

		time_left_label = tkinter.Label(self.CoachHome, text="System Time Left:", font=('serif', 14, 'bold'), fg='black', bg='white')
		time_left_label.place(rely=0.43, relx=0.11, anchor='center')
		timer_label = tkinter.Label(self.CoachHome, font=('serif', 14, 'bold'), fg='black', bg='white', bd=3, relief='sunken', padx=3, pady=1)
		timer_label.place(rely=0.433, relx=0.26, anchor='center')

		googlemapsphoto = PhotoImage(file=self.filepath + '\\_databases_images_doc\\Images\\Googlemaps.png')

		GoogleMapsButton = Button(self.CoachHome, cursor="tcross", image=googlemapsphoto, width=507, height=315, command=GoogleMapsLocation, bg="white", activebackground="grey")
		GoogleMapsButton.place(rely=0.73,relx=0.67,anchor=CENTER)
		GoogleMapsButton.image = googlemapsphoto

		img1 = Image.open(self.filepath + '\\_databases_images_doc\\Images\\MemberImageSlider4.png')
		img1.thumbnail((300, 300))
		img2 = Image.open(self.filepath + '\\_databases_images_doc\\Images\\MemberImageSlider1.png')
		img2.thumbnail((300, 300))
		img3 = Image.open(self.filepath + '\\_databases_images_doc\\Images\\MemberImageSlider2.png')
		img3.thumbnail((300, 300))
		img4 = Image.open(self.filepath + '\\_databases_images_doc\\Images\\MemberImageSlider5.png')
		img4.thumbnail((300, 300))
		img5 = Image.open(self.filepath + '\\_databases_images_doc\\Images\\MemberImageSlider3.png')
		img5.thumbnail((300, 300))
		img6 = Image.open(self.filepath + '\\_databases_images_doc\\Images\\MemberImageSlider6.png')
		img6.thumbnail((300, 300))

		image1 = ImageTk.PhotoImage(img1)
		image2 = ImageTk.PhotoImage(img2)
		image3 = ImageTk.PhotoImage(img3)
		image4 = ImageTk.PhotoImage(img4)
		image5 = ImageTk.PhotoImage(img5)
		image6 = ImageTk.PhotoImage(img6)

		images = [image1, image2, image3, image4, image5, image6]

		self.i = 0
		slide_image = Label(self.CoachHome, image=images[self.i], bd=10, relief='ridge', bg='green')
		slide_image.place(rely=0.732, relx=0.19, anchor='center')

		treeview_label =Label(self.CoachHome, text ="Past Events", fg ='black',bg='white',font=('serif',8,'bold'), bd=2, relief="ridge", padx=5, pady=2)
		treeview_label.place(rely=0.127,relx=0.81,anchor=CENTER)
		past_event_Tv=ttk.Treeview(self.CoachHome,height=9,columns=('Date','Status'))
		past_event_Tv.place(relx=0.81,rely=0.3,anchor=CENTER)

		past_event_Tv.heading("#0",text='Event')
		past_event_Tv.column("#0",minwidth=0,width=145)
		past_event_Tv.heading("#1",text='Date')
		past_event_Tv.column("#1",minwidth=0,width=85)
		past_event_Tv.heading("#2",text='Status')
		past_event_Tv.column("#2",minwidth=0,width=80)
		past_event_Tv.bind('<Button-1>', partial(treeviewresizedisable, past_event_Tv))

		past_event_scrollbar = Scrollbar(self.CoachHome, orient='vertical', command=past_event_Tv.yview, cursor="tcross")
		past_event_scrollbar.place(relx=0.975,rely=0.3,anchor='center',height=207)
		past_event_Tv.configure(yscrollcommand=past_event_scrollbar.set)



		countdown()
		if self.PassedLogin == True:
			ImageSlider()
			CoachShiftTime()
			GetCurrentWeeday()
			changeCalendarColour(cal)
			treeviewPopulate(past_event_Tv)
			SinglesChangeCalendarColour(cal)
			DoublesChangeCalendarColour(cal)