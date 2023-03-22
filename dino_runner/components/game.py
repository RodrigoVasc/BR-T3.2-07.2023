import pygame

from dino_runner.utils.constants import BG, MBG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE, SOUND
from dino_runner.components.dino import Dino
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.soundtrack import Music

half_screen_heigth = SCREEN_HEIGHT // 2
half_screen_width = SCREEN_WIDTH // 2

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.scores = []
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.x_pos_cloud = 0
        self.y_pos_cloud = 35
        self.font = pygame.font.Font(FONT_STYLE, 22)
        self.score = 0
        self.death_count = 0

        
        self.player = Dino()
        self.obstacle_manager = ObstacleManager()

    def execute(self):
        self.executing = True
        while self.executing:
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()
        

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.reset_game()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def reset_game(self):
        self.obstacle_manager.reset_obstacles()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)

        self.obstacle_manager.update(self)  
        self.update_score()  
        
    def update_score(self):
        self.score += 1
    
        if self.score % 100 == 0:
            self.game_speed += 2

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((100, 150, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.draw_score()
        self.draw_scoreRank()
        self.draw_death()
        self.obstacle_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_score(self):
        self.textScore = self.font.render(f"Score: {self.score}", True, (0,0,0))
        textScore_rect = self.textScore.get_rect()
        textScore_rect.center = (1000, 15)
        self.screen.blit(self.textScore, textScore_rect)

    def draw_scoreRank(self):
        self.scores.append(self.score)
        self.textMax = self.font.render(f"Max score: {max(self.scores)}", True, (0,0,0))
        textMax_rect = self.textMax.get_rect()
        textMax_rect.center = (850, 15)
        self.screen.blit(self.textMax, textMax_rect)

    def draw_death(self):
        self.textDeath = self.font.render(f'Death: {self.death_count}',True, (0,0,0))
        textDeath_rect = self.textDeath.get_rect()
        textDeath_rect.center = (750, 50)

    def draw_background(self):
        self.screen.blit(MBG, (self.x_pos_bg, self.y_pos_bg))
        image_width = MBG.get_width()
        self.screen.blit(MBG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(MBG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

# ----------------------VERSÃO DO DINO--------------------------------------------
    #def draw_background(self):
    #    image_width = BG.get_width()
    #    self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
    #    self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
    #    if self.x_pos_bg <= -image_width:
    #        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
    #        self.x_pos_bg = 0
    #    self.x_pos_bg -= self.game_speed

    def render_text(self, message, x, y):
        text = self.font.render(message, True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text, text_rect)

    def show_menu(self):
        self.screen.fill((255,255,255))

        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
    
            self.render_text("Press (SPACE) to start playing", half_screen_width, half_screen_height)
            
        else:

            self.render_text("Press (SPACE) to new playing", half_screen_width, half_screen_height - 25)
            self.render_text("Press (ENTER) to continue playing", half_screen_width, half_screen_height + 25)
            self.render_text("Press (ESC) to exit game", half_screen_width, half_screen_height + 75)
            self.screen.blit(self.textScore, (half_screen_width - 450, half_screen_height - 250))
            self.screen.blit(self.textMax, (half_screen_width - 450, half_screen_height - 220))
            self.screen.blit(self.textDeath, (half_screen_width - 450, half_screen_height - 190))
            
        pygame.display.update()

        self.handle_events_on_menu()

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.executing = False
            elif event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_SPACE] and self.death_count == 0:
                    Music.play_music(self)
                    self.run()
                elif pygame.key.get_pressed()[pygame.K_RETURN] and self.death_count >= 1:
                    Music.play_music(self)
                    self.run()
                elif pygame.key.get_pressed()[pygame.K_SPACE] and self.death_count >= 1:
                    Music.play_music(self)
                    self.death_count = 0
                    self.game_speed = 20
                    self.score = 0
                    self.run()
                elif pygame.key.get_pressed()[pygame.K_ESCAPE] and self.death_count >= 1:
                    event.type = pygame.QUIT