import random
import string

# Function to generate a random password
def generate_password(length):
    # Define the character sets for different complexity levels
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase
    digits = string.digits
    special_chars = "!@#$%^&*()_+[]{}|;:',<>.?"

    # Combine character sets based on desired complexity
    if length < 8:
        char_set = lowercase_chars + digits
    else:
        char_set = lowercase_chars + uppercase_chars + digits + special_chars

    # Generate the password
    password = ''.join(random.choice(char_set) for _ in range(length))
    return password

# Prompt the user to specify the desired length of the password
try:
    length = int(input("Enter the desired password length: "))
except ValueError:
    print("Invalid input. Please enter a valid number for the password length.")
    exit(1)

# Generate and display the password
password = generate_password(length)
print("Generated password: " + password)
