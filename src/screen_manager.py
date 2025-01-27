import pygame

class ScreenManager:
    def __init__(self, width=500, height=500, background_color=(243, 207, 198)):
        """
        Initializes the screen manager with default values.
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
        Sets up the Pygame screen.
        """
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
        pygame.display.set_caption('Fly Catcher')
        self.screen.fill(self.background_color)

    def resize(self, new_width, new_height):
        """
        Resizes the screen when the screen is resized.

        Args:
            new_width (int): The new width of the screen.
            new_height (int): The new height of the screen.
        """
        # Update the previous dimensions
        self.previous_width = self.width
        self.previous_height = self.height

        # Update the current dimensions
        self.width = new_width
        self.height = new_height

        # Resize the Pygame screen
        self.screen = pygame.display.set_mode((new_width, new_height), pygame.RESIZABLE)

    def clear(self):
        """
        Clears the screen with the background color.
        """
        if self.screen:
            self.screen.fill(self.background_color)

    def get_scaling_factors(self):
        """
        Returns a tuple containing scaling factors for width and height.
        """
        width_scale = self.width / self.previous_width
        height_scale = self.height / self.previous_height
        return width_scale, height_scale
