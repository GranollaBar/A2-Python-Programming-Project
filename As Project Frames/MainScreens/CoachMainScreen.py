import tkinter.simpledialog
from tkinter import *
from MemberFrame.MemberDetailsScreen import MemberContent
from CoachFrame.CoachDetailsScreen import CoachContent
from CoachingSessionFrame.CoachingSessionScreen import CoachingSessionContent
from MemberBooking.MemberBookingScreen import BookingContent
from NewCompetition.NewCompetitionScreen import NewCompetitionContent
from HomeFrame.MemberHomeScreen import MemberHomeScreenContent
from HomeFrame.CoachHomeScreen import CoachHomeScreenContent
from LoginFrame.AS_programming_loginscreen import LoginContent
from AttendCompetitionsFrame.AttendingCompetitionFrame import AttendingSinglesContent


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


def openMemberContent(mainScreen, content):
    clearContent(mainScreen, content)
    memberContent = MemberContent(mainScreen)
    memberContent.generateMemberContnt()


def openCoachContent(mainScreen, content):
    clearContent(mainScreen, content)
    coachContent = CoachContent(mainScreen)
    coachContent.generateCoachContnt()


def openCoachSessionContent(mainScreen, content):
    clearContent(mainScreen, content)
    myCoaching = CoachingSessionContent(mainScreen)
    myCoaching.coachSelection()
    myCoaching.generateCoachSessionContnt()


def openNewCompetitionContent(mainScreen, content):
    clearContent(mainScreen, content)
    competitioncontent = NewCompetitionContent(mainScreen)
    competitioncontent.generateCompetitionContnt()


def openAttendSinglesCompetitionContent(mainScreen, content):
    clearContent(mainScreen, content)
    attendingsinglescontent = AttendingSinglesContent(mainScreen)
    attendingsinglescontent.generateAttendingSinglesContnt()


def openMemberBooking(mainScreen, content):
    clearContent(mainScreen, content)
    bookingcontent = BookingContent(mainScreen)
    bookingcontent.memberSelection()
    bookingcontent.generateBookingContnt()


def openStaticstics(mainScreen, content):
    clearContent(mainScreen, content)




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


    coachHomeContent = CoachHomeScreenContent(mainScreen)
    coachHomeContent.generateCoachHomeScreenContnt(logins.finalloginname)


    coachhomephoto = PhotoImage(file="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Images/Home.png")
    CoachHomeButton = Button(header, cursor="tcross", image=coachhomephoto, width=30, height=30, command=lambda : openMemberHomeContent(mainScreen, content), bg="black",bd=4,relief='ridge')
    CoachHomeButton.place(rely=0.5,relx=0.05,anchor=CENTER)
    CoachHomeButton.image = coachhomephoto

    coachlogoffphoto = PhotoImage(file="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Images/Logoff.png")
    CoachLogoffButton = Button(header, cursor="tcross", image=coachlogoffphoto, width=30, height=30, command=lambda : openMemberHomeContent(mainScreen, content), bg="black",bd=4,relief='ridge')
    CoachLogoffButton.place(rely=0.5,relx=0.95,anchor=CENTER)
    CoachLogoffButton.image = coachlogoffphoto

    add_member_button = tkinter.Button(header, text="Member", command=lambda : openMemberContent(mainScreen, content), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 12, 'bold'), padx=10, cursor="tcross")
    add_member_button.place(rely=0.5, relx=0.155, anchor='center')

    # add_coach_button = tkinter.Button(header, text="Add Coach", command=lambda : openCoachContent(mainScreen, content), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 12, 'bold'), padx=10, cursor="tcross")
    # add_coach_button.place(rely=0.5, relx=0.22, anchor='center')

    coaching_session_button = tkinter.Button(header, text="Coaching Session", command=lambda : openCoachSessionContent(mainScreen, content), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 12, 'bold'), padx=10, cursor="tcross")
    coaching_session_button.place(rely=0.5, relx=0.315, anchor='center')

    new_competition_button = tkinter.Button(header, text="Competition", command=lambda : openNewCompetitionContent(mainScreen, content), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 12, 'bold'), padx=10, cursor="tcross")
    new_competition_button.place(rely=0.5, relx=0.491, anchor='center')

    attend_competition_button = tkinter.Button(header, text="Attend Competition", command=lambda : openAttendSinglesCompetitionContent(mainScreen, content), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 12, 'bold'), padx=10, cursor="tcross")
    attend_competition_button.place(rely=0.5, relx=0.678, anchor='center')

    reports_button = tkinter.Button(header, text="Reports", command=lambda : openNewCompetitionContent(mainScreen, content), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 12, 'bold'), padx=10, cursor="tcross")
    reports_button.place(rely=0.5, relx=0.845, anchor='center')

    # member_booking_button = tkinter.Button(header, text="Booking", command=openMemberBooking, fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 12, 'bold'), padx=10, cursor="tcross")
    # member_booking_button.place(rely=0.5, relx=0.676, anchor='center')


    mainScreen.mainloop()
