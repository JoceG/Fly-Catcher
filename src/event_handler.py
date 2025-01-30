import pygame
from constants import FLY_SPAWN, SPECIAL_FLY_SPAWN, SPECIAL_FLY_LEFT, SPECIAL_FLY_RIGHT
from fly import Fly
from special_fly import SpecialFly

def handle_resize(event, game_state, screen_manager):
    """
    Handles window resize events by updating the screen size and scaling game entities accordingly.

    Args:
        event (pygame.event.Event): The resize event containing the new width and height.
        game_state (GameState): The current game state containing dynamic game variables.
        screen_manager (ScreenManager): Manages screen size and scaling factors.
    """
    screen_manager.resize(event.w, event.h)
    width_scale, height_scale = screen_manager.get_scaling_factors()

    # Update the frog's position and size relative to the new screen size
    game_state.frog.resize(width_scale, height_scale)
    game_state.frog.reposition(width_scale, height_scale)

    # Scale the fly size dynamically based on the new screen size
    game_state.fly_width *= width_scale
    game_state.fly_height *= height_scale

    # Update each fly's position and size relative to the new screen size
    for fly in game_state.flies:
        fly.resize(width_scale, height_scale)
        fly.reposition(width_scale, height_scale)

def handle_key_event(event, frog, is_pressed):
    """
    Handles key press and release events to control the frog's movement.

    Args:
        event (pygame.event.Event): The key event.
        frog (Frog): The player's frog character.
        is_pressed (bool): Whether the key is being pressed or released.
    """
    if event.key == pygame.K_LEFT:
        frog.movement['left'] = is_pressed
        
    if event.key == pygame.K_RIGHT:
        frog.movement['right'] = is_pressed
        
    if event.key == pygame.K_DOWN:
        frog.movement['down'] = is_pressed
        
    if event.key == pygame.K_UP:
        frog.movement['up'] = is_pressed

def handle_events(game_state, screen_manager):
    """
    Processes all game events, including quitting, resizing, spawning flies, and handling key presses.

    Args:
        game_state (GameState): The current game state containing game entities and variables.
        screen_manager (ScreenManager): Manages screen size and scaling factors.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Spawn a fly when the timer event occurs
        if event.type == FLY_SPAWN:
            game_state.flies.append(Fly(screen_manager.width, screen_manager.height,
                             game_state.fly_width, game_state.fly_height))

        # Spawn a special fly when the timer event occurs
        if event.type == SPECIAL_FLY_SPAWN:
            game_state.flies.append(SpecialFly(screen_manager.width, screen_manager.height,
                                    game_state.fly_width, game_state.fly_height))
            
        if event.type == pygame.VIDEORESIZE:
            handle_resize(event, game_state, screen_manager)

        if event.type == pygame.KEYDOWN:
            handle_key_event(event, game_state.frog, True)
        elif event.type == pygame.KEYUP:
            handle_key_event(event, game_state.frog, False)
