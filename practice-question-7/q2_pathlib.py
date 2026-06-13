# ============================================================
# Q2: pathlib — Working with Paths
# ============================================================
# Use pathlib.Path for ALL path operations in this file.
# No os.path allowed.
# Run from inside practice-question-7/
# ============================================================

from pathlib import Path

# ---------------------------------------------------------------
# QUESTION 2a — Path properties:
# Given the path: data/employees.csv
# Using Path, print:
# 1. The full absolute path
# 2. The filename ("employees.csv")
# 3. The stem ("employees")
# 4. The suffix (".csv")
# 5. The parent directory name
#
# Your solution:
file_path = Path(__file__).parent / "data" / "employees.csv"

print(file_path.absolute())
print(file_path.name)
print(file_path.stem)
print(file_path.suffix)
print(file_path.parent.name)


# ---------------------------------------------------------------
# QUESTION 2b — Reading via pathlib:
# Use Path.read_text() to read data/config.json
# Print the total character count and line count.
#
# Your solution:
config_path = Path(__file__).parent / "data" / "config.json"
config_text = config_path.read_text()
config_lines = config_text.split("\n")

print(len(config_text), len(config_lines))


# ---------------------------------------------------------------
# QUESTION 2c — List files in a directory:
# List all files in the data/ directory.
# Print each filename and its size in bytes.
# Sort by file size, largest first.
#
# Example output:
# employees.csv — 312 bytes
# server.log — 721 bytes
# ...
#
# Hint: Path.stat().st_size gives file size in bytes.
#
# Your solution:
data_path = Path(__file__).parent / "data"
files = [(file.name, file.stat().st_size) for file in data_path.iterdir()]
sorted_files = sorted(files, key=lambda file_entry: -file_entry[1])

for name, size in sorted_files:
    print(f"{name} - {size} bytes")

# ---------------------------------------------------------------
# QUESTION 2d — Create and write:
# Using pathlib only (no open()):
# 1. Create a directory called data/output/ (use mkdir, don't crash if it exists)
# 2. Write the text "Hello from pathlib" to data/output/hello.txt
# 3. Read it back and print it
#
# Your solution:
output_path = Path(__file__).parent / "data" / "output"
try:
    output_path.mkdir()
except FileExistsError:
    print("Directory already exists")

file_path = output_path / "hello.txt"
file_path.write_text("Hello from pathlib")
print(file_path.read_text())


# ---------------------------------------------------------------
# QUESTION 2e (stretch) — Relative to script location:
# Write code that finds the data/ directory RELATIVE TO THIS FILE'S LOCATION,
# not relative to wherever the script is run from.
# Use __file__ and Path to build the path.
# Then print all .csv and .json files found in that data/ folder using glob.
#
# Your solution:
data_path = Path(__file__).parent / "data"
for file in data_path.glob("*.csv"):
    print(file)

for file in data_path.glob("*.json"):
    print(file)
