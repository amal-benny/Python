a = input("Enter the string to be cheked: ")
b = a.replace(" ","").lower()
c= b[::-1]

if b == c:
    print("The given string is a palindrome")
else:
    print("The given string is not a palindrome")