import pygame

class ScreenManager:
    def __init__(self, width=500, height=500, background_color=(243, 207, 198)):
        """
        Initializes the screen manager with default values.

        Args:
            width (int, optional): Initial width of the screen. Defaults to 500.
            height (int, optional): Initial height of the screen. Defaults to 500.
            background_color (tuple, optional): RGB color for the background. Defaults to (243, 207, 198).
        """
        self.width = width
        self.height = height
        self.previous_width = width
        self.previous_height = height
        self.background_color = background_color
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
