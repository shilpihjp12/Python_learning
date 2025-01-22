
contact = {
  'number': 4,
  'students': [
    {'name': 'Sarah', 'email': 'A@gmail.com'},
    {'name': 'John', 'email': 'B@web.de'},
    {'name': 'Mike', 'email': 'C@yahoo.com'},
    {'name': 'Sally', 'email': 'A@gmx.de'}
  ]
}

print('student emails:')

#how to take students list of dictionary from contact dictionary
for student in contact['students']:
  print(student['email'])