import boto3
from tkinter import messagebox
from tkinter import *
import tkinter

def MemberJoingSMS(username, password, firstname, surname, address, postcode, age, group):
    client= boto3.client('sns','eu-west-1')
    client.publish(PhoneNumber='+447758607064',Message='Thank you for choosing Lisburn Racquets Club' + '\n\n' + 'Details:' + '\n' + 'Username: ' + username + '\n' + 'Password: ' + password + '\n' + 'Fullname: ' + firstname + ' ' + surname + '\n' + 'Address: ' + address + '\n' + 'Postcode: ' + postcode + '\n' + 'Age: ' + age + '\n' + 'Group: ' + group)

def ChangingPassword(verificationCode, frame):
    try:
        client= boto3.client('sns','eu-west-1')
        client.publish(PhoneNumber='+447758607064',Message="Your verification code for Lisburn Racquets Club is: " + verificationCode)
        return True

    except:
        messagebox.showinfo('info','The SMS was not sent successfully.', icon='error')
        frame.destroy()
        return False