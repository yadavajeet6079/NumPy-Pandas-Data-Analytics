import pandas as pd

# -----------------------------
# Dataset 1: Employee Details
# -----------------------------

employees = pd.DataFrame({
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Amit", "Rahul", "Priya", "Neha", "Rohit"],
    "Department": ["IT", "HR", "IT", "Sales", "HR"]
})

# -----------------------------
# Dataset 2: Employee Salary
# -----------------------------

salary = pd.DataFrame({
    "Employee_ID": [101, 102, 103, 104, 105],
    "Salary": [50000, 45000, 60000, 55000, 48000],
    "Bonus": [5000, 4000, 6000, 5500, 4500]
})

print("Employee Details:")
print(employees)

print("\nEmployee Salary:")
print(salary)


# -----------------------------
# 1. MERGE
# -----------------------------

merged_df = pd.merge(
    employees,
    salary,
    on="Employee_ID"
)

print("\nMerged DataFrame:")
print(merged_df)


# -----------------------------
# 2. CONCATENATE
# -----------------------------

employees_part1 = pd.DataFrame({
    "Employee_ID": [106, 107],
    "Name": ["Ankit", "Pooja"],
    "Department": ["IT", "Sales"]
})

employees_part2 = pd.DataFrame({
    "Employee_ID": [108, 109],
    "Name": ["Vikas", "Kiran"],
    "Department": ["HR", "IT"]
})

concatenated_df = pd.concat(
    [employees_part1, employees_part2],
    ignore_index=True
)

print("\nConcatenated DataFrame:")
print(concatenated_df)


# -----------------------------
# 3. GROUPBY
# -----------------------------

grouped_df = merged_df.groupby("Department")["Salary"].sum()

print("\nTotal Salary by Department:")
print(grouped_df)


# -----------------------------
# 4. AGGREGATE FUNCTIONS
# -----------------------------

aggregate_df = merged_df.groupby("Department")["Salary"].agg(
    ["sum", "mean", "count", "min", "max"]
)

print("\nAggregate Salary by Department:")
print(aggregate_df)


# -----------------------------
# 5. PIVOT TABLE
# -----------------------------

pivot_table = pd.pivot_table(
    merged_df,
    values="Salary",
    index="Department",
    aggfunc=["sum", "mean", "count"]
)

print("\nPivot Table:")
print(pivot_table)

#Output

"""Employee Details:
   Employee_ID   Name Department
0          101   Amit         IT
1          102  Rahul         HR
2          103  Priya         IT
3          104   Neha      Sales
4          105  Rohit         HR

Employee Salary:
   Employee_ID  Salary  Bonus
0          101   50000   5000
1          102   45000   4000
2          103   60000   6000
3          104   55000   5500
4          105   48000   4500

Merged DataFrame:
   Employee_ID   Name Department  Salary  Bonus
0          101   Amit         IT   50000   5000
1          102  Rahul         HR   45000   4000
2          103  Priya         IT   60000   6000
3          104   Neha      Sales   55000   5500
4          105  Rohit         HR   48000   4500

Concatenated DataFrame:
   Employee_ID   Name Department
0          106  Ankit         IT
1          107  Pooja      Sales
2          108  Vikas         HR
3          109  Kiran         IT

Total Salary by Department:
Department
HR        93000
IT       110000
Sales     55000
Name: Salary, dtype: int64

Aggregate Salary by Department:
               sum     mean  count    min    max
Department                                      
HR           93000  46500.0      2  45000  48000
IT          110000  55000.0      2  50000  60000
Sales        55000  55000.0      1  55000  55000

Pivot Table:
               sum     mean  count
            Salary   Salary Salary
Department                        
HR           93000  46500.0      2
IT          110000  55000.0      2
Sales        55000  55000.0      1"""