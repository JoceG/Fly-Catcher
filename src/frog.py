import pygame

class Frog:
    def __init__(self, x, y, frog_img, width=70.0, height=60.0, speed=5.0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.movement = {
            'left': False,
            'right': False,
            'down': False,
            'up': False
        }

        self.original_img = frog_img
        self.img = pygame.transform.scale(self.original_img, (int(self.width), int(self.height)))

    def move(self, screen_manager):
        """
        Updates the frog's position based on movement states
        """
        if self.movement['left'] and self.x > 0:
            self.x -= self.speed
        if self.movement['right'] and self.x + self.width < screen_manager.width: 
            self.x += self.speed
        if self.movement['down'] and self.y + self.height < screen_manager.height:
            self.y += self.speed
        if self.movement['up'] and self.y > 0:
            self.y -= self.speed

    def resize(self, width_scale, height_scale):
        """
        Resizes the frog based on the scaling factors.
        """
        self.width *= width_scale
        self.height *= height_scale
        self.img = pygame.transform.scale(self.original_img, (int(self.width), int(self.height)))

    def reposition(self, width_scale, height_scale):
        """
        Repositions the frog based on the scaling factors to maintain its relative position
        on the screen.
        """
        self.x *= width_scale
        self.y *= height_scale

    def draw(self, screen):
        """
        Draws the frog (used after resize and reposition from screen resizing).
        """
        # Blit the image at the specified (x, y) coordinates
        screen.blit(self.img, (int(self.x), int(self.y)))
