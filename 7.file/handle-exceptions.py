# Handle exception
# handle try-except-finally block

acronym = { 'LOL': 'Laugh Out Loud',
           'IDK': "I Don't Know",
           'BFF': 'Best Friends Forever'}
try:
  print(acronym['LOL'])
except KeyError:
  print("That acronym is not in the dictionary.")
finally:
  print("This is executed no matter wahat")