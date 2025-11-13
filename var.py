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
