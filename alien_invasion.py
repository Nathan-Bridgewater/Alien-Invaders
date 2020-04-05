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
        # Create an instance of a screen object using the attributes defined
        # in the 'Settings' class and the set_mode function from pygame
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        # Create an instance of ship, using the current game instance as
        # The argument
        self.ship = Ship(self)

        pygame.display.set_caption('Alien Invasion')

    def run_game(self):
        """Start main loop for the game"""
        while True:
            # Helper methods are not called from an instance
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """Respond to keyboard and mouse."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """Update images on the screen and flip to the new screen"""
        self.screen.fill(self.settings.bg_colour)
        self.ship.blitme()
        # Make the game the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # Make game an instance and run the game.
    ai = AlienInvasion()
    ai.run_game()
