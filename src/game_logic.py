import pygame
from special_fly import SpecialFly

def check_collision(frog, fly):
    """
    Checks whether the frog and a fly are colliding.

    Args:
        frog: The frog object.
        fly: The fly object.

    Returns:
        bool: True if the frog and fly are colliding, otherwise False.
    """
    frog_rect = pygame.Rect(frog.x, frog.y, frog.width, frog.height)
    fly_rect = pygame.Rect(fly.x, fly.y, fly.width, fly.height)
    return frog_rect.colliderect(fly_rect)

def update_frog_and_flies(game_state, screen_width, screen_height):
    """
    Updates the frog's position and processes interactions with flies.

    Args:
        game_state: The current game state containing the frog, flies, 
                    score, countdown time, and score popups.
        screen_width: The width of the game screen.
        screen_height: The height of the game screen.
    """
    # Move the frog based on user input and screen boundaries
    game_state.frog.move(screen_width, screen_height)

    # Iterate over a copy of the fly list to safely remove flies if needed
    for fly in game_state.flies[:]:
        if check_collision(game_state.frog, fly):
            game_state.flies.remove(fly)
            game_state.score += 1
            game_state.countdown_time += 25 if isinstance(fly, SpecialFly) else 5

            # Store the position and timestamp of the score popup
            game_state.score_popups.append({
                "pos": (fly.x, fly.y),
                "time": pygame.time.get_ticks(),
                "special": isinstance(fly, SpecialFly)
            })
        elif isinstance(fly, SpecialFly) and not fly.move():
            # Remove special flies that move out of screen boundaries
            game_state.flies.remove(fly) 

        elif not isinstance(fly, SpecialFly):
            # Move regular flies within screen boundaries
            fly.move(screen_width, screen_height)
