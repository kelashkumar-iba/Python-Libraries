# Iterating over a list
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

# Iterating over a string
for char in "Python":
    print(char)


# Using break
for num in range(10):
    if num == 5:
        break
    print(num)

# Using continue
for num in range(10):
    if num % 2 == 0:
        continue
    print(num)


# Printing numbers from 1 to 5 using the (while loop)
count = 1
while count <= 5:
    print(count)
    count += 1