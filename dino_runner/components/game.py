import pygame

from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.utils.constants import MBG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE, DEFAULT_TYPE, GAME_SPEED, MENU, GAME_OVER
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
        self.game_speed = GAME_SPEED
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.x_pos_cloud = 0
        self.y_pos_cloud = 35
        self.timer_duration = 11000
        self.timer_start_time = None
        self.font = pygame.font.Font(FONT_STYLE, 22)
        self.score = 0
        self.death_count = 0
        self.power_up = PowerUpManager()
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
        self.playing = True
        self.reset_game()
        self.player.reset_dino_position()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def reset_game(self):
        self.obstacle_manager.reset_obstacles()
        self.power_up.reset_power_ups()
        self.obstacle_manager.life = 100
        

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                pygame.display.quit()
                pygame.quit()

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)  
        self.update_score()
        self.power_up.update(self)
        self.life_points()
        if self.death_count > 0 and self.timer_start_time is None:
            self.timer_start_time = pygame.time.get_ticks()

    def update_score(self):
        self.score += 1
    
        if self.score % 100 == 0:
            self.game_speed += 2
    
    def life_points(self):
        self.mostrar_life = self.font.render(f"Life: {self.obstacle_manager.life} / 100", True, (200, 50, 50))
        self.screen.blit(self.mostrar_life, (50, 50))
        if self.obstacle_manager.life > 100:
            self.obstacle_manager.life = 100
    
    def life_up(self):
        if self.player.life_up:
            self.obstacle_manager.life += 10
            self.player.life_up = False

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((100, 150, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.draw_score()
        self.draw_scoreRank()
        self.draw_death()
        self.draw_power_up_time()
        self.life_points()
        self.life_up()
        self.obstacle_manager.draw(self.screen)
        self.power_up.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time_up - pygame.time.get_ticks())/1000, 2)
            if time_to_show >=0:
                font = pygame.font.Font(FONT_STYLE, 22)
                text = font.render(f"Power Up: {time_to_show}", True, (40,50,100))
                text_rect = text.get_rect()
                text_rect.x = 425
                text_rect.y = 100
                self.screen.blit(text, text_rect)
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE
        
    def draw_score(self):
        self.textScore = self.font.render(f"Score: {self.score}", True, (100,150,255))
        textScore_rect = self.textScore.get_rect()
        textScore_rect.center = (1000, 15)
        self.screen.blit(self.textScore, textScore_rect)

    def draw_scoreRank(self):
        self.scores.append(self.score)
        self.textMax = self.font.render(f"Max score: {max(self.scores)}", True, (100,150,255))
        textMax_rect = self.textMax.get_rect()
        textMax_rect.center = (850, 15)
        self.screen.blit(self.textMax, textMax_rect)

    def draw_death(self):
        self.textDeath = self.font.render(f'Death: {self.death_count}',True, (100,150,255))
        textDeath_rect = self.textDeath.get_rect()
        textDeath_rect.center = (750, 50)

    def continue_timer(self):
            if self.timer_start_time is not None:
                elapsed_time = pygame.time.get_ticks() - self.timer_start_time
                remaining_time = max(self.timer_duration - elapsed_time, 0) // 1000
                self.textTimer = self.font.render(f"Continue? {remaining_time} ", True, (100,150,255))
                textTimer_rect = self.textTimer.get_rect()
                textTimer_rect.center = (555, 350)
                self.screen.blit(self.textTimer, textTimer_rect)
            if remaining_time == 0:
                pygame.display.QUIT()
    
    def draw_background(self):
        self.screen.blit(MBG, (self.x_pos_bg, self.y_pos_bg))
        image_width = MBG.get_width()
        self.screen.blit(MBG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(MBG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
        
    def render_text(self, message, x, y):
        text = self.font.render(message, True, (100,150,255))
        text_rect = text.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text, text_rect)

    def show_overMenu(self):
        self.screen.blit(GAME_OVER, (450, 15))

    def show_mainMenu(self):
        self.screen.blit(MENU, (self.x_pos_bg, self.y_pos_bg))
        
    def show_menu(self):
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            self.show_mainMenu()
            self.render_text("Press (SPACE) to start playing", half_screen_width - 10, half_screen_height + 100)
            self.render_text("Press (ESC) to exit game", half_screen_width-10, half_screen_height + 150)
        if self.death_count >=1:
            self.screen.fill((0,0,0))
            self.show_overMenu()
            self.render_text("Creditos: Rodrigo Vasco Luna Moraes", half_screen_width - 325, half_screen_height + 275)
            self.render_text("Press (SPACE) to new playing", half_screen_width, half_screen_height + 100)
            self.render_text("Press (ENTER) to continue playing", half_screen_width, half_screen_height + 150)
            self.render_text("Press (ESC) to exit game", half_screen_width, half_screen_height + 200)
            self.screen.blit(self.textScore, (half_screen_width - 450, half_screen_height - 250))
            self.screen.blit(self.textMax, (half_screen_width - 450, half_screen_height - 220))
            self.screen.blit(self.textDeath, (half_screen_width - 450, half_screen_height - 190))
            self.continue_timer()
         
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
              
                elif pygame.key.get_pressed()[pygame.K_ESCAPE] and self.death_count >=0:
                    event.type = pygame.QUIT
