

class Dinosaur:
    def __init__(self) -> None:
        self.name = 'Saurian'
        self.health = 100
        self.attack_power = 20
        pass

   
    def attack(self,robot):
        robot.health -= self.attack_power
        print(f"{self.name}'s attack, dealt {self.attack_power} damage!")
        print(f"{robot.name} has {robot.health} health remaining.\n")
        pass