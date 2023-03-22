import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cloud import Cloud
from dino_runner.components.obstacles.robo import Small_robo, Larg_robo
from dino_runner.components.soundtrack import Music
from dino_runner.utils.constants import SMALL_ROBOT,LARGE_ROBOT_GREEN, LARGE_ROBOT_RED ,MEGA_BIRD, MEGA_VESPA, MEGA_ROBOT_FLYR,MEGA_ROBOT_FLYG, MEGA_ROBOT_FLY, CLOUD , DEATH_SOUND

class ObstacleManager():
    def __init__(self):
        self.obstacle = []
        self.cloud = []
        self.robotFly_choice = [MEGA_VESPA, MEGA_BIRD, MEGA_ROBOT_FLYR, MEGA_ROBOT_FLYG, MEGA_ROBOT_FLY]
        self.robot_choice = [LARGE_ROBOT_RED, LARGE_ROBOT_GREEN]

    def update(self, game):
        self.num = random.randint(0,2)

        if len (self.cloud) == 0:
            self.cloud.append(Cloud(CLOUD)) 

        if len (self.obstacle) == 0:
            if self.num == 0:
                self.obstacle.append(Small_robo(SMALL_ROBOT, 480))
        
            if self.num == 1:
                self.obstacle.append(Larg_robo(random.choice(self.robot_choice), 460))
                
            if self.num == 2:
                self.obstacle.append(Small_robo(random.choice(self.robotFly_choice),random.randint(300, 450)))
        
        
        for obstacle in self.obstacle:
            obstacle.update(game.game_speed, self.obstacle)
            if game.player.dino_rect.colliderect(obstacle.rect):
                
                if not game.player.has_power_up:
                    
                    Music.play_sound(self, DEATH_SOUND, 0.1)
                    pygame.mixer.music.stop()
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    break
                else:
                    self.obstacle.remove(obstacle)
        
        for cloud in self.cloud:
            cloud.update(game.game_speed, self.cloud)

            
    def draw(self, screen):
        for obstacle in self.obstacle:
            obstacle.draw(screen)

        for cloud in self.cloud:
            cloud.draw(screen)

    def reset_obstacles(self):
        self.obstacle.clear()
        self.cloud.clear()