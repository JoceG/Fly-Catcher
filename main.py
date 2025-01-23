import pygame
from fly import Fly
from frog import Frog
from screen_manager import ScreenManager

def draw_score(screen, score):
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))  # Black color for the score
    screen.blit(score_text, (10, 10))  # Display the score at position (10, 10)

def check_collision(frog, fly):
    """
    Checks if the frog and a fly are colliding.
    """
    frog_rect = pygame.Rect(frog.x, frog.y, frog.width, frog.height)
    fly_rect = pygame.Rect(fly.x, fly.y, fly.width, fly.height)
    return frog_rect.colliderect(fly_rect)

def create_game_loop(screen_manager, frog_img, fly_img, initial_fly_count=5):
    """
    Runs the game loop, handling events and updating the display.
    
    Args:
        screen_manager (ScreenManager): The ScreenManager instance to handle screen resizing and updates.
    """
    # Create the Frog instance
    frog = Frog(screen_manager.width / 2, screen_manager.height / 2, frog_img)
    
    # Number of flies the frog has eaten
    score = 0
    
    # List to store flies
    flies = [Fly(screen_manager.width, screen_manager.height, fly_img) for i in range(initial_fly_count)]

    # Set initial size of the flies (using floats for precision)
    fly_width, fly_height = 30.0, 30.0

    # Set up a clock for a consistent frame rate
    clock = pygame.time.Clock()
    
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Generate a new fly when the timer event occurs
            if event.type == FLY_GENERATE_EVENT:
                flies.append(Fly(screen_manager.width, screen_manager.height, fly_img, fly_width, fly_height))
                
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
                    score += 1
                else:
                    # Update the fly's position based on the movement states
                    fly.move()
                    
                    # Update the display (draw the fly at new position)
                    fly.draw(screen_manager.screen)

            # Draw the score
            draw_score(screen_manager.screen, score)

            # Refresh display
            pygame.display.flip()

            # Limit the frame rate to 60 frames per second
            clock.tick(60)

    pygame.quit()
                
if __name__ == '__main__':
    # Initialize the ScreenManger
    screen_manager = ScreenManager()

    # Initialize the frog and fly images
    frog_img = pygame.image.load('frog.png')
    fly_img = pygame.image.load('fly.png')

    # Fly generation timer event
    FLY_GENERATE_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(FLY_GENERATE_EVENT, 2000) # Trigger every 5 seconds

    create_game_loop(screen_manager, frog_img, fly_img)
