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
from tkinter import PhotoImage
import tkinter as tk

class StatisticsContent:

	def __init__(self, mainScreen):
		self.booking = mainScreen
		self.conn = sqlite3.connect('BadmintonClub.db')
		self.c = self.conn.cursor()


	# self.c.execute("""CREATE TABLE booking (
	# 			username text,
	# 			username2 text,
	# 			date text,
	# 			time text,
	# 			court text,
	# 			bookingID integer
	# 			)""")


	def generateBookingContnt(self):

		pass