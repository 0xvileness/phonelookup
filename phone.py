from phonenumbers import *
import requests

print()
print(" ┏┓┓         ┏┓┏┓┳┳┓┏┳┓ ")
print(" ┃┃┣┓┏┓┏┓┏┓  ┃┃┗┓┃┃┃ ┃  ")
print(" ┣┛┛┗┗┛┛┗┗   ┗┛┗┛┻┛┗ ┻  ")
print("   Made By @Oxycrime ")
print()                  

phone_number = input("Enter a phone-number: ")
response = requests.get("http://apilayer.net/api/validate?access_key=&number=" + phone_number + "&country_code=US")

print(response.json())
