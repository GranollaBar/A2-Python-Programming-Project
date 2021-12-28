import tkinter.simpledialog
from tkinter import *
from MemberFrame.MemberDetailsScreen import MemberContent
from CoachFrame.CoachDetailsScreen import CoachContent
from CoachingSessionFrame.CoachingSessionScreen import CoachingSessionContent
from MemberBooking.MemberBookingScreen import BookingContent
from NewCompetition.NewCompetitionScreen import NewCompetitionContent
from HomeFrame.MemberHomeScreen import MemberHomeScreenContent
from LoginFrame.AS_programming_loginscreen import LoginContent


def clearContent():
    global content
    content.destroy()
    content = Frame(mainScreen, bg='white')
    content.grid(row=1, sticky="nsew")


def openMemberContent(mainScreen):
    clearContent()
    memberContent = MemberContent(mainScreen)
    memberContent.generateMemberContnt()


def openCoachContent(mainScreen):
    clearContent()
    coachContent = CoachContent(mainScreen)
    coachContent.generateCoachContnt()


def openCoachSessionContent(mainScreen):
    clearContent()
    myCoaching = CoachingSessionContent(mainScreen)
    myCoaching.coachSelection()
    myCoaching.generateCoachSessionContnt()


def openCompetitionContent(mainScreen):
    clearContent()
    resultscontent = CompetitionContent(mainScreen)
    resultscontent.memberSelection()
    resultscontent.generateResultsContnt()


def openNewCompetitionContent(mainScreen):
    clearContent()
    competitioncontent = NewCompetitionContent(mainScreen)
    competitioncontent.generateCompetitionContnt()


def openAttendCompetitionContent(mainScreen):
    clearContent()
    competitioncontent = NewCompetitionContent(mainScreen)
    competitioncontent.generateCompetitionContnt()


def openMemberBooking(mainScreen):
    clearContent()
    bookingcontent = BookingContent(mainScreen)
    bookingcontent.memberSelection()
    bookingcontent.generateBookingContnt()


def openStaticstics(mainScreen):
    clearContent()


def passLoginScreen(loginScreen: LoginContent):
    global logins
    logins = loginScreen



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


    memberHomeContent = MemberHomeScreenContent(mainScreen)
    memberHomeContent.generateMemberHomeScreenContnt(logins.finalloginname)


    add_member_button = tkinter.Button(header, text="Add Member", command=lambda : openMemberContent(mainScreen), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 12, 'bold'), padx=10, cursor="tcross")
    add_member_button.place(rely=0.5, relx=0.08, anchor='center')

    add_coach_button = tkinter.Button(header, text="Add Coach", command=lambda : openCoachContent(mainScreen), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 12, 'bold'), padx=10, cursor="tcross")
    add_coach_button.place(rely=0.5, relx=0.22, anchor='center')

    coaching_session_button = tkinter.Button(header, text="Coaching Session", command=lambda : openCoachSessionContent(mainScreen), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 12, 'bold'), padx=10, cursor="tcross")
    coaching_session_button.place(rely=0.5, relx=0.38, anchor='center')

    new_competition_button = tkinter.Button(header, text="Competition", command=lambda : openNewCompetitionContent(mainScreen), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 12, 'bold'), padx=10, cursor="tcross")
    new_competition_button.place(rely=0.5, relx=0.546, anchor='center')

    member_booking_button = tkinter.Button(header, text="Attend Competitions", command=lambda : openMemberBooking(mainScreen), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 12, 'bold'), padx=10, cursor="tcross")
    member_booking_button.place(rely=0.5, relx=0.676, anchor='center')

    # member_booking_button = tkinter.Button(header, text="Booking", command=openMemberBooking, fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 12, 'bold'), padx=10, cursor="tcross")
    # member_booking_button.place(rely=0.5, relx=0.676, anchor='center')

    # statistics_button = tkinter.Button(header, text="Stats", command=openStaticstics, fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 12, 'bold'), padx=10, cursor="tcross")
    # statistics_button.place(rely=0.5, relx=0.71, anchor='center')


    mainScreen.mainloop()
