# Manager Main Screen

import tkinter.simpledialog
from tkinter import *
from CoachFrame.CoachDetailsScreen import CoachContent
from HomeFrame.ManagerHomeScreen import ManagerHomeScreenContent
from ReportsFrame.ManagerReportsScreen import ManagerReportsContent
from LoginFrame.AS_programming_loginscreen import LoginContent
from LogoffFrame.LogoffScreen import LogoffContent
import Pmw



# Clears the content of the current screen
def clearContent(mainScreen, finalContent):
    finalContent.destroy()
    content = Frame(mainScreen, bg='white')
    content.grid(row=1, sticky="nsew")


# Stored the username of the manager entering the system
def passLoginScreen(loginScreen: LoginContent):
    global logins
    logins = loginScreen


# Opens manager home screen
def openManagerHomeContent(mainScreen, content):
    clearContent(mainScreen, content)
    managerHomeContent = ManagerHomeScreenContent(mainScreen)
    managerHomeContent.generateManagerHomeScreenContnt(logins.finalloginname)


# Opens coach details screen
def openCoachDetails(mainScreen, content):
    clearContent(mainScreen, content)
    coachcontent = CoachContent(mainScreen)
    coachcontent.generateCoachContnt()


# Opens manager reports screen
def openManagerReports(mainScreen, content):
    clearContent(mainScreen, content)
    managerreports = ManagerReportsContent(mainScreen)
    managerreports.generateManagerReportsContnt(logins.finalloginname)


# Log off system
def openLogoffContent(mainScreen):
    logoffcontent = LogoffContent()
    logoffcontent.generateLogoffContnt(mainScreen)



# Location of main screen and all associated windows
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


    managerHomeContent = ManagerHomeScreenContent(mainScreen)
    managerHomeContent.generateManagerHomeScreenContnt(logins.finalloginname)


    managerhomephoto = PhotoImage(file="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Images/Home.png")
    ManagerHomeButton = Button(header, cursor="tcross", image=managerhomephoto, width=30, height=30, command=lambda : openManagerHomeContent(mainScreen, content), bg="black",bd=4,relief='ridge')
    ManagerHomeButton.place(rely=0.5,relx=0.264,anchor=CENTER)
    ManagerHomeButton.image = managerhomephoto
    ToolTips.bind(ManagerHomeButton, 'Manager Home Screen')

    CoachDetailsButton = tkinter.Button(header, text="Coach Details", command=lambda : openCoachDetails(mainScreen, content), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 12, 'bold'), padx=10, cursor="tcross")
    CoachDetailsButton.place(rely=0.5, relx=0.4, anchor='center')
    ToolTips.bind(CoachDetailsButton, 'Coach Details Screen')

    ManagerReportsButton = tkinter.Button(header, text="Manager Reports", command=lambda : openManagerReports(mainScreen, content), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 12, 'bold'), padx=10, cursor="tcross")
    ManagerReportsButton.place(rely=0.5, relx=0.6, anchor='center')
    ToolTips.bind(ManagerReportsButton, 'Manager Reports Screen')

    managerlogoffphoto = PhotoImage(file="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Images/Logoff.png")
    ManagerLogoffButton = Button(header, cursor="tcross", image=managerlogoffphoto, width=30, height=30, command=lambda : openLogoffContent(mainScreen), bg="black",bd=4,relief='ridge')
    ManagerLogoffButton.place(rely=0.5,relx=0.75,anchor=CENTER)
    ManagerLogoffButton.image = managerlogoffphoto
    ToolTips.bind(ManagerLogoffButton, 'Log Out')


    mainScreen.mainloop()
