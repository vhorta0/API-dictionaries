# rest api's 
# application programming  interface
import requests #request something from the internet
import json #stands for javascript object notations

response=requests.get("https://randomuser.me/api/")
# print(response.json())

gender=response.json()['results'][0]['gender']
print(gender)
title=response.json()['results'][0]['name']['title']
print(title)
first_name=response.json()['results'][0]['name']['first']
print(first_name)
last_name=response.json()['results'][0]['name']['last']
print(last_name)
email=response.json()['results'][0]['email']
print(email)
phone_number=response.json()['results'][0]['phone']
print(phone_number)
city=response.json()['results'][0]['location']['city']
print(city)
postal_code=response.json()['results'][0]['location']['postcode']
print(postal_code)
street=response.json()['results'][0]['location']['street']
print(street)
login_id=response.json()['results'][0]['login']['username']
print(login_id)
age=response.json()['results'][0]['dob']['age']
print(age)