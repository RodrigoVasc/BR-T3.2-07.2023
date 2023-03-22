import pygame

from dino_runner.utils.constants import MEGA_RUN, MEGA_DUCK, MEGA_JUMP, JUMP_SOUND,DEFAULT_TYPE, MOTO_TYPE, MOTO_RUN, MOTO_JUMP, MOTO_DUCK
from dino_runner.components.soundtrack import Music

DUCK_IMG = {DEFAULT_TYPE: MEGA_DUCK, MOTO_TYPE: MOTO_DUCK}
JUMP_IMG = {DEFAULT_TYPE: MEGA_JUMP, MOTO_TYPE: MOTO_JUMP}
RUN_IMG = {DEFAULT_TYPE: MEGA_RUN, MOTO_TYPE: MOTO_RUN}

X_POS = 80
Y_POS = 480
JUMP_VEL = 8.5

class Dino:
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False
        self.step_index = 0
        self.jump_vel = JUMP_VEL
        self.has_power_up = False
        
    def run(self):
        if self.step_index < 5:
            self.image = RUN_IMG[self.type][0]
        elif self.step_index > 10:
            self.image = RUN_IMG[self.type][1]
        elif self.step_index > 15: 
            self.image = RUN_IMG[self.type][2]
            
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index+=1

        if self.step_index > 20:
          self.step_index = 0

    def jump(self):
        self.image = JUMP_IMG[self.type]
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel*4
            self.jump_vel -=0.8
        
        if self.jump_vel < -JUMP_VEL:
            self.dino_jump = False
            self.dino_rect.y = Y_POS
            self.jump_vel = JUMP_VEL

    def duck(self):
        self.image = DUCK_IMG[self.type]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = 485
        self.dino_duck = False

    def update(self, user_input):
        
        if (user_input[pygame.K_UP] or user_input[pygame.K_SPACE] or user_input[pygame.K_w]) and not self.dino_jump:
            Music.play_sound(self, JUMP_SOUND, 0.1)
            self.dino_jump = True
            self.dino_run = False
        elif (user_input[pygame.K_DOWN] or user_input[pygame.K_s]) and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            
        elif user_input[pygame.K_RIGHT]:
            if self.dino_rect.x < 1100:
                self.dino_rect.x += 5 
            else:
                self.dino_rect.x = 1098
        elif user_input[pygame.K_LEFT]:
            if self.dino_rect.x > 0:

                self.dino_rect.x -= 5
            else:
                self.dino_rect.x = 2            
            
        elif not self.dino_jump and not self.dino_duck:
            self.dino_run = True
        
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x,self.dino_rect.y))