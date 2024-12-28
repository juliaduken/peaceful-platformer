# Description: This file contains game objects (e.g., platforms, ladders, treasure chests)
from settings import *
import pygame
import random

class Platform:
    def __init__(self, x, y, width, height, color=YELLOW):
        """
        Initializes a platform at the specified position with the given dimensions and color.
        :param x: Horizontal position of the platform.
        :param y: Vertical position of the platform.
        :param width: Width of the platform.
        :param height: Height of the platform.
        :param color: Color of the platform (default is yellow).
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.collision_rect = self.rect.inflate(0, -height * 0.1)  # Adjust collision area
        self.color = color

    def draw(self, screen):
        """
        Draws the platform on the screen.
        :param screen: Pygame screen surface.
        """
        pygame.draw.rect(screen, self.color, self.rect)

class PlatformManager:
    def __init__(self):
        """
        Initializes the PlatformManager to handle multiple platforms.
        """
        self.platforms = []
        self.ladders = []
        self.chests = []

    def generate_platforms(self, num_platforms, level_width, screen_height):
        """
        Generates platforms with specific spacing constraints:
        - The first platform is 150 pixels above the ground.
        - Subsequent platforms are spaced 50-150 pixels horizontally apart (including widths).
        - Platforms are no more than 100 pixels vertically apart.
        - Platforms over 160 pixels from the ground have a ladder. If the platform before it had a ladder,
          it will not have a ladder.
        - Platforms at over 160 pixels from the ground have a treasure chest, randomly picked for a maximum of 7 treasure chests.
        :param num_platforms: Number of platforms to generate.
        :param level_width: Total width of the level.
        :param screen_height: Height of the screen.
        """
        self.platforms = [] 
        self.ladders = []
        self.chests = []

        # Define ground level
        ground_level = screen_height - 50

        # Track last platform with a ladder
        last_ladder_platform = None
        

        # First platform: Fixed height, slightly above the ground
        x = random.randint(50, 200)  # Start near the left side
        y = ground_level - 150  # 150 pixels above the ground

        width = random.randint(100, 200)  # Platform width
        height = 20  # Platform height
        self.platforms.append(Platform(x, y, width, height))

        eligible_platforms = [] # List of platforms eligible for chest

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

            # Add to eligible platforms if above 160 pixels from the ground
            if ground_level - y > 160:
                eligible_platforms.append(platform)

            # Add a ladder if the platform is above 160 pixels from the ground & the last platform did not have a ladder.
            if y < ground_level - 160 and last_ladder_platform != last_platform:
                ladder_x = platform.rect.centerx - 10  # Center the ladder on the platform
                ladder_y = platform.rect.top  # Ladder reaches 100 pixels above the platform
                ladder_width = 20
                ladder_height = 100  # Total ladder height
                self.ladders.append(Ladder(ladder_x, ladder_y, ladder_width, ladder_height))
                last_ladder_platform = platform
        
        # Randomly select up to 7 platforms for treasure chests
        chest_platforms = random.sample(eligible_platforms, min(7, len(eligible_platforms)))
        for platform in chest_platforms:
            chest_width = 75
            chest_height = 75
            self.chests.append(Chest(platform, chest_width, chest_height))



    def update_platforms(self, scroll_x):
        """
        Updates platform positions based on player's movement for scrolling.
        Locks in ladders and chests to the platforms.
        :param scroll_x: Player's scrolling offset.
        """
        for platform in self.platforms:
            platform.rect.x -= scroll_x 
        
        for ladder in self.ladders:
            ladder.rect.x -= scroll_x

        for chest in self.chests:
            chest.rect.x -= scroll_x

    def draw_platforms(self, screen):
        """
        Draws all platforms managed by the PlatformManager.
        :param screen: Pygame screen surface.
        """
        for platform in self.platforms:
            platform.draw(screen)

class Ladder:
    def __init__(self, x, y, width, height, image_path="assets/images/ladder.png"):  # Brown color for the ladder
        """
        Initializes a ladder at the specified position with the given dimensions and color.
        :param x: Horizontal position of the ladder.
        :param y: Vertical position of the ladder.
        :param width: Width of the ladder.
        :param height: Height of the ladder.
        :param color: Color of the ladder (default is brown).
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load(image_path)  # Load the ladder image
        self.image = pygame.transform.scale(self.image, (width, height))  # Scale the image to fit the ladder size

    def draw(self, screen):
        """
        Draws the ladder on the screen.
        :param screen: Pygame screen surface.
        """
        screen.blit(self.image, self.rect)

class Chest:
    def __init__(self, platform, width, height, image_path="assets\images\chest.png", open_image_path="assets\images\chest_open.png"):
        """
        Initializes a treasure chest with an image at the specified position.
        :param x: Horizontal position of the chest.
        :param y: Vertical position of the chest.
        :param width: Width of the chest (used for scaling the image).
        :param height: Height of the chest (used for scaling the image).
        :param image_path: Path to the chest image.
        :param open_image_path: Path to the opened chest image.
        """
        self.platform = platform
        self.rect = pygame.Rect(
            platform.rect.centerx - (width // 2), platform.rect.top - height, 
            width, 
            height
        )
        self.image = pygame.image.load(image_path)  # Load chest image
        self.open_image = pygame.image.load(open_image_path)  # Load opened chest image
        self.image = pygame.transform.scale(self.image, (width, height))  # Scale chest
        self.open_image = pygame.transform.scale(self.open_image, (width, height))  # Scale open chest
        self.collected = False  # Track if the chest has been opened


    def update_position(self):
        """Updates the chest's position to match its platform."""
        self.rect.x = self.platform.rect.centerx - (self.rect.width // 2)
        self.rect.y = self.platform.rect.top - self.rect.height

    def draw(self, screen):
        """Draw the chest on the screen if it hasn't been collected."""
        if not self.collected:
            screen.blit(self.image, self.rect)
        else:
            screen.blit(self.open_image, self.rect)  # Show open chest if collected