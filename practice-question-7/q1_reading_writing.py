from pathlib import Path
from datetime import datetime
import re

# ============================================================
# Q1: Reading and Writing Files
# ============================================================
# Run this file from inside the practice-question-7/ folder.
# All paths are relative to that folder.
# ============================================================

# ---------------------------------------------------------------
# QUESTION 1a — Read and print:
# Read data/server.log and print only the lines that contain "ERROR".
# Do NOT load the entire file into memory at once — iterate line by line.
#
# Expected output (4 lines):
# 2024-01-15 08:01:45 ERROR Database connection timeout
# 2024-01-15 08:04:00 ERROR Failed to send email: SMTP timeout
# 2024-01-15 08:05:10 ERROR Database connection timeout
# 2024-01-15 08:07:30 ERROR Unhandled exception in worker thread
#
# Your solution:
server_logs = Path(__file__).parent / "data" / "server.log"

with open(server_logs, mode="r", encoding="utf-8") as logs:
    for line in logs:
        match = re.search(r"error", line, flags=re.IGNORECASE)
        if match:
            print(line.strip())

# ---------------------------------------------------------------
# QUESTION 1b — Write to a file:
# Extract only the ERROR lines from server.log and write them
# to a new file: data/errors_only.txt
# Then read it back and print the line count.
#
# Expected output: "Found 4 errors"
#
# Your solution:
errors = []
server_logs = Path(__file__).parent / "data" / "server.log"

with open(server_logs, mode="r", encoding="utf-8") as logs:
    for line in logs:
        match = re.search(r"error", line, flags=re.IGNORECASE)
        if match:
            errors.append(line)

error_logs = Path(__file__).parent / "data" / "errors_only.txt"

with open(error_logs, mode="w", encoding="utf-8") as error:
    error.writelines(errors)

error_count = 0
with open(error_logs, mode="r", encoding="utf-8") as errors:
    for line in errors:
        error_count += 1

print(f'Found {error_count} {"errors" if error_count > 1 else "error"}')

# ---------------------------------------------------------------
# QUESTION 1c — Count log levels:
# Read server.log and count how many lines are INFO, WARNING, and ERROR.
# Print the counts.
#
# Expected output:
# INFO: 8
# WARNING: 2
# ERROR: 4
#
# Your solution:

info, warning, error = 0, 0, 0

server_logs = Path(__file__).parent / "data" / "server.log"

with open(server_logs) as logs:
    for line in logs:
        if re.search(r"info", line, flags=re.IGNORECASE):
            info += 1
        elif re.search(r"warning", line, flags=re.IGNORECASE):
            warning += 1
        elif re.search(r"error", line, flags=re.IGNORECASE):
            error += 1

print(f"INFO: {info}")
print(f"WARNING: {warning}")
print(f"ERROR: {error}")


# ---------------------------------------------------------------
# QUESTION 1d (stretch) — Append to a file:
# Write a function called `append_log(filepath, level, message)` that:
# - Appends a new log line to the given file
# - Format: "2024-01-15 09:00:00 {LEVEL} {message}"
#   (use datetime.now() for the timestamp)
# - Does NOT overwrite existing content
#
# Call it twice with different messages, then print the last 2 lines
# of the file to verify.
#
# Your solution:
def append_log(filepath, level, message):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log = f"{now} {level.upper()} {message}\n"

    with open(filepath, mode="a", encoding="utf-8") as file:
        file.write(log)


path = Path(__file__).parent / "data" / "demo.log"
append_log(path, "info", "some message")
append_log(path, "error", "another message")

with open(path, mode="r", encoding="utf-8") as file:
    last_two_lines = file.readlines()[-2:]

    for line in last_two_lines:
        print(line, end="")
