from tkinter import ttk
from tkinter import messagebox
import tkinter.simpledialog
from tkinter.messagebox import showinfo
from tkinter.messagebox import askyesno
import sqlite3
from tkinter import simpledialog
from tkinter import *
from functools import partial
from tkcalendar import Calendar
import datetime
from CoachingSessionFrame.CoachingSessionEmail import SessionEmail
import time
from datetime import date, datetime,timedelta
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from time import strftime



class AttendingSinglesContent:

    def __init__(self, mainScreen):
        self.attend = mainScreen
        self.conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
        self.c = self.conn.cursor()


        # self.c.execute("""CREATE TABLE CurrentCompetitionScores (
        #             Member/Team_1_Score text,
        #             Member/Team_2_Score text,
        #             Time text
        #             )""")


    def generateAttendingSinglesContnt(self):

        def ClearSinglesTV():
            record=unplayed_singles_competitions_Tv.get_children()
            for elements in record:
                unplayed_singles_competitions_Tv.delete(elements)


        def ClearDoublesTV():
            record=unplayed_doubles_competitions_Tv.get_children()
            for elements in record:
                unplayed_doubles_competitions_Tv.delete(elements)


        def UnplayedSinglesPopulate():
            ClearSinglesTV()

            conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
            c = conn.cursor()

            c.execute("SELECT * FROM SinglesCompetition")
            items = c.fetchall()

            conn.commit()
            conn.close()

            count=0
            for row in items:
                if row == []:
                    pass
                else:
                    if count%2==0:
                        unplayed_singles_competitions_Tv.insert('','end',text='Singles',values=(findfirstandsurnamemember(row[0]),findfirstandsurnamemember(row[1]),row[5]))
                    else:
                        unplayed_singles_competitions_Tv.insert('','end',text='Singles',values=(findfirstandsurnamemember(row[0]),findfirstandsurnamemember(row[1]),row[5]))
                    count+=1


        def UnplayedDoublesPopulate():
            ClearDoublesTV()

            conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
            c = conn.cursor()

            c.execute("SELECT * FROM DoublesCompetition")
            items = c.fetchall()

            conn.commit()
            conn.close()

            count=0
            for row in items:
                if row == []:
                    pass
                else:
                    if count%2==0:
                        unplayed_doubles_competitions_Tv.insert('','end',text='Doubles',values=(row[7],row[8],row[9]))
                    else:
                        unplayed_doubles_competitions_Tv.insert('','end',text='Doubles',values=(row[7],row[8],row[9]))
                    count+=1


        def findfirstandsurnamemember(username):
            conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
            c = conn.cursor()

            c.execute("SELECT * FROM member WHERE username=:memberusername", {
                "memberusername": username
            })
            singlesrow = c.fetchone()
            labelusername = singlesrow[2] + ' ' + singlesrow[3]

            return labelusername


        def treeviewresizedisable(treeview, event):
            if treeview.identify_region(event.x, event.y) == "separator":
                return "break"


        def ID_click(event):
            if ID_entry.get() == 'e.g. 3':
                ID_entry.delete(0, "end")
                ID_entry.insert(0, '')
                ID_entry.config(fg='black')


        def ID_unclick(event):
            if ID_entry.get() == '':
                ID_entry.insert(0, 'e.g. 3')
                ID_entry.config(fg='grey')


        CompetitionID = IntVar
        CompetitionType = ['Singles','Doubles']


        competitiontype_label = tkinter.Label(self.attend, text="Type:", font=('Tahoma', 14, 'bold'), fg='black', bg='white')
        competitiontype_label.place(rely=0.42, relx=0.08, anchor='center')

        CompetitionType_combobox = ttk.Combobox(self.attend, value=CompetitionType,font=('Tahoma', 11, 'bold'), width=7)
        CompetitionType_combobox.place(rely=0.424, relx=0.17, anchor='center')
        CompetitionType_combobox.current(0)
        CompetitionType_combobox.config(state="readonly")

        id_label = tkinter.Label(self.attend, text="ID:", font=('Tahoma', 14, 'bold'), fg='black', bg='white')
        id_label.place(rely=0.42, relx=0.28, anchor='center')

        ID_entry = tkinter.Entry(self.attend, width=6, textvariable=CompetitionID, bd=3, relief='ridge', cursor="tcross", font=('Tahoma', 12, 'bold'))
        ID_entry.place(rely=0.422, relx=0.34, anchor='center')
        ID_entry.insert(0, 'e.g. 3')
        ID_entry.bind('<FocusIn>', ID_click)
        ID_entry.bind('<FocusOut>', ID_unclick)
        ID_entry.config(fg='grey')


        unplayed_singles_competitions_Tv=ttk.Treeview(self.attend,height=7,columns=('Member 1','Member 2','ID'))
        unplayed_singles_competitions_Tv.place(relx=0.23,rely=0.25,anchor=CENTER)

        unplayed_singles_competitions_Tv.heading("#0",text='Competition Type')
        unplayed_singles_competitions_Tv.column("#0",minwidth=0,width=115)
        unplayed_singles_competitions_Tv.heading("#1",text='Member 1')
        unplayed_singles_competitions_Tv.column("#1",minwidth=0,width=110)
        unplayed_singles_competitions_Tv.heading("#2",text='Member 2')
        unplayed_singles_competitions_Tv.column("#2",minwidth=0,width=110)
        unplayed_singles_competitions_Tv.heading("#3",text='ID')
        unplayed_singles_competitions_Tv.column("#3",minwidth=0,width=40)
        unplayed_singles_competitions_Tv.bind('<Button-1>', partial(treeviewresizedisable, unplayed_singles_competitions_Tv))

        unplayed_singles_competitions_scrollbar = Scrollbar(self.attend, orient='vertical', command=unplayed_singles_competitions_Tv.yview, cursor="tcross")
        unplayed_singles_competitions_scrollbar.place(relx=0.425,rely=0.25,anchor='center',height=167)
        unplayed_singles_competitions_Tv.configure(yscrollcommand=unplayed_singles_competitions_scrollbar.set)


        unplayed_doubles_competitions_Tv=ttk.Treeview(self.attend,height=7,columns=('Team 1','Team 2','ID'))
        unplayed_doubles_competitions_Tv.place(relx=0.71,rely=0.25,anchor=CENTER)

        unplayed_doubles_competitions_Tv.heading("#0",text='Competition Type')
        unplayed_doubles_competitions_Tv.column("#0",minwidth=0,width=115)
        unplayed_doubles_competitions_Tv.heading("#1",text='Team 1')
        unplayed_doubles_competitions_Tv.column("#1",minwidth=0,width=170)
        unplayed_doubles_competitions_Tv.heading("#2",text='Team 2')
        unplayed_doubles_competitions_Tv.column("#2",minwidth=0,width=170)
        unplayed_doubles_competitions_Tv.heading("#3",text='ID')
        unplayed_doubles_competitions_Tv.column("#3",minwidth=0,width=40)
        unplayed_doubles_competitions_Tv.bind('<Button-1>', partial(treeviewresizedisable, unplayed_doubles_competitions_Tv))

        unplayed_doubles_competitions_scrollbar = Scrollbar(self.attend, orient='vertical', command=unplayed_doubles_competitions_Tv.yview, cursor="tcross")
        unplayed_doubles_competitions_scrollbar.place(relx=0.965,rely=0.25,anchor='center',height=167)
        unplayed_doubles_competitions_Tv.configure(yscrollcommand=unplayed_doubles_competitions_scrollbar.set)


        # conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
        # c = conn.cursor()
        #
        # c.execute("SELECT * FROM CurrentCompetitionScores")
        # items = c.fetchall()
        # print(items)
        #
        #
        # string = strftime('%H:%M:%S %p')
        # print(string)
        #
        # fig = Figure(figsize=(4,4), dpi=72)
        # a = fig.add_subplot(111)
        # a.plot([string],[1])
        # a.plot([string],[0])
        #
        # canvas = FigureCanvasTkAgg(fig, self.attend)
        # canvas.get_tk_widget().place(relx=0.5,rely=0.6,anchor=CENTER)
        # canvas.draw()
        #
        # toolbar = NavigationToolbar2Tk(canvas, self.attend, pack_toolbar=False)
        # toolbar.update()
        # toolbar.place(relx=0.7,rely=0.6,anchor=CENTER)


        UnplayedSinglesPopulate()
        UnplayedDoublesPopulate()

