## Description: Defines player behavior and button clicks.

import pygame
from settings import *


class Player:
    def __init__(self):
        # Score
        self.score = 0
        # Movement attributes
        self.vel_x = 0
        self.vel_y = 0
        self.is_jumping = False
        self.is_falling = False
        self.on_platform = False
        self.is_dropping = False
        self.jump_animation_timer = 0
        self.scroll_x = 0 # Track horizontal scrolling
        self.scroll_speed = 3 # Speed of scrolling
        self.scroll_offset = 0

        # Load images of player
        self.image_idle = pygame.image.load("assets/images/fairy.png")
        self.image_jump = pygame.image.load("assets/images/fairy_jump.png")
        
        # Ensure the images are the same size
        self.image_idle = pygame.transform.scale(self.image_idle, (100,100))
        self.image_jump = pygame.transform.scale(self.image_jump, (100,100))
 
        # Start with the idle image
        self.image = self.image_idle 
        self.rect = self.image.get_rect(midbottom=(SCREEN_WIDTH // 2, GROUND_LEVEL)) # Position image
        

    def check_platform_collisions(self, platforms):
        """
        Checks if the player's horizontal midpoint aligns with a platform's bounds and ensures
        the player snaps to the highest valid platform.
        :param platforms: List of Platform objects.
        """

        for platform in platforms:
            # Ignore platform collisions if dropping
            if self.is_dropping:
                continue
            
            # Horizontal midpoint of the player
            player_mid_x = self.rect.centerx

            # Horizontal condition: Player's midpoint must be over the platform
            is_midpoint_on_platform = platform.rect.left <= player_mid_x <= platform.rect.right

            # Vertical condition: Player's bottom is near the platform's top while falling
            is_falling_onto_platform = (
                self.rect.bottom >= platform.rect.top - 30 and  # Fairy's bottom reaches the platform
                self.rect.bottom <= platform.rect.top + 50 and  # Allow small buffer for snapping
                self.vel_y > 0  # Fairy is falling
            )

            # Both conditions must be met to land
            if is_midpoint_on_platform and is_falling_onto_platform:
                # Snap the player's bottom to the top of the platform
                self.rect.bottom = platform.rect.top
                self.vel_y = 0  # Stop vertical movement
                self.is_jumping = False  # Allow jumping again
                self.is_falling = False  # Stop falling
                self.on_platform = True  # Mark the player as on a platform
                return True  # Collision detected, stop further checks
        return False

    
    def update(self, platforms, ladders, chests, level_width):
        """
        Updates the player's position and handles collisions with platforms.
        :param platforms: List of Platform objects.
        """
        keys = pygame.key.get_pressed()

        # Horizontal movement
        if keys[pygame.K_LEFT]:
            if self.rect.x > SCREEN_WIDTH // 4 or self.scroll_x <= 0:
                self.vel_x = -PLAYER_SPEED
            else:
                self.scroll_x = max(self.scroll_x - self.scroll_speed, 0)  # Allow negative scrolling
        elif keys[pygame.K_RIGHT]:
            if self.rect.x < 2 * SCREEN_WIDTH // 4 or self.scroll_x + SCREEN_WIDTH >= level_width:
                self.vel_x = PLAYER_SPEED
            else:
                self.vel_x = 0
                self.scroll_x = min(self.scroll_x + self.scroll_speed, level_width - SCREEN_WIDTH)  # Scroll right
        else:
            self.vel_x = 0
        
        self.scroll_x = max(0, min(self.scroll_x, level_width - SCREEN_WIDTH))

        # Jumping
        if keys[pygame.K_SPACE] and not self.is_jumping and not self.is_falling:
            self.vel_y = -PLAYER_JUMP_POWER  # Vertical velocity for the jump
            self.vel_x = PLAYER_JUMP_FORWARD_SPEED if keys[pygame.K_RIGHT] else (
                -PLAYER_JUMP_FORWARD_SPEED if keys[pygame.K_LEFT] else 0
            )  # Add forward or backward velocity during jump
            self.is_jumping = True
            self.on_platform = False

            # Jump animation
            self.image = self.image_jump  # Switch to jump sprite
            self.jump_animation_timer = pygame.time.get_ticks()  # Start animation timer

        # Dropping through a platform
        if keys[pygame.K_DOWN]:
            self.is_dropping = True  # Enable drop-through state

        # Climbing ladders
        self.on_ladder = False
        for ladder in ladders:
            if self.rect.colliderect(ladder.rect) and keys[pygame.K_UP]:
                self.vel_y = -PLAYER_CLIMB_SPEED  # Move upward at climbing speed
                self.on_ladder = True
                break
            else:
                self.on_ladder = False  # Reset if not on a ladder

        # Opening chests
        for chest in chests:
            if self.rect.colliderect(chest.rect) and not chest.collected:
                # Handle chest interaction (e.g., key press)
                keys = pygame.key.get_pressed()
                if keys[pygame.K_e]:  # Press 'E' to open the chest
                    chest.collected = True  # Mark chest as opened
                    self.score += 10  # Increase the player's score
                    print(f"Chest opened! Score: {self.score}")

        # Apply gravity only if not climbing
        if not self.on_ladder:
            self.vel_y += GRAVITY

        # Update vertical position
        self.rect.y += self.vel_y

        # Prevent falling below the screen
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.vel_y = 0

        # Apply gravity only if not on platform
        if not self.on_platform or self.is_dropping:
            self.vel_y += GRAVITY
            if self.vel_y > 0:
                self.is_falling = True

        # Update vertical position
        self.rect.y += self.vel_y

        # Check for platform collisions
        if not self.is_dropping and self.check_platform_collisions(platforms):
            self.is_falling = False
        else:
            self.on_platform = False

        # Collision with ground
        if self.rect.bottom > GROUND_LEVEL:
            self.rect.bottom = GROUND_LEVEL
            self.vel_y = 0
            self.is_jumping = False
            self.is_falling = False
            self.on_platform = True
            self.is_dropping = False

        # Check if the player falls off platforms (if not on a platform)
        if not self.on_platform and self.rect.bottom < SCREEN_HEIGHT - 50:
            self.is_jumping = True  # Allow jumping again while falling
            
        # Update horizontal position
        self.rect.x += self.vel_x
        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.rect.width))

        # Jump animation duration
        if self.image == self.image_jump:
            if pygame.time.get_ticks() - self.jump_animation_timer > 200:  # 200ms duration
                self.image = self.image_idle



    def draw(self, screen):
        # Draw the player sprite
        screen.blit(self.image, self.rect)
        
        # Debug: Draw the player's midpoint
        pygame.draw.circle(screen, (255, 0, 0), self.rect.center, 3)  # Red dot for midpoint
        pygame.draw.rect(screen, (0, 0, 255), self.rect, 2)  # Blue outline

