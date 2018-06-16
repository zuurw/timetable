import json

subject = input("Enter name of subject here:")
filename = 'subject_' + str(subject) + '.json'
with open(filename, 'w') as f_obj:
    json.dump(subject, f_obj)

print("Note: Use commas between each one!")
times = input("Enter times you will attend the subject here:")
filename = 'subject_' + str(subject) + '.json'
with open(filename, 'w') as f_obj:
    json.dump(subject, f_obj)
