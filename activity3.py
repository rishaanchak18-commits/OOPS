class Parrot:
    species = "Bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age
Blu = Parrot("Blu", 2)
Wu= Parrot("Woo", 4)

print("Blu is a {}".format(Blu.species))
print("Wu is a {}".format(Wu.species))

print("{} is {} years old".format(Blu.name, Blu.age))
print("{} is {} years old".format (Wu.name, Wu.age))

print("Age of Parrot2 is", Wu.age)
print("Name of Parrot2 is", Wu.name)
print("Age of Parrot1 is", Blu.age)