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

        self._screen_width = screen_width  # Store screen width
        self._screen_height = screen_height  # Store screen height

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
    def x(self):
        """
        Returns the fly's x position.
        """
        return self._x

    @x.setter
    def x(self, value):
        # Ensure x is within bounds (cannot exceed screen width minus fly width)
        if value < 0:
            raise ValueError("x position cannot be negative.")
        if value > self._screen_width - self._width:
            raise ValueError(f"x position cannot be greater than screen width ({self._screen_width - self._width}).")
        self._x = value

    @property
    def y(self):
        """
        Returns the fly's y position.
        """
        return self._y

    @y.setter
    def y(self, value):
        # Ensure y is within bounds (cannot exceed screen height minus fly height)
        if value < 0:
            raise ValueError("y position cannot be negative.")
        if value > self._screen_height - self._height:
            raise ValueError(f"y position cannot be greater than screen height ({self._screen_height - self._height}).")
        self._y = value

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

