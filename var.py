message = "Hello from outside"

def greet():
    print(message)
    greet()
    print(message) 


def greet():
    message = "Hello from inside the function"
    print(message)  

greet()
# print(message)  
# on the line above will bring an error message that the message is not defined thus making it a comment 

name = "Patrickson"

def greet():
    message = "Welcome back"
    print(message, name)

def change_name():
    name = "Alex"
    print("Inside change_name:", name)

greet()
change_name()
print("Outside:", name)


# when wanting To change the value of a global variable from a local scope, we need to use the global keyword eg:
change_the_world = "change yourself"

def change_yourself():
    global change_the_world
    change_the_world = "world changed"

change_yourself() 
print(change_the_world)
# print(change_yourself)

# on this code below shows why you cannot print change yourself again on line 41 because python will like ignore it and produce it as a memory address
def say_hi():
    print("Hi there!")

print(say_hi)
say_hi()

# this is like a break down of the code on assigning the global keyword
change_the_world = "change yourself"

def change():
    print(change_the_world)
change()
