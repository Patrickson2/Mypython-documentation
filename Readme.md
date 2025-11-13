<!-- Python Datatypes -->
  <!-- Numeric -->

1,20,40

   <!-- String -->

"Hello world"/ "Hello Mungai"

 <!-- List -- mutable -->

[1,2,34,45]
['apple', 'banana','orange']

<!-- Tupple - immutable  -->

('apple', 'banana','orange')
(1,2,34,45)

<!-- range - it always starts from 0-->

range(10)//0,1,2,3,4,5,6,7,8,9

<!-- set -->

set([1,2,3,4,5,6,7,8,9]) //,1,2,3,4,5,6,7,8,9

<!-- Dictionary  -->

{
"name" : "Mungai",
"gender" : "Male",
"occupation" : "Student at Moringa School"
"age" : 16,
"isMarried" : "False"
}

<!-- Boolean -->

Either True or False

<!-- None  -->

name : None

# this is a comment used in python just like pressing on the ctr + / buttons in vannila javascript

# to run this application head to terminal and call the location of the file you want to run first

# eg:for this file i will call python3 lib/app.py

# you can choose how you want the python() to be outputed at the end while using the END parameter

# eg print("welcom to my world!", end="Mungai")

# print("Hello world!", end=" ")

# print("Hello sun!", end="!! ")

# print("Hello sky!", end="!!!\n")

Looping statements use the While - the "while" loops endlessly as seen in the (loop.py)


<!-- HOW TO READ ERRORS IN PYTHON -->
In this example it has 3 stages being the "where" "who" "why"
first the error message in the terminal is this
     File "lib/a_name_error.py",
       line 3, in <module>
        print(hello_world)
      NameError: name 'hello_world' is not defined
<!-- this the output of code in the terminal -->

  2.Showing "where" the error is 
     "lib/a_name_error.py"--is the file the error occurred in.
       line 3 --is the line of code with the error.
            <module> --is the scope of the error.

<!-- 3 COMMON ERRORS TYPES -->
1. Syntax Errors --Syntax errors are pretty self-explanatory: they're the result of incorrect syntax. Thankfully, they're usually followed by a guess about the location of the error. For instance:
     2 * #
   will result in 
   File "<stdin>", line 1
    2 * #
        ^
SyntaxError: invalid syntax

2. Logic Errors --



<!-- FUNCTIONS IN PYTHON -->
functions in python are written using methods like the key word "def" unlike in js where when writing out functions you use the key word "function"
we will see an example in the file func.py and how to know the difference when trying to execute a function 
writing the name of the code you use snake case instead of camel case in js 

<!-- FLAGS IN PYTESTING /TDD -->
pytest has many flags, but we're just going to focus on the few that will be most helpful to you.

(-x)is pytest's "exit" flag. This executes tests until one fails, then stops executing tests. This is very helpful for test-driven development, as you'll want to focus on developing to one test at a time.
(--pdb) opens the Python debugger when a test fails. It does not open the prettier, improved ipdb, but its basic functions are very similar.
(-s) tells pytest to show the full output for failed tests (i.e. print() statements).
(-q) (for quiet) shortens pytest's output. Running with the -q flag will only show a single line for the summary of the testing session and details of the failures.
(-h) will help you figure out where to place arguments for the pytest command and provide a long list of flags and configurations for use with pytest.

<!-- SCOPE -->
two diff scopes are "Global scope" & "Local Scope"
for more example on the diff check out on var.py
       <!-- Glocal scope -->
         these are variables created outside of a function and are made available to all functions in your module eg.

         message = "Hello from outside"

              def greet():
               print(message)  

           greet()
           print(message) 

       <!-- Local scope -->
        these are variables created inside the fuction eg.

           def greet():
                message = "Hello from inside the function"
                print(message)
            greet()

SO IN SHORT THIS IS ALL ABOUT WHAT I HAVE LEARNT 

# Python Basics — Data Types and Functions

This project demonstrates Python data types and functions for backend learning.

## Data Types Covered
- `int` → whole numbers
- `float` → decimal numbers
- `str` → text
- `bool` → True/False
- `list`, `tuple`, `dict`, `set`

## Functions
- Functions are reusable blocks of code.
- `return` sends a value back.
- Default values make functions flexible.
- Type hints show expected argument and return types.

## Examples

```python
# Integers and floats
x = 10
y = 3.5
print(x + y)  # 13.5

# Strings
name = "Patrickson"
print(f"Hello, {name}!")

# Booleans
is_ready = True
print(not is_ready)  # False

# Function with default value and type hints
def greet(name: str = "programmer") -> str:
    return f"Hello, {name}!"

print(greet())  # Hello, programmer!
print(greet("Patrickson"))  # Hello, Patrickson!

# Function returning half a number
def halve(number: float) -> float:
    return number / 2

print(halve(10))  # 5.0

```
## OPERATORS 
 There are two types of conditional statements the "Comparison OPerators" & "LOGICAL OPERATORS"
 <!-- COMPARISON OPERATORS -->
 1. Comparison operators 
You use these to compare values. They always return a boolean (True or False).

| Operator | Meaning          | Example           |
| -------- | ---------------- | ----------------- |
| `==`     | equal to         | `5 == 5` → True   |
| `!=`     | not equal        | `5 != 3` → True   |
| `>`      | greater than     | `7 > 4` → True    |
| `<`      | less than        | `2 < 10` → True   |
| `>=`     | greater or equal | `10 >= 10` → True |
| `<=`     | less or equal    | `8 <= 8` → True   |
