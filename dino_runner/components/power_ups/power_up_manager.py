import random
import pygame

from dino_runner.components.power_ups.moto import Moto, Life
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.life_ups = []
        self.when_appears = 110
        self.life_appears = 160
        self.life_show = ObstacleManager()
    
    def generate_power_up(self, score):
        if len(self.power_ups) == 0 and self.when_appears == score:
            self.when_appears += random.randint(200,300)
            self.power_ups.append(Moto())
            
    def life_power_up(self, score):
        if len(self.life_ups) == 0 and self.life_appears == score:
            self.life_appears += random.randint(150,200)
            self.life_ups.append(Life())
            
    def update(self, game):
        self.generate_power_up(game.score)
        player = game.player
        
        for power_up in self.power_ups:
            
            if player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                player.moto = True
                player.has_power_up = True
                player.type = power_up.type
                player.power_up_time_up = power_up.start_time + (power_up.duration * 1000)
                self.power_ups.remove(power_up)
            else:
                power_up.update(game.game_speed, self.power_ups)
        
        self.life_power_up(game.score)
        
        for life_up in self.life_ups:
            
            if player.dino_rect.colliderect(life_up.rect):
                player.life_up = True
                life_up.start_time = pygame.time.get_ticks()
                self.life_ups.remove(life_up)
            else:
                life_up.update(game.game_speed, self.life_ups)
    
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
            
        for life_up in self.life_ups:
            life_up.draw(screen)
    
    def reset_power_ups(self):
        self.power_ups.clear()
        self.life_ups.clear()
            
    
    