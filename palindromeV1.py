string = input("Enter the input to be cheked: ")
change = string.replace(" ","").lower()

left_ptr = 0
right_ptr = len(change)-1

palindrome = True

while left_ptr < right_ptr:
    if change[left_ptr] != change[right_ptr]:
        palindrome = False
        break
    left_ptr += 1
    right_ptr -= 1
    
if palindrome:
    print("The given string is a palindrome")
else:
    print("The given string is not a palindrome")
