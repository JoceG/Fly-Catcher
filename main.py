import pygame
import random
from fly import Fly
from frog import Frog
from screen_manager import ScreenManager
from special_fly import SpecialFly

# Define custom events for fly generation
FLY_SPAWN = pygame.USEREVENT + 1
SPECIAL_FLY_SPAWN = pygame.USEREVENT + 2

# Load frog and fly images
FROG = pygame.image.load('frog.png')
FLY_LEFT = pygame.image.load('fly_left_facing.png')
FLY_RIGHT = pygame.image.load('fly_right_facing.png')
SPECIAL_FLY_LEFT = pygame.image.load('special_fly_left_facing.png')
SPECIAL_FLY_RIGHT = pygame.image.load('special_fly_right_facing.png')

# Fixed game configurations
GAME_DURATION = 120  # Game time in seconds (2 minutes)
INITIAL_FLY_COUNT = 5
FLY_WIDTH = 30.0
FLY_HEIGHT = 30.0

# Use global variables for initial fly sizes, can be updated dynamically
fly_width, fly_height = FLY_WIDTH, FLY_HEIGHT

def show_game_over_screen(screen, screen_width, screen_height):
    game_over_text = "GAME OVER"
    play_again_text = "Play Again"
    exit_text = "Exit"

    # Define fonts
    font_large = pygame.font.Font(None, 80)
    font_small = pygame.font.Font(None, 40)

    # Render text
    game_over_surface = font_large.render(game_over_text, True, (0, 0, 0))
    play_again_surface = font_small.render(play_again_text, True, (255, 255, 255))
    exit_surface = font_small.render(exit_text, True, (255, 255, 255))

    # Text positions
    game_over_pos = game_over_surface.get_rect(center=(screen_width // 2, screen_height // 3))
    play_again_pos = play_again_surface.get_rect(center=(screen_width // 2, screen_height // 2))
    exit_pos = exit_surface.get_rect(center=(screen_width // 2, screen_height // 2 + 80))

    # Button dimensions
    play_again_button = pygame.Rect(screen_width // 2 - 100, screen_height // 2 - 25, 200, 50)
    exit_button = pygame.Rect(screen_width // 2 - 100, screen_height // 2 + 55, 200, 50)

    # Draw game over screen
    screen.fill((243, 207, 198))  # Background color
    screen.blit(game_over_surface, game_over_pos)

    # Draw buttons
    pygame.draw.rect(screen, (50, 150, 50), play_again_button)  # Green play button
    pygame.draw.rect(screen, (200, 50, 50), exit_button)  # Red exit button

    screen.blit(play_again_surface, play_again_pos)
    screen.blit(exit_surface, exit_pos)

    pygame.display.update()

    return play_again_button, exit_button

def game_over_loop(screen, screen_width, screen_height):
    play_again_button, exit_button = show_game_over_screen(screen, screen_width, screen_height)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                show_game_over_screen(screen, event.w, event.h)  # Re-render with new size
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if play_again_button.collidepoint(mouse_pos):
                    return # Exit game over screen, restart game
                    
                elif exit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    exit()
    
def draw_popups(score_popups, screen_manager):
    current_time = pygame.time.get_ticks()
    for popup in score_popups[:]:
        if current_time - popup["time"] < 1000:  # Show for 1 second
            font = pygame.font.Font(None, 30)

            if popup["special"]:
                text = font.render("+25s", True, (255, 223, 0))  # Gold text for special fly
            else:
                text = font.render("+5s", True, (169, 169, 169))  # Gray text for regular flies

            screen_manager.screen.blit(text, (popup["pos"][0], popup["pos"][1] - 20))
        else:
            score_popups.remove(popup)  # Remove after 1 second

def draw_score_and_time(screen, score, time_remaining):
    font = pygame.font.SysFont("Arial", 24)
    score_x = 10 
    minutes = time_remaining // 60
    seconds = time_remaining % 60

    # Render the score text
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    score_width = score_text.get_width()
    screen.blit(score_text, (score_x, 10))  # Display score at position (10, 10)

    # Render the time remaining text
    time_text = font.render(f"{minutes:02}:{seconds % 60:02}", True, (0, 0, 0))  # Format: MM:SS
    time_width = time_text.get_width()

    # Calculate the x-coordinate for centering the time relative to the score width
    time_x = score_x + (score_width - time_width) // 2  # Horizontally center the time under the score

    # Display the time below the score
    screen.blit(time_text, (time_x, 50))  # Position the time 50px below the score

def check_collision(frog, fly):
    """
    Checks if the frog and a fly are colliding.
    """
    frog_rect = pygame.Rect(frog.x, frog.y, frog.width, frog.height)
    fly_rect = pygame.Rect(fly.x, fly.y, fly.width, fly.height)
    return frog_rect.colliderect(fly_rect)

def handle_resize(event, screen_manager, frog, flies):
    global fly_width, fly_height
    new_width, new_height = event.w, event.h
    screen_manager.resize(new_width, new_height)
    width_scale, height_scale = screen_manager.get_scaling_factors()

    # Update the frog's position and size relative to the new screen size
    frog.resize(width_scale, height_scale)
    frog.reposition(width_scale, height_scale)

    # Update the flies' size relative to the new screen size
    fly_width *= width_scale
    fly_height *= height_scale

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

def handle_events(frog, flies, screen_manager):
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
            handle_resize(event, screen_manager, frog, flies)

        if event.type == pygame.KEYDOWN:
            handle_key_event(event, frog, True)
                
        elif event.type == pygame.KEYUP:
            handle_key_event(event, frog, False)

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
