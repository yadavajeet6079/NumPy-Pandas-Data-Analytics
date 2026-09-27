import pandas as pd

# Create a DataFrame
data = {
    "Name": ["Amit", "Rahul", "Priya", "Neha", "Rohit", "Ankit", "Pooja"],
    "Age": [20, 21, 20, 22, 21, 20, 22],
    "Marks": [85, 90, 78, 92, 88, 75, 95],
    "City": ["Lucknow", "Delhi", "Kanpur", "Jaipur", "Agra", "Lucknow", "Delhi"]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# 1. Select specific columns
print("\nSelected Columns (Name and Marks):")
print(df[["Name", "Marks"]])

# 2. Select specific rows
print("\nSelected Rows (First 3 Students):")
print(df.iloc[0:3])

# 3. Filter records based on a condition
print("\nStudents with Marks Greater Than 85:")
print(df[df["Marks"] > 85])

# 4. Apply multiple filtering conditions
print("\nStudents with Marks Greater Than 80 and Age Less Than 22:")
print(df[(df["Marks"] > 80) & (df["Age"] < 22)])

# 5. Sort data in ascending order
print("\nMarks in Ascending Order:")
print(df.sort_values(by="Marks", ascending=True))

# 6. Sort data in descending order
print("\nMarks in Descending Order:")
print(df.sort_values(by="Marks", ascending=False))

#Output
"""Original DataFrame:
    Name  Age  Marks     City
0   Amit   20     85  Lucknow
1  Rahul   21     90    Delhi
2  Priya   20     78   Kanpur
3   Neha   22     92   Jaipur
4  Rohit   21     88     Agra
5  Ankit   20     75  Lucknow
6  Pooja   22     95    Delhi

Selected Columns (Name and Marks):
    Name  Marks
0   Amit     85
1  Rahul     90
2  Priya     78
3   Neha     92
4  Rohit     88
5  Ankit     75
6  Pooja     95

Selected Rows (First 3 Students):
    Name  Age  Marks     City
0   Amit   20     85  Lucknow
1  Rahul   21     90    Delhi
2  Priya   20     78   Kanpur

Students with Marks Greater Than 85:
    Name  Age  Marks    City
1  Rahul   21     90   Delhi
3   Neha   22     92  Jaipur
4  Rohit   21     88    Agra
6  Pooja   22     95   Delhi

Students with Marks Greater Than 80 and Age Less Than 22:
    Name  Age  Marks     City
0   Amit   20     85  Lucknow
1  Rahul   21     90    Delhi
4  Rohit   21     88     Agra

Marks in Ascending Order:
    Name  Age  Marks     City
5  Ankit   20     75  Lucknow
2  Priya   20     78   Kanpur
0   Amit   20     85  Lucknow
4  Rohit   21     88     Agra
1  Rahul   21     90    Delhi
3   Neha   22     92   Jaipur
6  Pooja   22     95    Delhi

Marks in Descending Order:
    Name  Age  Marks     City
6  Pooja   22     95    Delhi
3   Neha   22     92   Jaipur
1  Rahul   21     90    Delhi
4  Rohit   21     88     Agra
0   Amit   20     85  Lucknow
2  Priya   20     78   Kanpur
5  Ankit   20     75  Lucknow"""