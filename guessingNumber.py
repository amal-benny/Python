import random

number = int(random.randint(1,100))
 
print("-----  GUESS THE NUMBER GAME ----------")
print("The number is from 1 to 100 integers")

guessed = int(input("Enter your guess: "))


if guessed == number:
    print(f"You have guessed the number {number} correctly")
else:
    print(f"The number you have guessed is incorrect ")
    print(f"The Correct number was {number}")
        
