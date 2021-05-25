import tkinter.simpledialog
from tkinter import *

def raise_frame(frame_name):
	frame_name.tkraise()

def coachingSession():
	from CustomerFrame import CustomerDetailsScreen
	CustomerDetailsScreen.content.grid(row=1, sticky="nsew")

def getHeader(attachToFrame):
	header = Frame(attachToFrame, bg='pale green')

	coaching_session_button = tkinter.Button(header, text="Coaching Session", command=coachingSession, fg='white', bg='black', bd=4, relief='ridge', font=('Segoe UI Black', 12, 'bold'), padx=10)
	coaching_session_button.place(rely=0.5, relx=0.3, anchor='center')

	add_member_button = tkinter.Button(header, text="Add Member", command=coachingSession, fg='white', bg='black', bd=4, relief='ridge', font=('Segoe UI Black', 12, 'bold'), padx=10)
	add_member_button.place(rely=0.5, relx=0.1, anchor='center')

	return header

