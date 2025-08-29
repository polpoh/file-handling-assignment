# file-handling-assignment
📘 Python File Handling & Error Handling Assignment
🔹 Overview

This project demonstrates file handling and exception handling in Python by combining two challenges into a single program:

File Read & Write Challenge 🖋️

Reads text from an input file.

Converts the text into uppercase.

Saves the modified content into a new file.

Error Handling Lab 🧪

Asks the user for a filename.

Tries to open and display its contents.

Handles errors gracefully (e.g., file not found, permission denied, unexpected errors).

🔹 How It Works

When you run the program, you’ll see a menu:

===== FILE HANDLING ASSIGNMENT =====
1. Modify a file
2. Read a file with error handling


If you choose 1, you’ll be asked for an input filename and an output filename.

The program reads the input file.

Converts its text to uppercase.

Writes the result to the output file.

If you choose 2, you’ll be asked for a filename to read.

If the file exists → the contents are displayed.

If not → a helpful error message is shown.

🔹 Example Usage
✅ Option 1: Modify a File
Enter input filename: input.txt
Enter output filename: output.txt
✅ Modified content written to output.txt

✅ Option 2: Read a File with Error Handling
Enter the filename to read: notes.txt

📄 File contents:

This is an example file for testing.


If the file doesn’t exist:

❌ Error: File not found. Please check the filename.

🔹 How to Run the Program

Make sure you have Python 3 installed.

Save the script as file_handling_assignment.py.

Run the script in a terminal or command prompt:

python file_handling_assignment.py


Follow the on-screen instructions.

🔹 Repository Structure
file-handling-assignment/
│── file_handling_assignment.py   # Main Python script
│── README.md                     # Project documentation
│── input.txt                     # (Optional) Sample file for testing

🔹 Outcomes 🎉

By completing this assignment, I learned how to:

Read from and write to files in Python.

Process and modify file content programmatically.

Use try/except to handle common file errors.

Build Python programs that are robust and user-friendly.
