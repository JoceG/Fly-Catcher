import pytest
from fly import Fly
from main import check_collision

@pytest.fixture
def frog():
    """
    Fixture to provide a common set of frog attributes
    """
    return {
        "x": 50,
        "y": 50,
        "width": 30,
        "height": 30
    }

@pytest.fixture
def fly():
    """
    Fixture to create a Fly instance with default size and random position.
    """
    return Fly(screen_width=500, screen_height=500, width=10, height=10, background_color = (0, 0, 0))

def test_collision_occurs(frog, fly):
    """
    Test that a collision is correctly detected when the frog and the fly overlap.
    """
    # Set fly position to collide with the frog
    fly.x, fly.y = 60, 60
    
    assert check_collision(frog["x"], frog["y"], frog["width"], frog["height"], fly) is True

def test_no_collision_occurs(frog, fly):
    """
    Test that no collision is detected when the frog and the fly do not overlap.
    """
    # Set fly position far away from the frog
    fly.x, fly.y = 100, 100

    assert check_collision(frog["x"], frog["y"], frog["width"], frog["height"], fly) is False
