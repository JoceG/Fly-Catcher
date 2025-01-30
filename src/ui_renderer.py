import pygame

def draw_flies(game_state, screen):
    """
    Draws all flies on the screen.

    Args:
        game_state (object): The game state containing the list of flies.
        screen (pygame.Surface): The game screen where the flies will be drawn.
    """
    for fly in game_state.flies:
        fly.draw(screen)

def draw_popups(score_popups, screen):
    """
    Draws score popups on the screen and removes expired ones.

    Args:
        score_popups (list): A list of dictionaries, each representing a popup with keys:
            - "time" (int): The timestamp when the popup was created.
            - "pos" (tuple): The (x, y) position of the popup.
            - "special" (bool): Whether it's a special popup (+25s) or a normal one (+5s).
        screen (pygame.Surface): The game screen where the popups will be drawn.
    """
    current_time = pygame.time.get_ticks()
    font = pygame.font.Font(None, 30)

    gold_color = (255, 223, 0)  # Color for special popups
    gray_color = (169, 169, 169)  # Color for regular popups

    active_popups = []  # Collect active popups to update the list for the next frame

    for popup in score_popups:
        if current_time - popup["time"] < 1000:  # Show for 1 second
            color = gold_color if popup["special"] else gray_color
            text = font.render("+25s" if popup["special"] else "+5s", True, color)
            screen.blit(text, (popup["pos"][0], popup["pos"][1] - 20))
            active_popups.append(popup)  # Keep active popups

    score_popups[:] = active_popups  # Update list with active popups only

def draw_score_and_time(screen, score, time_remaining):
    """
    Draws the score and remaining time on the screen.

    Args:
        screen (pygame.Surface): The game screen where the score and time will be displayed.
        score (int): The current score of the player.
        time_remaining (int): The remaining time in seconds.
    """
    font = pygame.font.SysFont("Arial", 24)
    score_x_position = 10
    minutes = time_remaining // 60
    seconds = time_remaining % 60

    # Render the score text
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    score_width = score_text.get_width()
    screen.blit(score_text, (score_x_position, 10))  # Display score at position (10, 10)

    # Render the time remaining text
    time_text = font.render(f"{minutes:02}:{seconds:02}", True, (0, 0, 0))  # Format time as MM:SS
    time_width = time_text.get_width()

    # Calculate x-coordinate to center the time text under the score
    time_x_position = score_x_position + (score_width - time_width) // 2

    # Display the time below the score
    screen.blit(time_text, (time_x_position, 50))  # Position the time 50px below the score

def draw_game_objects(game_state, screen_manager, start_time):
    """
    Updates and renders all game objects on the screen.

    Args:
        game_state (GameState): The current state of the game, including frog, flies, score, etc.
        screen_manager (ScreenManager): Manages the game screen.
        start_time (int): The timestamp when the game started, used for countdown calculations.
    """
    screen_manager.clear()  # Clear the screen to prepare for new frame rendering

    # Draw individual game elements
    game_state.frog.draw(screen_manager.screen)  # Draw frog
    draw_flies(game_state, screen_manager.screen)  # Draw flies
    draw_popups(game_state.score_popups, screen_manager.screen)  # Draw score popups (+5s and +25s)

    # Calculate the remaining time
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
    remaining_time = max(0, game_state.countdown_time - elapsed_time)

    # Draw score and time
    draw_score_and_time(screen_manager.screen, game_state.score, remaining_time)
