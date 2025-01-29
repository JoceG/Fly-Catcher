from constants import FROG, FLY_LEFT, FLY_RIGHT, GAME_DURATION, INITIAL_FLY_COUNT
from fly import Fly
from frog import Frog

class GameState:
    def __init__(self):
        # Countdown timer
        self.countdown_time = 0

        # Game entities
        self.frog = None
        self.flies = []

        # Score and visual effects
        self.score = 0
        self.score_popups = []

    def reset(self, screen_width, screen_height):
        """Reset the game state for a new game."""
        self.countdown_time = GAME_DURATION
        self.score = 0
        self.score_popups = []

        # Reset game entities
        self.frog = Frog(screen_width / 2, screen_height / 2, FROG)
        self.flies = [Fly(screen_width, screen_height, FLY_LEFT, FLY_RIGHT) for _ in range(INITIAL_FLY_COUNT)]
