import pygame

class Ladder:
    def __init__(self, x, y, width, height, image_path="../assets/images/ladder.png"):  # Brown color for the ladder
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