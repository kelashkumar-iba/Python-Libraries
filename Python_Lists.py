# Creating a new List:
# Empty list
empty_list = []

# List of integers
int_list = [1, 2, 3, 4, 5]

# List of strings
str_list = ["apple", "banana", "cherry"]

# Mixed data types
mixed_list = [1, "hello", 3.14, True]

# List of lists (nested list)
nested_list = [[1, 2], [3, 4], [5, 6]]

# ---------------------------------------------
# Accessing elements
print(int_list[0])  # Output: 1
print(str_list[1])  # Output: banana

# Negative indexing
print(int_list[-1])  # Output: 5
print(str_list[-2])  # Output: banana

# ----------------------------------------------
# Slicing lists
print(int_list[1:3])  # Output: [2, 3]
print(str_list[:2])   # Output: ['apple', 'banana']
print(int_list[2:])   # Output: [3, 4, 5]

# Step slicing
print(int_list[::2])  # Output: [1, 3, 5]

# -----------------------------------------------
# Changing elements
int_list[0] = 10
print(int_list)  # Output: [10, 2, 3, 4, 5]

# Changing a range of elements
int_list[1:3] = [20, 30]
print(int_list)  # Output: [10, 20, 30, 4, 5]

# -------------------------------------------------
# Append: adds a single element to the end
int_list.append(6)
print(int_list)  # Output: [10, 20, 30, 4, 5, 6]

# Extend: adds multiple elements to the end
int_list.extend([7, 8])
print(int_list)  # Output: [10, 20, 30, 4, 5, 6, 7, 8]

# Insert: adds an element at a specific position
int_list.insert(2, 25)
print(int_list)  # Output: [10, 20, 25, 30, 4, 5, 6, 7, 8]

# -------------------------------------------------
# Remove: removes the first occurrence of a value
int_list.remove(25)
print(int_list)  # Output: [10, 20, 30, 4, 5, 6, 7, 8]

# Pop: removes and returns the element at a specific index (default is the last element)
last_element = int_list.pop()
print(last_element)  # Output: 8
print(int_list)      # Output: [10, 20, 30, 4, 5, 6, 7]

# Del: removes an element or a slice from the list
del int_list[0]
print(int_list)  # Output: [20, 30, 4, 5, 6, 7]

del int_list[1:3]
print(int_list)  # Output: [20, 5, 6, 7]

# Clear: removes all elements from the list
int_list.clear()
print(int_list)  # Output: []

# -------------------------------------------------
# List Operations
# Concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print(combined_list)  # Output: [1, 2, 3, 4, 5, 6]

# Repetition
repeated_list = list1 * 3
print(repeated_list)  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Membership
print(2 in list1)  # Output: True
print(4 in list1)  # Output: False

# ---------------------------------------------------
# List Methods:
# Append
list1.append(4)
print(list1)  # Output: [1, 2, 3, 4]

# Count: counts the occurrences of a value
print(list1.count(2))  # Output: 1

# Index: finds the index of the first occurrence of a value
print(list1.index(3))  # Output: 2

# Sort: sorts the list in ascending order
list1.sort()
print(list1)  # Output: [1, 2, 3, 4]

# Reverse: reverses the list
list1.reverse()
print(list1)  # Output: [4, 3, 2, 1]

# Copy: returns a shallow copy of the list
list_copy = list1.copy()
print(list_copy)  # Output: [4, 3, 2, 1]



