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

previous1 = 0
previous2 = 0
counter = 0

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
        #
        # self.c.execute("""CREATE TABLE FinshedCompetitions (
        #             CompetitionType text,
        #             Member_Team_1 text,
        #             Member_Team_1_Score text,
        #             Member_Team_2 text,
        #             Member_Team_2_Score text,
        #             Final_time_seconds text,
        #             CurrentID text
        #             )""")


    def generateAttendingSinglesContnt(self):

        def validate_member_team_score(value1, value2):
            global previous1
            global previous2

            if value1 <= (previous1 - 1):
                messagebox.showinfo("Validation Error", "Score 1 must not be less than the previous score entered", icon='error')
                return False

            if value2 <= (previous2 - 1):
                messagebox.showinfo("Validation Error", "Score 2 must not be less than the previous score entered", icon='error')
                return False

            if value1 > (previous1 + 1):
                messagebox.showinfo("Validation Error", "Score 1 can only be increased by 1 each cycle", icon='error')
                return False

            if value2 > (previous2 + 1):
                messagebox.showinfo("Validation Error", "Score 2 can only be increased by 1 each cycle", icon='error')
                return False

            if value1 == previous1 and value2 == previous2:
                messagebox.showinfo("Validation Error", "One score must be increased by 1 each cycle", icon='error')
                return False

            if value1 == previous1+1 and value2 == previous2+1:
                messagebox.showinfo("Validation Error", "Only one score can be increased each cycle", icon='error')
                return False

            previous1 = value1
            previous2 = value2
            return True


        def clearcanvas(singlescanvas):
            for item in singlescanvas.get_tk_widget().find_all():
                singlescanvas.get_tk_widget().delete(item)


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
            o = 7
            w = 1
            startdatesarray = []
            enddatesarray = []
            enddatesarray.append(currentday)
            GotARow = False

            while l < 8:
                Begindatestring = date.today()
                newdate = Begindatestring + timedelta(days=l)
                splitnewdate=str(newdate).split('-')
                finalnewdate=splitnewdate[0],splitnewdate[1],splitnewdate[2]
                combineddate = datetime.date(int(finalnewdate[0]),int(finalnewdate[1]), int(finalnewdate[2]))
                CompleteDate = combineddate.strftime("%d/%m/%Y")
                enddatesarray.append(CompleteDate)
                l += 1

            while w < 8:
                Begindatestring = date.today()
                newdate = Begindatestring - timedelta(days=o)
                splitnewdate=str(newdate).split('-')
                finalnewdate=splitnewdate[0],splitnewdate[1],splitnewdate[2]
                combineddate = datetime.date(int(finalnewdate[0]),int(finalnewdate[1]), int(finalnewdate[2]))
                CompleteDate = combineddate.strftime("%d/%m/%Y")
                startdatesarray.append(CompleteDate)
                w += 1
                o -= 1

            finaldatesarray = startdatesarray + enddatesarray

            c.execute('SELECT * FROM SinglesCompetition')
            Allrows = c.fetchall()

            datesarray = []
            p = 1

            for starting in Allrows:
                c.execute("SELECT * FROM SinglesCompetition WHERE start_date>:realstartdate AND end_date<:realenddate AND singlescompetitionID=:ID", {
                    "realstartdate": finaldatesarray[0],
                    "realenddate": finaldatesarray[14],
                    "ID": p
                })
                singlerow = c.fetchone()
                if (singlerow is None):
                    pass
                else:
                    rowsplit = singlerow[2].split('/')
                    currentdaysplit = currentday.split('/')
                    if rowsplit[1] == currentdaysplit[1]:
                        datesarray.append(singlerow)
                    else:
                        pass
                p += 1

            r = 0
            s = 0

            if len(datesarray) != 0:
                if len(datesarray) == 1:
                    firstday = datesarray[0][2]
                    lastday = datesarray[0][3]
                    q = 0

                    for datevalues in finaldatesarray:
                        if finaldatesarray[q] >= firstday and finaldatesarray[q] <= lastday:
                            q += 1
                            pass
                            if finaldatesarray[q] == lastday:
                                break
                        else:
                            finaldatesarray.remove(finaldatesarray[q])

                    finallistlength = len(finaldatesarray)
                    finallength = finallistlength - q

                    q += 1

                    for x in range(0, finallength - 1):
                        del finaldatesarray[q]

                        for allvalues in finaldatesarray:
                            if allvalues == currentday:
                                GotARow = True

                        break

                else:
                    for z in range(0, len(datesarray)):
                        firstday = datesarray[r][2]
                        lastday = datesarray[r][3]
                        r = 0
                        s = 0
                        q = 0

                        if z != 0:
                            finaldatesarray.clear()
                            finaldatesarray = startdatesarray + enddatesarray

                        for datevalues in finaldatesarray:
                            if finaldatesarray[q] >= firstday and finaldatesarray[q] <= lastday:
                                q += 1
                                pass
                                if finaldatesarray[q] == lastday:
                                    break
                            else:
                                finaldatesarray.remove(finaldatesarray[q])

                        finallistlength = len(finaldatesarray)
                        finallength = finallistlength - q

                        q += 1

                        for x in range(0, finallength - 1):
                            del finaldatesarray[q]

                        for allvalues in finaldatesarray:
                            if allvalues == currentday:
                                GotARow = True
                                break
                            else:
                                if allvalues == finaldatesarray[len(finaldatesarray) - 1]:
                                    break
                                else:
                                    pass

                        if GotARow == True:
                            while s != z:
                                datesarray.remove(datesarray[s])
                                s += 1
                            break
                        else:
                            pass

                        r += 1

                if GotARow == True:
                    finalfirstday = datesarray[0][2]
                    finallastday = datesarray[0][3]

                    c.execute("SELECT * FROM SinglesCompetition WHERE end_date=:enddate AND start_date=:startdate", {
                        "enddate":finallastday,
                        "startdate": finalfirstday
                    })

                    items = c.fetchone()

                    conn.commit()
                    conn.close()

                    count=0
                    if items == []:
                        pass
                    else:
                        if count%2==0:
                            unplayed_singles_competitions_Tv.insert('','end',text='Singles',values=(findfirstandsurnamemember(items[0]),findfirstandsurnamemember(items[1]),items[5]))
                        else:
                            unplayed_singles_competitions_Tv.insert('','end',text='Singles',values=(findfirstandsurnamemember(items[0]),findfirstandsurnamemember(items[1]),items[5]))
                        count+=1

                else:
                    unplayed_singles_competitions_Tv.insert('','end',text='',values=('','',''))

            else:
                unplayed_singles_competitions_Tv.insert('','end',text='',values=('','',''))


        def UnplayedDoublesPopulate():
            ClearDoublesTV()

            conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
            c = conn.cursor()

            currentday = datetime.datetime.today().strftime('%d/%m/%Y')

            l = 1
            o = 7
            w = 1
            startdatesarray = []
            enddatesarray = []
            enddatesarray.append(currentday)
            GotARow = False

            while l < 8:
                Begindatestring = date.today()
                newdate = Begindatestring + timedelta(days=l)
                splitnewdate=str(newdate).split('-')
                finalnewdate=splitnewdate[0],splitnewdate[1],splitnewdate[2]
                combineddate = datetime.date(int(finalnewdate[0]),int(finalnewdate[1]), int(finalnewdate[2]))
                CompleteDate = combineddate.strftime("%d/%m/%Y")
                enddatesarray.append(CompleteDate)
                l += 1

            while w < 8:
                Begindatestring = date.today()
                newdate = Begindatestring - timedelta(days=o)
                splitnewdate=str(newdate).split('-')
                finalnewdate=splitnewdate[0],splitnewdate[1],splitnewdate[2]
                combineddate = datetime.date(int(finalnewdate[0]),int(finalnewdate[1]), int(finalnewdate[2]))
                CompleteDate = combineddate.strftime("%d/%m/%Y")
                startdatesarray.append(CompleteDate)
                w += 1
                o -= 1

            finaldatesarray = startdatesarray + enddatesarray

            c.execute('SELECT * FROM DoublesCompetition')
            Allrows = c.fetchall()

            Datesarray = []
            p = 1

            for starting in Allrows:
                c.execute("SELECT * FROM DoublesCompetition WHERE start_date>:realstartdate AND end_date<:realenddate AND doublescompetitionID=:ID", {
                    "realstartdate": finaldatesarray[0],
                    "realenddate": finaldatesarray[14],
                    "ID": p
                })
                doublerow = c.fetchone()
                if (doublerow is None):
                    pass
                else:
                    rowsplit = doublerow[4].split('/')
                    currentdaysplit = currentday.split('/')
                    if rowsplit[1] == currentdaysplit[1]:
                        Datesarray.append(doublerow)
                    else:
                        pass
                p += 1

            r = 0
            s = 0

            if len(Datesarray) != 0:
                if len(Datesarray) == 1:
                    firstday = Datesarray[0][4]
                    lastday = Datesarray[0][5]
                    q = 0

                    for datevalues in finaldatesarray:
                        if finaldatesarray[q] >= firstday and finaldatesarray[q] <= lastday:
                            q += 1
                            pass
                            if finaldatesarray[q] == lastday:
                                break
                        else:
                            finaldatesarray.remove(finaldatesarray[q])

                    finallistlength = len(finaldatesarray)
                    finallength = finallistlength - q

                    q += 1

                    for x in range(0, finallength - 1):
                        del finaldatesarray[q]

                        for allvalues in finaldatesarray:
                            if allvalues == currentday:
                                GotARow = True

                        break

                else:
                    for z in range(0, len(Datesarray)):
                        firstday = Datesarray[r][4]
                        lastday = Datesarray[r][5]
                        r = 0
                        s = 0
                        q = 0

                        if z != 0:
                            finaldatesarray.clear()
                            finaldatesarray = startdatesarray + enddatesarray

                        for datevalues in finaldatesarray:
                            if finaldatesarray[q] >= firstday and finaldatesarray[q] <= lastday:
                                q += 1
                                pass
                                if finaldatesarray[q] == lastday:
                                    break
                            else:
                                finaldatesarray.remove(finaldatesarray[q])

                        finallistlength = len(finaldatesarray)
                        finallength = finallistlength - q

                        q += 1

                        for x in range(0, finallength - 1):
                            del finaldatesarray[q]

                        for allvalues in finaldatesarray:
                            if allvalues == currentday:
                                GotARow = True
                                break
                            else:
                                if allvalues == finaldatesarray[len(finaldatesarray) - 1]:
                                    break
                                else:
                                    pass

                        if GotARow == True:
                            while s != z:
                                Datesarray.remove(Datesarray[s])
                                s += 1
                            break
                        else:
                            pass

                        r += 1

                if GotARow == True:
                    finalfirstday = Datesarray[0][4]
                    finallastday = Datesarray[0][5]

                    c.execute("SELECT * FROM DoublesCompetition WHERE end_date=:enddate AND start_date=:startdate", {
                        "enddate":finallastday,
                        "startdate": finalfirstday
                    })

                    items = c.fetchone()

                    conn.commit()
                    conn.close()

                    count=0
                    if items == []:
                        pass
                    else:
                        if count%2==0:
                            unplayed_doubles_competitions_Tv.insert('','end',text='Doubles',values=(items[7],items[8],items[9]))
                        else:
                            unplayed_doubles_competitions_Tv.insert('','end',text='Doubles',values=(items[7],items[8],items[9]))
                        count+=1

                else:
                    unplayed_doubles_competitions_Tv.insert('','end',text='',values=('','',''))

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
                    currentday = datetime.datetime.today().strftime('%d/%m/%Y')

                    l = 1
                    o = 7
                    w = 1
                    startdatesarray = []
                    enddatesarray = []
                    enddatesarray.append(currentday)
                    GotARow = False

                    while l < 8:
                        Begindatestring = date.today()
                        newdate = Begindatestring + timedelta(days=l)
                        splitnewdate=str(newdate).split('-')
                        finalnewdate=splitnewdate[0],splitnewdate[1],splitnewdate[2]
                        combineddate = datetime.date(int(finalnewdate[0]),int(finalnewdate[1]), int(finalnewdate[2]))
                        CompleteDate = combineddate.strftime("%d/%m/%Y")
                        enddatesarray.append(CompleteDate)
                        l += 1

                    while w < 8:
                        Begindatestring = date.today()
                        newdate = Begindatestring - timedelta(days=o)
                        splitnewdate=str(newdate).split('-')
                        finalnewdate=splitnewdate[0],splitnewdate[1],splitnewdate[2]
                        combineddate = datetime.date(int(finalnewdate[0]),int(finalnewdate[1]), int(finalnewdate[2]))
                        CompleteDate = combineddate.strftime("%d/%m/%Y")
                        startdatesarray.append(CompleteDate)
                        w += 1
                        o -= 1

                    finaldatesarray = startdatesarray + enddatesarray

                    c.execute('SELECT * FROM SinglesCompetition')
                    Allrows = c.fetchall()

                    Datesarray = []
                    p = 1

                    for starting in Allrows:
                        c.execute("SELECT * FROM SinglesCompetition WHERE start_date>:realstartdate AND end_date<:realenddate AND singlescompetitionID=:ID", {
                            "realstartdate": finaldatesarray[0],
                            "realenddate": finaldatesarray[14],
                            "ID": p
                        })
                        singlerow = c.fetchone()
                        if (singlerow is None):
                            pass
                        else:
                            rowsplit = singlerow[2].split('/')
                            currentdaysplit = currentday.split('/')
                            if rowsplit[1] == currentdaysplit[1]:
                                Datesarray.append(singlerow)
                            else:
                                pass
                        p += 1

                    r = 0
                    s = 0

                    if len(Datesarray) != 0:
                        if len(Datesarray) == 1:
                            firstday = Datesarray[0][2]
                            lastday = Datesarray[0][3]
                            q = 0

                            for datevalues in finaldatesarray:
                                if finaldatesarray[q] >= firstday and finaldatesarray[q] <= lastday:
                                    q += 1
                                    pass
                                    if finaldatesarray[q] == lastday:
                                        break
                                else:
                                    finaldatesarray.remove(finaldatesarray[q])

                            finallistlength = len(finaldatesarray)
                            finallength = finallistlength - q

                            q += 1

                            for x in range(0, finallength - 1):
                                del finaldatesarray[q]

                                for allvalues in finaldatesarray:
                                    if allvalues == currentday:
                                        GotARow = True

                                break

                        else:
                            for z in range(0, len(Datesarray)):
                                firstday = Datesarray[r][2]
                                lastday = Datesarray[r][3]
                                r = 0
                                s = 0
                                q = 0

                                if z != 0:
                                    finaldatesarray.clear()
                                    finaldatesarray = startdatesarray + enddatesarray

                                for datevalues in finaldatesarray:
                                    if finaldatesarray[q] >= firstday and finaldatesarray[q] <= lastday:
                                        q += 1
                                        pass
                                        if finaldatesarray[q] == lastday:
                                            break
                                    else:
                                        finaldatesarray.remove(finaldatesarray[q])

                                finallistlength = len(finaldatesarray)
                                finallength = finallistlength - q

                                q += 1

                                for x in range(0, finallength - 1):
                                    del finaldatesarray[q]

                                for allvalues in finaldatesarray:
                                    if allvalues == currentday:
                                        GotARow = True
                                        break
                                    else:
                                        if allvalues == finaldatesarray[len(finaldatesarray) - 1]:
                                            break
                                        else:
                                            pass

                                if GotARow == True:
                                    while s != z:
                                        Datesarray.remove(Datesarray[s])
                                        s += 1
                                    break
                                else:
                                    pass

                                r += 1

                        if GotARow == True:
                            finalfirstday = Datesarray[0][2]
                            finallastday = Datesarray[0][3]

                            c.execute("SELECT * FROM SinglesCompetition WHERE end_date=:enddate AND start_date=:startdate", {
                                "enddate":finallastday,
                                "startdate": finalfirstday
                            })

                            singlesrow2 = c.fetchone()

                            if IDSelected == singlesrow2[5]:
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
                                score1_spinbox.config(state="readonly")
                                score2_spinbox.config(state="readonly")
                                submit_competition_button.place_forget()

                                singles_submit_competition_button = tkinter.Button(self.attend, cursor="tcross",text="Submit", command=lambda : SubmitSinglesResults(singles_submit_competition_button), fg='white', bg='black', bd=3, relief='ridge', font=('serif', 12, 'bold'))
                                singles_submit_competition_button.place(rely=0.925, relx=0.4, anchor='center')
                                ToolTips.bind(singles_submit_competition_button, 'Enter and submit values for the singles competition')

                                DrawLineGraphSingles(singles_submit_competition_button)

                            else:
                                messagebox.showinfo('Error', 'The ID entered does not have a singles competition on: ' + currentday, icon='error')
                        else:
                            messagebox.showinfo('Error', 'The ID entered does not have a singles competition on: ' + currentday, icon='error')
                    else:
                        messagebox.showinfo('Error', 'There are no singles competitions currently listed for the date: ' + currentday, icon='error')


                if competitiontext == 'Doubles':
                    currentday = datetime.datetime.today().strftime('%d/%m/%Y')

                    l = 1
                    o = 7
                    w = 1
                    startdatesarray = []
                    enddatesarray = []
                    enddatesarray.append(currentday)
                    GotARow = False

                    while l < 8:
                        Begindatestring = date.today()
                        newdate = Begindatestring + timedelta(days=l)
                        splitnewdate=str(newdate).split('-')
                        finalnewdate=splitnewdate[0],splitnewdate[1],splitnewdate[2]
                        combineddate = datetime.date(int(finalnewdate[0]),int(finalnewdate[1]), int(finalnewdate[2]))
                        CompleteDate = combineddate.strftime("%d/%m/%Y")
                        enddatesarray.append(CompleteDate)
                        l += 1

                    while w < 8:
                        Begindatestring = date.today()
                        newdate = Begindatestring - timedelta(days=o)
                        splitnewdate=str(newdate).split('-')
                        finalnewdate=splitnewdate[0],splitnewdate[1],splitnewdate[2]
                        combineddate = datetime.date(int(finalnewdate[0]),int(finalnewdate[1]), int(finalnewdate[2]))
                        CompleteDate = combineddate.strftime("%d/%m/%Y")
                        startdatesarray.append(CompleteDate)
                        w += 1
                        o -= 1

                    finaldatesarray = startdatesarray + enddatesarray

                    c.execute('SELECT * FROM DoublesCompetition')
                    Allrows = c.fetchall()

                    Datesarray = []
                    p = 1

                    for starting in Allrows:
                        c.execute("SELECT * FROM DoublesCompetition WHERE start_date>:realstartdate AND end_date<:realenddate AND doublescompetitionID=:ID", {
                            "realstartdate": finaldatesarray[0],
                            "realenddate": finaldatesarray[14],
                            "ID": p
                        })
                        doublerow = c.fetchone()
                        if (doublerow is None):
                            pass
                        else:
                            rowsplit = doublerow[4].split('/')
                            currentdaysplit = currentday.split('/')
                            if rowsplit[1] == currentdaysplit[1]:
                                Datesarray.append(doublerow)
                            else:
                                pass
                        p += 1

                    r = 0
                    s = 0

                    if len(Datesarray) != 0:
                        if len(Datesarray) == 1:
                            firstday = Datesarray[0][4]
                            lastday = Datesarray[0][5]
                            q = 0

                            for datevalues in finaldatesarray:
                                if finaldatesarray[q] >= firstday and finaldatesarray[q] <= lastday:
                                    q += 1
                                    pass
                                    if finaldatesarray[q] == lastday:
                                        break
                                else:
                                    finaldatesarray.remove(finaldatesarray[q])

                            finallistlength = len(finaldatesarray)
                            finallength = finallistlength - q

                            q += 1

                            for x in range(0, finallength - 1):
                                del finaldatesarray[q]

                                for allvalues in finaldatesarray:
                                    if allvalues == currentday:
                                        GotARow = True

                                break

                        else:
                            for z in range(0, len(Datesarray)):
                                firstday = Datesarray[r][4]
                                lastday = Datesarray[r][5]
                                r = 0
                                s = 0
                                q = 0

                                if z != 0:
                                    finaldatesarray.clear()
                                    finaldatesarray = startdatesarray + enddatesarray

                                for datevalues in finaldatesarray:
                                    if finaldatesarray[q] >= firstday and finaldatesarray[q] <= lastday:
                                        q += 1
                                        pass
                                        if finaldatesarray[q] == lastday:
                                            break
                                    else:
                                        finaldatesarray.remove(finaldatesarray[q])

                                finallistlength = len(finaldatesarray)
                                finallength = finallistlength - q

                                q += 1

                                for x in range(0, finallength - 1):
                                    del finaldatesarray[q]

                                for allvalues in finaldatesarray:
                                    if allvalues == currentday:
                                        GotARow = True
                                        break
                                    else:
                                        if allvalues == finaldatesarray[len(finaldatesarray) - 1]:
                                            break
                                        else:
                                            pass

                                if GotARow == True:
                                    while s != z:
                                        Datesarray.remove(Datesarray[s])
                                        s += 1
                                    break
                                else:
                                    pass

                                r += 1

                        if GotARow == True:
                            finalfirstday = Datesarray[0][4]
                            finallastday = Datesarray[0][5]

                            c.execute("SELECT * FROM DoublesCompetition WHERE end_date=:enddate AND start_date=:startdate", {
                                "enddate":finallastday,
                                "startdate": finalfirstday
                            })

                            doublesrow2 = c.fetchone()

                            if IDSelected == doublesrow2[9]:
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
                                score1_spinbox.config(state="readonly")
                                score2_spinbox.config(state="readonly")
                                submit_competition_button.place_forget()

                                doubles_submit_competition_button = tkinter.Button(self.attend, cursor="tcross",text="Submit", command=lambda : SubmitDoublesResults(doubles_submit_competition_button), fg='white', bg='black', bd=3, relief='ridge', font=('serif', 12, 'bold'))
                                doubles_submit_competition_button.place(rely=0.925, relx=0.4, anchor='center')
                                ToolTips.bind(doubles_submit_competition_button, 'Enter and submit values for the doubles competition')

                                DrawLineGraphDoubles(doubles_submit_competition_button)

                            else:
                                messagebox.showinfo('Error', 'The ID entered does not have a doubles competition on: ' + currentday, icon='error')
                        else:
                            messagebox.showinfo('Error', 'The ID entered does not have a doubles competition on: ' + currentday, icon='error')
                    else:
                        messagebox.showinfo('Error', 'There are no doubles competitions currently listed for the date: ' + currentday, icon='error')


        def DrawLineGraphSingles(singlessubmitbutton):
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
                ax1.set_xlabel('Time (Seconds)', fontdict=font)
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
                ax1.set_xlabel('Time (Seconds)', fontdict=font)
                ax1.set_ylabel('Score', fontdict=font)

                canvas = FigureCanvasTkAgg(fig, self.attend)
                canvas.get_tk_widget().place(relx=0.2,rely=0.662,anchor=CENTER)
                canvas.draw()

            if score1.get() == 21 or score2.get() == 21:
                FinishedSinglesGraph(singlessubmitbutton, canvas)


        def DrawLineGraphDoubles(doublessubmitbutton):
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
                ax1.set_xlabel('Time (Seconds)', fontdict=font)
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
                ax1.set_xlabel('Time (Seconds)', fontdict=font)
                ax1.set_ylabel('Score', fontdict=font)

                canvas = FigureCanvasTkAgg(fig, self.attend)
                canvas.get_tk_widget().place(relx=0.2,rely=0.662,anchor=CENTER)
                canvas.draw()

            if score1.get() == 21 or score2.get() == 21:
                FinishedDoublesGraph(doublessubmitbutton, canvas)


        def FinishedSinglesGraph(singlessubmitbutton, singlescanvas):
            conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
            c = conn.cursor()

            c.execute("SELECT * FROM CurrentCompetitionScores")
            row = c.fetchall()

            u = len(row)-1
            GotARow = False

            messagebox.showinfo('Info', 'Single competition with ID: ' + row[0][4] + ' has now been completed')

            finaltime = int(row[len(row)-1][3]) - int(row[0][3])

            c.execute("SELECT * FROM SinglesCompetition WHERE singlescompetitionID=:ID", {
                "ID":row[u][4]
            })
            namesrow = c.fetchone()

            c.execute("INSERT INTO FinshedCompetitions VALUES (:CompetitionType, :Member_Team_1, :Member_Team_1_Score, :Member_Team_2, :Member_Team_2_Score, :Final_time_seconds, :CurrentID)",
                      {
                          'CompetitionType': 'Singles',
                          'Member_Team_1': findfirstandsurnamemember(namesrow[0]),
                          'Member_Team_1_Score': row[len(row)-1][1],
                          'Member_Team_2': findfirstandsurnamemember(namesrow[1]),
                          'Member_Team_2_Score': row[len(row)-1][2],
                          'Final_time_seconds': finaltime,
                          'CurrentID': row[0][4],
                      })
            conn.commit()

            CompetitionType_combobox.config(state="normal")
            ID_entry.config(state="normal")
            select_competition_button.config(state="normal")
            score1_spinbox.config(state="disable")
            score2_spinbox.config(state="disable")
            CompetitionType_combobox.set('Singles')
            CompetitionID.set('')
            score1.set('0')
            score2.set('0')
            singlessubmitbutton.place_forget()
            submit_competition_button.place(rely=0.925, relx=0.4, anchor='center')
            submit_competition_button.config(state="disable")

            clearcanvas(singlescanvas)

            c.execute("SELECT * FROM FinshedCompetitions")
            row2 = c.fetchall()

            v = len(row2) - 1

            for z in (0, v):
                c.execute("SELECT * FROM FinshedCompetitions WHERE CurrentID=:ID AND CompetitionType=:Type", {
                    "ID":row2[v][6],
                    "Type": 'Singles'
                })
                singlerow = c.fetchone()
                if (singlerow is None):
                    pass
                else:
                    GotARow = True
                    break
                v -= 1

            if GotARow == True:
                StartUpFinishedSinglesGraph()

            else:
                pass


        def StartUpFinishedSinglesGraph():
            global counter

            conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
            c = conn.cursor()

            c.execute("SELECT * FROM FinshedCompetitions")
            row2 = c.fetchall()

            if len(row2) != 0:
                GotARow = False

                if row2[len(row2)-1][0] == 'Singles':
                    c.execute("SELECT * FROM FinshedCompetitions WHERE CompetitionType=:Type AND CurrentID=:ID", {
                        "Type": 'Singles',
                        "ID": row2[len(row2)-1][6]
                    })
                    singlerow = c.fetchone()
                    GotARow = True

                if GotARow == False:
                    for x in reversed(row2):
                        c.execute("SELECT * FROM FinshedCompetitions WHERE CompetitionType=:Type", {
                            "Type": 'Singles'
                        })
                        singlerow = c.fetchone()
                        if (singlerow is None):
                            pass
                        else:
                            GotARow = True
                            break

                if GotARow == True:
                    final_result_label = tkinter.Label(self.attend, text='Final Results', font=('serif', 10, 'bold', 'underline'), fg='black', bg='white')
                    final_result_label.place(rely=0.865, relx=0.592, anchor='center')

                    member1_score_label = tkinter.Label(self.attend, text='   #' + singlerow[1] + ' - ' + singlerow[2] +'#   ', font=('serif', 9, 'bold'), fg='SpringGreen3', bg='white')
                    member1_score_label.place(rely=0.905, relx=0.592, anchor='center')

                    member2_score_label = tkinter.Label(self.attend, text='   #' + singlerow[3] + ' - ' + singlerow[4] + '#   ', font=('serif', 9, 'bold'), fg='blue', bg='white')
                    member2_score_label.place(rely=0.945, relx=0.592, anchor='center')

                    text = 'ID: ' + str(singlerow[6])

                    style.use('seaborn-darkgrid')

                    font = {'family': 'serif',
                            'color':  'black',
                            'weight': 'normal',
                            'size': 16,
                            }

                    score1list = []
                    score2list = []
                    timelist = []

                    score1list.append(0)
                    score2list.append(0)
                    timelist.append(0)
                    score1list.append(singlerow[2])
                    score2list.append(singlerow[4])
                    timelist.append(singlerow[5])

                    fig = plt.figure(figsize=(3.9,3.5), dpi=60)
                    fig.tight_layout()
                    ax1 = fig.add_subplot(111)
                    if score1list[1] == '21':
                        ax1.plot(timelist, score2list, color="blue")
                        ax1.plot(timelist, score1list, color="limegreen")
                    else:
                        ax1.plot(timelist, score1list, color="limegreen")
                        ax1.plot(timelist, score2list, color="blue")
                    ax1.set_title(text, fontdict=font)
                    ax1.set_xlabel('Time (Seconds)', fontdict=font)
                    ax1.set_ylabel('Score', fontdict=font)

                    finishedcanvas = FigureCanvasTkAgg(fig, self.attend)
                    finishedcanvas.get_tk_widget().place(relx=0.592,rely=0.673,anchor=CENTER)
                    finishedcanvas.draw()

                else:
                    pass

            else:
                pass



        def FinishedDoublesGraph(doublessubmitbutton, doublescanvas):
            conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
            c = conn.cursor()

            c.execute("SELECT * FROM CurrentCompetitionScores")
            row = c.fetchall()

            u = len(row)-1
            GotARow = False

            messagebox.showinfo('Info', 'Double competition with ID: ' + row[0][4] + ' has now been completed')

            finaltime = int(row[len(row)-1][3]) - int(row[0][3])

            c.execute("SELECT * FROM DoublesCompetition WHERE doublescompetitionID=:ID", {
                "ID":row[u][4]
            })
            namesrow = c.fetchone()

            c.execute("INSERT INTO FinshedCompetitions VALUES (:CompetitionType, :Member_Team_1, :Member_Team_1_Score, :Member_Team_2, :Member_Team_2_Score, :Final_time_seconds, :CurrentID)",
                      {
                          'CompetitionType': 'Doubles',
                          'Member_Team_1': namesrow[7],
                          'Member_Team_1_Score': row[len(row)-1][1],
                          'Member_Team_2': namesrow[8],
                          'Member_Team_2_Score': row[len(row)-1][2],
                          'Final_time_seconds': finaltime,
                          'CurrentID': row[0][4],
                      })
            conn.commit()

            CompetitionType_combobox.config(state="normal")
            ID_entry.config(state="normal")
            select_competition_button.config(state="normal")
            score1_spinbox.config(state="disable")
            score2_spinbox.config(state="disable")
            CompetitionType_combobox.set('Singles')
            CompetitionID.set('')
            score1.set('0')
            score2.set('0')
            doublessubmitbutton.place_forget()
            submit_competition_button.place(rely=0.925, relx=0.4, anchor='center')
            submit_competition_button.config(state="disable")

            clearcanvas(doublescanvas)

            c.execute("SELECT * FROM FinshedCompetitions")
            row2 = c.fetchall()

            v = len(row2) - 1

            for z in (0, v):
                c.execute("SELECT * FROM FinshedCompetitions WHERE CurrentID=:ID AND CompetitionType=:Type", {
                    "ID":row2[v][6],
                    "Type": 'Doubles'
                })
                doublerow = c.fetchone()
                if (doublerow is None):
                    pass
                else:
                    GotARow = True
                    break
                v -= 1

            if GotARow == True:
                StartUpFinishedDoublesGraph()

            else:
                pass


        def StartUpFinishedDoublesGraph():
            conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
            c = conn.cursor()

            c.execute("SELECT * FROM FinshedCompetitions")
            row2 = c.fetchall()

            if len(row2) != 0:
                GotARow = False

                if row2[len(row2)-1][0] == 'Doubles':
                    c.execute("SELECT * FROM FinshedCompetitions WHERE CompetitionType=:Type AND CurrentID=:ID", {
                        "Type": 'Doubles',
                        "ID": row2[len(row2)-1][6]
                    })
                    doublerow = c.fetchone()
                    GotARow = True

                if GotARow == False:
                    for x in reversed(row2):
                        c.execute("SELECT * FROM FinshedCompetitions WHERE CompetitionType=:Type", {
                            "Type": 'Doubles'
                        })
                        doublerow = c.fetchone()
                        if (doublerow is None):
                            pass
                        else:
                            GotARow = True
                            break

                if GotARow == True:
                    final_result_label = tkinter.Label(self.attend, text='Final Results', font=('serif', 10, 'bold', 'underline'), fg='black', bg='white')
                    final_result_label.place(rely=0.865, relx=0.848, anchor='center')

                    member1_score_label = tkinter.Label(self.attend, text='   #' + doublerow[1] + ' - ' + doublerow[2] + '#   ', font=('serif', 9, 'bold'), fg='SpringGreen3', bg='white')
                    member1_score_label.place(rely=0.905, relx=0.848, anchor='center')

                    member2_score_label = tkinter.Label(self.attend, text='   #' + doublerow[3] + ' - ' + doublerow[4] + '#   ', font=('serif', 9, 'bold'), fg='blue', bg='white')
                    member2_score_label.place(rely=0.945, relx=0.848, anchor='center')

                    text = 'ID: ' + str(doublerow[6])

                    style.use('seaborn-darkgrid')

                    font = {'family': 'serif',
                            'color':  'black',
                            'weight': 'normal',
                            'size': 16,
                            }

                    score1list = []
                    score2list = []
                    timelist = []

                    score1list.append(0)
                    score2list.append(0)
                    timelist.append(0)
                    score1list.append(doublerow[2])
                    score2list.append(doublerow[4])
                    timelist.append(doublerow[5])

                    fig = plt.figure(figsize=(3.9,3.5), dpi=60)
                    fig.tight_layout()
                    ax1 = fig.add_subplot(111)
                    if score1list[1] == '21':
                        ax1.plot(timelist, score2list, color="blue")
                        ax1.plot(timelist, score1list, color="limegreen")
                    else:
                        ax1.plot(timelist, score1list, color="limegreen")
                        ax1.plot(timelist, score2list, color="blue")
                    ax1.set_title(text, fontdict=font)
                    ax1.set_xlabel('Time (Seconds)', fontdict=font)
                    ax1.set_ylabel('Score', fontdict=font)

                    finishedcanvas = FigureCanvasTkAgg(fig, self.attend)
                    finishedcanvas.get_tk_widget().place(relx=0.848,rely=0.673,anchor=CENTER)
                    finishedcanvas.draw()

                else:
                    pass

            else:
                pass


        def SubmitSinglesResults(singlessubmitbutton):
            member_team1_score = score1.get()
            member_team2_score = score2.get()
            currentTime = int(time.time())

            isValid = True
            isValid = isValid and validate_member_team_score(member_team1_score, member_team2_score)

            if isValid:
                conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
                c = conn.cursor()

                c.execute("SELECT * FROM CurrentCompetitionScores")
                Row = c.fetchall()

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

                DrawLineGraphSingles(singlessubmitbutton)


        def SubmitDoublesResults(doublessubmitbutton):
            member_team1_score = score1.get()
            member_team2_score = score2.get()
            currentTime = int(time.time())

            isValid = True
            isValid = isValid and validate_member_team_score(member_team1_score, member_team2_score)

            if isValid:
                conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
                c = conn.cursor()

                c.execute("SELECT * FROM CurrentCompetitionScores")
                Row = c.fetchall()

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

                DrawLineGraphDoubles(doublessubmitbutton)


        CompetitionID = IntVar()
        score1=IntVar()
        score2=IntVar()


        CompetitionType = ['Singles','Doubles']

        ToolTips = Pmw.Balloon()


        conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
        c = conn.cursor()

        c.execute("DELETE FROM CurrentCompetitionScores")

        conn.commit()
        conn.close()


        competitiontype_label = tkinter.Label(self.attend, text="Type:", font=('serif', 14, 'bold'), fg='black', bg='white')
        competitiontype_label.place(rely=0.41, relx=0.07, anchor='center')

        CompetitionType_combobox = ttk.Combobox(self.attend, value=CompetitionType, font=('serif', 11, 'bold'), width=7)
        CompetitionType_combobox.place(rely=0.413, relx=0.15, anchor='center')
        CompetitionType_combobox.current(0)
        CompetitionType_combobox.config(state="readonly")

        id_label = tkinter.Label(self.attend, text="ID:", font=('serif', 14, 'bold'), fg='black', bg='white')
        id_label.place(rely=0.41, relx=0.245, anchor='center')

        ID_entry = tkinter.Entry(self.attend, width=6, textvariable=CompetitionID, bd=3, relief='ridge', cursor="tcross", font=('serif', 12, 'bold'))
        ID_entry.place(rely=0.412, relx=0.3, anchor='center')
        CompetitionID.set('')
        ID_entry.insert(0, 'e.g. 3')
        ID_entry.bind('<FocusIn>', ID_click)
        ID_entry.bind('<FocusOut>', ID_unclick)
        ID_entry.config(fg='grey')

        select_competition_button = tkinter.Button(self.attend, cursor="tcross",text="Select", command=SelectTypeandID, fg='white', bg='black', bd=3, relief='ridge', font=('serif', 11, 'bold'))
        select_competition_button.place(rely=0.415, relx=0.4, anchor='center')
        ToolTips.bind(select_competition_button, 'Confirm ID and competition type')


        score1_label = tkinter.Label(self.attend, text="Member/Team Score 1:", font=('serif', 14, 'bold'), fg='black', bg='white')
        score1_label.place(rely=0.9, relx=0.135, anchor='center')

        score1_spinbox = Spinbox(self.attend, width=6,font=("serif",12, 'bold'), bd=3, relief='ridge', cursor="tcross",textvariable=score1, values=('0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21'))
        score1_spinbox.place(rely=0.9, relx=0.3, anchor='center')
        score1_spinbox.config(state='readonly')


        score2_label = tkinter.Label(self.attend, text="Member/Team Score 2:", font=('serif', 14, 'bold'), fg='black', bg='white')
        score2_label.place(rely=0.96, relx=0.135, anchor='center')

        score2_spinbox = Spinbox(self.attend, width=6,font=("serif",12, 'bold'), bd=3, relief='ridge', cursor="tcross",textvariable=score2, values=('0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21'))
        score2_spinbox.place(rely=0.96, relx=0.3, anchor='center')
        score2_spinbox.config(state='readonly')

        submit_competition_button = tkinter.Button(self.attend, cursor="tcross",text="Submit", command=SubmitSinglesResults, fg='white', bg='black', bd=3, relief='ridge', font=('serif', 12, 'bold'))
        submit_competition_button.place(rely=0.925, relx=0.4, anchor='center')
        ToolTips.bind(submit_competition_button, 'Enter and submit values for the competition')


        title_label =Label(self.attend, text = "Most Recent Matches (Sketch)", fg ='black',bg='white',font=('serif',11,'bold'), bd=2, relief="ridge", padx=5, pady=2)
        title_label.place(rely=0.435,relx=0.72,anchor=CENTER)

        box =Label(self.attend, text = "blank", fg ='white',bg='white',font=('serif',8,'bold'), bd=2, relief="sunken", padx=230, pady=160)
        box.place(rely=0.71,relx=0.72,anchor=CENTER)

        boxsplitvertical =Label(self.attend, text = "b", fg ='white',bg='white',font=('serif',8,'bold'), bd=2, relief="ridge", padx=1, pady=158.5)
        boxsplitvertical.place(rely=0.711,relx=0.72,anchor=CENTER)

        box_singles_title = tkinter.Label(self.attend, text="Most Recent Singles Match", font=('serif', 10, 'bold'), fg='black', bg='white')
        box_singles_title.place(rely=0.479, relx=0.595, anchor='center')

        box_doubles_title = tkinter.Label(self.attend, text="Most Recent Doubles Match", font=('serif', 10, 'bold'), fg='black', bg='white')
        box_doubles_title.place(rely=0.479, relx=0.847, anchor='center')

        boxsplithorizontal =Label(self.attend, text = "b", fg ='white',bg='white',font=('serif',1), bd=2, relief="ridge", padx=244, pady=0.5)
        boxsplithorizontal.place(rely=0.505,relx=0.72,anchor=CENTER)


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


        score1_spinbox.config(state="disable")
        score2_spinbox.config(state="disable")
        submit_competition_button.config(state="disable")


        UnplayedSinglesPopulate()
        UnplayedDoublesPopulate()
        StartUpFinishedSinglesGraph()
        StartUpFinishedDoublesGraph()

