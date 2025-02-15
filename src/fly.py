import random
import pygame
from constants import FLY_LEFT, FLY_RIGHT, FLY_SPEED

class Fly:
    def __init__(self, screen_width, screen_height, width, height, img_left=FLY_LEFT, img_right=FLY_RIGHT):
        """
        Initialize the fly with default size, movement, and position.

        Args:
            screen_width (int): Width of the screen the fly can move within.
            screen_height (int): Height of the screen the fly can move within.
            width (float): Width of the fly. 
            height (float): Height of the fly.
            img_left (pygame.Surface, optional): Image of the fly facing left. Defaults to FLY_LEFT.
            img_right (pygame.Surface, optional): Image of the fly facing right. Defaults to FLY_RIGHT.
        """
        self.width = width
        self.height = height
        self.speed = FLY_SPEED

        self.img_left = img_left
        self.img_right = img_right
        self.facing_left = True
        self.img = pygame.transform.scale(self.img_left, (int(self.width), int(self.height)))

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
        self.ensure_at_least_one_direction(movement, ["left", "right", "up", "down"])
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

    def ensure_at_least_one_direction(self, movement, directions):
        """
        Ensures that at least one movement direction is set to True in the given movement dictionary.

        Args:
            movement (dict): A dictionary containing movement directions (`left`, `right`, `up`, `down`) as keys,
                              with boolean values indicating whether each direction is active.
            directions (list): A list containing keys (`left`, `right`, `up`, `down`) that represent the movement directions 
                               to check and activate if necessary.
        """
        if not any(movement[dir] for dir in directions):
            movement[random.choice(directions)] = True

    def update_image(self):
        """
        Updates the fly's image based on its movement direction.
        """
        if self.movement["right"] and not self.facing_left:
            return  # Already facing right, no need to update

        if self.movement["right"]:
            self.img = pygame.transform.scale(self.img_right, (int(self.width), int(self.height)))
            self.facing_left = False
            return  # Prevents further updates in the same call

        if self.movement["left"] and self.facing_left:
            return  # Already facing left, no need to update

        if self.movement["left"]:
            self.img = pygame.transform.scale(self.img_left, (int(self.width), int(self.height)))
            self.facing_left = True

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
        self.ensure_at_least_one_direction(self.movement, ["left", "right", "up", "down"])

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

    def resize(self, new_width, new_height):
        """
        Updates the fly's size using the new width and height.

        Args:
            new_width (float): The new width of the fly.
            new_height (float): The new height of the fly.
        """
        self.width = new_width
        self.height = new_height
        self.update_image()
        
    def reposition(self, width_scale, height_scale):
        """
        Adjusts the fly's position after resizing to maintain relative placement.

        Args:
            width_scale (float): Factor to scale the x position.
            height_scale (float): Factor to scale the y position.
        """
        self.x = self.x * width_scale
        self.y = self.y * height_scale

    def draw(self, screen):
        """
        Renders the fly onto the given screen.

        Args:
            screen (pygame.Surface): The screen where the fly will be drawn.
        """
        screen.blit(self.img, (self.x, self.y))
