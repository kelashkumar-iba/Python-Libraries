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

# Nested for loop
for i in range(3):
    for j in range(2):
        print(f'i = {i}, j = {j}')

# Printing numbers from 1 to 5 using the (while loop)
count = 1
while count <= 5:
    print(count)
    count += 1

# Practical example.
# Find prime numbers within a range
start = 10
end = 45

for num in range(start, end + 1):
    # Prime numbers are greater than 1.
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)

#Loops.
# Practice By Kelash.


