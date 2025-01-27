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
