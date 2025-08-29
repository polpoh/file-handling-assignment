# error_handling_lab.py

def read_user_file():
    filename = input("Enter the filename: ")

    try:
        with open(filename, "r") as f:
            print("File contents:\n")
            print(f.read())

    except FileNotFoundError:
        print("Error: File not found. Please check the filename.")
    except PermissionError:
        print("Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage:
# read_user_file()
