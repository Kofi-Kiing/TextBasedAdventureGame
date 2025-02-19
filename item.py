import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Item:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.loc = None

    def describe(self):
        clear()
        print(self.desc)
        print()
        input("Press enter to continue...")   
    
    def putInRoom(self, room):
        self.loc = room
        room.addItem(self)
    
class Pocketknife(Item):
    def __init__(self):
        pass
        self.name = "pocket knife"
        self.desc = "Designed for killing animals from close range either on land or lake"
        self.loc = None
        self.weapon = True
        self.impact = 5
        

class Stone(Item):
    def __init__(self):
        self.name = "stone"
        self.desc = "Make fire for the night and can also be used as a weapon"
        self.loc = None
        self.weapon = True
        self.impact = 2

class Firewood(Item):
    def __init__(self):
        self.name = "firewood"
        self.desc = "Make fire for the night"
        self.loc = None
        self.weapon = False
        print("you've made some fire")
        

class Sword(Item):
    def __init__(self):
        self.name = "sword"
        self.desc = "Designed to strike aggressive animals on land"
        self.loc = None
        self.weapon = True
        self.impact = 7

class HuntingRifle(Item):
    def __init__(self):
        self.name = "hunting rifle"
        self.desc = "Designed to shoot animals from a far range on land"
        self.loc = None
        self.weapon = True
        self.impact = 9

class Trident(Item):
    def __init__(self):
        self.name = "trident"
        self.desc = "Designed to kill animals in lake"
        self.loc = None
        self.weapon = True
        self.impact = 9

class Shield(Item):
    def __init__(self):
        self.name = "shield"
        self.desc = "Designed to protect you against attack from animals on land"
        self.loc = None
        self.weapon = False

class Fish(Item):
    def __init__(self):
        self.name = "fish"
        self.desc = "Eat to fill health by 6"
        self.loc = None
        self.weapon = False
    def eat(self, player):
        player.health += 6
    