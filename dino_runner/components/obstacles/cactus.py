import random
from dino_runner.components.obstacles.obstacle import Obstacle

class Cactus(Obstacle):
    def __init__(self, images, position_y):
        self.type = random.randint(0,2)
        super().__init__(images, self.type)  

        self.rect.y = position_y