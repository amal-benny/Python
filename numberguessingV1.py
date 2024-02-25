import random

def guess():
    print("-----WELCOME TO THE NUMBER GUESSING GAME------")
    print("I have randomly selected a number from 1 to 100 guess it within 3 tries")
    number = random.randint(1,100)
    
    guessed = False
    attempt = 0
    
    while not guessed:
        guess = int(input("Enter your guess: "))
        attempt += 1
        
        if (guess == number) and attempt < 4:
            print("You have guessed the number correctly")
            guessed = True
        elif guess < number:
            print(f"The value to be guessed is larger than {guess}")
        else:
             print(f"The value to be guessed is smaller than {guess}")
             
guess()
