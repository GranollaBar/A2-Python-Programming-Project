import docx
import os
from docx.shared import Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

def buildCoachDocument(username, password, firstname, surname, gender, DOB, postcode, availability):
    doc = docx.Document()
    heading = doc.add_heading('Lisburn Racquets Coach Details',0)
    heading.alignment = WD_ALIGN_PARAGRAPH.CENTER
    parag=doc.add_paragraph("")
    parag.add_run("You have successfully created your coach account for Lisburn Racquets Club").bold=True
    parag.add_run("\n\n" + "Your details are listed below:").bold=True
    parag.add_run("\n\n" + "Username: " + username)
    parag.add_run("\n" + "Password: " + password)
    parag.add_run("\n" + "Firstname: " + firstname)
    parag.add_run("\n" + "Surname: " + surname)
    parag.add_run("\n" + "Gender: " + gender)
    parag.add_run("\n" + "Date Of Birth: " + DOB)
    parag.add_run("\n" + "Postcode: " + postcode)
    parag.add_run("\n" + "availability: " + availability)
    parag.add_run("\n\n" + "Thanks for choosing Lisburn Racquets Club").bold=True
    doc.add_picture('rsz_lisburnraquetsclub.png',width=Inches(3))

    filename = "coach_Account_Details.docx"
    doc.save(filename)
    return open(filename,'rb')
