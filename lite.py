class Empire:
    def __init__(self, song, name, age):
        self.song = song
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Empire(song='{self.song}', name='{self.name}', age={self.age})"

    def introduce(self):
        return f"My name is {self.name}, I am {self.age}, and my song is '{self.song}'."

    def change_song(self, new_song):
        self.song = new_song
        return f"{self.name}'s song has been updated to '{self.song}'."

# Create objects
empire1 = Empire("Hii maisha", "Pat", 20)
empire2 = Empire("Nairobi vibe", "John", 25)
empire3 = Empire("Summer Love", "Lisa", 22)

# Store in a list
empires = [empire1, empire2, empire3]

# Print all objects
print("All Empire Objects:")
for e in empires:
    print(e)

# Use the methods
print("\nIntroductions:")
print(empire1.introduce())
print(empire2.introduce())

print("\nUpdating Song:")
print(empire1.change_song("New Anthem"))
print(empire1.introduce())

