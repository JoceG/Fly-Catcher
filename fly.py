import random
import pygame

class Fly:
    def __init__(self, screen_width, screen_height, fly_img, width=30.0, height=30.0, background_color=(0, 0, 0)):
        """
        Initialize the fly with default size and color and random position.
        """
        # Dimensions of the fly
        self.width = width
        self.height = height

        self.original_img = fly_img
        self.img = pygame.transform.scale(self.original_img, (int(self.width), int(self.height)))

        # Random initial position
        self.x = random.randint(0, int(screen_width) - int(self.width))
        self.y = random.randint(0, int(screen_height) - int(self.height))

        self.color = background_color # Black color for the fly
        self.screen_width = screen_width  # Store screen width
        self.screen_height = screen_height  # Store screen height

    def set_x(self, value):
        # Ensures x position is within bounds (cannot exceed screen width minus fly width)
        if value < 0:
            raise ValueError("x position cannot be negative.")
        if value > self.screen_width - self.width:
            raise ValueError(f"x position cannot be greater than screen width ({self.screen_width - self.width}).")
        self.x = value

    def set_y(self, value):
        # Ensures y position is within bounds (cannot exceed screen height minus fly height)
        if value < 0:
            raise ValueError("y position cannot be negative.")
        if value > self.screen_height - self.height:
            raise ValueError(f"y position cannot be greater than screen height ({self.screen_height - self.height}).")
        self.y = value
    
    def resize(self, width_scale, height_scale):
        """
        Resizes the object based on the scaling factors.
        """
        self.width *= width_scale
        self.height *= height_scale
        self.img = pygame.transform.scale(self.original_img, (int(self.width), int(self.height)))

    def reposition(self, width_scale, height_scale):
        """
        Repositions the object to maintain its relative position on the screen.
        """
        self.x *= width_scale
        self.y *= height_scale

    def draw(self, screen):
        """
        Draws the fly (used after resizing and reposition from screen resizing).
        """
        # Blit the image at the specified (x, y) coordinates
        screen.blit(self.img, (int(self.x), int(self.y)))
