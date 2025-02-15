import pygame
from constants import FROG, FROG_SPEED

class Frog:
    def __init__(self, x, y, width, height):
        """
        Initializes the frog with position, size, speed, and movement states.

        Args:
            x (float): The initial x-coordinate of the frog.
            y (float): The initial y-coordinate of the frog.
            width (float): The width of the frog. 
            height (float): The height of the frog.
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = FROG_SPEED
        self.movement = {
            'left': False,
            'right': False,
            'down': False,
            'up': False
        }

        self.original_img = FROG
        self.img = pygame.transform.scale(self.original_img, (int(self.width), int(self.height)))

    def move(self, screen_width, screen_height):
        """
        Updates the frog's position based on movement states while keeping it within screen bounds.

        Args:
            screen_width (int): The width of the game screen.
            screen_height (int): The height of the game screen.
        """
        if self.movement['left'] and self.x > 0:
            self.x -= self.speed
            
        if self.movement['right'] and self.x + self.width < screen_width: 
            self.x += self.speed

        if self.movement['up'] and self.y > 0:
            self.y -= self.speed
            
        if self.movement['down'] and self.y + self.height < screen_height:
            self.y += self.speed

    def resize(self, width_scale, height_scale):
        """
        Resizes the frog's dimensions based on scaling factors.

        Args:
            width_scale (float): The scale factor for width adjustment.
            height_scale (float): The scale factor for height adjustment.
        """
        self.width *= width_scale
        self.height *= height_scale
        self.img = pygame.transform.scale(self.original_img, (int(self.width), int(self.height)))

    def reposition(self, width_scale, height_scale):
        """
        Adjusts the frog’s position to maintain its relative placement on the screen after resizing.

        Args:
            width_scale (float): The scale factor for adjusting the x-coordinate.
            height_scale (float): The scale factor for adjusting the y-coordinate.
        """
        self.x *= width_scale
        self.y *= height_scale

    def draw(self, screen):
        """
        Draws the frog onto the given screen.

        Args:
            screen (pygame.Surface): The surface to draw the frog on.
        """
        screen.blit(self.img, (self.x, self.y))
