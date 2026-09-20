
class Herbivore:
    def eat_plants(self):
        print("Eats plants")


class Carnivore:
    def eat_meat(self):
        print("Eats meat")


class Omnivore:
    def eat_both(self):
        print("Eats both plants and meat")


class Bear(Herbivore, Carnivore, Omnivore):
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Animal name:", self.name)


# Creating an object
b1 = Bear("Bear")

b1.show_name()
b1.eat_plants()
b1.eat_meat()
b1.eat_both()