import random
from fly import Fly

class SpecialFly(Fly):
    """
    A special fly that disappears when it moves off the screen.
    """
    def __init__(self, screen_width, screen_height, special_fly_img, width=30.0, height=30.0, speed=2):
        # Call the parent class (Fly) constructor to inherit its properties
        super().__init__(screen_width, screen_height, special_fly_img, width, height, speed)

        # Randomly spawn near the center of the screen
        self.x = random.randint(screen_width // 4, 3 * screen_width // 4)  # Random position in the middle third of the screen
        self.y = random.randint(screen_height // 4, 3 * screen_height // 4)  # Random position in the middle third of the screen

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

        # Check if the fly is past the left edge
        if self.x + self.width <= 0:  # The right edge of the fly is off the left side
            return False

        # Check if the fly is past the right edge
        if self.x >= self.screen_width:  # The left edge of the fly is off the right side
            return False

        # Check if the fly is past the top edge
        if self.y + self.height <= 0:  # The bottom edge of the fly is off the top side
            return False

        # Check if the fly is past the bottom edge
        if self.y >= self.screen_height:  # The top edge of the fly is off the bottom side
            return False

        return True
