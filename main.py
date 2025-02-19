from room import Room
from player import Player
from item import Item, Pocketknife,HuntingRifle,Sword,Stone,Trident,Shield,Fish,Firewood
from monster import Monster
import os
import updater
import random 

player = Player()

a = Room("You are in checkpoint 1")
b = Room("You are in checkpoint 2")
c = Room("You are in checkpoint 3")
d = Room("You are in checkpoint 4")
e = Room("You are in checkpoint 5")
f = Room("You are in checkpoint 6")
g = Room("You are in checkpoint 7")
h = Room("You are in checkpoint 8")
j = Room("You are in checkpoint 10")

    
Monster("Leopard", b, 10, 3)
Monster("Wolf", c, 12, 4)
Monster("Alligator", d, 14, 4)
Monster("Tiger", e, 18, 5)
Monster("Crocodile", g, 20, 5)
Monster("Lion", h, 30, 6)
Monster("Grizzly Bear", j, 50, 10)

Room.connectRooms(a, "east", b, "west")
i = Sword()
fish = Fish()
stone=Stone()
firewood=Firewood()
tr = Trident()
i.putInRoom(a)
fish.putInRoom(a)
fish.putInRoom(f)
stone.putInRoom(f)
tr.putInRoom(f)
firewood.putInRoom(f)

player.location = a
def gift(room):
    gifts = [Fish(), Stone(), HuntingRifle(), Sword(), Trident(), Shield()]
    for gh in range(2):
        gift = random.choice(gifts)
        gift.putInRoom(room)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def printSituation():
    clear()
    print(player.location.desc)
    print()
    if player.location.hasMonsters():
        print("You've been spotted by a ",end='')
        for m in player.location.monsters:
            print(m.name, end='')
        print(" and its about to about to attack you")
        print()
    if player.location.hasItems():
        print("There are items hidden at this checkpoint, pick them up:")
        for i in player.location.items:
            print(i.name)
        print()
    print("You can go in the following directions:")
    for e in player.location.exitNames(player):
        print(e)
    print()


def introduction():
    clear()
    print("Welcome to the Golden Stool Quest! 🏆")
    print("Your mission: Retrieve the stolen Golden Stool from dwarfs in the Amazon.")
    print("Defeat wild animals guarding the treasure.")
    print("Type 'help' for game commands.")
    print()
    input("Press enter to continue...")


def showHelp():
    clear()
    print("go <direction> -- moves you in the given direction")
    print("inventory / inv / inven -- opens your inventory")
    print("inspect <item> -- gives details about the weapon, either you're carrying it or it's in the room you are.")
    print("defend -- defend yourself against wild animals")
    print("wait -- delay the player in the room, but time keep on passing")
    print("pickup <item> -- picks up the item")
    print("status -- provides an overview of your character's current condition and possessions")
    print('drop <item> -- remove an item from your personal inventory')
    print("exit -- terminates the game session")
    print("heal --- fully replenishes the player's health points")
    print("Navigation options include: 'n' for north, 'e' for east, 's' for south, 'w' for west")
    print("Simply typing 'attack' will initiate combat with nearby monsters.")
    print("Use 'y' to confirm and 'n' to deny")
    print("Weapon selection significantly influences damage dealt to monsters.")
    print("Your character's aggression level directly impacts the intensity of combat strikes.")
    print("Utilizing a shield reduces incoming monster damage by 50%")
    print()
    input("Press enter to continue...")

def arsenal(room):
    number = random.randint(1,2)
    a1 = Sword()
    a2 = Shield()
    a3 = HuntingRifle()
    asn = [a1, a2, a3]
    random.shuffle(asn)
    while number:
        an = random.choice(asn)
        an.putInRoom(room)
        number -= 1
    return

arsenal(b)
arsenal(g)
arsenal(h)
arsenal(a)
arsenal(d)
arsenal(c)


