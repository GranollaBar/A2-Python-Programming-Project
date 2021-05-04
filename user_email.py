import smtplib
import config
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def sendEmail(subject,msg,recipientemail):
	try:
		server=smtplib.SMTP('smtp.gmail.com:587')
		server.ehlo()
		server.starttls()
		server.login(config.emailAddress,config.password)
		#message= 'Subject: {} \n\n {}'.format(subject,msg)

		server.sendmail(config.emailAddress,recipientemail,text)
		server.quit()
		print("Email sent successfully")
	except:
		print("Email not sent")



#If you want to send one email to recipient
#subject="New deal avaliable"
#msg="Get the new pizza here rn"
#sendEmail(subject,msg,config.recipientemail)

#If you want to send to various emails
#must include for loop
#emailList=["josnoble113@gmail.com","josnoble113@gmail.com","josnoble113@gmail.com"]
#for email in emailList:
#	sendEmail(subject,msg,email)


subject="New deal avaliable"
msg=MIMEMultipart()
msg['From'] = config.emailAddress
msg['To'] = config.recipientemail
msg['Subject'] = subject
body = "Hello, this is sent by python"
msg.attach(MIMEText (body,'plain'))

filename = "?.docx"
attachment = open(filename, 'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)
msg.attach(part)
text = msg.as_string()

sendEmail(subject,msg,config.recipientemail)