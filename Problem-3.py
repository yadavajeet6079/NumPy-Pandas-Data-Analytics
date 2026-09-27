import numpy as np
data = np.array([10, 20, 30, 40, 50])

print("Dataset:")
print(data)
print("\nMathematical Operations:")
# Addition
print("Addition:", data + 5)
# Subtraction
print("Subtraction:", data - 5)
# Multiplication
print("Multiplication:", data * 2)
# Division
print("Division:", data / 2)
# Statistical Operations
print("\nStatistical Operations:")
# Mean
print("Mean:", np.mean(data))
# Median
print("Median:", np.median(data))
# Minimum
print("Minimum:", np.min(data))
# Maximum
print("Maximum:", np.max(data))
# Standard Deviation
print("Standard Deviation:", np.std(data))
# Sum
print("Sum:", np.sum(data))

#Output
"""Dataset:
[10 20 30 40 50]

Mathematical Operations:
Addition: [15 25 35 45 55]
Subtraction: [ 5 15 25 35 45]
Multiplication: [ 20  40  60  80 100]
Division: [ 5. 10. 15. 20. 25.]

Statistical Operations:
Mean: 30.0
Median: 30.0
Minimum: 10
Maximum: 50
Standard Deviation: 14.142135623730951
Sum: 150"""