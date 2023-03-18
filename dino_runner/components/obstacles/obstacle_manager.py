import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS

class ObstacleManager():
    def __init__(self,obstacle, position):
        self.obstacle = []
        self.position = self.rect.y
        
    def update(self, game):
        self.num = random.randint(0,1)
        if len (self.obstacle) == 0:
            if self.num == 0:
                self.obstacle.append(Cactus(SMALL_CACTUS, 325))
            if self.num == 1:
                self.obstacle.append(Cactus(LARGE_CACTUS, 300))





        for obstacle in self.obstacle:
            obstacle.update(game.game_speed, self.obstacle)
            if game.player.dino_rect.colliderect(obstacle.rect):    
                pygame.time.delay(500)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacle:
            obstacle.draw(screen)