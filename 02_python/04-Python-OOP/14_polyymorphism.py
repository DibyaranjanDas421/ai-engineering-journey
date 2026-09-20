class Dog:
    def make_sound(self):
        print("Woof!")


class Cat:
    def make_sound(self):
        print("Meow!")



def play_sound(animal):
    animal.make_sound()


dog = Dog()
cat = Cat()

play_sound(dog)
play_sound(cat)