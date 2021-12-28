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
from MainScreens.SMSSystem import MemberJoingSMS
from MainScreens.SMSSystem import ChangingPassword



class LoginContent:

    def getloginname(self):
        return self.finalloginname

    def __init__(self, mainScreen):
        self.finalloginname = ''

        self.login = mainScreen
        self.conn = sqlite3.connect('C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Databases/LisburnRacquetsDatabase.db')
        self.c = self.conn.cursor()


        # self.c.execute("""CREATE TABLE account (
        #                 username text,
        #                 password text,
        #                 status text
        #                 )""")


    def generateLoginContnt(self):

        def validate_password(value, label):
            if value is None:
                return False
            if (value == ''):
                label.config(fg="red")
                messagebox.showinfo("Validation Error", "The password field must contain a .", icon='error')
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


        def validate_username(value, label):
            if value is None:
                return False
            if (value == ''):
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

                    choosing_toplevel=Toplevel(width=250, height=100, bg="white")

                    title_label = tkinter.Label(choosing_toplevel, text="Where do you want the code sent to", font=('Verdana', 9, 'underline', 'bold'), fg='SpringGreen3', bg='white')
                    title_label.place(rely=0.125, relx=0.5, anchor='center')

                    choosing1_radiobutton = Radiobutton(choosing_toplevel, text="Email", variable=choosing, value=1, font=("Segoe UI Black",9, 'bold'), cursor="tcross", bg="white", bd=2, relief="ridge")
                    choosing1_radiobutton.place(rely=0.4, relx=0.3, anchor='center')

                    choosing2_radiobutton = Radiobutton(choosing_toplevel, text="SMS", variable=choosing, value=2, font=("Segoe UI Black",9, 'bold'), cursor="tcross", bg="white", bd=2, relief="ridge")
                    choosing2_radiobutton.place(rely=0.4, relx=0.7, anchor='center')

                    choosing_button=Button(choosing_toplevel,text = 'Select', command = lambda : completeVerification(choosing, recipient, choosing_toplevel), fg ='white', bg='black', relief= 'groove', font = ('Verdana',10,'bold'), padx =30)
                    choosing_button.place(rely=0.8,relx=0.5,anchor=CENTER)


        def completeVerification(value, name, frame):
            final_choosing = value.get()

            if (final_choosing == 1):
                emailSending(name, frame)
            if (final_choosing == 2):
                SMSSending(name, frame)


        def emailSending(finalname, finalframe):
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

                finalframe.destroy()


        def SMSSending(finalname, finalframe):
            verification = IntVar()
            newpassword = StringVar()
            verificationCode = random.randint(100000,999999)

            found = ChangingPassword(str(verificationCode), finalframe)
            if found:

                SMS_toplevel=Toplevel(width=300, height=200, bg="white")

                title_label = tkinter.Label(SMS_toplevel, text="Forgot Password System", font=('Verdana', 14, 'underline', 'bold'), fg='SpringGreen3', bg='white')
                title_label.place(rely=0.125, relx=0.5, anchor='center')

                verification_label = Label(SMS_toplevel,text = 'Verification Code:', fg ='black', bg='white', font = ('Verdana',12,'bold'))
                verification_label.place(rely=0.4,relx=0.3,anchor=CENTER)

                newpassword_label = Label(SMS_toplevel,text = 'New Password:', fg ='black', bg='white', font = ('Verdana',12,'bold'))
                newpassword_label.place(rely=0.6,relx=0.3,anchor=CENTER)

                verification_entry = Entry(SMS_toplevel,width=15, borderwidth=2, textvariable=verification)
                verification_entry.place(rely=0.403,relx=0.8,anchor=CENTER)
                verification.set('')

                newpassword_entry = Entry(SMS_toplevel,width=15, borderwidth=2, textvariable=newpassword)
                newpassword_entry.place(rely=0.603,relx=0.8,anchor=CENTER)

                def completeVerification():
                    newPasswordUpdate(newpassword.get(), verificationCode, verification.get(), SMS_toplevel, verification, newpassword, finalname)

                newpassword_button=Button(SMS_toplevel,text = 'Update Password', command = completeVerification, fg ='white', bg='black', relief= 'groove', font = ('Verdana',10,'bold'), padx =20)
                newpassword_button.place(rely=0.85,relx=0.5,anchor=CENTER)

                finalframe.destroy()


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
                        from MainScreens import MainScreen
                        MainScreen.passLoginScreen(self)
                        MainScreen.main()


                    if (data[2] == 'coach'):
                        from MainScreens import MainScreen
                        MainScreen.passLoginScreen(self)
                        MainScreen.main()


                    if (data[2] == 'manager'):
                        from MainScreens import MainScreen
                        MainScreen.passLoginScreen(self)
                        MainScreen.main()


            conn.commit()
            conn.close()


        def login_clear():
            response = askyesno("Question", "Do you want to clear all details entered so far", icon='question')
            if response == False:
                showinfo("Info", "clearance cancelled", icon='info')

            else:

                loginUsername.set('')
                loginPassword.set('')


        def show_password(self):
            password_entry.config(show="")


        def dont_show_password(self):
            password_entry.config(show="*")


        def twitterLink():
            webbrowser.open("https://twitter.com/lisburnracquets")


        def facebookLink():
            webbrowser.open("https://www.facebook.com/LisburnRacquetsClub")



        loginUsername = StringVar()
        loginPassword = StringVar()
        choosing=IntVar()



        title_label = tkinter.Label(self.login, text="Welcome To Lisburn Racquets Club", font=('Tahoma', 18, 'underline', 'bold'), fg='SpringGreen3', bg='white')
        title_label.place(rely=0.06, relx=0.5, anchor='center')

        username_label = tkinter.Label(self.login, text="Username:", font=('Tahoma', 20, 'bold'),fg='black', bg='white')
        username_label.place(rely=0.45, relx=0.295, anchor='center')

        password_label = tkinter.Label(self.login, text="Password:", font=('Tahoma', 20, 'bold'), fg='black', bg='white')
        password_label.place(rely=0.6, relx=0.3, anchor='center')


        username_entry = tkinter.Entry(self.login, width=30, textvariable = loginUsername, bd=4, relief='ridge', cursor="tcross")
        username_entry.place(rely=0.454, relx=0.655, anchor='center')

        password_entry = tkinter.Entry(self.login, width=30, show="*", textvariable = loginPassword, bd=4, relief='ridge', cursor="tcross")
        password_entry.place(rely=0.604, relx=0.655, anchor='center')


        twitterImage = PhotoImage(file="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Images/twitter.png")
        facebookImage = PhotoImage(file="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Images/facebook.png")
        passwordImage = PhotoImage(file="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Images/eye.png")
        notpasswordImage = PhotoImage(file="C:/Users/Josh/pyqt tutorial/AS-Programming-Project/AS Project Frames/_databases_images_doc/Images/noteye.png")


        twitterButton = Button(self.login, cursor="tcross", image=twitterImage, width=75, height=75, command=twitterLink, bg="white", highlightthickness=2, activebackground="grey")
        twitterButton.place(rely=0.25,relx=0.86,anchor=CENTER)
        twitterButton.image = twitterImage

        facebookButton = Button(self.login, cursor="tcross", image=facebookImage, width=74, height=74, command=facebookLink, bg="white", highlightthickness=2, activebackground="grey")
        facebookButton.place(rely=0.25,relx=0.14,anchor=CENTER)
        facebookButton.image = facebookImage

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


        forgot_password_button = tkinter.Button(self.login, cursor="tcross", text="Forgot Password", command=forgot_system, fg='white', bg='black', bd=6, relief='ridge', font=('Segoe UI Black', 12, 'bold'), padx=10)
        forgot_password_button.place(rely=0.7, relx=0.5, anchor='center')

        clear_button = tkinter.Button(self.login, cursor="tcross", text="Clear", command=login_clear, fg='white', bg='black', bd=6, relief='groove', font=('Segoe UI Black', 16, 'bold'), padx=50)
        clear_button.place(rely=0.9, relx=0.27, anchor='center')

        def completeLogin():
            self.finalloginname = loginUsername.get()
            login_submit(loginUsername.get(), loginPassword.get())

        login_button = tkinter.Button(self.login, cursor="tcross",text="Login", command=completeLogin, fg='white', bg='black', bd=6, relief='groove', font=('Segoe UI Black', 16, 'bold'), padx=50)
        login_button.place(rely=0.9, relx=0.73, anchor='center')
