import pygame, sys
from settings import *
from level import Level
from titlescreen import TitleScreen
from transition import Transition

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()  # Initialize the mixer module
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption("Echoes of Valor")
        self.logo = pygame.image.load("Game/logo/Logo.png").convert_alpha()
        pygame.display.set_icon(self.logo)
        self.clock = pygame.time.Clock()
        self.level = Level()

        #sound
        self.main_sound = pygame.mixer.Sound("Game/sound/Excision x Downlink - Crowd Control (Delta Heavy Remix).mp3")
        self.main_sound.set_volume(0.5)

    def run(self):
        self.main_sound.play(loops = -1)  # Play the game music
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                #upgrade
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        self.level.toggle_menu()

            self.screen.fill(WATER_COLOR)
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    #Title Screen
    title_screen = TitleScreen(game.screen)
    title_screen.run()
    if not title_screen.quit:
        # Transition
        transition = Transition(game.screen)
        transition.run()
        # Start the game after the transition
        game.run()
    else:
        # Transition
        transition = Transition(game.screen)
        transition.run()
        pygame.quit()
        sys.exit()
