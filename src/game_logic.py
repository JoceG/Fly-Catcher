import pygame
from special_fly import SpecialFly

def check_collision(frog, fly):
    """
    Checks if the frog and a fly are colliding.
    """
    frog_rect = pygame.Rect(frog.x, frog.y, frog.width, frog.height)
    fly_rect = pygame.Rect(fly.x, fly.y, fly.width, fly.height)
    return frog_rect.colliderect(fly_rect)

def draw_flies(flies, frog, screen_manager, countdown_time, score, score_popups):
    for fly in flies[:]:
        if check_collision(frog, fly):
            flies.remove(fly)

            if isinstance(fly, SpecialFly):
                countdown_time += 25
            else:
                countdown_time += 5
            
            score += 1

            # Store the position and the time of the popup
            score_popups.append({
                "pos": (fly.x, fly.y),
                "time": pygame.time.get_ticks(),
                "special": isinstance(fly, SpecialFly)
            })

        elif isinstance(fly, SpecialFly) and not fly.move():
            flies.remove(fly) # Remove the special fly if it moves out of bounds

        else:
            # Update the generic fly's position based on the movement states
            if not isinstance(fly, SpecialFly):
                fly.move()
            
            # Update the display (draw the fly at new position)
            fly.draw(screen_manager.screen)

    return countdown_time, score
