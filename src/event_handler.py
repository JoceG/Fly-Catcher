import pygame
from constants import *
from fly import Fly
from special_fly import SpecialFly

def handle_resize(event, game_state, screen_manager, frog, flies):
    new_width, new_height = event.w, event.h
    screen_manager.resize(new_width, new_height)
    width_scale, height_scale = screen_manager.get_scaling_factors()

    # Update the frog's position and size relative to the new screen size
    frog.resize(width_scale, height_scale)
    frog.reposition(width_scale, height_scale)

    # Update the flies' size relative to the new screen size
    game_state.fly_width *= width_scale
    game_state.fly_height *= height_scale

    # Update each fly's position and size relative to the new screen size
    for fly in flies:
        fly.resize(width_scale, height_scale)
        fly.reposition(width_scale, height_scale)

def handle_key_event(event, frog, is_pressed):
    if event.key == pygame.K_LEFT:
        frog.movement['left'] = is_pressed
    if event.key == pygame.K_RIGHT:
        frog.movement['right'] = is_pressed
    if event.key == pygame.K_DOWN:
        frog.movement['down'] = is_pressed
    if event.key == pygame.K_UP:
        frog.movement['up'] = is_pressed

def handle_events(game_state, screen_manager):
    frog = game_state.frog
    flies = game_state.flies
    fly_width, fly_height = game_state.fly_width, game_state.fly_height
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Spawn a fly when the timer event occurs
        if event.type == FLY_SPAWN:
            flies.append(Fly(screen_manager.width, screen_manager.height, FLY_LEFT, FLY_RIGHT, fly_width, fly_height))

        # Spawn a special fly when the timer event occurs
        if event.type == SPECIAL_FLY_SPAWN:
            flies.append(SpecialFly(screen_manager.width, screen_manager.height, SPECIAL_FLY_LEFT, SPECIAL_FLY_RIGHT, fly_width, fly_height))
            
        if event.type == pygame.VIDEORESIZE:
            handle_resize(event, game_state, screen_manager, frog, flies)

        if event.type == pygame.KEYDOWN:
            handle_key_event(event, frog, True)
                
        elif event.type == pygame.KEYUP:
            handle_key_event(event, frog, False)
