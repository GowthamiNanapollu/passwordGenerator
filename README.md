# Password Generator Project
#### Video Demo:  <https://youtu.be/9B2Zx_z7PFQ?si=eTUD4Xyx7onvAGCv>

#### Description:

The Password Generator project is a Python-based application designed to help users generate secure passwords with varying complexity levels. This application allows users to choose the length and complexity of the passwords they need, ranging from simple numeric-only passwords to highly secure passwords including special symbols.

##### Features:

- **Simple Passwords**: Numeric-only passwords, ideal for low-security situations.
- **Medium Passwords**: Alphanumeric passwords (upper and lower case letters, numbers), suitable for most situations.
- **Complex Passwords**: Alphanumeric passwords with added special symbols, perfect for high-security scenarios.

##### How it Works:

The user is prompted to select a complexity level:
1. **Simple**: The password will consist only of numeric digits.
2. **Medium**: The password will contain a mix of upper-case and lower-case letters along with digits.
3. **Complex**: The password will include upper-case and lower-case letters, digits, and special symbols like `!`, `@`, `#`, etc.

Additionally, the user is asked to specify the number of characters in the password, with the restriction that the password must be at least 4 characters long but no more than 15 characters.

The password generator then creates the password according to these choices and displays it to the user.

##### Files in the Project:

1. **main.py**:
   This is the main Python file that contains the password generation logic. It defines three functions:
   - `simple(n_chars)`: Generates a simple, numeric-only password of the specified length.
   - `medium(n_chars)`: Generates a password with a mix of letters and digits.
   - `complex(n_chars)`: Generates a more secure password, including letters, digits, and special symbols.

2. **test_project.py**:
   This file contains unit tests for each of the password generation functions. It ensures that the functions behave as expected, particularly by checking that the length of the generated passwords matches the user's input.

##### Testing:

The project includes a separate file `test_project.py` that defines unit tests using `pytest`. This ensures that the password generation functions produce passwords of the correct length. Below are the defined test cases:

- **test_simple()**:
  - Calls the `simple()` function with a password length of 10.
  - Asserts that the generated password is exactly 10 characters long.

- **test_medium()**:
  - Calls the `medium()` function with a password length of 9.
  - Asserts that the password generated is 9 characters long.

- **test_complex()**:
  - Calls the `complex()` function with a password length of 12.
  - Verifies that the length of the password is 12 characters.

##### Running Tests:

To run the tests, make sure you have `pytest` installed. You can install it using pip:
```bash
pip install pytest
