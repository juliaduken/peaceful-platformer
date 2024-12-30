## Description: This file contains the main game loop.

import pygame
import sys
import random

from background import BackgroundManager
from objects.managers import PlatformManager, LadderManager, ChestManager, EnemyManager
from player import Player
from screens import StartScreen, GameOverScreen
from settings import GROUND_LEVEL, SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND, FPS, GAME_TIME    

# Initialize Pygame
pygame.init()

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Peaceful Platformer")
    clock = pygame.time.Clock()

    # Display start screen & Initialize game over screen
    game_over_screen = GameOverScreen()
    start_screen = StartScreen()
    
    # Start the game loop
    running = True
    while running:
        start_screen.display(screen)  # Show the start screen
        
        # Create player instance
        player = Player()

        # Create platforms (x, y, width, height)
        platform_manager = PlatformManager()
        platform_manager.generate_platforms(20, SCREEN_HEIGHT)

        # Create ladders
        ladder_manager = LadderManager()
        ladder_manager.place_ladders(platform_manager.platforms, GROUND_LEVEL)
        
        # Create chests
        chest_manager = ChestManager()
        chest_manager.place_chests(platform_manager.platforms)

        # Create background manager
        background_manager = BackgroundManager()

        # Spawn enemies
        enemy_manager = EnemyManager()
        enemy_manager.generate_enemies(SCREEN_WIDTH, GROUND_LEVEL)

        start_ticks = pygame.time.get_ticks()  # Start time in milliseconds

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Check if 30 seconds have passed
            if pygame.time.get_ticks() - start_ticks >= GAME_TIME: 
                if game_over_screen.display(screen, player.score):  # Restart if True
                    break  # Exit the current loop to restart the game

            # Get current time
            current_time = pygame.time.get_ticks()
            # Update player
            player.update(platform_manager.platforms, ladder_manager.ladders, chest_manager.chests, enemy_manager.enemies, platform_manager.level_width)

            # Move platforms only when the level scrolls
            platform_manager.update(player.scroll_speed if player.rect.x >= 2 * SCREEN_WIDTH // 4 else 0)
            ladder_manager.update(player.scroll_speed if player.rect.x >= 2 * SCREEN_WIDTH // 4 else 0)
            chest_manager.update(player.scroll_speed if player.rect.x >= 2 * SCREEN_WIDTH // 4 else 0)
            enemy_manager.update(current_time, SCREEN_WIDTH, player.scroll_speed if player.rect.x >= 2 * SCREEN_WIDTH // 4 else 0, GROUND_LEVEL)
            background_manager.update_clouds()
            
            # Draw background
            background_manager.draw(screen)

            # Draw player
            
            # Draw platforms, ladders, and chests
            platform_manager.draw(screen)
            player.draw(screen)
            ladder_manager.draw(screen)
            chest_manager.draw(screen)

            # Draw enemies
            enemy_manager.draw(screen)

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
