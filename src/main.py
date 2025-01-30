import pygame
from constants import FLY_SPAWN, FLY_SPAWN_INTERVAL, SPECIAL_FLY_SPAWN, SPECIAL_FLY_SPAWN_INTERVAL
from game_loop import create_game_loop
from game_state import GameState
from screen_manager import ScreenManager

if __name__ == '__main__':
    screen_manager = ScreenManager() # Initialize screen manager

    # Set up fly spawn timers
    pygame.time.set_timer(FLY_SPAWN, FLY_SPAWN_INTERVAL)
    pygame.time.set_timer(SPECIAL_FLY_SPAWN, SPECIAL_FLY_SPAWN_INTERVAL)

    game_state = GameState() # Initialize game state

    # Main loop for replay functionality
    while True:
        game_state.reset(screen_manager.width, screen_manager.height)
        create_game_loop(screen_manager, game_state)
