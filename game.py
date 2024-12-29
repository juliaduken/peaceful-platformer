## Description: This file contains the main game loop.

import pygame
import sys
import random
from background import BackgroundManager
from objects.managers import PlatformManager, LadderManager, ChestManager
from player import Player
from screens import StartScreen
from settings import GROUND_LEVEL, SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND, FPS, level_width    

# Initialize Pygame
pygame.init()

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Peaceful Platformer")
    clock = pygame.time.Clock()

    # Display start screen
    start_screen = StartScreen()
    start_screen.display(screen)

    # Create player instance
    player = Player()

    # Create platforms (x, y, width, height)
    platform_manager = PlatformManager()
    platform_manager.generate_platforms(20, level_width, SCREEN_HEIGHT)

    # Create ladders
    ladder_manager = LadderManager()
    ladder_manager.place_ladders(platform_manager.platforms, GROUND_LEVEL)
    
    # Create chests
    chest_manager = ChestManager()
    chest_manager.place_chests(platform_manager.platforms)

    # Create background manager
    background_manager = BackgroundManager()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update player
        player.update(platform_manager.platforms, ladder_manager.ladders, chest_manager.chests, level_width)

        # Move platforms only when the level scrolls
        platform_manager.update(player.scroll_speed if player.rect.x >= 2 * SCREEN_WIDTH // 4 else 0)
        ladder_manager.update(player.scroll_speed if player.rect.x >= 2 * SCREEN_WIDTH // 4 else 0)
        chest_manager.update(player.scroll_speed if player.rect.x >= 2 * SCREEN_WIDTH // 4 else 0)
        background_manager.update_clouds()

        # Draw background
        background_manager.draw(screen)

        # Draw player
        player.draw(screen)

        # Draw platforms, ladders, and chests
        platform_manager.draw(screen)
        ladder_manager.draw(screen)
        chest_manager.draw(screen)

        # Render the score
        font = pygame.font.Font(None, 36)  # Use a Pygame font
        score_text = font.render(f"Score: {player.score}", True, (255, 255, 255))  # White text
        screen.blit(score_text, (10, 10))  # Draw score in the top-left corner

        pygame.display.flip()

        # Limit frames per second
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
