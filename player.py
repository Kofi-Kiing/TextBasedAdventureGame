import os
import random
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Player:
    def __init__(self):
        self.location = None
        self.items = []
        self.inventory = {}
        self.health = 50
        self.full_health = 60
        self.inventory_max = 7
        self.alive = True
        self.shield_active = False
        self.max_heal_limit = 3
        self.heal_attempts = 0
        self.aggression = round(random.random(), 2)
        

    def move(self, direction):
        directions = {
            'n': 'north', 's': 'south', 'e': 'east', 'w': 'west'
        }
        direction = directions.get(direction, direction)
        if direction not in ['north', 'south', 'east', 'west']:
            return False  
        new_location = self.location.getDestination(direction)
        if new_location:
            self.location = new_location
            return True
        return False
     
    def pickup(self, item):
        if len(self.items) >= self.inventory_max:
            clear()
            print("Inventory full! Consider dropping some items.")
            input("Press Enter to continue...")
            return

        self.items.append(item)
        item.loc = self
        self.location.removeItem(item)

        self.inventory[item.name] = self.inventory.get(item.name, 0) + 1

    
    def display_inventory(self):
        clear()
        print("You currently possess:")
        print()
        for item, value in self.inventory.items():
            if value > 1:
                print(f"{item} x{value}")
            else:
                print(f"{item}")
        print()
        input("Press enter to continue...")
    

    def release(self, item_name):
        clear()
        if not self.items:
            print("\nYour inventory is empty.\n")
            input("Press Enter to continue...")
            return
        item_name = item_name.lower()
        for weapon in self.items:
            if item_name == weapon.name.lower():
                self.items.remove(weapon)
                self.location.addItem(weapon)  
                weapon.loc = self.location     
                if self.inventory.get(weapon.name, 0) > 1:
                    self.inventory[weapon.name] -= 1
                else:
                    self.inventory.pop(weapon.name, None)  
                print(f"\nYou dropped {weapon.name}.\n")
                input("Press Enter to continue...")
                return
        print("\nNo such item in your inventory.\n")
        input("Press Enter to continue...")

   
    def attackMonster(self, mon):
        clear()
        print("You are attacking " + mon.name)
        print()
        print("Your health is " + str(self.health) + ".")
        print(mon.name + "'s health is " + str(mon.health) + ".")
        print()
        if self.health > mon.health:
            self.health -= mon.health
            print("You win. Your health is now " + str(self.health) + ".")
            mon.die()
        else:
            print("You lose.")
            self.alive = False
        print()
        input("Press enter to continue...")
        
    def eat(self):
        clear()
        check = True
        for item in self.items:
            if item.name == 'fish':
                self.health += 5
                print(f"You have eaten a fish. As a result, your health has increased by 6.")
                if self.health > self.full_health:
                    self.health = self.full_health
                    print(f"Your health is {self.health}")
                    print()
                else:
                    print(f"Your health is now {self.health}")
                    print()
                    pass
                check = False
                if 'fish' in self.inventory:
                    if self.inventory['fish'] <= 0:
                        for i in self.items:
                            if i.name == 'fish':
                                self.items.remove(i)
                                break
                        if self.items[-1] == 'fish':
                            self.items.remove(self.items[-1])
                        del self.inventory['fish']
                    else:
                        self.inventory['fish'] -= 1
                else:
                    clear()
                    print("You don't have any fish")
                    input("Press enter to continue...")
                break
        if check:
            clear()
            print("You don't have any fish")
        input("Press enter to continue...")


    def status(self):  
        clear()
        print(f"Health: {self.health}/{self.full_health}") 
        print(f"Aggressiveness: {self.aggression}")
        print(self.location.desc)
        print(f"Inventory: {len(self.items)} items")
        remaining_heals = self.max_heal_limit - self.heal_attempts
        if remaining_heals > 0:
            print(f"Heals remaining: {remaining_heals} ")
        else:
            print("No more heals available.") 
        print()
        input("Press Enter to continue...")

    def specs(self, item_name):
        item_found = False
        for item in self.items:  
            if item_name.lower() == item.name.lower():
                clear()
                print(item.desc)
                print(f"{item.name}'s attack impact: {item.impact}") 
                print()
                input("Press Enter to continue...")
                item_found = True
                break
        if not item_found: 
            for item in self.location.items:
                if item_name.lower() == item.name.lower():
                    clear()
                    print(item.desc)
                    print(f"{item.name}'s attack impact: {item.impact}") 
                    print()
                    input("Press Enter to continue...")
                    item_found = True
                    break
        if not item_found:
             clear()
             print(f"No such item named '{item_name}'.")
             print()
             input("Press Enter to continue...")
        

    def has_combat_gear(self):
        clear()  
        print("\nTaking stock of your equipment...\n")

        weapon_count = 0
        for item in self.items:  
            if item.weapon:  
                print(f"Weapon: {item.name}")
                print(f"Power Level: {item.impact}")
                print("-" * 20)
                weapon_count += 1

        if weapon_count > 0:
            print("\nYou are armed and ready to fight.")
            return True
        else:
            print("\nYour inventory is empty of weapons.")
            print("Find some gear before confronting any threats!")
            input("Press Enter to move on...")
            return False


    def retrieve_weapon(self, weapon):
        weapon = weapon.lower()
        matching_item = next((item for item in self.items if item.name.lower() == weapon), None)

        if matching_item:
            self.items = [item for item in self.items if item != matching_item]  
            matching_item.loc = None

            if self.inventory.get(matching_item.name, 0) > 1:  
                self.inventory[matching_item.name] -= 1
            else:
                self.inventory.pop(matching_item.name, None)  
            return matching_item
        else:
            print("\nYou don't seem to have that weapon in your inventory.")
            input("Press Enter to continue...")
            return None


    def activate_weapon(self, weapon):
        weapon = weapon.lower()
        matching_weapon = next((tool for tool in self.items if tool.name.lower() == weapon), None)

        if matching_weapon:
            self.items = [tool for tool in self.items if tool != matching_weapon]  
            matching_weapon.activate_weapon(self)  
            matching_weapon.loc = None  

            if self.inventory.get(matching_weapon.name, 0) > 1:
                self.inventory[matching_weapon.name] -= 1
            else:
                self.inventory.pop(matching_weapon.name, None)  
        else:
            clear()  
            print("\nThe item you're looking for isn't in your inventory.\n")
            input("Press Enter to continue...")
             

    def restore_health(self):
        if self.heal_attempts < self.max_heal_limit:
            clear()  
            self.health = self.full_health  
            self.heal_attempts += 1  
            
            print("\nYour health has been fully restored. You now have one less healing opportunity.")
            input("Press Enter to continue...")
        else:
            clear()  
            print("\nAll healing options have been used up.")
            input("Press Enter to move on...")

    
    def activate_shield(self):
        shield_item = next((item for item in self.items if item.name.lower() == 'shield'), None)

        if shield_item:
            user_response = input("Would you like to activate your shield? (yes/no): ").strip().lower()

            if user_response == 'yes':
                self.shield_active = True
                self.items = [item for item in self.items if item != shield_item]  
                self.inventory.pop('shield', None)  

                print("\nShield activated successfully.")
            else:
                print("\nShield activation canceled.")
        else:
            print("\nYou don't have a shield in your inventory.")

        return

            

    def sustain_damage(self, animal):
            damage_multiplier = 0.5 if self.shield_active else 1.0
            self.health -= animal.impact_of_attack * damage_multiplier
        
    
    def attack_animal(self, weapon, animal):
        
        def display_initial_status(self, animal):
            clear()
            print(f"Get ready to fight {animal.name} !!!")
            print(f"Your health: {self.health}")
            print(f"{animal.name}'s health: {animal.health}")
            print("Defeat occurs when health reaches zero")
            
            # Check if shield is in inventory
            if 'shield' in self.inventory:
                print("Shield detected in inventory!")
                self.activate_shield()
            
            clear()
            input("Press enter to continue...")
        
        def check_input(question, valid_options):
            while True:
                user_input = input(question).lower()
                if user_input in valid_options:
                    return user_input
                print("Wrong Input. Try again.")
        
        def exit():
            while True:
                exit_choice = check_input("Confirm exit? (yes/no): ", ['yes', 'no', 'y', 'n'])
                if exit_choice in ['yes', 'y']:
                    return False
                return True
        
        display_initial_status(self,animal)
        
        while True:
            clear()
            print(f"Your health: {self.health}")
            print(f"{animal.name}'s health: {animal.health}")
            print()
            
            # Player's attack turn
            player_direction = check_input("Attacking direction? (left/right/exit): ", ['left', 'right', 'exit'])
            
            if player_direction == 'exit':
                if not exit():
                    return False
            
            animal_direction = random.choice(["left", "right"])
            
            if (player_direction == "right" and animal_direction == "right") or \
            (player_direction == "left" and animal_direction == "left"):
                animal.sustain_damage(self, weapon)
                print(f"Direct hit on {animal.name}!")
            else:
                print("You missed your target!")
            
            input("Press Enter to continue...")
            
            # Checking if player or animal is defeated
            if self.health <= 0:
                clear()
                print("Quest Terminated!")
                print("Poor performance")
                print("Reconsider your strategy.")
                input("Press Enter to continue...")
                self.alive = False
                return
            
            if animal.health <= 0:
                clear()
                print("Victory Secured!")
                print(f"You defeated the {animal.name} to move to the next checkpoint!")
                input("Press Enter to continue...")
                animal.die()
                return
            
            # Animal's attack turn
            clear()
            print(f"Your health: {self.health}")
            print(f"{animal.name}'s health: {animal.health}")
            print(f"{animal.name} prepares to counterattack!")
            
            player_direction = check_input("Which way to evade? (left/right/exit): ", ['left', 'right', 'exit'])
            
            if player_direction == 'exit':
                if not exit():
                    return False
            
            animal_direction = random.choice(["left", "right"])
            
            if (player_direction == "right" and animal_direction == "right") or \
            (player_direction == "left" and animal_direction == "left"):
                self.sustain_damage(animal)
                print(f"{animal.name} bit you!")
            else:
                print(f"{animal.name}'s attack was thwarted.")
            
            input("Press Enter to continue...")
            
            # Rechecking defeat conditions after animal's turn
            if self.health <= 0:
                clear()
                print("You've been defeated!")
                print("Your quest concludes in failure.")
                print("Reconsider your strategy.")
                input("Press Enter to continue...")
                self.alive = False
                return
            
            if animal.health <= 0:
                clear()
                print("Victory Secured!")
                print(f"You killed {animal.name}")
                input("Press Enter to continue...")
                animal.die()
                return