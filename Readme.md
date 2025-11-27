# Python Datatypes
  # Numeric

1,20,40

   # String

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
   2 _ #
   will result in
   File "<stdin>", line 1
   2 _ #
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

 # COMPARISON OPERATORS

1.  Comparison operators
    You use these to compare values. They always return a boolean (True or False).

| Operator | Meaning          | Example           |
| -------- | ---------------- | ----------------- |
| `==`     | equal to         | `5 == 5` → True   |
| `!=`     | not equal        | `5 != 3` → True   |
| `>`      | greater than     | `7 > 4` → True    |
| `<`      | less than        | `2 < 10` → True   |
| `>=`     | greater or equal | `10 >= 10` → True |
| `<=`     | less or equal    | `8 <= 8` → True   |

# LOGICAL OPERATORS

2. Logical operators
   These combine boolean values.

| Operator | Meaning           | Example                  |
| -------- | ----------------- | ------------------------ |
| `and`    | both must be True | `True and False` → False |
| `or`     | at least one True | `True or False` → True   |
| `not`    | flips boolean     | `not True` → False       |

## LOOPS IN PYTHON 
<!-- Python Loops -->

This guide covers Python loops, how they work, and how they can be applied in backend logic.

# What loops do

Loops repeat code so you don’t have to write it multiple times. You can use them to go through numbers, lists, or filter data in backend systems.

## EXAMPLES

1. for loop -Use a for loop when you know how many times you want the code to run.
   for more example check on file name "LOOP.PY"

2. while loop
   ## EXMPLE IN A REAL WORLD PROJECT

I went on and gave this prompt to CHATgpt for mor clarity
so meaning that when lets say i am trying to build an application for a backend like movie site and then before one logs in and they are being prompted to choose their variety of movies ie action,thriller,romance horror they they choose thriller and romance, so this means that their choise would be looped through the backend of the system so to check their variety choice then they get the output of movies in their dashboard so they can choose which they will watch on that day
or the loop can act like for search bar when one searches a movie it brings out the diff movies starting with that title in the server or database is it true to the example i am trying to give
i dont know if i have made any sense hahahaha

## THis is the output/ responce i got back 

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
def **init**(self , marks, grade):
self.marks = marks
self.grade = grade
def **str**(self):
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

<!-- Building Class Methods and Using Class Attributes -->

1. An instance attribute is responsible for holding information regarding an instance. It is a variable that is available in scope for all instance methods in the class.

2. A class attribute is accessible to the entire class — it has class scope. A class method is a method that is called on the class itself, not on the instances of that class.
     <!-- Understanding Class Attributes & Class Methods -->
   Imagine you have a factory that makes things.
   In Python, that factory is called a class, and the things it makes are called instances.

🧱 What Are Attributes?
Attributes = information stored inside an object.

Example:
If you make an Album object, it might have:

a release date

a genre

an artist

This info belongs to each individual album.

python
Copy code
class Album:
def **init**(self, date):
self.release_date = date
Here, self.release_date is instance attribute ➜ because every album has its own release date.

🏭 But Guess What? A Class Is Also an Object!
Just like a single album is an object…
The Album class itself is ALSO an object.
That means the class can have:

its own attributes (class attributes)

its own methods (class methods)

🔢 Why Use Class Attributes?
Imagine you want to count how many albums you have created.

Is it each album’s job to count all albums?
Nope — that doesn’t make sense.

It’s the Album factory’s job to keep track.

So we put that information on the class, not the individual album.

python
Copy code
class Album:
album_count = 0
This is a class attribute.

You can access it like this:

python
Copy code
Album.album_count # works
album1.album_count # also works but still refers to the class
⚙️ Making the Counter Go Up Automatically
Every time we create a new album, the album_count should increase.

Where do albums get created?
Inside the **init** method.

So we add:

python
Copy code
Album.album_count += 1
This way, every time an album is made, the counter goes up.

🧠 Class Methods: What Are They?
A class method is a function that belongs to the class itself, not to a single album.

We create one like this:

python
Copy code
@classmethod
def something(cls):
...
cls means “the whole class,” like Album itself.

