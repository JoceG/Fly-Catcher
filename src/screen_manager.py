import pygame
from constants import INITIAL_SCREEN_WIDTH, INITIAL_SCREEN_HEIGHT, BACKGROUND_COLOR

class ScreenManager:
    def __init__(self):
        """
        Initializes the screen manager with default values.
        """
        self.width = INITIAL_SCREEN_WIDTH
        self.height = INITIAL_SCREEN_HEIGHT
        self.previous_width = self.width
        self.previous_height = self.height
        self.background_color = BACKGROUND_COLOR
        self.screen = None
        self.initialize_screen()

    def initialize_screen(self):
        """
        Sets up the Pygame screen with the specified dimensions and background color.
        The screen is resizable.
        """
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
        pygame.display.set_caption('Fly Catcher')
        self.screen.fill(self.background_color)

    def resize(self, new_width, new_height):
        """
        Resizes the screen and updates previous dimensions.

        Args:
            new_width (int): The new width of the screen.
            new_height (int): The new height of the screen.
        """
        self.previous_width, self.previous_height = self.width, self.height
        self.width, self.height = new_width, new_height
        self.screen = pygame.display.set_mode((new_width, new_height), pygame.RESIZABLE)

    def clear(self):
        """
        Clears the screen by filling it with the background color.
        """
        if self.screen:
            self.screen.fill(self.background_color)

    def get_scaling_factors(self):
        """
        Calculates the scaling factors for width and height based on the previous screen size.

        Returns:
            tuple: A tuple (width_scale, height_scale) where both values are floats representing 
                   the scaling factors for width and height.
        """
        return self.width / self.previous_width, self.height / self.previous_height
