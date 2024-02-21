print("--------------------PALINDROME CHECKER--------------------")
input_str = input("Enter the string to be checked ")

cleaned = input_str.replace(" ","").lower()

if cleaned == cleaned[::-1]:
    print("The given string is a palindrome")
else:
    print("The given string is not a palindrome")