Example: a class method to increase the album count:

python
Copy code
@classmethod
def increase_album_count(cls, increment=1):
cls.album_count += increment
Now the class can update its own counter.

🧊 Class Constants
A class constant is just data inside the class that is not supposed to change, like a list of allowed music genres.

We write constants in ALL CAPS so other programmers know not to touch them.

python
Copy code
class Album:
GENRES = ["Hip-Hop", "Pop", "Jazz"]
Even though Python won’t stop someone from changing it, the ALL CAPS name is a “don’t change me” sign.

You can still access it like:

python
Copy code
Album.GENRES
🧩 Putting It All Together
With instance attributes, class attributes, and class methods, a class becomes smarter.

Instance attributes = info about one object

Class attributes = info shared by every object the class makes

Class methods = actions the class itself can do

Class constants = info that shouldn’t change

🏁 Final Summary (Super Simple)
Thing What It Is Example
Instance attribute belongs to one object self.release_date
Class attribute belongs to the class album_count = 0
Class method a function for the class @classmethod
Class constant class data that shouldn’t change GENRES = [...]

<!-- WHEN WANTING TO CREATE A PYTHON FILE FOLLOW THESE STEPS  -->

Environment Setup (Code-Along)
GitHub RepoCreate New Issue
Learning Goals
Use pyenv to use different Python versions
Set up virtual environment using pipenv
Key Vocab
Module: a file containing Python definitions and statements. A module's functions, classes, and global variables can be accessed by other modules.
Package: a collection of modules that can be accessed as a group using the package name.
import: the Python keyword used to access data from other packages and modules inside of the current module.
PyPI: the Python Package Index. A repository of Python packages that can be downloaded and made available to your application.
pip: the command line tool used to download packages from PyPI. pip is installed on your computer automatically when you download Python.
Virtual Environment: a collection of modules, packages, and scripts that can be activated or deactivated at any time.
Pipenv: a virtual environment tool that uses pip to manage the modules, packages, and scripts that you intend to use in your application.
Introduction
In this lesson we will talk about environment tools like pyenv and pipenv. These tools allows us to separate different Python environments for all kinds of use cases. This is useful when we need an isolated environment with libraries and specific versions of Python.

You should execute the commands shown in this lesson to get practice working with pyenv and pipenv.

Pyenv
In an earlier lesson, you installed pyenv and Python 3.8.13. (If needed, you can use the following instructions to install pyenv for your operating system.)

pyenv install instructionsLinks to an external site.

Run the following command to confirm pyenv was installed for version 3.8.13:

pyenv versions
system

- 3.8.13 (set by /Users/username/.pyenv/version)
  ...
  Confirm your current global Python version is 3.8.13:

python3 --version
Python 3.8.13
Take a look at the file program.py, which simply prints the current Python version:

import sys
print("Python version")
print(sys.version)
You can also run this program to confirm your Python version is 3.8.13:

python program.py
Python version
3.8.13
We can see the different versions of Python available to install using the following command

pyenv install -l
Available versions:
2.1.3
2.2.3
2.3.7
...
...
Lets install a new version of Python (3.11). We can do this using the following command

pyenv install 3.11
Installing a new version of Python does not however change the current global version. We can confirm this by checking the Python version:

python3 --version
Python 3.8.13
Use pyenv to set the global Python version to the new version 3.11:

pyenv global 3.11
Confirm the current global Python version (full version 3.11.x may differ):

python3 --version
Python 3.11.4
Now if we run a Python program, we'll see it is executed using Python version 3.11.x. For example, let's run program.py:

python program.py
Python version
3.11.4
Let's set the global Python version back to 3.8.13:

pyenv global 3.8.13
Confirm the global Python version:

python3 --version
Python 3.8.13
Confirm our Python program program.py runs in this version:

python program.py
Python version
3.8.13
Pipenv
Pyenv allows us to manage the version of Python we are working with.

What if we want to manage dependencies as well?

Pipenv automatically creates and manages a virtualenv for your projects, it also adds/removes packages from your Pipfile as you install/uninstall packages. Pipenv also let's you run programs with a particular version of Python.

