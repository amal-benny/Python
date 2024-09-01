def prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(n**0.5)):
            if n % i == 0:
                return False
        return True
 
a = int(input("Enter the numbers in which the prime numbers lesser than that should be printed: "))       
print(f"The numbers that are prime inbetween 1 and {a} are")
for i in range(1,a+1):
    if prime(i):
        print(i, end=" ")
