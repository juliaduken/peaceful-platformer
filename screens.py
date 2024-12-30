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
                        return # Exit start screen

            # Draw the start screen
            screen.fill(BACKGROUND)
            screen.blit(self.button_img, button_rect)
            pygame.display.flip()

class GameOverScreen:
    def __init__(self):
        self.font = pygame.font.Font(None, 72)  # Use a Pygame font
        self.button_img = pygame.image.load("assets/images/restart.png")
        self.button_img = pygame.transform.scale(self.button_img, (600, 300))

    def display(self, screen, score):
        button_rect = self.button_img.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
        score_text = self.font.render(f"Your Score: {score}", True, (255, 255, 255))  # White text

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_rect.collidepoint(event.pos):
                        return True # Restart the game or exit

            screen.fill(BACKGROUND)
            screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 3))
            screen.blit(self.button_img, button_rect)
            pygame.display.flip()
