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
