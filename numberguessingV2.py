import random

def guess():
    print("-----WELCOME TO THE NUMBER GUESSING GAME------")
    print("I have randomly selected a number from 1 to 100 guess it within 3 tries")
    print("You have 3 tries to guess the number")
    number = random.randint(1,100)
    
    guessed = False
    attempt = 0
    
    while not guessed and attempt < 3:
        guess = int(input("Enter your guess: "))
        attempt += 1
        
        if attempt <= 3:
            print(f"This was your {attempt} attempt")
            if (guess == number):
                 print("You have guessed the number correctly")
                guessed = True
            elif guess < number:
                print(f"The value to be guessed is larger than {guess}")
            else:
                print(f"The value to be guessed is smaller than {guess}")
    if not guessed:
        print("Your attempts to try has run out")
        print(f"The random number that was generated was {number}")
guess()