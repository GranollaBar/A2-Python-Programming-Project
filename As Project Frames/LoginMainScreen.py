# Login Main screen

from tkinter import *
from AS_programming_loginscreen import LoginContent
import os

# This is the realtive file path to all files in the program
dirname = os.path.dirname(__file__)

# Login tkinter window
LoginMainScreen = Tk()
LoginMainScreen.title('Lisburn Raquets Club')
LoginMainScreen.geometry('500x500')
LoginMainScreen.configure(bg='white')
LoginMainScreen.resizable(0, 0)


# Will perform and run AS_programming_loginscreen class and all its content
FinalLoginContent = LoginContent(LoginMainScreen, dirname)
FinalLoginContent.generateLoginContnt()

LoginMainScreen.mainloop()
