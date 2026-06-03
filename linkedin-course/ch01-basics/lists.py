# Lists in Python
# A list is a collection of items that are ordered and changeable.
# Lists are written with square brackets.

# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Create a list of strings
fruits = ["apple", "banana", "cherry"]

# mixed data types
mixed = [1, "hello", 3.14, True]

# list of lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# ------------------------------------------lists of dictionaries-------------------------------
employees = [{'name': "a", 'age': 5, 'year': 2026}, {'name': "b",
                                                     'age': 6, 'year': 2025}, {'name': "c", 'age': 7, 'year': 2026}]

# display all names in list
names = [employee['name'] for employee in employees]
print(names)

first_employee = employees[0]['name']
print(first_employee)

target_user = []
for employee in employees:
    if employee.get('year') == 2026:
        target_user.append(employee)
print(target_user)

# print 5 zeros - * is used to repeat an item in a list
zeros = [0] * 5
print(zeros)

# + operator is used to concatenate lists
combined = numbers + fruits
print(combined)

# create a list of numbers from 0 to 9 using range
numbers = list(range(10))
print(numbers)

# create a list for string "hello World"
hello_world_string = list("hello World")
print(hello_world_string)

# ------------------------------------------Accessing List Items-------------------------------

# Accessing list items using index
print(fruits[0])  # prints "apple"

# negative indexing - starts from the end of the list
print(fruits[-1])  # prints "cherry"

# creates a new list with the items from index 0 to 1 (not including index 2), doesn't change the original list
print(fruits[0:2])  # prints "banana"
print(fruits)  # prints the original list

# Modifying list items
fruits[0] = "orange"
print(fruits)  # prints the modified list

# ------------------------------------------Unpacking Lists-------------------------------
unpacking_list = [1, 2, 3, 4, 5, 7, 8, 9, 10]

# traditional way to unpack a list
first = unpacking_list[0]
second = unpacking_list[1]
rest = unpacking_list[2:]
print("traditional way:", first, second, rest)

# unpacking a list using * operator
first, *rest, second = unpacking_list
print("unpacking way:", first, second, rest)

# ------------------------------------------Add/Remove Items-------------------------------
letters = ["a", "b", "c", "d", "e", "c"]

# add
letters.append("d")  # adds "d" to the end of the list
letters.insert(0, "z")  # adds "z" at index 0
print(letters)

# remove
letters.pop(0)  # removes the item at index 0
letters.remove("c")  # removes the first occurrence of "c"
del letters[1]  # removes the item at index 1
print(letters)
