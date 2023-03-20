import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD
class ObstacleManager():
    def __init__(self):
        self.obstacle = []
    
    def update(self, game):
        self.num = random.randint(0,2)
        if len (self.obstacle) == 0:
            if self.num == 0:
                self.obstacle.append(Cactus(SMALL_CACTUS, 325))
            if self.num == 1:
                self.obstacle.append(Cactus(LARGE_CACTUS, 300))
            if self.num == 2:
                self.obstacle.append(Bird(BIRD))
    
        for obstacle in self.obstacle:
            obstacle.update(game.game_speed, self.obstacle)
            if game.player.dino_rect.colliderect(obstacle.rect):    
                pygame.time.delay(500)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacle:
            obstacle.draw(screen)