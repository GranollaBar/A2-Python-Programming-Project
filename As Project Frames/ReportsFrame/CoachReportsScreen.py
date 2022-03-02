# Coach Reports Screen

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



# Coach Reports Class
class CoachReportsContent:

	# Initiates main screen window
	def __init__(self, mainScreen):
		self.Reports = mainScreen
		self.conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
		self.c = self.conn.cursor()


	# Generate coach reports content
	def generateCoachReportsContnt(self, FinalUsername):

		# Find coach's first name and surname and returns the value
		def findfirstandsurname():
			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
			c = conn.cursor()

			c.execute("SELECT * FROM coach WHERE username=:coachusername", {
				"coachusername": FinalUsername
			})
			items = c.fetchone()
			labelusername = items[2] + ' ' + items[3]

			return labelusername


		# Find coach's first name and surname and returns the value (capitalized form)
		def Capitalizedfindfirstandsurname():
			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
			c = conn.cursor()

			c.execute("SELECT * FROM coach WHERE username=:coachusername", {
				"coachusername": FinalUsername
			})
			items = c.fetchone()
			labelusername = str(items[2]).title() + ' ' + str(items[3]).title()

			return labelusername


		# Opens the member account doc (most recently added member)
		def OpenMemberAccountDoc():
			os.startfile(r'C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Doc/Member_Account_Details.docx')


		# Opens the competition doc (most recently added competition - singles & doubles)
		def OpenCompetitionDoc():
			os.startfile(r'C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Doc/Current_Competition_Results.docx')


		# Draws the most recently finished singles competition
		def StartUpFinishedSinglesGraph():
			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
			c = conn.cursor()

			c.execute("SELECT * FROM FinshedCompetitions")
			row2 = c.fetchall()

			if len(row2) != 0:
				GotARow = False

				if row2[len(row2)-1][0] == 'Singles':
					c.execute("SELECT * FROM FinshedCompetitions WHERE CompetitionType=:Type AND CurrentID=:ID", {
						"Type": 'Singles',
						"ID": row2[len(row2)-1][6]
					})
					singlerow = c.fetchone()
					GotARow = True

				if GotARow == False:
					for x in reversed(row2):
						c.execute("SELECT * FROM FinshedCompetitions WHERE CompetitionType=:Type", {
							"Type": 'Singles'
						})
						singlerow = c.fetchone()
						if (singlerow is None):
							pass
						else:
							GotARow = True
							break

				if GotARow == True:
					final_result_label = tkinter.Label(self.Reports, text='Final Results', font=('serif', 9, 'bold', 'underline'), fg='black', bg='white')
					final_result_label.place(rely=0.88, relx=0.652, anchor='center')

					member1_score_label = tkinter.Label(self.Reports, text='   #' + singlerow[1] + ' - ' + singlerow[2] +'#   ', font=('serif', 8, 'bold'), fg='SpringGreen3', bg='white')
					member1_score_label.place(rely=0.92, relx=0.652, anchor='center')

					member2_score_label = tkinter.Label(self.Reports, text='   #' + singlerow[3] + ' - ' + singlerow[4] + '#   ', font=('serif', 8, 'bold'), fg='blue', bg='white')
					member2_score_label.place(rely=0.96, relx=0.652, anchor='center')

					text = 'ID: ' + str(singlerow[6])

					style.use('seaborn-darkgrid')

					font = {'family': 'serif',
							'color':  'black',
							'weight': 'normal',
							'size': 12,
							}

					score1list = []
					score2list = []
					timelist = []

					score1list.append(0)
					score2list.append(0)
					timelist.append(0)
					score1list.append(singlerow[2])
					score2list.append(singlerow[4])
					timelist.append(singlerow[5])

					fig = plt.figure(figsize=(3.5,3.2), dpi=58)
					fig.tight_layout()
					ax1 = fig.add_subplot(111)
					if score1list[1] == '21':
						ax1.plot(timelist, score2list, color="blue", label="Score 2")
						ax1.plot(timelist, score1list, color="limegreen", label="Score 1")
						ax1.legend(loc="upper left")
					else:
						ax1.plot(timelist, score1list, color="limegreen", label="Score 1")
						ax1.plot(timelist, score2list, color="blue", label="Score 2")
						ax1.legend(loc="upper left")
					ax1.set_title(text, fontdict=font)
					ax1.set_xlabel('Time (Seconds)', fontdict=font)
					ax1.set_ylabel('Score', fontdict=font)

					finishedcanvas = FigureCanvasTkAgg(fig, self.Reports)
					finishedcanvas.get_tk_widget().place(relx=0.652,rely=0.712,anchor=CENTER)
					finishedcanvas.draw()

				else:
					pass

			else:
				pass


		# Draws the most recently finished doubles competition
		def StartUpFinishedDoublesGraph():
			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
			c = conn.cursor()

			c.execute("SELECT * FROM FinshedCompetitions")
			row2 = c.fetchall()

			if len(row2) != 0:
				GotARow = False

				if row2[len(row2)-1][0] == 'Doubles':
					c.execute("SELECT * FROM FinshedCompetitions WHERE CompetitionType=:Type AND CurrentID=:ID", {
						"Type": 'Doubles',
						"ID": row2[len(row2)-1][6]
					})
					doublerow = c.fetchone()
					GotARow = True

				if GotARow == False:
					for x in reversed(row2):
						c.execute("SELECT * FROM FinshedCompetitions WHERE CompetitionType=:Type", {
							"Type": 'Doubles'
						})
						doublerow = c.fetchone()
						if (doublerow is None):
							pass
						else:
							GotARow = True
							break

				if GotARow == True:
					final_result_label = tkinter.Label(self.Reports, text='Final Results', font=('serif', 9, 'bold', 'underline'), fg='black', bg='white')
					final_result_label.place(rely=0.88, relx=0.872, anchor='center')

					member1_score_label = tkinter.Label(self.Reports, text='   #' + doublerow[1] + ' - ' + doublerow[2] + '#   ', font=('serif', 8, 'bold'), fg='SpringGreen3', bg='white')
					member1_score_label.place(rely=0.92, relx=0.872, anchor='center')

					member2_score_label = tkinter.Label(self.Reports, text='   #' + doublerow[3] + ' - ' + doublerow[4] + '#   ', font=('serif', 8, 'bold'), fg='blue', bg='white')
					member2_score_label.place(rely=0.96, relx=0.872, anchor='center')

					text = 'ID: ' + str(doublerow[6])

					style.use('seaborn-darkgrid')

					font = {'family': 'serif',
							'color':  'black',
							'weight': 'normal',
							'size': 12,
							}

					score1list = []
					score2list = []
					timelist = []

					score1list.append(0)
					score2list.append(0)
					timelist.append(0)
					score1list.append(doublerow[2])
					score2list.append(doublerow[4])
					timelist.append(doublerow[5])

					fig = plt.figure(figsize=(3.5,3.2), dpi=58)
					fig.tight_layout()
					ax1 = fig.add_subplot(111)
					if score1list[1] == '21':
						ax1.plot(timelist, score2list, color="blue", label="Score 2")
						ax1.plot(timelist, score1list, color="limegreen", label="Score 1")
						ax1.legend(loc="upper left")
					else:
						ax1.plot(timelist, score1list, color="limegreen", label="Score 1")
						ax1.plot(timelist, score2list, color="blue", label="Score 2")
						ax1.legend(loc="upper left")
					ax1.set_title(text, fontdict=font)
					ax1.set_xlabel('Time (Seconds)', fontdict=font)
					ax1.set_ylabel('Score', fontdict=font)

					finishedcanvas = FigureCanvasTkAgg(fig, self.Reports)
					finishedcanvas.get_tk_widget().place(relx=0.872,rely=0.712,anchor=CENTER)
					finishedcanvas.draw()

				else:
					pass

			else:
				pass



		ToolTips = Pmw.Balloon()

		title_label = tkinter.Label(self.Reports, text=Capitalizedfindfirstandsurname() + "'s Reports", font=('serif', 14, 'bold','underline'), fg='black', bg='white', bd=4, relief='groove', padx=10, pady=4)
		title_label.place(rely=0.145, relx=0.5, anchor='center')

		wordphoto = PhotoImage(file="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Images/word.png")

		memberaccount_title_label =Label(self.Reports, text = findfirstandsurname() + "'s Latest Added Member", fg ='black',bg='white',font=('serif',11,'bold'), bd=2, relief="ridge", padx=7, pady=2)
		memberaccount_title_label.place(rely=0.207,relx=0.765,anchor=CENTER)
		View_member_account_doc = tkinter.Button(self.Reports, cursor="tcross",text="         Member_Account_Details.docx", command=OpenMemberAccountDoc, fg='black', bg='white', bd=3, relief='sunken', font=('serif', 14, 'bold'), padx=6, pady=6)
		View_member_account_doc.place(rely=0.26, relx=0.765, anchor='center')
		ToolTips.bind(View_member_account_doc, 'Click to see the latest member added to the system')
		wordlogo = Button(self.Reports, cursor="tcross", image=wordphoto, width=40, height=40, command=OpenMemberAccountDoc, borderwidth=0, activebackground="white")
		wordlogo.place(rely=0.26,relx=0.612,anchor=CENTER)
		wordlogo.image = wordphoto
		wordlogo['relief'] = 'sunken'
		ToolTips.bind(wordlogo, 'Click to see the latest member added to the system')

		competition_title_label =Label(self.Reports, text = findfirstandsurname() + "'s Lastest Added Results", fg ='black',bg='white',font=('serif',11,'bold'), bd=2, relief="ridge", padx=7, pady=2)
		competition_title_label.place(rely=0.347,relx=0.765,anchor=CENTER)
		View_competition_doc = tkinter.Button(self.Reports, cursor="tcross",text="         Current_Competition_Results.docx", command=OpenCompetitionDoc, fg='black', bg='white', bd=3, relief='sunken', font=('serif', 14, 'bold'), padx=6, pady=6)
		View_competition_doc.place(rely=0.4, relx=0.765, anchor='center')
		ToolTips.bind(View_competition_doc, 'Click to see the latest singles/doubles competition completed')
		wordlogo2 = Button(self.Reports, cursor="tcross", image=wordphoto, width=40, height=40, command=OpenCompetitionDoc, borderwidth=0, activebackground="white")
		wordlogo2.place(rely=0.4,relx=0.594,anchor=CENTER)
		wordlogo2.image = wordphoto
		wordlogo2['relief'] = 'sunken'
		ToolTips.bind(wordlogo, 'Click to see the latest singles/doubles competition completed')

		style.use('seaborn-darkgrid')

		font = {'family': 'serif',
				'color':  'black',
				'weight': 'normal',
				'size': 16,
				}

		conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
		c = conn.cursor()

		c.execute("SELECT * FROM SinglesCompetition")
		row = c.fetchall()

		c.execute("SELECT * FROM DoublesCompetition")
		row2 = c.fetchall()

		c.execute("SELECT * FROM FinshedCompetitions")
		row3 = c.fetchall()

		currentsinglescompetitions = []
		currentdoublescompetitions = []
		finishedsinglescompetitions = []
		finisheddoublescompetitions = []

		singlescounter = 0
		doublescounter = 0

		currentsinglescompetitions.append(len(row))
		currentdoublescompetitions.append(len(row2))

		for items in row3:
			if items[0] == 'Singles':
				singlescounter += 1
			else:
				doublescounter += 1

		finishedsinglescompetitions.append(singlescounter)
		finisheddoublescompetitions.append(doublescounter)

		finalvalues = currentsinglescompetitions + currentdoublescompetitions + finishedsinglescompetitions + finisheddoublescompetitions

		pielabels = ['Unfin. Singles','Unfin. Doubles','Fin. Singles','Fin. Doubles']
		text = 'Types of Competitions Ratio'

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

		fig = plt.Figure(figsize=(6.5,8), dpi=75, tight_layout=True)
		ax1 = fig.add_subplot(111)
		ax1.pie(finalvalues, radius=1, labels=pielabels, autopct='%1.1f%%', shadow=True, colors=finalcolours, textprops={'fontsize': 13, 'family': 'serif', 'color':  'black', 'weight': 'normal'})
		ax1.legend(loc="upper center")
		ax1.set_title(text, fontdict=font)
		ax1.axis('equal')

		finishedcanvas = FigureCanvasTkAgg(fig, self.Reports)
		finishedcanvas.get_tk_widget().place(relx=0.256,rely=0.65,anchor=CENTER)
		finishedcanvas.draw()


		title_label =Label(self.Reports, text = "Most Recent Matches", fg ='black',bg='white',font=('serif',11,'bold'), bd=2, relief="ridge", padx=5, pady=2)
		title_label.place(rely=0.49,relx=0.763,anchor=CENTER)

		box =Label(self.Reports, text = "blank", fg ='white',bg='white',font=('serif',8,'bold'), bd=2, relief="sunken", padx=200, pady=145)
		box.place(rely=0.745,relx=0.76,anchor=CENTER)

		boxsplitvertical =Label(self.Reports, text = "b", fg ='white',bg='white',font=('serif',8,'bold'), bd=2, relief="ridge", padx=1, pady=143.5)
		boxsplitvertical.place(rely=0.746,relx=0.76,anchor=CENTER)

		box_singles_title = tkinter.Label(self.Reports, text="Most Recent Singles Match", font=('serif', 10, 'bold'), fg='black', bg='white')
		box_singles_title.place(rely=0.539, relx=0.645, anchor='center')

		box_doubles_title = tkinter.Label(self.Reports, text="Most Recent Doubles Match", font=('serif', 10, 'bold'), fg='black', bg='white')
		box_doubles_title.place(rely=0.539, relx=0.877, anchor='center')

		boxsplithorizontal =Label(self.Reports, text = "b", fg ='white',bg='white',font=('serif',1), bd=2, relief="ridge", padx=214, pady=0.5)
		boxsplithorizontal.place(rely=0.565,relx=0.76,anchor=CENTER)


		StartUpFinishedSinglesGraph()
		StartUpFinishedDoublesGraph()

