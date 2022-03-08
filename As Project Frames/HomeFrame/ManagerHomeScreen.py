# Manager Home Screen

import tkinter.simpledialog
import sqlite3
from tkinter import *
from datetime import datetime
import datetime
from PIL import Image, ImageTk
import webbrowser



# Manager Home Class
class ManagerHomeScreenContent:

	i = 0

	# Initiates main screen window
	def __init__(self, mainScreen):
		self.ManagerHome = mainScreen
		self.conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
		self.c = self.conn.cursor()


	# Generate manager home content
	def generateManagerHomeScreenContnt(self, FinalUsername):

		# Showcases the Lisburn Racquets Club badminton, tennis and squash facilities with an image slider
		def ImageSlider():
			if self.i >= (len(images)-1):
				self.i = 0
				slide_image.config(image=images[self.i])
			else:
				self.i = self.i + 1
				slide_image.configure(image=images[self.i])
			show = slide_image.after(3000, ImageSlider)


		# Will calculate how many members and coaches have been added to the system
		def Memberandcoachcounter():
			conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
			c = conn.cursor()

			membercounter = 0
			coachcounter = 0

			c.execute('SELECT * FROM member')
			members = c.fetchall()

			if len(members) != 0:
				for finalmembers in members:
					membercounter += 1
			else:
				pass

			c.execute('SELECT * FROM coach')
			coaches = c.fetchall()

			if len(coaches) != 0:
				for finalcoaches in coaches:
					coachcounter += 1
			else:
				pass

			no_members.config(text=membercounter)
			no_coaches.config(text=coachcounter)


		# Will calculate the current week day for the coach
		def GetCurrentWeeday():
			Weekday = datetime.datetime.today().strftime('%A')
			weekday.config(text=Weekday)


		# Opens a link to the specific google maps location of Lisburn Racquets Club
		def GoogleMapsLocation():
			webbrowser.open("https://www.google.com/maps/place/Lisburn+Racquets+Club/@54.5173416,-6.0428075,15z/data=!4m5!3m4!1s0x4861044f4e4d451b:0x9a328c6b732d12eb!8m2!3d54.5173416!4d-6.0340528")



		# Tkinter labels, entry boxes, buttons, tree views, etc.
		title_label = tkinter.Label(self.ManagerHome, text="Main Menu: Manager", font=('serif', 18, 'bold','underline'), fg='black', bg='white', bd=4, relief='groove', padx=10, pady=4)
		title_label.place(rely=0.16, relx=0.5, anchor='center')

		weekday_label = tkinter.Label(self.ManagerHome, text="Current Weekday:", font=('serif', 14, 'bold'), fg='black', bg='white')
		weekday_label.place(rely=0.25, relx=0.425, anchor='center')
		weekday = Label(self.ManagerHome, font=('serif', 14, 'bold'), fg='black', bg='white', bd=3, relief='sunken', padx=3, pady=1)
		weekday.place(rely=0.253, relx=0.575, anchor='center')

		no_members_label = tkinter.Label(self.ManagerHome, text="No. Members:", font=('serif', 14, 'bold'), fg='black', bg='white')
		no_members_label.place(rely=0.32, relx=0.425, anchor='center')
		no_members = Label(self.ManagerHome, font=('serif', 14, 'bold'), fg='black', bg='white', bd=3, relief='sunken', padx=3, pady=1)
		no_members.place(rely=0.323, relx=0.575, anchor='center')

		no_coaches_label = tkinter.Label(self.ManagerHome, text="No. Coaches:", font=('serif', 14, 'bold'), fg='black', bg='white')
		no_coaches_label.place(rely=0.39, relx=0.425, anchor='center')
		no_coaches = Label(self.ManagerHome, font=('serif', 14, 'bold'), fg='black', bg='white', bd=3, relief='sunken', padx=3, pady=1)
		no_coaches.place(rely=0.393, relx=0.575, anchor='center')

		googlemapsphoto = PhotoImage(file="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Images/Googlemaps.png")

		GoogleMapsButton = Button(self.ManagerHome, cursor="tcross", image=googlemapsphoto, width=507, height=315, command=GoogleMapsLocation, bg="white", activebackground="grey")
		GoogleMapsButton.place(rely=0.73,relx=0.67,anchor=CENTER)
		GoogleMapsButton.image = googlemapsphoto

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

		self.i = 0
		slide_image = Label(self.ManagerHome, image=images[self.i], bd=10, relief='ridge', bg='green')
		slide_image.place(rely=0.732, relx=0.19, anchor='center')




		ImageSlider()
		GetCurrentWeeday()
		Memberandcoachcounter()