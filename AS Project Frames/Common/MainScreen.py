import tkinter.simpledialog
from tkinter import *
from CoachingFrame.CoachingSessionScreen import CoachingSessionContent

mainScreen = Tk()
mainScreen.geometry('900x600')

header = Frame(mainScreen, bg='pale green')
content = Frame(mainScreen, bg='white')

mainScreen.columnconfigure(0, weight=1)
mainScreen.rowconfigure(0, weight=1)
mainScreen.rowconfigure(1, weight=9)

header.grid(row=0, sticky="nsew")
content.grid(row=1, sticky="nsew")

myCoaching = CoachingSessionContent(mainScreen)

add_member_button = tkinter.Button(header, text="Add Member", command=myCoaching.coachingSession(), fg='white', bg='black', bd=4, relief='ridge', font=('Segoe UI Black', 12, 'bold'), padx=10)
add_member_button.place(rely=0.5, relx=0.1, anchor='center')

coaching_session_button = tkinter.Button(header, text="Coaching Session", command=myCoaching.coachingSession(), fg='white', bg='black', bd=4, relief='ridge', font=('Segoe UI Black', 12, 'bold'), padx=10)
coaching_session_button.place(rely=0.5, relx=0.3, anchor='center')

#test_button = tkinter.Button(header, text="test", command=myCoaching.coachSelection(), fg='white', bg='black', bd=4, relief='ridge', font=('Tahoma', 14, 'bold'), padx=10, cursor="tcross")
#test_button.place(rely=0.5, relx=0.5, anchor='center')

myCoaching.generateContnt()
