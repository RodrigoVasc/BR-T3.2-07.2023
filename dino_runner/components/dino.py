import pygame

from dino_runner.utils.constants import RUNNING, JUMPING
X_POS = 
Y_POS = 

class Dino:
    def __init__(self):
        self.image = RUNNING[0]
        self.dinoRun = True
        self.dinoJump = False
        self.stepIndex = 0

    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.dino_rect = self.image.get_react()
        self.dino_react.x = X_POS
        self.dino_react.y = Y_POS
        self.step_index += 1

    def jump(self):
        pass

    def update(self):
        pass

    def draw(self):
        screen.blit