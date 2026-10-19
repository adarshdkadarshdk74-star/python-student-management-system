# Python Student Management System

My first Python project — a beginner-friendly Student Management System built using Python.

## About the Project

The Student Management System is a beginner-friendly Python project that allows users to manage student names through a simple, menu-driven console application.

I built this project to practise Python programming concepts, improve my problem-solving skills, and learn file handling and permanent data storage.

## Features

* **Add Student:** Add a new student's name.
* **View Students:** Display all registered students in a numbered list.
* **Search Student:** Search for a student by name.
* **Update Student:** Change an existing student's name.
* **Delete Student:** Remove a student from the list.
* **Input Validation:** Reject empty names and names containing only numbers when adding or updating students.
* **Duplicate Prevention:** Prevent students from being added with duplicate names and prevent duplicate names during updates.
* **Case-Insensitive Search:** Find students regardless of uppercase or lowercase letters.
* **Permanent Storage:** Save student records in a JSON file named `student.json`.
* **Automatic Loading:** Load previously saved student records when the program starts.
* **Error Handling:** Handle invalid menu input, missing files, and invalid JSON data.
* **Data Validation:** Check whether loaded student data is a list containing strings.

## Technologies Used

* Python 3
* JSON
* File Handling
* Python Lists
* Functions
* Loops and Conditional Statements
* String Methods
* Exception Handling
* Git and GitHub

## How to Run the Project

### Prerequisites

Python 3 must be installed on your computer.

### Steps

1. Download or clone this repository.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run the following command:

```bash
python student_management_system.py
```

5. Follow the instructions displayed in the terminal.

## How to Use

When you run the program, a menu appears with six options:

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit

Enter the number of the option you want to use and follow the instructions displayed in the terminal.

## Data Storage

Student records are stored in a JSON file named `student.json`.

The program loads previously saved records when it starts and saves changes when students are added, updated, or deleted.

This allows student records to remain available after the program closes.

## Python Concepts Practised

This project helped me practise:

* Variables and user input
* Lists and list methods
* Functions
* `while` and `for` loops
* `if`, `elif`, and `else`
* String methods such as `.strip()`, `.lower()`, and `.isdigit()`
* `break` and `for-else`
* JSON serialization and deserialization using `json.dump()` and `json.load()`
* File handling using `open()`
* Exception handling with `try-except`
* Handling `FileNotFoundError` and `json.JSONDecodeError`
* Data type checking using `isinstance()`
* CRUD operations: Create, Read, Update, and Delete

## Current Limitations

* Student records contain only names.
* Data is stored in a local JSON file rather than a database.
* The application runs in the terminal and does not have a graphical user interface.

## Future Improvements

* Store additional student information, such as branch and semester.
* Use an SQLite database to manage student records.
* Add automated tests.
* Improve recovery of invalid or corrupted saved data.
* Develop a graphical user interface.

## Author

Created as a Python learning project to improve my programming and problem-solving skills.