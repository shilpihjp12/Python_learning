#its a key, value map

acronyms = { 'LOL': 'Laugh out loud2', 'BRB': 'Be right back', 'TBH': 'To be honest' }

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


print('--------------Manipulate Dictionary----------------------')
print(acronyms.keys())
print(acronyms.values())
print(acronyms.items()) #get as tuples[]
print(sorted(acronyms.keys())) #sort keys
print(sorted(acronyms.values(), reverse=True)) #sort values
print(acronyms.get('LOL2', 'Not found')) #get value from key, if key not found return default value
print(acronyms.pop('BRB')) #remove item from dictionary