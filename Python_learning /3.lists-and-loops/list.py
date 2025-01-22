

acronyms = ['lol', 'brb', 'smh', 'lmk', 'tbh']

#Add new in list
acronyms.append('idk')
acronyms.append('imho')

print(acronyms[0])
print(acronyms[6])
print(acronyms)

#remove item from list
acronyms.remove('smh')
print(acronyms)

#check for item is available in list
if 'smh' in acronyms:
  print('smh is in the list')
else:
  print('smh is not in the list')

#print items in seperate lint 
print('print items in seperate list:')
for acronym in acronyms:
  print(acronym)