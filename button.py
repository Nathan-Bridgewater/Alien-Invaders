import pygame.font


class Button:
    """Initialise button attributes"""

    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        screen_rect = self.screen.get_rect()

        # Set the dimensions and poperties of the button
        self.width, self.height = 200, 50
        self.button_colour = (0, 255, 0)
        self.text_colour = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the buttons rect and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = screen_rect.center

        # Button message only needs to be prepped once
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn a message into a rendered imagine and center text on button"""
        self.msg_image = self.font.render(msg, True, self.text_colour,
                                          self.button_colour)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_colour, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)