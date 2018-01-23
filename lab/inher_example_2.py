class Animal:
    def __init__(self, name):
        self.name = name
        self.age = 3
        self.weight = 3
        self.hasTail = True
        self.likePlayWool = True

    def makeNoise(self):
        pass

    def eat(self):
        self.weight += 3


class Dog(Animal):
    def __init__(self, name):
        super().__init__()

    def eat(self):
        self.weight += 10


d = Dog('hey')
d.eat()
print(d.weight)
