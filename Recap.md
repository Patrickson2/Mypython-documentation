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


<!-- NOW WE ENTER OOP -->

I’ll explain this VERY simply ⬇️

⭐ 8. OOP — Object Oriented Programming

OOP is building your code the same way you organize real life:

A class = blueprint

An object = thing created from the blueprint

Example:
A “Human” class is like the blueprint.
Each person (Patrickson, Kamau) is an object made from that blueprint.

9. init() method

You know how when a baby is born, we immediately give them:

a name

an age

That moment is init.
It sets up the object's first details.

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
<!-- NOW I WANT TO EXPLAIN THE PURPOSE OF USING THE SELF() MORE -->
    self in Python means:

       👉 “THIS object right here.”

          It’s how the object talks about itself.

         Whenever you create an object from a class, self is the way Python lets that object store its own information.

              🎒 Imagine this:

           You make a Student object:

        s1 = Student("Alice", 5)


Inside the class, when it’s assigning the name…

self.name = name


self is like the object raising its hand and saying:

➡️ “Put the name on me!”
➡️ “Store this value in my memory!”

Without self, Python wouldn't know where to put “Alice” or what object the data belongs to.

🧩 Why do we need self?

Because a class is just the blueprint.

self is how each individual object remembers its own data.

Example:

s1 = Student("Alice", 5)
s2 = Student("Bob", 6)


self makes sure:

Alice's object stores Alice’s grade

Bob’s object stores Bob’s grade

If you didn't have self, both objects would get mixed up and overwrite each other.

🧪 What self actually is

Technically:

self is just the first parameter of any method in a class.

Python automatically passes the object into self.

When you call:

s1.log_in()


Python secretly turns it into:

Student.log_in(s1)


So self = s1.

✔️ Summary (super simple)

self means:

“The object we’re talking about right now.”

It lets each object store and access its own data.

It must be the first argument in class methods (Python adds it automatically).


10. INSTANCE VS CLASS ATTRIBUTES
✔ Instance Attribute
Belongs to one person only.

python
Copy code
self.name
self.age
Each human has their own name and age.

✔ Class Attribute
Something all humans share.

python
Copy code
species = "Homo Sapiens"
All humans share the same species.

Your Example Code (Explained Simply)
python
Copy code
class Human:
    def __init__(self, name, age="40"):
        self.name = name
        self.age = age

h1 = Human("Kamau", 20)
h2 = Human("kamara")

print(h1.name, h1.age)   
print(h2.name, h2.age)
Line-by-line (10-year-old style):
We create a class Human.

When someone is created, they get a name and an age.

If no age is given, we use 40 as the default.

h1 is Kamau who is 20.

h2 is Kamara who didn’t give an age, so he becomes 40.

✔ Output
nginx
Copy code
Kamau 20
kamara 40
Correct.