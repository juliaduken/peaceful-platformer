import pygame
from settings import YELLOW

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