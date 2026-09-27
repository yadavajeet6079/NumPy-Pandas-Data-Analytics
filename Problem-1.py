import numpy as np
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print("Array:")
print(arr)
print("\nShape:", arr.shape)
print("Size:", arr.size)
print("Data Type:", arr.dtype)
one_d = np.array([1, 2, 3, 4, 5])

print("\nOne-Dimensional Array:")
print(one_d)
two_d = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\nTwo-Dimensional Array:")
print(two_d)

print("Shape of 2D Array:", two_d.shape)

#Outputs
"""Array:
[ 10  20  30  40  50  60  70  80  90 100]

Shape: (10,)
Size: 10
Data Type: int64

One-Dimensional Array:
[1 2 3 4 5]

Two-Dimensional Array:
[[1 2 3]
 [4 5 6]]
Shape of 2D Array: (2, 3)"""