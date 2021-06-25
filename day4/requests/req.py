import requests

r = requests.get('https://api.agify.io?name=Siti&country_id=MY')
print(r)
#{"name":"Siti","age":30,"count":6794,"country_id":"MY"}

url = 'https://api.github.com/events'
headers = {'user-agent': 'my-app/0.0.1'}

r = requests.get(url, headers=headers)

print(r)
body_ = r.content
print(body_)

items = {'Selangor': 'SEL', 'Johor':'JHR'}
r = requests.post("https://httpbin.org/post", data= items)

#posting tuples/dict
items_tuple = [('Selangor', 'SEL'), ('Selangor', 'SGR')]
r1 = requests.post('https://httpbin.org/post', data=items_tuple)
items_dict = {'Selangor' : ['SEL', 'SGR']}
r2 = requests.post('https://httpbin.org/post', data=items_dict)
print('r1 text: ' , r1.text)
#r1 text:  {
#  "args": {}, 
#  "data": "", 
#  "files": {}, 
#  "form": {
#    "Selangor": [
#      "SEL", 
#      "SGR"
#    ]
#  },

print('r2.text: ' , r2.text)
#r2.text:  {
#  "args": {}, 
#  "data": "", 
#  "files": {}, 
#  "form": {
#    "Selangor": [
#      "SEL", 
#      "SGR"
#    ]
#  }
