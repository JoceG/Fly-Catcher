import random
import pygame

class Fly:
    def __init__(self, screen_width, screen_height, width=10, height=10, background_color=(0, 0, 0)):
        """
        Initialize the fly with default size and color and random position.
        """
        # Dimensions of the fly
        self._width = width
        self._height = height

        # Random initial position
        self._x = random.randint(0, int(screen_width) - int(self._width))
        self._y = random.randint(0, int(screen_width) - int(self._height))

        self._color = background_color # Black color for the fly

    @property
    def width(self):
        """
        Returns the current fly width.
        """
        return self._width

    @property
    def height(self):
        """
        Returns the current fly height.
        """
        return self._height

    @property
    def x_pos(self):
        """
        Returns the fly's x position.
        """
        return self._x

    @property
    def y_pos(self):
        """
        Returns the fly's y position.
        """
        return self._y

    @property
    def color(self):
        """
        Returns the fly's color
        """
        return self._color
    
    def resize(self, width_scale, height_scale):
        """
        Resizes the object based on the scaling factors.
        """
        self._width *= width_scale
        self._height *= height_scale

    def reposition(self, width_scale, height_scale):
        """
        Repositions the object to maintain its relative position on the screen.
        """
        self._x *= width_scale
        self._y *= height_scale

    def draw(self, screen):
        """
        Draws the fly (used after resizing and reposition from screen resizing).
        """
        pygame.draw.rect(screen, self._color, (self._x, self._y, self._width, self._height))

