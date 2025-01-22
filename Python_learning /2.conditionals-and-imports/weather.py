#If-elif-else statements and logical operators

temperature = 50
forecast = "rainy"
raining = true

# or logical operator
if temperature > 80 or temperature < 60:
  # evaluate as inside the block
  print("Stay inside!")
else:
  print('Enjoy the outdoors!')

# and logical operator
if temperature < 80 and forecast != 'rainy':
  print('Go outside!')
else:
  print('Stay inside!')


# not logical operator
if not forecast == 'rainy':
  print('Go outside!')
else:
  print('Stay inside!')

# boolean values
if raining:
  print('Stay inside!')
else:
  print('Go outside!')