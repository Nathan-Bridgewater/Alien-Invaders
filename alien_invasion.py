import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overall class to manage game assest and behaviour."""

    def __init__(self):
        """Initialise the game, create game resources """
        pygame.init()
        # Create an instance of the settings class
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        self.ship = Ship(self)

        pygame.display.set_caption('Alien Invasion')

    def run_game(self):
        """Start main loop for the game"""
        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                # Redraw the screen during each pass through the loop.
                self.screen.fill(self.settings.bg_colour)
                self.ship.blitme()

                # Make the game the most recently drawn screen visible.
                pygame.display.flip()


if __name__ == '__main__':
    # Make game an instance and run the game.
    ai = AlienInvasion()
    ai.run_game()
