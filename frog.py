import pygame

class Frog:
    def __init__(self, x, y, width=30.0, height=30.0, speed=5.0, color=(0, 255, 0)):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._speed = speed
        self._color = color
        self._movement = {
            'left': False,
            'right': False,
            'down': False,
            'up': False
        }

    @property
    def x(self):
        """
        Returns the frog's x position.
        """
        return self._x

    @property
    def y(self):
        """
        Returns the frog's y position.
        """
        return self._y

    @property
    def width(self):
        """
        Returns the frog's current width.
        """
        return self._width

    @property
    def height(self):
        """
        Returns the frog's current height.
        """
        return self._height

    @property
    def speed(self):
        """
        Returns the frog's speed.
        """
        return self._speed

    @property
    def color(self):
        """
        Returns the frog's color.
        """
        return self._color

    @property
    def movement(self):
        """
        Returns the frog's movement direction dictionary
        """
        return self._movement

    def move(self, screen_manager):
        """
        Updates the frog's position based on movement states
        """
        if self._movement['left'] and self._x > 0:
            self._x -= self._speed
        if self._movement['right'] and self._x + self._width < screen_manager.width: 
            self._x += self._speed
        if self._movement['down'] and self._y + self._height < screen_manager.height:
            self._y += self._speed
        if self._movement['up'] and self._y > 0:
            self._y -= self._speed

    def resize(self, width_scale, height_scale):
        """
        Resizes the frog based on the scaling factors.
        """
        self._width *= width_scale
        self._height *= height_scale

    def reposition(self, width_scale, height_scale):
        """
        Repositions the frog based on the scaling factors to maintain its relative position
        on the screen.
        """
        self._x *= width_scale
        self._y *= height_scale

    def draw(self, screen):
        """
        Draws the frog (used after resize and reposition from screen resizing).
        """
        pygame.draw.rect(screen, self._color, (int(self._x), int(self._y), int(self._width), int(self._height)))
