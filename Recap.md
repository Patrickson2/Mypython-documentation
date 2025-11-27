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


## SQL
SQL Queries

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
In this lesson, we'll cover how to write SQL queries to retrieve and add specific data to SQL database tables.

Fork and clone this lessonLinks to an external site. to follow along.

What is a SQL Query?
The term "query" refers to any SQL statement that retrieves data from your database. In fact, we've already written a number of SQL queries using basic SELECT statements. We've already seen how to retrieve single units of data, or rows, with queries like these:

To select all of the rows from a cats table:

SELECT * FROM cats;
To select only rows representing data meeting certain conditions:

SELECT * FROM cats WHERE name = "Maru";
What if, however, we wanted to select the oldest cat? Or all of the cats that don't currently belong to an owner? Or all of the cats with short names?

Data storage isn't very useful if we can't manipulate, view, and analyze that data. Luckily for us, SQL is actually a powerful tool for doing just that.

In this exercise, we'll walk through executing a handful of common and handy SQL queries.

Is a DELETE statement a query?



Code Along: SQL Queries
Creating our Database
For this code along we have pets_database.db file with a cats table.

Just like with the last code along, you can run the SQL commands one of two ways, depending on your preference. You can either open the database using the sqlite3 CLI, and run the SQL commands from the terminal:

$ sqlite3 pets_database.db
Or you can open the pets_database.db file in DB Browser for SQLite, and run the SQL commands from the "Execute SQL" tab.

Let's check out our cats table now:

SELECT * FROM cats;
This should return:

1|Maru|3|Scottish Fold|1
2|Hana|1|Tabby|1
3|Lil\' Bub|5|American Shorthair|
4|Moe|10|Tabby|
5|Patches|2|Calico|
Top-Tip: In sqlite3, you can format the output of your select statements with a few helpful options:

.headers on      # output the name of each column
.mode column     # now we are in column mode, enabling us to run the next two .width commands
.width auto      # adjusts and normalizes column width
# or
.width NUM1, NUM2 # customize column width
Run the first two commands from the sqlite3 prompt and then execute the above SELECT statement again and you should see something like this:

id          name        age         breed          owner_id
----------  ----------  ----------  -------------  ----------
1           Maru        3           Scottish Fold  1
2           Hana        1           Tabby          1
3           Lil\' Bub   5           American Shor
4           Moe         10          Tabby
5           Patches     2           Calico
Much better.

ORDER BY
The first query modifier we'll explore is ORDER BY. This modifier allows us to order the table rows returned by a certain SELECT statement. Here's a boilerplate SELECT statement that uses ORDER BY:

SELECT column_name FROM table_name ORDER BY column_name ASC|DESC;
Let's select our cats and order them by age:

SELECT * FROM cats ORDER BY age;
This should return the following:

id          name        age         breed       owner_id
----------  ----------  ----------  ----------  ----------
2           Hana        1           Tabby       1
5           Patches     2           Calico
1           Maru        3           Scottish F  1
3           Lil\' Bub   5           American S
4           Moe         10          Tabby
When using ORDER BY, the default is to order in ascending order. If we want to specify though, we can use ASC for "ascending" or DESC for "descending." Let's try to select all of our cats and sort them by age in descending order.

SELECT * FROM cats ORDER BY age DESC;
This should return

id          name        age         breed       owner_id
----------  ----------  ----------  ----------  ----------
4           Moe         10          Tabby
3           Lil\' Bub   5           American S
1           Maru        3           Scottish F  1
5           Patches     2           Calico
2           Hana        1           Tabby       1
LIMIT
What if we want the oldest cat? If we want to select extremes from a database table — for example, the employee with the highest paycheck or the patient with the most recent appointment — we can use ORDER BY in conjunction with LIMIT.

LIMIT is used to determine the number of records you want to return from a dataset. For example:

SELECT * FROM cats ORDER BY age DESC LIMIT 1;
This part of the statement: SELECT * FROM cats ORDER BY age DESC returns all of the cats in order from oldest to youngest. Setting a LIMIT of 1 returns just the first, i.e. oldest, cat on the list.

Execute the above statement in your terminal and you should see:

id          name        age         breed       owner_id
----------  ----------  ----------  ----------  ----------
4           Moe         10          Tabby
Let's get the two oldest cats:

SELECT * FROM cats ORDER BY age DESC LIMIT 2;
Execute that statement and you should see:

id          name        age         breed       owner_id
----------  ----------  ----------  ----------  ----------
4           Moe         10          Tabby
3           Lil\' Bub   5           American S
How could you retrieve the three youngest cats?
SELECT * FROM cats ORDER BY age ASC LIMIT 3
Ordering query results in ascending order puts the lowest numbers and earliest letters first. Limiting to the first three results will return the three cats with the lowest ages.



BETWEEN
As we've already established, being able to sort and select specific data sets is important. Continuing on with our example, let's say we urgently need to select all of the cats whose age is between 1 and 3. To create such a query, we can use BETWEEN. Here's a boilerplate SELECT statement using BETWEEN:

