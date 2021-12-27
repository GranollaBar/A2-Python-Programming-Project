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


class CompetitionContent:

	def __init__(self, mainScreen):
		self.results = mainScreen
		self.conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
		self.c = self.conn.cursor()


		# self.c.execute("""CREATE TABLE competition (
		# 			username text,
		# 			username2 text,
		# 			start_date text,
		# 			end_date text,
		# 			score text,
		# 			winner text,
		# 			competitionID integer
		# 			)""")


	def generateResultsContnt(self):

		def validate_username(value, value2, fieldname, fieldname2, label, label2):
			if (value == ''):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " Can Not Be empty")
				return False
			if (value2 == ''):
				label2.config(fg="red")
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname2 + " Can Not Be empty")
				return False
			if value == value2:
				label.config(fg="red")
				label2.config(fg="red")
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " and " + fieldname2 + " Can Not Be the same for both members")
				return False

			label.config(fg="SpringGreen3")
			label2.config(fg="SpringGreen3")
			return True


		def validate_date(value, value2, fieldname, fieldname2, label, label2):
			presentDate = datetime.datetime.now()
			date_formated = presentDate.strftime("%d/%m/%Y")

			d1 = datetime.datetime.strptime(value, "%d/%m/%Y").date()
			d2 = datetime.datetime.strptime(str(date_formated), "%d/%m/%Y").date()

			if value == '':
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " must have a date selected")
				return False
			if value2 == '':
				label.config(fg="SpringGreen3")
				label2.config(fg="red")
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname2 + " must have a date selected")
				return False
			if d2>d1:
				label.config(fg="red")
				label2.config(fg="red")
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " Can Not Be before the current date")
				return False
			if value > value2:
				label.config(fg="red")
				label2.config(fg="red")
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " must be before " + fieldname2)
				return False

			label.config(fg="SpringGreen3")
			label2.config(fg="SpringGreen3")
			return True


		def startDateCheck(dob):
			def assign_start_date():
				startDate.set(start_cal.get_date())
				startDateTop.withdraw()

			today = datetime.date.today()
			startDateTop = Toplevel(self.results)

			start_cal = Calendar(startDateTop, font="Tahoma 16", date_pattern='dd/mm/yyyy',selectmode='day', cursor="tcross", year=today.year, month=today.month, day=today.day)
			start_cal.pack(fill="both", expand=True)
			ttk.Button(startDateTop, text="ok", command=assign_start_date).pack()


		def endDateCheck(dob):
			def assign_end_date():
				endDate.set(end_cal.get_date())
				endDateTop.withdraw()

			today = datetime.date.today()
			endDateTop = Toplevel(self.results)

			end_cal = Calendar(endDateTop, font="Tahoma 16", date_pattern='dd/mm/yyyy',selectmode='day', cursor="tcross", year=today.year, month=today.month, day=today.day)
			end_cal.pack(fill="both", expand=True)
			ttk.Button(endDateTop, text="ok", command=assign_end_date).pack()


		def validate_group_selected(value, fieldname, label):
			if (value == ''):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " Can Not Be empty")
				return False

			label.config(fg="SpringGreen3")
			return True


		def validate_member_scores(value1, value2, fieldname1, fieldname2, label1, label2):
			if (str(value1) == ''):
				label1.config(fg="red")
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname1 + " Can Not Be empty")
				return False
			if (value1.isnumeric() == False):
				label1.config(fg="red")
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname1 + " Must be an integer")
				return False
			if (int(value1) > 21):
				label1.config(fg="red")
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname1 + " Must be below 21")
				return False
			if (str(value2) == ''):
				label1.config(fg="SpringGreen3")
				label2.config(fg="red")
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname2 + " Can Not Be empty")
				return False
			if (value2.isnumeric() == False):
				label1.config(fg="SpringGreen3")
				label2.config(fg="red")
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname2 + " Must be an integer")
				return False
			if (int(value2) > 21):
				label1.config(fg="SpringGreen3")
				label2.config(fg="red")
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname2 + " Must be below 21")
				return False
			if (int(value1) != 21 and int(value2) != 21):
				label1.config(fg="red")
				label2.config(fg="red")
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname1 + " and " + fieldname2 + " Must have one score equal to 21")
				return False
			if (int(value1) == 21 and int(value2) == 21):
				label1.config(fg="red")
				label2.config(fg="red")
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname1 + " and " + fieldname2 + " Must only have one score equal to 21")
				return False

			label1.config(fg="SpringGreen3")
			label2.config(fg="SpringGreen3")
			return True


		def validate_competition_date(MemberID):
			conn = sqlite3.connect('BadmintonClub.db')
			c = conn.cursor()

			c.execute("SELECT * From competition WHERE competitionID=?", (MemberID,))
			items = c.fetchone()
			if not items:
				messagebox.showinfo("info", "There is no group that exists with that number")

			else:
				member_start_date = items[2]
				member_end_date = items[3]

				presentDate = datetime.datetime.now()
				date_formated = presentDate.strftime("%d/%m/%Y")

				d1 = datetime.datetime.strptime(member_start_date, "%d/%m/%Y").date()
				d2 = datetime.datetime.strptime(member_end_date, "%d/%m/%Y").date()
				d3 = datetime.datetime.strptime(str(date_formated), "%d/%m/%Y").date()

				if d3>d2:
					messagebox.showinfo("Validation Error", "The competition cannot be ran after " + member_end_date)
					return False
				if d3<d1:
					messagebox.showinfo("Validation Error", "The competition cannot be ran before " + member_start_date)
					return False

				conn.commit()
				conn.close()

				return True




		def clearTv():
			record=competition_TV.get_children()
			for elements in record:
				competition_TV.delete(elements)


		def treeviewPopulate():
			clearTv()

			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
			c = conn.cursor()

			c.execute("SELECT * From competition")
			items = c.fetchall()

			conn.commit()
			conn.close()

			count=0
			for row in items:
				if row == []:
					pass
				else:
					if count%2==0:
						competition_TV.insert('','end',text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6]))
					else:
						competition_TV.insert('','end',text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6]))
					count+=1


		def returnColour(usernameReturn, username2Return, startDateReturn, endDateReturn, viewGroupReturn):
			usernameReturn.config(fg="black")
			username2Return.config(fg="black")
			startDateReturn.config(fg="black")
			endDateReturn.config(fg="black")
			viewGroupReturn.config(fg="black")


		def submitMemberToCompetition():
			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
			c = conn.cursor()

			isValid = True
			isValid = isValid and validate_username(self.memberNamesAndPasswords.get(),self.memberNamesAndPasswords2.get(), "User 1", "User 2", username_label, username2_label)

			if isValid:
				member_username = self.memberNamesAndPasswords.get()
				member_username2 = self.memberNamesAndPasswords2.get()

				response = askyesno("Are you sure?", "Are you sure that the member's selected are correct?")
				if response == False:
					returnColour(username_label, username2_label, start_date_label, end_date_label, view_group_label)
					showinfo("Info", "submition cancelled")

				else:
					c.execute("SELECT * FROM competition")
					competition_array = c.fetchall()

					newId = len(competition_array) + 1

					c.execute("INSERT INTO competition VALUES(?, ?, ?, ?, ?, ?, ?)", (
						member_username,member_username2,"","","","",newId

					))

					returnColour(username_label, username2_label, start_date_label, end_date_label, view_group_label)
					messagebox.showinfo("info", "User's has been successfully stored for the competition")

			conn.commit()
			conn.close()

			treeviewPopulate()


		def submitDateToCompetition():
			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
			c = conn.cursor()

			isValid = True
			isValid = isValid and validate_date(startDate.get(),endDate.get(), "Start Date", "End Date", start_date_label, end_date_label)

			if isValid:
				member_start_date = startDate.get()
				member_end_date = endDate.get()

				response = askyesno("Are you sure?", "Are you sure that the date's selected are correct?")
				if response == False:
					returnColour(username_label, username2_label, start_date_label, end_date_label, view_group_label)
					showinfo("Info", "submition cancelled")

				else:
					response2 = askyesno("Are you sure?", "These new dates will update the latest member competition added, is this okay?")
					if response2 == False:
						returnColour(username_label, username2_label, start_date_label, end_date_label)
						showinfo("Info", "submition cancelled")

					else:

						c.execute("SELECT * FROM competition")
						competition_array = c.fetchall()

						CompetitionID = len(competition_array)

						c.execute("""UPDATE competition SET start_date = :start_date WHERE competitionID=:CompetitionID""", {
							"start_date": member_start_date,
							"CompetitionID": CompetitionID
						})

						c.execute("""UPDATE competition SET end_date = :end_date WHERE competitionID=:CompetitionID""", {
							"end_date": member_end_date,
							"CompetitionID": CompetitionID
						})

						memberGroupSelection(self)

					returnColour(username_label, username2_label, start_date_label, end_date_label, view_group_label)
					messagebox.showinfo("info", "User's has been successfully stored for the competition")

			conn.commit()
			conn.close()

			treeviewPopulate()


		def confirmCompetition():
			conn = sqlite3.connect('BadmintonClub.db')
			c = conn.cursor()

			isValid = True
			isValid = isValid and validate_group_selected(memberGroupSelection(), "Member Group Selected", view_group_label)

			if isValid:
				member_group_selected = memberGroups.get()

				c.execute("SELECT * From competition WHERE competitionID=?", (member_group_selected,))
				items = c.fetchone()
				if not items:
					messagebox.showinfo("info", "There is no group that exists with that number")

				else:

					memberUsername = items[0]
					memberUsername2 = items[1]


					c.execute("SELECT * From member WHERE username=?", (memberUsername,))
					member1 = c.fetchone()
					if not member1:
						messagebox.showinfo("info", "There is no username named " + memberUsername)

					else:

						contestant1_label.config(text= member1[2] + " " + member1[3])

					c.execute("SELECT * From member WHERE username=?", (memberUsername2,))
					member2 = c.fetchone()
					if not member2:
						messagebox.showinfo("info", "There is no username named " + memberUsername2)

					else:

						contestant2_label.config(text= member2[2] + " " + member2[3])


					c.execute("SELECT * From competition WHERE competitionID=?", (member_group_selected,))
					items = c.fetchone()
					if not items:
						messagebox.showinfo("info", "There is no group that exists with that number")

					else:

						contestant_winner_label.config(text=items[5])

				returnColour(username_label, username2_label, start_date_label, end_date_label, view_group_label)
				messagebox.showinfo("info", "The competition has now been populated")

			conn.commit()
			conn.close()


		def completeCompetition(label1, label2):
			conn = sqlite3.connect('BadmintonClub.db')
			c = conn.cursor()

			isDateValid = True
			isDateValid = isDateValid and validate_competition_date(self.memberGroups.get())

			if isDateValid:

				if label1 == "" or label2 == "":
					messagebox.showinfo("info", "No Group has been selected yet", icon="error")

				else:

					isValid = True
					isValid = isValid and validate_group_selected(self.memberGroups.get(), "Member Group Selected", view_group_label)

					if isValid:
						member_group_selected = self.memberGroups.get()

						c.execute("SELECT * From competition WHERE competitionID=?", (member_group_selected,))
						items = c.fetchone()
						if not items:
							messagebox.showinfo("info", "There is no group that exists with that number", icon="error")

						else:

							memberUsername = items[0]
							memberUsername2 = items[1]


							completeFrame=Toplevel(bg="white")
							completeFrame.geometry('200x200')

							title_label =Label(completeFrame,text ="Input Competition Scores" , fg ='SpringGreen3',bg='white',font=('Tahoma',11,'bold','underline'))
							title_label.place(rely=0.06,relx=0.5,anchor=CENTER)

							contestant1_score_label = tkinter.Label(completeFrame, text="", font=('Tahoma', 10, 'bold'), fg='black', bg='white')
							contestant1_score_label.place(rely=0.3, relx=0.35, anchor='center')

							c.execute("SELECT * From member WHERE username=?", (memberUsername,))
							member1 = c.fetchone()
							if not member1:
								messagebox.showinfo("info", "There is no username named " + memberUsername)
								completeFrame.withdraw()

							else:

								contestant1_score_label.config(text= member1[2] + " " + member1[3] + ":")

							contestant2_score_label = tkinter.Label(completeFrame, text="", font=('Tahoma', 10, 'bold'), fg='black', bg='white')
							contestant2_score_label.place(rely=0.5, relx=0.35, anchor='center')

							c.execute("SELECT * From member WHERE username=?", (memberUsername2,))
							member2 = c.fetchone()
							if not member2:
								messagebox.showinfo("info", "There is no username named " + memberUsername2)
								completeFrame.withdraw()

							else:

								contestant2_score_label.config(text= member2[2] + " " + member2[3] + ":")

							contestant1_score_entry = tkinter.Entry(completeFrame, width=4, textvariable=contestant1Score, bd=4, relief='ridge', cursor="tcross", font=('Tahoma', 10, 'bold'))
							contestant1_score_entry.place(rely=0.3, relx=0.8, anchor='center')
							contestant1Score.set('')

							contestant2_score_entry = tkinter.Entry(completeFrame, width=4, textvariable=contestant2Score, bd=4, relief='ridge', cursor="tcross", font=('Tahoma', 10, 'bold'))
							contestant2_score_entry.place(rely=0.5, relx=0.8, anchor='center')
							contestant2Score.set('')

							confirm_scores_button=Button(completeFrame,text = 'Confirm Scores', command = lambda : finalCompetitionCompletition(completeFrame, contestant1_score_label, contestant2_score_label), fg ='white', bg='black', relief= 'groove', font = ('Verdana',11,'bold'), padx =35)
							confirm_scores_button.place(rely=0.93,relx=0.5,anchor=CENTER)


						returnColour(username_label, username2_label, start_date_label, end_date_label, view_group_label)

			conn.commit()
			conn.close()


		def finalCompetitionCompletition(frame, label1, label2):
			conn = sqlite3.connect('BadmintonClub.db')
			c = conn.cursor()

			frame.withdraw()

			isValid = True
			isValid = isValid and validate_member_scores(contestant1Score.get(), contestant2Score.get(), "Member Score 1", "Member Score 2", label1, label2)

			if isValid:
				final_member1_score = contestant1Score.get()
				final_member2_score = contestant2Score.get()

				final_score = final_member1_score + "-" + final_member2_score

				memberID = self.memberGroups.get()

				c.execute("SELECT * From competition WHERE competitionID=?", (memberID,))
				items = c.fetchone()
				if not items:
					messagebox.showinfo("info", "There is no group that exists with that number", icon="error")

				else:

					memberUsername = items[0]
					memberUsername2 = items[1]

					c.execute("""UPDATE competition SET score = :score WHERE competitionID=:competitionID""", {
						"score": str(final_score),
						"competitionID": memberID
					})

					member_winner = ""

					if int(final_member1_score) == 21:
						c.execute("SELECT * From member WHERE username=?", (memberUsername,))
						member1 = c.fetchone()
						if not member1:
							messagebox.showinfo("info", "There is no username named " + memberUsername)

						else:

							member_winner = member1[2] + " " + member1[3]

					if int(final_member2_score) == 21:
						c.execute("SELECT * From member WHERE username=?", (memberUsername2,))
						member2 = c.fetchone()
						if not member2:
							messagebox.showinfo("info", "There is no username named " + memberUsername2)

						else:

							member_winner = member2[2] + " " + member2[3]


					c.execute("""UPDATE competition SET winner = :winner WHERE competitionID=:competitionID""", {
						"winner": str(member_winner),
						"competitionID": memberID
					})


					messagebox.showinfo("info", "The final score has been saved as " + str(final_score))
					messagebox.showinfo("info", "The winner is " + str(member_winner))


			conn.commit()
			conn.close()

			treeviewPopulate()


		def memberGroupSelection(self):
			memberGroups = StringVar()

			group_name_choices = get_group_details(self)
			if (len(group_name_choices) > 0) :
				group_selection_dropdown = ttk.Combobox(self.results, value=group_name_choices, textvariable=memberGroups,font=('Tahoma', 11, 'bold'), width=5)
				group_selection_dropdown.place(rely=0.163, relx=0.73, anchor='center')
				group_selection_dropdown.config(state='readonly')


		def get_group_details(self):
			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
			c = conn.cursor()

			group_name_list = []

			c.execute("SELECT * From competition")
			items = c.fetchall()

			for row in items:
				if row == [] or row[2] == '' or row[3] == '' or row[5] != '':
					pass
				else:
					group_name = row[6]
					group_name_list.append(group_name)

			conn.commit()
			conn.close()

			return group_name_list



		startDate=StringVar()
		endDate=StringVar()

		contestant1Score = StringVar()
		contestant2Score = StringVar()




		username_label = tkinter.Label(self.results, text="Member 1:", font=('Tahoma', 15, 'bold'), fg='black', bg='white')
		username_label.place(rely=0.16, relx=0.09, anchor='center')

		username2_label = tkinter.Label(self.results, text="Member 2:", font=('Tahoma', 15, 'bold'), fg='black', bg='white')
		username2_label.place(rely=0.24, relx=0.09, anchor='center')


		background_entry_canvas = Canvas(self.results,width=257, height=28, bg = "white")
		background_entry_canvas.place(rely=0.5,relx=0.46,anchor=CENTER)

		background_entry_image = PhotoImage(file ="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Images/Competition_boxes.png")

		background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
		background_entry_canvas.background_entry_image = background_entry_image


		contestant1_label = tkinter.Label(self.results, text="", font=('Tahoma', 10, 'bold'), fg='black', bg='white')
		contestant1_label.place(rely=0.5, relx=0.46, anchor='center')

		background_entry_canvas = Canvas(self.results,width=257, height=28, bg = "white")
		background_entry_canvas.place(rely=0.5,relx=0.856,anchor=CENTER)

		background_entry_image = PhotoImage(file ="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Images/Competition_boxes.png")

		background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
		background_entry_canvas.background_entry_image = background_entry_image

		contestant2_label = tkinter.Label(self.results, text="", font=('Tahoma', 10, 'bold'), fg='black', bg='white')
		contestant2_label.place(rely=0.5, relx=0.856, anchor='center')


		line1 = Canvas(self.results, width=3, height=130)
		line1.config(bg='white')
		line1.create_line(3, 0, 140, 100000)
		line1.place(rely=0.4, relx=0.643, anchor='center')

		line2 = Canvas(self.results, width=3, height=130)
		line2.config(bg='white')
		line2.create_line(3, 0, 140, 100000)
		line2.place(rely=0.4, relx=0.673, anchor='center')

		line3 = Canvas(self.results, width=45, height=3)
		line3.config(bg='white')
		line3.create_line(0, 3, 50, 3)
		line3.place(rely=0.5, relx=0.622, anchor='center')

		line4 = Canvas(self.results, width=45, height=3)
		line4.config(bg='white')
		line4.create_line(0, 3, 50, 3)
		line4.place(rely=0.5, relx=0.694, anchor='center')


		background_entry_canvas = Canvas(self.results,width=257, height=28, bg = "white")
		background_entry_canvas.place(rely=0.25,relx=0.658,anchor=CENTER)

		background_entry_image = PhotoImage(file ="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Images/Competition_boxes.png")

		background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
		background_entry_canvas.background_entry_image = background_entry_image


		contestant_winner_label = tkinter.Label(self.results, text="", font=('Tahoma', 10, 'bold'), fg='black', bg='white')
		contestant_winner_label.place(rely=0.25, relx=0.658, anchor='center')


		start_date_label = tkinter.Label(self.results, text="Start Date:", font=('Tahoma', 15, 'bold'), fg='black', bg='white')
		start_date_label.place(rely=0.42, relx=0.09, anchor='center')

		end_date_label = tkinter.Label(self.results, text="End Date:", font=('Tahoma', 15, 'bold'), fg='black', bg='white')
		end_date_label.place(rely=0.5, relx=0.09, anchor='center')

		start_date_entry = Button(self.results, text='Select Start Date',font=("Tahoma",10, 'bold'), cursor="tcross",command=lambda : startDateCheck(startDate), padx=10, bd=4, relief="ridge")
		start_date_entry.place(rely=0.423, relx=0.24, anchor='center')

		end_date_entry = Button(self.results, text='Select End Date',font=("Tahoma",10, 'bold'), cursor="tcross",command=lambda : endDateCheck(endDate), padx=10, bd=4, relief="ridge")
		end_date_entry.place(rely=0.503, relx=0.24, anchor='center')


		view_group_label = tkinter.Label(self.results, text="View Competition Group:", font=('Tahoma', 15, 'bold'), fg='black', bg='white')
		view_group_label.place(rely=0.16, relx=0.55, anchor='center')


		submit_member_button = tkinter.Button(self.results, cursor="tcross",text="Submit Members To Competition", command=submitMemberToCompetition, fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 10, 'bold'), padx=5, pady=2)
		submit_member_button.place(rely=0.32, relx=0.17, anchor='center')

		submit_date_button = tkinter.Button(self.results, cursor="tcross",text="Submit Dates of Competition", command=submitDateToCompetition, fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 10, 'bold'), padx=5, pady=2)
		submit_date_button.place(rely=0.59, relx=0.17, anchor='center')

		confirm_group_button = tkinter.Button(self.results, cursor="tcross",text="Confirm", command=confirmCompetition, fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 10, 'bold'), padx=40)
		confirm_group_button.place(rely=0.1635, relx=0.86, anchor='center')

		complete_competition_button = tkinter.Button(self.results, cursor="tcross",text="Complete Competition", command=lambda : completeCompetition(contestant1_label, contestant2_label), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 10, 'bold'), padx=5, pady=8)
		complete_competition_button.place(rely=0.582, relx=0.658, anchor='center')


		competition_TV=ttk.Treeview(self.results,height=9,columns=('Username2','Start Date','End Date','Score','Winner'))
		competition_TV.place(relx=0.5,rely=0.8, anchor=CENTER)

		competition_TV.heading("#0",text='Username')
		competition_TV.column("#0",minwidth=0,width=180)
		competition_TV.heading("#1",text='Username2')
		competition_TV.column("#1",minwidth=0,width=180)
		competition_TV.heading("#2",text='Start Date')
		competition_TV.column("#2",minwidth=0,width=100)
		competition_TV.heading("#3",text='End Date')
		competition_TV.column("#3",minwidth=0,width=100)
		competition_TV.heading("#4",text='Score')
		competition_TV.column("#4",minwidth=0,width=80)
		competition_TV.heading("#5",text='Winner')
		competition_TV.column("#5",minwidth=0,width=140)

		competition_ysearch_scrollbar = Scrollbar(self.results, orient = 'vertical', command = competition_TV.yview, cursor="tcross")
		competition_ysearch_scrollbar.place(relx=0.9,rely=0.8,anchor='center',height=210)
		competition_TV.configure(yscrollcommand=competition_ysearch_scrollbar.set)


		memberGroupSelection(self)
		treeviewPopulate()


		# def onTreeviewPopup(tvPopup, event=None):
		# 	try:
		# 		rowItem = competition_TV.identify_row(event.y)
		# 		tvPopup.selection = competition_TV.set(rowItem)
		#
		# 		competition_TV.selection_set(rowItem)
		# 		competition_TV.focus(rowItem)
		# 		tvPopup.post(event.x_root, event.y_root)
		# 	finally:
		# 		tvPopup.grab_release()
		#
		# tvPopup = Menu(self.results, tearoff = 0)
		# tvPopup.add_command(label = "Update", command = partial(updateCoachSessionDetails, True))
		# tvPopup.add_separator()
		# tvPopup.add_command(label = "Delete", command = partial(deleteCoachSessionDetails,True))
		#
		# competition_TV.bind("<Button-3>", partial(onTreeviewPopup, tvPopup))


	def memberSelection(self):
		self.memberNamesAndPasswords = StringVar()
		self.memberNamesAndPasswords2 = StringVar()

		member_name_choices = self.get_member_details()
		if (len(member_name_choices) > 0) :
			coach_selection_dropdown = ttk.Combobox(self.results, value=member_name_choices, textvariable=self.memberNamesAndPasswords ,font=('Tahoma', 9, 'bold'), width=25)
			coach_selection_dropdown.place(rely=0.163, relx=0.277, anchor='center')
			coach_selection_dropdown.config(state='readonly')

			coach_selection_dropdown2 = ttk.Combobox(self.results, value=member_name_choices, textvariable=self.memberNamesAndPasswords2 ,font=('Tahoma', 9, 'bold'), width=25)
			coach_selection_dropdown2.place(rely=0.243, relx=0.277, anchor='center')
			coach_selection_dropdown2.config(state='readonly')


	def get_member_details(self):
		conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
		c = conn.cursor()

		member_name_list = []

		c.execute("SELECT * From member")
		items = c.fetchall()

		for row in items:
			if row[8] == "no" or row == []:
				pass
			else:
				member_name = row[0]
				member_name_list.append(member_name)

		conn.commit()
		conn.close()

		return member_name_list