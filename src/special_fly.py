import random
from constants import SPECIAL_FLY_LEFT, SPECIAL_FLY_RIGHT
from fly import Fly

class SpecialFly(Fly):
    """
    A special fly that disappears when it moves off the screen.
    """

    """
    A special fly that disappears when it moves off the screen.

        Args:
            screen_width (int): Width of the screen the fly can move within.
            screen_height (int): Height of the screen the fly can move within.
            width (float, optional): Width of the special fly. Defaults to 30.0.
            height (float, optional): Height of the special fly. Defaults to 30.0.
            special_fly_img_left (pygame.Surface, optional): Image of the special fly facing left. Defaults to SPECIAL_FLY_LEFT.
            special_fly_img_right (pygame.Surface, optional): Image of the special fly facing right. Defaults to SPECIAL_FLY_RIGHT.
            speed (int, optional): Speed at which the special fly moves. Defaults to 2.
    """
    def __init__(self, screen_width, screen_height, width=30.0, height=30.0,
                 special_fly_img_left=SPECIAL_FLY_LEFT,
                 special_fly_img_right=SPECIAL_FLY_RIGHT, speed=2):
        # Call the parent class (Fly) constructor to inherit its properties
        super().__init__(screen_width, screen_height, width, height,
                         special_fly_img_left, special_fly_img_right, speed)

        # Randomly spawn near the center of the screen
        self.x = random.randint(screen_width // 4, 3 * screen_width // 4)  # Random position from the first to the third quarter of the screen width
        self.y = random.randint(screen_height // 4, 3 * screen_height // 4)  # Random position from the first to the third quarter of the screen height

        # Adjust initial movement direction after random position is set
        self.adjust_movement(screen_width, screen_height)

    def adjust_movement(self, screen_width, screen_height):
        """
        Adjusts the movement direction of the fly if it's too close to the screen edge.

        Args:
            screen_width (int): The width of the screen, used to check if the fly is too close to the right or left edge.
            screen_height (int): The height of the screen, used to check if the fly is too close to the top or bottom edge.
        """
        # If the fly is near the left edge and moving left, change direction to right
        if self.x <= 0 and self.movement["left"]:
            self.movement["left"] = False
            self.movement["right"] = True

        # If the fly is near the right edge and moving right, change direction to left
        if self.x + self.width >= screen_width and self.movement["right"]:
            self.movement["right"] = False
            self.movement["left"] = True

        # If the fly is near the top edge and moving up, change direction to down
        if self.y <= 0 and self.movement["up"]:
            self.movement["up"] = False
            self.movement["down"] = True

        # If the fly is near the bottom edge and moving down, change direction to up
        if self.y + self.height >= screen_height and self.movement["down"]:
            self.movement["down"] = False
            self.movement["up"] = True
    
    def move(self, screen_width, screen_height):
        """
        Moves the special fly and returns a boolean indicating whether the fly is still on the screen.
        The special fly will be removed if it moves off the screen.

        Args:
            screen_width (int): The width of the screen, used to check if the fly has moved off the screen.
            screen_height (int): The height of the screen, used to check if the fly has moved off the screen.

        Returns:
            bool: True if the fly is still on the screen, False if it has moved off the screen.
        """
        # Update the fly's position based on its movement direction
        self.update_position()

        # Check if the special fly is off the screen
        if not self.is_on_screen(screen_width, screen_height):
            return False

        return True

    def update_position(self):
        """
        Update the position of the special fly based on its current movement direction.
        """
        if self.movement["left"]:
            self.x -= self.speed
        elif self.movement["right"]:
            self.x += self.speed
            
        if self.movement["up"]:
            self.y -= self.speed
        elif self.movement["down"]:
            self.y += self.speed

    def is_on_screen(self, screen_width, screen_height):
        """
        Check if the special fly is still within the screen boundaries.

        Args:
            screen_width (int): The width of the screen, used to check if the fly is within the screen's left and right boundaries.
            screen_height (int): The height of the screen, used to check if the fly is within the screen's top and bottom boundaries.

        Returns:
            bool: True if the fly is within the screen boundaries, False if it is outside the screen.
        """
        if self.x + self.width <= 0 or self.x >= screen_width: # Left or Right boundary
            return False
        
        if self.y + self.height <= 0 or self.y >= screen_height: # Top or Bottom boundary
            return False
        
        return True
