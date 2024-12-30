# Description: Defines enemy behavior and movement.

import pygame
import os
from settings import ASSETS_PATH

class Enemy:
    def __init__(self, start_x, start_y):
        self.rect = pygame.Rect(start_x, start_y, 20, 20)
        self.speed = 2  # Enemy's speed
        self.gravity = 1  # Gravity effect
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_PATH, 'images/enemy.png')), (50, 50))

    def update(self, scroll_x, ground_level):
        # Move left
        self.rect.x -= self.speed + scroll_x
    def check_collision(self, enemies):
                # Check collisions with enemies
        for enemy in enemies:
            if self.rect.colliderect(enemy.rect):
                print("Player hit by enemy!")  # Replace with damage logic or game over logic

    def draw(self, screen):
        screen.blit(self.image, self.rect)
