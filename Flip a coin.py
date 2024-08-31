import random
print("-----------FLIP THE COIN-------------")
print("Do you wish to flip the coin")
input_str = input("Enter yes if you wish to flip the coin: ")
value = input_str.lower()

if value == "yes":
    cars = ( "Heads", "Tails")
    coin = random.choice(cars)
    print(f"{coin}")
else:
    print("Try again")
    
