# Python - Test-driven Development

This project focuses on the concept and practice of test-driven development (TDD) in Python, emphasizing the importance of writing documentation and tests before the actual coding process begins. It aims to inculcate the habit of considering all possible edge cases during the development phase.

## Background Context

This section emphasizes the shift towards test-driven development in Python projects, highlighting the importance of writing tests and documentation prior to coding. It encourages collaboration on test cases while ensuring individual understanding and implementation.

## Resources

**Read or Watch:**

- [doctest — Test interactive Python examples](https://docs.python.org/3/library/doctest.html) (until "26.2.3.7. Warnings" included)
- [doctest – Testing through documentation](https://pymotw.com/3/doctest/)
- [Unit Tests in Python](https://www.youtube.com/watch?v=1Lfv5tUGsn8)

## Learning Objectives

By the end of the project, participants should be able to:

- Explain the essence and importance of tests in programming.
- Understand and implement interactive tests.
- Write comprehensive Docstrings to create tests.
- Document modules, classes, and functions properly.
- Identify and use basic option flags for creating tests.
- Discover and manage edge cases effectively.

## Requirements

### Python Scripts

- Use Python 3.8.5, with all scripts starting with `#!/usr/bin/python3`.
- Follow PEP 8 styling (version 2.7.*).
- Include a `README.md` at the root of the project directory.
- Ensure all files are executable.

### Python Test Cases

- Store test files in a `tests` folder with `.txt` extension.
- Execute tests using `python3 -m doctest ./tests/*`.
- Document all modules, classes, and functions.
- Collaborate on test cases to cover all edge cases.

## Tasks

0. **Integers addition**: Write a function that adds 2 integers, with tests to cover edge cases and ensure all inputs are valid.

1. **Divide a matrix**: Develop a function that divides all elements of a matrix by a divisor, ensuring type and value validations are in place.

2. **Say my name**: Create a function to print a full name, handling edge cases for non-string inputs.

3. **Print square**: Write a function that prints a square using the `#` character, including validations for input size.

4. **Text indentation**: Develop a function that formats text with specific indentation rules, ensuring correct handling of special characters.

5. **Max integer - Unittest**: Implement unittests for a provided function `max_integer(list=[])`, focusing on edge cases and correct output.

## Additional Information

To ensure a deep understanding of TDD, all development should start with writing tests and documentation. This approach helps in thinking through the functionality before implementation, resulting in more robust and error-free code.
