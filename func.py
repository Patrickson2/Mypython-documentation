# my function display
# the use of the def word shows that the rest of the code is being a function
def greet_programmer():
    print("Hello, programmer!")

# greet_programmer = "Hello, programmer!"
greet_programmer()

# on this code i cannot excute because i am overiding the entire code wile still calling line 6
            #  python3 func.py
            #  Traceback (most recent call last):
            #    File "/home/mungai/Documents/moringaProjects/phase3/python-class/func.py", line 7, in <module>
                #  greet_programmer()
            #  TypeError: 'str' object is not callable

# so to go about this i commented on line 6 to remove the overide of the code.

# this is a default argument  
def say_hi(name="Engineer"):
    # the "f"(formatted string)It lets you insert variables directly inside a string using {} then Python replaces the {} part with the actual value of the variable.
    # inshort nisipoweka the "F" the whole text in the "" itakuwa passed down kwa terminal.
    print(f"Hi there, {name}!")

say_hi()

say_hi("Sunny")
# output will be Hi there, Engineer! Hi there, Sunny!









