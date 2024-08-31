def sort(number):
    sorted_number = sorted(number)
    return sorted_number
    
list_value = input("Enter the numbers with the spaces inbetween the numbers")
value = [int(num) for num in list_value.split()]
old = [value]
print(f" The unsorted values are {old}")
print(f" The sorted values are {sort(value)}")
