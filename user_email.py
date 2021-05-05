import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from tkinter import messagebox, END
import random


def sendEmail(subject,msg,recipientemail,forgot_username,forgot_password):
	try:
		server=smtplib.SMTP('smtp.gmail.com:587')
		server.ehlo()
		server.starttls()
		server.login(forgot_username,forgot_password)
		#message= 'Subject: {} \n\n {}'.format(subject,msg)

		server.sendmail(forgot_username,recipientemail)
		server.quit()
		messagebox.showinfo('info','The email was sent successfully')
	except:
		messagebox.showinfo('info','The email was not sent successfully', icon='error')



#If you want to send one email to recipient
#subject="New deal avaliable"
#msg="Get the new pizza here rn"
#sendEmail(subject,msg,config.recipientemail)

#If you want to send to various emails
#must include for loop
#emailList=["josnoble113@gmail.com","josnoble113@gmail.com","josnoble113@gmail.com"]
#for email in emailList:
#	sendEmail(subject,msg,email)


subject="Verification Code For Lisburn Raquets Club"
msg=MIMEMultipart()
msg['From'] = "twoods@lisburnracquets.co.uk"
msg['To'] = "monkey@gmail.com"
msg['Subject'] = subject
verification_code = random.randint(100000,999999)
body = "The verification code is " , "\n\n" , verification_code , "\n\n", "Thank you for choosing Lisburn raquets club"
msg.attach(MIMEText (body,'plain'))

#sendEmail(subject,msg,recipientemail)