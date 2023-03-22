from dino_runner.components.obstacles.obstacle import Obstacle

class Small_robo(Obstacle):
    def __init__(self, images, position_y):
        self.type = 0
        super().__init__(images, self.type)
        self.rect.y = position_y
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

class Larg_robo(Obstacle):
    def __init__(self, images, position_y):
        self.type = 0
        super().__init__(images, self.type)
        self.rect.y = position_y
        self.image = images
        self.contador = 0

    def draw(self, screen):
        if self.contador <= 5:
            screen.blit(self.image[0], (self.rect.x, self.rect.y))
        elif self.contador > 5:
            screen.blit(self.image[1], (self.rect.x, self.rect.y))
        elif self.contador > 10:
            screen.blit(self.image[2], (self.rect.x, self.rect.y))
        if self.contador == 15:
            self.contador = 0
        self.contador += 1