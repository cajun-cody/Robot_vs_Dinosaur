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

    def battle(self):
        while self.robot.health > 0 and self.dinosaur.health > 0:
            self.robot.attack(self.dinosaur)
            self.dinosaur.attack(self.robot)
           
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





              