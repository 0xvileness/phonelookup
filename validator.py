import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier



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
print()

# Enter phone number with the country code

number = input("Enter phone number with country code : ")

# Parsing String to the Phone number
phone_number = phonenumbers.parse(number)

# Printing the country code and national number separately
country_code = phone_number.country_code
national_number = phone_number.national_number
print("Country Code:", country_code)
print("National Number:", national_number)

# Printing the timezone using the timezone module
time_zone = timezone.time_zones_for_number(phone_number)
print("Timezone :", time_zone)

# Printing the geolocation of the given number using the geocoder module
location = geocoder.description_for_number(phone_number, "en")
print("Location :", location)

# Printing the service provider name using the carrier module
service_provider = carrier.name_for_number(phone_number, "en")
print("Service Provider :", service_provider)
