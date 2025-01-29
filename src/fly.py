import random
import pygame
from constants import FLY_LEFT, FLY_RIGHT

class Fly:
    def __init__(self, screen_width, screen_height, fly_img_left=FLY_LEFT, fly_img_right=FLY_RIGHT, width=30.0, height=30.0, speed=2):
        """
        Initialize the fly with default size and color and random position.
        """
        self.original_img_left = fly_img_left
        self.original_img_right = fly_img_right
        self.img = pygame.transform.scale(self.original_img_left, (int(self.width), int(self.height)))
        self.facing_left = True
        
        # Dimensions of the fly
        self.width = width
        self.height = height

        # Speed of the fly
        self.speed = speed

        # Random initial position
        self.x = random.randint(0, int(screen_width) - int(width))
        self.y = random.randint(0, int(screen_height) - int(height))

        # Initialize random direction movement dictionary
        self.movement = {
            "left": random.choice([True, False]),
            "right": random.choice([True, False]),
            "up": random.choice([True, False]),
            "down": random.choice([True, False])
        }

        # Ensure no conflicting directions in self.movement
        self.set_valid_movement()
        self.set_fly_image()

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

    def set_fly_image(self):
        """
        Ensures the correct fly image is used (left-facing vs right-facing).
        """
        if self.movement["left"]:
            self.img = pygame.transform.scale(self.original_img_left, (int(self.width), int(self.height)))
            self.facing_left = True  
        elif self.movement["right"]:
            self.img = pygame.transform.scale(self.original_img_right, (int(self.width), int(self.height)))
            self.facing_left = False
        
    def check_edges(self, screen_width, screen_height):
        """
        Checks if the fly is near an edge and changes its direction.
        """
        # Check if the fly is near the left edge
        if self.x <= 0:
            self.movement["left"] = False
            self.movement["right"] = random.choice([True, False])
            self.movement["up"] = random.choice([True, False])
            self.movement["down"] = random.choice([True, False])

            # Ensure no conflicting directions (both up-down cannot be True simultaneously)
            if self.movement["up"] and self.movement["down"]:
                direction = random.choice(["up", "down"])
                self.movement[direction] = False

             # Ensure at least one direction is true
            if not any([self.movement["right"], self.movement["up"], self.movement["down"]]):
                direction = random.choice(["right", "up", "down"])
                self.movement[direction] = True

        # Check if the fly is near the right edge
        if self.x >= screen_width - self.width:
            self.movement["left"] = random.choice([True, False])
            self.movement["right"] = False
            self.movement["up"] = random.choice([True, False])
            self.movement["down"] = random.choice([True, False])

            # Ensure no conflicting directions (both up-down cannot be True simultaneously)
            if self.movement["up"] and self.movement["down"]:
                direction = random.choice(["up", "down"])
                self.movement[direction] = False

             # Ensure at least one direction is true
            if not any([self.movement["left"], self.movement["up"], self.movement["down"]]):
                direction = random.choice(["left", "up", "down"])
                self.movement[direction] = True

        # Check if the fly is near the top edge
        if self.y <= 0:
            self.movement["left"] = random.choice([True, False])
            self.movement["right"] = random.choice([True, False])
            self.movement["up"] = False
            self.movement["down"] = random.choice([True, False])

            # Ensure no conflicting directions (both up-down cannot be True simultaneously)
            if self.movement["left"] and self.movement["right"]:
                direction = random.choice(["left", "right"])
                self.movement[direction] = False

             # Ensure at least one direction is true
            if not any([self.movement["left"], self.movement["right"], self.movement["down"]]):
                direction = random.choice(["left", "right", "down"])
                self.movement[direction] = True

        # Check if the fly is near the bottom edge
        if self.y >= screen_height - self.height:
            self.movement["left"] = random.choice([True, False])
            self.movement["right"] = random.choice([True, False])
            self.movement["up"] = random.choice([True, False])
            self.movement["down"] = False

            # Ensure no conflicting directions (both up-down cannot be True simultaneously)
            if self.movement["left"] and self.movement["right"]:
                direction = random.choice(["left", "right"])
                self.movement[direction] = False

             # Ensure at least one direction is true
            if not any([self.movement["left"], self.movement["right"], self.movement["up"]]):
                direction = random.choice(["left", "right", "up"])
                self.movement[direction] = True

    def move(self, screen_width, screen_height):
        """
        Moves the fly and changes direction if it hits the edge.
        """
        if self.movement["left"]:
            self.x -= self.speed  
        elif self.movement["right"]:
            self.x += self.speed
            
        if self.movement["up"]:
            self.y -= self.speed 
        elif self.movement["down"]:
            self.y += self.speed

        # Check edges and change direction
        self.check_edges(screen_width, screen_height)

        # Set the correct fly image
        self.set_fly_image()

    def resize(self, width_scale, height_scale):
        """
        Resizes the object based on the scaling factors.
        """
        self.width *= width_scale
        self.height *= height_scale

        if self.facing_left:
            self.img = pygame.transform.scale(self.original_img_left, (int(self.width), int(self.height)))
        else:
            self.img = pygame.transform.scale(self.original_img_right, (int(self.width), int(self.height)))

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
