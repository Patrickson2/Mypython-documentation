# so this is all about classes and objects 
# CLASS
#    -classes are like blueprint 
#  Example: A blueprint for a car. It defines what a car can have (attributes) and can do (methods)

# OBJECT
    #  -An object is an actual thing made from the blueprint.
# Example: Your red Toyota car is an object of the class Car.


        #    EXAMPLE CODE 1
# this code contains only attributes where Attributes are data or properties that belong to an object.
class Movie:
    
    # the innit is a constructor
    # laymans lang the __innit__ acts like a mother yeye ndo anazaa mtoto
    def __init__ (self):
    # alafu self acts like the father giving out the name to the child
        self.my_movies = ["rambo", "spiderman","ben10"]

my_movie = Movie()
print(my_movie.my_movies)


        #    EXAMPLE CODE 2
# this code contains both attributes and methods where methods are functions that objects can perform
class student:
    def __init__(self , marks, grade):
        self.marks = marks
        self.grade = grade
    def __str__(self):
        return f'this {self.marks} is the marks and this {self.grade}'
so = student('79' , 'grade')
print(so)
