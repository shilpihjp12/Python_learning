# with open('./acronym_input.txt') as file:
#   result = file.read()
#   print(result)

file = open('./acronym_input.txt', 'r')
print(file.read())
file.close()