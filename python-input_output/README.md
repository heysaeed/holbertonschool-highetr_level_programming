# Python - Input/Output

This project explores various aspects of reading from and writing to files in Python, including JSON serialization and deserialization.

## Learning Objectives

- Open a file in Python.
- Write text to a file and read the full content of a file.
- Understand how to read a file line by line and move the cursor in a file.
- Ensure a file is closed after using it.
- Use the `with` statement for file manipulation.
- Understand JSON and its importance.
- Learn serialization and deserialization processes.
- Convert Python data structures to JSON strings and vice versa.
- Access command line parameters with Python.

## Requirements

### Python Scripts

- Compatible with Ubuntu 20.04 LTS and Python 3.8.5.
- Scripts should include a shebang with `#!/usr/bin/python3`.
- Follow PEP 8 style (version 2.7.*).
- Must end with a new line.
- Must be executable.

### Python Test Cases

- All test files should be placed inside a `tests` folder.
- Test files should have a `.txt` extension.
- Execute tests with: `python3 -m doctest ./tests/*`.
- Include documentation for all modules, classes, and methods.

## Tasks

### 0. Read file

Function that reads a text file (UTF8) and prints it to stdout.

### 1. Write to a file

Function that writes a string to a text file (UTF8) and returns the number of characters written.

### 2. Append to a file

Function that appends a string at the end of a text file (UTF8) and returns the number of characters added.

### 3. To JSON string

Function that returns the JSON representation of an object (string).

### 4. From JSON string to Object

Function that returns an object (Python data structure) represented by a JSON string.

### 5. Save Object to a file

Function that writes an Object to a text file, using a JSON representation.

### 6. Create object from a JSON file

Function that creates an Object from a “JSON file”.

### 7. Load, add, save

Script that adds all arguments to a Python list, and then save them to a file.

### 8. Class to JSON

Function that returns the dictionary description with simple data structure for JSON serialization of an object.

### 9. Student to JSON

Class `Student` that defines a student by first name, last name, and age with a method to retrieve a dictionary representation of the student instance.

### 10. Student to JSON with filter

Class `Student` that defines a student; method to retrieve a dictionary representation of a student instance with a filter.

### 11. Student to disk and reload

Class `Student` that defines a student with methods to serialize to disk and deserialize from disk.

### 12. Pascal's Triangle

Function that returns a list of lists of integers representing the Pascal’s triangle of n.
