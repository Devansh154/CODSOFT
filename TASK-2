import random
import string

# Ask the user for the desired password length
print("Welcome to the Password Generator!")
length = int(input("Enter the desired password length: "))

# Define the characters to use in the password
all_characters = string.ascii_letters + string.digits + string.punctuation

# Generate the password using random choices
password = ''.join(random.choice(all_characters) for _ in range(length))

# Display the generated password
print("Your generated password is: ",password)
