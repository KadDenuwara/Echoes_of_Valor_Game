import pygame
from settings import *

class Transition:
    def __init__(self, screen):
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 0, HEIGTH)  # Start with a thin rectangle
        self.speed = 35  # Speed of transition

    def update(self):
        self.rect.width += self.speed  # Increase the width of the rectangle

    def draw(self):
        pygame.draw.rect(self.screen, (0, 0, 0), self.rect)  # Draw the rectangle

    def run(self):
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.update()
            self.draw()
            if self.rect.width >= WIDTH:  # If the rectangle has filled the screen
                run = False
            pygame.display.update()
