import pandas as pd
marks = pd.Series([85, 90, 78, 92, 88])

print("Pandas Series:")
print(marks)
data = {
    "Name": ["Amit", "Rahul", "Priya", "Neha", "Rohit"],
    "Age": [20, 21, 20, 22, 21],
    "Marks": [85, 90, 78, 92, 88]
}
df = pd.DataFrame(data)
print("\nStudent DataFrame:")
print(df)
print("\nColumn Names:")
print(df.columns)
print("\nIndex:")
print(df.index)
df["Grade"] = ["A", "A+", "B", "A+", "A"]
print("\nUpdated DataFrame:")
print(df)

#Output
"""Pandas Series:
0    85
1    90
2    78
3    92
4    88
dtype: int64

Student DataFrame:
    Name  Age  Marks
0   Amit   20     85
1  Rahul   21     90
2  Priya   20     78
3   Neha   22     92
4  Rohit   21     88

Column Names:
Index(['Name', 'Age', 'Marks'], dtype='object')

Index:
RangeIndex(start=0, stop=5, step=1)

Updated DataFrame:
    Name  Age  Marks Grade
0   Amit   20     85     A
1  Rahul   21     90    A+
2  Priya   20     78     B
3   Neha   22     92    A+
4  Rohit   21     88     A"""