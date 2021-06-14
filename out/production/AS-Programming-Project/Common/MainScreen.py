import tkinter.simpledialog
from tkinter import *
from MemberFrame.MemberDetailsScreen import MemberContent
from CoachingSessionFrame.CoachingSessionScreen import CoachingSessionContent
from CoachFrame.CoachDetailsScreen import CoachContent



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



mainScreen = Tk()
mainScreen.geometry('985x650')

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
add_member_button.place(rely=0.5, relx=0.09, anchor='center')

add_coach_button = tkinter.Button(header, text="Add Coach", command=openCoachContent, fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 12, 'bold'), padx=10, cursor="tcross")
add_coach_button.place(rely=0.5, relx=0.24, anchor='center')

coaching_session_button = tkinter.Button(header, text="Coaching Session", command=openCoachSessionContent, fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 12, 'bold'), padx=10, cursor="tcross")
coaching_session_button.place(rely=0.5, relx=0.408, anchor='center')



mainScreen.mainloop()