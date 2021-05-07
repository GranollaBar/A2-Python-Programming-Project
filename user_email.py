import smtplib
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from tkinter import messagebox, END
import random

'''
def sendEmail(subject, userMsg, recipientEmail):
	try:
		server=smtplib.SMTP('smtp.gmail.com', 587)
		server.ehlo()
		server.starttls()
		server.login('josnoble113@gmail.com', 'Jn11jn11')
		message= 'Subject: {} \n\n {}'.format(subject,msg)

		server.sendmail("josnoble113@gmail.com", recipientEmail, message)
		server.quit()
		messagebox.showinfo('info','The email was sent successfully')
	except:
		e = sys.exc_info()[0]
		messagebox.showinfo('info','The email was not sent successfully ' + str(e), icon='error')
'''


#If you want to send one email to recipient
#subject="New deal avaliable"
#msg="Get the new pizza here rn"
#sendEmail(subject,msg,config.recipientemail)

#If you want to send to various emails
#must include for loop
#emailList=["josnoble113@gmail.com","josnoble113@gmail.com","josnoble113@gmail.com"]
#for email in emailList:
#	sendEmail(subject,msg,email)




#sendEmail(subject,msg,recipientemail)

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
		messagebox.showinfo('info','The email was not sent successfully to '+ recipientemail, icon='error')
		messagebox.showinfo('info','Make sure the username entered exists', icon='error')

		return False
