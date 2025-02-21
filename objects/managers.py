import random
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, GROUND_LEVEL
from objects.platform import Platform
from objects.ladder import Ladder
from objects.chest import Chest
from objects.enemy import Enemy

class PlatformManager:
    """
    Generates platforms with specific spacing constraints:
        - The first platform is no more than 150 pixels above the ground.
        - Subsequent platforms are spaced 50-150 pixels horizontally apart (including widths).
        - Platforms are no more than 100 pixels vertically apart.
    """
    def __init__(self):
        """
        Initializes the PlatformManager to handle multiple platforms and determine level width.
        """
        self.platforms = []
        self.level_width = 0 
    
    def generate_platforms(self, num_platforms, screen_height):
        """
        Generates platforms and calculates the level width based on the rightmost platform.
        """
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
        
        # Update level width based on the rightmost platform
        self.level_width = self.platforms[-1].rect.right
        print(f"Level width: {self.level_width}")
    
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
        chest_platforms = random.sample(eligible_platforms, min(7, len(eligible_platforms)))
        
        for platform in chest_platforms:
            self.chests.append(Chest(platform, 75, 75))
    
    def update(self, scroll_x):
        for chest in self.chests:
            chest.rect.x -= scroll_x
    
    def draw(self, screen):
        for chest in self.chests:
            chest.draw(screen)

class EnemyManager:
    """
    Handles the generation, updating, and rendering of enemies in the game.
    """
    def __init__(self):
        """
        Initializes the EnemyManager to manage a list of enemies and control spawn timing.
        """
        self.enemies = []
        self.last_spawn_time = 0  # Time when the last enemy was spawned

    def generate_enemies(self, screen_width, ground_level):
        """
        Generates a single enemy at a random position on the screen.
        :param screen_width: Width of the game screen.
        :param ground_level: Y-coordinate of the ground.
        """
        x = screen_width + 50  # Spawn just off the right edge of the screen
        y = ground_level - 50  # Ground level
        self.enemies.append(Enemy(x, y))
        print(f"Generated Enemy at ({x}, {y})")  # Debug

    def update(self, current_time, screen_width, scroll_x, ground_level):
        """
        Updates the positions and behavior of all enemies and spawns new ones every 10 seconds.
        :param current_time: Current game time in milliseconds.
        :param screen_width: Width of the screen (used for spawning).
        :param scroll_x: Horizontal scrolling value to move enemies.
        :param ground_level: Y-coordinate of the ground.
        """
        # Spawn a new enemy every 10 seconds
        if current_time - self.last_spawn_time > 10000:  # 10 seconds = 10000 ms
            self.generate_enemies(screen_width, ground_level)
            self.last_spawn_time = current_time  # Reset spawn time

        # Update all enemies
        for enemy in self.enemies[:]:
            enemy.update(scroll_x, ground_level)

            # Remove enemies that move off-screen
            if enemy.rect.right < 0:
                self.enemies.remove(enemy)

    def draw(self, screen):
        """
        Draws all enemies on the screen.
        :param screen: Pygame screen surface.
        """
        for enemy in self.enemies:
            enemy.draw(screen)
