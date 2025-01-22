# Age calculator
age = int(input('enter your age: '))
decades = age // 10 # // back slash is used to get the integer value
years = age % 10
print("you are getting " + str(decades) + " decades and " + str(years) + " years old")