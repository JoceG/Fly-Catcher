import pygame
from fly import Fly
from screenmanager import ScreenManager

def create_game_loop(screen_manager, initial_fly_count=5):
    """
    Runs the game loop, handling events and updating the display.
    
    Args:
        screen_manager (ScreenManager): The ScreenManager instance to handle screen resizing and updates.
    """
    # List to store flies
    flies = [Fly(screen_manager.width, screen_manager.height) for i in range(initial_fly_count)]
    
    # Set initial position and movement speed of the frog (using floats for precision)
    frog_x, frog_y = screen_manager.width / 2.0, screen_manager.height / 2.0
    frog_width, frog_height = 30.0, 30.0
    frog_speed = 5.0

    # Dictionary to store movement states
    movement = {
        'left': False,
        'right': False,
        'down': False,
        'up': False
    }

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
                flies.append(Fly(screen_manager.width, screen_manager.height))
                
            if event.type == pygame.VIDEORESIZE:
                # Get the new width and height from the resize event
                new_width, new_height = event.w, event.h

                # Resize the screen via ScreenManager
                screen_manager.resize(new_width, new_height)

                # Get the scaling factor to adjust the game elements based on the new screen size
                # The scaling factor ensures that the frog's position and size are proportional to the new screen size
                width_scale, height_scale = screen_manager.get_scaling_factors()

                # Update the frog's position and size relative to the new screen size
                frog_x *= width_scale
                frog_y *= height_scale
                frog_width *= width_scale
                frog_height *= height_scale

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    movement['left'] = True
                if event.key == pygame.K_RIGHT:
                    movement['right'] = True
                if event.key == pygame.K_DOWN:
                    movement['down'] = True
                if event.key == pygame.K_UP:
                    movement['up'] = True
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    movement['left'] = False
                if event.key == pygame.K_RIGHT:
                    movement['right'] = False
                if event.key == pygame.K_DOWN:
                    movement['down'] = False
                if event.key == pygame.K_UP:
                    movement['up'] = False

        # Update frog position based on movement states
        if movement['left'] and frog_x > 0:
            frog_x -= frog_speed
        if movement['right'] and frog_x + frog_width < screen_manager.width: 
            frog_x += frog_speed
        if movement['down'] and frog_y + frog_height < screen_manager.height:
            frog_y += frog_speed
        if movement['up'] and frog_y > 0:
            frog_y -= frog_speed
        
        # Update the display (draw the frog at new position)
        screen_manager.clear() # clear screen with the background color
        pygame.draw.rect(screen_manager.screen, (0, 255, 0), (frog_x, frog_y, frog_width, frog_height))  # draw frog (green rectangle for now)

        # Draw flies
        for fly in flies:
            fly.draw(screen_manager.screen)

        # Refresh display
        pygame.display.flip()

        # Limit the frame rate to 60 frames per second
        clock.tick(60)

    pygame.quit()
                
if __name__ == '__main__':
    # Initialize the ScreenManger
    screen_manager = ScreenManager()
    
    # Fly generation timer event
    FLY_GENERATE_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(FLY_GENERATE_EVENT, 2000) # Trigger every 5 seconds

    create_game_loop(screen_manager)
