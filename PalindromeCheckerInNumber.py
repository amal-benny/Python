def reverse(n):
    reversed = 0
    if n == 0:
        return reversed
    while n > 0:
        r = n % 10
        reversed = reversed * 10 + r
        n = n // 10
    return reversed
        
a = int(input("Enter a number to check if palindrome"))
b = reverse(a)
print(b)
if a == b:
    print("The given number is a palindrome")
else:
    print("The given number is not a palindrome")

