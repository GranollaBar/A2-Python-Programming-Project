import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import messagebox

# Sends an email to the user seeking to change their password
def ChangePassword(subject, msg, recipientemail):
	try:
		server=smtplib.SMTP('smtp.gmail.com:587')
		server.ehlo()
		server.starttls()
		server.login("gamblingwolf113@gmail.com", "WPKa4VAqpuHxdQyt")
		print('hello')
		emailText = buildEmailMsg(subject, msg, recipientemail)
		server.sendmail("gamblingwolf113@gmail.com",recipientemail,emailText)
		server.quit()
		return True

	except:
		messagebox.showinfo('info','The email was not sent successfully to '+ recipientemail + "\n" + "Make sure the username entered exists", icon='error')
		return False

# Builds the entire message for sending to the user
def buildEmailMsg(subject, msgBody, recipientemail):	
	msg = MIMEMultipart()
	msg['From'] = "gamblingwolf113@gmail.com"
	msg['To'] = recipientemail
	msg['Subject'] = subject
	msg.attach(MIMEText(msgBody,'plain'))
	return msg.as_string()