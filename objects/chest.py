import pygame
import os
from settings import ASSETS_PATH

class Chest:
    def __init__(self, platform, width, height):
        """
        Initializes a treasure chest with an image at the specified position.
        :param x: Horizontal position of the chest.
        :param y: Vertical position of the chest.
        :param width: Width of the chest (used for scaling the image).
        :param height: Height of the chest (used for scaling the image).
        """

        image_path = os.path.join(ASSETS_PATH, 'images/chest.png')
        open_image_path = os.path.join(ASSETS_PATH, 'images/chest_open.png')

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

    def draw(self, screen):
        """Draw the chest on the screen if it hasn't been collected."""
        if not self.collected:
            screen.blit(self.image, self.rect)
        else:
            screen.blit(self.open_image, self.rect)  # Show open chest if collected