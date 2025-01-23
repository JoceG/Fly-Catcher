import random
import pygame

class Fly:
    def __init__(self, screen_width, screen_height, fly_img, width=30.0, height=30.0, speed=2):
        """
        Initialize the fly with default size and color and random position.
        """
        # Dimensions of the fly
        self.width = width
        self.height = height

        # Speed of the fly
        self.speed = speed

        self.original_img = fly_img
        self.img = pygame.transform.scale(self.original_img, (int(self.width), int(self.height)))

        # Random initial position
        self.x = random.randint(0, int(screen_width) - int(self.width))
        self.y = random.randint(0, int(screen_height) - int(self.height))

        self.screen_width = screen_width  # Store screen width
        self.screen_height = screen_height  # Store screen height

        # Initialize random direction movement dictionary
        self.movement = {
            "left": random.choice([True, False]),
            "right": random.choice([True, False]),
            "up": random.choice([True, False]),
            "down": random.choice([True, False])
        }

        # Ensure no conflicting directions in self.movement
        self.set_valid_movement()

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

    def set_valid_movement(self):
        """
        Ensures no conflicting directions and at least one direction is True.
        """
        # Ensure no conflicting directions (both left-right cannot be True simultaneously)
        if self.movement["left"] and self.movement["right"]:
            direction = random.choice(["left", "right"])
            self.movement[direction] = False

        # Ensure no conflicting directions (both up-down cannot be True simultaneously)
        if self.movement["up"] and self.movement["down"]:
            direction = random.choice(["up", "down"])
            self.movement[direction] = False

        # Ensure at least one direction is true
        if not any([self.movement["left"], self.movement["right"], self.movement["up"], self.movement["down"]]):
            direction = random.choice(["left", "right", "up", "down"])
            self.movement[direction] = True

    def move(self):
        """
        Moves the fly and changes direction if it hits the edge.
        """
        if self.movement["left"]:
            self.x -= self.speed
        if self.movement["right"]:
            self.x += self.speed
        if self.movement["up"]:
            self.y -= self.speed
        if self.movement["down"]:
            self.y += self.speed

        # Check edges and change direction
        self.check_edges()

    def check_edges(self):
        """
        Checks if the fly is near an edge and changes its direction.
        """
        # Check if the fly is near the left edge
        if self.x <= 0: 
            self.movement["left"] = False
            self.movement["right"] = True

        # Check if the fly is near the right edge
        if self.x >= self.screen_width - self.width:
            self.movement["right"] = False
            self.movement["left"] = True

        # Check if the fly is near the top edge
        if self.y <= 0:
            self.movement["up"] = False
            self.movement["down"] = True

        # Check if the fly is near the bottom edge
        if self.y >= self.screen_height - self.height:
            self.movement["down"] = False
            self.movement["up"] = True

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
