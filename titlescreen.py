import pygame
import math
from settings import *

class TitleScreen:
    def __init__(self, screen):
        self.screen = screen
        self.bg = pygame.image.load("Game/image/titlescreenbg3.png").convert()
        self.bg_width = self.bg.get_width()
        self.bg_rect = self.bg.get_rect()
        self.scroll = 0
        self.tiles = math.ceil(WIDTH / self.bg_width) + 1
        self.quit = False

        # Set up the font and title
        self.font = pygame.font.Font(TITLE_SCREEN_FONT, 88)  # You can adjust the size as needed
        self.title = self.font.render('Echoes of Valor', False, (255, 255, 255))  # White color
        self.title_rect = self.title.get_rect(center=(WIDTH/2, HEIGTH/4))

        # Set up the start and quit options
        self.option_font = pygame.font.Font(TITLE_SCREEN_FONT, 48)  # Adjust the size as needed
        self.start_option = self.option_font.render('Start', False, (255, 255, 255))  # White color
        self.start_option_rect = self.start_option.get_rect(center=(WIDTH/2, HEIGTH/2))
        self.quit_option = self.option_font.render('Quit', False, (255, 255, 255))  # White color
        self.quit_option_rect = self.quit_option.get_rect(center=(WIDTH/2, HEIGTH/2 + 100))

        # Set up the music
        pygame.mixer.music.load("Game\sound\Excision _ Kai Wachi - F.Y.U. [Official Visualizer].mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)  # Play the music indefinitely

    def draw_background(self):
        for i in range(0, self.tiles):
            self.screen.blit(self.bg, (i * self.bg_width + self.scroll, 0))
            self.bg_rect.x = i * self.bg_width + self.scroll
            #pygame.draw.rect(self.screen, (255, 0, 0), self.bg_rect, 1)

    def update(self):
        self.scroll -= 5
        if abs(self.scroll) > self.bg_width:
            self.scroll = 0

    def run(self):
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(FPS)
            self.draw_background()
            mouse_pos = pygame.mouse.get_pos()
            if self.start_option_rect.collidepoint(mouse_pos):
                self.start_option = self.option_font.render('Start', False, (24, 11, 11))  # Black color
            else:
                self.start_option = self.option_font.render('Start', False, (255, 255, 255))  # White color
            if self.quit_option_rect.collidepoint(mouse_pos):
                self.quit_option = self.option_font.render('Quit', False, (24, 11, 11))  # Black color
            else:
                self.quit_option = self.option_font.render('Quit', False, (255, 255, 255))  # White color
            self.screen.blit(self.title, self.title_rect)  # Draw the title
            self.screen.blit(self.start_option, self.start_option_rect)  # Draw the start option
            self.screen.blit(self.quit_option, self.quit_option_rect)  # Draw the quit option
            self.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    self.quit = True
                    pygame.mixer.music.stop()  # Stop the music when the title screen is exited
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_option_rect.collidepoint(mouse_pos):
                        run = False
                        pygame.mixer.music.stop()  # Stop the music when Start is clicked
                    elif self.quit_option_rect.collidepoint(mouse_pos):
                        run = False
                        self.quit = True
                        pygame.mixer.music.stop()  # Stop the music when Quit is clicked
            pygame.display.update()
