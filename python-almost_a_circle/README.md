# Python - Almost a Circle

This project is a comprehensive review of Python, covering topics such as import, exceptions, class, inheritance, unit testing, file I/O, args/kwargs, and JSON serialization/deserialization. It involves the implementation of a system to manage geometric shapes, specifically rectangles and squares, demonstrating an understanding of OOP, file management, and JSON in Python.

## Background Context

The project involves creating a Base class that serves as the foundation for other classes representing geometric shapes. This project allows for the practice of class inheritance, the use of static and class methods, input validation, and file I/O operations to serialize and deserialize object instances to and from JSON format.

## Learning Objectives

- Implement unit testing and understand its importance in large projects.
- Serialize and deserialize Class objects.
- Read and write JSON files.
- Use *args and **kwargs in function definitions.
- Handle named arguments in functions.

## Requirements

### Python Scripts

- Compatible with Ubuntu 20.04 LTS and Python 3.8.5.
- Scripts should include a shebang with `#!/usr/bin/python3`.
- Follow PEP 8 style (version 2.7.*).
- Must be executable and end with a new line.

### Python Unit Tests

- All test files should end with a new line.
- Test files should be located in a `tests` folder.
- Use the `unittest` module for testing.
- Execute tests with `python3 -m unittest discover tests`.

## Tasks

### 0. If it's not tested it doesn't work

All files, classes, and methods must be unit tested and PEP 8 validated.

### 1. Base class

Create the first class `Base` that manages the `id` attribute in all future classes, to avoid duplicating the same code.

### 2. First Rectangle

Create the class `Rectangle` that inherits from `Base`.

### 3. Validate attributes

Add validation of all setter methods and instantiation in the `Rectangle` class.

### 4. Area first

Implement the `area` method in the `Rectangle` class that returns the area of the instance.

### 5. Display #0

Implement the `display` method in the `Rectangle` class that prints the rectangle instance using the `#` character.

### 6. __str__

Override the `__str__` method in the `Rectangle` class to improve object representation.

### 7. Display #1

Improve the `display` method in the `Rectangle` class to handle `x` and `y` coordinates.

### 8. Update #0

Add the `update` method to the `Rectangle` class to assign arguments to attributes.

### 9. Update #1

Enhance the `update` method in the `Rectangle` class to handle key/value argument assignment.

### 10. And now, the Square!

Create the `Square` class that inherits from `Rectangle`.

### More Tasks...

Further tasks involve enhancing the `Square` and `Rectangle` classes with additional functionality, including JSON serialization/deserialization and file I/O operations.


