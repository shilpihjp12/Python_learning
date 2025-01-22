#its a key, value map

acronyms = { 'LOL': 'Laugh out loud', 'BRB': 'Be right back', 'TBH': 'To be honest' }

#Add new in dictionary
acronyms['SMH'] = 'Shaking my head'

print(acronyms)

#update value in dictionary
acronyms['LOL'] = 'Laughing out loud2'

print(acronyms)

#delete item from dictionary
del acronyms['LOL']

print(acronyms)

#to get value from key
print(acronyms.get('BRB'))
#if key dont exist it will return None
print(acronyms.get('BTB')) 