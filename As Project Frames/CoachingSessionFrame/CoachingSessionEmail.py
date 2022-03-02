import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import messagebox

# Sends an email to all members participating within the selected group of the coach session
def SessionEmail(subject, msg, recipientemail, label):
	try:
		server=smtplib.SMTP('smtp.gmail.com:587')
		server.ehlo()
		server.starttls()
		server.login("gamblingwolf113@gmail.com", "WPKa4VAqpuHxdQyt")
		emailText = buildEmailMsg(subject, msg, recipientemail)
		server.sendmail("josnoble113@gmail.com",recipientemail,emailText)
		server.quit()
		return True

	except:
		label.config(fg='red')
		messagebox.showinfo('info','The email was not sent successfully to '+ recipientemail + "\n" + "Make sure the username entered exists", icon='error')
		return False

# Builds the entire message to the member
def buildEmailMsg(subject, msgBody, recipientemail):	
	msg = MIMEMultipart()
	msg['From'] = "gamblingwolf113@gmail.com"
	msg['To'] = recipientemail
	msg['Subject'] = subject
	msg.attach(MIMEText(msgBody,'plain'))
	return msg.as_string()