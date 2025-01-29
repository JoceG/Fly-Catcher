import pygame
from event_handler import handle_events
from game_logic import update_frog_and_flies
from game_over import game_over_loop
from ui_renderer import draw_game_objects

def is_time_up(start_time, countdown_time):
    """
    Checks if the game time has run out.

    Args:
        start time (int): The time (in milliseconds) when the game started.
        countdown_time (int): The time left in the game (in seconds).

    Returns:
        bool: True if the countdown timer has reached zero, False otherwise.
    """
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
    return elapsed_time >= countdown_time

def create_game_loop(screen_manager, game_state):
    """
    Runs the main game loop.

    Args:
        screen_manager (ScreenManager): Manages screen updates and resizing.
        game_state (GameState): Tracks the state of the game (score, time, entities).
    """
    start_time = pygame.time.get_ticks()
    clock = pygame.time.Clock()
    
    while True:
        handle_events(game_state.frog, game_state.flies, screen_manager)
        update_frog_and_flies(game_state, screen_manager.width, screen_manager.height)
        draw_game_objects(game_state, screen_manager, start_time)
        pygame.display.flip() # Refresh display
        clock.tick(60) # Limit frame rate

        # End the game if time is up
        if is_time_up(start_time, game_state.countdown_time):
            game_over_loop(screen_manager)
            return
