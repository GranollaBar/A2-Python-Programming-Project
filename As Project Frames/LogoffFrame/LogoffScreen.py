# Log Off Screen

from tkinter import messagebox
from tkinter.messagebox import askyesno



# Log Off Class
class LogoffContent:


	# Generate log off content
	def generateLogoffContnt(self, main):
		response = askyesno("Question", "Are you sure you want to logout?", icon='question')
		if response == False:
			messagebox.showinfo("Info", "Logout cancelled", icon='info')

		else:
			messagebox.showinfo('Info', 'Logout Successful', icon='info')

			main.destroy()

			import LoginMainScreen