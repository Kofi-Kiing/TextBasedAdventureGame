import random
import updater
import os
import player
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
class Monster:
    def __init__(self, name, location, health, impact_of_attack = 0,aggression = 0):
        self.name = name
        self.location = location
        self.health = health
        self.impact_of_attack = impact_of_attack 
        location.addMonster(self)
        if aggression:
            self.aggression=aggression
        else:
            self.aggression=random.random()
        updater.register(self)
    
    def update(self):
        pass
    
    def moveTo(self, location):
        self.location.removeMonster(self)
        self.location = location
        location.addMonster(self)
   
    def die(self):
        self.location.removeMonster(self)
        updater.deregister(self)


    def sustain_damage(self, player, weapon):
        if player.aggression >= 0.85:
            self.health -= 2.0 * weapon.impact
        elif player.aggression >= 0.65 and player.aggression < 0.85:
            self.health -= 1.5 * weapon.impact
        elif player.aggression >= 0.45 and player.aggression < 0.65:
            self.health -= 1.2 * weapon.impact
        else:
            self.health -= 0.8 * weapon.impact



    def attack_player(self, player):
        print(f"You sense danger looming as {self.name} draws closer.")
        print()
        print(f"Your health stands at {player.health}.")
        print("Do you have the courage to face the threat or will you retreat?")
        print(f"Staying here will only give {self.name} the chance to corner you.")
        print(f"Every second you hesitate, {self.name} inches closer, ready to strike.")

        battle_in_progress = False
        while not battle_in_progress:
            print()
            print(f"{self.name} strikes!")  
            battle_in_progress = True
            player.sustain_damage(self)
            print(f"Your health is now {player.health}")
            action = input("What will you do next? (fight/run): ").strip().lower()
            if action.lower() == 'run' or action.lower() == 'r':
                clear()
                pass
            elif action.lower() == 'fight' or action.lower() == 'f':
                if player.has_combat_gear(): 
                    print()
                    print("Kindly select a weapon to fight")
                    weapon = input("Weapon? ")
                    weapon = player.retrieve_weapon(weapon)
                    if weapon:
                        player.attack_animal(weapon, self)
                        return
                else:
                    print(f"You are unarmed and defenseless against {self.name}. Retreat is your only option!")
                    battle_in_progress = False
            else:
                battle_in_progress = False

        