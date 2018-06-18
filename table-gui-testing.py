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
    subject = AddSubjectField.get()
    time = AddSubjectTimeField.get()


#content / buttons and GUI
AddSubjectText = Label(master, text="Add a new subject")
AddSubjectField = Entry(master)
AddSubjectTimeText = Label(master, text="Add times ( DD/MM/YY HH:MM , DD/MM/YY HH:MM... )")
AddSubjectTimeField = Entry(master)
AddSubjectButton = Button(master, text="Confirm!", command=addsubject)

AddSubjectText.pack()
AddSubjectField.pack()
AddSubjectTimeText.pack()
AddSubjectTimeField.pack()
AddSubjectButton.pack()

#loops and starts the GUI
master.mainloop()

subject = input("Enter name of subject here:")
filename = 'subject_' + str(subject) + '.json'
with open(filename, 'w') as f_obj:
    json.dump(subject, f_obj)

print("Note: Requires format: DD/MM/YYYY (Y2K KEK) then HH:MM")
times = input("Enter times you will attend the subject here:")
filename = 'subject_' + str(subject) + '.json'
with open(filename, 'w') as f_obj:
    json.dump(subject, f_obj)
print(times)