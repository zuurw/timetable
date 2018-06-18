#import relevant modules
from tkinter import *
import json

#define Tk and the window, title and favicon.
master = Tk()
master.geometry('300x300')
master.title("tableTimes")
master.iconbitmap("favicon.ico")

#defines code for the 'add subject button'
def addsubject():
    
#content / buttons and GUI
AddSubjectB = Button(master, text="Add new subject", command=addsubject)
AddSubjectB.pack(expand=YES)

#loops and starts the GUI
master.mainloop()