To install pipenv follow the instructions here pipenv installLinks to an external site.

We can use pipenv to create a virtual environment to run Python programs with version 3.11:

pipenv --python 3.11
In the Python flag we can define which version of --python we want to use.

You will notice a Pipfile and a Pipfile.lock have been added to the directory.

The Pipfile describes the dependencies we have installed and the Python version.

[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]

[dev-packages]

[requires]
python_version = "3.11"
python_full_version = "3.11.4"

The Pipfile.lock describes all the dependencies our dependencies rely on. The lock file gives us the ability to produce a deterministic and reproducible project environment.

We can now install a library into the virtual environment. Lets use the requests library as an example

pipenv install requests
if we want to install a specific version of the requests library we can pin the version in the command

pipenv install requests==2.28.1
Pipenv has created a virtual environment for our project. We can see the location of this virtual environment by using the command (your location will differ):

pipenv --venv
Successfully created virtual environment!
Virtualenv location: /Users/username/python-p3-environment-setup/.venv
Pipenv allows us to install dev dependencies. We can do so by adding the --dev argument.

pipenv install pytest --dev
Pytest will be added to the Pipfile as a dev dependency

Dev dependencies are modules which are not needed in production but they help us develop and test the code.

The command pipenv --version 3.11 created the Pipfile and Pipfile.lock files that define a virtual environment. However, the environment is not yet activated, and the current shell is still running Python 3.8.13. We can confirm this by:

python3 --version
Python 3.8.13
We can also run program.py to print the current Python version:

python program.py
Python version
3.8.13
How do we get into our virtual environment to run programs with version 3.11 and the various imported modules?

Use the following command to activate the virtual environment and run commands inside of it:

pipenv shell
Now we are in the virtual environment running Python 3.11, and have access to the dependencies we defined in the Pipfile. If we run the following commands in the virtual environment we will see that we can import the requests module we installed previously using pipenv install requests.

python

> > import requests
> > exit()
> > If we run our Python program program.py in the virtual environment, we should see we are running 3.11.x:

python program.py
Python version
3.11.4
If you ever need to remove a virtual environment you can use the pipenv --rm command.

pipenv --rm
Removing virtualenv (/Users/username/python-p3-environment-setup/.venv)...
This should return us back to our global Python version of 3.8.13, which we can confirm in a few different ways:

