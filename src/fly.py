import random
import pygame
from constants import FLY_LEFT, FLY_RIGHT, FLY_SPEED

class Fly:
    def __init__(self, screen_width, screen_height, width, height):
        """
        Initialize the fly with default size, movement, and position.

        Args:
            screen_width (int): Width of the screen the fly can move within.
            screen_height (int): Height of the screen the fly can move within.
            width (float, optional): Width of the fly. Defaults to 30.0.
            height (float, optional): Height of the fly. Defaults to 30.0.
            fly_img_left (pygame.Surface, optional): Image of the fly facing left. Defaults to FLY_LEFT.
            fly_img_right (pygame.Surface, optional): Image of the fly facing right. Defaults to FLY_RIGHT.
            speed (int, optional): Speed at which the fly moves. Defaults to 2.
        """
        self.width = width
        self.height = height
        self.speed = FLY_SPEED

        self.original_img_left = FLY_LEFT
        self.original_img_right = FLY_RIGHT
        self.facing_left = True
        self.img = pygame.transform.scale(self.original_img_left, (int(self.width), int(self.height)))

        self.x = random.randint(0, int(screen_width) - int(width))
        self.y = random.randint(0, int(screen_height) - int(height))

        self.movement = self.generate_valid_movement()
        self.update_image()

    def generate_valid_movement(self):
        """
        Generates a valid initial movement direction ensuring no conflicts.

        Returns:
            dict: A dictionary containing movement directions (`left`, `right`, `up`, `down`) set to True or False.
        """
        movement = {
            "left": random.choice([True, False]),
            "right": random.choice([True, False]),
            "up": random.choice([True, False]),
            "down": random.choice([True, False])
        }
        self.resolve_movement_conflicts(movement)
        return movement

    def resolve_movement_conflicts(self, movement):
        """
        Ensures that conflicting opposite directions (left/right or up/down) are not both set to True.

        Args:
            movement (dict): A dictionary containing movement directions (`left`, `right`, `up`, `down`) as keys, with boolean values indicating whether each direction is active.
        """
        opposite_pairs = [("left", "right"), ("up", "down")]

        for dir1, dir2 in opposite_pairs:
            if movement[dir1] and movement[dir2]:
                movement[random.choice([dir1, dir2])] = False

    def ensure_at_least_one_direction(self, directions):
        """
        Ensures that at least one movement direction is True.

        Args:
            directions (dict): A dictionary containing movement directions (`left`, `right`, `up`, `down`) as keys.
        """
        if not any(self.movement[dir] for dir in directions):
            self.movement[random.choice(directions)] = True

    def update_image(self):
        """
        Updates the fly's image based on its movement direction.
        """
        if self.facing_left and self.movement["right"]:
            self.img = pygame.transform.scale(self.original_img_right, (self.width, self.height))
            self.facing_left = False
        elif self.facing_left:
            self.img = pygame.transform.scale(self.original_img_left, (self.width, self.height))

        if not self.facing_left and self.movement["left"]:
            self.img = pygame.transform.scale(self.original_img_left, (self.width, self.height))
            self.facing_left = True
        elif not self.facing_left:
            self.img = pygame.transform.scale(self.original_img_right, (self.width, self.height))

    def check_edges(self, screen_width, screen_height):
        """
        Checks if the fly has hit the screen boundaries and adjusts its movement accordingly.

        Args:
            screen_width (int): The width of the screen to check if the fly goes beyond the right or left edges.
            screen_height (int): The height of the screen to check if the fly goes beyond the top or bottom edges.
        """
        if self.x <= 0:
            self.handle_edge_collision("left", ["right", "up", "down"])
        elif self.x >= screen_width - self.width:
            self.handle_edge_collision("right", ["left", "up", "down"])
            
        if self.y <= 0:
            self.handle_edge_collision("up", ["left", "right", "down"])
        elif self.y >= screen_height - self.height:
            self.handle_edge_collision("down", ["left", "right", "up"])

    def handle_edge_collision(self, edge, possible_directions):
        """
        Handles movement adjustments when the fly collides with the screen boundaries.

        Args:
            edge (str): The direction where the collision occurred (e.g., "left", "right").
            possible_directions (list): List of directions the fly can move towards.
        """
        self.movement[edge] = False
        for direction in possible_directions:
            self.movement[direction] = random.choice([True, False])
        self.resolve_movement_conflicts(self.movement)

    def move(self, screen_width, screen_height):
        """
        Moves the fly based on its current movement direction and prevents out-of-bounds movement.

        Args:
            screen_width (int): The width of the screen to ensure the fly doesn't move off the right or left edges.
            screen_height (int): The height of the screen to ensure the fly doesn't move off the top or bottom edges.
        """
        if self.movement["left"]:
            self.x = max(0, self.x - self.speed)   
        elif self.movement["right"]:
            self.x = min(screen_width - self.width, self.x + self.speed)
            
        if self.movement["up"]:
            self.y = max(0, self.y - self.speed)  
        elif self.movement["down"]:
            self.y = min(screen_height - self.height, self.y + self.speed)

        self.check_edges(screen_width, screen_height)
        self.update_image()

    def resize(self, width_scale, height_scale):
        """
        Scales the fly's size by the given scale factors.

        Args:
            width_scale (float): Factor to scale the width.
            height_scale (float): Factor to scale the height.
        """
        self.width = int(self.width * width_scale)
        self.height = int(self.height * height_scale)
        self.update_image()
        
    def reposition(self, width_scale, height_scale):
        """
        Adjusts the fly's position after resizing to maintain relative placement.

        Args:
            width_scale (float): Factor to scale the x position.
            height_scale (float): Factor to scale the y position.
        """
        self.x = int(self.x * width_scale)
        self.y = int(self.y * height_scale)

    def draw(self, screen):
        """
        Renders the fly onto the given screen.

        Args:
            screen (pygame.Surface): The screen where the fly will be drawn.
        """
        screen.blit(self.img, (self.x, self.y))
