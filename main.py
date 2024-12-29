## Description: This file contains the main game loop and the start screen of the game.

import pygame
import sys
from settings import GROUND_LEVEL, SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND, FPS, level_width    
from player import Player
import random
from objects.managers import PlatformManager, LadderManager, ChestManager

# Initialize Pygame
pygame.init()

# Load assets
button_img = pygame.image.load("assets/images/button.png")
button_down_img = pygame.image.load("assets/images/buttondown.png")
dirt_img = pygame.image.load("assets/images/dirt.png")
cloud_img = pygame.image.load("assets/images/cloud.png")

# Scale the button images
BUTTON_WIDTH, BUTTON_HEIGHT = 400, 400
button_img = pygame.transform.scale(button_img, (BUTTON_WIDTH, BUTTON_HEIGHT))
button_down_img = pygame.transform.scale(button_down_img, (BUTTON_WIDTH, BUTTON_HEIGHT))

# Scale the dirt texture image
DIRT_WIDTH, DIRT_HEIGHT = 200, 100  
dirt_img = pygame.transform.scale(dirt_img, (DIRT_WIDTH, DIRT_HEIGHT))

# Scale the cloud image
CLOUD_WIDTH, CLOUD_HEIGHT = 200, 100  # Set desired width and height
cloud_img = pygame.transform.scale(cloud_img, (CLOUD_WIDTH, CLOUD_HEIGHT))

def draw_dirt(screen):
    """Draws the dirt texture repeatedly across the bottom of the screen."""
    for x in range(0, SCREEN_WIDTH, DIRT_WIDTH):
        screen.blit(dirt_img, (x, SCREEN_HEIGHT - DIRT_HEIGHT))

def start_screen(screen):
    """Displays the start screen with a clickable button."""

    button_rect = button_img.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    # Flash the button briefly
                    screen.blit(button_down_img, button_rect)
                    pygame.display.flip()
                    pygame.time.delay(200)  # 200ms delay for effect
                    return  # Start the game

        # Draw the button
        screen.fill(BACKGROUND)
        screen.blit(button_img, button_rect)
        pygame.display.flip()

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Platformer Game")
    clock = pygame.time.Clock()

    # Display start screen
    start_screen(screen)

    # Create player instance
    player = Player()

    # Cloud positions
    clouds = [
        [SCREEN_WIDTH, 100],
        [SCREEN_WIDTH + 200, 200],
        [SCREEN_WIDTH + 400, 150],
    ]
    cloud_speed = 1  # Adjust to control cloud movement speed

    # Create platforms (x, y, width, height)
    platform_manager = PlatformManager()
    platform_manager.generate_platforms(20, level_width, SCREEN_HEIGHT)

    ladder_manager = LadderManager()
    ladder_manager.place_ladders(platform_manager.platforms, GROUND_LEVEL)
    
    chest_manager = ChestManager()
    chest_manager.place_chests(platform_manager.platforms)

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



        # Update cloud positions
        for cloud in clouds:
            cloud[0] -= cloud_speed
            if cloud[0] < -CLOUD_WIDTH:  # Recycle cloud when it moves off-screen
                cloud[0] = SCREEN_WIDTH
                cloud[1] = random.randint(50, 200)  # Randomize height for variety


        # Draw background
        screen.fill(BACKGROUND)

        # Draw clouds
        for cloud in clouds:
            screen.blit(cloud_img, cloud)

        # Draw player
        player.draw(screen)

        # Draw Dirt
        screen.blit(dirt_img, (0, GROUND_LEVEL))  # Draw the dirt
        draw_dirt(screen)

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
