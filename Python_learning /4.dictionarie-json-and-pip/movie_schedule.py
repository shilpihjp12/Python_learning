
current_movies = {'The Grinch': '11:00am', 'Rudolph': '1:00pm', 'Frosty the Snowman': '3:00pm', 'christmas Vacation': '5:00pm'}

print('We are showing the following movies:')
for key in current_movies:
  print(key)

movie = input('what movie would you like the showtime for?\n')

showtime = current_movies.get(movie)

if showtime == None:
  print("Requested movie isn't playing")
else:
  print(movie, 'is playing at', showtime)