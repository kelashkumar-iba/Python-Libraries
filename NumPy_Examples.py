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

# -------------------------------------------------
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

# -----------------------------------------------------
# Example Question 3: Slicing and Indexing

import numpy as np

arr = np.array([[1, 2, 3], 
                [4, 5, 6], 
                [7, 8, 9]])

# Extract sub-array
sub_array = arr[1:3, 1:3]

print("Original Array:")
print(arr)
print("\nSub-array (2nd and 3rd rows, 2nd and 3rd columns):")
print(sub_array)

# -----------------------------------------------------
# Example Question 4: Statistical Operations

import numpy as np

data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# Calculate statistics
mean = np.mean(data)
median = np.median(data)
std_dev = np.std(data)

print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)

# -----------------------------------------------------
# Example Question 5: Matrix Multiplication
import numpy as np

A = np.array([[1, 2], 
              [3, 4]])

B = np.array([[5, 6], 
              [7, 8]])

# Perform matrix multiplication
C = np.dot(A, B)

print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)
print("\nMatrix Multiplication (A dot B):")
print(C)

# -----------------------------------------------------

