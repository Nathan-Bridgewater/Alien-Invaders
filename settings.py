class Settings:
    """A class to store all of the settings."""

    def __init__(self):
        """Initialise the games settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_colour = (60, 60, 60)
        self.bullets_allowed = 5

        # Alien settings
        self.fleet_drop_speed = 10


        # How quickly the game speeds up
        self.speedup_scale = 1.1
        self.score_scale = 1.5

    def initialise_dynamic_settings(self):
        """Initialise settings that change through the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        # fleet direction of 1 represents right; -1 is left
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        """Increase the speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points*self.score_scale)
        print(self.alien_points)
