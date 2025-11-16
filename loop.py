# loops- have diff types 
#    1. A for loop lets you repeat a block of code for each item in a sequence (like a list, tuple, or range of numbers).
 
# EXAMPLE CODE using FOR
# fruit is a temporary variable for each item in this list.
# The loop runs once for each item.

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
                #    OUTPUT WILL BE 
                # (apple, banana, cherry)

# EXAMPLE 2 using RANGE
for i in range(5):
    print(i)
                #    OUTPUT WILL BE 
                # (0,1,2,3,4) meaning that range(5) generates numbers from 0-4 and (i) changes automatically each time the loop runs

# MY EXAMPLE1 TO CHECK UNDERSTANDING
for i in range(3, 8):
    print(i)
                #    OUTPUT WILL BE 
                # (4,5,6,7) this is because the i is looping the numbers btwn 3 and 8 

# MY EXAMPLE2 TO CHECK UNDERSTANDING
for n in range(2, 10, 2):
    print(n)
                #    OUTPUT WILL BE 
                # (2,4,6,8) this is known as the (step size) in the Range  
                #  The last number in range(start, stop, step) is the step size.
                #  It’s how much Python adds every time the loop runs.

# ADDITIONAL RANGE
squared_minus_one = list()

for n in range(1, 11):
    squared_minus_one.append((n ** 2) - 1)

print(squared_minus_one)
                #    OUTPUT WILL BE 
                # [0, 3, 8, 15, 24, 35, 48, 63, 80, 99]
                
                    # FOR BETTER UNDERSTANDING IN THIS RANGE LOOP
# | start            | stop          | step | Works?                     | Reason |
# | ---------------- | ------------- | ---- | -------------------------- | ------ |
# | smaller → bigger | positive step | ✔️   | moving the right direction |        |
# | smaller → bigger | negative step | ❌    | step direction wrong       |        |
# | bigger → smaller | negative step | ✔️   | moving the right direction |        |
# | bigger → smaller | positive step | ❌    | step direction wrong       |        |


            #    WHILE LOOPS

# while =>executes a statement number of times while the condition is true 
    # EXAMPLE CODE 1

count = 0

while count <= 10:
    print("Kiongozi")
    count += 1  

# for >= used to iterate over the sequence
    # EXAMPLE CODE 2

Fruit = ["Apple", "Orange","Kiwi","Mango"]

for Fruit in Fruit:
    if Fruit == "Kiwi":
        print("Healthy")
        break 

# ininite loops are the ones that never end untill you introduce a special work "BREAK" that stops the ininite like example above 

# | Concept              | Example                 | Behaviour                    |
# | -------------------- | ----------------------- | ---------------------------- |
# | Basic while          | `while x < 5:`          | Runs while condition is true |
# | Updating variable    | `x += 1`                | Prevents infinite loop       |
# | User-controlled loop | `while name != "stop":` | Stops when user types stop   |
# | Infinite loop        | Condition never changes | Never ends                   |
# | break                | `break` inside loop     | Stops the loop early         |


