import pygame
import pytest
from frog import Frog
from fly import Fly
from main import check_collision

@pytest.fixture(scope="session", autouse=True)
def init_pygame():
    """
    Initialize Pygame once for the entire test session.
    """
    pygame.init()
    yield
    pygame.quit()  # Clean up after tests

@pytest.fixture
def frog():
    """
    Fixture to create a Frog instance with default values.
    """
    frog_img = pygame.image.load('frog.png') # Load the frog image
    return Frog(x=250.0, y=250.0, frog_img=frog_img)

@pytest.fixture
def fly():
    """
    Fixture to create a Fly instance with default size and random position.
    """
    fly_img = pygame.image.load('fly.png') # Load the fly image
    return Fly(screen_width=500, screen_height=500, fly_img=fly_img, width=10, height=10, background_color = (0, 0, 0))

def test_collision_occurs(frog, fly):
    """
    Test that a collision is correctly detected when the frog and the fly overlap.
    """
    # Set fly position to collide with the frog
    fly.x, fly.y = 250.0, 250.0
    
    assert check_collision(frog, fly) is True

def test_no_collision_occurs(frog, fly):
    """
    Test that no collision is detected when the frog and the fly do not overlap.
    """
    # Set fly position far away from the frog
    fly.x, fly.y = 100, 100

    assert check_collision(frog, fly) is False
