import re

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


def phone_lookup(phone_number):
    # Remove non-digit characters
    phone_number = re.sub(r'\D', '', phone_number)

    # Validate phone number format
    if len(phone_number) == 10:
        # Format phone number
        formatted_number = f"({phone_number[:3]}) {phone_number[3:6]}-{phone_number[6:]}"
        return formatted_number
    elif len(phone_number) == 11 and phone_number[0] == '1':
        # Format phone number with country code
        formatted_number = f"+1 ({phone_number[1:4]}) {phone_number[4:7]}-{phone_number[7:]}"
        return formatted_number
    else:
        return "Invalid phone number"

# Example usage:
phone_number = input("Enter a phone number: ")
result = phone_lookup(phone_number)
print(result)
