import pygame

def setup_pygame_window(width=500, height=500, background_color=(243, 207, 198)):
    """
    Sets up the Pygame window.

    Args:
        width (int): Width of the window. Default is 500.
        height (int): Height of the window. Default is 500.
        background_color (tuple): RGB tuple for the background color. Default is (243, 207, 198).
        
    Returns:
        pygame.Surface: The created Pygame screen.
    """
    
    # Initialize Pygame
    pygame.init()

    # Create window
    screen = pygame.display.set_mode((width, height))
    
    # Set window title
    pygame.display.set_caption('Fly Catcher')

    # Set background color
    screen.fill(background_color)

    return screen

def create_game_loop(screen):
    """
    Runs the game loop, handling events and updating the display.
    
    Args:
        screen (pygame.Surface): The Pygame screen where the game is rendered
    """
    # Set initial position and movement speed of the frog
    frog_x, frog_y = 250, 250
    frog_width, frog_height = 30, 30
    frog_speed = 5

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
        if movement['right'] and frog_x < screen.get_width() - frog_width: 
            frog_x += frog_speed
        if movement['down'] and frog_y < screen.get_height() - frog_height:
            frog_y += frog_speed
        if movement['up'] and frog_y > 0:
            frog_y -= frog_speed
        
        # Update the display (draw the frog at new position)
        screen.fill((243, 207, 198))  # clear screen with background color
        pygame.draw.rect(screen, (0, 255, 0), (frog_x, frog_y, frog_width, frog_height))  # draw frog (green rectangle for now)
        pygame.display.flip()

        # Limit the frame rate to 60 frames per second
        clock.tick(60)

    pygame.quit()
                
if __name__ == '__main__':
    screen = setup_pygame_window()
    create_game_loop(screen)
