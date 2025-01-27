import pygame
import random
from constants import *
from event_handler import *
from fly import Fly
from frog import Frog
from game_logic import *
from game_over import *
from screen_manager import ScreenManager
from ui_renderer import *

def create_game_loop(screen_manager):
    """
    Runs the game loop, handling events and updating the display.
    
    Args:
        screen_manager (ScreenManager): The ScreenManager instance to handle screen resizing and updates.
    """
    # Start the timer for the game
    start_time = pygame.time.get_ticks()

    # Set up the clock to maintain a consistent frame rate
    clock = pygame.time.Clock()

    # Set countdown timer to the game duration
    countdown_time = GAME_DURATION

    # Number of flies the frog has eaten
    score = 0

    # List to store active pop-ups
    score_popups = []
    
    # List to store fly objects, initialized with the specified number of flies (INITIAL_FLY_COUNT)
    flies = [Fly(screen_manager.width, screen_manager.height, FLY_LEFT, FLY_RIGHT) for i in range(INITIAL_FLY_COUNT)]

    # Create the Frog instance at the center of the screen
    frog = Frog(screen_manager.width / 2, screen_manager.height / 2, FROG)
    
    while True:
        handle_events(frog, flies, screen_manager)

        # Update the frog's position based on the movement states
        frog.move(screen_manager)
        
        # Update the display (draw the frog at new position)
        screen_manager.clear() # clear screen with the background color
        frog.draw(screen_manager.screen)

        # Draw flies
        countdown_time, score = draw_flies(flies, frog, screen_manager, countdown_time, score, score_popups)

        # Draw the +5 popups
        draw_popups(score_popups, screen_manager)

        # Draw the score and time
        elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
        remaining_time = max(0, countdown_time - elapsed_time)
        draw_score_and_time(screen_manager.screen, score, remaining_time)

        # Refresh display
        pygame.display.flip()

        # Limit the frame rate to 60 frames per second
        clock.tick(60)

        if remaining_time == 0:
            game_over_loop(screen_manager.screen, screen_manager.width, screen_manager.height)
            return

if __name__ == '__main__':
    while True:
        # Initialize the ScreenManger
        screen_manager = ScreenManager()

        # Set timers for regular and special flies
        pygame.time.set_timer(FLY_SPAWN, 2000)  # Regular flies every 2 seconds
        pygame.time.set_timer(SPECIAL_FLY_SPAWN, 8000)  # Special flies every 8 seconds

        create_game_loop(screen_manager)
