def read_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()

    except FileNotFoundError:
        return "File not found."

    except PermissionError:
        return "Permission denied."

    except Exception as e:
        return f"Error: {e}"


print(read_file("sample.txt"))