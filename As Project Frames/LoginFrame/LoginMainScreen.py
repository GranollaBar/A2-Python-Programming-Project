from tkinter import *
from LoginFrame.AS_programming_loginscreen import LoginContent


LoginMainScreen = Tk()
LoginMainScreen.title('Lisburn Raquets Club')
LoginMainScreen.geometry('500x500')
LoginMainScreen.configure(bg='white')
LoginMainScreen.resizable(0,0)


FinalLoginContent = LoginContent(LoginMainScreen)
FinalLoginContent.generateLoginContnt()


LoginMainScreen.mainloop()
