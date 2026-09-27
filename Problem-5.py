import pandas as pd

# Read CSV file
df = pd.read_csv("students.csv")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Display last 5 rows
print("\nLast 5 Rows:")
print(df.tail())

# Check number of rows and columns
print("\nNumber of Rows and Columns:")
print(df.shape)

# Display column names
print("\nColumn Names:")
print(df.columns)

# Check data types
print("\nData Types:")
print(df.dtypes)

# Display information about the dataset
print("\nDataset Information:")
df.info()

# Display statistical summary
print("\nStatistical Description:")
print(df.describe())

#Output
"""First 5 Rows:
    Name  Age  Marks     City
0   Amit   20     85  Lucknow
1  Rahul   21     90    Delhi
2  Priya   20     78   Kanpur
3   Neha   22     92   Jaipur
4  Rohit   21     88     Agra

Last 5 Rows:
    Name  Age  Marks     City
2  Priya   20     78   Kanpur
3   Neha   22     92   Jaipur
4  Rohit   21     88     Agra
5  Ankit   20     75  Lucknow
6  Pooja   22     95    Delhi

Number of Rows and Columns:
(7, 4)

Column Names:
Index(['Name', 'Age', 'Marks', 'City'], dtype='object')

Data Types:
Name     object
Age       int64
Marks     int64
City     object
dtype: object

Dataset Information:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 7 entries, 0 to 6
Data columns (total 4 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   Name    7 non-null      object
 1   Age     7 non-null      int64 
 2   Marks   7 non-null      int64 
 3   City    7 non-null      object
dtypes: int64(2), object(2)
memory usage: 356.0+ bytes

Statistical Description:
             Age      Marks
count   7.000000   7.000000
mean   20.857143  86.142857
std     0.899735   7.335498
min    20.000000  75.000000
25%    20.000000  81.500000
50%    21.000000  88.000000
75%    21.500000  91.000000
max    22.000000  95.000000"""