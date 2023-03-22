import random
from dino_runner.components.obstacles.obstacle import Obstacle

class Cloud(Obstacle):
       def __init__(self, images):
        self.type = 0
        super().__init__(images, self.type)
        self.rect.y = random.randint(100, 200)
        