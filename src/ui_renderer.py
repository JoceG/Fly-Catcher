import pygame

def draw_game_objects(game_state, screen_manager, start_time):
    """
    Updates and renders all game objects on the screen.

    Args:
        game_state (GameState): The current state of the game, including frog, flies, score, etc.
        screen_manager (ScreenManager): Manages the game screen.
        start_time (int): The timestamp when the game started, used for countdown calculations.
    """
    screen_manager.clear() # Clear the screen
    game_state.frog.draw(screen_manager.screen) # Draw frog
    draw_flies(game_state, screen_manager)
    draw_popups(game_state.score_popups, screen_manager) # Draw +5 and +25 popups
    
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
    remaining_time = max(0, game_state.countdown_time - elapsed_time)
    draw_score_and_time(screen_manager.screen, game_state.score, remaining_time)

def draw_flies(game_state, screen_manager):
    for fly in game_state.flies:
        fly.draw(screen_manager.screen)

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
