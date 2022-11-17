
from weapon import Weapon

class Robot:
    def __init__(self) -> None:
        self.name = 'Cyrax'
        self.health = 100
        self.active_weapon = Weapon()
        pass

    def attack(self,dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
        print(f"{self.name}, dealt {self.active_weapon.attack_power} damage with {self.active_weapon.name}!")
        print(f"{dinosaur.name} has {dinosaur.health} health remaining.\n")
        pass

