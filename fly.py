import random
import pygame

class Fly:
    def __init__(self, screen_width, screen_height):
        # Dimensions of the fly
        self.width = 10
        self.height = 10

        # Random initial position
        self.x = random.randint(0, screen_width - self.width)
        self.y = random.randint(0, screen_width - self.height)

        self.color = (0, 0, 0) # Black color for the fly

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

        
