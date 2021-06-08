class Pets:
    def walk(self):
        print("walk")


class Dog(Pets):
    def bark(self):
        print("bark")


class Cat(Pets):
    def scratch(self):
        print("scratching")

    def annoying(self):
        print("is annoying")


dog1 = Dog()
dog1.bark()
cat1 = Cat()
cat1.annoying()
