# def fact(n):
#     if n==0 or n == 1:
#         return 1;
#     else:
#         return n*fact(n-1)

def fact(n):
    result = 1
    for i in range(1, n):
        result = result*i
    return result
        
number = int(input("What number's factorial should be checked: "))
print(f"The factorial of {number} is {fact(number)}")
