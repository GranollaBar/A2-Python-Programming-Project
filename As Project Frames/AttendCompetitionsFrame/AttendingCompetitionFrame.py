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
from datetime import timedelta
from datetime import date
from CoachingSessionFrame.CoachingSessionEmail import SessionEmail
import time
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
import matplotlib.pyplot as plt
import Pmw



class AttendingSinglesContent:

    def __init__(self, mainScreen):
        self.attend = mainScreen
        self.conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
        self.c = self.conn.cursor()


        # self.c.execute("""CREATE TABLE CurrentCompetitionScores (
        #             CompetitionType text,
        #             Member_Team_1_Score text,
        #             Member_Team_2_Score text,
        #             Time text,
        #             CurrentID text
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

            currentday = datetime.datetime.today().strftime('%d/%m/%Y')

            l = 1
            datesarray = []
            datesarray.append(currentday)
            GotARow = False

            while l < 8:
                Begindatestring = date.today()
                newdate = Begindatestring + timedelta(days=l)
                splitnewdate=str(newdate).split('-')
                finalnewdate=splitnewdate[0],splitnewdate[1],splitnewdate[2]
                combineddate = datetime.date(int(finalnewdate[0]),int(finalnewdate[1]), int(finalnewdate[2]))
                CompleteDate = combineddate.strftime("%d/%m/%Y")
                datesarray.append(CompleteDate)
                l += 1

            m = 0

            possibledate = len(datesarray)
            finalpossibledate = datesarray[possibledate - 1]

            for values in datesarray:
                c.execute("SELECT * FROM SinglesCompetition WHERE start_date=:realstartdate AND end_date<:realenddate", {
                    "realstartdate": datesarray[m],
                    "realenddate": finalpossibledate
                })
                singlerow = c.fetchone()
                if (singlerow is None):
                    pass
                else:
                    GotARow = True
                    break
                m += 1

            if GotARow == True:
                lastday = singlerow[3]

                c.execute("SELECT * FROM SinglesCompetition WHERE start_date>=:startdate AND end_date<=:enddate", {
                    "startdate":currentday,
                    "enddate":lastday,
                })

                items = c.fetchall()

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
                    break

            else:
                unplayed_singles_competitions_Tv.insert('','end',text='',values=('','',''))


        def UnplayedDoublesPopulate():
            ClearDoublesTV()

            conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
            c = conn.cursor()

            currentday = datetime.datetime.today().strftime('%d/%m/%Y')

            l = 1
            datesarray = []
            datesarray.append(currentday)
            GotARow = False

            while l < 8:
                Begindatestring = date.today()
                newdate = Begindatestring + timedelta(days=l)
                splitnewdate=str(newdate).split('-')
                finalnewdate=splitnewdate[0],splitnewdate[1],splitnewdate[2]
                combineddate = datetime.date(int(finalnewdate[0]),int(finalnewdate[1]), int(finalnewdate[2]))
                CompleteDate = combineddate.strftime("%d/%m/%Y")
                datesarray.append(CompleteDate)
                l += 1

            m = 0

            possibledate = len(datesarray)
            finalpossibledate = datesarray[possibledate - 1]

            for values in datesarray:
                c.execute("SELECT * FROM DoublesCompetition WHERE start_date=:realstartdate AND end_date<:realenddate", {
                    "realstartdate": datesarray[m],
                    "realenddate": finalpossibledate
                })
                doublerow = c.fetchone()
                print(doublerow)
                if (doublerow is None):
                    pass
                else:
                    GotARow = True
                    break
                m += 1

            if GotARow == True:
                lastday = doublerow[5]

                c.execute("SELECT * FROM DoublesCompetition WHERE start_date>=:startdate AND end_date<=:enddate", {
                    "startdate":currentday,
                    "enddate":lastday
                })

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

            else:
                unplayed_doubles_competitions_Tv.insert('','end',text='',values=('','',''))


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


        def SelectTypeandID():
            conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
            c = conn.cursor()

            c.execute("SELECT * FROM CurrentCompetitionScores")
            row = c.fetchall()

            if len(row) <= 0:

                IDSelected = CompetitionID.get()
                competitiontext = CompetitionType_combobox.get()
                member_team1_score = score1.get()
                member_team2_score = score2.get()
                currentTime = int(time.time())

                if competitiontext == 'Singles':
                    GotAnID = False
                    currentday = datetime.datetime.today().strftime('%d/%m/%Y')

                    l = 1
                    datesarray = []
                    datesarray.append(currentday)
                    GotARow = False

                    while l < 8:
                        Begindatestring = date.today()
                        newdate = Begindatestring + timedelta(days=l)
                        splitnewdate=str(newdate).split('-')
                        finalnewdate=splitnewdate[0],splitnewdate[1],splitnewdate[2]
                        combineddate = datetime.date(int(finalnewdate[0]),int(finalnewdate[1]), int(finalnewdate[2]))
                        CompleteDate = combineddate.strftime("%d/%m/%Y")
                        datesarray.append(CompleteDate)
                        l += 1

                    m = 0

                    possibledate = len(datesarray)
                    finalpossibledate = datesarray[possibledate - 1]

                    for values in datesarray:
                        c.execute("SELECT * FROM SinglesCompetition WHERE start_date=:realstartdate AND end_date<:realenddate", {
                            "realstartdate": datesarray[m],
                            "realenddate": finalpossibledate
                        })
                        singlerow = c.fetchone()
                        if (singlerow is None):
                            pass
                        else:
                            GotARow = True
                            break
                        m += 1

                    if GotARow == True:
                        lastday = singlerow[3]

                        c.execute("SELECT * FROM SinglesCompetition WHERE start_date>=:startdate AND end_date<=:enddate", {
                            "startdate":currentday,
                            "enddate":lastday
                        })

                        singlesrow = c.fetchall()
                        singlesarray = []
                        i = 0

                        for row in singlesrow:
                            singlesarray.append(singlesrow[i][5])
                            i += 1

                        j = 0

                        for rows in singlesarray:
                            if IDSelected == singlesarray[0 + j]:
                                GotAnID = True
                                c.execute("INSERT INTO CurrentCompetitionScores VALUES (:CompetitionType, :Member_Team_1_Score, :Member_Team_2_Score, :Time, :CurrentID)",
                                          {
                                              'CompetitionType': 'Singles',
                                              'Member_Team_1_Score': member_team1_score,
                                              'Member_Team_2_Score': member_team2_score,
                                              'Time': currentTime,
                                              'CurrentID': CompetitionID.get(),
                                          })
                                conn.commit()
                                conn.close()

                                CompetitionType_combobox.config(state="disable")
                                ID_entry.config(state="disable")
                                select_competition_button.config(state="disable")
                                score1_entry.config(state="normal")
                                score2_entry.config(state="normal")
                                submit_competition_button.config(state="normal")

                                DrawLineGraphSingles()

                            else:
                                j += 1

                        if GotAnID == False:
                            messagebox.showinfo('Error', 'The ID entered does not have a singles competition on ' + currentday, icon='error')
                    else:
                        messagebox.showinfo('Error', 'There are no singles competitions currently listed for the date: ' + currentday, icon='error')


                if competitiontext == 'Doubles':
                    GotAnID = False
                    currentday = datetime.datetime.today().strftime('%d/%m/%Y')

                    l = 1
                    datesarray = []
                    datesarray.append(currentday)
                    GotARow = False

                    while l < 8:
                        Begindatestring = date.today()
                        newdate = Begindatestring + timedelta(days=l)
                        splitnewdate=str(newdate).split('-')
                        finalnewdate=splitnewdate[0],splitnewdate[1],splitnewdate[2]
                        combineddate = datetime.date(int(finalnewdate[0]),int(finalnewdate[1]), int(finalnewdate[2]))
                        CompleteDate = combineddate.strftime("%d/%m/%Y")
                        datesarray.append(CompleteDate)
                        l += 1

                    m = 0

                    possibledate = len(datesarray)
                    finalpossibledate = datesarray[possibledate - 1]

                    for values in datesarray:
                        c.execute("SELECT * FROM DoublesCompetition WHERE start_date=:realstartdate AND end_date<:realenddate", {
                            "realstartdate": datesarray[m],
                            "realenddate": finalpossibledate
                        })
                        singlerow = c.fetchone()
                        if (singlerow is None):
                            pass
                        else:
                            GotARow = True
                            break
                        m += 1

                    if GotARow == True:
                        lastday = singlerow[5]

                        c.execute("SELECT * FROM DoublesCompetition WHERE start_date>=:startdate AND end_date<=:enddate", {
                            "startdate":currentday,
                            "enddate":lastday
                        })

                        doublesrow = c.fetchall()
                        doublesarray = []
                        i = 0

                        for row in doublesrow:
                            doublesarray.append(doublesrow[i][9])
                            i += 1

                        j = 0

                        for rows in doublesarray:
                            if IDSelected == doublesarray[0 + j]:
                                GotAnID = True
                                c.execute("INSERT INTO CurrentCompetitionScores VALUES (:CompetitionType, :Member_Team_1_Score, :Member_Team_2_Score, :Time, :CurrentID)",
                                          {
                                              'CompetitionType': 'Doubles',
                                              'Member_Team_1_Score': member_team1_score,
                                              'Member_Team_2_Score': member_team2_score,
                                              'Time': currentTime,
                                              'CurrentID': CompetitionID.get(),
                                          })
                                conn.commit()
                                conn.close()

                                CompetitionType_combobox.config(state="disable")
                                ID_entry.config(state="disable")
                                select_competition_button.config(state="disable")
                                score1_entry.config(state="normal")
                                score2_entry.config(state="normal")
                                submit_competition_button.config(state="normal")

                                DrawLineGraphDoubles()

                            else:
                                j += 1

                        if GotAnID == False:
                            messagebox.showinfo('Error', 'The ID entered does not have a doubles competition on ' + currentday, icon='error')
                    else:
                        messagebox.showinfo('Error', 'There are no Doubles competitions currently listed for the date: ' + currentday, icon='error')


        def DrawLineGraphSingles():
            conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
            c = conn.cursor()

            c.execute("SELECT * FROM CurrentCompetitionScores")
            IDRow = c.fetchall()

            text = 'ID: ' + str(IDRow[0][4]) + ' - Singles Competition'

            style.use('seaborn-darkgrid')

            font = {'family': 'serif',
                    'color':  'black',
                    'weight': 'normal',
                    'size': 16,
                    }

            c.execute("SELECT * FROM CurrentCompetitionScores")
            scoreRows = c.fetchall()

            player1Scores = []
            player2Scores = []
            secondsIntoGame = []

            if len(scoreRows) > 1:
                baseTime = int(scoreRows[0][3])

                for scoreRow in scoreRows:
                    player1Scores.append(scoreRow[1])
                    player2Scores.append(scoreRow[2])
                    secondsIntoGame.append(int(scoreRow[3]) - int(baseTime))

                fig = plt.figure(figsize=(4,4), dpi=70, tight_layout=True)
                ax1 = fig.add_subplot(111)
                ax1.plot(secondsIntoGame, player1Scores, color="limegreen", label="Score1")
                ax1.plot(secondsIntoGame, player2Scores, color="blue", label="Score2")
                ax1.set_title(text, fontdict=font)
                ax1.set_xlabel('Time', fontdict=font)
                ax1.set_ylabel('Score', fontdict=font)

                canvas = FigureCanvasTkAgg(fig, self.attend)
                canvas.get_tk_widget().place(relx=0.2,rely=0.662,anchor=CENTER)
                canvas.draw()

            else:
                fig = plt.figure(figsize=(4,4), dpi=70, tight_layout=True)
                ax1 = fig.add_subplot(111)
                ax1.plot([0], [0], color="limegreen", label="Score1")
                ax1.plot([0], [0], color="blue", label="Score2")
                ax1.set_title(text, fontdict=font)
                ax1.set_xlabel('Time', fontdict=font)
                ax1.set_ylabel('Score', fontdict=font)

                canvas = FigureCanvasTkAgg(fig, self.attend)
                canvas.get_tk_widget().place(relx=0.2,rely=0.662,anchor=CENTER)
                canvas.draw()


        def DrawLineGraphDoubles():
            conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
            c = conn.cursor()

            c.execute("SELECT * FROM CurrentCompetitionScores")
            IDRow = c.fetchall()

            text = 'ID: ' + str(IDRow[0][4]) + ' - Doubles Competition'

            style.use('seaborn-darkgrid')

            font = {'family': 'serif',
                    'color':  'black',
                    'weight': 'normal',
                    'size': 16,
                    }

            c.execute("SELECT * FROM CurrentCompetitionScores")
            scoreRows = c.fetchall()

            player1Scores = []
            player2Scores = []
            secondsIntoGame = []

            if len(scoreRows) > 1:
                baseTime = int(scoreRows[0][3])

                for scoreRow in scoreRows:
                    player1Scores.append(scoreRow[1])
                    player2Scores.append(scoreRow[2])
                    secondsIntoGame.append(int(scoreRow[3]) - int(baseTime))

                fig = plt.figure(figsize=(4,4), dpi=70, tight_layout=True)
                ax1 = fig.add_subplot(111)
                ax1.plot(secondsIntoGame, player1Scores, color="limegreen")
                ax1.plot(secondsIntoGame, player2Scores, color="blue")
                ax1.set_title(text, fontdict=font)
                ax1.set_xlabel('Time', fontdict=font)
                ax1.set_ylabel('Score', fontdict=font)

                canvas = FigureCanvasTkAgg(fig, self.attend)
                canvas.get_tk_widget().place(relx=0.2,rely=0.662,anchor=CENTER)
                canvas.draw()

            else:
                fig = plt.figure(figsize=(4,4), dpi=70, tight_layout=True)
                ax1 = fig.add_subplot(111)
                ax1.plot([0], [0], color="limegreen")
                ax1.plot([0], [0], color="blue")
                ax1.set_title(text, fontdict=font)
                ax1.set_xlabel('Time', fontdict=font)
                ax1.set_ylabel('Score', fontdict=font)

                canvas = FigureCanvasTkAgg(fig, self.attend)
                canvas.get_tk_widget().place(relx=0.2,rely=0.662,anchor=CENTER)
                canvas.draw()


        def SubmitSinglesResults():
            member_team1_score = score1.get()
            member_team2_score = score2.get()
            currentTime = int(time.time())

            conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
            c = conn.cursor()

            c.execute("SELECT * FROM CurrentCompetitionScores")
            Row = c.fetchall()

            if len(Row) == 1 and len(Row[0][0]) > 0:
                c.execute("INSERT INTO CurrentCompetitionScores VALUES (:CompetitionType, :Member_Team_1_Score, :Member_Team_2_Score, :Time, :CurrentID)",
                          {
                              'CompetitionType': 'Singles',
                              'Member_Team_1_Score': member_team1_score,
                              'Member_Team_2_Score': member_team2_score,
                              'Time': currentTime,
                              'CurrentID': Row[0][4],
                          })

                conn.commit()
                conn.close()

            elif len(Row) > 1:
                c.execute("INSERT INTO CurrentCompetitionScores VALUES (:CompetitionType, :Member_Team_1_Score, :Member_Team_2_Score, :Time, :CurrentID)",
                          {
                              'CompetitionType': 'Singles',
                              'Member_Team_1_Score': member_team1_score,
                              'Member_Team_2_Score': member_team2_score,
                              'Time': currentTime,
                              'CurrentID': Row[0][4],
                          })

                conn.commit()
                conn.close()

            DrawLineGraphSingles()


        def SubmitDoublesResults():
            member_team1_score = score1.get()
            member_team2_score = score2.get()
            currentTime = int(time.time())

            conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
            c = conn.cursor()

            c.execute("SELECT * FROM CurrentCompetitionScores")
            Row = c.fetchall()

            if len(Row) == 1:
                c.execute("UPDATE CurrentCompetitionScores SET CompetitionType = :competitiontype AND Member_Team_1_Score = :score1 AND Member_Team_2_Score = :score2 AND Time = :time",
                          {
                              'competitiontype': 'Doubles',
                              'score1': member_team1_score,
                              'score2': member_team2_score,
                              'time': currentTime,
                          })

            elif len(Row) == 1 and len(Row[0][0]) > 0:
                c.execute("INSERT INTO CurrentCompetitionScores VALUES (:CompetitionType, :Member_Team_1_Score, :Member_Team_2_Score, :Time, :CurrentID)",
                          {
                              'CompetitionType': 'Doubles',
                              'Member_Team_1_Score': member_team1_score,
                              'Member_Team_2_Score': member_team2_score,
                              'Time': currentTime,
                              'CurrentID': Row[0][4],
                          })

            elif len(Row) > 1:
                c.execute("INSERT INTO CurrentCompetitionScores VALUES (:CompetitionType, :Member_Team_1_Score, :Member_Team_2_Score, :Time, :CurrentID)",
                          {
                              'CompetitionType': 'Doubles',
                              'Member_Team_1_Score': member_team1_score,
                              'Member_Team_2_Score': member_team2_score,
                              'Time': currentTime,
                              'CurrentID': Row[0][4],
                          })

            conn.commit()
            conn.close()

            DrawLineGraphDoubles()


        def temporary():
            pass



        CompetitionID = IntVar()
        score1 = IntVar()
        score2 = IntVar()

        CompetitionType = ['Singles','Doubles']

        ToolTips = Pmw.Balloon()


        conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
        c = conn.cursor()

        c.execute("DELETE FROM CurrentCompetitionScores")

        conn.commit()
        conn.close()


        competitiontype_label = tkinter.Label(self.attend, text="Type:", font=('Tahoma', 14, 'bold'), fg='black', bg='white')
        competitiontype_label.place(rely=0.41, relx=0.06, anchor='center')

        CompetitionType_combobox = ttk.Combobox(self.attend, value=CompetitionType,font=('Tahoma', 11, 'bold'), width=7)
        CompetitionType_combobox.place(rely=0.413, relx=0.15, anchor='center')
        CompetitionType_combobox.current(0)
        CompetitionType_combobox.config(state="readonly")

        id_label = tkinter.Label(self.attend, text="ID:", font=('Tahoma', 14, 'bold'), fg='black', bg='white')
        id_label.place(rely=0.41, relx=0.24, anchor='center')

        ID_entry = tkinter.Entry(self.attend, width=6, textvariable=CompetitionID, bd=3, relief='ridge', cursor="tcross", font=('Tahoma', 12, 'bold'))
        ID_entry.place(rely=0.412, relx=0.3, anchor='center')
        CompetitionID.set('')
        ID_entry.insert(0, 'e.g. 3')
        ID_entry.bind('<FocusIn>', ID_click)
        ID_entry.bind('<FocusOut>', ID_unclick)
        ID_entry.config(fg='grey')

        select_competition_button = tkinter.Button(self.attend, cursor="tcross",text="Select", command=SelectTypeandID, fg='white', bg='black', bd=3, relief='ridge', font=('Tahoma', 11, 'bold'))
        select_competition_button.place(rely=0.415, relx=0.4, anchor='center')
        ToolTips.bind(select_competition_button, 'Confirm ID and competition type')


        score1_label = tkinter.Label(self.attend, text="Member/Team Score 1:", font=('serif', 14, 'bold'), fg='black', bg='white')
        score1_label.place(rely=0.9, relx=0.135, anchor='center')

        score1_entry = tkinter.Entry(self.attend, width=6, textvariable=score1, bd=3, relief='ridge', cursor="tcross", font=('Tahoma', 12, 'bold'))
        score1_entry.place(rely=0.9, relx=0.3, anchor='center')


        score2_label = tkinter.Label(self.attend, text="Member/Team Score 2:", font=('Tahoma', 14, 'bold'), fg='black', bg='white')
        score2_label.place(rely=0.96, relx=0.135, anchor='center')

        score2_entry = tkinter.Entry(self.attend, width=6, textvariable=score2, bd=3, relief='ridge', cursor="tcross", font=('Tahoma', 12, 'bold'))
        score2_entry.place(rely=0.96, relx=0.3, anchor='center')


        conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
        c = conn.cursor()

        c.execute("SELECT * FROM CurrentCompetitionScores")
        RawRow = c.fetchall()

        if len(RawRow) <= 0:
                submit_competition_button = tkinter.Button(self.attend, cursor="tcross",text="Submit", command=SubmitSinglesResults, fg='white', bg='black', bd=3, relief='ridge', font=('Tahoma', 12, 'bold'))
                submit_competition_button.place(rely=0.925, relx=0.4, anchor='center')
                ToolTips.bind(submit_competition_button, 'Enter and submit values for the competition')

        if len(RawRow) > 0:
            print(RawRow[0][0])
            if RawRow[0][0] == 'Singles':
                submit_competition_button = tkinter.Button(self.attend, cursor="tcross",text="Submit", command=SubmitSinglesResults, fg='white', bg='black', bd=3, relief='ridge', font=('Tahoma', 12, 'bold'))
                submit_competition_button.place(rely=0.925, relx=0.4, anchor='center')
                ToolTips.bind(submit_competition_button, 'Enter and submit values for the competition')
            else:
                submit_competition_button = tkinter.Button(self.attend, cursor="tcross",text="Submit", command=SubmitDoublesResults, fg='white', bg='black', bd=3, relief='ridge', font=('Tahoma', 12, 'bold'))
                submit_competition_button.place(rely=0.925, relx=0.4, anchor='center')
                ToolTips.bind(submit_competition_button, 'Enter and submit values for the competition')


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
        unplayed_singles_competitions_scrollbar.place(relx=0.425,rely=0.25,anchor='center',height=166)
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
        unplayed_doubles_competitions_scrollbar.place(relx=0.965,rely=0.25,anchor='center',height=166)
        unplayed_doubles_competitions_Tv.configure(yscrollcommand=unplayed_doubles_competitions_scrollbar.set)


        score1_entry.config(state="disable")
        score2_entry.config(state="disable")
        submit_competition_button.config(state="disable")


        conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
        c = conn.cursor()

        c.execute("SELECT * FROM CurrentCompetitionScores")
        row = c.fetchall()

        if len(row) > 0:
            CompetitionType_combobox.config(state="disable")
            ID_entry.config(state="disable")
            select_competition_button.config(state="disable")
            score1_entry.config(state="normal")
            score2_entry.config(state="normal")
            submit_competition_button.config(state="normal")

            if row[0][0] == 'Singles':
                DrawLineGraphSingles()
            else:
                DrawLineGraphDoubles()


        UnplayedSinglesPopulate()
        UnplayedDoublesPopulate()