checkpoint_1, checkpoint_2, checkpoint_3, checkpoint_4, checkpoint_5, checkpoint_6, checkpoint_7, checkpoint_8, checkpoint_9 =  True, True, True, True, True, True, True, True, True
def Situation():
    global checkpoint_1, checkpoint_2, checkpoint_3, checkpoint_4, checkpoint_5, checkpoint_6, checkpoint_7, checkpoint_8, checkpoint_9
    if player.location == j and not player.location.hasMonsters() and checkpoint_9:
        clear()
        print("Congratulations you have completed the quest! 🎉🎊🥳")
        print("You've retrieved the golden stool!!!")
        print("Return it to the Ashanti kingdom to restore honor to the Kingdom!")
        print()
        input("Press enter to continue...")
        return True
    if player.location == b and not player.location.hasMonsters() and checkpoint_1:
        clear()
        gift(player.location)
        player.health += 2
        player.full_health += 2
        checkpoint_1 = False
        Room.connectRooms(b, "north", c, "south")
            
            
    if player.location == c and not player.location.hasMonsters() and checkpoint_2:
        clear()
        gift(player.location)
        player.health += 2
        player.full_health += 2
        checkpoint_2 = False
        Room.connectRooms(c, "east", d, "west")
            
    if player.location == d and not player.location.hasMonsters() and checkpoint_3:
        clear()
        print("You've gained 2 additional health points and also expanded your maximum health by 2")
        print()
        input("Press enter to continue...")
        gift(player.location)
        player.health += 2
        player.full_health += 2
        checkpoint_3 = False
        Room.connectRooms(d, "north", e, "south")

    if player.location == e and not player.location.hasMonsters() and checkpoint_4:
        clear()
        player.health += 2
        player.full_health += 2
        checkpoint_4 = False
        Room.connectRooms(e, "east", f, "west")
        
    if player.location == f and checkpoint_5:
        clear()
        print()
        print("It's night time already")
        print("pickup some firewood and stone to make fire to keep yourself warm for the night!") 
        print("You increase your health by making a fire🔥")
        checkpoint_5 = False
        print()
        input("Press enter to continue...")
        Room.connectRooms(f, "north", g, "south")
        
    if player.location == g and not player.location.hasMonsters() and checkpoint_6:
        clear()
        gift(player.location)
        player.health += 3
        player.full_health += 3
        checkpoint_6 = False
        Room.connectRooms(g, "east", h, "west")
    
    if player.location == h and not player.location.hasMonsters() and checkpoint_7:
        clear()
        gift(player.location)
        player.health += 4
        player.full_health += 4
        checkpoint_7 = False
        Room.connectRooms(h, "north", j, "south")

    

    
introduction()        
playing = True
while playing and player.alive:
    if Situation():
        break
    printSituation()
    for mon in player.location.monsters:
        if mon.aggression >= 0.70:
            mon.attack_player(player)
            Situation()
            printSituation()
            break
    commandSuccess = False
    timePasses = False
    while not commandSuccess:
        commandSuccess = True
        command = input("What now? ")
        while not command:
            printSituation()
            print("Invalid command. Please try again.")
            print()
            command = input("Your next action: ")
        
        commandWords = command.split()
        if commandWords[0].lower() == "go":
            direction = commandWords[1].lower()
            go_ahead = player.move(direction)
            if go_ahead:
                timePasses = True
            else:
                clear()
                print("That path is not accessible.")
                input("Press Enter to choose a different path...")


        elif commandWords[0].lower() == "inventory" or commandWords[0].lower() == "inv":
            player.display_inventory()      

        elif commandWords[0].lower() == "help":
            showHelp()
  
        elif commandWords[0].lower() == "status":
            player.status()

        elif commandWords[0].lower() == "wait":
            timePasses = True

        elif commandWords[0].lower() == 'heal':
            player.restore_health()

        elif commandWords[0].lower() == "specs":
            weapon = command[6:]
            player.specs(weapon)
            
        elif commandWords[0].lower() == "eat":
            player.eat()
            
        elif commandWords[0].lower() == "drop":
            item = command[5:].lower()
            player.release(item)
        
        elif commandWords[0].lower() == "pickup" or commandWords[0].lower() == "pick":  #can handle multi-word objects
            targetName = command[7:]
            target = player.location.getItemByName(targetName)
            if 'firewood' in targetName:
                player.health+=1
            if target != False:
                player.pickup(target)
            else:
                print("No such item.")
                commandSuccess = False

        elif commandWords[0].lower() == "exit":
            clear()
            print("Are you sure you want to quit?")
            decision = input("yes / no? ")
            if decision.lower() == 'yes' or decision.lower() == 'y':
                playing = False
            elif decision.lower() == 'no' or decision.lower() == 'n':
                input("Press enter to continue...")
                pass
            else:
                clear()
                print("Invalid Input")
                print("Re-type exit, yes or no.")
                print()
                commandSuccess = False


        elif commandWords[0].lower() == "defend":
            if player.location.hasMonsters():
                if player.has_combat_gear():
                    
                    target = player.location.getMonsterByLocation()
                    if target != False:
                        if player.has_combat_gear():
                            print()
                            print("Kindly select a weapon to fight. ")
                            print()
                            weapon = input("Weapon? ")
                            if weapon =='':
                                while True:
                                    clear()
                                    player.has_combat_gear()
                                    print("Kindly select a weapon to fight. ")
                                    print()
                                    weapon = input('Weapon? ')
                                    if weapon != '':
                                        break
                            weapon = player.retrieve_weapon(weapon)
                            if weapon:
                                player.attack_animal(weapon, target) 
                            else:
                                check = True
                                while check:
                                    clear()
                                    player.has_combat_gear()
                                    print("Kindly select a weapon to fight. ")
                                    print()
                                    print("Make no mistakes in typing the weapon name")
                                    print()
                                    weapon = input('Weapon? ')
                                    weapon = player.retrieve_weapon(weapon)
                                    if weapon:
                                        check = False
                                        player.attack_animal(weapon, target)
                        else:
                            commandSuccess = False
                    else:
                        print("No such monster.")
                        commandSuccess = False
            else:
                clear()
                print("Checkpoint has no wild animals. ")
                print()
                input("Press enter to continue...")
        else:
            clear()
            print("Not a valid command")
            print()
            input("Press enter to continue...")
    if timePasses == True:
        updater.updateAll() 

