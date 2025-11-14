# Simple Password Generator for Beginners

import random
import string

print("=== PASSWORD GENERATOR ===")

# Ask user for password length
length = int(input("Enter the password length: "))

# Characters to choose from
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = ""
for i in range(length):
    password += random.choice(characters)

# Show the password
print("Your generated password is:", password)
