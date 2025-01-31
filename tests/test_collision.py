import pygame
import pytest
from frog import Frog
from fly import Fly
from game_logic import check_collision

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
    return Frog(x=250.0, y=250.0, width=70.0, height=60.0)

@pytest.fixture
def fly():
    """
    Fixture to create a Fly instance with default size and random position.
    """
    return Fly(screen_width=500, screen_height=500, width=30.0, height=30.0)

def test_collision_occurs(frog, fly):
    """
    Test that a collision is correctly detected when the frog and the fly overlap.
    """
    # Set fly position to collide with the frog
    fly.x, fly.y = 250, 250
    
    assert check_collision(frog, fly) is True

def test_no_collision_occurs(frog, fly):
    """
    Test that no collision is detected when the frog and the fly do not overlap.
    """
    # Set fly position far away from the frog
    fly.x, fly.y = 100, 100

    assert check_collision(frog, fly) is False
