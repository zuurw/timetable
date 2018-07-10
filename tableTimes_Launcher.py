from tkinter import *
import json
import sys
# define Tk, window geometry, favicon, and window.
master = Tk()
master.geometry('275x125')
master.title("tableTimes")
master.iconbitmap("favicon.ico")
# define background
mycolour = '#404040'
master.configure(bg=mycolour)


# define link to launch the writeJSON file.
def openwriteJSON():
    import tableTimes_writeJSON
    raise SystemExit


# define link to launch the readJSONS
def openreadJSONS():
    import tableTimes_writeJSON


# define link to close the program
def closeLauncher():
    raise SystemExit


# content
AddIntroText = Label(
    master,
    text="Welcome to tableTimes - Choose a choice below.",
    fg="white",
    bg="#404040")
AddButtonWriteJSON = Button(
    master, text="Add a subject", command=openwriteJSON)
AddButtonReadJSONS = Button(
    master, text="What's my schedule?", command=openreadJSONS)
AddButtonExitLauncher = Button(
    master, text="Exit tableTimes", command=closeLauncher)
#pack contents of content
AddIntroText.pack()
AddButtonWriteJSON.pack()
AddButtonReadJSONS.pack()
AddButtonExitLauncher.pack()

# loop & start the GUI
master.mainloop()
