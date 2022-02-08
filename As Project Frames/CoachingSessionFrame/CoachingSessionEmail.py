import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import messagebox

def SessionEmail(subject, msg, recipientemail, label):
	try:
		server=smtplib.SMTP('smtp.gmail.com:587')
		server.ehlo()
		server.starttls()
		server.login("josnoble113@gmail.com", "jn11jn11")
		emailText = buildEmailMsg(subject, msg, recipientemail)
		server.sendmail("josnoble113@gmail.com",recipientemail,emailText)
		server.quit()
		return True

	except:
		label.config(fg='red')
		messagebox.showinfo('info','The email was not sent successfully to '+ recipientemail + "\n" + "Make sure the username entered exists", icon='error')
		return False

def buildEmailMsg(subject, msgBody, recipientemail):	
	msg = MIMEMultipart()
	msg['From'] = "josnoble113@gmail.com"
	msg['To'] = recipientemail
	msg['Subject'] = subject
	msg.attach(MIMEText(msgBody,'plain'))
	return msg.as_string()