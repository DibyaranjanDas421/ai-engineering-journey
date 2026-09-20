
class Person:

    def __init__(self, name, age=None, address=None):
        self.name = name
        self.age = age
        self.address = address

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Address:", self.address)


# 1. Name only
p1 = Person("Dibya")

# 2. Name + age
p2 = Person("Rahul", 25)

# 3. Name + age + address
p3 = Person("Amit", 30, "Mumbai")

p1.display()
print()

p2.display()
print()

p3.display()