python3 --version
Python 3.8.13
python program.py
Python version
3.8.13
If you type pipenv shell (but don't!), you are activating the virtual environment in a new shell and every command you type is executed within that environment. Sometimes you might want to run a single command in a virtual environment. We can do with by running pipenv install then pipenv run <command> to execute a particular command within the virtual environment.

Run pipenv install again, but don't activate the environment in a new shell. You'll see the global version of Python for the current shell is still 3.8.13:

pipenv install
python program.py
Python version
3.8.13
We can run program.py in the virtual environment defined in Pipfile (i.e. Python 3.11 and installed modules) as shown:

pipenv run python program.py
Python version
3.11.4
Since we did not activate the virtual environment in a new shell, the environment is no longer active after the program completes, and the current shell is still using 3.8.13:

python program.py
Python version
3.8.13
Since we've set the python version for this program to 3.11, the program will run using python 3.11, even though the global version is 3.8.13. As long as we have a specific python version installed on our computer, we can use it locally in specific programs without having to reset our global python version.

Conclusion
Confirm you are no longer in a virtual environment (you might see an error message if you already removed the virtual environment).

pipenv --rm
Confirm you are back using global Python version 3.8.13:

python3 --version
Python 3.8.13
Virtual environments allow us to have a deterministic and predictable runtime for our Python projects. We can define specific versions for Python and the dependencies we need. We can easily add new virtual environments for multiple projects we have on our machine.

<!-- NOW I WANT TO KNOW HOW TO USE THE PIP&PIPE -->

PyPi and Pip

Learning Goals
Installing packages using pip.
Key Vocab
Module: a file containing Python definitions and statements. A module's functions, classes, and global variables can be accessed by other modules.
Package: a collection of modules that can be accessed as a group using the package name.
import: the Python keyword used to access data from other packages and modules inside of the current module.
PyPI: the Python Package Index. A repository of Python packages that can be downloaded and made available to your application.
pip: the command line tool used to download packages from PyPI. pip is installed on your computer automatically when you download Python.
Virtual Environment: a collection of modules, packages, and scripts that can be activated or deactivated at any time.
Pipenv: a virtual environment tool that uses pip to manage the modules, packages, and scripts that you intend to use in your application.
Introduction
Package Installer for Python (Pip) is the default package manager for python and is used to install and manage software packages. It uses an online repository called Python Package Index (PyPi).

We can search PyPi for libraries using the search bar on the site.

Installing Packages using Pip
We can use the Pip command to install python packages from the Python Package Index (PyPi). Lets practice this using a package called requests. Requests is a HTTP library for the Python programming language.

pip install requests
Now we have access to the requests module. It can be imported in our python programs.

$ python

> > > import requests
> > > To install a specific version of the module we can use pip install

pip install requests==2.22.0
Requirements files are files containing a list of modules to be installed using pip install.

pip install -r requirements.txt
Constraints files are requirements files that only control which version of a requirement is installed, not whether it is installed or not.

pip install -c constraints.txt
Example of a requirements.txt or constraints.txt file.

requests==2.28.1
uvicorn==0.18.2
fastapi==0.79.0
To uninstall a package

pip uninstall requests
Conclusion
Pip can be used to install packages from the Python Package Index. It gives us access to many libraries to help us develop.


% SCRIPTING IN PYTHON
GitHub RepoCreate New Issue
Learning Goals
Learn about scripting.
Write a script in python.
Key Vocab
Module: a file containing Python definitions and statements. A module's functions, classes, and global variables can be accessed by other modules.
Package: a collection of modules that can be accessed as a group using the package name.
import: the Python keyword used to access data from other packages and modules inside of the current module.
PyPI: the Python Package Index. A repository of Python packages that can be downloaded and made available to your application.
pip: the command line tool used to download packages from PyPI. pip is installed on your computer automatically when you download Python.
Virtual Environment: a collection of modules, packages, and scripts that can be activated or deactivated at any time.
Pipenv: a virtual environment tool that uses pip to manage the modules, packages, and scripts that you intend to use in your application.
Introduction
The word script in the context of programming refers to a code file containing a program which usually executes some tasks that need to be automated. Scripts are meant to be directly executed by the users.

How are scripts different than the modules we write in python?

Code that is meant to be imported and used in another program is a module. Script are meant to be run directly.

Shebang
The shebang at the beginning of a script allows us to run our python script as an executable without typing python before the file name.

#!/usr/bin/env python3

If we add this code in the beginning of the script the user can run the script using ./script.py instead of python script.py

if name == "main":
if __name__ == "__main__":
    # do things
You may have seen this syntax before when working with python or looking at python examples. This tells python that you only want to run the the code if the program is executed as a standalone file. If we import the script into another program the code in the if statement will not run because the __name__ variable will not be equal "__main__".

Accepting arguments from command line
Using the sys module we can accept inputs from the user from the command line. Lets use the sys.argv list which allows us to get input from the user and print it.

Lets look at the following script

#!/usr/bin/env python3
import sys
# The user input starts at index 1 in the sys.argv list. 
name = sys.argv[1]
if __name__ == "__main__":
    print(f"The name is {name} ")
We can run this script in the terminal using the following command

$ ./bin/script.py Steve
The name is Steve 
Using os.system to Run a shell command
We can also run shell commands using the os module Lets try to use the ls -l shell command in our script.

#!/usr/bin/env python3
import os
if __name__ == "__main__":
    os.system('ls -l')
The script will give us a list of files that are in the current directory.

$ ./bin/script.py
-rw-r--r--  1 user  staff  1810 Jul 28 19:23 CONTRIBUTING.md
-rw-r--r--  1 user  staff  1346 Jul 28 19:23 LICENSE.md
-rw-r--r--@ 1 user  staff  3653 Sep 27 22:30 README.md
drwxr-xr-x  3 user  staff    96 Sep 27 21:53 bin
Bash Scripts
A Bash script is a text file which can contains a series of commands. These commands can help us automate tasks that would require the developer to type multiple commands in the terminal. Any task you can run in the terminal can be put in a Bash script. All you need to do is add the commands sequentially in the Bash file. For Bash scripts the convention is to use the .sh file extension.

Lets take a look at a Bash script.

#!/bin/bash
echo "Files in this directory"
ls -a
Before running the script you may need to give it executable permission. You can change the permissions by running chmod +x script.sh. Now we can run the script using the following command.

./script.sh
The output should return a message and the output of the ls command will output the files of the directory the script is being run in.

Files in this directory
.               .canvas         .github         LICENSE.md      Pipfile.lock    bin
..              .git            CONTRIBUTING.md Pipfile         README.md       script.sh
Conclusion
We have covered some introductory concepts in scripting. You have learned how to accept inputs from the users and run system commands in a script. These tools can help us become much more productive by automating tasks and procedures.


--
## CRUD Operations in SQL


GitHub RepoCreate New Issue
Learning Goals
Use SQL to store data and retrieve it later on.
Use SQLite to build relational databases on your computer.
Perform CRUD operations on relational databases using SQL.
Key Vocab
SQL (Structured Query Language): a programming language that is used to manage relational databases and perform operations on the data that they contain.
Relational Database: a collection of data that is organized in well-defined relationships. The most common type of database.
Query: a statement used to return data from a database.
Table: a collection of related data in a database. Composed of rows and columns. Similar to a class in Python.
Row: a single record in a database table. Each column represents an attribute of the record. Similar to an object in Python.
Column: a single field in a database table. Each row contains values in each column. Similar to a Python object’s attributes.
Schema: a blueprint of the construction of the tables in a database and how they relate to one another.
Introduction
In this lesson, we'll cover different ways to manipulate and select data from SQL database tables. We'll see how to perform different Create, Read, Update, and Delete (or CRUD) actions in a database table.

Fork and clone this lessonLinks to an external site. to follow along.

Setting Up Our Database
In this code along, we'll be working with a cats table in the provided pets_database.db file. Explore the cats table structure using the SQLite VSCode extension, or with DB Browser, or by running the sqlite3 prompt:

 sqlite3 pets_database.db
 .schema
CREATE TABLE cats (
  id INTEGER PRIMARY KEY,
  name TEXT,
  age INTEGER,
  breed TEXT

Okay, let's start storing some cats.

Code Along 1: INSERT INTO
Run the following command with the pets_database.db file (either in DB Browser, or in your terminal from the sqlite3 prompt):

INSERT INTO cats (name, age, breed) VALUES ('Maru', 3, 'Scottish Fold');
We use the INSERT INTO command, followed by the name of the table to which we want to add data. Then, in parentheses, we put the column names that we will be filling with data. This is followed by the VALUES keyword, which is accompanied by a parentheses enclosed list of the values that correspond to each column name.

Important: Note that we didn't specify the "id" column name or value. Since we created the cats table with an "id" column whose type is INTEGER PRIMARY KEY, we don't have to specify the id column values when we insert data. Primary Key columns are auto-incrementing. As long as you have defined an id column with a data type of INTEGER PRIMARY KEY, a newly inserted row's id column will be automatically given the correct value.

Let's add a few more cats to our table. This time we'll do this via our text editor. Create a file, 01_insert_cats_into_cats_table.sql. Use two INSERT INTO statements to insert the following cats into the table:

name	age	breed
"Lil' Bub"	5	"American Shorthair"
"Hannah"	1	"Tabby"
Each INSERT INTO statement gets its own line in the .sql file in your text editor. Each line needs to end with a ;. Run the file with the following code in your terminal:

 sqlite3 pets_database.db < 01_insert_cats_into_cats_table.sql
NOTE: This command should be run from your terminal prompt, not in the sqlite console.

Now, we'll learn how to SELECT data from a table, which will help us to confirm that we inserted the above data correctly.

What immediately follows INSERT INTO in a SQL statement?


Selecting Data
Now that we've inserted some data into our cats table, we likely want to read that data. This is where the SELECT statement comes in. We use it to retrieve database data, or rows.

Code Along 2: SELECT FROM
A basic SELECT statement works like this:

SELECT [names of columns we are going to select] FROM [table we are selecting from];
We specify the names of the columns we want to SELECT and then tell SQL the table we want to select them FROM.

We want to select all the rows in our table, and we want to return the data stored in any and all columns in those rows. To do this, we could pass the name of each column explicitly.

For the rest of this code along, you can run the SQL commands one of two ways, depending on your preference.

You can either open the database using the sqlite3 CLI, and run the SQL commands from the terminal:

 sqlite3 pets_database.db
Or you can open the pets_database.db file in DB Browser for SQLite, and run the SQL commands from the "Execute SQL" tab.

Run this command from the sqlite prompt in your terminal, or in DB Browser:

SELECT id, name, age, breed FROM cats;
This should give us back all the data from the cats table:

1|Maru|3|Scottish Fold
2|Lil' Bub|5|American Shorthair
3|Hannah|1|Tabby
A faster way to get data from every column in our table is to use a special selector, known commonly as the 'wildcard' selector *. The * selector means: "Give me all the data from all the columns for all of the cats" Using the wildcard, we can SELECT all the data from all of the columns in the cats table like this:

SELECT * FROM cats;
Now let's try out some more specific SELECT statements.

Selecting by Column Names
To select just certain columns from a table, use the following:

SELECT name FROM cats;
That should return the following:

Maru
Lil' Bub
Hannah
You can even select more than one column name at a time. For example, try out:

SELECT name, age FROM cats;
Top-Tip: If you have duplicate data (for example, two cats with the same name) and you only want to select unique values, you can use the DISTINCT keyword. For example:

SELECT DISTINCT name FROM cats;
Selecting Based on Conditions: The WHERE Clause
What happens when we want to retrieve a specific table row? For example the row that belongs to Maru? Or to retrieve all the baby cats who are younger than two years old? We can use the WHERE keyword to select data based on specific conditions. Here's an example of a boilerplate SELECT statement using a WHERE clause.

SELECT * FROM [table name] WHERE [column name] = [some value];
Let's retrieve just Maru from our cats table:

SELECT * FROM cats WHERE name = "Maru";
That statement should return the following:

1|Maru|3|Scottish Fold
We can also use comparison operators, like < or > to select specific data. Let's give it a shot. Use the following statement to select the young cats:

SELECT * FROM cats WHERE age < 2;
The SQL statements we're learning here will eventually be used to integrate the applications you'll build with a database. For example, it's easy to imagine a web application that has many users. When a user signs into your app, you'll need to access your database and select the user that matches the credentials an individual is using to log in.

What immediately follows SELECT in a SQL statement?


Updating Data
Let's talk about updating, or changing, data in our table rows. We do this with the UPDATE keyword.

Code Along 3: UPDATE
A boilerplate UPDATE statement looks like this:

UPDATE [table name] SET [column name] = [new value] WHERE [column name] = [value];
The UPDATE statement uses a WHERE clause to grab the row you want to update. It identifies the table name you are looking in and resets the data in a particular column to a new value.

Let's update one of our cats. Turns out Maru's friend Hannah is actually Maru's friend Hana. Let's update that row to change the name to the correct spelling:

UPDATE cats SET name = "Hana" WHERE name = "Hannah";
One last thing before we move on: deleting table rows.

Deleting Data
To delete table rows, we use the DELETE keyword.

Code Along 4: DELETE
A boilerplate DELETE statement looks like this:

DELETE FROM [table name] WHERE [column name] = [value];
Let's go ahead and delete Hana from our cats table (it turns out Hana is actually an iguana):

DELETE FROM cats WHERE id = 3;
Notice that this time we selected the row to delete using the Primary Key column. Remember that every table row has a Primary Key column that is unique. Hana was the third row in the database and thus had an id of 3.

Conclusion
You've now successfully performed all four CRUD actions — Create, Read, Update, and Delete — using SQL with the INSERT, SELECT, UPDATE and DESTROY commands. These four actions are among the most important when it comes to working with SQL databases.


