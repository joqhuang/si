class Pet:
    def __init__(self, hungry=0, bored=0):
        self.hungry = hungry
        self.bored = bored

    def eat(self):
        self.hungry -= 2
        self.bored += 1

    def play(self):
        self.bored -= 2
        self.hungry += 5

    def check_mood(self):
        if self.hungry > 10:
            print("I'm hungry :(")
        elif self.bored > 6:
            print("I'm bored >.<")
        elif self.hungry > 2 and self.bored > 2:
            print("Meh")
        else:
            print("Happy! o3o")

pet_inst = Pet(7,5)
pet_inst.play()
pet_inst.check_mood()
pet_inst.eat()
pet_inst.check_mood()
