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

if __name__ == '__main__':
    screen = setup_pygame_window()
    pygame.display.flip()
    pygame.quit()
