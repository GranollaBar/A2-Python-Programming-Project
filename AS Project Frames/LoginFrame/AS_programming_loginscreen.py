# Login Screen

import tkinter
from tkinter import messagebox
import random
import tkinter.simpledialog
from tkinter.messagebox import showinfo
from tkinter.messagebox import askyesno
import sqlite3
from tkinter import *
import webbrowser
from MainScreens.ChangingPasswordEmail import ChangePassword
import Pmw
from datetime import datetime
import datetime



# Login Class
class LoginContent:

    # will store the username of the user entering the system
    def getloginname(self):
        return self.finalloginname

    # Initiates main screen window
    def __init__(self, mainScreen):
        self.finalloginname = ''

        self.login = mainScreen
        self.conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
        self.c = self.conn.cursor()


        # Creates account database table if it does not exist
        self.c.execute("""CREATE TABLE IF NOT EXISTS account (
                        username text,
                        password text,
                        status text
                        )""")

        # Creates manager database table if it does not exist
        self.c.execute("""CREATE TABLE IF NOT EXISTS manager (
                        username text,
                        password text,
                        firstname text,
                        surname text
                        )""")

        # Creates fees database table if it does not exist
        self.c.execute("""CREATE TABLE IF NOT EXISTS fees (
                        username text,
                        coachingsessionfee text,
                        memberbookingfee text
                        )""")


    # Generate login content
    def generateLoginContnt(self):

        # Ensures password entered conforms to the rules
        def validate_password(value, label):
            if value is None:
                return False
            if (value == 'e.g. password123'):
                label.config(fg="red")
                messagebox.showinfo("Validation Error", "The password field cannot be empty", icon='error')
                return False
            if (value == ''):
                label.config(fg="red")
                messagebox.showinfo("Validation Error", "The password field cannot be empty", icon='error')
                return False
            if (len(value) < 8):
                label.config(fg="red")
                messagebox.showinfo("Validation Error", "The password field must contain more than 7 characters", icon='error')
                return False
            if (len(value) > 15):
                label.config(fg="red")
                messagebox.showinfo("Validation Error", "The password field must contain less than 16 characters", icon='error')
                return False

            label.config(fg="SpringGreen3")
            return True


        # Ensures username entered conforms to the rules
        def validate_username(value, label):
            if value is None:
                return False
            if (value == 'e.g. greg@gmail.com'):
                label.config(fg="red")
                messagebox.showinfo("Validation Error", "The username field cannot be empty", icon='error')
                return False
            if value == '':
                label.config(fg="red")
                messagebox.showinfo("Validation Error", "The username field cannot be empty", icon='error')
                return False
            if ('@' not in value):
                label.config(fg="red")
                messagebox.showinfo("Validation Error", "The username field must contain @", icon='error')
                return False
            if ('.' not in value):
                label.config(fg="red")
                messagebox.showinfo("Validation Error", "The username field must contain a .", icon='error')
                return False

            label.config(fg="SpringGreen3")
            return True


        # Ensures username entered  for email conforms to the rules
        def validate_username2(value):
            if value is None:
                return False
            if (value == ''):
                messagebox.showinfo("Validation Error", "The username field cannot be empty", icon='error')
                return False
            if ('@' not in value):
                messagebox.showinfo("Validation Error", "The username field must contain @", icon='error')
                return False
            if ('.' not in value):
                messagebox.showinfo("Validation Error", "The username field must contain a .", icon='error')
                return False

            return True


        # Ensures firstname entered conforms to the rules
        def validate_firstname(value, label):
            if value is None:
                return False
            if (value == 'e.g. joe'):
                label.config(fg="red")
                messagebox.showinfo("Validation Error", "The username field cannot be empty", icon='error')
                return False
            if (value == ''):
                label.config(fg="red")
                messagebox.showinfo("Validation Error", "The firstname field cannot be empty", icon='error')
                return False
            if (len(value) > 15):
                label.config(fg="red")
                messagebox.showinfo("Validation Error", "The firstname field have more than 15 characters", icon='error')
                return False

            label.config(fg="SpringGreen3")
            return True


        # Ensures surname entered conforms to the rules
        def validate_surname(value, label):
            if value is None:
                return False
            if (value == 'e.g. jones'):
                label.config(fg="red")
                messagebox.showinfo("Validation Error", "The surname field cannot be empty", icon='error')
                return False
            if (value == ''):
                label.config(fg="red")
                messagebox.showinfo("Validation Error", "The surname field cannot be empty", icon='error')
                return False
            if (len(value) > 15):
                label.config(fg="red")
                messagebox.showinfo("Validation Error", "The surname field have more than 15 characters", icon='error')
                return False

            label.config(fg="SpringGreen3")
            return True


        # An existent user can create a new password if they have forgotten their old password
        # An email will be sent to the user containing the verification code
        def forgot_system():
            conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
            c = conn.cursor()

            recipient = tkinter.simpledialog.askstring("Response","Enter the username of the user's password you want to change")

            isValid = True
            isValid = isValid and validate_username2(recipient)

            if isValid:

                c.execute(f"SELECT * FROM account WHERE username =?", (recipient,))
                data = c.fetchone()
                if not data:
                    messagebox.showinfo("Error", "The username entered was not found in the database", icon='error')

                else:

                    verification = IntVar()
                    newpassword = StringVar()
                    verificationCode = random.randint(100000,999999)

                    found = ChangePassword("Lisburn Racquets Verification code","\n" + "This is an automated message sent from Lisburn Racquet's Club" + "\n" + "The verification code to change your passwords is: " + "\n\n" + str(verificationCode) + "\n\n" + "Please do not respond to this email",finalname)
                    if found:

                        email_toplevel=Toplevel(width=300, height=200, bg="white")

                        title_label = tkinter.Label(email_toplevel, text="Forgot Password System", font=('Verdana', 14, 'underline', 'bold'), fg='SpringGreen3', bg='white')
                        title_label.place(rely=0.125, relx=0.5, anchor='center')

                        verification_label = Label(email_toplevel,text = 'Verification Code:', fg ='black', bg='white', font = ('Verdana',12,'bold'))
                        verification_label.place(rely=0.4,relx=0.3,anchor=CENTER)

                        newpassword_label = Label(email_toplevel,text = 'New Password:', fg ='black', bg='white', font = ('Verdana',12,'bold'))
                        newpassword_label.place(rely=0.6,relx=0.3,anchor=CENTER)

                        verification_entry = Entry(email_toplevel,width=15, borderwidth=2, textvariable=verification)
                        verification_entry.place(rely=0.403,relx=0.8,anchor=CENTER)
                        verification.set('')

                        newpassword_entry = Entry(email_toplevel,width=15, borderwidth=2, textvariable=newpassword)
                        newpassword_entry.place(rely=0.603,relx=0.8,anchor=CENTER)

                        def completeVerification():
                            newPasswordUpdate(newpassword.get(), verificationCode, verification.get(), email_toplevel, verification, newpassword, finalname)

                        newpassword_button=Button(email_toplevel,text = 'Update Password', command = completeVerification, fg ='white', bg='black', relief= 'groove', font = ('Verdana',10,'bold'), padx =20)
                        newpassword_button.place(rely=0.85,relx=0.5,anchor=CENTER)
                        ToolTips.bind(newpassword_button, 'Updates the password to the new one inputted')

                        email_toplevel.destroy()


        # Password will be validated and then will be updated for the user
        def newPasswordUpdate(newPassword, verificationCode, verification_entry, frame, value, value2, finalname):
            conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
            c = conn.cursor()

            if verification_entry != verificationCode:
                messagebox.showinfo("Error","The verification code entered was wrong compared to the one sent to the users email", icon='error')
            elif newPassword == '' or newPassword.isnumeric() == True or len(newPassword) >15 and len(newPassword) <8:
                messagebox.showinfo("Error","The password entered did not comply with the rules", icon='error')

            else:
                c.execute(f"SELECT * FROM account WHERE username=?", (finalname,))
                data = c.fetchone()

                c.execute("""UPDATE account SET password = :newPassword WHERE username=:username""", {
                    "newPassword": newPassword,
                    "username": finalname
                })

                if (data[2] == 'member'):
                    c.execute("""UPDATE member SET password = :newPassword WHERE username=:username""", {
                        "newPassword": newPassword,
                        "username": finalname
                    })

                if (data[2] == 'coach'):
                    c.execute("""UPDATE coach SET password = :newPassword WHERE username=:username""", {
                        "newPassword": newPassword,
                        "username": finalname
                    })

                if (data[2] == 'manager'):
                    c.execute("""UPDATE manager SET password = :newPassword WHERE username=:username""", {
                        "newPassword": newPassword,
                        "username": finalname
                    })

                frame.destroy()
                messagebox.showinfo("Info", "The users password is now "+newPassword, icon='info')
                value.set('')
                value2.set('')

            conn.commit()
            conn.close()


        # This will only occur for the first user entering the system (i.e. manager)
        # The first user in the system will be assigned management
        def first_login_submit(username, password, firstname, surname):
            conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
            c = conn.cursor()

            isValid = True
            isValid = isValid and validate_username(username, username_label)
            isValid = isValid and validate_password(password, password_label)
            isValid = isValid and validate_firstname(firstname, firstname_label)
            isValid = isValid and validate_surname(surname, surname_label)

            if isValid:
                c.execute("INSERT INTO manager VALUES (:username, :password, :firstname, :surname)",
                          {
                              'username': username,
                              'password': password,
                              'firstname': firstname,
                              'surname': surname,
                          })

                c.execute("INSERT INTO account VALUES (:username, :password, :status)",
                          {
                              'username': username,
                              'password': password,
                              'status': 'manager',
                          })

                messagebox.showinfo("Info", "Manager account created for " + firstname + " " + surname, icon='info')
                messagebox.showinfo("Info", "Login Successful", icon='info')

                username_label.config(fg="black")
                password_label.config(fg="black")
                firstname_label.config(fg="black")
                surname_label.config(fg="black")

                loginUsername.set('')
                loginPassword.set('')
                loginfirstname.set('')
                loginsurname.set('')

                self.login.destroy()

                conn.commit()
                conn.close()

                from MainScreens import ManagerMainScreen
                ManagerMainScreen.passLoginScreen(self)
                ManagerMainScreen.main()


        # Login Details entered will be submitted to ensure the entered username and password exist in the system
        # The user will be logged in based on their system level
        def login_submit(login_username, login_password):
            conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
            c = conn.cursor()

            isValid = True
            isValid = isValid and validate_username(login_username, username_label)
            isValid = isValid and validate_password(login_password, password_label)

            if isValid:
                c.execute(f"SELECT * FROM account WHERE username =? and password =?", (login_username, login_password,))
                data = c.fetchone()
                if not data:
                    username_label.config(fg="red")
                    password_label.config(fg="red")
                    messagebox.showinfo("Error", "The coach with username " + login_username + " and password " + login_password + " was not found in the database", icon='error')

                else:

                    messagebox.showinfo("Info", "Login Successful", icon='info')

                    username_label.config(fg="black")
                    password_label.config(fg="black")

                    loginUsername.set('')
                    loginPassword.set('')

                    self.login.destroy()

                    if (data[2] == 'member'):
                        from MainScreens import MemberMainScreen
                        MemberMainScreen.passLoginScreen(self)
                        MemberMainScreen.main()


                    if (data[2] == 'coach'):
                        from MainScreens import CoachMainScreen
                        CoachMainScreen.passLoginScreen(self)
                        CoachMainScreen.main()


                    if (data[2] == 'manager'):
                        from MainScreens import ManagerMainScreen
                        ManagerMainScreen.passLoginScreen(self)
                        ManagerMainScreen.main()


            conn.commit()
            conn.close()


        # Will clear all details inputted into the login screen
        def login_clear():
            response = askyesno("Question", "Do you want to clear all details entered so far", icon='question')
            if response == False:
                showinfo("Info", "clearance cancelled", icon='info')

            else:

                loginUsername.set('')
                loginPassword.set('')


        # This will remove all coaching session, member bookings and competitions made in the system that have expired
        # It will place these events in the database table: PastEvents and delete them from their respective tables
        def RemoveDates():
            presentDate = datetime.datetime.now()
            today=datetime.datetime(int(presentDate.year),int(presentDate.month),int(presentDate.day))

            conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
            c = conn.cursor()

            c.execute("SELECT * From coachSessionDetails")
            coachitems = c.fetchall()

            for row in coachitems:
                coachrowsplitdate = str(row[3]).split('/')
                coachdate=datetime.datetime(int(coachrowsplitdate[2]),int(coachrowsplitdate[1]),int(coachrowsplitdate[0]))

                if (coachdate < today)==True:
                    c.execute("INSERT INTO PastEvents VALUES (:username, :event, :date, :status)",
                              {
                                  'username': row[0],
                                  'event': 'Coaching Session',
                                  'date': row[3],
                                  'status': 'coach/member',
                              })

                    c.execute('DELETE FROM coachSessionDetails WHERE sessionID=:ID', {
                        "ID": row[8]
                    })

            c.execute("SELECT * From SinglesCompetition")
            singlesitems = c.fetchall()

            for items in singlesitems:
                singlesrowsplitdate = str(items[3]).split('/')
                singlesdate=datetime.datetime(int(singlesrowsplitdate[2]),int(singlesrowsplitdate[1]),int(singlesrowsplitdate[0]))

                if (singlesdate < today)==True:
                    c.execute("INSERT INTO PastEvents VALUES (:username, :event, :date, :status)",
                              {
                                  'username': items[0],
                                  'event': 'Singles Competition',
                                  'date': items[3],
                                  'status': 'coach/member',
                              })

                    c.execute('DELETE FROM SinglesCompetition WHERE singlescompetitionID=:ID', {
                        "ID": items[5]
                    })

            c.execute("SELECT * From DoublesCompetition")
            doublesitems = c.fetchall()

            for values in doublesitems:
                doublesrowsplitdate = str(values[3]).split('/')
                doublesdate=datetime.datetime(int(doublesrowsplitdate[2]),int(doublesrowsplitdate[1]),int(doublesrowsplitdate[0]))

                if (doublesdate < today)==True:
                    c.execute("INSERT INTO PastEvents VALUES (:username, :event, :date, :status)",
                              {
                                  'username': values[0],
                                  'event': 'Doubles Competition',
                                  'date': values[3],
                                  'status': 'coach/member'
                              })

                    c.execute('DELETE FROM DoublesCompetition WHERE doublescompetitionID=:ID', {
                        "ID": values[9]
                    })

            c.execute("SELECT * From MemberBooking")
            bookingitems = c.fetchall()

            for data in bookingitems:
                bookingrowsplitdate = str(data[3]).split('/')
                bookingdate=datetime.datetime(int(bookingrowsplitdate[2]),int(bookingrowsplitdate[1]),int(bookingrowsplitdate[0]))

                if (bookingdate < today)==True:
                    c.execute("INSERT INTO PastEvents VALUES (:username, :event, :date, :status)",
                              {
                                  'username': data[1],
                                  'event': 'Member Booking',
                                  'date': data[3],
                                  'status': 'member'
                              })

                    c.execute('DELETE FROM MemberBooking WHERE bookingID=:ID', {
                        "ID": data[5]
                    })

            conn.commit()
            conn.close()


        # Will add and remove placeholder text into the username entry box
        def username_click(event):
            if username_entry.get() == 'e.g. greg@gmail.com':
                username_entry.delete(0, "end")
                username_entry.insert(0, '')
                username_entry.config(fg='black')

        def username_unclick(event):
            if username_entry.get() == '':
                username_entry.insert(0, 'e.g. greg@gmail.com')
                username_entry.config(fg='grey')


        # Will add and remove placeholder text into the password entry box
        def password_click(event):
            if password_entry.get() == 'e.g. password123':
                password_entry.delete(0, "end")
                password_entry.insert(0, '')
                password_entry.config(fg='black')
                password_entry.config(show="*")

        def password_unclick(event):
            if password_entry.get() == '':
                password_entry.config(show="")
                password_entry.insert(0, 'e.g. password123')
                password_entry.config(fg='grey')


        # Will add and remove placeholder text into the first name entry box
        def firstname_click(event):
            if firstname_entry.get() == 'e.g. joe':
                firstname_entry.delete(0, "end")
                firstname_entry.insert(0, '')
                firstname_entry.config(fg='black')

        def firstname_unclick(event):
            if firstname_entry.get() == '':
                firstname_entry.config(show="")
                firstname_entry.insert(0, 'e.g. joe')
                firstname_entry.config(fg='grey')


        # Will add and remove placeholder text into the surname entry box
        def surname_click(event):
            if surname_entry.get() == 'e.g. jones':
                surname_entry.delete(0, "end")
                surname_entry.insert(0, '')
                surname_entry.config(fg='black')

        def surname_unclick(event):
            if surname_entry.get() == '':
                surname_entry.config(show="")
                surname_entry.insert(0, 'e.g. jones')
                surname_entry.config(fg='grey')


        # Shows the password entered in plain text
        def show_password(self):
            password_entry.config(show="")


        # Shows the password entered as stars
        def dont_show_password(self):
            if password_entry.get() != 'e.g. password123':
                password_entry.config(show="*")
            else:
                password_entry.config(show="")


        # Links to Lisburn Racquets Club twitter account
        def twitterLink():
            webbrowser.open("https://twitter.com/lisburnracquets")


        # Links to Lisburn Racquets Club facebook account
        def facebookLink():
            webbrowser.open("https://www.facebook.com/LisburnRacquetsClub")



        conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
        c = conn.cursor()

        c.execute("SELECT * FROM account")
        row = c.fetchall()

        # Variables used
        loginUsername = StringVar()
        loginPassword = StringVar()
        loginfirstname = StringVar()
        loginsurname = StringVar()

        ToolTips = Pmw.Balloon()


        # Tkinter labels, entry boxes, buttons, tree views, etc.
        if len(row) != 0:
            title_label = tkinter.Label(self.login, text="Welcome To Lisburn Racquets Club", font=('serif', 18, 'underline', 'bold'), fg='SpringGreen3', bg='white')
            title_label.place(rely=0.06, relx=0.5, anchor='center')

            username_label = tkinter.Label(self.login, text="Username:", font=('serif', 18, 'bold'),fg='black', bg='white')
            username_label.place(rely=0.45, relx=0.295, anchor='center')

            password_label = tkinter.Label(self.login, text="Password:", font=('serif', 18, 'bold'), fg='black', bg='white')
            password_label.place(rely=0.6, relx=0.3, anchor='center')


            username_entry = tkinter.Entry(self.login, width=30, textvariable=loginUsername, bd=4, relief='ridge', cursor="tcross")
            username_entry.place(rely=0.454, relx=0.655, anchor='center')
            username_entry.insert(0, 'e.g. greg@gmail.com')
            username_entry.bind('<FocusIn>', username_click)
            username_entry.bind('<FocusOut>', username_unclick)
            username_entry.config(fg='grey')

            password_entry = tkinter.Entry(self.login, width=30, textvariable=loginPassword, bd=4, relief='ridge', cursor="tcross")
            password_entry.place(rely=0.604, relx=0.655, anchor='center')
            password_entry.insert(0, 'e.g. password123')
            password_entry.bind('<FocusIn>', password_click)
            password_entry.bind('<FocusOut>', password_unclick)
            password_entry.config(fg='grey')


            twitterImage = PhotoImage(file="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Images/twitter.png")
            facebookImage = PhotoImage(file="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Images/facebook.png")
            passwordImage = PhotoImage(file="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Images/eye.png")
            notpasswordImage = PhotoImage(file="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Images/noteye.png")


            twitterButton = Button(self.login, cursor="tcross", image=twitterImage, width=75, height=75, command=twitterLink, bg="white", highlightthickness=2, activebackground="grey")
            twitterButton.place(rely=0.25,relx=0.86,anchor=CENTER)
            twitterButton.image = twitterImage
            ToolTips.bind(twitterButton, 'Follow link to Lisburn Racquets Club Twitter')

            facebookButton = Button(self.login, cursor="tcross", image=facebookImage, width=74, height=74, command=facebookLink, bg="white", highlightthickness=2, activebackground="grey")
            facebookButton.place(rely=0.25,relx=0.14,anchor=CENTER)
            facebookButton.image = facebookImage
            ToolTips.bind(facebookButton, 'Follow link to Lisburn Racquets Club Facebook')

            passwordButton = Button(self.login, cursor="tcross", image=passwordImage, width=20, height=20, bg="white", highlightthickness=2, activebackground="grey")
            passwordButton.place(rely=0.604,relx=0.885,anchor=CENTER)
            passwordButton.image = passwordImage
            passwordButton.bind("<ButtonRelease-1>", show_password)

            notpasswordButton = Button(self.login, cursor="tcross", image=notpasswordImage, width=20, height=20, bg="white", highlightthickness=2, activebackground="grey")
            notpasswordButton.place(rely=0.604,relx=0.955,anchor=CENTER)
            notpasswordButton.image = notpasswordImage
            notpasswordButton.bind("<ButtonRelease-1>", dont_show_password)


            background_entry_canvas = Canvas(self.login,width=218, height=130, bg = "white")
            background_entry_canvas.place(rely=0.26,relx=0.5,anchor=CENTER)

            background_entry_image = PhotoImage(file ="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Images/lisburnraquetsclub.png")

            background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
            background_entry_canvas.background_entry_image = background_entry_image


            forgot_password_button = tkinter.Button(self.login, cursor="tcross", text="Forgot Password", command=forgot_system, fg='white', bg='black', bd=6, relief='ridge', font=('serif', 12, 'bold'), padx=10)
            forgot_password_button.place(rely=0.7, relx=0.5, anchor='center')
            ToolTips.bind(forgot_password_button, 'Create a new password to enter the system')

            clear_button = tkinter.Button(self.login, cursor="tcross", text="Clear", command=login_clear, fg='white', bg='black', bd=6, relief='groove', font=('serif', 16, 'bold'), padx=50)
            clear_button.place(rely=0.9, relx=0.27, anchor='center')
            ToolTips.bind(clear_button, 'Clears data entered')

            def completeLogin():
                self.finalloginname = loginUsername.get()
                login_submit(loginUsername.get(), loginPassword.get())

            login_button = tkinter.Button(self.login, cursor="tcross",text="Login", command=completeLogin, fg='white', bg='black', bd=6, relief='groove', font=('serif', 16, 'bold'), padx=50)
            login_button.place(rely=0.9, relx=0.73, anchor='center')
            ToolTips.bind(login_button, 'Login to the system')


        else:


            title_label = tkinter.Label(self.login, text="Welcome To Lisburn Racquets Club", font=('serif', 18, 'underline', 'bold'), fg='SpringGreen3', bg='white')
            title_label.place(rely=0.06, relx=0.5, anchor='center')

            username_label = tkinter.Label(self.login, text="Username:", font=('serif', 12, 'bold'),fg='black', bg='white')
            username_label.place(rely=0.45, relx=0.295, anchor='center')

            password_label = tkinter.Label(self.login, text="Password:", font=('serif', 12, 'bold'), fg='black', bg='white')
            password_label.place(rely=0.55, relx=0.3, anchor='center')

            firstname_label = tkinter.Label(self.login, text="Firstname:", font=('serif', 12, 'bold'), fg='black', bg='white')
            firstname_label.place(rely=0.65, relx=0.295, anchor='center')

            surname_label = tkinter.Label(self.login, text="Surname:", font=('serif', 12, 'bold'), fg='black', bg='white')
            surname_label.place(rely=0.75, relx=0.295, anchor='center')


            username_entry = tkinter.Entry(self.login, width=30, textvariable=loginUsername, bd=2, relief='ridge', cursor="tcross")
            username_entry.place(rely=0.454, relx=0.655, anchor='center')
            username_entry.insert(0, 'e.g. greg@gmail.com')
            username_entry.bind('<FocusIn>', username_click)
            username_entry.bind('<FocusOut>', username_unclick)
            username_entry.config(fg='grey')

            password_entry = tkinter.Entry(self.login, width=30, textvariable=loginPassword, bd=2, relief='ridge', cursor="tcross")
            password_entry.place(rely=0.554, relx=0.655, anchor='center')
            password_entry.insert(0, 'e.g. password123')
            password_entry.bind('<FocusIn>', password_click)
            password_entry.bind('<FocusOut>', password_unclick)
            password_entry.config(fg='grey')

            firstname_entry = tkinter.Entry(self.login, width=17, textvariable=loginfirstname, bd=2, relief='ridge', cursor="tcross")
            firstname_entry.place(rely=0.654, relx=0.655, anchor='center')
            firstname_entry.insert(0, 'e.g. joe')
            firstname_entry.bind('<FocusIn>', firstname_click)
            firstname_entry.bind('<FocusOut>', firstname_unclick)
            firstname_entry.config(fg='grey')

            surname_entry = tkinter.Entry(self.login, width=17, textvariable=loginsurname, bd=2, relief='ridge', cursor="tcross")
            surname_entry.place(rely=0.754, relx=0.655, anchor='center')
            surname_entry.insert(0, 'e.g. jones')
            surname_entry.bind('<FocusIn>', surname_click)
            surname_entry.bind('<FocusOut>', surname_unclick)
            surname_entry.config(fg='grey')


            twitterImage = PhotoImage(file="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Images/twitter.png")
            facebookImage = PhotoImage(file="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Images/facebook.png")
            passwordImage = PhotoImage(file="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Images/eye.png")
            notpasswordImage = PhotoImage(file="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Images/noteye.png")


            twitterButton = Button(self.login, cursor="tcross", image=twitterImage, width=75, height=75, command=twitterLink, bg="white", highlightthickness=2, activebackground="grey")
            twitterButton.place(rely=0.25,relx=0.86,anchor=CENTER)
            twitterButton.image = twitterImage
            ToolTips.bind(twitterButton, 'Follow link to Lisburn Racquets Club Twitter')

            facebookButton = Button(self.login, cursor="tcross", image=facebookImage, width=74, height=74, command=facebookLink, bg="white", highlightthickness=2, activebackground="grey")
            facebookButton.place(rely=0.25,relx=0.14,anchor=CENTER)
            facebookButton.image = facebookImage
            ToolTips.bind(facebookButton, 'Follow link to Lisburn Racquets Club Facebook')

            passwordButton = Button(self.login, cursor="tcross", image=passwordImage, width=20, height=20, bg="white", highlightthickness=2, activebackground="grey")
            passwordButton.place(rely=0.554,relx=0.885,anchor=CENTER)
            passwordButton.image = passwordImage
            passwordButton.bind("<ButtonRelease-1>", show_password)

            notpasswordButton = Button(self.login, cursor="tcross", image=notpasswordImage, width=20, height=20, bg="white", highlightthickness=2, activebackground="grey")
            notpasswordButton.place(rely=0.554,relx=0.955,anchor=CENTER)
            notpasswordButton.image = notpasswordImage
            notpasswordButton.bind("<ButtonRelease-1>", dont_show_password)


            background_entry_canvas = Canvas(self.login,width=218, height=130, bg = "white")
            background_entry_canvas.place(rely=0.26,relx=0.5,anchor=CENTER)

            background_entry_image = PhotoImage(file ="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Images/lisburnraquetsclub.png")

            background_entry_canvas.create_image(0,0, anchor = NW, image=background_entry_image)
            background_entry_canvas.background_entry_image = background_entry_image


            clear_button = tkinter.Button(self.login, cursor="tcross", text="Clear", command=login_clear, fg='white', bg='black', bd=6, relief='groove', font=('serif', 16, 'bold'), padx=50)
            clear_button.place(rely=0.9, relx=0.27, anchor='center')
            ToolTips.bind(clear_button, 'Clears data entered')

            def firstcompleteLogin():
                self.finalloginname = loginUsername.get()
                first_login_submit(loginUsername.get(), loginPassword.get(), loginfirstname.get(), loginsurname.get())

            login_button = tkinter.Button(self.login, cursor="tcross",text="Login", command=firstcompleteLogin, fg='white', bg='black', bd=6, relief='groove', font=('serif', 16, 'bold'), padx=50)
            login_button.place(rely=0.9, relx=0.73, anchor='center')
            ToolTips.bind(login_button, 'Login to the system')


        RemoveDates()