print('hello JD')
print('Welcome to Data Engineering')
print('Hello \'Sasha\' how are you? This is ur dad talking.')

print("    /|")
print("   / |")
print("  /  |")
print(" /   |")
print("/____|")

# Variables in Python

character_name = 'John Doe'
character_age = '35'

print('There was a man named ' + character_name + ', ' )
print('he was ' + character_age + ' years old.')
print('He really liked the name ' + character_name + ',')
print('but he didnt like being ' + character_age + '!')


# Working with Strings
# https://www.freecodecamp.org/learn/learn-python-for-beginners/core-primitives-in-python/working-with-strings

phrase = 'Giraffe Academy'
print(phrase.upper() + ' is cool')
print(phrase.upper().isupper())
print(len(phrase))
#indexing 012345
print(phrase[3])
print(phrase.index('y'))
print(phrase.replace('Giraffe', 'Snake'))

"""
================================================================================
THE COMPLETE PYTHON NUMBERS HANDBOOK: GUIDE & CODE EXAMPLES
================================================================================
This handbook covers everything you need to know about working with numbers in 
Python, ranging from basic arithmetic operations to built-in math functions, 
type conversions, and the math module.

Topics Covered:
1. Number Types (int, float, complex)
2. Basic Arithmetic Operations & Operator Precedence
3. Augmented Assignment Operators
4. Built-in Number Functions
5. Type Conversion (Casting)
6. The Python `math` Module
================================================================================
"""

# ==============================================================================
# 1. NUMBER TYPES IN PYTHON
# ==============================================================================
# Python has three primary numeric types:
# - int: Integer numbers (whole numbers without a fractional part)
# - float: Floating-point numbers (numbers with a decimal point)
# - complex: Complex numbers with real and imaginary parts

integer_num = 42          # <class 'int'>
float_num = 3.14159       # <class 'float'>
complex_num = 2 + 3j      # <class 'complex'>

print("--- 1. Number Types ---")
print(f"Value: {integer_num}, Type: {type(integer_num)}")
print(f"Value: {float_num}, Type: {type(float_num)}")
print(f"Value: {complex_num}, Type: {type(complex_num)}")
print("-" * 50)


# ==============================================================================
# 2. BASIC ARITHMETIC OPERATIONS & OPERATOR PRECEDENCE
# ==============================================================================
# Python supports all standard mathematical operators.
# Precedence follows the standard mathematical rule: PEMDAS / BODMAS
# (Parentheses, Exponents, Multiplication/Division, Addition/Subtraction)

a = 10
b = 3

addition = a + b         # 13
subtraction = a - b      # 7
multiplication = a * b   # 30
division = a / b         # 3.3333333333333335 (Always returns a float)
floor_division = a // b  # 3 (Divides and rounds down to the nearest integer)
modulo = a % b           # 1 (Returns the remainder of the division)
exponentiation = a ** b  # 1000 (a raised to the power of b: 10^3)

print("--- 2. Basic Arithmetic ---")
print(f"{a} + {b} = {addition}")
print(f"{a} - {b} = {subtraction}")
print(f"{a} * {b} = {multiplication}")
print(f"{a} / {b} = {division}")
print(f"{a} // {b} (Floor Division) = {floor_division}")
print(f"{a} % {b} (Modulo/Remainder) = {modulo}")
print(f"{a} ** {b} (Exponent) = {exponentiation}")

# Operator Precedence Example
result = 10 + 2 * 3 ** 2 - 4 / 2
# Step 1: Exponentiation -> 3 ** 2 = 9
# Step 2: Multiplication -> 2 * 9 = 18
# Step 3: Division -> 4 / 2 = 2.0
# Step 4: Addition & Subtraction (Left to Right) -> 10 + 18 - 2.0 = 26.0
print(f"Precedence result of '10 + 2 * 3 ** 2 - 4 / 2': {result}")
print("-" * 50)


# ==============================================================================
# 3. AUGMENTED ASSIGNMENT OPERATORS
# ==============================================================================
# Shortcut operators to update a variable's value based on its current value.

count = 5
count += 2   # Equivalent to: count = count + 2  (Now 7)
count -= 1   # Equivalent to: count = count - 1  (Now 6)
count *= 3   # Equivalent to: count = count * 3  (Now 18)
count /= 2   # Equivalent to: count = count / 2  (Now 9.0)

print("--- 3. Augmented Assignment ---")
print(f"Final count value after operations: {count}")
print("-" * 50)


# ==============================================================================
# 4. BUILT-IN NUMBER FUNCTIONS
# ==============================================================================
# Python provides several built-in functions that require no imports.

neg_num = -15
decimals = 3.6789

print("--- 4. Built-in Number Functions ---")
print(f"abs({neg_num}) -> Absolute value: {abs(neg_num)}")
print(f"pow(2, 3) -> Power (2^3): {pow(2, 3)}")
print(f'max(4,6) -> Maximum value: {max(4,6)}')
print(f"round({decimals}, 2) -> Rounded to 2 decimals: {round(decimals, 2)}")
print(f"round(3.5) -> Rounds to nearest even (banker's rounding): {round(3.5)}")
print(f"round(4.5) -> Rounds to nearest even: {round(4.5)}")

numbers_list = [10, 45, 2, 89, 23]
print(f"min({numbers_list}) -> Minimum value: {min(numbers_list)}")
print(f"max({numbers_list}) -> Maximum value: {max(numbers_list)}")
print(f"sum({numbers_list}) -> Total sum: {sum(numbers_list)}")
print("-" * 50)


