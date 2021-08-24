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


class BookingContent:

	def __init__(self, mainScreen):
		self.booking = mainScreen
		self.conn = sqlite3.connect('BadmintonClub.db')
		self.c = self.conn.cursor()


		# self.c.execute("""CREATE TABLE competition (
		# 			username text,
		# 			username2 text,
		# 			date text,
		# 			time text,
		# 			court text
		# 			)""")


	def generateBookingContnt(self):

		background_entry_canvas = Canvas(self.booking,width=800, height=300, bg = "white")
		background_entry_canvas.place(rely=0.35,relx=0.5,anchor=CENTER)

		background_entry_image = PhotoImage(file ="rectangleHeader2_800x300.png")

		background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
		background_entry_canvas.background_entry_image = background_entry_image
