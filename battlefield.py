from dinosaur import Dinosaur
from robot import Robot

class Battlefield:          #Call dino and robot into battlefield
    def __init__(self) -> None:
        self.dinosaur = Dinosaur()
        self.robot = Robot()
        pass
    
    def start_fight(self):
        print('\nRound 1!\nFight!')
        pass

    def robot_attack(self):
        self.dinosaur.health -= self.robot.active_weapon.attack_power
        print(f"{self.robot.name}, dealt {self.robot.active_weapon.attack_power} damage!\n")
        pass
            
    def dinosaur_attack(self):
        self.robot.health -= self.dinosaur.attack_power
        print(f"{self.dinosaur.name}, dealt {self.dinosaur.attack_power}!")
        pass

    def battle(self):
        self.robot_attack()
        self.dinosaur_attack()
        for a in range(1, 100):
            if self.robot.health or self.dinosaur.health > 0:
                print("Robot health is {self.robot.health}.")
                print("Robot health is {self.dinosaur.health}.")
        pass           

    def run_game(self):
        self.battle()
        pass


 