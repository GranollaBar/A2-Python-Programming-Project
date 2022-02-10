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
import Pmw


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
		# 			court text,
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


		def validate_singles_competition_start_date(value, label):
			if (value == ''):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The start date cannot be empty", icon='error')
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

			c.execute("SELECT * FROM SinglesCompetition")
			singles_competition_array = c.fetchall()

			ColourDates = []

			for i in singles_competition_array:
				date_1 = datetime.datetime.strptime(i[2], "%d/%m/%Y")
				stringdate = date_1.date()
				ColourDates.append(i[2])
				ColourDates.append(i[3])

				if i[2] != i[3]:
					while stringdate != i[3]:
						stringdateadd = stringdate + datetime.timedelta(days=1)
						finaldate=str(stringdateadd).split('-')
						finalnewdate=finaldate[0],finaldate[1],finaldate[2]
						a_date = datetime.date(int(finalnewdate[0]),int(finalnewdate[1]), int(finalnewdate[2]))

						date_2 = a_date.strftime("%d/%m/%Y")
						ColourDates.append(date_2)
						break

			print(ColourDates)

			for row in ColourDates:
				if value == row:
					label.config(fg="red")
					messagebox.showinfo("Validation Error", "You cannot create a competition on top of an already existing singles competition", icon='error')
					return False
				else:
					pass

			conn.commit()
			conn.close()

			label.config(fg="SpringGreen3")
			return True


		def validate_doubles_competition_start_date(value, label):
			if (value == ''):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The start date cannot be empty", icon='error')
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

			c.execute("SELECT * FROM DoublesCompetition")
			singles_competition_array = c.fetchall()

			ColourDates = []

			for i in singles_competition_array:
				date_1 = datetime.datetime.strptime(i[4], "%d/%m/%Y")
				stringdate = date_1.date()
				ColourDates.append(i[4])
				ColourDates.append(i[5])

				while stringdate != i[5]:
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
					messagebox.showinfo("Validation Error", "You cannot create a competition on top of an already existing doubles competition", icon='error')
					return False
				else:
					pass

			conn.commit()
			conn.close()

			label.config(fg="SpringGreen3")
			return True


		def validate_singles_competition_end_date(value, value2, label2):
			if (value2 == ''):
				label2.config(fg="red")
				messagebox.showinfo("Validation Error", "The end date cannot be empty", icon='error')
				return False
			if (value > value2):
				label2.config(fg="red")
				messagebox.showinfo("Validation Error", "The end date cannot be before the start date", icon='error')
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

			if (numberdate >= 8):
				label2.config(fg='red')
				messagebox.showinfo("Validation Error", "The competition can only be ran for seven days total", icon='error')
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
					messagebox.showinfo("Validation Error", "You cannot create a competition on top of an already existing singles competition", icon='error')
					return False
				else:
					pass

			conn.commit()
			conn.close()

			label2.config(fg="SpringGreen3")
			return True


		def validate_doubles_competition_end_date(value, value2, label2):
			if (value2 == ''):
				label2.config(fg="red")
				messagebox.showinfo("Validation Error", "The end date cannot be empty", icon='error')
				return False
			if (value > value2):
				label2.config(fg="red")
				messagebox.showinfo("Validation Error", "The end date cannot be before the start date", icon='error')
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

			if (numberdate >= 8):
				label2.config(fg='red')
				messagebox.showinfo("Validation Error", "The competition can only be ran for seven days total", icon='error')
				return False
			else:
				pass

			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
			c = conn.cursor()

			c.execute("SELECT * FROM DoublesCompetition")
			singles_competition_array = c.fetchall()

			ColourDates = []

			for i in singles_competition_array:
				date_1 = datetime.datetime.strptime(i[4], "%d/%m/%Y")
				stringdate = date_1.date()
				ColourDates.append(i[4])
				ColourDates.append(i[5])

				while stringdate != i[5]:
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
					messagebox.showinfo("Validation Error", "You cannot create a competition on top of an already existing doubles competition", icon='error')
					return False
				else:
					pass

			conn.commit()
			conn.close()

			label2.config(fg="SpringGreen3")
			return True


		def validate_startdate_update(value, label, SinglesTrue):
			if (value == ''):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The new start date cannot be empty", icon='error')
				return False

			presentDate = datetime.datetime.now()
			date_formated = presentDate.strftime("%d/%m/%Y")

			d1 = datetime.datetime.strptime(value, "%d/%m/%Y").date()
			d2 = datetime.datetime.strptime(str(date_formated), "%d/%m/%Y").date()

			if d2>d1:
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The start date before the current date", icon='error')
				return False

			if (SinglesTrue == True):
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
						messagebox.showinfo("Validation Error", "You cannot create a competition on top of an already existing singles competition", icon='error')
						return False
					else:
						pass

				conn.commit()
				conn.close()

				label.config(fg="SpringGreen3")
				return True

			else:
				conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
				c = conn.cursor()

				c.execute("SELECT * FROM DoublesCompetition")
				singles_competition_array = c.fetchall()

				ColourDates = []

				for i in singles_competition_array:
					date_1 = datetime.datetime.strptime(i[4], "%d/%m/%Y")
					stringdate = date_1.date()
					ColourDates.append(i[4])
					ColourDates.append(i[5])

					while stringdate != i[5]:
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
						messagebox.showinfo("Validation Error", "You cannot create a competition on top of an already existing singles competition", icon='error')
						return False
					else:
						pass

				conn.commit()
				conn.close()

				label.config(fg="SpringGreen3")
				return True


		def validate_enddate_update(value, value2, label, DoublesTrue):
			if (value2 == ''):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The end date cannot be empty", icon='error')
				return False
			if (value > value2):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The end date cannot be before the start date", icon='error')
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
				label.config(fg='red')
				messagebox.showinfo("Validation Error", "The competition can only be ran for three days total", icon='error')
				return False
			else:
				pass

			if (DoublesTrue == True):
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
						label.config(fg="red")
						messagebox.showinfo("Validation Error", "You cannot create a competition on top of an already existing singles competition", icon='error')
						return False
					else:
						pass

				conn.commit()
				conn.close()

				label.config(fg="SpringGreen3")
				return True

			else:
				conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
				c = conn.cursor()

				c.execute("SELECT * FROM DoublesCompetition")
				singles_competition_array = c.fetchall()

				ColourDates = []

				for i in singles_competition_array:
					date_1 = datetime.datetime.strptime(i[4], "%d/%m/%Y")
					stringdate = date_1.date()
					ColourDates.append(i[4])
					ColourDates.append(i[5])

					while stringdate != i[4]:
						stringdateadd = stringdate + datetime.timedelta(days=1)
						finaldate=str(stringdateadd).split('-')
						finalnewdate=finaldate[0],finaldate[1],finaldate[2]
						a_date = datetime.date(int(finalnewdate[0]),int(finalnewdate[1]), int(finalnewdate[2]))

						date_2 = a_date.strftime("%d/%m/%Y")
						ColourDates.append(date_2)
						break

				for row in ColourDates:
					if value2 == row:
						label.config(fg="red")
						messagebox.showinfo("Validation Error", "You cannot create a competition on top of an already existing singles competition", icon='error')
						return False
					else:
						pass

				conn.commit()
				conn.close()

				label.config(fg="SpringGreen3")
				return True



		def validate_singles_first_member(value, label):
			if (value == ''):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The username cannot be empty", icon='error')
				return False

			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
			c = conn.cursor()

			c.execute(f"SELECT * FROM member WHERE username=?", (str(value),))
			data = c.fetchone()

			if ('no' in data[8]):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "This member cannot be selected because they don't want to be involved with competitions", icon='error')
				return False

			label.config(fg="SpringGreen3")
			return True


		def validate_singles_second_member(value, value2, label, label2):
			if (value2 == ''):
				label2.config(fg="red")
				messagebox.showinfo("Validation Error", "The username cannot be empty", icon='error')
				return False

			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
			c = conn.cursor()

			c.execute(f"SELECT * FROM member WHERE username=?", (str(value2),))
			data = c.fetchone()

			if ('no' in data[8]):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "This member cannot be selected because they don't want to be involved with competitions", icon='error')
				return False

			if (value == value2):
				label.config(fg="red")
				label2.config(fg="red")
				messagebox.showinfo("Validation Error", "Both members cannot have the same username selected", icon='error')
				return False

			label.config(fg="SpringGreen3")
			label2.config(fg="SpringGreen3")
			return True


		def validate_doubles_first_member(value, label):
			if (value == ''):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The username cannot be empty", icon='error')
				return False

			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
			c = conn.cursor()

			c.execute(f"SELECT * FROM member WHERE username=?", (str(value),))
			data = c.fetchone()

			if ('no' in data[8]):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "This member cannot be selected because they don't want to be involved with competitions", icon='error')
				return False

			label.config(fg="SpringGreen3")
			return True


		def validate_doubles_second_member(value, value2, label):
			if (value2 == ''):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The username cannot be empty", icon='error')
				return False

			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
			c = conn.cursor()

			c.execute(f"SELECT * FROM member WHERE username=?", (str(value2),))
			data = c.fetchone()

			if ('no' in data[8]):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "This member cannot be selected because they don't want to be involved with competitions", icon='error')
				return False

			if (value == value2):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "Member 2 cannot have the same username as member 1", icon='error')
				return False

			label.config(fg="SpringGreen3")
			return True


		def validate_doubles_third_member(value, value2, value3, label):
			if (value3 == ''):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The username cannot be empty", icon='error')
				return False

			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
			c = conn.cursor()

			c.execute(f"SELECT * FROM member WHERE username=?", (str(value3),))
			data = c.fetchone()

			if ('no' in data[8]):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "This member cannot be selected because they don't want to be involved with competitions", icon='error')
				return False

			if (value3 == value):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "Member 3 cannot have the same username as member 1", icon='error')
				return False
			if (value3 == value2):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "Member 3 cannot have the same username as member 2", icon='error')
				return False

			label.config(fg="SpringGreen3")
			return True


		def validate_doubles_fourth_member(value, value2, value3, value4, label):
			if (value4 == ''):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The username cannot be empty", icon='error')
				return False

			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
			c = conn.cursor()

			c.execute(f"SELECT * FROM member WHERE username=?", (str(value4),))
			data = c.fetchone()

			if ('no' in data[8]):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "This member cannot be selected because they don't want to be involved with competitions", icon='error')
				return False

			if (value4 == value):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "Member 4 cannot have the same username as member 1", icon='error')
				return False
			if (value4 == value2):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "Member 4 cannot have the same username as member 2", icon='error')
				return False
			if (value4 == value3):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "Member 4 cannot have the same username as member 3", icon='error')
				return False

			label.config(fg="SpringGreen3")
			return True


		def validate_username_update(value, value2, label1, label2):
			if (value == ''):
				label1.config(fg="red")
				messagebox.showinfo("Validation Error", "Username1 cannot be empty", icon='error')
				return False
			if (value2 == ''):
				label2.config(fg="red")
				messagebox.showinfo("Validation Error", "Username2 cannot be empty", icon='error')
				return False
			if (value == value2):
				label1.config(fg="red")
				label2.config(fg="red")
				messagebox.showinfo("Validation Error", "Member 2 cannot have the same username as member 1", icon='error')
				return False

			label1.config(fg="SpringGreen3")
			label2.config(fg="SpringGreen3")
			return True


		def validate_court(value, label):
			if (value != True):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "One court must be selected", icon='error')
				return False

			label.config(fg="SpringGreen3")
			return True


		def validate_group_delete(value, label):
			if (value == ''):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "There must be a group selected", icon='error')
				return False

			label.config(fg='SpringGreen3')
			return True


		def clearTv(treeview):
			record=treeview.get_children()
			for elements in record:
				treeview.delete(elements)


		def singlestreeviewPopulate(treeview):
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


		def doublestreeviewPopulate(treeview):
			clearTv(treeview)

			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
			c = conn.cursor()

			c.execute("SELECT * From DoublesCompetition")
			items = c.fetchall()

			conn.commit()
			conn.close()

			count=0
			for row in items:
				if row == []:
					pass
				else:
					if count%2==0:
						treeview.insert('','end',text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]))
					else:
						treeview.insert('','end',text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]))
					count+=1


		def treeviewresizedisable(treeview, event):
			if treeview.identify_region(event.x, event.y) == "separator":
				return "break"


		def returnColour(usernameReturn, username2Return, startDateReturn, endDateReturn, CourtReturn):
			usernameReturn.config(fg="black")
			username2Return.config(fg="black")
			startDateReturn.config(fg="black")
			endDateReturn.config(fg="black")
			CourtReturn.config(fg="black")


		def one_return_colour(DeleteGroup):
			DeleteGroup.config(fg="black")


		def return_two_colour(UpdateGroup, UpdateCourt):
			UpdateGroup.config(fg="black")
			UpdateCourt.config(fg="black")


		def return_three_colour(UpdateGroup, Updatemember1, UpdateMember2):
			UpdateGroup.config(fg='black')
			Updatemember1.config(fg='black')
			UpdateMember2.config(fg='black')


		def return_five_colour(UpdateGroup, Updatemember1, Updatemember2, Updatemember3, Updatemember4):
			UpdateGroup.config(fg='black')
			Updatemember1.config(fg='black')
			Updatemember2.config(fg='black')
			Updatemember3.config(fg='black')
			Updatemember4.config(fg='black')


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
			ToolTips.bind(SelectCourtsButton, 'Confirm courts selected')


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


		def SinglesCalendarSelection(cal, event=None):
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
					messagebox.showinfo("Info", "There is a singles competition on these dates" + "\n" +
																	"The details are listed below:" + "\n\n"
																	+ "Member 1: " + str(i[0]) + "\n"
																	+ "Member 2: " + str(i[1]) + "\n"
																	+ "Start Date: " + str(i[2]) + "\n"
																	+ "End Date: " + str(i[3]) + "\n"
																	+ "Court: " + str(i[4]) + "\n"
																	, icon='info')

				if (ListComplete == False and AllListComplete == len(singles_competition_array)):
					messagebox.showinfo("Error", "There is no competition on this date", icon='error')


			conn.commit()
			conn.close()


		def DoublesCalendarSelection(cal, event=None):
			ListComplete = False
			AllListComplete = 0

			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
			c = conn.cursor()

			c.execute("SELECT * FROM DoublesCompetition")
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
				AllListComplete += 1

				if current_day[1] == start[1] and current_day[2] >= start[0] and current_day[2] <= end[0]:
					ListComplete = True
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

				if (ListComplete == False and AllListComplete == len(doubles_competition_array)):
					messagebox.showinfo("Error", "There is no competition on this date", icon='error')

			conn.commit()
			conn.close()


		def SinglesChangeCalendarColour(cal):
			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
			c = conn.cursor()

			c.execute("SELECT * FROM SinglesCompetition")
			singles_competition_array = c.fetchall()

			for dates in singles_competition_array:
				start_date = dates[2]
				end_date = dates[3]

				if start_date != end_date:
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
						print(add)
						add=str(d1+timedelta(days=i)).strip('00:00:00')
						print(add)
						add=add.split('-')
						add=add[2].strip(',')+'/'+add[1].strip(',')+'/'+add[0].strip(',')
						all_days_inbetween.append(add)

					if end_date not in all_days_inbetween:
						all_days_inbetween.append(end_date)

					for finaldates in all_days_inbetween:
						finalfinaldate=str(finaldates).split('/')
						cal.calevent_create(datetime.date(int(finalfinaldate[2]), int(finalfinaldate[1]), int(finalfinaldate[0])),"View Coaching Session Details","message")

					cal.tag_config("message", background="SpringGreen3", foreground="black")

				else:
					cal.calevent_create(datetime.date(int(dates[3][6:10]), int(dates[3][3:5]), int(dates[3][0:2])),"View Coaching Session Details","message")
					cal.tag_config("message", background="SpringGreen3", foreground="black")

			conn.close()


		def DoublesChangeCalendarColour(cal):
			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
			c = conn.cursor()

			c.execute("SELECT * FROM DoublesCompetition")
			doubles_competition_array = c.fetchall()


			for dates in doubles_competition_array:
				start_date = dates[4]
				end_date = dates[5]

				if start_date != end_date:
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
						add=str(d1+timedelta(days=i)).strip('00:00:00')
						add=add.split('-')
						add=add[2].strip(',')+'/'+add[1].strip(',')+'/'+add[0].strip(',')
						all_days_inbetween.append(add)

					if end_date not in all_days_inbetween:
						all_days_inbetween.append(end_date)

					for finaldates in all_days_inbetween:
						finalfinaldate=str(finaldates).split('/')
						cal.calevent_create(datetime.date(int(finalfinaldate[2]), int(finalfinaldate[1]), int(finalfinaldate[0])),"View Coaching Session Details","message")

					cal.tag_config("message", background="SpringGreen3", foreground="black")

				else:
					cal.calevent_create(datetime.date(int(dates[3][6:10]), int(dates[3][3:5]), int(dates[3][0:2])),"View Coaching Session Details","message")
					cal.tag_config("message", background="SpringGreen3", foreground="black")

			conn.close()


		def SinglesDeleteCompetition(value, value2, value3):
			isValid = True
			isValid = isValid and validate_group_delete(value2.get(), value)

			if isValid:
				GroupSelected = value2.get()

				response = askyesno("Question", "Are you sure you want to delete this group?", icon='question')
				if response == False:
					showinfo("Info", "Deletion cancelled", icon='info')

				else:
					conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
					c = conn.cursor()

					c.execute(f"SELECT * FROM SinglesCompetition WHERE singlescompetitionID =?", (str(GroupSelected),))
					data = c.fetchone()
					if not data:
						messagebox.showinfo("Error", "The group selected was not found in the database", icon='error')

					else:

						c.execute(f"DELETE FROM SinglesCompetition WHERE singlescompetitionID =?", (str(GroupSelected),))
						messagebox.showinfo('Info', "Group " + str(GroupSelected) + " has been removed from the singles competition list", icon='info')

						conn.commit()

						c.execute("SELECT * From SinglesCompetition")
						items = c.fetchall()

						newID = len(items) - len(items) + 1
						oldID = len(items) - len(items) + 2

						for row in items:
							if row != '':
								c.execute("UPDATE SinglesCompetition SET singlescompetitionID = :newsinglescompetitionID WHERE singlescompetitionID=:oldsinglescompetitionID", {
									"newsinglescompetitionID": newID,
									"oldsinglescompetitionID": oldID
								})
								newID += 1
								oldID += 1
							else:
								break

						conn.commit()

						value2.place_forget()
						one_return_colour(value)

						singles_competitionID_list = []

						c.execute("SELECT * From SinglesCompetition")
						information = c.fetchall()

						for row in information:
							if row == []:
								pass
							else:
								singlesCompetitionID = row[5]
								singles_competitionID_list.append(singlesCompetitionID)

						final_singlesID_choices = singles_competitionID_list

						final_member_delete_dropdown = ttk.Combobox(self.competition, value=final_singlesID_choices, textvariable=SinglesIDChoice ,font=('Tahoma', 10, 'bold'), width=5)
						final_member_delete_dropdown.place(rely=0.29, relx=0.53, anchor='center')
						final_member_delete_dropdown.config(state='readonly')
						final_member_delete_dropdown.set('')

						singlestreeviewPopulate(value3)

						conn.close()



		def DoublesDeleteCompetition(value, value2, value3):
			isValid = True
			isValid = isValid and validate_group_delete(value2.get(), value)

			if isValid:
				GroupSelected = value2.get()

				response = askyesno("Question", "Are you sure you want to delete this group?", icon='question')
				if response == False:
					showinfo("Info", "Deletion cancelled", icon='info')

				else:
					conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
					c = conn.cursor()

					c.execute(f"SELECT * FROM DoublesCompetition WHERE doublescompetitionID =?", (str(GroupSelected),))
					data = c.fetchone()
					if not data:
						messagebox.showinfo("Error", "The group selected was not found in the database", icon='error')

					else:

						c.execute(f"DELETE FROM DoublesCompetition WHERE doublescompetitionID =?", (str(GroupSelected),))
						messagebox.showinfo('Info', "Group " + str(GroupSelected) + " has been removed from the doubles competition list", icon='info')

						conn.commit()

						c.execute("SELECT * From DoublesCompetition")
						items = c.fetchall()

						newID = len(items) - len(items) + 1
						oldID = len(items) - len(items) + 2

						for row in items:
							if row != '':
								c.execute("UPDATE DoublesCompetition SET doublescompetitionID = :newdoublescompetitionID WHERE doublescompetitionID=:olddoublescompetitionID", {
									"newdoublescompetitionID": newID,
									"olddoublescompetitionID": oldID
								})
								newID += 1
								oldID += 1
								if (newID == len(items)):
									c.execute("UPDATE DoublesCompetition SET doublescompetitionID = :newdoublescompetitionID WHERE doublescompetitionID=:olddoublescompetitionID", {
										"newdoublescompetitionID": newID,
										"olddoublescompetitionID": oldID
									})
							else:
								break

						conn.commit()

						value2.place_forget()
						one_return_colour(value)

						doubles_competitionID_list = []

						c.execute("SELECT * From DoublesCompetition")
						information = c.fetchall()

						for row in information:
							if row == []:
								pass
							else:
								doublesCompetitionID = row[9]
								doubles_competitionID_list.append(doublesCompetitionID)

						final_doublesID_choices = doubles_competitionID_list

						final_member_delete_dropdown = ttk.Combobox(self.competition, value=final_doublesID_choices, textvariable=DoublesIDChoice ,font=('Tahoma', 10, 'bold'), width=5)
						final_member_delete_dropdown.place(rely=0.29, relx=0.53, anchor='center')
						final_member_delete_dropdown.config(state='readonly')
						final_member_delete_dropdown.set('')

						doublestreeviewPopulate(value3)

						conn.close()



		def SinglesUpdateCompetition(label1, label2, label3, value1, value2, value3, treeview):
			if (UpdateSelectionSingles.get() == 1):
				isValid = True
				isValid = isValid and validate_group_delete(value1.get(), label1)
				isValid = isValid and validate_username_update(value2.get(), value3.get(), label2, label3)

				if isValid:
					GroupSelected = value1.get()
					newmember1 = value2.get()
					newmember2 = value3.get()

					response = askyesno("Question", "Are you sure you want to update this group?", icon='question')
					if response == False:
						showinfo("Info", "Update cancelled", icon='info')

					else:
						conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
						c = conn.cursor()

						c.execute(f"SELECT * FROM SinglesCompetition WHERE singlescompetitionID =?", (str(GroupSelected),))
						data = c.fetchone()
						if not data:
							messagebox.showinfo("Error", "The group selected was not found in the database", icon='error')

						else:

							c.execute("UPDATE SinglesCompetition SET username = :newusername WHERE singlescompetitionID=:groupID", {
								"newusername": newmember1,
								"groupID": str(GroupSelected)
							})

							c.execute("UPDATE SinglesCompetition SET username2 = :newusername2 WHERE singlescompetitionID=:groupID", {
								"newusername2": newmember2,
								"groupID": str(GroupSelected)
							})

							messagebox.showinfo('Info', "Group " + str(GroupSelected) + " has been updated to include member emails " + newmember1 + " and " + newmember2, icon='info')

							value1.set('')
							value2.set('')
							value3.set('')

							return_two_colour(label1, label2)

							conn.commit()
							conn.close()

							singlestreeviewPopulate(treeview)

			if (UpdateSelectionSingles.get() == 2):
				SinglesStartDateUpdate = True
				SinglesEndDateUpdate = True
				isValid = True
				isValid = isValid and validate_group_delete(value1.get(), label1)
				isValid = isValid and validate_startdate_update(startDate.get(), label2, SinglesStartDateUpdate)
				isValid = isValid and validate_enddate_update(startDate.get(), endDate.get(), label3, SinglesEndDateUpdate)

				if isValid:
					GroupSelected = value1.get()
					finalstartdate = startDate.get()
					finalenddate = endDate.get()

					response = askyesno("Question", "Are you sure you want to update this group?", icon='question')
					if response == False:
						showinfo("Info", "Update cancelled", icon='info')

					else:
						conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
						c = conn.cursor()

						c.execute(f"SELECT * FROM SinglesCompetition WHERE singlescompetitionID =?", (str(GroupSelected),))
						data = c.fetchone()
						if not data:
							messagebox.showinfo("Error", "The group selected was not found in the database", icon='error')

						else:

							c.execute("UPDATE SinglesCompetition SET start_date = :newstartdate WHERE singlescompetitionID=:groupID", {
								"newstartdate": finalstartdate,
								"groupID": str(GroupSelected)
							})

							c.execute("UPDATE SinglesCompetition SET end_date = :newenddate WHERE singlescompetitionID=:groupID", {
								"newenddate": finalenddate,
								"groupID": str(GroupSelected)
							})

							messagebox.showinfo('Info', "Group " + str(GroupSelected) + " has been updated with new start date: " + finalstartdate + " and new end date: " + finalenddate, icon='info')

							value1.set('')
							startDate.set('')
							endDate.set('')

							return_three_colour(label1, label2, label3)

							conn.commit()
							conn.close()

							singlestreeviewPopulate(treeview)

			if (UpdateSelectionSingles.get() == 3):
				isValid = True
				isValid = isValid and validate_group_delete(value1.get(), label1)
				isValid = isValid and validate_court(CourtsTrue, label2)

				if isValid:
					GroupSelected = value1.get()

					response = askyesno("Question", "Are you sure you want to update this group?", icon='question')
					if response == False:
						showinfo("Info", "Update cancelled", icon='info')

					else:
						conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
						c = conn.cursor()

						c.execute(f"SELECT * FROM SinglesCompetition WHERE singlescompetitionID =?", (str(GroupSelected),))
						data = c.fetchone()
						if not data:
							messagebox.showinfo("Error", "The group selected was not found in the database", icon='error')

						else:

							c.execute("UPDATE SinglesCompetition SET court = :newcourt WHERE singlescompetitionID=:groupID", {
								"newcourt": FinalSelectedCourts,
								"groupID": str(GroupSelected)
							})

							messagebox.showinfo('Info', "Group " + str(GroupSelected) + " has been updated, and has now been assigned court " + FinalSelectedCourts, icon='info')

							value1.set('')

							return_two_colour(label1, label2)

							conn.commit()
							conn.close()

							singlestreeviewPopulate(treeview)


		def DoublesUpdateCompetition(label1, label2, label3, label4, label5, value1, value2, value3, value4, value5, treeview):
			if (UpdateSelectionDoubles.get() == 1):
				isValid = True
				isValid = isValid and validate_group_delete(value1.get(), label1)
				isValid = isValid and validate_doubles_first_member(value2.get(), label2)
				isValid = isValid and validate_doubles_second_member(value2.get(), value3.get(), label3)
				isValid = isValid and validate_doubles_third_member(value2.get(), value3.get(), value4.get(), label4)
				isValid = isValid and validate_doubles_fourth_member(value2.get(), value3.get(), value4.get(), value5.get(), label5)

				if isValid:
					GroupSelected = value1.get()
					newmember1 = value2.get()
					newmember2 = value3.get()
					newmember3 = value4.get()
					newmember4 = value5.get()

					response = askyesno("Question", "Are you sure you want to update this group?", icon='question')
					if response == False:
						showinfo("Info", "Update cancelled", icon='info')

					else:
						conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
						c = conn.cursor()

						c.execute(f"SELECT * FROM DoublesCompetition WHERE doublescompetitionID =?", (str(GroupSelected),))
						data = c.fetchone()
						if not data:
							messagebox.showinfo("Error", "The group selected was not found in the database", icon='error')

						else:

							c.execute("UPDATE DoublesCompetition SET username = :newusername WHERE doublescompetitionID=:groupID", {
								"newusername": newmember1,
								"groupID": str(GroupSelected)
							})

							c.execute("UPDATE DoublesCompetition SET username2 = :newusername2 WHERE doublescompetitionID=:groupID", {
								"newusername2": newmember2,
								"groupID": str(GroupSelected)
							})

							c.execute("UPDATE DoublesCompetition SET username3 = :newusername3 WHERE doublescompetitionID=:groupID", {
								"newusername3": newmember3,
								"groupID": str(GroupSelected)
							})

							c.execute("UPDATE DoublesCompetition SET username4 = :newusername4 WHERE doublescompetitionID=:groupID", {
								"newusername4": newmember4,
								"groupID": str(GroupSelected)
							})

							messagebox.showinfo('Info', "Group " + str(GroupSelected) + " has been updated to include member emails " + newmember1 + ", " + newmember2 + ", " + newmember3 + " and " + newmember4, icon='info')

							value1.set('')
							value2.set('')
							value3.set('')
							value4.set('')
							value5.set('')

							return_five_colour(label1, label2, label3, label4, label5)

							conn.commit()
							conn.close()

							doublestreeviewPopulate(treeview)

			if (UpdateSelectionDoubles.get() == 2):
				isValid = True
				isValid = isValid and validate_group_delete(value1.get(), label1)
				isValid = isValid and validate_startdate_update(startDate.get(), label2, None)
				isValid = isValid and validate_enddate_update(startDate.get(), endDate.get(), label3, None)

				if isValid:
					GroupSelected = value1.get()
					finalstartdate = startDate.get()
					finalenddate = endDate.get()

					response = askyesno("Question", "Are you sure you want to update this group?", icon='question')
					if response == False:
						showinfo("Info", "Update cancelled", icon='info')

					else:
						conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
						c = conn.cursor()

						c.execute(f"SELECT * FROM DoublesCompetition WHERE doublescompetitionID =?", (str(GroupSelected),))
						data = c.fetchone()
						if not data:
							messagebox.showinfo("Error", "The group selected was not found in the database", icon='error')

						else:

							c.execute("UPDATE DoublesCompetition SET start_date = :newstartdate WHERE doublescompetitionID=:groupID", {
								"newstartdate": finalstartdate,
								"groupID": str(GroupSelected)
							})

							c.execute("UPDATE DoublesCompetition SET end_date = :newenddate WHERE doublescompetitionID=:groupID", {
								"newenddate": finalenddate,
								"groupID": str(GroupSelected)
							})

							messagebox.showinfo('Info', "Group " + str(GroupSelected) + " has been updated with new start date: " + finalstartdate + " and new end date: " + finalenddate, icon='info')

							value1.set('')
							startDate.set('')
							endDate.set('')

							return_three_colour(label1, label2, label3)

							conn.commit()
							conn.close()

							doublestreeviewPopulate(treeview)

			if (UpdateSelectionDoubles.get() == 3):
				isValid = True
				isValid = isValid and validate_group_delete(value1.get(), label1)
				isValid = isValid and validate_court(CourtsTrue, label2)

				if isValid:
					GroupSelected = value1.get()

					response = askyesno("Question", "Are you sure you want to update this group?", icon='question')
					if response == False:
						showinfo("Info", "Update cancelled", icon='info')

					else:
						conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
						c = conn.cursor()

						c.execute(f"SELECT * FROM DoublesCompetition WHERE doublescompetitionID =?", (str(GroupSelected),))
						data = c.fetchone()
						if not data:
							messagebox.showinfo("Error", "The group selected was not found in the database", icon='error')

						else:

							c.execute("UPDATE DoublesCompetition SET court = :newcourt WHERE doublescompetitionID=:groupID", {
								"newcourt": FinalSelectedCourts,
								"groupID": str(GroupSelected)
							})

							messagebox.showinfo('Info', "Group " + str(GroupSelected) + " has been updated, and has now been assigned court " + FinalSelectedCourts, icon='info')

							value1.set('')

							return_two_colour(label1, label2)

							conn.commit()
							conn.close()

							doublestreeviewPopulate(treeview)



		def SubmitNewSingles(label1, label2, label3, label4, label5, cal, treeview):
			AllEmailsComplete = 0

			isValid = True
			isValid = isValid and validate_singles_first_member(memberNamesAndPasswords.get(), label1)
			isValid = isValid and validate_singles_second_member(memberNamesAndPasswords.get(), memberNamesAndPasswords2.get(), label1, label2)
			isValid = isValid and validate_singles_competition_start_date(startDate.get(), label3)
			isValid = isValid and validate_singles_competition_end_date(startDate.get(), endDate.get(), label4)
			isValid = isValid and validate_court(CourtsTrue, label5)

			if isValid:
				FinalMember1 = memberNamesAndPasswords.get()
				FinalMember2 = memberNamesAndPasswords2.get()
				FinalStartDate = startDate.get()
				FinalEndDate = endDate.get()
				FinalCourt = FinalSelectedCourts

				response = askyesno("Question", "Are you sure that all information above is correct?", icon='question')
				if response == False:
					showinfo("Info", "submition cancelled", icon='info')

				else:
					conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
					c = conn.cursor()

					c.execute("SELECT * From member")
					items = c.fetchall()

					for row in items:
						if str(row[0]) != str(memberNamesAndPasswords.get()) and str(row[0]) != str(memberNamesAndPasswords2.get()):
							AllEmailsComplete += 1
							pass
						else:
							member_name = row[0]
							SessionEmail("New Singles Competition Date Set", "A coach at Lisburn Racquets Club has set up a new singles competition. The start and end date of the competition is listed below:" + "\n\n" + "Start Date: " + FinalStartDate + "\n" + "End Date: " + FinalEndDate + "\n\n" + "Court: " + FinalCourt + "\n\n" + "Check the opening and closing times of the club as you will need to complete the competition between them" + "\n" + "Thanks for choosing Lisburn Racquets Club", member_name, label1)
							AllEmailsComplete += 1
							if (AllEmailsComplete == len(items)):
								messagebox.showinfo('Info', 'All members involved have been sent information about the upcoming singles competition', icon='info')

					c.execute("SELECT * FROM SinglesCompetition")
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

					SinglesChangeCalendarColour(cal)

					memberNamesAndPasswords.set('')
					memberNamesAndPasswords2.set('')

					returnColour(label1, label2, label3, label4, label5)
					messagebox.showinfo("Info", "Details have been successfully stored", icon='info')

			singlestreeviewPopulate(treeview)


		def SubmitNewDoubles(label1, label2, label3, label4, label5, cal, treeview):
			AllEmailsComplete = 0

			isValid = True
			isValid = isValid and validate_doubles_first_member(memberNamesAndPasswords.get(), label1)
			isValid = isValid and validate_doubles_second_member(memberNamesAndPasswords.get(), memberNamesAndPasswords2.get(), label1)
			isValid = isValid and validate_doubles_third_member(memberNamesAndPasswords.get(), memberNamesAndPasswords2.get(), memberNamesAndPasswords3.get(), label2)
			isValid = isValid and validate_doubles_fourth_member(memberNamesAndPasswords.get(), memberNamesAndPasswords2.get(), memberNamesAndPasswords3.get(), memberNamesAndPasswords4.get(), label2)
			isValid = isValid and validate_doubles_competition_start_date(startDate.get(), label3)
			isValid = isValid and validate_doubles_competition_end_date(startDate.get(), endDate.get(), label4)
			isValid = isValid and validate_court(CourtsTrue, label5)

			if isValid:
				FinalMember1 = memberNamesAndPasswords.get()
				FinalMember2 = memberNamesAndPasswords2.get()
				FinalMember3 = memberNamesAndPasswords3.get()
				FinalMember4 = memberNamesAndPasswords4.get()
				FinalStartDate = startDate.get()
				FinalEndDate = endDate.get()
				FinalCourt = FinalSelectedCourts

				response = askyesno("Question", "Are you sure that all information above is correct?", icon='question')
				if response == False:
					showinfo("Info", "submition cancelled", icon='info')

				else:
					conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
					c = conn.cursor()

					c.execute("SELECT * From member")
					items = c.fetchall()

					for users in items:
						if str(users[0]) == str(FinalMember1):
							c.execute(f"SELECT * FROM member WHERE username=?", (str(FinalMember1),))
							data = c.fetchone()
							first_firstname = data[2]
							first_surname = data[3]
							finalUsername1 = first_firstname + ' ' + first_surname
						if str(users[0]) == str(FinalMember2):
							c.execute(f"SELECT * FROM member WHERE username=?", (str(FinalMember2),))
							data = c.fetchone()
							second_firstname = data[2]
							second_surname = data[3]
							finalUsername2 = second_firstname + ' ' + second_surname
						if str(users[0]) == str(FinalMember3):
							c.execute(f"SELECT * FROM member WHERE username=?", (str(FinalMember3),))
							data = c.fetchone()
							third_firstname = data[2]
							third_surname = data[3]
							finalUsername3 = third_firstname + ' ' + third_surname
						if str(users[0]) == str(FinalMember4):
							c.execute(f"SELECT * FROM member WHERE username=?", (str(FinalMember4),))
							data = c.fetchone()
							fourth_firstname = data[2]
							fourth_surname = data[3]
							finalUsername4 = fourth_firstname + ' ' + fourth_surname

					c.execute("SELECT * From member")
					otheritems = c.fetchall()

					counter = 0
					finalfinalusername1 = str(finalUsername1)
					finalfinalusername2 = str(finalUsername2)
					finalfinalusername3 = str(finalUsername3)
					finalfinalusername4 = str(finalUsername4)

					for row in otheritems:
						if str(row[0]) != str(FinalMember1) and str(row[0]) != str(FinalMember2) and str(row[0]) != str(FinalMember3) and str(row[0]) != str(FinalMember1):
							AllEmailsComplete += 1
							pass
						else:
							if str(row[0]) == str(FinalMember1):
								member_name = row[0]
								SessionEmail("New Doubles Competition Date Set", "A coach at Lisburn Racquets Club has set up a new doubles competition. The start and end date of the competition is listed below:" + "\n\n" + "Start Date: " + FinalStartDate + "\n" + "End Date: " + FinalEndDate + "\n\n" + "Court: " + FinalCourt + "\n\n" + "The coach has assigned your teammate as: " + finalfinalusername2 + "\n\n" + "Check the opening and closing times of the club as you will need to complete the competition between them" + "\n" + "Thanks for choosing Lisburn Racquets Club", member_name, label1)
								AllEmailsComplete += 1
							if str(row[0]) == str(FinalMember2):
								member_name = row[0]
								SessionEmail("New Doubles Competition Date Set", "A coach at Lisburn Racquets Club has set up a new doubles competition. The start and end date of the competition is listed below:" + "\n\n" + "Start Date: " + FinalStartDate + "\n" + "End Date: " + FinalEndDate + "\n\n" + "Court: " + FinalCourt + "\n\n" + "The coach has assigned your teammate as: " + finalfinalusername1 + "\n\n" + "Check the opening and closing times of the club as you will need to complete the competition between them" + "\n" + "Thanks for choosing Lisburn Racquets Club", member_name, label1)
								AllEmailsComplete += 1
							if str(row[0]) == str(FinalMember3):
								member_name = row[0]
								SessionEmail("New Doubles Competition Date Set", "A coach at Lisburn Racquets Club has set up a new doubles competition. The start and end date of the competition is listed below:" + "\n\n" + "Start Date: " + FinalStartDate + "\n" + "End Date: " + FinalEndDate + "\n\n" + "Court: " + FinalCourt + "\n\n" + "The coach has assigned your teammate as: " + finalfinalusername4 + "\n\n" + "Check the opening and closing times of the club as you will need to complete the competition between them" + "\n" + "Thanks for choosing Lisburn Racquets Club", member_name, label1)
								AllEmailsComplete += 1
							if str(row[0]) == str(FinalMember4):
								member_name = row[0]
								SessionEmail("New Doubles Competition Date Set", "A coach at Lisburn Racquets Club has set up a new doubles competition. The start and end date of the competition is listed below:" + "\n\n" + "Start Date: " + FinalStartDate + "\n" + "End Date: " + FinalEndDate + "\n\n" + "Court: " + FinalCourt + "\n\n" + "The coach has assigned your teammate as: " + finalfinalusername3 + "\n\n" + "Check the opening and closing times of the club as you will need to complete the competition between them" + "\n" + "Thanks for choosing Lisburn Racquets Club", member_name, label1)
								AllEmailsComplete += 1

					if (AllEmailsComplete == len(items)):
						messagebox.showinfo('Info', 'All members involved have been sent information about the upcoming doublescompetition', icon='info')

					team1 = finalUsername1 + ' / ' + finalUsername2
					team2 = finalUsername3 + ' / ' + finalUsername4

					c.execute("SELECT * FROM DoublesCompetition")
					competition_array = c.fetchall()
					newId = len(competition_array) + 1

					c.execute("INSERT INTO DoublesCompetition VALUES (:member1, :member2, :member3, :member4, :startDate, :endDate, :court, :team1, :team2, :doublescompetitionID)",
							  {
								  'member1': FinalMember1,
								  'member2': FinalMember2,
								  'member3': FinalMember3,
								  'member4': FinalMember4,
								  'startDate': FinalStartDate,
								  'endDate': FinalEndDate,
								  'court': FinalSelectedCourts,
								  'team1': team1,
								  'team2': team2,
								  'doublescompetitionID': newId,
							  })

					conn.commit()
					conn.close()

					DoublesChangeCalendarColour(cal)

					memberNamesAndPasswords.set('')
					memberNamesAndPasswords2.set('')
					memberNamesAndPasswords3.set('')
					memberNamesAndPasswords4.set('')

					returnColour(label1, label2, label3, label4, label5)
					messagebox.showinfo("Info", "Details have been successfully stored", icon='info')

			doublestreeviewPopulate(treeview)


		def UpdateSinglesSelectionConfirmation(value, value2, value3, value4, value5):
			value.config(fg='grey')
			value2.config(state='disabled')
			value3.config(state='disabled')
			value4.config(state='disabled')
			value5.config(state='disabled')

			line1 = Canvas(self.competition, width=3, height=130)
			line1.config(bg='white')
			line1.create_line(3, 0, 140, 100000)
			line1.place(rely=0.9, relx=0.31, anchor='center')

			if (UpdateSelectionSingles.get() == 1):
				singles_competition_treeview=ttk.Treeview(self.competition,height=15,columns=('Member 2','Start Date','End Date','Court','singlescompetitionID'))
				singles_competition_treeview.place(relx=0.495,rely=0.59,anchor=CENTER)

				singles_competition_treeview.heading("#0",text='Member 1')
				singles_competition_treeview.column("#0",minwidth=0,width=230)
				singles_competition_treeview.heading("#1",text='Member 2')
				singles_competition_treeview.column("#1",minwidth=0,width=230)
				singles_competition_treeview.heading("#2",text='Start Date')
				singles_competition_treeview.column("#2",minwidth=0,width=125)
				singles_competition_treeview.heading("#3",text='End Date')
				singles_competition_treeview.column("#3",minwidth=0,width=125)
				singles_competition_treeview.heading("#4",text='Court')
				singles_competition_treeview.column("#4",minwidth=0,width=125)
				singles_competition_treeview.heading("#5",text='Group ID')
				singles_competition_treeview.column("#5",minwidth=0,width=100)
				singles_competition_treeview.bind('<Button-1>', partial(treeviewresizedisable, singles_competition_treeview))

				singles_competition_ysearch_scrollbar = Scrollbar(self.competition, orient = 'vertical', command = singles_competition_treeview.yview, cursor="tcross")
				singles_competition_ysearch_scrollbar.place(relx=0.975,rely=0.59,anchor='center',height=327)
				singles_competition_treeview.configure(yscrollcommand=singles_competition_ysearch_scrollbar.set)

				singlestreeviewPopulate(singles_competition_treeview)


				select_singles_group_label = tkinter.Label(self.competition, text="Select group:", font=('Tahoma', 12, 'bold'), fg='black', bg='white')
				select_singles_group_label.place(rely=0.92, relx=0.1, anchor='center')

				conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
				c = conn.cursor()

				singles_competitionID_list = []

				c.execute("SELECT * From SinglesCompetition")
				items = c.fetchall()

				for row in items:
					if row == []:
						pass
					else:
						singlesCompetitionID = row[5]
						singles_competitionID_list.append(singlesCompetitionID)

				final_singlesID_choices = singles_competitionID_list

				member_update_dropdown = ttk.Combobox(self.competition, value=final_singlesID_choices, textvariable=SinglesIDChoice ,font=('Tahoma', 10, 'bold'), width=5)
				member_update_dropdown.place(rely=0.924, relx=0.205, anchor='center')
				member_update_dropdown.config(state='readonly')


				username_label = tkinter.Label(self.competition, text="New Member 1:", font=('Tahoma', 12, 'bold'), fg='black', bg='white')
				username_label.place(rely=0.883, relx=0.47, anchor='center')

				username2_label = tkinter.Label(self.competition, text="New Member 2:", font=('Tahoma', 12, 'bold'), fg='black', bg='white')
				username2_label.place(rely=0.943, relx=0.47, anchor='center')

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

				member_selection_dropdown = ttk.Combobox(self.competition, value=member_name_choices, textvariable=memberNamesAndPasswords ,font=('Tahoma', 8, 'bold'), width=25)
				member_selection_dropdown.place(rely=0.883, relx=0.66, anchor='center')
				member_selection_dropdown.config(state='readonly')

				member_selection_dropdown2 = ttk.Combobox(self.competition, value=member_name_choices, textvariable=memberNamesAndPasswords2 ,font=('Tahoma', 8, 'bold'), width=25)
				member_selection_dropdown2.place(rely=0.943, relx=0.66, anchor='center')
				member_selection_dropdown2.config(state='readonly')

				singles_update_button = tkinter.Button(self.competition, cursor="tcross",text="Update Group", command= lambda : SinglesUpdateCompetition(select_singles_group_label, username_label, username2_label, member_update_dropdown, member_selection_dropdown, member_selection_dropdown2, singles_competition_treeview), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 10, 'bold'), padx=5, pady=2)
				singles_update_button.place(rely=0.92, relx=0.9, anchor='center')
				ToolTips.bind(singles_update_button, 'Update details of singles competition')

			if (UpdateSelectionSingles.get() == 2):
				singles_competition_treeview=ttk.Treeview(self.competition,height=15,columns=('Member 2','Start Date','End Date','Court','singlescompetitionID'))
				singles_competition_treeview.place(relx=0.495,rely=0.59,anchor=CENTER)

				singles_competition_treeview.heading("#0",text='Member 1')
				singles_competition_treeview.column("#0",minwidth=0,width=230)
				singles_competition_treeview.heading("#1",text='Member 2')
				singles_competition_treeview.column("#1",minwidth=0,width=230)
				singles_competition_treeview.heading("#2",text='Start Date')
				singles_competition_treeview.column("#2",minwidth=0,width=125)
				singles_competition_treeview.heading("#3",text='End Date')
				singles_competition_treeview.column("#3",minwidth=0,width=125)
				singles_competition_treeview.heading("#4",text='Court')
				singles_competition_treeview.column("#4",minwidth=0,width=125)
				singles_competition_treeview.heading("#5",text='Group ID')
				singles_competition_treeview.column("#5",minwidth=0,width=100)
				singles_competition_treeview.bind('<Button-1>', partial(treeviewresizedisable, singles_competition_treeview))

				singles_competition_ysearch_scrollbar = Scrollbar(self.competition, orient = 'vertical', command = singles_competition_treeview.yview, cursor="tcross")
				singles_competition_ysearch_scrollbar.place(relx=0.975,rely=0.59,anchor='center',height=327)
				singles_competition_treeview.configure(yscrollcommand=singles_competition_ysearch_scrollbar.set)

				singlestreeviewPopulate(singles_competition_treeview)


				select_singles_group_label = tkinter.Label(self.competition, text="Select group:", font=('Tahoma', 12, 'bold'), fg='black', bg='white')
				select_singles_group_label.place(rely=0.92, relx=0.1, anchor='center')

				conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
				c = conn.cursor()

				singles_competitionID_list = []

				c.execute("SELECT * From SinglesCompetition")
				items = c.fetchall()

				for row in items:
					if row == []:
						pass
					else:
						singlesCompetitionID = row[5]
						singles_competitionID_list.append(singlesCompetitionID)

				final_singlesID_choices = singles_competitionID_list

				member_update_dropdown = ttk.Combobox(self.competition, value=final_singlesID_choices, textvariable=SinglesIDChoice ,font=('Tahoma', 10, 'bold'), width=5)
				member_update_dropdown.place(rely=0.924, relx=0.205, anchor='center')
				member_update_dropdown.config(state='readonly')

				new_start_date_label = tkinter.Label(self.competition, text="New Start Date:", font=('Tahoma', 12, 'bold'), fg='black', bg='white')
				new_start_date_label.place(rely=0.883, relx=0.48, anchor='center')

				new_end_date_label = tkinter.Label(self.competition, text="New End Date:", font=('Tahoma', 12, 'bold'), fg='black', bg='white')
				new_end_date_label.place(rely=0.953, relx=0.48, anchor='center')

				new_start_date_entry = Button(self.competition, text='Select New Start Date',font=("Tahoma",10, 'bold'), cursor="tcross",command=lambda : startDateCheck(startDate), padx=10, bd=4, relief="ridge")
				new_start_date_entry.place(rely=0.883, relx=0.66, anchor='center')
				ToolTips.bind(new_start_date_entry, 'Update start date of singles competition')

				new_end_date_entry = Button(self.competition, text='Select New End Date',font=("Tahoma",10, 'bold'), cursor="tcross",command=lambda : endDateCheck(endDate), padx=10, bd=4, relief="ridge")
				new_end_date_entry.place(rely=0.953, relx=0.66, anchor='center')
				ToolTips.bind(new_end_date_entry, 'Update end date of singles competition')

				singles_update_button = tkinter.Button(self.competition, cursor="tcross",text="Update Group", command= lambda : SinglesUpdateCompetition(select_singles_group_label, new_start_date_label, new_end_date_label, member_update_dropdown, new_start_date_entry, new_end_date_entry, singles_competition_treeview), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 10, 'bold'), padx=5, pady=2)
				singles_update_button.place(rely=0.92, relx=0.9, anchor='center')
				ToolTips.bind(singles_update_button, 'Update details of singles competition')


			if (UpdateSelectionSingles.get() == 3):
				singles_competition_treeview=ttk.Treeview(self.competition,height=15,columns=('Member 2','Start Date','End Date','Court','singlescompetitionID'))
				singles_competition_treeview.place(relx=0.495,rely=0.59,anchor=CENTER)

				singles_competition_treeview.heading("#0",text='Member 1')
				singles_competition_treeview.column("#0",minwidth=0,width=230)
				singles_competition_treeview.heading("#1",text='Member 2')
				singles_competition_treeview.column("#1",minwidth=0,width=230)
				singles_competition_treeview.heading("#2",text='Start Date')
				singles_competition_treeview.column("#2",minwidth=0,width=125)
				singles_competition_treeview.heading("#3",text='End Date')
				singles_competition_treeview.column("#3",minwidth=0,width=125)
				singles_competition_treeview.heading("#4",text='Court')
				singles_competition_treeview.column("#4",minwidth=0,width=125)
				singles_competition_treeview.heading("#5",text='Group ID')
				singles_competition_treeview.column("#5",minwidth=0,width=100)
				singles_competition_treeview.bind('<Button-1>', partial(treeviewresizedisable, singles_competition_treeview))

				singles_competition_ysearch_scrollbar = Scrollbar(self.competition, orient = 'vertical', command = singles_competition_treeview.yview, cursor="tcross")
				singles_competition_ysearch_scrollbar.place(relx=0.975,rely=0.59,anchor='center',height=327)
				singles_competition_treeview.configure(yscrollcommand=singles_competition_ysearch_scrollbar.set)

				singlestreeviewPopulate(singles_competition_treeview)


				select_singles_group_label = tkinter.Label(self.competition, text="Select group:", font=('Tahoma', 12, 'bold'), fg='black', bg='white')
				select_singles_group_label.place(rely=0.92, relx=0.1, anchor='center')

				conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
				c = conn.cursor()

				singles_competitionID_list = []

				c.execute("SELECT * From SinglesCompetition")
				items = c.fetchall()

				for row in items:
					if row == []:
						pass
					else:
						singlesCompetitionID = row[5]
						singles_competitionID_list.append(singlesCompetitionID)

				final_singlesID_choices = singles_competitionID_list

				member_update_dropdown = ttk.Combobox(self.competition, value=final_singlesID_choices, textvariable=SinglesIDChoice ,font=('Tahoma', 10, 'bold'), width=5)
				member_update_dropdown.place(rely=0.924, relx=0.205, anchor='center')
				member_update_dropdown.config(state='readonly')


				new_court_label = tkinter.Label(self.competition, text="New Court:", font=('Tahoma', 12, 'bold'), fg='black', bg='white')
				new_court_label.place(rely=0.92, relx=0.52, anchor='center')

				new_court_button = Button(self.competition, text='Select New Court',font=("Tahoma",10, 'bold'), cursor="tcross",command=courtRequired, padx=10, bd=4, relief="ridge")
				new_court_button.place(rely=0.921, relx=0.66, anchor='center')
				ToolTips.bind(new_court_button, 'Update court of singles competition')

				singles_update_button = tkinter.Button(self.competition, cursor="tcross",text="Update Group", command= lambda : SinglesUpdateCompetition(select_singles_group_label, new_court_label, None, member_update_dropdown, None, None, singles_competition_treeview), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 10, 'bold'), padx=5, pady=2)
				singles_update_button.place(rely=0.92, relx=0.9, anchor='center')
				ToolTips.bind(singles_update_button, 'Update details of singles competition')


		def UpdateDoublesSelectionConfirmation(value1, value2, value3, value4, value5):
			value1.config(fg='grey')
			value2.config(state='disabled')
			value3.config(state='disabled')
			value4.config(state='disabled')
			value5.config(state='disabled')

			line1 = Canvas(self.competition, width=2, height=180)
			line1.config(bg='black')
			line1.create_line(3, 0, 140, 100000)
			line1.place(rely=0.88, relx=0.31, anchor='center')

			if (UpdateSelectionDoubles.get() == 1):
				doubles_competition_treeview=ttk.Treeview(self.competition,height=13,columns=('Member 2','Member 3','Member 4','Start Date','End Date','court','Team 1','Team 2','Group ID'))
				doubles_competition_treeview.place(relx=0.495,rely=0.55,anchor=CENTER)

				doubles_competition_treeview.heading("#0",text='Member 1')
				doubles_competition_treeview.column("#0",minwidth=0,width=115)
				doubles_competition_treeview.heading("#1",text='Member 2')
				doubles_competition_treeview.column("#1",minwidth=0,width=115)
				doubles_competition_treeview.heading("#2",text='Member 3')
				doubles_competition_treeview.column("#2",minwidth=0,width=115)
				doubles_competition_treeview.heading("#3",text='Member 4')
				doubles_competition_treeview.column("#3",minwidth=0,width=115)
				doubles_competition_treeview.heading("#4",text='Start Date')
				doubles_competition_treeview.column("#4",minwidth=0,width=70)
				doubles_competition_treeview.heading("#5",text='End Date')
				doubles_competition_treeview.column("#5",minwidth=0,width=70)
				doubles_competition_treeview.heading("#6",text='court')
				doubles_competition_treeview.column("#6",minwidth=0,width=50)
				doubles_competition_treeview.heading("#7",text='Team 1')
				doubles_competition_treeview.column("#7",minwidth=0,width=115)
				doubles_competition_treeview.heading("#8",text='Team 2')
				doubles_competition_treeview.column("#8",minwidth=0,width=115)
				doubles_competition_treeview.heading("#9",text='Group ID')
				doubles_competition_treeview.column("#9",minwidth=0,width=70)
				doubles_competition_treeview.bind('<Button-1>', partial(treeviewresizedisable, doubles_competition_treeview))

				doubles_competition_ysearch_scrollbar = Scrollbar(self.competition, orient = 'vertical', command = doubles_competition_treeview.yview, cursor="tcross")
				doubles_competition_ysearch_scrollbar.place(relx=0.985,rely=0.55,anchor='center',height=286)
				doubles_competition_treeview.configure(yscrollcommand=doubles_competition_ysearch_scrollbar.set)

				doublestreeviewPopulate(doubles_competition_treeview)


				select_doubles_group_label = tkinter.Label(self.competition, text="Select group:", font=('Tahoma', 12, 'bold'), fg='black', bg='white')
				select_doubles_group_label.place(rely=0.884, relx=0.1, anchor='center')

				conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
				c = conn.cursor()

				doubles_competitionID_list = []

				c.execute("SELECT * From DoublesCompetition")
				items = c.fetchall()

				for row in items:
					if row == []:
						pass
					else:
						doublesCompetitionID = row[9]
						doubles_competitionID_list.append(doublesCompetitionID)

				final_doublesID_choices = doubles_competitionID_list

				member_update_dropdown = ttk.Combobox(self.competition, value=final_doublesID_choices, textvariable=DoublesIDChoice ,font=('Tahoma', 10, 'bold'), width=5)
				member_update_dropdown.place(rely=0.888, relx=0.205, anchor='center')
				member_update_dropdown.config(state='readonly')


				username_label = tkinter.Label(self.competition, text="New Member 1:", font=('Tahoma', 12, 'bold'), fg='black', bg='white')
				username_label.place(rely=0.809, relx=0.47, anchor='center')

				username2_label = tkinter.Label(self.competition, text="New Member 2:", font=('Tahoma', 12, 'bold'), fg='black', bg='white')
				username2_label.place(rely=0.859, relx=0.47, anchor='center')

				username3_label = tkinter.Label(self.competition, text="New Member 3:", font=('Tahoma', 12, 'bold'), fg='black', bg='white')
				username3_label.place(rely=0.909, relx=0.47, anchor='center')

				username4_label = tkinter.Label(self.competition, text="New Member 4:", font=('Tahoma', 12, 'bold'), fg='black', bg='white')
				username4_label.place(rely=0.959, relx=0.47, anchor='center')

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

				member_selection_dropdown = ttk.Combobox(self.competition, value=member_name_choices, textvariable=memberNamesAndPasswords ,font=('Tahoma', 8, 'bold'), width=25)
				member_selection_dropdown.place(rely=0.812, relx=0.66, anchor='center')
				member_selection_dropdown.config(state='readonly')

				member_selection_dropdown2 = ttk.Combobox(self.competition, value=member_name_choices, textvariable=memberNamesAndPasswords2 ,font=('Tahoma', 8, 'bold'), width=25)
				member_selection_dropdown2.place(rely=0.862, relx=0.66, anchor='center')
				member_selection_dropdown2.config(state='readonly')

				member_selection_dropdown3 = ttk.Combobox(self.competition, value=member_name_choices, textvariable=memberNamesAndPasswords3 ,font=('Tahoma', 8, 'bold'), width=25)
				member_selection_dropdown3.place(rely=0.912, relx=0.66, anchor='center')
				member_selection_dropdown3.config(state='readonly')

				member_selection_dropdown4 = ttk.Combobox(self.competition, value=member_name_choices, textvariable=memberNamesAndPasswords4 ,font=('Tahoma', 8, 'bold'), width=25)
				member_selection_dropdown4.place(rely=0.962, relx=0.66, anchor='center')
				member_selection_dropdown4.config(state='readonly')

				doubles_update_button = tkinter.Button(self.competition, cursor="tcross",text="Update Group", command= lambda : DoublesUpdateCompetition(select_doubles_group_label, username_label, username2_label, username3_label, username4_label, member_update_dropdown, member_selection_dropdown, member_selection_dropdown2, member_selection_dropdown3, member_selection_dropdown4, doubles_competition_treeview), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 10, 'bold'), padx=5, pady=2)
				doubles_update_button.place(rely=0.884, relx=0.9, anchor='center')
				ToolTips.bind(doubles_update_button, 'Update details of doubles competition')

			if (UpdateSelectionDoubles.get() == 2):
				doubles_competition_treeview=ttk.Treeview(self.competition,height=15,columns=('Member 2','Member 3','Member 4','Start Date','End Date','court','Team 1','Team 2','Group ID'))
				doubles_competition_treeview.place(relx=0.495,rely=0.59,anchor=CENTER)

				doubles_competition_treeview.heading("#0",text='Member 1')
				doubles_competition_treeview.column("#0",minwidth=0,width=115)
				doubles_competition_treeview.heading("#1",text='Member 2')
				doubles_competition_treeview.column("#1",minwidth=0,width=115)
				doubles_competition_treeview.heading("#2",text='Member 3')
				doubles_competition_treeview.column("#2",minwidth=0,width=115)
				doubles_competition_treeview.heading("#3",text='Member 4')
				doubles_competition_treeview.column("#3",minwidth=0,width=115)
				doubles_competition_treeview.heading("#4",text='Start Date')
				doubles_competition_treeview.column("#4",minwidth=0,width=70)
				doubles_competition_treeview.heading("#5",text='End Date')
				doubles_competition_treeview.column("#5",minwidth=0,width=70)
				doubles_competition_treeview.heading("#6",text='court')
				doubles_competition_treeview.column("#6",minwidth=0,width=50)
				doubles_competition_treeview.heading("#7",text='Team 1')
				doubles_competition_treeview.column("#7",minwidth=0,width=115)
				doubles_competition_treeview.heading("#8",text='Team 2')
				doubles_competition_treeview.column("#8",minwidth=0,width=115)
				doubles_competition_treeview.heading("#9",text='Group ID')
				doubles_competition_treeview.column("#9",minwidth=0,width=70)
				doubles_competition_treeview.bind('<Button-1>', partial(treeviewresizedisable, doubles_competition_treeview))

				doubles_competition_ysearch_scrollbar = Scrollbar(self.competition, orient = 'vertical', command = doubles_competition_treeview.yview, cursor="tcross")
				doubles_competition_ysearch_scrollbar.place(relx=0.985,rely=0.59,anchor='center',height=327)
				doubles_competition_treeview.configure(yscrollcommand=doubles_competition_ysearch_scrollbar.set)

				doublestreeviewPopulate(doubles_competition_treeview)


				select_doubles_group_label = tkinter.Label(self.competition, text="Select group:", font=('Tahoma', 12, 'bold'), fg='black', bg='white')
				select_doubles_group_label.place(rely=0.92, relx=0.1, anchor='center')

				conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
				c = conn.cursor()

				doubles_competitionID_list = []

				c.execute("SELECT * From DoublesCompetition")
				items = c.fetchall()

				for row in items:
					if row == []:
						pass
					else:
						doublesCompetitionID = row[9]
						doubles_competitionID_list.append(doublesCompetitionID)

				final_doublesID_choices = doubles_competitionID_list

				member_update_dropdown = ttk.Combobox(self.competition, value=final_doublesID_choices, textvariable=DoublesIDChoice ,font=('Tahoma', 10, 'bold'), width=5)
				member_update_dropdown.place(rely=0.924, relx=0.205, anchor='center')
				member_update_dropdown.config(state='readonly')


				new_start_date_label = tkinter.Label(self.competition, text="New Start Date:", font=('Tahoma', 12, 'bold'), fg='black', bg='white')
				new_start_date_label.place(rely=0.883, relx=0.48, anchor='center')

				new_end_date_label = tkinter.Label(self.competition, text="New End Date:", font=('Tahoma', 12, 'bold'), fg='black', bg='white')
				new_end_date_label.place(rely=0.953, relx=0.48, anchor='center')

				new_start_date_entry = Button(self.competition, text='Select New Start Date',font=("Tahoma",10, 'bold'), cursor="tcross",command=lambda : startDateCheck(startDate), padx=10, bd=4, relief="ridge")
				new_start_date_entry.place(rely=0.883, relx=0.66, anchor='center')
				ToolTips.bind(new_start_date_entry, 'Update the start date of the doubles competition')

				new_end_date_entry = Button(self.competition, text='Select New End Date',font=("Tahoma",10, 'bold'), cursor="tcross",command=lambda : endDateCheck(endDate), padx=10, bd=4, relief="ridge")
				new_end_date_entry.place(rely=0.953, relx=0.66, anchor='center')
				ToolTips.bind(new_end_date_entry, 'Update the end date of the doubles competition')

				doubles_update_button = tkinter.Button(self.competition, cursor="tcross",text="Update Group", command= lambda : DoublesUpdateCompetition(select_doubles_group_label, new_start_date_label, new_end_date_label, None, None, member_update_dropdown, None, None, None, None, doubles_competition_treeview), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 10, 'bold'), padx=5, pady=2)
				doubles_update_button.place(rely=0.92, relx=0.9, anchor='center')
				ToolTips.bind(doubles_update_button, 'Update details of doubles competition')

			if (UpdateSelectionDoubles.get() == 3):
				doubles_competition_treeview=ttk.Treeview(self.competition,height=15,columns=('Member 2','Member 3','Member 4','Start Date','End Date','court','Team 1','Team 2','Group ID'))
				doubles_competition_treeview.place(relx=0.495,rely=0.59,anchor=CENTER)

				doubles_competition_treeview.heading("#0",text='Member 1')
				doubles_competition_treeview.column("#0",minwidth=0,width=115)
				doubles_competition_treeview.heading("#1",text='Member 2')
				doubles_competition_treeview.column("#1",minwidth=0,width=115)
				doubles_competition_treeview.heading("#2",text='Member 3')
				doubles_competition_treeview.column("#2",minwidth=0,width=115)
				doubles_competition_treeview.heading("#3",text='Member 4')
				doubles_competition_treeview.column("#3",minwidth=0,width=115)
				doubles_competition_treeview.heading("#4",text='Start Date')
				doubles_competition_treeview.column("#4",minwidth=0,width=70)
				doubles_competition_treeview.heading("#5",text='End Date')
				doubles_competition_treeview.column("#5",minwidth=0,width=70)
				doubles_competition_treeview.heading("#6",text='court')
				doubles_competition_treeview.column("#6",minwidth=0,width=50)
				doubles_competition_treeview.heading("#7",text='Team 1')
				doubles_competition_treeview.column("#7",minwidth=0,width=115)
				doubles_competition_treeview.heading("#8",text='Team 2')
				doubles_competition_treeview.column("#8",minwidth=0,width=115)
				doubles_competition_treeview.heading("#9",text='Group ID')
				doubles_competition_treeview.column("#9",minwidth=0,width=70)
				doubles_competition_treeview.bind('<Button-1>', partial(treeviewresizedisable, doubles_competition_treeview))

				doubles_competition_ysearch_scrollbar = Scrollbar(self.competition, orient = 'vertical', command = doubles_competition_treeview.yview, cursor="tcross")
				doubles_competition_ysearch_scrollbar.place(relx=0.985,rely=0.59,anchor='center',height=327)
				doubles_competition_treeview.configure(yscrollcommand=doubles_competition_ysearch_scrollbar.set)

				doublestreeviewPopulate(doubles_competition_treeview)


				select_doubles_group_label = tkinter.Label(self.competition, text="Select group:", font=('Tahoma', 12, 'bold'), fg='black', bg='white')
				select_doubles_group_label.place(rely=0.92, relx=0.1, anchor='center')

				conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
				c = conn.cursor()

				doubles_competitionID_list = []

				c.execute("SELECT * From DoublesCompetition")
				items = c.fetchall()

				for row in items:
					if row == []:
						pass
					else:
						doublesCompetitionID = row[9]
						doubles_competitionID_list.append(doublesCompetitionID)

				final_doublesID_choices = doubles_competitionID_list

				member_update_dropdown = ttk.Combobox(self.competition, value=final_doublesID_choices, textvariable=DoublesIDChoice ,font=('Tahoma', 10, 'bold'), width=5)
				member_update_dropdown.place(rely=0.924, relx=0.205, anchor='center')
				member_update_dropdown.config(state='readonly')


				new_court_label = tkinter.Label(self.competition, text="New Court:", font=('Tahoma', 12, 'bold'), fg='black', bg='white')
				new_court_label.place(rely=0.92, relx=0.52, anchor='center')

				new_court_button = Button(self.competition, text='Select New Court',font=("Tahoma",10, 'bold'), cursor="tcross",command=courtRequired, padx=10, bd=4, relief="ridge")
				new_court_button.place(rely=0.921, relx=0.66, anchor='center')
				ToolTips.bind(new_court_button, 'Update the doubles court of the competition')

				doubles_update_button = tkinter.Button(self.competition, cursor="tcross",text="Update Group", command= lambda : DoublesUpdateCompetition(select_doubles_group_label, new_court_label, None, None, None, member_update_dropdown, None, None, None, None, doubles_competition_treeview), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 10, 'bold'), padx=5, pady=2)
				doubles_update_button.place(rely=0.92, relx=0.9, anchor='center')
				ToolTips.bind(doubles_update_button, 'Update doubles group of the competition')




		def MatchTypeConfirmation(value, value2, value3, value4):
			value.config(fg='grey')
			value2.config(state='disabled')
			value3.config(state='disabled')
			value4.config(state='disabled')

			competition_status_label = tkinter.Label(self.competition, text="Competition Status:", font=('Tahoma', 12, 'bold'), fg='black', bg='white')
			competition_status_label.place(rely=0.198, relx=0.205, anchor='center')

			competition_status_new = Radiobutton(self.competition, text="Create New", variable=CompetitionStatus, value=1, font=("Tahoma",9, 'bold'), cursor="tcross", bg="white", bd=2, relief="ridge")
			competition_status_new.place(rely=0.2, relx=0.36, anchor='center')

			competition_status_update = Radiobutton(self.competition, text="Update Existing", variable=CompetitionStatus, value=2, font=("Tahoma",9, 'bold'), cursor="tcross", bg="white", bd=2, relief="ridge")
			competition_status_update.place(rely=0.2, relx=0.5, anchor='center')

			competition_status_delete = Radiobutton(self.competition, text="Delete Existing", variable=CompetitionStatus, value=3, font=("Tahoma",9, 'bold'), cursor="tcross", bg="white", bd=2, relief="ridge")
			competition_status_delete.place(rely=0.2, relx=0.65, anchor='center')
			CompetitionStatus.set("1")

			competition_status_button = tkinter.Button(self.competition, cursor="tcross",text="Select Status", command= lambda : CompetitionStatusConfirmation(competition_status_label, competition_status_new, competition_status_update, competition_status_delete, competition_status_button), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 9, 'bold'), padx=2)
			competition_status_button.place(rely=0.1995, relx=0.79, anchor='center')
			ToolTips.bind(competition_status_button, 'Confirm the status of the competition')

			competition_status_line = Canvas(self.competition, width=1000, height=2)
			competition_status_line.config(bg='black')
			competition_status_line.create_line(3, 0, 200, 100000)
			competition_status_line.place(rely=0.233, relx=0.5, anchor='center')


		def CompetitionStatusConfirmation(value5, value6, value7, value8, value9):
			value5.config(fg='grey')
			value6.config(state='disabled')
			value7.config(state='disabled')
			value8.config(state='disabled')
			value9.config(state='disabled')

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

				member_selection_dropdown = ttk.Combobox(self.competition, value=member_name_choices, textvariable=memberNamesAndPasswords ,font=('Tahoma', 9, 'bold'), width=25)
				member_selection_dropdown.place(rely=0.293, relx=0.277, anchor='center')
				member_selection_dropdown.config(state='readonly')

				member_selection_dropdown2 = ttk.Combobox(self.competition, value=member_name_choices, textvariable=memberNamesAndPasswords2 ,font=('Tahoma', 9, 'bold'), width=25)
				member_selection_dropdown2.place(rely=0.373, relx=0.277, anchor='center')
				member_selection_dropdown2.config(state='readonly')


				start_date_label = tkinter.Label(self.competition, text="Start Date:", font=('Tahoma', 15, 'bold'), fg='black', bg='white')
				start_date_label.place(rely=0.45, relx=0.09, anchor='center')

				end_date_label = tkinter.Label(self.competition, text="End Date:", font=('Tahoma', 15, 'bold'), fg='black', bg='white')
				end_date_label.place(rely=0.53, relx=0.09, anchor='center')

				start_date_entry = Button(self.competition, text='Select Start Date',font=("Tahoma",10, 'bold'), cursor="tcross",command=lambda : startDateCheck(startDate), padx=10, bd=4, relief="ridge")
				start_date_entry.place(rely=0.453, relx=0.277, anchor='center')
				ToolTips.bind(start_date_entry, 'Select the start date for the competition')

				end_date_entry = Button(self.competition, text='Select End Date',font=("Tahoma",10, 'bold'), cursor="tcross",command=lambda : endDateCheck(endDate), padx=10, bd=4, relief="ridge")
				end_date_entry.place(rely=0.533, relx=0.277, anchor='center')
				ToolTips.bind(end_date_entry, 'Select the end date for the competition')

				court_label = tkinter.Label(self.competition, text="Court:", font=('Tahoma', 15, 'bold'), fg='black', bg='white')
				court_label.place(rely=0.61, relx=0.09, anchor='center')

				court_button = Button(self.competition, text='Select Court',font=("Tahoma",10, 'bold'), cursor="tcross",command=courtRequired, padx=10, bd=4, relief="ridge")
				court_button.place(rely=0.613, relx=0.277, anchor='center')
				ToolTips.bind(court_button, 'Select the court required for the competition')


				calendar_label =Label(self.competition, text = 'Singles Competition Dates', fg ='black',bg='white',font=('Tahoma',11,'bold'), bd=2, relief="ridge", padx=10, pady=3)
				calendar_label.place(rely=0.286,relx=0.67,anchor=CENTER)
				today = date.today()
				cal = Calendar(self.competition, font="Tahoma 16", selectmode='day', cursor="tcross", year=today.year, month=today.month, day=today.day)
				cal.place(rely=0.51, relx=0.67, anchor='center')
				cal.bind("<<CalendarSelected>>", partial(SinglesCalendarSelection, cal))


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
				singles_competition_treeview.bind('<Button-1>', partial(treeviewresizedisable, singles_competition_treeview))

				singles_competition_ysearch_scrollbar = Scrollbar(self.competition, orient = 'vertical', command = singles_competition_treeview.yview, cursor="tcross")
				singles_competition_ysearch_scrollbar.place(relx=0.98,rely=0.86,anchor='center',height=147)
				singles_competition_treeview.configure(yscrollcommand=singles_competition_ysearch_scrollbar.set)

				singlestreeviewPopulate(singles_competition_treeview)
				SinglesChangeCalendarColour(cal)

				submit_new_singles_button = tkinter.Button(self.competition, cursor="tcross",text="Submit", command=lambda : SubmitNewSingles(username_label, username2_label, start_date_label, end_date_label, court_label, cal, singles_competition_treeview), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 11, 'bold'), padx=30, pady=2)
				submit_new_singles_button.place(rely=0.695, relx=0.28, anchor='center')
				ToolTips.bind(submit_new_singles_button, 'Submit new singles competition')



			if (MatchType.get() == 2 and CompetitionStatus.get() == 1):
				team_label = tkinter.Label(self.competition, text="Team 1:", font=('Tahoma', 15, 'bold'), fg='black', bg='white')
				team_label.place(rely=0.29, relx=0.09, anchor='center')

				team2_label = tkinter.Label(self.competition, text="Team 2:", font=('Tahoma', 15, 'bold'), fg='black', bg='white')
				team2_label.place(rely=0.37, relx=0.09, anchor='center')


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

				member_team_selection_dropdown = ttk.Combobox(self.competition, value=member_name_choices, textvariable=memberNamesAndPasswords ,font=('Tahoma', 9, 'bold'), width=35)
				member_team_selection_dropdown.place(rely=0.293, relx=0.32, anchor='center')
				member_team_selection_dropdown.config(state='readonly')

				member2_team_selection_dropdown = ttk.Combobox(self.competition, value=member_name_choices, textvariable=memberNamesAndPasswords2 ,font=('Tahoma', 9, 'bold'), width=35)
				member2_team_selection_dropdown.place(rely=0.293, relx=0.68, anchor='center')
				member2_team_selection_dropdown.config(state='readonly')

				member_team_selection_dropdown2 = ttk.Combobox(self.competition, value=member_name_choices, textvariable=memberNamesAndPasswords3 ,font=('Tahoma', 9, 'bold'), width=35)
				member_team_selection_dropdown2.place(rely=0.373, relx=0.32, anchor='center')
				member_team_selection_dropdown2.config(state='readonly')

				member2_team_selection_dropdown2 = ttk.Combobox(self.competition, value=member_name_choices, textvariable=memberNamesAndPasswords4 ,font=('Tahoma', 9, 'bold'), width=35)
				member2_team_selection_dropdown2.place(rely=0.373, relx=0.68, anchor='center')
				member2_team_selection_dropdown2.config(state='readonly')


				start_date_label = tkinter.Label(self.competition, text="Start Date:", font=('Tahoma', 15, 'bold'), fg='black', bg='white')
				start_date_label.place(rely=0.45, relx=0.09, anchor='center')

				end_date_label = tkinter.Label(self.competition, text="End Date:", font=('Tahoma', 15, 'bold'), fg='black', bg='white')
				end_date_label.place(rely=0.53, relx=0.09, anchor='center')

				start_date_entry = Button(self.competition, text='Select Start Date',font=("Tahoma",10, 'bold'), cursor="tcross",command=lambda : startDateCheck(startDate), padx=10, bd=4, relief="ridge")
				start_date_entry.place(rely=0.453, relx=0.277, anchor='center')
				ToolTips.bind(start_date_entry, 'Select the start date for the competition')

				end_date_entry = Button(self.competition, text='Select End Date',font=("Tahoma",10, 'bold'), cursor="tcross",command=lambda : endDateCheck(endDate), padx=10, bd=4, relief="ridge")
				end_date_entry.place(rely=0.533, relx=0.277, anchor='center')
				ToolTips.bind(end_date_entry, 'Select the end date for the competition')

				court_label = tkinter.Label(self.competition, text="Court:", font=('Tahoma', 15, 'bold'), fg='black', bg='white')
				court_label.place(rely=0.61, relx=0.09, anchor='center')

				court_button = Button(self.competition, text='Select Court',font=("Tahoma",10, 'bold'), cursor="tcross",command=courtRequired, padx=10, bd=4, relief="ridge")
				court_button.place(rely=0.613, relx=0.277, anchor='center')
				ToolTips.bind(court_button, 'Select the court required for the competition')


				calendar_label =Label(self.competition, text = 'Doubles Competition Dates', fg ='black',bg='white',font=('Tahoma',7,'bold'), bd=2, relief="ridge", padx=10, pady=3)
				calendar_label.place(rely=0.426,relx=0.67,anchor=CENTER)
				today = datetime.date.today()
				cal = Calendar(self.competition, font="Tahoma 10", selectmode='day', cursor="tcross", year=today.year, month=today.month, day=today.day)
				cal.place(rely=0.588, relx=0.67, anchor='center')
				cal.bind("<<CalendarSelected>>", partial(DoublesCalendarSelection, cal))


				doubles_competition_treeview=ttk.Treeview(self.competition,height=5,columns=('Member 2','Member 3','Member 4','Start Date','End Date','court','Team 1','Team 2'))
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
				doubles_competition_treeview.column("#4",minwidth=0,width=70)
				doubles_competition_treeview.heading("#5",text='End Date')
				doubles_competition_treeview.column("#5",minwidth=0,width=70)
				doubles_competition_treeview.heading("#6",text='court')
				doubles_competition_treeview.column("#6",minwidth=0,width=50)
				doubles_competition_treeview.heading("#7",text='Team 1')
				doubles_competition_treeview.column("#7",minwidth=0,width=140)
				doubles_competition_treeview.heading("#8",text='Team 2')
				doubles_competition_treeview.column("#8",minwidth=0,width=140)
				doubles_competition_treeview.bind('<Button-1>', partial(treeviewresizedisable, doubles_competition_treeview))

				doubles_competition_ysearch_scrollbar = Scrollbar(self.competition, orient = 'vertical', command = doubles_competition_treeview.yview, cursor="tcross")
				doubles_competition_ysearch_scrollbar.place(relx=0.976,rely=0.86,anchor='center',height=127)
				doubles_competition_treeview.configure(yscrollcommand=doubles_competition_ysearch_scrollbar.set)


				doublestreeviewPopulate(doubles_competition_treeview)
				DoublesChangeCalendarColour(cal)

				submit_new_doubles_button = tkinter.Button(self.competition, cursor="tcross",text="Submit", command=lambda : SubmitNewDoubles(team_label, team2_label, start_date_label, end_date_label, court_label, cal, doubles_competition_treeview), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 11, 'bold'), padx=30, pady=2)
				submit_new_doubles_button.place(rely=0.695, relx=0.28, anchor='center')
				ToolTips.bind(submit_new_doubles_button, 'Submit new doubles competition')



			if (MatchType.get() == 1 and CompetitionStatus.get() == 2):
				singles_update_label = tkinter.Label(self.competition, text="Which section do you want to update:", font=('Tahoma', 12, 'bold'), fg='black', bg='white')
				singles_update_label.place(rely=0.274, relx=0.175, anchor='center')

				update_usernames_radiobutton = Radiobutton(self.competition, text="Usernames", variable=UpdateSelectionSingles, value=1, font=("Tahoma",9, 'bold'), cursor="tcross", bg="white", bd=2, relief="ridge")
				update_usernames_radiobutton.place(rely=0.277, relx=0.4, anchor='center')

				update_dates_radiobutton = Radiobutton(self.competition, text="Dates", variable=UpdateSelectionSingles, value=2, font=("Tahoma",9, 'bold'), cursor="tcross", bg="white", bd=2, relief="ridge")
				update_dates_radiobutton.place(rely=0.277, relx=0.5025, anchor='center')

				update_court_radiobutton = Radiobutton(self.competition, text="Court", variable=UpdateSelectionSingles, value=3, font=("Tahoma",9, 'bold'), cursor="tcross", bg="white", bd=2, relief="ridge")
				update_court_radiobutton.place(rely=0.277, relx=0.59, anchor='center')
				UpdateSelectionSingles.set("1")

				singles_update_button = tkinter.Button(self.competition, cursor="tcross",text="Select Section", command= lambda : UpdateSinglesSelectionConfirmation(singles_update_label, update_usernames_radiobutton, update_dates_radiobutton, update_court_radiobutton, singles_update_button), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 9, 'bold'), padx=2)
				singles_update_button.place(rely=0.2765, relx=0.703, anchor='center')
				ToolTips.bind(singles_update_button, 'Confirm match to update')

				update_selection_line = Canvas(self.competition, width=1000, height=2)
				update_selection_line.config(bg='black')
				update_selection_line.create_line(3, 0, 200, 100000)
				update_selection_line.place(rely=0.313, relx=0.5, anchor='center')





			if (MatchType.get() == 2 and CompetitionStatus.get() == 2):
				doubles_update_label = tkinter.Label(self.competition, text="Which section do you want to update:", font=('Tahoma', 12, 'bold'), fg='black', bg='white')
				doubles_update_label.place(rely=0.274, relx=0.175, anchor='center')

				update_usernames_radiobutton = Radiobutton(self.competition, text="Usernames", variable=UpdateSelectionDoubles, value=1, font=("Tahoma",9, 'bold'), cursor="tcross", bg="white", bd=2, relief="ridge")
				update_usernames_radiobutton.place(rely=0.277, relx=0.4, anchor='center')

				update_dates_radiobutton = Radiobutton(self.competition, text="Dates", variable=UpdateSelectionDoubles, value=2, font=("Tahoma",9, 'bold'), cursor="tcross", bg="white", bd=2, relief="ridge")
				update_dates_radiobutton.place(rely=0.277, relx=0.5025, anchor='center')

				update_court_radiobutton = Radiobutton(self.competition, text="Court", variable=UpdateSelectionDoubles, value=3, font=("Tahoma",9, 'bold'), cursor="tcross", bg="white", bd=2, relief="ridge")
				update_court_radiobutton.place(rely=0.277, relx=0.59, anchor='center')
				UpdateSelectionDoubles.set("1")

				doubles_update_button = tkinter.Button(self.competition, cursor="tcross",text="Select Section", command= lambda : UpdateDoublesSelectionConfirmation(doubles_update_label, update_usernames_radiobutton, update_dates_radiobutton, update_court_radiobutton, doubles_update_button), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 9, 'bold'), padx=2)
				doubles_update_button.place(rely=0.2765, relx=0.703, anchor='center')
				ToolTips.bind(doubles_update_button, 'Confirm match to update')

				update_selection_line = Canvas(self.competition, width=1000, height=2)
				update_selection_line.config(bg='black')
				update_selection_line.create_line(3, 0, 200, 100000)
				update_selection_line.place(rely=0.313, relx=0.5, anchor='center')



			if (MatchType.get() == 1 and CompetitionStatus.get() == 3):
				select_group_delete_label = tkinter.Label(self.competition, text="Select which group to delete:", font=('Tahoma', 12, 'bold'), fg='black', bg='white')
				select_group_delete_label.place(rely=0.288, relx=0.355, anchor='center')

				conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
				c = conn.cursor()

				singles_competitionID_list = []

				c.execute("SELECT * From SinglesCompetition")
				items = c.fetchall()

				for row in items:
					if row == []:
						pass
					else:
						singlesCompetitionID = row[5]
						singles_competitionID_list.append(singlesCompetitionID)

				final_singlesID_choices = singles_competitionID_list

				member_delete_dropdown = ttk.Combobox(self.competition, value=final_singlesID_choices, textvariable=SinglesIDChoice ,font=('Tahoma', 10, 'bold'), width=5)
				member_delete_dropdown.place(rely=0.29, relx=0.53, anchor='center')
				member_delete_dropdown.config(state='readonly')

				singles_delete_button = tkinter.Button(self.competition, cursor="tcross",text="Delete Group", command= lambda : SinglesDeleteCompetition(select_group_delete_label, member_delete_dropdown, singles_competition_treeview), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 9, 'bold'), padx=2)
				singles_delete_button.place(rely=0.2895, relx=0.642, anchor='center')
				ToolTips.bind(singles_delete_button, 'Confirm singles match to delete')

				singles_competition_treeview=ttk.Treeview(self.competition,height=19,columns=('Member 2','Start Date','End Date','Court','singlescompetitionID'))
				singles_competition_treeview.place(relx=0.5,rely=0.66,anchor=CENTER)

				singles_competition_treeview.heading("#0",text='Member 1')
				singles_competition_treeview.column("#0",minwidth=0,width=230)
				singles_competition_treeview.heading("#1",text='Member 2')
				singles_competition_treeview.column("#1",minwidth=0,width=230)
				singles_competition_treeview.heading("#2",text='Start Date')
				singles_competition_treeview.column("#2",minwidth=0,width=125)
				singles_competition_treeview.heading("#3",text='End Date')
				singles_competition_treeview.column("#3",minwidth=0,width=125)
				singles_competition_treeview.heading("#4",text='Court')
				singles_competition_treeview.column("#4",minwidth=0,width=125)
				singles_competition_treeview.heading("#5",text='Group ID')
				singles_competition_treeview.column("#5",minwidth=0,width=100)
				singles_competition_treeview.bind('<Button-1>', partial(treeviewresizedisable, singles_competition_treeview))

				singles_competition_ysearch_scrollbar = Scrollbar(self.competition, orient = 'vertical', command = singles_competition_treeview.yview, cursor="tcross")
				singles_competition_ysearch_scrollbar.place(relx=0.98,rely=0.66,anchor='center',height=407)
				singles_competition_treeview.configure(yscrollcommand=singles_competition_ysearch_scrollbar.set)

				singlestreeviewPopulate(singles_competition_treeview)


			if (MatchType.get() == 2 and CompetitionStatus.get() == 3):
				select_group_delete_label = tkinter.Label(self.competition, text="Select which group to delete:", font=('Tahoma', 12, 'bold'), fg='black', bg='white')
				select_group_delete_label.place(rely=0.288, relx=0.355, anchor='center')

				conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
				c = conn.cursor()

				doubles_competitionID_list = []

				c.execute("SELECT * From DoublesCompetition")
				items = c.fetchall()

				for row in items:
					if row == []:
						pass
					else:
						doublesCompetitionID = row[9]
						doubles_competitionID_list.append(doublesCompetitionID)

				final_doublesID_choices = doubles_competitionID_list

				member_delete_dropdown = ttk.Combobox(self.competition, value=final_doublesID_choices, textvariable=DoublesIDChoice ,font=('Tahoma', 10, 'bold'), width=5)
				member_delete_dropdown.place(rely=0.29, relx=0.53, anchor='center')
				member_delete_dropdown.config(state='readonly')

				doubles_delete_button = tkinter.Button(self.competition, cursor="tcross",text="Delete Group", command= lambda : DoublesDeleteCompetition(select_group_delete_label, member_delete_dropdown, doubles_competition_treeview), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 9, 'bold'), padx=2)
				doubles_delete_button.place(rely=0.2895, relx=0.642, anchor='center')
				ToolTips.bind(doubles_delete_button, 'Confirm doubles match to delete')

				doubles_competition_treeview=ttk.Treeview(self.competition,height=19,columns=('Member 2','Member 3','Member 4','Start Date','End Date','court','Team 1','Team 2','Group ID'))
				doubles_competition_treeview.place(relx=0.5,rely=0.66,anchor=CENTER)

				doubles_competition_treeview.heading("#0",text='Member 1')
				doubles_competition_treeview.column("#0",minwidth=0,width=115)
				doubles_competition_treeview.heading("#1",text='Member 2')
				doubles_competition_treeview.column("#1",minwidth=0,width=115)
				doubles_competition_treeview.heading("#2",text='Member 3')
				doubles_competition_treeview.column("#2",minwidth=0,width=115)
				doubles_competition_treeview.heading("#3",text='Member 4')
				doubles_competition_treeview.column("#3",minwidth=0,width=115)
				doubles_competition_treeview.heading("#4",text='Start Date')
				doubles_competition_treeview.column("#4",minwidth=0,width=70)
				doubles_competition_treeview.heading("#5",text='End Date')
				doubles_competition_treeview.column("#5",minwidth=0,width=70)
				doubles_competition_treeview.heading("#6",text='court')
				doubles_competition_treeview.column("#6",minwidth=0,width=50)
				doubles_competition_treeview.heading("#7",text='Team 1')
				doubles_competition_treeview.column("#7",minwidth=0,width=115)
				doubles_competition_treeview.heading("#8",text='Team 2')
				doubles_competition_treeview.column("#8",minwidth=0,width=115)
				doubles_competition_treeview.heading("#9",text='Group ID')
				doubles_competition_treeview.column("#9",minwidth=0,width=70)
				doubles_competition_treeview.bind('<Button-1>', partial(treeviewresizedisable, doubles_competition_treeview))

				doubles_competition_ysearch_scrollbar = Scrollbar(self.competition, orient = 'vertical', command = doubles_competition_treeview.yview, cursor="tcross")
				doubles_competition_ysearch_scrollbar.place(relx=0.98,rely=0.66,anchor='center',height=407)
				doubles_competition_treeview.configure(yscrollcommand=doubles_competition_ysearch_scrollbar.set)

				doublestreeviewPopulate(doubles_competition_treeview)



		MatchType=IntVar()
		CompetitionStatus=IntVar()
		UpdateSelectionSingles=IntVar()
		UpdateSelectionDoubles=IntVar()

		memberNamesAndPasswords = StringVar()
		memberNamesAndPasswords2 = StringVar()
		memberNamesAndPasswords3 = StringVar()
		memberNamesAndPasswords4 = StringVar()
		SinglesIDChoice = StringVar()
		DoublesIDChoice = StringVar()
		startDate=StringVar()
		endDate=StringVar()


		ToolTips = Pmw.Balloon()



		match_type_label = tkinter.Label(self.competition, text="Type of Match:", font=('Tahoma', 12, 'bold'), fg='black', bg='white')
		match_type_label.place(rely=0.128, relx=0.33, anchor='center')

		match_type_singles = Radiobutton(self.competition, text="Singles", variable=MatchType, value=1, font=("Tahoma",9, 'bold'), cursor="tcross", bg="white", bd=2, relief="ridge")
		match_type_singles.place(rely=0.13, relx=0.45, anchor='center')

		match_type_doubles = Radiobutton(self.competition, text="Doubles", variable=MatchType, value=2, font=("Tahoma",9, 'bold'), cursor="tcross", bg="white", bd=2, relief="ridge")
		match_type_doubles.place(rely=0.13, relx=0.55, anchor='center')
		MatchType.set("1")

		match_type_button = tkinter.Button(self.competition, cursor="tcross",text="Select Match Type", command=lambda : MatchTypeConfirmation(match_type_label, match_type_singles, match_type_doubles, match_type_button), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 9, 'bold'), padx=2)
		match_type_button.place(rely=0.1295, relx=0.685, anchor='center')
		ToolTips.bind(match_type_button, 'Confirm match type selection')

		match_type_line = Canvas(self.competition, width=1000, height=2)
		match_type_line.config(bg='black')
		match_type_line.create_line(3, 0, 200, 100000)
		match_type_line.place(rely=0.163, relx=0.5, anchor='center')








