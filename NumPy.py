import numpy as np

# From a list
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)  # Output: [1 2 3 4 5]

# From a tuple
arr2 = np.array((1, 2, 3, 4, 5))
print(arr2)  # Output: [1 2 3 4 5]

# -------------------------------------------------

# Using Builtin functions.
# Array of zeros
zeros = np.zeros((2, 3))
print(zeros)  # Output: [[0. 0. 0.]
              #          [0. 0. 0.]]

# Array of ones
ones = np.ones((2, 3))
print(ones)  # Output: [[1. 1. 1.]
             #          [1. 1. 1.]]

# Array of a constant value
full = np.full((2, 3), 7)
print(full)  # Output: [[7 7 7]
             #          [7 7 7]]

# Array of a range of values
range_arr = np.arange(10)
print(range_arr)  # Output: [0 1 2 3 4 5 6 7 8 9]

# Array of evenly spaced values
linspace = np.linspace(0, 1, 5)
print(linspace)  # Output: [0.   0.25 0.5  0.75 1.  ]

# Identity matrix
identity = np.eye(3)
print(identity)  # Output: [[1. 0. 0.]
                #          [0. 1. 0.]
                #          [0. 0. 1.]]

# -------------------------------------------------

# Array Attributes.
arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr.shape)    # Output: (2, 3)
print(arr.size)     # Output: 6
print(arr.ndim)     # Output: 2
print(arr.dtype)    # Output: int64 (or int32 depending on your system)
print(arr.itemsize) # Output: 8 (or 4 depending on the dtype)
print(arr.nbytes)   # Output: 48 (or 24 depending on the dtype)

# ---------------------------------------------------

# Array Indexing and Slicing
arr = np.array([1, 2, 3, 4, 5])

# Indexing
print(arr[0])  # Output: 1
print(arr[-1]) # Output: 5

# Slicing
print(arr[1:3])  # Output: [2 3]
print(arr[:3])   # Output: [1 2 3]
print(arr[2:])   # Output: [3 4 5]

# Multidimensional arrays
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d[0, 1])  # Output: 2
print(arr2d[:, 1])  # Output: [2 5]

# ---------------------------------------------------

# Array Operations.
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print(arr1 + arr2)  # Output: [5 7 9]
print(arr1 - arr2)  # Output: [-3 -3 -3]
print(arr1 * arr2)  # Output: [ 4 10 18]
print(arr1 / arr2)  # Output: [0.25 0.4  0.5 ]

print(arr1 ** 2)    # Output: [1 4 9]

# Here I used lists to know the difference between numpy arrays and lists.
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]

print(lst1 + lst2)  # Output: [1, 2, 3, 4, 5, 6]

# ------------------------------------------------------