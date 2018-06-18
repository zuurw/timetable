from tkinter import *

master = Tk()
master.geometry('300x300')
master.title("tableTimes")
master.iconbitmap("favicon.ico")

def addsubject():
    

AddSubjectB = Button(master, text="Add new subject", command=addsubject)
AddSubjectB.pack(expand=YES)

master.mainloop()