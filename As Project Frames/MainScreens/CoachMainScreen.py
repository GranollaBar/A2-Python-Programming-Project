import tkinter.simpledialog
from tkinter import *
from MemberFrame.MemberDetailsScreen import MemberContent
from CoachFrame.CoachDetailsScreen import CoachContent
from CoachingSessionFrame.CoachingSessionScreen import CoachingSessionContent
from CompetitionFrame.ResultsScreen import ResultsContent
from MemberBooking.MemberBookingScreen import BookingContent
from BookingContent



def clearContent():
    global content
    content.destroy()
    content = Frame(mainScreen, bg='white')
    content.grid(row=1, sticky="nsew")


def openCoachContent():
    clearContent()
    coachContent = CoachContent(mainScreen)
    coachContent.generateCoachContnt()


def openMemberContent():
    clearContent()
    memberContent = MemberContent(mainScreen)
    memberContent.generateMemberContnt()


def openCoachSessionContent():
    clearContent()
    myCoaching = CoachingSessionContent(mainScreen)
    myCoaching.coachSelection()
    myCoaching.generateCoachSessionContnt()


def openCompetitionContent():
    clearContent()
    resultscontent = ResultsContent(mainScreen)
    resultscontent.memberSelection()
    resultscontent.generateResultsContnt()


def openMemberBooking():
    clearContent()
    bookingcontent = BookingContent(mainScreen)
    bookingcontent.memberSelection()
    bookingcontent.generateBookingContnt()


def openStaticstics():
    clearContent()


mainScreen = Tk()
mainScreen.geometry('985x650')
mainScreen.resizable(0,0)

header = Frame(mainScreen, bg='pale green')
content = Frame(mainScreen, bg='white')

mainScreen.columnconfigure(0, weight=1)
mainScreen.rowconfigure(0, weight=1)
mainScreen.rowconfigure(1, weight=9)

header.grid(row=0, sticky="nsew")
content.grid(row=1, sticky="nsew")


memberContent = MemberContent(mainScreen)
memberContent.generateMemberContnt()


add_member_button = tkinter.Button(header, text="Add Member", command=openMemberContent, fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 12, 'bold'), padx=10, cursor="tcross")
add_member_button.place(rely=0.5, relx=0.08, anchor='center')

add_coach_button = tkinter.Button(header, text="Add Coach", command=openCoachContent, fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 12, 'bold'), padx=10, cursor="tcross")
add_coach_button.place(rely=0.5, relx=0.22, anchor='center')

coaching_session_button = tkinter.Button(header, text="Coaching Session", command=openCoachSessionContent, fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 12, 'bold'), padx=10, cursor="tcross")
coaching_session_button.place(rely=0.5, relx=0.38, anchor='center')

competition_button = tkinter.Button(header, text="Competition", command=openCompetitionContent, fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 12, 'bold'), padx=10, cursor="tcross")
competition_button.place(rely=0.5, relx=0.546, anchor='center')

member_booking_button = tkinter.Button(header, text="Booking", command=openMemberBooking, fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 12, 'bold'), padx=10, cursor="tcross")
member_booking_button.place(rely=0.5, relx=0.676, anchor='center')

statistics_button = tkinter.Button(header, text="Stats", command=openStaticstics, fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 12, 'bold'), padx=10, cursor="tcross")
statistics_button.place(rely=0.5, relx=0.71, anchor='center')


mainScreen.mainloop()