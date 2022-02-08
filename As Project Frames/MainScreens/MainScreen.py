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


#testing 123


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


def openCompetitionContent(mainScreen, content):
    clearContent(mainScreen, content)
    resultscontent = CompetitionContent(mainScreen)
    resultscontent.memberSelection()
    resultscontent.generateResultsContnt()


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


    # memberHomeContent = MemberHomeScreenContent(mainScreen)
    # memberHomeContent.generateMemberHomeScreenContnt(logins.finalloginname)

    coachHomeContent = CoachHomeScreenContent(mainScreen)
    coachHomeContent.generateCoachHomeScreenContnt(logins.finalloginname)


    add_member_button = tkinter.Button(header, text="Add Member", command=lambda : openMemberContent(mainScreen, content), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 12, 'bold'), padx=10, cursor="tcross")
    add_member_button.place(rely=0.5, relx=0.08, anchor='center')

    add_coach_button = tkinter.Button(header, text="Add Coach", command=lambda : openCoachContent(mainScreen, content), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 12, 'bold'), padx=10, cursor="tcross")
    add_coach_button.place(rely=0.5, relx=0.22, anchor='center')

    coaching_session_button = tkinter.Button(header, text="Coaching Session", command=lambda : openCoachSessionContent(mainScreen, content), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 12, 'bold'), padx=10, cursor="tcross")
    coaching_session_button.place(rely=0.5, relx=0.38, anchor='center')

    new_competition_button = tkinter.Button(header, text="Competition", command=lambda : openNewCompetitionContent(mainScreen, content), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 12, 'bold'), padx=10, cursor="tcross")
    new_competition_button.place(rely=0.5, relx=0.546, anchor='center')

    attend_competition_button = tkinter.Button(header, text="Attend Competitions", command=lambda : openAttendSinglesCompetitionContent(mainScreen, content), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 12, 'bold'), padx=10, cursor="tcross")
    attend_competition_button.place(rely=0.5, relx=0.676, anchor='center')

    memberhomephoto = PhotoImage(file="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Images/Home.png")
    MemberHomeButton = Button(header, cursor="tcross", image=memberhomephoto, width=30, height=30, command=lambda : openMemberHomeContent(mainScreen, content), bg="black",bd=4,relief='ridge')
    MemberHomeButton.place(rely=0.5,relx=0.8,anchor=CENTER)
    MemberHomeButton.image = memberhomephoto

    # member_booking_button = tkinter.Button(header, text="Booking", command=openMemberBooking, fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 12, 'bold'), padx=10, cursor="tcross")
    # member_booking_button.place(rely=0.5, relx=0.676, anchor='center')

    # statistics_button = tkinter.Button(header, text="Stats", command=openStaticstics, fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 12, 'bold'), padx=10, cursor="tcross")
    # statistics_button.place(rely=0.5, relx=0.71, anchor='center')


    mainScreen.mainloop()
