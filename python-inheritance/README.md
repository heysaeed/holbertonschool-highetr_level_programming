# Python - Inheritance

This project explores the concept of inheritance in Python, including how to inherit methods and attributes from parent classes to create subclasses, override inherited methods, and utilize built-in functions related to inheritance.

## Learning Objectives

- Understand superclass, baseclass, or parentclass and subclass concepts.
- Learn how to list all attributes and methods of a class or instance.
- Discover when an instance can have new attributes.
- Learn how to inherit a class from another and define a class with multiple base classes.
- Understand the default class every class inherits from.
- Learn how to override methods or attributes inherited from the base class.
- Know which attributes or methods are available by heritage to subclasses.
- Understand the purpose of inheritance.
- Learn how to use `isinstance`, `issubclass`, `type`, and `super` built-in functions.

## Requirements

### Python Scripts

- Use Python 3.8.5, with all scripts starting with `#!/usr/bin/python3`.
- Follow PEP 8 styling (version 2.7.*).
- Include a `README.md` at the root of the project directory.
- Ensure all files are executable.

### Python Test Cases

- Ensure all files end with a new line.
- Place all test files inside a `tests` folder with `.txt` extensions.
- Execute all tests with `python3 -m doctest ./tests/*`.
- Include documentation for all modules, classes, and methods.

## Tasks

### 0. Lookup

Function that returns the list of available attributes and methods of an object.

### 1. My list

A class `MyList` that inherits from `list` and has a public instance method to print the list in ascending order.

### 2. Exact same object

Function to check if an object is exactly an instance of a specified class.

### 3. Same class or inherit from

Function to check if an object is an instance of, or if it is an instance of a class that inherited from, a specified class.

### 4. Only sub class of

Function to check if an object is an instance of a class that inherited (directly or indirectly) from a specified class.

### 5. Geometry module

An empty class `BaseGeometry`.

### 6. Improve Geometry

Expanding `BaseGeometry` with a public instance method `area()` that raises an Exception with a specific message.

### 7. Integer validator

Enhancing `BaseGeometry` with a validator method to check if a value is an integer and greater than 0.

### 8. Rectangle

A class `Rectangle` that inherits from `BaseGeometry`, initialized with `width` and `height`.

### 9. Full rectangle

Enhancing the `Rectangle` class to implement the `area()` method and a `__str__` method to return rectangle description.

### 10. Square #1

A class `Square` that inherits from `Rectangle`, initialized with `size`.

### 11. Square #2

Enhancing the `Square` class to implement a `__str__` method returning the square description.

## Additional Information

This project is designed to help students understand the principles of inheritance in Python, providing a solid foundation for object-oriented programming.

