from phonenumbers import *
import requests

print()
print(" ┏┓┓         ┏┓┏┓┳┳┓┏┳┓ ")
print(" ┃┃┣┓┏┓┏┓┏┓  ┃┃┗┓┃┃┃ ┃  ")
print(" ┣┛┛┗┗┛┛┗┗   ┗┛┗┛┻┛┗ ┻  ")
print("   Made By @Oxycrime ")
print()                  

phone_number = input("Enter a phone-number: ")
response = requests.get("http://apilayer.net/api/validate?access_key=0934c36cd49141e24778e5dffa755e5b&number=" + phone_number + "&country_code=US")

print(response.json())
