class Settings():
    #A Class to Store All Settings for Alien Armageddon

    def __init__(self):
        #Initialize the Settings of the Game
        #Screen Settings
        self.screen_width = 1280
        self.screen_height = 600
        self.bg_color = (0, 25, 51)

        #Ship Settings
        self.ship_speed_factor = 1.5

        #Bullet Settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 250, 100, 0
        self.bullets_allowed = 5