import pygame
from constants import BLACK_COLOR, GOLD_COLOR, GRAY_COLOR

def draw_flies(game_state, screen):
    """
    Draws all flies on the screen.

    Args:
        game_state (object): The game state containing the list of flies.
        screen (pygame.Surface): The game screen where the flies will be drawn.
    """
    for fly in game_state.flies:
        fly.draw(screen)

def draw_popups(score_popups, screen, screen_height):
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
    font = pygame.font.Font(None, int(screen_height * 0.05))
    
    active_popups = []  # Collect active popups to update the list for the next frame

    for popup in score_popups:
        if current_time - popup["time"] < 1000:  # Show for 1 second
            color = GOLD_COLOR if popup["special"] else GRAY_COLOR
            text = font.render("+5s" if popup["special"] else "+1", True, color)
            screen.blit(text, (popup["pos"][0], popup["pos"][1] - 20))
            active_popups.append(popup)  # Keep active popups

    score_popups[:] = active_popups  # Update list with active popups only

def draw_score_and_time(screen, screen_height, score, time_remaining):
    """
    Draws the score and remaining time on the screen.

    Args:
        screen (pygame.Surface): The game screen where the score and time will be displayed.
        score (int): The current score of the player.
        time_remaining (int): The remaining time in seconds.
    """
    font_size = int(screen_height * 0.05)
    font = pygame.font.SysFont("Arial", font_size)
    score_x_position = 10
    minutes = time_remaining // 60
    seconds = time_remaining % 60

    # Render the score text
    score_text = font.render(f"Score: {score}", True, BLACK_COLOR)
    score_width = score_text.get_width()
    screen.blit(score_text, (score_x_position, 10))  # Display score at position (10, 10)

    # Render the time remaining text
    time_text = font.render(f"{minutes:02}:{seconds:02}", True, BLACK_COLOR)  # Format time as MM:SS
    time_width = time_text.get_width()

    # Calculate x-coordinate to center the time text under the score
    time_x_position = score_x_position + (score_width - time_width) // 2

    # Position the time based on the font size (to keep spacing proportional)
    vertical_spacing = int(font_size * 1.2)  # 1.2x font size as spacing
    screen.blit(time_text, (time_x_position, int(screen_height * 0.02) + vertical_spacing)) 

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
    draw_popups(game_state.score_popups, screen_manager.screen, screen_manager.height)  # Draw score popups (+5s and +25s)

    # Calculate the remaining time
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
    remaining_time = max(0, game_state.countdown_time - elapsed_time)

    # Draw score and time
    draw_score_and_time(screen_manager.screen, screen_manager.height, game_state.score, remaining_time)
