# ============================================================
# Q3: CSV Files
# ============================================================
# Use Python's built-in `csv` module. No pandas.
# Run from inside practice-question-7/
# ============================================================

import csv
from pathlib import Path
from collections import defaultdict

# ---------------------------------------------------------------
# QUESTION 3a — Read and filter:
# Read data/employees.csv using DictReader.
# Print the name and salary of every Engineering employee,
# sorted by salary descending.
#
# Expected output:
# Grace - 120000
# Carol - 110000
# Judy - 98000
# Alice - 95000
# Eve - 72000
#
# Note: all CSV values are strings — convert salary to int before sorting.
#
# Your solution:

file_path = Path(__file__).parent / "data" / "employees.csv"

employees = []
with open(file_path, mode="r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for employee in reader:
        if employee["department"] == "Engineering":
            employees.append(employee)

sorted_employees = sorted(employees, key=lambda employee: -int(employee["salary"]))

for employee in sorted_employees:
    print(f"{employee['name']} - {employee['salary']}")


# ---------------------------------------------------------------
# QUESTION 3b — Aggregate:
# Read employees.csv and compute the average salary per department.
# Print each department and its average, sorted alphabetically by department.
#
# Expected output:
# Engineering: 99000.0
# HR: 66500.0
# Marketing: 78333.33...
#
# Your solution:


file_path = Path(__file__).parent / "data" / "employees.csv"

department_dict = defaultdict(list)

with open(file_path, mode="r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for employee in reader:
        department_dict[employee["department"]].append(employee)

sorted_department_dict = sorted(department_dict.items(), key=lambda item: item[0])

for department, employees in sorted_department_dict:
    # total = sum([int(employee['salary']) for employee in employees])
    total = 0
    for employee in employees:
        try:
            salary = int(employee["salary"])
        except ValueError:
            print(f"ValueError for {employee['salary']}")
            salary = 0

        total += salary

    average = total / len(employees)
    print(f"{department}: {average}")


# ---------------------------------------------------------------
# QUESTION 3c — Write a CSV:
# Filter employees with salary > 90000 and write them to data/high_earners.csv
# Keep all original columns. Then read it back and verify the row count.
#
# Expected: "4 high earners written"
#
# Your solution:

file_path = Path(__file__).parent / "data" / "employees.csv"

lines = []

with open(file_path, mode="r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)

    for employee in reader:
        try:
            salary = int(employee["salary"])
            if salary > 90000:
                lines.append(employee)
        except ValueError:
            print(f"ValueError for {employee['salary']}")

output_file_path = Path(__file__).parent / "data" / "high_earners.csv"

if len(lines) > 0:
    with open(output_file_path, mode="w", encoding="utf-8", newline="") as output_file:
        writer = csv.writer(output_file)
        writer.writerow(lines[0].keys())
        writer.writerows([line.values() for line in lines])

    with open(output_file_path, mode="r", encoding="utf-8", newline="") as output_file:
        reader = csv.DictReader(output_file)
        count = 0
        for row in reader:
            count += 1
        print(f"{count} high earners written")


# ---------------------------------------------------------------
# QUESTION 3d (stretch) — Transform and write:
# Read employees.csv, add a new column called "seniority" based on years_of_experience:
#   < 3 years  → "Junior"
#   3-6 years  → "Mid"
#   > 6 years  → "Senior"
#
# Write the updated data (all original columns + seniority) to data/employees_leveled.csv
#
# Your solution:

file_path = Path(__file__).parent / "data" / "employees.csv"

with open(file_path, mode="r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)

    employees = []

    for employee in reader:
        try:
            exp = int(employee["years_of_experience"])
            if exp < 3:
                employee["seniority"] = "Junior"
            elif exp <= 6:
                employee["seniority"] = "Mid"
            else:
                employee["seniority"] = "Senior"

        except ValueError:
            print(f"ValueError for {employee['years_of_experience']}")
            employee["seniority"] = ""

        employees.append(employee)

output_file_path = Path(__file__).parent / "data" / "employees_leveled.csv"

if len(employees) > 0:
    with open(output_file_path, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(employees[0].keys())
        writer.writerows([emp.values() for emp in employees])
