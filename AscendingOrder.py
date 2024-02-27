def sort(number):
    number = sorted(number)
    return number
    
print("------Ascending Order--------")
input_str = input("Enter the list value with spaces to get a sorted list: ")

value = [int(num) for num in input_str.split()]

print(f"The unordered list is : {value}")
print(f"The ordered list is : {sort(value)}")
