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
<!-- LOGICAL OPERATORS -->
2. Logical operators
These combine boolean values.

| Operator | Meaning           | Example                  |
| -------- | ----------------- | ------------------------ |
| `and`    | both must be True | `True and False` → False |
| `or`     | at least one True | `True or False` → True   |
| `not`    | flips boolean     | `not True` → False       |


<!-- LOOPS IN PYTHON  -->
<!-- Python Loops -->
This guide covers Python loops, how they work, and how they can be applied in backend logic.

<!-- What loops do -->
Loops repeat code so you don’t have to write it multiple times. You can use them to go through numbers, lists, or filter data in backend systems.
<!-- EXAMPLES -->
1. for loop -Use a for loop when you know how many times you want the code to run.
     for more example check on file name "LOOP.PY"

2. while loop
   <!-- EXMPLE IN A REAL WORLD PROJECT -->

I went on and gave this prompt to CHATgpt for mor clarity 
     so meaning that when lets say i am trying to build an application for a backend like movie site and then before one logs in and they are being prompted to choose their variety of movies ie action,thriller,romance horror they they choose thriller and romance, so this means that their choise would be looped through the backend of the system so to check their variety choice then they get the output of movies in their dashboard so they can choose which they will watch on that day 
or the loop can act like for search bar when one searches a movie it brings out the diff movies starting with that title in the server or database is it true to the example i am trying to give 
i dont know if i have made any sense hahahaha

<!-- THis is the output/ responce i got back  -->
How loops fit into your example
1. User chooses categories (e.g., Thriller and Romance)
In the backend you’d have something like:

A list of movies stored in a database

Each movie has categories/tags

When the user selects Thriller and Romance, your code loops through the movie list to find movies that match those categories.

Example (simple version):

python
Copy code
movies = [
    {"title": "Movie A", "category": "thriller"},
    {"title": "Movie B", "category": "romance"},
    {"title": "Movie C", "category": "action"},
]

chosen = ["thriller", "romance"]

result = []

for m in movies:
    if m["category"] in chosen:
        result.append(m)
This loop filters movies based on user preference.

2. Search bar example
Your search bar idea is also correct.

If a user types "sp", a loop checks all movies in the database whose title starts with "sp".

Example:

python
Copy code
search = "sp"
matches = []

for movie in movies:
    if movie["title"].lower().startswith(search):
        matches.append(movie)
Result might be:

Spider-Man

Spawn

Space Jam

3. Loops in real backend apps
In a real API or backend:

You don’t loop in Python manually every time.

The database engine does the heavy lifting using queries.

But the concept is exactly the same:

Filter

Search

Match categories

Return results

Even if a database handles it, the idea of looping through items is still behind the scenes.

In short
You're correct on all points:
✔️ Loops help filter user-selected categories

✔️ Loops help run search queries

✔️ Loops help match information in backend logic

✔️ Loops help structure the data sent to the dashboard



<!-- OBJECT ORIENTED PROGRAMMING IN PYTHON -->
So oop is built using these syntaxes 
 [Classes and objects, Attributes (properties of objects), Methods (functions inside classes), Constructors (__init__),
    Encapsulation / access modifiers, Inheritance, Polymorphism, Practical examples]

example codes find them on objectpp.py file




class student:
    def __init__(self , marks, grade):
        self.marks = marks
        self.grade = grade
    def __str__(self):
        return f'this {self.marks} is the marks and this {self.grade}'
so = student('79' , 'grade')
print(so)
student {
    
}


<!-- AN EXPLANATION OF HOW TO USE SUPER() AND ALSO AN EXAMPLE CODE  -->
🧒 Imagine this:

You have a student in school.

A Student is also a User (a regular person with a login).

The User class already has a log_in() function that knows how to log someone in.

But the Student class wants to do extra things when a student logs in — like mark them as “in class.”

🤔 So what does super() do?
👉 super() basically means:

“Hey, run the parent’s version of this function first.”

So when you write:
<!-- example code -->
def log_in(self):
    super().log_in()
    self.in_class = True


This means:

super().log_in() → “Do everything the User class normally does when someone logs in.”

self.in_class = True → THEN do the extra student-only thing.

🧒 Simple analogy:

Imagine you’re at school.
When you enter the building:

Everyone has to check in at the front desk.
(This is the parent class: User.log_in())

But students also have to go to their classroom after checking in.
(This is the child class: Student.log_in())

super() is like saying:

➡️ “Let me do what everyone does first… then I’ll do the extra student part.”

📌 Why do we need super()?

Because without it:

The User's login stuff wouldn’t happen.

Only the student-specific part would happen.

You might skip important steps like authentication.











