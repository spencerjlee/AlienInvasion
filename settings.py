class Settings():
    """A Class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Game settings
        self.sideways_shooter = False

        #Ship settings
        self.ship_speed_factor = 2.5
        self.vertical_movements_permitted = False
        self.horizontal_movements_permitted = True

        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
