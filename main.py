import csv

file = open('./data.csv')
csv_file = csv.reader(file)
student_data = []
next(csv_file, None)
DATA_SCIENCE = "Education - LIVE - Data Science"
CYBER_SEC = "Education - LIVE - Cyber"
CYBER_SEC_NETWORKING = "Education - LIVE - Cyber; Education - LIVE - Networking"
courses = [
    'ITIC-DS',  # Data Science
    'CCIRM'  # Cybersecurity
]
for row in csv_file:
    course = ''
    if row[5] == DATA_SCIENCE:
        course = courses[0]
    elif row[5] == CYBER_SEC or row[5] == CYBER_SEC_NETWORKING:
        course = courses[1]
    #                    username, fname,        lname,          email,  course, role
    student_data.append([row[4], row[1].title(), row[2].title(), row[4], course, 'student'])

with open('students.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['username', 'firstname', 'lastname', 'email', 'course1', 'role1'])
    writer.writerows(student_data)
