import tkinter.simpledialog
from tkinter import *
from MemberBooking.MemberBookingScreen import BookingContent
from HomeFrame.MemberHomeScreen import MemberHomeScreenContent
from LoginFrame.AS_programming_loginscreen import LoginContent
import Pmw


def clearContent(mainScreen, finalContent):
    finalContent.destroy()
    content = Frame(mainScreen, bg='white')
    content.grid(row=1, sticky="nsew")


def passLoginScreen(loginScreen: LoginContent):
    global logins
    logins = loginScreen


def openMemberHomeContent(mainScreen, content):
    clearContent(mainScreen, content)
    memberHomeContent = MemberHomeScreenContent(mainScreen)
    memberHomeContent.generateMemberHomeScreenContnt(logins.finalloginname)


def openMemberBooking(mainScreen, content):
    clearContent(mainScreen, content)
    bookingcontent = BookingContent(mainScreen)
    bookingcontent.memberSelection()
    bookingcontent.generateBookingContnt()



def main():
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


    memberHomeContent = MemberHomeScreenContent(mainScreen)
    memberHomeContent.generateMemberHomeScreenContnt(logins.finalloginname)


    memberhomephoto = PhotoImage(file="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Images/Home.png")
    MemberHomeButton = Button(header, cursor="tcross", image=memberhomephoto, width=30, height=30, command=lambda : openMemberHomeContent(mainScreen, content), bg="black",bd=4,relief='ridge')
    MemberHomeButton.place(rely=0.5,relx=0.35,anchor=CENTER)
    MemberHomeButton.image = memberhomephoto
    ToolTips.bind(MemberHomeButton, 'Member Home Screen')

    member_booking_button = tkinter.Button(header, text="Member Booking", command=lambda : openMemberBooking(mainScreen, content), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 12, 'bold'), padx=10, cursor="tcross")
    member_booking_button.place(rely=0.5, relx=0.5, anchor='center')
    ToolTips.bind(member_booking_button, 'Member Booking Screen')

    memberlogoffphoto = PhotoImage(file="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Images/Logoff.png")
    MemberLogoffButton = Button(header, cursor="tcross", image=memberlogoffphoto, width=30, height=30, command=lambda : openMemberHomeContent(mainScreen, content), bg="black",bd=4,relief='ridge')
    MemberLogoffButton.place(rely=0.5,relx=0.65,anchor=CENTER)
    MemberLogoffButton.image = memberlogoffphoto
    ToolTips.bind(MemberLogoffButton, 'Log Out')


    mainScreen.mainloop()
