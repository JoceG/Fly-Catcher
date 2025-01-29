import pygame
from game_logic import draw_flies
from ui_renderer import draw_popups, draw_score_and_time

def draw_game_objects(game_state, screen_manager, start_time):
    """
    Updates and renders all game objects on the screen.

    Args:
        game_state (GameState): The current state of the game, including frog, flies, score, etc.
        screen_manager (ScreenManager): Manages the game screen.
        start_time (int): The timestamp when the game started, used for countdown calculations.
    """
    screen_manager.clear() # Clear the screen
    game_state.frog.draw(screen_manager.screen) # Draw frog
    draw_flies(game_state, screen_manager)
    draw_popups(game_state.score_popups, screen_manager) # Draw +5 and +25 popups
    
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
    remaining_time = max(0, game_state.countdown_time - elapsed_time)
    draw_score_and_time(screen_manager.screen, game_state.score, remaining_time)
