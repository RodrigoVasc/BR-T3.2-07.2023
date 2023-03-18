import random
from dino_runner.components.obstacles import Obstacle

class Cactus(Obstacle):
    def __init__(self, images):
        self.type = random.randint(0,2)
        super()._init__(images, self.type)  
        self.rect.y = 325
