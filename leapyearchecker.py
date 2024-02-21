print("--------------------LEAP YEAR CHECKER--------------------")

def check(n):
    return n % 4 == 0
    
year = int(input("Enter the year to be checked "))

if check(year):
    print(f"The given year {year} is an leap year")
else:
    print(f"The given year {year} is not an leap year")