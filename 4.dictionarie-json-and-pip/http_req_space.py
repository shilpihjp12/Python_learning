#http request to get current people in space
# install requests package from pip3
# pip3 install requests

#virtual environment to maintain different pakage at same time


import requests

response = requests.get("http://api.open-notify.org/astros.json")
json = response.json()

print('People in space:', json)

for person in json['people']:
    print(person['name'], 'is in', person['craft'])
