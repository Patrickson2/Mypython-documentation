# Data types tell Python what kind of value you’re dealing with.
# Example:

# python
# Copy code
# x = 5        # integer
# y = "five"   # string
# Python treats them differently: one can do math, one is text.

# EXAMPLE CODE INTERGES & FLOATS

x = 10
y = 3.5
print(x + y)
print(type(x), type(y))

# EXAMPLE  CODE 2  STRINGS 
# strings in Python are immutable or ordered --meaning their position matters, but you can’t change them directly once created.
# they are defined by either single quotes '' or double quotes ""
name = "Patrickson"
greeting = "Hello, " + name + "!"
print(greeting)
# (TYPE) -- in python represents if the data being shown id either a class,string or boolean
print(type(name))  
print(name.upper())
# the 0:4 indicates the total numbers or texts that will bne dispalyed in the console/ termianal
print(name[0:4])


# EXAMPLE CODE 3 BOOLEAN
# The boolean always represent the true/ false logic 

is_ready = True
is_logged_in = False

print(is_ready, type(is_ready))
print("not is_ready:", not is_ready)
print("is_ready and is_logged_in:", is_ready and is_logged_in)
print("is_ready or is_logged_in:", is_ready or is_logged_in)

