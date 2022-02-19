from tkinter import messagebox
from tkinter.messagebox import askyesno


class LogoffContent:

	def __init__(self, mainScreen):
		self.logoff = mainScreen


	def generateLogoffContnt(self, main):
		response = askyesno("Question", "Are you sure you want to logout?", icon='question')
		if response == False:
			messagebox.showinfo("Info", "Logout cancelled", icon='info')

		else:
			messagebox.showinfo('Info', 'Logout Successful', icon='info')

			main.destroy()

			from LoginFrame import LoginMainScreen