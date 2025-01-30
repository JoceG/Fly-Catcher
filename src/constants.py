import pygame

# Define custom events for fly generation
FLY_SPAWN = pygame.USEREVENT + 1
SPECIAL_FLY_SPAWN = pygame.USEREVENT + 2

# Timer constants
FLY_SPAWN_INTERVAL = 2000
SPECIAL_FLY_SPAWN_INTERVAL = 8000

# Load frog and fly images
FROG = pygame.image.load('../assets/frog.png')
FLY_LEFT = pygame.image.load('../assets/fly_left_facing.png')
FLY_RIGHT = pygame.image.load('../assets/fly_right_facing.png')
SPECIAL_FLY_LEFT = pygame.image.load('../assets/special_fly_left_facing.png')
SPECIAL_FLY_RIGHT = pygame.image.load('../assets/special_fly_right_facing.png')

# Fixed game configurations
GAME_DURATION = 120  # Game duration in seconds
INITIAL_FLY_COUNT = 5
FROG_SPEED = 5.0
FLY_SPEED = 2.0