# ==============================================================================
# 5. TYPE CONVERSION (CASTING)
# ==============================================================================
# Convert between integers, floats, and strings representing numbers.

num_str = "123"
num_float = 45.89

print("--- 5. Type Conversion ---")
print(f"String '{num_str}' to int: {int(num_str)} (Type: {type(int(num_str))})")
print(f"Float {num_float} to int (truncates decimal): {int(num_float)}")
print(f"Int 50 to float: {float(50)} (Type: {type(float(50))})")
print("-" * 50)


# ==============================================================================
# 6. THE PYTHON `math` MODULE
# ==============================================================================
# For advanced mathematical operations, import the built-in `math` library.

import math

print("--- 6. The Math Module ---")
print(f"math.pi (Constant): {math.pi}")
print(f"math.e (Constant): {math.e}")
print(f"math.sqrt(144) -> Square root: {math.sqrt(144)}")
print(f"math.ceil(4.2) -> Round up to nearest int: {math.ceil(4.2)}")
print(f"math.floor(4.9) -> Round down to nearest int: {math.floor(4.9)}")
print(f"math.factorial(5) -> 5! (5*4*3*2*1): {math.factorial(5)}")
print(f"math.log(100, 10) -> Logarithm base 10 of 100: {math.log(100, 10)}")
print(math.floor(3.75))
print(math.ceil(3.75))

# Trigonometry (expects angles in radians)
angle_degrees = 90
angle_radians = math.radians(angle_degrees)
print(f"math.sin(90 degrees in radians): {math.sin(angle_radians)}")
print("===============================================================================")
"""
================================================================================
THE COMPLETE PYTHON USER INPUT HANDBOOK: GUIDE & CODE EXAMPLES
================================================================================
This handbook covers how to accept, process, and validate user input in Python,
transitioning raw string inputs into useful data types like numbers and booleans.

Topics Covered:
1. The Basic `input()` Function
2. Handling Numeric Input (Type Casting)
3. Multiple Inputs in a Single Line
4. Basic Input Validation & Error Handling
================================================================================
"""

# ==============================================================================
# 1. THE BASIC `input()` FUNCTION
# ==============================================================================
# The `input()` function pauses program execution, displays an optional prompt
# string to the user, waits for the user to type something, and presses Enter.
# CRITICAL RULE: `input()` ALWAYS returns data as a string (`str`).

print("--- 1. Basic Input ---")
# Simulated example (uncomment below line to run interactively in your terminal):
# user_name = input("Enter your name: ")
# print(f"Hello, {user_name}! (Type: {type(user_name)})")

user_name = input ('Enter your name: ')
print("--- 2. Basic Input ---")
print(f'User name: {user_name})')
print(f'Hello {user_name}')


# For demonstration purposes, we simulate a hardcoded user response:
simulated_input = "Alice"
print(f"User entered (simulated): {simulated_input}")
print(f"Data type of input: {type(simulated_input)}")
print("-" * 50)

# ==============================================================================
# 2. HANDLING NUMERIC INPUT (TYPE CASTING)
# ==============================================================================
# Because `input()` returns a string, you cannot perform math directly on it.
# You must explicitly convert (cast) the string to an `int` or `float`.

print("--- 2. Numeric Input & Casting ---")
# Simulated user entering age and height
simulated_age_str = "25"
simulated_height_str = "5.9"

# Casting to numeric types
user_age = int(simulated_age_str)
user_height = float(simulated_height_str)

# Now we can perform calculations
age_in_five_years = user_age + 5

print(f"Parsed Age: {user_age} (Type: {type(user_age)})")
print(f"Parsed Height: {user_height} (Type: {type(user_height)})")
print(f"Age in 5 years: {age_in_five_years}")
print("-" * 50)

# ==============================================================================
# 3. MULTIPLE INPUTS IN A SINGLE LINE
# ==============================================================================
# You can capture multiple values at once using `.split()` to break a string
# apart by whitespace (or a specified delimiter).

print("--- 3. Multiple Inputs ---")
# Simulated input string: "10 20" (representing coordinates or dimensions)
simulated_coords = "10 20"

# .split() returns a list of strings: ['10', '20']
x_str, y_str = simulated_coords.split()

# Convert each item individually
x = int(x_str)
y = int(y_str)

print(f"Raw split result: {simulated_coords.split()}")
print(f"Processed coordinates -> X: {x}, Y: {y}")

# Advanced trick: Using map() to cast multiple inputs in one line
# x, y = map(int, input("Enter X and Y separated by space: ").split())
print("-" * 50)

# ==============================================================================
# 4. BASIC INPUT VALIDATION & ERROR HANDLING
# ==============================================================================
# Users often make mistakes (e.g., typing letters when asked for a number).
# We use `try-except` blocks along with `while` loops to handle bad inputs safely.

print("--- 4. Input Validation (Safe Parsing) ---")

# Simulating a user who types an invalid value first ("abc"), then a valid one ("30")
user_inputs_queue = ["abc", "30"]
attempt = 0

while True:
    current_input = user_inputs_queue[attempt]
    attempt += 1
    print(f"User typed: '{current_input}'")

    try:
        # Try converting input to an integer
        valid_number = int(current_input)
        print(f"Success! Valid integer received: {valid_number}")
        break  # Exit the loop once valid input is secured
    except ValueError:
        # Catch error if int() fails, preventing program crash
        print("Error: That's not a valid integer! Please try again.\n")

print("===============================================================================")