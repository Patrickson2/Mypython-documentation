# this is the comparison operator example code 
a = 10
b = 15

print(a == b)
print(a != b)
print(a < b)
print(a >= b)

# this is a logical operator example code
x = True
y = False

print(x and y)
print(x or y)
print(not x)

# combining the conditions

# if age >= 18 or canVote:
#     print("You are an Adult")
# else:
#     print("You are under age")

# example 2 of combining conditions 
age = 20
has_id = False

if age >= 18 and has_id:
    print("You may enter.")
elif age >= 18 and not has_id:
    print("You are old enough but missing ID.")
else:
    print("You cannot enter.")
    #   this outputs the "You are old enough but missing ID." because of the "and" statement that is being passed 
    # this is because we are using the and logic operator and thus if the has_id was to be true , 
    # it will output would be passed but in here the has id is being passed as false under the use of and making it to be false in the end 
    # so in the end With "and", both conditions must be true. and Since "has_id is False", the whole expression becomes "False".

# example 3 but now trying to input something in the terminal
name = input("Enter your name: ")
    # the int is to input an integer mostly without placing any integer you get an error in output
age = int(input("Enter your age: "))

if age < 18:
    print(f"Hello {name}, you are still young.")
elif age <= 30:
    print(f"Hello {name}, you are in your youth.")
else:
    print(f"Hello {name}, you are grown.")


# example 4 the output shows if number is even or odd while using modulus
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# example 4 the marks grading in python
marks = int(input("Enter your score: "))

if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
elif marks >= 60:
    print("D")
else:
    print("F")



# example 5 positive, negative pattern if a num is being inputted 
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

