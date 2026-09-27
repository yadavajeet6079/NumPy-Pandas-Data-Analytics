import pandas as pd
import numpy as np

# -----------------------------------
# 1. Create Student Performance Dataset
# -----------------------------------

data = {
    "Name": ["Amit", "Rahul", "Priya", "Neha", "Rohit",
             "Ankit", "Pooja", "Vikas", "Kiran", "Sneha"],

    "Gender": ["Male", "Male", "Female", "Female", "Male",
               "Male", "Female", "Male", "Female", "Female"],

    "Age": [20, 21, 20, 22, 21, 20, 22, 21, 20, 22],

    "Study_Hours": [4, 6, 3, 7, 5, 2, 8, 6, 4, 7],

    "Marks": [75, 88, 65, 92, 80, 60, 95, 85, 72, 90]
}

df = pd.DataFrame(data)

# -----------------------------------
# 2. Display Dataset
# -----------------------------------

print("Student Performance Dataset:")
print(df)

# -----------------------------------
# 3. Basic Dataset Information
# -----------------------------------

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

# -----------------------------------
# 4. Statistical Analysis using NumPy
# -----------------------------------

marks = df["Marks"].to_numpy()

print("\nStatistical Analysis of Marks:")

print("Mean Marks:", np.mean(marks))
print("Median Marks:", np.median(marks))
print("Minimum Marks:", np.min(marks))
print("Maximum Marks:", np.max(marks))
print("Standard Deviation:", np.std(marks))
print("Total Marks:", np.sum(marks))

# -----------------------------------
# 5. Students Scoring Above 80
# -----------------------------------

high_scorers = df[df["Marks"] > 80]

print("\nStudents Scoring Above 80:")
print(high_scorers)

# -----------------------------------
# 6. Students Studying More Than 5 Hours
# -----------------------------------

hard_working_students = df[df["Study_Hours"] > 5]

print("\nStudents Studying More Than 5 Hours:")
print(hard_working_students)

# -----------------------------------
# 7. Average Marks by Gender
# -----------------------------------

gender_analysis = df.groupby("Gender")["Marks"].mean()

print("\nAverage Marks by Gender:")
print(gender_analysis)

# -----------------------------------
# 8. Find Top Performing Student
# -----------------------------------

top_student = df.loc[df["Marks"].idxmax()]

print("\nTop Performing Student:")
print(top_student)

# -----------------------------------
# 9. Add Performance Category
# -----------------------------------

df["Performance"] = np.where(
    df["Marks"] >= 80,
    "Good",
    "Needs Improvement"
)

print("\nUpdated Dataset:")
print(df)

# -----------------------------------
# 10. Final Analysis Summary
# -----------------------------------

print("\n--- Analysis Summary ---")

print("Average Marks:", np.mean(marks))
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))
print("Average Study Hours:", np.mean(df["Study_Hours"]))

print("\nNumber of Students Scoring Above 80:",
      len(high_scorers))

print("Number of Students Studying More Than 5 Hours:",
      len(hard_working_students))

#Output
"""Student Performance Dataset:
    Name  Gender  Age  Study_Hours  Marks
0   Amit    Male   20            4     75
1  Rahul    Male   21            6     88
2  Priya  Female   20            3     65
3   Neha  Female   22            7     92
4  Rohit    Male   21            5     80
5  Ankit    Male   20            2     60
6  Pooja  Female   22            8     95
7  Vikas    Male   21            6     85
8  Kiran  Female   20            4     72
9  Sneha  Female   22            7     90

Dataset Shape:
(10, 5)

Column Names:
Index(['Name', 'Gender', 'Age', 'Study_Hours', 'Marks'], dtype='object')

Data Types:
Name           object
Gender         object
Age             int64
Study_Hours     int64
Marks           int64
dtype: object

Statistical Analysis of Marks:
Mean Marks: 80.2
Median Marks: 82.5
Minimum Marks: 60
Maximum Marks: 95
Standard Deviation: 11.27652428720836
Total Marks: 802

Students Scoring Above 80:
    Name  Gender  Age  Study_Hours  Marks
1  Rahul    Male   21            6     88
3   Neha  Female   22            7     92
6  Pooja  Female   22            8     95
7  Vikas    Male   21            6     85
9  Sneha  Female   22            7     90

Students Studying More Than 5 Hours:
    Name  Gender  Age  Study_Hours  Marks
1  Rahul    Male   21            6     88
3   Neha  Female   22            7     92
6  Pooja  Female   22            8     95
7  Vikas    Male   21            6     85
9  Sneha  Female   22            7     90

Average Marks by Gender:
Gender
Female    82.8
Male      77.6
Name: Marks, dtype: float64

Top Performing Student:
Name            Pooja
Gender         Female
Age                22
Study_Hours         8
Marks              95
Name: 6, dtype: object

Updated Dataset:
    Name  Gender  Age  Study_Hours  Marks        Performance
0   Amit    Male   20            4     75  Needs Improvement
1  Rahul    Male   21            6     88               Good
2  Priya  Female   20            3     65  Needs Improvement
3   Neha  Female   22            7     92               Good
4  Rohit    Male   21            5     80               Good
5  Ankit    Male   20            2     60  Needs Improvement
6  Pooja  Female   22            8     95               Good
7  Vikas    Male   21            6     85               Good
8  Kiran  Female   20            4     72  Needs Improvement
9  Sneha  Female   22            7     90               Good

--- Analysis Summary ---
Average Marks: 80.2
Highest Marks: 95
Lowest Marks: 60
Average Study Hours: 5.2

Number of Students Scoring Above 80: 5
Number of Students Studying More Than 5 Hours: 5"""