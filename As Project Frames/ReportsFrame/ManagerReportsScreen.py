# Manager Reports Screen

import tkinter.simpledialog
import sqlite3
from tkinter import *
import Pmw
import os
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import style
import matplotlib.pyplot as plt
import random
from pandas import DataFrame
import numpy as np



# Manager Reports Class
class ManagerReportsContent:

	# Initiates main screen window
	# Initiates Lisburn Racquets Club Database
	# Initiates Filepath
	def __init__(self, mainScreen, filepath):
		self.Reports = mainScreen
		self.conn = sqlite3.connect(filepath + '\\_databases_images_doc\\Databases\\LisburnRacquetsDatabase.db')
		self.c = self.conn.cursor()
		self.filepath = filepath


	# Generate manager reports content
	def generateManagerReportsContnt(self, FinalUsername):

		# Find manager's first name and surname and returns the value
		# Based on the manager entered into the system
		def findfirstandsurname():
			conn = sqlite3.connect(self.filepath + '\\_databases_images_doc\\Databases\\LisburnRacquetsDatabase.db')
			c = conn.cursor()

			c.execute("SELECT * FROM manager WHERE username=:managerusername", {
				"managerusername": FinalUsername
			})
			items = c.fetchone()
			labelusername = items[2] + ' ' + items[3]

			return labelusername


		# Find manager's first name and surname and returns the value (capitalized form)
		# Based on the manager entered into the system
		def Capitalizedfindfirstandsurname():
			conn = sqlite3.connect(self.filepath + '\\_databases_images_doc\\Databases\\LisburnRacquetsDatabase.db')
			c = conn.cursor()

			c.execute("SELECT * FROM manager WHERE username=:managerusername", {
				"managerusername": FinalUsername
			})
			items = c.fetchone()
			labelusername = str(items[2]).title() + ' ' + str(items[3]).title()

			return labelusername


		# Opens the coach account doc
		# This contains all the information about the most recently added coach into the system
		def OpenCoachAccountDoc():
			os.startfile(self.filepath + '\\_databases_images_doc\\Doc\\coach_Account_Details.docx')



		ToolTips = Pmw.Balloon()


		# Tkinter labels, entry boxes, buttons, tree views, etc.
		title_label = tkinter.Label(self.Reports, text=Capitalizedfindfirstandsurname() + "'s Reports", font=('serif', 14, 'bold','underline'), fg='black', bg='white', bd=4, relief='groove', padx=10, pady=4)
		title_label.place(rely=0.145, relx=0.5, anchor='center')

		wordphoto = PhotoImage(file=self.filepath + '\\_databases_images_doc\\Images\\word.png')

		coachaccount_title_label =Label(self.Reports, text = findfirstandsurname() + "'s Latest Added Coach", fg ='black',bg='white',font=('serif',11,'bold'), bd=2, relief="ridge", padx=7, pady=2)
		coachaccount_title_label.place(rely=0.227,relx=0.765,anchor=CENTER)
		View_coach_account_doc = tkinter.Button(self.Reports, cursor="tcross",text="         Coach_Account_Details.docx", command=OpenCoachAccountDoc, fg='black', bg='white', bd=3, relief='sunken', font=('serif', 14, 'bold'), padx=6, pady=6)
		View_coach_account_doc.place(rely=0.28, relx=0.765, anchor='center')
		ToolTips.bind(View_coach_account_doc, 'Click to see the latest coach added to the system')
		wordlogo = Button(self.Reports, cursor="tcross", image=wordphoto, width=40, height=40, command=OpenCoachAccountDoc, borderwidth=0, activebackground="white")
		wordlogo.place(rely=0.28,relx=0.612,anchor=CENTER)
		wordlogo.image = wordphoto
		wordlogo['relief'] = 'sunken'
		ToolTips.bind(wordlogo, 'Click to see the latest coach added to the system')


		# Creation of a bar chart showing the number of bookings for each type of competition by members
		style.use('seaborn-darkgrid')

		font = {'family': 'serif',
				'color':  'black',
				'weight': 'normal',
				'size': 10,
				}

		conn = sqlite3.connect(self.filepath + '\\_databases_images_doc\\Databases\\LisburnRacquetsDatabase.db')
		c = conn.cursor()

		c.execute("SELECT * FROM MemberBooking")
		row = c.fetchall()

		badmintoncounter = 0
		tenniscounter = 0
		squashcounter = 0

		for data in row:
			if data[2] == 'Badminton':
				badmintoncounter += 1
			elif data[2] == 'Tennis':
				tenniscounter += 1
			else:
				squashcounter += 1

		xvalues = ['Badminton', 'Tennis', 'Squash']
		yvalues = [badmintoncounter, tenniscounter, squashcounter]

		dictionary = {'Type Of Competition': xvalues, 'No. Bookings': yvalues}

		framedata = DataFrame(dictionary, columns=['Type Of Competition','No. Bookings'])

		fig = plt.figure(figsize=(7.5,4), dpi=65)
		fig.tight_layout()
		ax1 = fig.add_subplot(111)
		framedata = framedata[['Type Of Competition','No. Bookings']].groupby('Type Of Competition').sum()
		framedata.plot(kind='barh', legend='True', ax=ax1, fontsize=10)
		ax1.set_title('No. Bookings For Each Competition Type')

		finishedcanvas = FigureCanvasTkAgg(fig, self.Reports)
		finishedcanvas.get_tk_widget().place(relx=0.3,rely=0.38,anchor=CENTER)
		finishedcanvas.draw()


		# Creation of a bar chart showing the total fees for each member
		# This is divided into two separate bar charts beside each other
		# One shows the fees of that member's coaching sessions while the other are the fees of each of their bookings
		c.execute("SELECT * FROM fees")
		data = c.fetchall()

		member_name_list = []

		for values in data:
			if values == []:
				pass
			else:
				member_name = values[0]
				if member_name in member_name_list:
					pass
				else:
					member_name_list.append(member_name)

		coachingfees = 0
		bookingfees = 0

		MemberBookingFees = []
		CoachingSessionFees = []

		t = 0

		for names in member_name_list:
			c.execute("SELECT * FROM fees WHERE username =?", (names,))
			namerows = c.fetchall()
			for individualrows in namerows:
				if individualrows[1] != '':
					newcoachingfee = str(individualrows[1])[1:]
					finalcoachingfee = format(float(newcoachingfee), '.2f')
					coachingfees = coachingfees + float(finalcoachingfee)
					t += 1
				else:
					newbookingfee = str(individualrows[2])[1:]
					finalbookingfee = format(float(newbookingfee), '.2f')
					bookingfees = bookingfees + float(finalbookingfee)
					t += 1

			if t == len(namerows):
				t = 0
				CoachingSessionFees.append(coachingfees)
				MemberBookingFees.append(bookingfees)
				coachingfees = 0
				bookingfees = 0

		fullnames = []

		for fullgivennames in member_name_list:
			c.execute("SELECT * FROM member WHERE username=:memberusername", {
				"memberusername": fullgivennames
			})
			rowdata = c.fetchone()
			fulltitle = rowdata[2] + ' ' + rowdata[3]
			fullnames.append(fulltitle)


		fig2 = plt.figure(figsize=(6.1,4.1), dpi=65, tight_layout=True)
		ax2 = fig2.add_subplot(111)

		bar1 = np.arange(len(member_name_list))
		bar2 = [i+0.4 for i in bar1]

		ax2.bar(bar1, MemberBookingFees, 0.4, label='MemberBookingFees')
		ax2.bar(bar2, CoachingSessionFees, 0.4, Label='CoachingSessionFees')
		ax2.legend(loc="upper right")
		ax2.set_title('Costs For Each Member', fontdict=font)
		ax2.set_xlabel('Type Of Fee', fontdict=font)
		ax2.set_ylabel('Cost', fontdict=font)
		ax2.set_xticks(bar1)
		ax2.set_xticklabels(fullnames)

		finishedfeescanvas = FigureCanvasTkAgg(fig2, self.Reports)
		finishedfeescanvas.get_tk_widget().place(relx=0.3,rely=0.78,anchor=CENTER)
		finishedfeescanvas.draw()


		# The creation of a pie chart which shows the perecentage of fees for both coaching sessions and member bookings
		c.execute("SELECT * FROM fees")
		row = c.fetchall()

		finalsessioncost = 0
		finalbookingcost = 0

		if len(row) > 0:
			for items in row:
				if items[1] != '':
					cutsessionfee = str(items[1])[1:]
					finalsessioncost = finalsessioncost + float(cutsessionfee)
					newfinalsessioncost = format(float(finalsessioncost), '.2f')
				else:
					cutbookingfee = str(items[2])[1:]
					finalbookingcost = finalbookingcost + float(cutbookingfee)
					newfinalbookingcost = format(float(finalbookingcost), '.2f')

		else:
			newfinalsessioncost = 0
			newfinalbookingcost = 0

		sessioncosts = [newfinalsessioncost]
		bookingcosts = [newfinalbookingcost]

		finalvalues = sessioncosts + bookingcosts

		pielabels = ['Coaching Sessions','Member Bookings']
		text = 'Overall Fees Ratio'

		allcolours = ['r','g','b','c','m','y','#760000','#b24900','#b2b300','#b2f800'
			,'#f5f800','#976d01','#004b01','#004b63','#ff4bc8','#b24bc8','#754bc8','#751783'
			,'#e81783','#001783','#00a583','#00a5e6','#cc5200','#ffe0cc','#cc0000','#999966'
			,'#ffff66','#cccc00','#5c8a8a','#000066','#9999ff','#33cccc','#805500','#4d0026']
		randomlist = []
		t = 0

		while t != 4:
			randomnumber = random.randint(0,33)
			randomlist.append(randomnumber)
			t += 1

		finalcolours = [allcolours[randomlist[0]],allcolours[randomlist[1]],allcolours[randomlist[2]],allcolours[randomlist[3]]]

		fig3 = plt.Figure(figsize=(6,7), dpi=65, tight_layout=True)
		ax3 = fig3.add_subplot(111)
		ax3.pie(finalvalues, radius=1, labels=pielabels, autopct='%1.1f%%', shadow=True, colors=finalcolours, textprops={'fontsize': 10, 'family': 'serif', 'color':  'black', 'weight': 'normal'})
		ax3.legend(loc="upper center")
		ax3.set_title(text, fontdict=font)
		ax3.axis('equal')

		piefinishedcanvas = FigureCanvasTkAgg(fig3, self.Reports)
		piefinishedcanvas.get_tk_widget().place(relx=0.75,rely=0.7,anchor=CENTER)
		piefinishedcanvas.draw()
