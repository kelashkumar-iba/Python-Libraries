# LIST:
# Creating a list
my_list = [1, 2, 3, 4, 5]

# Modifying a list
my_list.append(6)
my_list[2] = 10

# Accessing elements
print(my_list[0])  # Output: 1
print(my_list)     # Output: [1, 2, 10, 4, 5, 6]

# Practical Example
# List of names
names = ['Kelash', 'Zeesan', 'Saleh', 'Danish']

# Adding a new name
names.append('Jai')

# Printing all names
for name in names:
    print(name)

# SET:
# Creating a set
my_set = {1, 2, 3, 4, 5}

# Adding elements
my_set.add(6)

# Removing elements
my_set.remove(3)

# Set operations
other_set = {4, 5, 6, 7}
union_set = my_set.union(other_set)
print(union_set)  # Output: {1, 2, 4, 5, 6, 7}

# Practical Example.
# Tags for a blog post
tags = {'python', 'programming', 'tutorial'}

# Adding a new tag
tags.add('beginner')

# Checking if a tag exists
if 'python' in tags:
    print("Python tag found!")

# Removing a tag
tags.remove('tutorial')
print(tags)  # Output: {'python', 'programming', 'beginner'}

# DICTIONARY:
# Creating a dictionary
my_dict = {'name': 'Kelash', 'age': 20, 'city': 'Sukkur'}

# Accessing values
print(my_dict['name'])  # Output: 'Kelash'

# Modifying values
my_dict['age'] = 21

# Adding new key-value pairs
my_dict['job'] = 'Engineer'

# Dictionary operations
del my_dict['city']
print(my_dict)  # Output: {'name': 'Kelash', 'age': 21, 'job': 'Engineer'}

# Practical Example
# Information about a person
person = {
    'Name': 'Ali',
    'Age': 23,
    'City': 'Sukkur'
}

# Adding a new attribute
person['Occupation'] = 'Software Developer'

# Printing all attributes
for key, value in person.items():
    print(f"{key}: {value}")
