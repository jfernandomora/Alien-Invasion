class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        #Screen settings
        self.screen_width = 1200
        self.screen_heigh = 800
        self.bg_color = (135, 206, 235)

        #Ship settings
        self.ship_speed_factor = 1.5