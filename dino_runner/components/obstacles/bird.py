import random
from dino_runner.components.obstacles.obstacle import Obstacle

class Bird(Obstacle):
    def __init__(self, images):
        self.type = 0
        super().__init__(images, self.type)
        self.rect.y = random.randint(400, 470)
        self.image = images
        self.contador = 0

    def draw(self, screen):
        if self.contador <= 5:
            screen.blit(self.image[0], (self.rect.x, self.rect.y))
        elif self.contador > 5:
            screen.blit(self.image[1], (self.rect.x, self.rect.y))
        if self.contador == 10:
            self.contador = 0
        self.contador += 1