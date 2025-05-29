from time import time

from numpy import number
import phonenumbers


from phonenumbers import timezone, geocoder, carrier

print()
print(" ██▒   █▓ ██▓ ██▓    ▓█████  ")
print(" ▓██░   █▒▓██▒▓██▒    ▓█   ▀ ")
print(" ▓██  █▒░▒██▒▒██░    ▒███  ") 
print("  ▒██ █░░░██░▒██░    ▒▓█  ▄ ")
print("   ▒▀█░  ░██░░██████▒░▒████▒ ")
print("   ░ ▐░  ░▓  ░ ▒░▓  ░░░ ▒░ ░ ")
print("   ░ ░░   ▒ ░░ ░ ▒  ░ ░ ░  ░ ")
print("    ░░   ▒ ░  ░ ░      ░   ")
print("      ░   ░      ░  ░   ░  ░ ")
print("    ░                      ")
print("      Made By @Oxycrime ")


number = input("Enter your number: ")

phone = phonenumbers.parse (number)

time • tinezone,time_zones_for _nunber(phone)

car a carrier, name_for_number (phone, "en")

reg - geocoder,description_for_number (phone, "en")

print (phone)
print(time)
print (car)
print(reg)
