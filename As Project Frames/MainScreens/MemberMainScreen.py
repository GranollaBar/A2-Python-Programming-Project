# Member Main Screen

import tkinter.simpledialog
from tkinter import *
from MemberBooking.MemberBookingScreen import BookingContent
from HomeFrame.MemberHomeScreen import MemberHomeScreenContent
from AS_programming_loginscreen import LoginContent
from LogoffFrame.LogoffScreen import LogoffContent
import Pmw



# Clears the content of the current screen
def clearContent(mainScreen, finalContent):
    finalContent.destroy()
    content = Frame(mainScreen, bg='white')
    content.grid(row=1, sticky="nsew")


# Stored the username of the member entering the system
def passLoginScreen(loginScreen: LoginContent):
    global logins
    logins = loginScreen


# Opens member home screen
def openMemberHomeContent(mainScreen, content, filepath):
    clearContent(mainScreen, content)
    memberHomeContent = MemberHomeScreenContent(mainScreen, filepath)
    memberHomeContent.generateMemberHomeScreenContnt(logins.finalloginname)


# Opens member booking screen
def openMemberBooking(mainScreen, content, filepath):
    clearContent(mainScreen, content)
    bookingcontent = BookingContent(mainScreen, filepath)
    bookingcontent.memberSelection()
    bookingcontent.generateBookingContnt()


# Log off system
def openLogoffContent(mainScreen):
    logoffcontent = LogoffContent()
    logoffcontent.generateLogoffContnt(mainScreen)



# Location of main screen and all associated windows
def main(filepath):
    mainScreen = Tk()
    mainScreen.title('Lisburn Raquets Club')
    mainScreen.geometry('985x650')
    mainScreen.resizable(0,0)

    header = Frame(mainScreen, bg='pale green')
    content = Frame(mainScreen, bg='white')

    mainScreen.columnconfigure(0, weight=1)
    mainScreen.rowconfigure(0, weight=1)
    mainScreen.rowconfigure(1, weight=9)

    header.grid(row=0, sticky="nsew")
    content.grid(row=1, sticky="nsew")


    ToolTips = Pmw.Balloon()


    memberHomeContent = MemberHomeScreenContent(mainScreen, filepath)
    memberHomeContent.generateMemberHomeScreenContnt(logins.finalloginname)


    memberhomephoto = PhotoImage(file="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Images/Home.png")
    MemberHomeButton = Button(header, cursor="tcross", image=memberhomephoto, width=30, height=30, command=lambda : openMemberHomeContent(mainScreen, content, filepath), bg="black",bd=4,relief='ridge')
    MemberHomeButton.place(rely=0.5,relx=0.35,anchor=CENTER)
    MemberHomeButton.image = memberhomephoto
    ToolTips.bind(MemberHomeButton, 'Member Home Screen')

    member_booking_button = tkinter.Button(header, text="Member Booking", command=lambda : openMemberBooking(mainScreen, content, filepath), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 12, 'bold'), padx=10, cursor="tcross")
    member_booking_button.place(rely=0.5, relx=0.5, anchor='center')
    ToolTips.bind(member_booking_button, 'Member Booking Screen')

    memberlogoffphoto = PhotoImage(file="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Images/Logoff.png")
    MemberLogoffButton = Button(header, cursor="tcross", image=memberlogoffphoto, width=30, height=30, command=lambda : openLogoffContent(mainScreen), bg="black",bd=4,relief='ridge')
    MemberLogoffButton.place(rely=0.5,relx=0.65,anchor=CENTER)
    MemberLogoffButton.image = memberlogoffphoto
    ToolTips.bind(MemberLogoffButton, 'Log Out')


    mainScreen.mainloop()
