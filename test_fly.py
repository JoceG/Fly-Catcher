import pygame
import pytest
from fly import Fly

@pytest.fixture
def fly():
    """
    Fixture to create a Fly instance with default size and random position.
    """
    pygame.init()  # Ensure pygame is initialized in the test environment
    fly_img = pygame.image.load('fly.png') # Load the fly image
    return Fly(screen_width=500, screen_height=500, fly_img=fly_img)

def test_initialization(fly):
    """
    Test that the Fly initializes with correct attributes.
    """
    assert fly.width == 30
    assert fly.height == 30
    assert 0 <= fly.x <= 500 - fly.width
    assert 0 <= fly.y <= 500 - fly.height
    assert fly.color == (0, 0, 0)

def test_resize(fly):
    """
    Test that the Fly resizes correctly based on scaling factors.
    """
    initial_width = fly.width
    initial_height = fly.height
    width_scale = 2.0
    height_scale = 1.5
    fly.resize(width_scale, height_scale)
    assert fly.width == initial_width * width_scale
    assert fly.height == initial_height * height_scale

def test_reposition(fly):
    """
    Test that the Fly repositions correctly based on scaling factors.
    """
    initial_x = fly.x
    initial_y = fly.y
    width_scale = 2.0
    height_scale = 1.5
    fly.reposition(width_scale, height_scale)
    assert fly.x == initial_x * width_scale
    assert fly.y == initial_y * height_scale

def test_resize_and_reposition(fly):
    """
    Test that resizing and repositioning work together as expected.
    """
    initial_x = fly.x
    initial_y = fly.y
    width_scale = 2.0
    height_scale = 1.5

    # Resize and reposition
    fly.resize(width_scale, height_scale)
    fly.reposition(width_scale, height_scale)

    # Validate changes
    assert fly.width == 60
    assert fly.height == 45
    assert fly.x == initial_x * width_scale
    assert fly.y == initial_y * height_scale
