from tkinter import Tk

windowBox = Tk()
import json

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

windowBox.mainloop()
