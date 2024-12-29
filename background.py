# Description: This file manages the art for the background (dirt, clouds, etc.)
import pygame
import random
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND, GROUND_LEVEL

class BackgroundManager:
    def __init__(self):
        # Load and scale assets
        # Dirt
        self.dirt_img = pygame.image.load("assets/images/dirt.png")
        self.dirt_img = pygame.transform.scale(self.dirt_img, (200, 100))
        # Dimensions
        self.DIRT_WIDTH = 200
        self.DIRT_HEIGHT = 100

        # Cloud
        self.cloud_img = pygame.image.load("assets/images/cloud.png")
        self.cloud_img = pygame.transform.scale(self.cloud_img, (200, 100))
        # Settings
        self.clouds = [
            [SCREEN_WIDTH, 100],
            [SCREEN_WIDTH + 200, 200],
            [SCREEN_WIDTH + 400, 150],
        ]
        self.cloud_speed = 1  # Control cloud movement speed

    def update_clouds(self):
        """Update cloud positions, recycling them when off-screen."""
        for cloud in self.clouds:
            cloud[0] -= self.cloud_speed
            if cloud[0] < -self.cloud_img.get_width():  # Recycle off-screen clouds
                cloud[0] = SCREEN_WIDTH
                cloud[1] = random.randint(50, 200)  # Randomize height for variety

    def draw(self, screen):
        """Draw the background elements: solid color, dirt, and clouds."""
        # Fill background color
        screen.fill(BACKGROUND)

        # Draw clouds
        for cloud in self.clouds:
            screen.blit(self.cloud_img, cloud)

        # Draw dirt
        self.draw_dirt(screen)

    def draw_dirt(self, screen):
        """Draw the dirt texture repeatedly across the bottom of the screen."""
        for x in range(0, SCREEN_WIDTH, self.DIRT_WIDTH):
            screen.blit(self.dirt_img, (x, SCREEN_HEIGHT - self.DIRT_HEIGHT))