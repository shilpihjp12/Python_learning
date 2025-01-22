
#list of list
menus = [ ['Egg', 'Bacon', 'Sausage', 'Spam'], ['BLT', 'Ham', 'Cheese', 'Spam'], ['Soup', 'Sandwich', 'Spam', 'Spam'] ]

print(menus[0][0])

# its good to keep the list of list in dictionary
menus = { 'breakfast': ['Egg', 'Bacon', 'Sausage', 'Spam'], 'lunch': ['BLT', 'Ham', 'Cheese', 'Spam'], 'dinner': ['Soup', 'Sandwich', 'Spam', 'Spam'] }

#look key and value in dictionary
for name, menu in menus.items():
  print(name, ':', menu)

#use dict for reprensenting the object

person = { 'name' : 'John', 'age' : 30, 'city' : 'New York' }

print(person.get('name'), 'is', person.get('age'), 'years old and lives in', person.get('city'))