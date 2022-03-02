import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from tkinter import messagebox

#Sends an email to users
def Email(subject, msg, recipientemail, doc, label):
	try:
		server=smtplib.SMTP('smtp.gmail.com:587')
		server.ehlo()
		server.starttls()
		server.login("gamblingwolf113@gmail.com", "WPKa4VAqpuHxdQyt")
		emailText = buildEmailMsg(subject, msg, recipientemail, doc)
		server.sendmail("gamblingwolf113@gmail.com",recipientemail,emailText)
		server.quit()
		messagebox.showinfo("Info","The details of the user were sent to "+ recipientemail)
		return True

	except:
		label.config(fg='red')
		messagebox.showinfo('info','The email was not sent successfully to '+ recipientemail + "\n" + "Make sure the username entered exists", icon='error')
		return False

# Builds the entire message to the user
def buildEmailMsg(subject, msgBody, recipientemail, attachment):
	msg = MIMEMultipart()
	msg['From'] = "gamblingwolf113@gmail.com"
	msg['To'] = recipientemail
	msg['Subject'] = subject
	msg.attach(MIMEText (msgBody,'plain'))

	part = MIMEBase('application','octet-stream')

	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition',"attachment; filename=Coach_Account_Details.docx")
	msg.attach(part)
	return msg.as_string()

