from tkinter import ttk
from tkinter import messagebox
import tkinter.simpledialog
from tkinter.messagebox import showinfo
from tkinter.messagebox import askyesno
import sqlite3
from tkinter import simpledialog
from tkinter import *
import math
from functools import partial
import datetime
from tkcalendar import Calendar, DateEntry

from MemberFrame.member_email import memberEmail
from MemberFrame.memberWordDocument import buildMemberDocument

class CoachingSessionContent:

	def __init__(self, mainScreen):
		self.coachSession = mainScreen
		self.conn = sqlite3.connect('CoachDetails.db')
		self.c = self.conn.cursor()



		self.c.execute("""CREATE TABLE coachSession (
					username text,
					startTime integer,
					endTime integer,
					date text,
					courts integer,
					group integer,
					numberPeople text,
					technique integer
					)""")


	def generateCoachSessionContnt(self):

		def dateEntryCheck(dob):
			def assign_dob():
				eventDate.set(cal.selection_get())
				top.withdraw()

			top = Toplevel(self.coachSession)

			cal = Calendar(top, font="Tahoma 16", selectmode='day', cursor="tcross", year=2021, month=5, day=29)
			cal.pack(fill="both", expand=True)
			ttk.Button(top, text="ok", command=assign_dob).pack()


		court1=IntVar()
		court2=IntVar()
		court3=IntVar()
		court4=IntVar()
		court5=IntVar()
		court6=IntVar()
		court7=IntVar()
		court8=IntVar()
		court9=IntVar()
		court10=IntVar()
		court11=IntVar()
		court12=IntVar()


		def courtsRequired():
			courts = Toplevel(self.coachSession, bg="white")
			courts.geometry('500x500')

			title_label = tkinter.Label(courts, text="Check the No. Courts Needed For The Session", font=('Tahoma', 16, 'underline', 'bold'), fg='black', bg='white')
			title_label.place(rely=0.03, relx=0.5, anchor='center')

			confirm_button = tkinter.Button(courts, text="Confirm Selection", command=lambda : confirmSelection(courts), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 10, 'bold'), padx=35, cursor="tcross")
			confirm_button.place(rely=0.112, relx=0.5, anchor='center')

			confirm_court1 = Checkbutton(courts, cursor="tcross",text="Court 1  V", variable=court1,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_court1.place(rely=0.2, relx=0.15, anchor='center')

			confirm_court2 = Checkbutton(courts, cursor="tcross",text="Court 2  V", variable=court2,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_court2.place(rely=0.4, relx=0.15, anchor='center')

			confirm_court3 = Checkbutton(courts, cursor="tcross",text="Court 3  V", variable=court3,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_court3.place(rely=0.6, relx=0.15, anchor='center')

			confirm_court4 = Checkbutton(courts, cursor="tcross",text="Court 4  V", variable=court4,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_court4.place(rely=0.8, relx=0.15, anchor='center')

			confirm_court5 = Checkbutton(courts, cursor="tcross",text="Court 5  V", variable=court5,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_court5.place(rely=0.2, relx=0.5, anchor='center')

			confirm_court6 = Checkbutton(courts, cursor="tcross",text="Court 6  V", variable=court6,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_court6.place(rely=0.4, relx=0.5, anchor='center')

			confirm_court7 = Checkbutton(courts, cursor="tcross",text="Court 7  V", variable=court7,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_court7.place(rely=0.6, relx=0.5, anchor='center')

			confirm_court8 = Checkbutton(courts, cursor="tcross",text="Court 8  V", variable=court8,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_court8.place(rely=0.8, relx=0.5, anchor='center')

			confirm_court9 = Checkbutton(courts, cursor="tcross",text="Court 9  V", variable=court9,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_court9.place(rely=0.2, relx=0.85, anchor='center')

			confirm_court10 = Checkbutton(courts, cursor="tcross",text="Court 10  V", variable=court10,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_court10.place(rely=0.4, relx=0.85, anchor='center')

			confirm_court11 = Checkbutton(courts, cursor="tcross",text="Court 11 V", variable=court11,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_court11.place(rely=0.6, relx=0.85, anchor='center')

			confirm_court12 = Checkbutton(courts, cursor="tcross",text="Court 12 V", variable=court12,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_court12.place(rely=0.8, relx=0.85, anchor='center')


			background_entry_canvas = Canvas(courts,width=100, height=58, bg = "white")
			background_entry_canvas.place(rely=0.3,relx=0.15,anchor=CENTER)

			background_entry_image = PhotoImage(file ="blueRectangle_100x58.png")

			background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
			background_entry_canvas.background_entry_image = background_entry_image


			background_entry_canvas = Canvas(courts,width=100, height=58, bg = "white")
			background_entry_canvas.place(rely=0.5,relx=0.15,anchor=CENTER)

			background_entry_image = PhotoImage(file ="blueRectangle_100x58.png")

			background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
			background_entry_canvas.background_entry_image = background_entry_image


			background_entry_canvas = Canvas(courts,width=100, height=58, bg = "white")
			background_entry_canvas.place(rely=0.7,relx=0.15,anchor=CENTER)

			background_entry_image = PhotoImage(file ="blueRectangle_100x58.png")

			background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
			background_entry_canvas.background_entry_image = background_entry_image


			background_entry_canvas = Canvas(courts,width=100, height=58, bg = "white")
			background_entry_canvas.place(rely=0.9,relx=0.15,anchor=CENTER)

			background_entry_image = PhotoImage(file ="blueRectangle_100x58.png")

			background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
			background_entry_canvas.background_entry_image = background_entry_image


			background_entry_canvas = Canvas(courts,width=100, height=58, bg = "white")
			background_entry_canvas.place(rely=0.3,relx=0.5,anchor=CENTER)

			background_entry_image = PhotoImage(file ="blueRectangle_100x58.png")

			background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
			background_entry_canvas.background_entry_image = background_entry_image


			background_entry_canvas = Canvas(courts,width=100, height=58, bg = "white")
			background_entry_canvas.place(rely=0.5,relx=0.5,anchor=CENTER)

			background_entry_image = PhotoImage(file ="blueRectangle_100x58.png")

			background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
			background_entry_canvas.background_entry_image = background_entry_image


			background_entry_canvas = Canvas(courts,width=100, height=58, bg = "white")
			background_entry_canvas.place(rely=0.7,relx=0.5,anchor=CENTER)

			background_entry_image = PhotoImage(file ="blueRectangle_100x58.png")

			background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
			background_entry_canvas.background_entry_image = background_entry_image


			background_entry_canvas = Canvas(courts,width=100, height=58, bg = "white")
			background_entry_canvas.place(rely=0.9,relx=0.5,anchor=CENTER)

			background_entry_image = PhotoImage(file ="blueRectangle_100x58.png")

			background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
			background_entry_canvas.background_entry_image = background_entry_image


			background_entry_canvas = Canvas(courts,width=100, height=58, bg = "white")
			background_entry_canvas.place(rely=0.3,relx=0.85,anchor=CENTER)

			background_entry_image = PhotoImage(file ="blueRectangle_100x58.png")

			background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
			background_entry_canvas.background_entry_image = background_entry_image


			background_entry_canvas = Canvas(courts,width=100, height=58, bg = "white")
			background_entry_canvas.place(rely=0.5,relx=0.85,anchor=CENTER)

			background_entry_image = PhotoImage(file ="blueRectangle_100x58.png")

			background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
			background_entry_canvas.background_entry_image = background_entry_image


			background_entry_canvas = Canvas(courts,width=100, height=58, bg = "white")
			background_entry_canvas.place(rely=0.7,relx=0.85,anchor=CENTER)

			background_entry_image = PhotoImage(file ="blueRectangle_100x58.png")

			background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
			background_entry_canvas.background_entry_image = background_entry_image


			background_entry_canvas = Canvas(courts,width=100, height=58, bg = "white")
			background_entry_canvas.place(rely=0.9,relx=0.85,anchor=CENTER)

			background_entry_image = PhotoImage(file ="blueRectangle_100x58.png")

			background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
			background_entry_canvas.background_entry_image = background_entry_image



		def confirmSelection(frame):
			frame.withdraw()


		group1=IntVar()
		group2=IntVar()
		group3=IntVar()
		group4=IntVar()
		group5=IntVar()
		group6=IntVar()
		group7=IntVar()
		group8=IntVar()
		group9=IntVar()
		group10=IntVar()
		group11=IntVar()
		group12=IntVar()
		group13=IntVar()
		group14=IntVar()
		group15=IntVar()
		group16=IntVar()
		group17=IntVar()
		group18=IntVar()
		group19=IntVar()
		group20=IntVar()




		def groupsRequired():
			groups = Toplevel(self.coachSession, bg="white")
			groups.geometry('450x350')

			title_label = tkinter.Label(groups, text="Check the No. Groups Needed For The Session", font=('Tahoma', 13, 'underline', 'bold'), fg='black', bg='white')
			title_label.place(rely=0.03, relx=0.5, anchor='center')

			confirm_button = tkinter.Button(groups, text="Confirm Selection", command=lambda : confirmSelection2(groups), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 9, 'bold'), padx=35, cursor="tcross")
			confirm_button.place(rely=0.15, relx=0.5, anchor='center')


			confirm_group1 = Checkbutton(groups, cursor="tcross",text="Group 1", variable=group1,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_group1.place(rely=0.3, relx=0.15, anchor='center')

			confirm_group2 = Checkbutton(groups, cursor="tcross",text="Group 2", variable=group2,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_group2.place(rely=0.3, relx=0.38, anchor='center')

			confirm_group3 = Checkbutton(groups, cursor="tcross",text="Group 3", variable=group3,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_group3.place(rely=0.3, relx=0.61, anchor='center')

			confirm_group4 = Checkbutton(groups, cursor="tcross",text="Group 4", variable=group4,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_group4.place(rely=0.3, relx=0.84, anchor='center')

			confirm_group5 = Checkbutton(groups, cursor="tcross",text="Group 5", variable=group5,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_group5.place(rely=0.45, relx=0.15, anchor='center')

			confirm_group6 = Checkbutton(groups, cursor="tcross",text="Group 6", variable=group6,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_group6.place(rely=0.45, relx=0.38, anchor='center')

			confirm_group7 = Checkbutton(groups, cursor="tcross",text="Group 7", variable=group7,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_group7.place(rely=0.45, relx=0.61, anchor='center')

			confirm_group8 = Checkbutton(groups, cursor="tcross",text="Group 8", variable=group8,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_group8.place(rely=0.45, relx=0.84, anchor='center')

			confirm_group9 = Checkbutton(groups, cursor="tcross",text="Group 9", variable=group9,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_group9.place(rely=0.6, relx=0.15, anchor='center')

			confirm_group10 = Checkbutton(groups, cursor="tcross",text="Group 10", variable=group10,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_group10.place(rely=0.6, relx=0.38, anchor='center')

			confirm_group11 = Checkbutton(groups, cursor="tcross",text="Group 11", variable=group11,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_group11.place(rely=0.6, relx=0.61, anchor='center')

			confirm_group12 = Checkbutton(groups, cursor="tcross",text="Group 12", variable=group12,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_group12.place(rely=0.6, relx=0.84, anchor='center')

			confirm_group13 = Checkbutton(groups, cursor="tcross",text="Group 13", variable=group13,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_group13.place(rely=0.75, relx=0.15, anchor='center')

			confirm_group14 = Checkbutton(groups, cursor="tcross",text="Group 14", variable=group14,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_group14.place(rely=0.75, relx=0.38, anchor='center')

			confirm_group15 = Checkbutton(groups, cursor="tcross",text="Group 15", variable=group15,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_group15.place(rely=0.75, relx=0.61, anchor='center')

			confirm_group16 = Checkbutton(groups, cursor="tcross",text="Group 16", variable=group16,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_group16.place(rely=0.75, relx=0.84, anchor='center')

			confirm_group17 = Checkbutton(groups, cursor="tcross",text="Group 17", variable=group17,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_group17.place(rely=0.9, relx=0.15, anchor='center')

			confirm_group18 = Checkbutton(groups, cursor="tcross",text="Group 18", variable=group18,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_group18.place(rely=0.9, relx=0.38, anchor='center')

			confirm_group19 = Checkbutton(groups, cursor="tcross",text="Group 19", variable=group19,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_group19.place(rely=0.9, relx=0.61, anchor='center')

			confirm_group20 = Checkbutton(groups, cursor="tcross",text="Group 20", variable=group20,bg="white",bd=2, relief="sunken", font=('Tahoma', 10,'bold'),onvalue=1, offvalue=0)
			confirm_group20.place(rely=0.9, relx=0.84, anchor='center')


		def confirmSelection2(frame):
			frame.withdraw()


		def clearTv():
			record=member_search_Tv.get_children()
			for elements in record:
				member_search_Tv.delete(elements)


		def treeviewPopulate():
			clearTv()

			conn = sqlite3.connect('Badmington_club.db')

			c = conn.cursor()

			c.execute("SELECT * From member")
			items = c.fetchall()
			conn.commit()
			conn.close()

			member_search_Tv.tag_configure("even",background="green")
			member_search_Tv.tag_configure("odd",background="red")

			count=0
			for row in items:
				if row == []:
					pass
				else:
					if count%2==0:
						member_search_Tv.insert('','end',text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7]),tags=["even"])
					else:
						member_search_Tv.insert('','end',text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7]),tags=["odd"])
					count+=1







		def returnColour(usernameReturn, passwordReturn, firstnameReturn, surnameReturn, addressReturn, postcodeReturn, ageReturn):
			usernameReturn.config(fg="black")
			passwordReturn.config(fg="black")
			firstnameReturn.config(fg="black")
			surnameReturn.config(fg="black")
			addressReturn.config(fg="black")
			postcodeReturn.config(fg="black")
			ageReturn.config(fg="black")


		def updateAccountDetails():
			response = askyesno("Are you sure?", "Do you want to update a students details")
			if response == False:
				showinfo("Info", "Update cancelled")

			else:

				update_member=Toplevel(bg="white")

				title_label =Label(update_member,text = 'Update Member' , fg ='SpringGreen3',bg='white',font=('Verdana',15,'bold'))
				title_label.place(rely=0.13,relx=0.5,anchor=CENTER)

				update_address=Button(update_member,text = 'Update Address', command = update_member_address, fg ='white', bg='black', relief= 'groove', font = ('Verdana',10,'bold'), padx =20, pady =10)
				update_address.place(rely=0.43,relx=0.5,anchor=CENTER)

				update_postcode=Button(update_member,text = 'Update Postcode', command = update_member_postcode, fg ='white', bg='black', relief= 'groove', font = ('Verdana',10,'bold'), padx =20, pady =10)
				update_postcode.place(rely=0.75,relx=0.5,anchor=CENTER)



		def update_member_address():
			conn = sqlite3.connect('Badmington_club.db')

			c = conn.cursor()

			memberUsername = simpledialog.askstring("info", "Enter the username of the member you want to see information for")
			if memberUsername != '' and len(memberUsername) <25:
				c.execute(f"SELECT * FROM member WHERE username=?", (memberUsername,))
				data = c.fetchone()
				if not data:
					messagebox.showinfo("Warning", "The username entered was not found in the database", icon='error')

				else:

					new_address = simpledialog.askstring("info", "Enter the new address of the member")

					if new_address != '' and len(new_address) < 30:

						c.execute("""UPDATE member SET address = :new_address""", {'new_address': new_address})
						messagebox.showinfo("info", "The members address is now "+new_address)

					else:

						messagebox.showinfo("Warning", "The address entered does not meet the rules", icon='error')

			else:

				messagebox.showinfo("Warning", "The username entered does not meet the rules", icon='error')

			conn.commit()
			conn.close()

			treeviewPopulate()


		def update_member_postcode():
			conn = sqlite3.connect('Badmington_club.db')

			c = conn.cursor()

			memberUsername = simpledialog.askstring("info", "Enter the username of the member you want to see information for")
			if memberUsername != '' and len(memberUsername) <25:
				c.execute(f"SELECT * FROM member WHERE username=?", (memberUsername,))
				data = c.fetchone()
				if not data:
					messagebox.showinfo("Warning", "The username entered was not found in the database", icon='error')

				else:

					new_postcode = simpledialog.askstring("info", "Enter the new postcode of the member")

					if new_postcode != '' and len(new_postcode) < 9:

						c.execute("""UPDATE member SET postcode = :new_postcode""", {'new_postcode': new_postcode})
						messagebox.showinfo("info", "The members postcode is now "+new_postcode)

					else:

						messagebox.showinfo("Warning", "The postcode entered does not meet the rules", icon='error')

			else:

				messagebox.showinfo("Warning", "The username entered does not meet the rules", icon='error')

			conn.commit()
			conn.close()

			treeviewPopulate()


		def deleteAccountDetails():
			conn = sqlite3.connect('Badmington_club.db')

			c = conn.cursor()

			response = askyesno("Are you sure?", "Do you want to delete a member")
			if response == False:
				showinfo("Info", "Deletion cancelled")

			else:

				accountUsername = simpledialog.askstring("Info", "Enter the username of the member you want to delete")

				if accountUsername !='' and len(accountUsername) <25:

					c.execute(f"SELECT * FROM member WHERE username =?", (accountUsername,))
					data = c.fetchone()
					if not data:
						messagebox.showinfo("Warning", "The username entered was not found in the database", icon='error')

					else:

						c.execute(f"DELETE FROM member WHERE username =?", (accountUsername,))
						messagebox.showinfo("info", "The member with username "+accountUsername+" has been deleted from the database")

				else:

					messagebox.showinfo("Warning", "The username entered does not meet the rules", icon='error')

			conn.commit()
			conn.close()

			treeviewPopulate()


		def searchAccountDetails():
			conn = sqlite3.connect('Badmington_club.db')

			c = conn.cursor()

			response = askyesno("Are you sure?", "Do you want to search a members details")
			if response == False:
				showinfo("Info", "Search cancelled")

			else:

				memberUsername = simpledialog.askstring("info", "Enter the username of the member you want to see information for")
				if memberUsername != '' and len(memberUsername) <25:
					c.execute(f"SELECT * FROM member WHERE username=?", (memberUsername,))
					data = c.fetchone()
					if not data:
						messagebox.showinfo("Warning", "The username entered was not found in the database", icon='error')
					else:

						messagebox.showinfo("info", "The members details are listed below" + "\n\n" + "Username: " + str(data[0]) + "\n" + "Password: " + str(data[1]) + "\n" + "Firstname: " + str(data[2]) + "\n" + "Surname: " + str(data[3]) + "\n" + "Address: " + str(data[4]) + "\n" + "Postcode: " + str(data[5]) + "\n" + "Age: " + str(data[6]) + "\n" + "Group: " + str(data[7]))

				else:

					messagebox.showinfo("Warning", "The username entered does not meet the rules", icon='error')

			conn.commit()
			conn.close()

			treeviewPopulate()


		def validate_username(value, fieldname, label):
			if (value == ''):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " Can Not Be empty")
				return False

			label.config(fg="SpringGreen3")
			return True


		def validate_start_time(value, value2, fieldname, label):
			if (int(value) <8):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " Can Not Be before 8am")
				return False
			if (int(value) >22):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " Can Not Be past 10pm")
				return False
			if (value > value2):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " Can Not Be higher than the end time")
				return False

			label.config(fg="SpringGreen3")
			return True


		def validate_end_time(value, fieldname, label):
			if (int(value) <9):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " Can Not Be empty")
				return False
			if (int(value) >23):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " Can Not Be empty")
				return False

			label.config(fg="SpringGreen3")
			return True


		def validate_courts(value, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11, value12, fieldname, label):
			if (value ==0 and value2 ==0 and value3 ==0 and value4 ==0 and value5 ==0 and value6 ==0 and value7 ==0 and value8 ==0 and value9 ==0 and value10 ==0 and value11 ==0 and value12 ==0):
				label.config(fg="red")
				messagebox.showinfo("Validation Error", "The Value For Field " + fieldname + " must have at least 1 selected")
				return False

			label.config(fg="SpringGreen3")
			return True


		def submitSession():
			conn = sqlite3.connect('CoachDetails.db')
			c = conn.cursor()

			isValid = True
			isValid = isValid and validate_username(self.coachNamesAndPasswords.get()[:4], "Username", username_label)
			isValid = isValid and validate_start_time(timeStart.get(), timeEnd.get(),"Start Time", starttime_label)
			isValid = isValid and validate_end_time(timeEnd.get(), "End Time", endtime_label)
			isValid = isValid and validate_courts(court1.get(), court2.get(),court3.get(), court4.get(), court5.get(), court6.get(), court7.get(), court8.get(), court9.get(), court10.get(), court11.get(), court12.get(),  "Court", courts_needed_label)
			isValid = isValid and validate_empty(address.get(), "Address", address_label)
			isValid = isValid and validate_empty(postcode.get(), "Postcode", postcode_label)
			isValid = isValid and validate_age(age.get(), "Age", age_label)

			if isValid:
				account_username = username.get()
				account_password = password.get()
				account_firstname = firstname.get()
				account_surname = surname.get()
				account_address = address.get()
				account_postcode = postcode.get()
				account_age = age.get()

				account_group = ageToGroup(age)

				response = askyesno("Are you sure?", "Are you sure that all information above is correct?")
				if response == False:
					showinfo("Info", "submition cancelled")

				else:

					doc = buildMemberDocument(account_username, account_password, account_firstname, account_surname, account_address, account_postcode, account_age, account_group)
					found = memberEmail("Lisburn Racquets Account Added", "You have been accepted into Lisburn Raquets Club." + "\n" + "Your details can be found in the document below." + "\n\n" + "Thanks for choosing Lisburn Racquets Club", account_username, doc, username_label)
					if found:

						c.execute("INSERT INTO member VALUES (:username, :password, :firstname, :surname, :address, :postcode, :age, :member_group)",
								  {
									  'username': account_username,
									  'password': account_password,
									  'firstname': account_firstname,
									  'surname': account_surname,
									  'address': account_address,
									  'postcode': account_postcode,
									  'age': account_age,
									  'member_group': account_group,
								  })

						username.set('')
						password.set('')
						firstname.set('')
						surname.set('')
						address.set('')
						postcode.set('')
						age.set('')

						returnColour(username_label, password_label, firstname_label, surname_label, address_label, postcode_label, age_label)


				conn.commit()
				conn.close()

				treeviewPopulate()


		def selection():
			pass

		def updateSession():
			pass

		def deleteSession():
			pass



		timeStart=StringVar()
		timeEnd=StringVar()
		eventDate=StringVar()
		technique=IntVar()



		username_label = tkinter.Label(self.coachSession, text="Username:", font=('Tahoma', 14, 'bold'), fg='black', bg='white')
		username_label.place(rely=0.36, relx=0.12, anchor='center')

		starttime_label = tkinter.Label(self.coachSession, text="Start Time:", font=('Tahoma', 14, 'bold'), fg='black', bg='white')
		starttime_label.place(rely=0.44, relx=0.12, anchor='center')

		endtime_label = tkinter.Label(self.coachSession, text="End Time:", font=('Tahoma', 14, 'bold'), fg='black', bg='white')
		endtime_label.place(rely=0.52, relx=0.12, anchor='center')

		date_label = tkinter.Label(self.coachSession, text="Session Date:", font=('Tahoma', 14, 'bold'), fg='black', bg='white')
		date_label.place(rely=0.6, relx=0.12, anchor='center')

		courts_needed_label = tkinter.Label(self.coachSession, text="Courts Required:", font=('Tahoma', 14, 'bold'), fg='black', bg='white')
		courts_needed_label.place(rely=0.68, relx=0.12, anchor='center')

		level_label = tkinter.Label(self.coachSession, text="Group Level:", font=('Tahoma', 14, 'bold'), fg='black', bg='white')
		level_label.place(rely=0.76, relx=0.12, anchor='center')

		techniques_label = tkinter.Label(self.coachSession, text="Techniques:", font=('Tahoma', 14, 'bold'), fg='black', bg='white')
		techniques_label.place(rely=0.84, relx=0.12, anchor='center')


		starttime_spinbox = Spinbox(self.coachSession, width=7,font=("Tahoma",12, 'bold'), bd=3, relief='ridge', cursor="tcross",textvariable=timeStart, values=('8.00', '8.15', '8.30', '8.45', '9.00', '9.15', '9.30', '9.45', '10.00', '10.15', '10.30', '10.45', '11.00', '11.15', '11.30', '11.45', '12.00', '12.15','12.30','12.45','13.00','13.15','13.30','13.45','14.00','14.15','14.30','14.45','15.00','15.15','15.30','15.45','16.00','16.15','16.30','16.45','17.00','17.15','17.30','17.45','18.00','18.15','18.30','18.45','19.00','19.15','19.30','19.45','20.00','20.15','20.30','20.45','21.00','21.15','21.30','21.45','22.00'))
		starttime_spinbox.place(rely=0.4425, relx=0.3, anchor='center')

		endtime_spinbox = Spinbox(self.coachSession, width=7,font=("Tahoma",12, 'bold'), bd=3, relief='ridge', cursor="tcross", textvariable=timeEnd, values=('9.00', '9.15', '9.30', '9.45', '10.00', '10.15', '10.30', '10.45', '11.00', '11.15', '11.30', '11.45', '12.00', '12.15','12.30','12.45','13.00','13.15','13.30','13.45','14.00','14.15','14.30','14.45','15.00','15.15','15.30','15.45','16.00','16.15','16.30','16.45','17.00','17.15','17.30','17.45','18.00','18.15','18.30','18.45','19.00','19.15','19.30','19.45','20.00','20.15','20.30','20.45','21.00','21.15','21.30','21.45','22.00','22.15','22.30','22.45','23.00'))
		endtime_spinbox.place(rely=0.5225, relx=0.3, anchor='center')

		date_entry = Button(self.coachSession, text='Select Date',font=("Tahoma",10, 'bold'), cursor="tcross",command=lambda : dateEntryCheck(eventDate), padx=10, bd=4, relief="ridge")
		date_entry.place(rely=0.603, relx=0.3, anchor='center')

		courts_needed_button = Button(self.coachSession, text='Select Courts',font=("Tahoma",10, 'bold'), cursor="tcross",command=lambda : courtsRequired(), padx=10, bd=4, relief="ridge")
		courts_needed_button.place(rely=0.683, relx=0.3, anchor='center')

		groups_needed_button = Button(self.coachSession, text='Select Groups',font=("Tahoma",10, 'bold'), cursor="tcross",command=lambda : groupsRequired(), padx=10, bd=4, relief="ridge")
		groups_needed_button.place(rely=0.763, relx=0.3, anchor='center')


		techniqu1_radiobutton = Radiobutton(self.coachSession, text="Net Play", variable=technique, value=1, font=("Tahoma",9, 'bold'), cursor="tcross", bg="white", bd=2, relief="ridge")
		techniqu1_radiobutton.place(rely=0.82, relx=0.25, anchor='center')

		techniqu2_radiobutton = Radiobutton(self.coachSession, text="Smash", variable=technique, value=2, font=("Tahoma",9, 'bold'), cursor="tcross", bg="white", bd=2, relief="ridge")
		techniqu2_radiobutton.place(rely=0.87, relx=0.25, anchor='center')

		techniqu3_radiobutton = Radiobutton(self.coachSession, text="Rally", variable=technique, value=3, font=("Tahoma",9, 'bold'), cursor="tcross", bg="white", bd=2, relief="ridge")
		techniqu3_radiobutton.place(rely=0.82, relx=0.37, anchor='center')

		techniqu4_radiobutton = Radiobutton(self.coachSession, text="Back Court", variable=technique, value=4, font=("Tahoma",9, 'bold'), cursor="tcross", bg="white", bd=2, relief="ridge")
		techniqu4_radiobutton.place(rely=0.87, relx=0.37, anchor='center')


		delete_button = tkinter.Button(self.coachSession, text="Delete", command=deleteSession, fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 14, 'bold'), padx=10, cursor="tcross")
		delete_button.place(rely=0.945, relx=0.08, anchor='center')

		update_button = tkinter.Button(self.coachSession, text="Update", command=updateSession, fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 14, 'bold'), padx=10, cursor="tcross")
		update_button.place(rely=0.945, relx=0.22, anchor='center')

		submit_button = tkinter.Button(self.coachSession, text="Submit", command=submitSession, fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 14, 'bold'), padx=10, cursor="tcross")
		submit_button.place(rely=0.945, relx=0.36, anchor='center')


		coachsession_search_Tv=ttk.Treeview(self.coachSession,height=4,columns=('Start Time','End Time','Date','Courts','Groups','No. People','Technique'))
		coachsession_search_Tv.place(relx=0.5,rely=0.22,anchor=CENTER)


		coachsession_search_Tv.heading("#0",text='Username')
		coachsession_search_Tv.column("#0",minwidth=0,width=160)
		coachsession_search_Tv.heading("#1",text='Start Time')
		coachsession_search_Tv.column("#1",minwidth=0,width=90)
		coachsession_search_Tv.heading("#2",text='End Time')
		coachsession_search_Tv.column("#2",minwidth=0,width=90)
		coachsession_search_Tv.heading("#3",text='Date')
		coachsession_search_Tv.column("#3",minwidth=0,width=100)
		coachsession_search_Tv.heading("#4",text='Courts')
		coachsession_search_Tv.column("#4",minwidth=0,width=100)
		coachsession_search_Tv.heading("#5",text='Groups')
		coachsession_search_Tv.column("#5",minwidth=0,width=100)
		coachsession_search_Tv.heading("#6",text='No. People')
		coachsession_search_Tv.column("#6",minwidth=0,width=80)
		coachsession_search_Tv.heading("#7",text='Technique')
		coachsession_search_Tv.column("#7",minwidth=0,width=80)

		coachsession_ysearch_scrollbar = Scrollbar(self.coachSession, orient = 'vertical', command = coachsession_search_Tv.yview, cursor="tcross")
		coachsession_ysearch_scrollbar.place(relx=0.95,rely=0.22,anchor='center',height=109)
		coachsession_search_Tv.configure(yscrollcommand=coachsession_ysearch_scrollbar.set)


		cal = Calendar(self.coachSession, font="Tahoma 19", selectmode='day', cursor="tcross", year=2021, month=5, day=29)
		cal.place(rely=0.7, relx=0.71, anchor='center')

	def coachSelection(self):
		self.coachNamesAndPasswords = StringVar()

		coach_name_choices = self.get_coach_details()
		if (len(coach_name_choices) > 0) :
			coach_selection_dropdown = OptionMenu(self.coachSession, self.coachNamesAndPasswords, *coach_name_choices)
			coach_selection_dropdown.place(rely=0.365, relx=0.305, anchor='center')

	def get_coach_details(self):
		conn = sqlite3.connect('login.db')
		c = conn.cursor()

		coach_name_list = []

		c.execute("SELECT * From account")
		items = c.fetchall()

		for row in items:
			if row == []:
				pass
			else:
				coach_name = row[0]
				coach_name_list.append(coach_name)

		return coach_name_list

		conn.commit()
		conn.close()

		'''
		def onTreeviewPopup(event):
			try:
				rowItem = member_search_Tv.treeview.identify_row(event.y)
				tvPopup.selection = member_search_Tv.treeview.set(rowItem)
		
				member_search_Tv.treeview.selection_set(rowItem)
				member_search_Tv.treeview.focus(rowItem)
				tvPopup.post(event.x_root, event.y_root)
			finally:
				tvPopup.grab_release()
		
		
		tvPopup = Menu(member, tearoff = 0)
		tvPopup.add_command(label = "Update", command = partial(updateAccountDetails, True))
		tvPopup.add_separator()
		tvPopup.add_command(label = "Delete", command = partial(deleteAccountDetails,True))
		'''