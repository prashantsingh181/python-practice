# ============================================================
# Q5: Mini Project — Employee Report Generator
# ============================================================
# Combine everything: pathlib, CSV reading, JSON writing, file writing.
# Run from inside practice-question-7/
#
# Build a function called `generate_report(csv_path, output_dir)` that:
#
# 1. Reads the employees CSV from csv_path
#
# 2. Computes a summary dict:
#    {
#      "total_employees": 10,
#      "departments": {
#        "Engineering": {
#          "count": 5,
#          "avg_salary": 99000.0,
#          "highest_paid": "Grace"
#        },
#        ...
#      },
#      "company_avg_salary": 86300.0,
#      "highest_paid_overall": "Grace"
#    }
#
# 3. Writes the summary to output_dir/summary.json (pretty-printed, indent=2)
#
# 4. Writes a plain text report to output_dir/report.txt in this format:
#    === Employee Report ===
#    Total employees: 10
#    Company average salary: ₹86,300.00
#
#    Engineering (5 employees)
#      Average salary: ₹99,000.00
#      Highest paid: Grace
#
#    HR (2 employees)
#      ...
#
# 5. Returns the summary dict
#
# Requirements:
# - Use pathlib for all paths
# - Create output_dir if it doesn't exist
# - Use f"₹{amount:,.2f}" for currency formatting
# - Departments should be sorted alphabetically in the report
#
# Test it:
# summary = generate_report("data/employees.csv", "data/output")
# print(f"Report written. {summary['total_employees']} employees across "
#       f"{len(summary['departments'])} departments.")
#
# Your solution:

from collections import defaultdict
from pathlib import Path
import json
import csv


def group_by_department(csv_path):
    department_dict = defaultdict(list)

    with open(csv_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for employee in reader:
            department_dict[employee["department"]].append(employee)

    return department_dict


def compute_summary_dict_and_report(department_dict):

    sorted_department_data = sorted(department_dict.items(), key=lambda item: item[0])

    total_employees = 0
    total_employees_salary = 0
    highest_overall = None
    summary_dict = {}
    dept_summary_dict = {}
    dept_summary_string = ""
    summary_string = ""

    for department, employees in sorted_department_data:
        count = 0
        total_salary = 0
        highest = None

        for employee in employees:
            count += 1
            total_employees += 1
            try:
                salary = int(employee["salary"])
            except ValueError:
                salary = 0

            total_salary += salary
            total_employees_salary += salary
            if highest is None or salary > highest["salary"]:
                highest = {**employee, "salary": salary}

        avg_salary = total_salary / count

        dept_summary_dict[department] = {
            "count": count,
            "avg_salary": avg_salary,
            "highest_paid": highest["name"],
        }

        dept_summary_string += f"""{department} ({count} {"employees" if count > 1 else "employee"})
  Average Salary: ₹{avg_salary:,.2f}
  Highest Paid: {highest['name']}

"""
        if highest_overall is None or highest["salary"] > highest_overall["salary"]:
            highest_overall = highest

    company_avg_salary = total_employees_salary / total_employees

    summary_dict["total_employees"] = total_employees
    summary_dict["departments"] = dept_summary_dict
    summary_dict["company_avg_salary"] = company_avg_salary
    summary_dict["highest_overall"] = highest_overall["name"]

    summary_string += f"""=== Employee Report ===
Total employees: {total_employees}
Company average salary: ₹{company_avg_salary:,.2f}

{dept_summary_string}
"""

    return (summary_dict, summary_string)


def write_json_and_report(summary_dict, summary_string, output_dir):

    output_dir_path = Path(output_dir)

    if not output_dir_path.exists():
        output_dir_path.mkdir()

    with open(output_dir_path / "summary.json", mode="w", encoding="utf-8") as file:
        json.dump(summary_dict, file, indent=2)

    with open(output_dir_path / "report.txt", mode="w", encoding="utf-8") as file:
        file.write(summary_string)

    print(
        f"Report written. {summary_dict['total_employees']} employees across {len(summary_dict['departments'])} departments.",
    )


def generate_report(csv_path, output_dir):

    department_dict = group_by_department(csv_path)

    summary_dict, summary_string = compute_summary_dict_and_report(department_dict)

    write_json_and_report(summary_dict, summary_string, output_dir)

    return summary_dict


generate_report("data/employees.csv", "data/output")
