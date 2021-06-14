import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from tkinter import messagebox
from CoachFrame.coachWordDocument import buildCoachDocument

def coachEmail(subject, msg, recipientemail, doc, label):
	try:
		server=smtplib.SMTP('smtp.gmail.com:587')
		server.ehlo()
		server.starttls()
		server.login("josnoble113@gmail.com", "jn11jn11")
		emailText = buildEmailMsg(subject, msg, recipientemail, doc)
		server.sendmail("josnoble113@gmail.com",recipientemail,emailText)
		server.quit()
		messagebox.showinfo("Info","The details of the user were sent to "+ recipientemail)
		return True

	except:
		messagebox.showinfo('info','The email was not sent successfully to '+ recipientemail + "\n" + "Make sure the username entered exists", icon='error')
		return False

def buildEmailMsg(subject, msgBody, recipientemail, attachment):
	msg = MIMEMultipart()
	msg['From'] = "josnoble113@gmail.com"
	msg['To'] = recipientemail
	msg['Subject'] = subject
	msg.attach(MIMEText (msgBody,'plain'))

	part = MIMEBase('application','octet-stream')

	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition',"attachment; filename=coach_Account_Details.docx")
	msg.attach(part)
	return msg.as_string()

