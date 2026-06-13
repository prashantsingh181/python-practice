# ============================================================
# Q4: JSON Files
# ============================================================
# Run from inside practice-question-7/
# ============================================================

from pathlib import Path
from json import load, loads, dump, dumps, JSONDecodeError
import datetime

# ---------------------------------------------------------------
# QUESTION 4a — Read and navigate:
# Read data/config.json and print:
# 1. The app name and version: "MyApp v1.0.0"
# 2. The server host and port: "Running on localhost:8080"
# 3. All allowed origins, one per line
#
# Your solution:

file_path = Path(__file__).parent / "data" / "config.json"

try:
    with open(file_path, mode="r", encoding="utf-8") as file:
        config = load(file)

        if isinstance(config, dict):
            app_name = config.get("app_name")
            version = config.get("version")
            server = config.get("server")
            allowed_origins = config.get("allowed_origins")

            if app_name and version:
                print(f"{app_name} v{version}")

            if isinstance(server, dict):
                host = server.get("host")
                port = server.get("port")

                if port and host:
                    print(f"Running on {host}:{port}")

            if isinstance(allowed_origins, list) and len(allowed_origins) > 0:
                for origin in allowed_origins:
                    print(origin)


except FileNotFoundError:
    print("File not found")
except JSONDecodeError:
    print("Not a valid JSON")


# ---------------------------------------------------------------
# QUESTION 4b — Modify and write back:
# Read data/config.json, make these changes IN MEMORY:
# 1. Set server.debug to False
# 2. Change server.port to 9090
# 3. Add a new key "last_updated" at the top level with today's date as a string
#    (use datetime.date.today().isoformat())
#
# Write the modified config back to data/config_updated.json (not the original).
# Then read and print it to verify.
#
# Your solution:

file_path = Path(__file__).parent / "data" / "config.json"

try:
    config = loads(file_path.read_text())

    if isinstance(config, dict):
        server = config.get("server")
        if isinstance(server, dict):
            server["debug"] = False
            server["port"] = 9090

        config["last_updated"] = datetime.date.today().isoformat()


except FileNotFoundError:
    print("File not found")
except JSONDecodeError:
    print("Not a valid JSON")

updated_file_path = Path(__file__).parent / "data" / "config_updated.json"

with open(updated_file_path, mode="w", encoding="utf-8") as file:
    dump(config, file, indent=2)

with open(updated_file_path, encoding="utf-8") as file:
    print(file.read())

# ---------------------------------------------------------------
# QUESTION 4c — Build and write JSON from scratch:
# You have this data:
students = [
    {"name": "Alice", "grades": [88, 92, 79, 95]},
    {"name": "Bob", "grades": [72, 68, 85, 90]},
    {"name": "Carol", "grades": [95, 98, 92, 97]},
]
#
# For each student, compute their average grade (round to 2 decimal places).
# Write a NEW JSON file to data/student_report.json in this format:
# [
#   {"name": "Alice", "average": 88.5, "grade": "B"},
#   ...
# ]
#
# Grade scale: >= 90 → "A", >= 80 → "B", >= 70 → "C", else → "F"
#
# Your solution:
updated_students = []
for student in students:
    updated_student = {"name": student["name"]}
    if len(student["grades"]) > 0:
        total = sum(student["grades"])
        average = round(total / len(student["grades"]), 2)
        updated_student["average"] = average
        if average >= 90:
            updated_student["grade"] = "A"
        elif average >= 80:
            updated_student["grade"] = "B"
        elif average >= 70:
            updated_student["grade"] = "C"
        else:
            updated_student["grade"] = "F"
    updated_students.append(updated_student)

output_file_path = Path(__file__).parent / "data" / "student_report.json"

with open(output_file_path, mode="w", encoding="utf-8") as file:
    dump(updated_students, file, indent=2)


# ---------------------------------------------------------------
# QUESTION 4d (stretch) — Safe config loader:
# Write a function called `load_config(filepath, defaults)` that:
# - Tries to read and parse the JSON file at filepath
# - If the file doesn't exist, returns defaults
# - If the file exists but contains invalid JSON, raises a ValueError
#   with a message like: "Invalid JSON in config.json: ..."
# - If successful, MERGES the file's values into defaults
#   (file values override defaults, but defaults fill in missing keys)
#
# Test all three paths: valid file, missing file, invalid JSON.
#
# Your solution:


def load_config(filepath, defaults):
    try:
        with open(filepath, mode="r", encoding="utf-8") as file:
            config = load(file)
            if isinstance(config, dict) and isinstance(defaults, dict):
                return {**defaults, **config}
            return config
    except FileNotFoundError:
        return defaults
    except JSONDecodeError:
        raise ValueError(f"Invalid JSON in config.json: {Path(file_path.name)}")


print(
    load_config(
        Path(__file__).parent / "data" / "config.json",
        {"app_name": "New App"},
    )
)

print(
    load_config(
        Path(__file__).parent / "data" / "some_config.json",
        {"app_name": "New App"},
    )
)
