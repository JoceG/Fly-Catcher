import pygame

def show_game_over_screen(screen, screen_width, screen_height):
    """
    Displays the game over screen with options to play again or exit.

    Args:
        screen (pygame.Surface): The game screen where elements will be drawn.
        screen_width (int): The width of the game screen.
        screen_height (int): The height of the game screen.

    Returns:
        tuple: (play_again_button, exit_button), pygame.Rect objects representing 
               the interactive button areas.
    """
    screen.fill((243, 207, 198)) # Background color

    game_over_surface = render_text("GAME OVER", 80, (0, 0, 0))
    game_over_pos = game_over_surface.get_rect(center=(screen_width // 2, screen_height // 3))
    screen.blit(game_over_surface, game_over_pos)

    # Draw buttons and return their Rect objects
    play_again_button = draw_button(screen, "Play Again", (screen_width // 2, screen_height // 2), (50, 150, 50))
    exit_button = draw_button(screen, "Exit", (screen_width // 2, screen_height // 2 + 80), (200, 50, 50))

    pygame.display.update()

    return play_again_button, exit_button

def render_text(text, font_size, color):
    """
    Renders text as a Pygame surface.

    Args:
        text (str): The text to render.
        font_size (int): The size of the font.
        color (tuple): RGB color of the text.

    Returns:
        pygame.Surface: The rendered text surface.
    """
    font = pygame.font.Font(None, font_size)
    return font.render(text, True, color)

def draw_button(screen, text, center_pos, color):
    """
    Draws a button with centered text.

    Args:
        screen (pygame.Surface): The game screen to draw on.
        text (str): The button text.
        center_pos (tuple): (x, y) position for centering the button.
        color (tuple): RGB color of the button.

    Returns:
        pygame.Rect: The rectangle representing the button area.
    """
    font = pygame.font.Font(None, 40)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=center_pos)

    button_rect = pygame.Rect(center_pos[0] - 100, center_pos[1] - 25, 200, 50)
    pygame.draw.rect(screen, color, button_rect)
    screen.blit(text_surface, text_rect)

    return button_rect

def game_over(screen_manager):
    """
    Handles the game over screen, allowing the player to restart or exit.

    Args:
        screen_manager: An instance of ScreenManager that manages the game screen.
    """
    screen = screen_manager.screen
    screen_width = screen_manager.width
    screen_height = screen_manager.height
    
    play_again_button, exit_button = show_game_over_screen(screen, screen_width, screen_height)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.VIDEORESIZE:
                # Update the screen dimensions
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                screen_manager.resize(event.w, event.h)

                # Re-render the game over screen and update button positions
                play_again_button, exit_button = show_game_over_screen(screen, event.w, event.h)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if play_again_button.collidepoint(mouse_pos):
                    return # Exit game over screen, restart game
                    
                elif exit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    exit()
