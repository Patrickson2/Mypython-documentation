class Human:
    def __init__(self, name, age="40"):
        self.name = name
        self.age = age
h1 = Human("Kamau", 20)
h2 = Human("kamara")
print(h1.name, h1.age)   
print(h2.name, h2.age)     


# line-by-line meaning

# class Human:
# Create a blueprint for a human.

# def __init__(self, name, age="40"):
# When you make a human, they must have a name.
# If you don’t give an age, it will be 40 by default.

# self.name = name
# Give that person their name.

# self.age = age
# Give that person their age.

# h1 = Human("Kamau", 20)
# Make a human named Kamau, age 20.

# h2 = Human("kamara")
# Make a human named kamara, age defaults to 40.