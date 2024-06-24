# Example Question 1: Array Creation and Manipulation:
# Task: Create a 1D NumPy array of the first 20 even numbers and reshape it into a 2D array with 4 rows and 5 columns.

import numpy as np

# Create a 1D array of the first 20 even numbers
even_numbers = np.arange(2, 41, 2)

# Reshape the array to 4 rows and 5 columns
reshaped_array = even_numbers.reshape(4, 5)

print("1D Array of even numbers:")
print(even_numbers)
print("\nReshaped 2D Array (4x5):")
print(reshaped_array)


# Example Question 2: Element-wise Operations

import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9, 10])

# Element-wise operations
addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)

