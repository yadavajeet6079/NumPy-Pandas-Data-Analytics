import pandas as pd
import numpy as np

# Create a dataset containing missing values
data = {
    "Name": ["Amit", "Rahul", "Priya", "Neha", "Rohit"],
    "Age": [20, 21, np.nan, 22, 21],
    "Marks": [85, np.nan, 78, 92, np.nan],
    "City": ["Lucknow", "Delhi", "Kanpur", np.nan, "Agra"]
}

df = pd.DataFrame(data)

# Display dataset before handling missing values
print("Dataset Before Handling Missing Values:")
print(df)

# Identify missing values using isnull()
print("\nMissing Values using isnull():")
print(df.isnull())

# Identify missing values using isna()
print("\nMissing Values using isna():")
print(df.isna())

# Count missing values in each column
print("\nCount of Missing Values in Each Column:")
print(df.isnull().sum())

# Remove rows containing missing values
df_removed = df.dropna()

print("\nDataset After Removing Rows with Missing Values:")
print(df_removed)

# Fill missing values using appropriate methods
df_filled = df.copy()

# Fill missing Age with the mean age
df_filled["Age"] = df_filled["Age"].fillna(df_filled["Age"].mean())

# Fill missing Marks with the mean marks
df_filled["Marks"] = df_filled["Marks"].fillna(df_filled["Marks"].mean())

# Fill missing City with "Unknown"
df_filled["City"] = df_filled["City"].fillna("Unknown")

# Display dataset after filling missing values
print("\nDataset After Filling Missing Values:")
print(df_filled)

#Output
"""Dataset Before Handling Missing Values:
    Name   Age  Marks     City
0   Amit  20.0   85.0  Lucknow
1  Rahul  21.0    NaN    Delhi
2  Priya   NaN   78.0   Kanpur
3   Neha  22.0   92.0      NaN
4  Rohit  21.0    NaN     Agra

Missing Values using isnull():
    Name    Age  Marks   City
0  False  False  False  False
1  False  False   True  False
2  False   True  False  False
3  False  False  False   True
4  False  False   True  False

Missing Values using isna():
    Name    Age  Marks   City
0  False  False  False  False
1  False  False   True  False
2  False   True  False  False
3  False  False  False   True
4  False  False   True  False

Count of Missing Values in Each Column:
Name     0
Age      1
Marks    2
City     1
dtype: int64

Dataset After Removing Rows with Missing Values:
   Name   Age  Marks     City
0  Amit  20.0   85.0  Lucknow

Dataset After Filling Missing Values:
    Name   Age  Marks     City
0   Amit  20.0   85.0  Lucknow
1  Rahul  21.0   85.0    Delhi
2  Priya  21.0   78.0   Kanpur
3   Neha  22.0   92.0  Unknown
4  Rohit  21.0   85.0     Agra"""