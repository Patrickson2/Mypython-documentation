<!-- This is a recap of what i have learned for the past few days -->
🔁 FULL PYTHON RECAP (Explained like you’re 10–12 years old)
Short, simple, practical.

1. VARIABLES
Think of a variable like a labeled box where you store something.

python
Copy code
name = "Patrickson"
age = 20
Real-life example:
When a user signs up, you store their name, age, email in “variables” inside your program.

2. DATA TYPES
You already know them.

Type	Meaning	Example
int	whole number	15
float	number with decimal	3.14
str	text	"Kenya"
bool	True/False	True

Real-life example:
A movie app uses:

str for movie title

int for movie length

bool for “is_user_logged_in?”

3. OPERATORS
They help you compare or do math.

Math:
diff
Copy code
+, -, *, /
Comparison:
yaml
Copy code
==, >, <, !=
Real example:
Checking if a student passed:

python
Copy code
marks = 75
print(marks >= 50)  # True
4. IF STATEMENTS
They help your program make decisions, like a guard at the gate.

python
Copy code
if age >= 18:
    print("You can watch this movie.")
else:
    print("Not allowed.")
5. LOOPS
Loops repeat things.

for loop
Think of it like scrolling through a list one by one.

python
Copy code
movies = ["Rambo", "Spiderman", "Ben10"]

for m in movies:
    print(m)
while loop
It repeats until a condition becomes false.

python
Copy code
count = 1
while count <= 5:
    print(count)
    count += 1
6. LISTS
A list is like a shopping basket where you store many items.

python
Copy code
users = []
users.append("Patrickson")
Real example:
Every time someone signs up, you append their name to the list.

7. FUNCTIONS
A function is like a machine.
You give it something, it does work, it gives something back.

python
Copy code
def greet(name):
    return f"Hello {name}"


    