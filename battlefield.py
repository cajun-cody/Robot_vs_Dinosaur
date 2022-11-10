from dinosaur import Dinosaur
from robot import Robot

class Battlefield:          
    def __init__(self) -> None:
        self.dinosaur = Dinosaur()
        self.robot = Robot()
        pass
    
    def start_fight(self):
        print('\nRound 1!\nFight!\n')
        pass

    def robot_attack(self):
        self.dinosaur.health -= self.robot.active_weapon.attack_power
        print(f"{self.robot.name}, dealt {self.robot.active_weapon.attack_power} damage with {self.robot.active_weapon.name}!")
        print(f"{self.dinosaur.name} has {self.dinosaur.health} health remaining.\n")
        pass
            
    def dinosaur_attack(self):
        self.robot.health -= self.dinosaur.attack_power
        print(f"{self.dinosaur.name}'s attack, dealt {self.dinosaur.attack_power} damage!")
        print(f"{self.robot.name} has {self.robot.health} health remaining.\n")
        pass

    def battle(self):
        while self.robot.health > 0 and self.dinosaur.health > 0:
            self.robot_attack()
            if self.dinosaur.health > 0:
                self.dinosaur_attack()
           
    def declare_winner(self):
        if self.robot.health <= 0:
            print(f'{self.dinosaur.name} is Victorious!')
        elif self.dinosaur.health <= 0:
            print(f'{self.robot.name} is Victorious!\n')


    def run_game(self):
        self.start_fight()
        self.battle()
        self.declare_winner()
        pass





              