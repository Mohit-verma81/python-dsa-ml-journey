# log_analyzer.py

def analyze_logs(filename):
    error_count = 0
    warning_count = 0

    with open(filename, "r") as file:
        for line in file:
            if "ERROR" in line:
                error_count += 1
            elif "WARNING" in line:
                warning_count += 1

    return error_count, warning_count


# Sample log file creation
with open("logs.txt", "w") as f:
    f.write("INFO: System started\n")
    f.write("WARNING: Low memory\n")
    f.write("ERROR: Crash detected\n")
    f.write("ERROR: Disk failure\n")

errors, warnings = analyze_logs("logs.txt")

print("Errors:", errors)
print("Warnings:", warnings)