import os

look_up = input("what software acronym do you want to look up? ")

found = False
with open('acronym_input.txt') as file:
  for line in file:
    if look_up in line:
      print(line)
      found = True
      break # breaks the loop

if not found:
  print('Acronym not found')