SELECT column_name(s) FROM table_name WHERE column_name BETWEEN value1 AND value2;
Let's try it out on our cats table:

SELECT name FROM cats WHERE age BETWEEN 1 AND 3;
This should return:

Maru
Hana
Patches
NULL
Let's say the administrator of our Pets Database has found a new cat. This kitty doesn't have a name yet, but should be added to our database right away. We can add data with missing values using the NULL keyword.

Let's insert our new cat into the database. Our abandoned kitty has a breed, but no name or age as of yet:

INSERT INTO cats (name, age, breed) VALUES (NULL, NULL, "Tabby");
Now, if we look at our cats data with SELECT * FROM cats;, we should see:

id          name        age         breed          owner_id
----------  ----------  ----------  -------------  ----------
1           Maru        3           Scottish Fold  1
2           Hana        1           Tabby          1
3           Lil\' Bub   5           American Shor
4           Moe         10          Tabby
5           Patches     2           Calico
6                                   Tabby
We can even select the mysterious, nameless kitty with the following query:

SELECT * FROM cats WHERE name IS NULL;
This should return the following:

id          name        age         breed       owner_id
----------  ----------  ----------  ----------  ----------
6                                   Tabby
COUNT
Now, we'll talk about a SQL aggregate function, COUNT.

SQL aggregate functions are SQL statements that operate on groups of records in our database rather than individual records. For example, we can retrieve minimum and maximum values from a column, sum values in a column, get the average of a column's values, or count a number of records that meet certain conditions. You can learn more about these SQL aggregators hereLinks to an external site. and hereLinks to an external site..

For now, we'll just focus on COUNT. COUNT will count the number of records that meet a certain condition. Here's a boilerplate SQL query using COUNT:

SELECT COUNT([column name]) FROM [table name] WHERE [column name] = [value]
Let's try it out and count the number of cats who have an owner_id of 1:

SELECT COUNT(owner_id) FROM cats WHERE owner_id = 1;
This should return:

COUNT(owner_id)
---------------
2
GROUP BY
Lastly, we'll talk about the handy aggregate function GROUP BY. Like its name suggests, it groups your results by a given column.

Let's take our table of cats

id          name        age         breed          owner_id
----------  ----------  ----------  -------------  ----------
1           Maru        3           Scottish Fold  1
2           Hana        1           Tabby          1
3           Lil\' Bub   5           American Shor
4           Moe         10          Tabby
5           Patches     2           Calico
6                                   Tabby
Here, we can see at a glance that there are three tabby cats and one of every other breed — but what if we had a larger database where we couldn't easily see the number of cats grouped by breed? That's where — you guessed it! — GROUP BY comes in handy.

SELECT breed, COUNT(breed) FROM cats GROUP BY breed;
This should return

breed               COUNT(breed)
------------------  ------------
American Shorthair  1
Calico              1
Scottish Fold       1
Tabby               3
GROUP BY is a great function for aggregating results into different segments — you can even use it on multiple columns!

SELECT breed, owner_id, COUNT(breed) FROM cats GROUP BY breed, owner_id;
Below you can see that the cats are still grouped by breed but are also now further broken down by owner_id, so the two tabby cats without an owner_id are listed separately from the tabby who belongs to owner 1.

breed               owner_id    COUNT(breed)
------------------  ----------  ------------
American Shorthair              1
Calico                          1
Scottish Fold       1           1
Tabby                           2
Tabby               1           1
Note on SELECT
We are now familiar with this syntax:

SELECT name FROM cats;
However, you may not know that this can be written like this as well:

SELECT cats.name FROM cats;
Both return:

name
----------
Maru
Hana
Lil\' Bub
Moe
Patches
SQLite allows us to explicitly state the tableName.columnName we want to select. This is particularly useful when we want data from two different tables.

Imagine we have another table called dogs with a column for the dog names:

CREATE TABLE dogs (
  id INTEGER PRIMARY KEY,
  name TEXT
);
INSERT INTO dogs (name) VALUES ("Clifford");
If we want to get the names of all the dogs and cats, we can no longer run a query with just the column name. SELECT name FROM cats,dogs; will return Error: ambiguous column name: name.

Instead, we must explicitly follow the tableName.columnName syntax.

SELECT cats.name, dogs.name FROM cats, dogs;
You may see this in the future. Don't let it trip you up.

Conclusion
SQL gives you a lot of tools for fine-grained control over how to view data from various database tables. When you start working with larger databases that have 5000 or 50,000 rows in a table instead of 5, having this level of control is crucial for accessing and analyzing data that's useful to your applications, and can help you improve your application's performance significantly by limiting the amount of data being returned.

CRUD Operations in SQL

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

$ sqlite3 pets_database.db
sqlite> .schema
CREATE TABLE cats (
  id INTEGER PRIMARY KEY,
  name TEXT,
  age INTEGER,
  breed TEXT
);
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

$ sqlite3 pets_database.db < 01_insert_cats_into_cats_table.sql
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

$ sqlite3 pets_database.db
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