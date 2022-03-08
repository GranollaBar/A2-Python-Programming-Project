# Coach Main Screen

import tkinter.simpledialog
from tkinter import *
from MemberFrame.MemberDetailsScreen import MemberContent
from CoachingSessionFrame.CoachingSessionScreen import CoachingSessionContent
from NewCompetition.NewCompetitionScreen import NewCompetitionContent
from HomeFrame.CoachHomeScreen import CoachHomeScreenContent
from LoginFrame.AS_programming_loginscreen import LoginContent
from AttendCompetitionsFrame.AttendingCompetitionFrame import AttendingContent
from ReportsFrame.CoachReportsScreen import CoachReportsContent
from LogoffFrame.LogoffScreen import LogoffContent
import Pmw



# Clears the content of the current screen
def clearContent(mainScreen, finalContent):
    finalContent.destroy()
    content = Frame(mainScreen, bg='white')
    content.grid(row=1, sticky="nsew")


# Stored the username of the coach entering the system
def passLoginScreen(loginScreen: LoginContent):
    global logins
    logins = loginScreen


# Opens coach home screen
def openCoachHomeContent(mainScreen, content):
    clearContent(mainScreen, content)
    coachHomeContent = CoachHomeScreenContent(mainScreen)
    coachHomeContent.generateCoachHomeScreenContnt(logins.finalloginname, mainScreen)


# Opens member details screen
def openMemberContent(mainScreen, content):
    clearContent(mainScreen, content)
    memberContent = MemberContent(mainScreen)
    memberContent.generateMemberContnt()


# Opens coaching session screen
def openCoachSessionContent(mainScreen, content):
    clearContent(mainScreen, content)
    myCoaching = CoachingSessionContent(mainScreen)
    myCoaching.coachSelection()
    myCoaching.generateCoachSessionContnt()


# Opens competition screen
def openNewCompetitionContent(mainScreen, content):
    clearContent(mainScreen, content)
    competitioncontent = NewCompetitionContent(mainScreen)
    competitioncontent.generateCompetitionContnt()


# Opens attend competitions screen
def openAttendCompetitionContent(mainScreen, content):
    clearContent(mainScreen, content)
    attendingcontent = AttendingContent(mainScreen)
    attendingcontent.generateAttendingContnt()


# Opens coach reports screen
def openReportsContent(mainScreen, content):
    clearContent(mainScreen, content)
    coachreportcontent = CoachReportsContent(mainScreen)
    coachreportcontent.generateCoachReportsContnt(logins.finalloginname)


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


    coachHomeContent = CoachHomeScreenContent(mainScreen)
    coachHomeContent.generateCoachHomeScreenContnt(logins.finalloginname, mainScreen)


    coachhomephoto = PhotoImage(file="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Images/Home.png")
    CoachHomeButton = Button(header, cursor="tcross", image=coachhomephoto, width=30, height=30, command=lambda : openCoachHomeContent(mainScreen, content), bg="black",bd=4,relief='ridge')
    CoachHomeButton.place(rely=0.5,relx=0.05,anchor=CENTER)
    CoachHomeButton.image = coachhomephoto
    ToolTips.bind(CoachHomeButton, 'Coach Home Screen')

    add_member_button = tkinter.Button(header, text="Member", command=lambda : openMemberContent(mainScreen, content), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 12, 'bold'), padx=10, cursor="tcross")
    add_member_button.place(rely=0.5, relx=0.155, anchor='center')
    ToolTips.bind(add_member_button, 'Member Screen')

    coaching_session_button = tkinter.Button(header, text="Coaching Session", command=lambda : openCoachSessionContent(mainScreen, content), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 12, 'bold'), padx=10, cursor="tcross")
    coaching_session_button.place(rely=0.5, relx=0.315, anchor='center')
    ToolTips.bind(coaching_session_button, 'Coaching Session Screen')

    new_competition_button = tkinter.Button(header, text="Competition", command=lambda : openNewCompetitionContent(mainScreen, content), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 12, 'bold'), padx=10, cursor="tcross")
    new_competition_button.place(rely=0.5, relx=0.491, anchor='center')
    ToolTips.bind(new_competition_button, 'Competition Screen')

    attend_competition_button = tkinter.Button(header, text="Attend Competition", command=lambda : openAttendCompetitionContent(mainScreen, content), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 12, 'bold'), padx=10, cursor="tcross")
    attend_competition_button.place(rely=0.5, relx=0.678, anchor='center')
    ToolTips.bind(attend_competition_button, 'Attend Competition Screen')

    reports_button = tkinter.Button(header, text="Reports", command=lambda : openReportsContent(mainScreen, content), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 12, 'bold'), padx=10, cursor="tcross")
    reports_button.place(rely=0.5, relx=0.845, anchor='center')
    ToolTips.bind(reports_button, 'Coach Reports Screen')

    coachlogoffphoto = PhotoImage(file="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Images/Logoff.png")
    CoachLogoffButton = Button(header, cursor="tcross", image=coachlogoffphoto, width=30, height=30, command=lambda : openLogoffContent(mainScreen), bg="black",bd=4,relief='ridge')
    CoachLogoffButton.place(rely=0.5,relx=0.95,anchor=CENTER)
    CoachLogoffButton.image = coachlogoffphoto
    ToolTips.bind(CoachLogoffButton, 'Log Out')


    mainScreen.mainloop()
