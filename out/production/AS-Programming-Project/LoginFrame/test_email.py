import smtplib
from tkinter import messagebox

def sendEmail(subject, msg, recipientemail):
	try:
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.ehlo()
		server.starttls()
		server.login("josnoble113@gmail.com", "jn11jn11")
		message = 'Subject: {} \n\n {}'.format(subject, msg)
		server.sendmail("josnoble113@gmail.com", recipientemail, message)
		server.quit()
		messagebox.showinfo("Info","The verification code to change passwords was sent to "+ recipientemail)
		return True

	except:

		messagebox.showinfo('info','The email was not sent successfully to '+ recipientemail + "\n" + "Make sure the username entered exists", icon='error')
		return False
