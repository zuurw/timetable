# import relevant modules
from tkinter import *
import json
import sys

# define Tk and the window, title and favicon.
master = Tk()
master.geometry('325x150')
master.title("tableTimes")
master.iconbitmap("favicon.ico")

# define background
mycolor = '#404040'
master.configure(bg=mycolor)

# defines code for the 'add subject button'


def addsubject():
    subject = AddSubjectField.get()
    time = AddSubjectTimeField.get()
    filename = 'subject_' + str(subject) + '.json'
    with open(filename, 'w') as f_obj:
        json.dump('[' + time + ']', f_obj)


#define link to close program
def exitWRITEJSON():
    raise SystemExit


#content / buttons and GUI
AddSubjectText = Label(
    master, text="Add a new subject", fg="white", bg="#404040")
AddSubjectField = Entry(master)
AddSubjectTimeText = Label(
    master,
    text="Add times ( DD/MM/YY HH:MM , DD/MM/YY HH:MM... )",
    fg="white",
    bg="#404040")
AddSubjectTimeField = Entry(master)
AddSubjectButton = Button(master, text="Confirm!", command=addsubject)
AddExitButton = Button(master, text="Done adding!", command=exitWRITEJSON)

AddSubjectText.pack()
AddSubjectField.pack()
AddSubjectTimeText.pack()
AddSubjectTimeField.pack()
AddSubjectButton.pack()
AddExitButton.pack()

# loops and starts the GUI
master.mainloop()
