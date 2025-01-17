#9.1 Accessing Array Elements.
numbers = [10, 20, 30, 40, 50]
index = int(input("Enter an index (0-4): "))
if 0 <= index < len(numbers):
    print("Element at index", index, "is:", numbers[index])
else:
    print("Invalid index!")


#9.2 Insert Element into Array.
numbers = [10, 20, 30, 40, 50]
new_value = int(input("Enter a number to insert: "))
position = int(input("Enter the position (0-5): "))

if 0 <= position <= len(numbers):
    numbers.insert(position, new_value)
    print("Updated array:", numbers)
else:
    print("Invalid position!")


#9.3 Remove Element from Array.
numbers = [10, 20, 30, 40, 50]
value_to_remove = int(input("Enter a value to remove: "))

if value_to_remove in numbers:
    numbers.remove(value_to_remove)
    print("Updated array:", numbers)
else:
    print("Value not found in the array!")


#9.4 Reverse the Array.
numbers = [10, 20, 30, 40, 50]
reversed_numbers = numbers[::-1]
print("Reversed array:", reversed_numbers)


#9.5 Find Minimum and Maximum.
numbers = [10, 20, 30, 40, 50]
print("Minimum value:", min(numbers))
print("Maximum value:", max(numbers))


#9.6 Sum of Array Elements.
numbers = [10, 20, 30, 40, 50]
total_sum = sum(numbers)
print("Sum of array elements:", total_sum)