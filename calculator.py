# Day 2: Simple Calculator
# Problem: Create a basic calculator that takes two numbers
# and performs addition, subtraction, multiplication, and division.

# Solution:
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero."

# Input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Output
print(f"\n{num1} + {num2} = ",(add(num1, num2)))
print(f"{num1} - {num2} = {subtract(num1, num2)}")
print(f"{num1} * {num2} = {multiply(num1, num2)}")
print(f"{num1} / {num2} = {divide(num1, num2)}")
