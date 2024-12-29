import random
from objects.platform import Platform
from objects.ladder import Ladder
from objects.chest import Chest

class PlatformManager:
    """
    Generates platforms with specific spacing constraints:
        - The first platform is no more than 150 pixels above the ground.
        - Subsequent platforms are spaced 50-150 pixels horizontally apart (including widths).
        - Platforms are no more than 100 pixels vertically apart.
    """
    def __init__(self):
        """
        Initializes the PlatformManager to handle multiple platforms.
        """
        self.platforms = []
    
    def generate_platforms(self, num_platforms, level_width, screen_height):
        # Define ground level
        ground_level = screen_height - 50

        # First platform: Fixed height, slightly above the ground
        x = random.randint(50, 200)  # Start near the left side
        y = ground_level - 150  # 150 pixels above the ground

        width = random.randint(100, 200)  # Platform width
        height = 20  # Platform height

        self.platforms.append(Platform(x, y, width, height))

        # Generate subsequent platforms
        for i in range(num_platforms - 1):
            # Get the last platform's position and size
            last_platform = self.platforms[-1]
            last_x_end = last_platform.rect.right  # Right edge of the last platform
            last_y = last_platform.rect.y

            # Calculate new platform position
            x = last_x_end + random.randint(50, 150)  # 50-150 pixels horizontally apart
            y = last_y + random.randint(-75, 75)  # No more than 100 pixels vertically apart

            # Clamp the vertical position to screen bounds
            y = max(50, min(y, screen_height - 150))

            # Create and add the platform
            width = random.randint(100, 200)
            platform = Platform(x, y, width, height)
            self.platforms.append(platform)
    
    def update(self, scroll_x):
        """
        Updates platform positions based on player's movement for scrolling.
        :param scroll_x: Horizontal scroll amount.
        """
        for platform in self.platforms:
            platform.rect.x -= scroll_x

    def draw(self, screen):
        """
        Draws all platforms managed by the PlatformManager.
        :param screen: Pygame screen surface.
        """
        for platform in self.platforms:
            platform.draw(screen)

class LadderManager:
    """
    Platforms over 160 pixels from the ground have a ladder. 
    If the platform before it had a ladder, it will not have a ladder.
    """
    def __init__(self):
        """
        Initializes the LadderManager to add multiple ladders to platforms.

        """
        self.ladders = []
    
    def place_ladders(self, platforms, ground_level):
        last_had_ladder = False # Track last platform with a ladder

        for platform in platforms:
            if ground_level - platform.rect.top > 160:
                if not last_had_ladder:
                    ladder_x = platform.rect.centerx - 10
                    ladder_y = platform.rect.top
                    self.ladders.append(Ladder(ladder_x, ladder_y, 20, 100))
                    last_had_ladder = True
                else:
                    last_had_ladder = False

    def update(self, scroll_x):
        for ladder in self.ladders:
            ladder.rect.x -= scroll_x

    def draw(self, screen):
        for ladder in self.ladders:
            ladder.draw(screen)

class ChestManager:
    def __init__(self):
        self.chests = []

    def place_chests(self, platforms):
        eligible_platforms = [p for p in platforms if p.rect.bottom > 160] 
        print(eligible_platforms)
        chest_platforms = random.sample(eligible_platforms, min(7, len(eligible_platforms)))
        
        for platform in chest_platforms:
            self.chests.append(Chest(platform, 75, 75))
    
    def update(self, scroll_x):
        for chest in self.chests:
            chest.rect.x -= scroll_x
    
    def draw(self, screen):
        for chest in self.chests:
            chest.draw(screen)