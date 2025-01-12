import pygame

class ScreenManager:
    def __init__(self, width=500, height=500, background_color=(243, 207, 198)):
        """
        Initialize the screen manager with default screen size and color.
        """
        self._width = width
        self._height = height
        self._previous_width = width
        self._previous_height = height
        self._background_color = background_color
        self._screen = None
        self._initialize_screen()

    @property
    def width(self):
        """
        Returns the current screen width.
        """
        return self._width

    @property
    def height(self):
        """
        Returns the Pygame screen height.
        """
        return self._height

    @property
    def screen(self):
        """
        Returns the Pygame screen for use in the game loop.
        """
        if self._screen is None:
            raise ValueError("Screen has not be initialized.")
        return self._screen

    def _initialize_screen(self):
        """
        Set up the Pygame screen.
        """
        pygame.init()
        self._screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
        pygame.display.set_caption('Fly Catcher')
        self._screen.fill(self._background_color)

    def resize(self, new_width, new_height):
        """
        Resize the screen when the screen is resized.

        Args:
            new_width (int): The new width of the screen.
            new_height (int): The new height of the screen.
        """
        # Update the previous dimensions
        self._previous_width = self._width
        self._previous_height = self._height

        # Update the current dimensions
        self._width = new_width
        self._height = new_height

        # Resize the Pygame screen
        self._screen = pygame.display.set_mode((new_width, new_height), pygame.RESIZABLE)

    def clear(self):
        """
        Clear the screen with the background color.
        """
        if self._screen:
            self._screen.fill(self._background_color)

    def get_scaling_factors(self):
        """
        Returns a tuple containing scaling factors for width and height.
        """
        width_scale = self._width / self._previous_width
        height_scale = self._height / self._previous_height
        return width_scale, height_scale
