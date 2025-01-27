import pygame
import pytest
from constants import FROG
from frog import Frog
from screen_manager import ScreenManager

@pytest.fixture
def screen_manager():
    """
    Fixture to create a ScreenManager instance.
    """
    return ScreenManager(width=800, height=600, background_color=(255, 255, 255))

@pytest.fixture
def frog():
    """
    Fixture to create a Frog instance with default values.
    """
    pygame.init()  # Ensure pygame is initialized in the test environment
    return Frog(x=250.0, y=250.0, frog_img=FROG)

def test_initialization(frog):
    """
    Test that the Frog initializes with correct attributes.
    """
    assert frog.x == 250.0
    assert frog.y == 250.0
    assert frog.width == 70.0
    assert frog.height == 60.0
    assert frog.speed == 5.0
    assert frog.movement == {
        'left': False,
        'right': False,
        'down': False,
        'up': False
    }

def test_move_left(frog, screen_manager):
    """
    Test that the move function correctly moves the Frog to the left.
    """
    initial_x = frog.x
    frog.movement['left'] = True
    frog.move(screen_manager)
    assert frog.x == initial_x - frog.speed

def test_move_right(frog, screen_manager):
    """
    Test that the move function correctly moves the Frog to the right.
    """
    initial_x = frog.x
    frog.movement['right'] = True
    frog.move(screen_manager)
    assert frog.x == initial_x + frog.speed

def test_move_down(frog, screen_manager):
    """
    Test that the move function correctly moves the Frog down.
    """
    initial_y = frog.y
    frog.movement['down'] = True
    frog.move(screen_manager)
    assert frog.y == initial_y + frog.speed

def test_move_up(frog, screen_manager):
    """
    Test that the move function correctly moves the Frog up.
    """
    initial_y = frog.y
    frog.movement['up'] = True
    frog.move(screen_manager)
    assert frog.y == initial_y - frog.speed

def test_resize(frog):
    """
    Test that the Frog resizes correctly based on scaling factors.
    """
    initial_width = frog.width
    initial_height = frog.height
    width_scale = 2.0
    height_scale = 1.5
    frog.resize(width_scale, height_scale)
    assert frog.width == initial_width * width_scale
    assert frog.height == initial_height * height_scale

def test_reposition(frog):
    """
    Test that the Frog repositions correctly based on scaling factors.
    """
    initial_x = frog.x
    initial_y = frog.y
    width_scale = 2.0
    height_scale = 1.5
    frog.reposition(width_scale, height_scale)
    assert frog.x == initial_x * width_scale
    assert frog.y == initial_y * height_scale

def test_resize_and_reposition(frog):
    """
    Test that resizing and repositioning work together as expected.
    """
    initial_x = frog.x
    initial_y = frog.y
    width_scale = 2.0
    height_scale = 1.5

    # Resize and reposition
    frog.resize(width_scale, height_scale)
    frog.reposition(width_scale, height_scale)

    # Validate changes
    assert frog.width == 140
    assert frog.height == 90
    assert frog.x == initial_x * width_scale
    assert frog.y == initial_y * height_scale
