from constants import GAME_DURATION, INITIAL_FLY_COUNT
from fly import Fly
from frog import Frog

class GameState:
    def __init__(self):
        """
        Initializes the game state with default values.
        """
        self.countdown_time = 0
        self.frog = None
        self.flies = []
        self.score = 0
        self.score_popups = []
        self.fly_width, self.fly_height = 0, 0

    def reset(self, screen_width, screen_height):
        """
        Resets the game state for a new game session.

        Args:
            screen_width (int): The width of the game screen.
            screen_height (int): The height of the game screen.
        """
        self.countdown_time = GAME_DURATION
        self.score = 0
        self.score_popups = []
        self.fly_width = screen_width / 20
        self.fly_height = screen_width / 20

        # Reset game entities
        self.frog = Frog(screen_width / 2, screen_height / 2,
                         screen_width / 10, screen_height / 10)
        self.flies = [Fly(screen_width, screen_height, self.fly_width,
                          self.fly_height) for _ in range(INITIAL_FLY_COUNT)]

