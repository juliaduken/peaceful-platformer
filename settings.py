import os 

## Constants and Configurations ##
# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GROUND_LEVEL = 500
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 150, 255)
BACKGROUND = (170, 192, 255)
YELLOW = (255, 196, 0)

# Player settings
PLAYER_SPEED = 5
PLAYER_JUMP_POWER = 17
PLAYER_JUMP_FORWARD_SPEED = 10
PLAYER_CLIMB_SPEED = 5
GRAVITY = 0.75

# Level settings
GAME_TIME = 30000 # 30 seconds = 30000 ms

# Assets path
ASSETS_PATH = os.path.join(os.path.dirname(__file__), 'assets')
