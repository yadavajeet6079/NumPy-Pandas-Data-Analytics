import pandas as pd

# Create a DataFrame
data = {
    "Name": ["Amit", "Rahul", "Priya", "Neha", "Rohit"],
    "Age": [20, 21, 20, 22, 21],
    "Marks": [85, 90, 78, 92, 88]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Process the DataFrame
# Add a new column for Grade
df["Grade"] = ["A", "A+", "B", "A+", "A"]

print("\nProcessed DataFrame:")
print(df)

# Export the final DataFrame to a CSV file
file_name = "final_student_data.csv"
df.to_csv(file_name, index=False)

print("\nData exported successfully to:", file_name)

# Verify the exported file
verified_df = pd.read_csv(file_name)

print("\nVerified Exported Data:")
print(verified_df)

#Output
"""Original DataFrame:
    Name  Age  Marks
0   Amit   20     85
1  Rahul   21     90
2  Priya   20     78
3   Neha   22     92
4  Rohit   21     88

Processed DataFrame:
    Name  Age  Marks Grade
0   Amit   20     85     A
1  Rahul   21     90    A+
2  Priya   20     78     B
3   Neha   22     92    A+
4  Rohit   21     88     A

Data exported successfully to: final_student_data.csv

Verified Exported Data:
    Name  Age  Marks Grade
0   Amit   20     85     A
1  Rahul   21     90    A+
2  Priya   20     78     B
3   Neha   22     92    A+
4  Rohit   21     88     A"""