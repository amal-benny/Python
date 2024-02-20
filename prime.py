def prime(number):
    n = number*number
    data = n -1
    if (data % 24) == 0:
        return True
    else:
        return False

check = int(input("Enter any number greater than 3 "))

            
if prime(check):
    print(f"The given number {check} is a prime number")
else:
    print(f"The given number {check} is not a prime number")
