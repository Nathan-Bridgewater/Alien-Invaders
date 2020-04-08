class GameStats:
    """Track statistics for Alien invasion"""

    def __init__(self, ai_game):
        """Initilise statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        """Initialise statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

