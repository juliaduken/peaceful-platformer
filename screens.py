# Description: This file contains the logic for different screens (start, game over)
import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND

class StartScreen:
    def __init__(self):
        """Initialize the start screen with assets and layout."""
        # Load and scale button assets
        self.button_img = pygame.image.load("assets/images/button.png")
        self.button_down_img = pygame.image.load("assets/images/buttondown.png")
        self.button_img = pygame.transform.scale(self.button_img, (400, 400))
        self.button_down_img = pygame.transform.scale(self.button_down_img, (400, 400))

    def display(self, screen):
        """Displays the start screen with a clickable button."""
        button_rect = self.button_img.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_rect.collidepoint(event.pos):
                        # Flash the button briefly
                        screen.blit(self.button_down_img, button_rect)
                        pygame.display.flip()
                        pygame.time.delay(200)  # 200ms delay for effect
                        return  # Exit the start screen

            # Draw the start screen
            screen.fill(BACKGROUND)
            screen.blit(self.button_img, button_rect)
            pygame.display.flip()
