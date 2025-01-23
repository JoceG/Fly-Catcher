import pygame
import random
from fly import Fly
from frog import Frog
from screen_manager import ScreenManager
from special_fly import SpecialFly

def draw_popups(score_popups):
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

def create_game_loop(screen_manager, frog_img, fly_img_left, fly_img_right, special_fly_img_left,
                     special_fly_img_right, initial_fly_count=5):
    """
    Runs the game loop, handling events and updating the display.
    
    Args:
        screen_manager (ScreenManager): The ScreenManager instance to handle screen resizing and updates.
    """
    # Timer starts here when the loop begins
    start_time = pygame.time.get_ticks()

    # Time given (2 minutes)
    countdown_time = 120

    # Store active pop-ups
    score_popups = []
    
    # Create the Frog instance
    frog = Frog(screen_manager.width / 2, screen_manager.height / 2, frog_img)
    
    # Number of flies the frog has eaten
    score = 0
    
    # List to store flies
    flies = [Fly(screen_manager.width, screen_manager.height, fly_img_left, fly_img_right) for i in range(initial_fly_count)]

    # Set initial size of the flies (using floats for precision)
    fly_width, fly_height = 30.0, 30.0

    # Set up a clock for a consistent frame rate
    clock = pygame.time.Clock()
    
    running = True
    game_over = False
    
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Generate a new fly when the timer event occurs
            if event.type == REGULAR_FLY_EVENT:
                flies.append(Fly(screen_manager.width, screen_manager.height, fly_img_left, fly_img_right, fly_width, fly_height))

            if event.type == SPECIAL_FLY_EVENT:
                # Occasionally spawn a special fly with a 30% chance
                #if random.random() < 0.3:
                flies.append(SpecialFly(screen_manager.width, screen_manager.height, special_fly_img_left, special_fly_img_right, fly_width, fly_height))
                
            if event.type == pygame.VIDEORESIZE:
                # Get the new width and height from the resize event
                new_width, new_height = event.w, event.h

                # Resize the screen via ScreenManager
                screen_manager.resize(new_width, new_height)

                # Get the scaling factor to adjust the game elements based on the new screen size
                # The scaling factor ensures that the frog's position and size are proportional to the new screen size
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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    frog.movement['left'] = True
                if event.key == pygame.K_RIGHT:
                    frog.movement['right'] = True
                if event.key == pygame.K_DOWN:
                    frog.movement['down'] = True
                if event.key == pygame.K_UP:
                    frog.movement['up'] = True
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    frog.movement['left'] = False
                if event.key == pygame.K_RIGHT:
                    frog.movement['right'] = False
                if event.key == pygame.K_DOWN:
                    frog.movement['down'] = False
                if event.key == pygame.K_UP:
                    frog.movement['up'] = False

        # Only proceed with game logic if still running
        if running:
            # Update the frog's position based on the movement states
            frog.move(screen_manager)
            
            # Update the display (draw the frog at new position)
            screen_manager.clear() # clear screen with the background color
            frog.draw(screen_manager.screen)

            # Draw flies
            for fly in flies:
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

            # Draw the +5 popups
            draw_popups(score_popups)

            # Draw the score and time
            elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
            remaining_time = max(0, countdown_time - elapsed_time)
            draw_score_and_time(screen_manager.screen, score, remaining_time)

            if remaining_time == 0:
                game_over = True
                break

            # Refresh display
            pygame.display.flip()

            # Limit the frame rate to 60 frames per second
            clock.tick(60)

    if game_over:
        print("Time's up! Game over.")

    pygame.quit()
                
if __name__ == '__main__':
    # Initialize the ScreenManger
    screen_manager = ScreenManager()

    # Initialize the frog and fly images
    frog_img = pygame.image.load('frog.png')
    fly_img_left = pygame.image.load('fly_left_facing.png')
    fly_img_right = pygame.image.load('fly_right_facing.png')
    special_fly_img_left = pygame.image.load('special_fly_left_facing.png')
    special_fly_img_right = pygame.image.load('special_fly_right_facing.png')

    # Define custom events for fly generation
    REGULAR_FLY_EVENT = pygame.USEREVENT + 1
    SPECIAL_FLY_EVENT = pygame.USEREVENT + 2

    # Set timers for regular and special flies
    pygame.time.set_timer(REGULAR_FLY_EVENT, 2000)  # Regular flies every 2 seconds
    pygame.time.set_timer(SPECIAL_FLY_EVENT, 8000)  # Special flies every 8 seconds

    create_game_loop(screen_manager, frog_img, fly_img_left, fly_img_right, special_fly_img_left, special_fly_img_right)
