import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from tkinter import messagebox

def Email(subject, msg, recipientemail, label, value):
	try:
		server=smtplib.SMTP('smtp.gmail.com:587')
		server.ehlo()
		server.starttls()
		server.login("josnoble113@gmail.com", "jn11jn11")
		emailText = buildEmailMsg(subject, msg, recipientemail, value)
		server.sendmail("josnoble113@gmail.com",recipientemail,emailText)
		server.quit()
		messagebox.showinfo("Info","The details of the user were sent to "+ recipientemail)
		return True

	except:
		label.config(fg='red')
		messagebox.showinfo('info','The email was not sent successfully to '+ recipientemail + "\n" + "Make sure the username entered exists", icon='error')
		return False

def buildEmailMsg(subject, msgBody, recipientemail, type):
	msg = MIMEMultipart()
	msg['From'] = "josnoble113@gmail.com"
	msg['To'] = recipientemail
	msg['Subject'] = subject
	msg.attach(MIMEText (msgBody,'plain'))

	filename = 'C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Images/' + type + 'blob.png'
	attachment = open(filename, 'rb')

	part = MIMEBase('application','octet-stream')

	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition',"attachment; filename=" + filename)
	msg.attach(part)
	return msg.as_string()

