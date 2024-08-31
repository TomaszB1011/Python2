class Animal:
    def __init__(self):
        print("Animal")

    def increase_age(self):
        print("increase age")

class Mammal(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Mammal")

    def introduce_yourself(self):
        print("introduce_yourself")

class Cat(Mammal):
    def __init__(self):
        Mammal.__init__(self)
        print("Cat")

    def purr(self):
        print("Purr")

my_cat = Cat()

my_cat.introduce_yourself()
my_cat.purr()
my_cat.increase_age()