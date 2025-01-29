import pygame
from special_fly import SpecialFly

def check_collision(frog, fly):
    """
    Checks if the frog and a fly are colliding.
    """
    frog_rect = pygame.Rect(frog.x, frog.y, frog.width, frog.height)
    fly_rect = pygame.Rect(fly.x, fly.y, fly.width, fly.height)
    return frog_rect.colliderect(fly_rect)

def draw_flies(game_state, screen_manager):
    for fly in game_state.flies[:]:
        if check_collision(game_state.frog, fly):
            game_state.flies.remove(fly)

            if isinstance(fly, SpecialFly):
                game_state.countdown_time += 25
            else:
                game_state.countdown_time += 5
            
            game_state.score += 1

            # Store the position and the time of the popup
            game_state.score_popups.append({
                "pos": (fly.x, fly.y),
                "time": pygame.time.get_ticks(),
                "special": isinstance(fly, SpecialFly)
            })

        elif isinstance(fly, SpecialFly) and not fly.move():
            game_state.flies.remove(fly) # Remove the special fly if it moves out of bounds

        else:
            # Update the generic fly's position based on the movement states
            if not isinstance(fly, SpecialFly):
                fly.move()
            
            # Update the display (draw the fly at new position)
            fly.draw(screen_manager.screen)
