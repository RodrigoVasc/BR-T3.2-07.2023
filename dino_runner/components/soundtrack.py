import random
import pygame

from dino_runner.utils.constants import SOUND

class Music:
    def __init__(self):
        pygame.mixer.init()

    def play_music(self):
        self.musics = random.choice(SOUND)
        pygame.mixer.music.load(self.musics)
        pygame.mixer.music.set_volume(0.25)
        pygame.mixer.music.play(-1)

    def play_sound(self, sound, volume):
        self.sons = pygame.mixer.Sound(sound)
        self.sons.set_volume(volume)
        self.sons.play()
        