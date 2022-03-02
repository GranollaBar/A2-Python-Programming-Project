# Login Main screen

from tkinter import *
from LoginFrame.AS_programming_loginscreen import LoginContent

# Login tkinter window
LoginMainScreen = Tk()
LoginMainScreen.title('Lisburn Raquets Club')
LoginMainScreen.geometry('500x500')
LoginMainScreen.configure(bg='white')
LoginMainScreen.resizable(0, 0)

# Will perform and run AS_programming_loginscreen class and all its content
FinalLoginContent = LoginContent(LoginMainScreen)
FinalLoginContent.generateLoginContnt()

LoginMainScreen.mainloop()
