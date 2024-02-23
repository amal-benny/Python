import random
import string

def generate(length, uppercase, lowercase, digits, punctuation):
    chars = ''
    if uppercase:
        chars += string.ascii_uppercase
    if lowercase:
        chars += string.ascii_lowercase
    if digits:
        chars += string.digits
    if punctuation:
        chars += string.punctuation
        
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

print("---------------PASSWORD GENERATOR-------------------")    
length = int(input("Enter the length of the password: "))
uppercase = input("Do you want to include uppercase yes/no: ").lower() == "yes"
lowercase = input("Do you want to include lowercase yes/no: ").lower() == "yes"
digits = input("Do you want to include digits yes/no: ").lower() == "yes"
specialsymbols = input("Do you want to include specialsymbols yes/no: ").lower() == "yes"

result = generate(length, uppercase, lowercase, digits, specialsymbols)

print(f"The required password is {result}")
