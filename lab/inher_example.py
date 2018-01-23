class Dog:
    def __init__(self, name):
        self.name = name
        self.age = 7
        self.weight = 10
        self.hasTail = True
        self.likePlayBall = True

    def makeNoise(self):
        print("Bark")

    def eat(self):
        self.weight += 10

####################################
class Cat:
    def __init__(self, name):
        self.name = name
        self.age = 3
        self.weight = 3
        self.hasTail = True
        self.likePlayWool = True

    def makeNoise(self):
        print("Meow")

    def eat(self):
        self.weight += 3

####################################
class Fish:
    def __init__(self, name):
        self.name = name
        self.age = 3
        self.weight = 0.1
        self.hasTail = True
        self.closeEyes = False

    def makeNoise(self):
        print("...")

    def eat(self):
        self.weight += 0.01

#####################################

# class Insect:
    # ...
