# file_read_write.py

# Writing to a file
with open("sample.txt", "w") as file:
    file.write("Hello, this is Day 9\n")
    file.write("Learning file handling in Python\n")

# Reading from file
with open("sample.txt", "r") as file:
    content = file.read()
    print("File Content:\n", content)