import pygame
import pytest
from frog import Frog
from screen_manager import ScreenManager

@pytest.fixture
def screen_manager():
    """
    Fixture to create a ScreenManager instance.
    """
    return ScreenManager()

@pytest.fixture
def frog():
    """
    Fixture to create a Frog instance.
    """
    pygame.init()  # Ensure pygame is initialized in the test environment
    return Frog(x=400.0, y=250.0, width=70.0, height=60.0)

def test_initialization(frog):
    """
    Test that the Frog initializes with correct attributes.
    """
    assert frog.x == 400
    assert frog.y == 250
    assert frog.width == 70
    assert frog.height == 60
    assert frog.speed == 5
    assert frog.movement == {
        'left': False,
        'right': False,
        'down': False,
        'up': False
    }

def test_move_left_updates_frog_position(frog, screen_manager):
    """
    Test that the move function correctly moves the Frog to the left.
    """
    initial_x = frog.x
    frog.movement['left'] = True
    frog.move(screen_manager.width, screen_manager.height)
    assert frog.x == initial_x - frog.speed

def test_move_right_updates_frog_position(frog, screen_manager):
    """
    Test that the move function correctly moves the Frog to the right.
    """
    initial_x = frog.x
    frog.movement['right'] = True
    frog.move(screen_manager.width, screen_manager.height)
    assert frog.x == initial_x + frog.speed

def test_move_up_updates_frog_position(frog, screen_manager):
    """
    Test that the move function correctly moves the Frog up.
    """
    initial_y = frog.y
    frog.movement['up'] = True
    frog.move(screen_manager.width, screen_manager.height)
    assert frog.y == initial_y - frog.speed

def test_move_down_updates_frog_position(frog, screen_manager):
    """
    Test that the move function correctly moves the Frog down.
    """
    initial_y = frog.y
    frog.movement['down'] = True
    frog.move(screen_manager.width, screen_manager.height)
    assert frog.y == initial_y + frog.speed

def test_move_left_at_boundary(frog, screen_manager):
    """
    Test that the Frog does not move left beyond the screen's left boundary.
    """
    frog.x = 0
    frog.movement['left'] = True
    frog.move(screen_manager.width, screen_manager.height)
    assert frog.x == 0  # Should not go past the left edge

def test_move_right_at_boundary(frog, screen_manager):
    """
    Test that the Frog does not move right beyond the screen's right boundary.
    """
    frog.x = screen_manager.width - frog.width
    frog.movement['right'] = True
    frog.move(screen_manager.width, screen_manager.height)
    assert frog.x == screen_manager.width - frog.width  # Should not go past the right edge

def test_move_up_at_boundary(frog, screen_manager):
    """
    Test that the Frog does not move up beyond the screen's top boundary.
    """
    frog.y = 0
    frog.movement['up'] = True
    frog.move(screen_manager.width, screen_manager.height)
    assert frog.y == 0  # Should not go past the top edge

def test_move_down_at_boundary(frog, screen_manager):
    """
    Test that the Frog does not move down beyond the screen's bottom boundary.
    """
    frog.y = screen_manager.height - frog.height
    frog.movement['down'] = True
    frog.move(screen_manager.width, screen_manager.height)
    assert frog.y == screen_manager.height - frog.height  # Should not go past the bottom edge

def test_resize(frog):
    """
    Test that the Frog resizes correctly based on scaling factors.
    """
    initial_width = frog.width
    initial_height = frog.height
    frog.resize(2.0, 1.5)
    assert frog.width == initial_width * 2.0
    assert frog.height == initial_height * 1.5

def test_resize_with_no_change(frog):
    """
    Test that resizing with a factor of 1 does not change the Frog's size.
    """
    initial_width = frog.width
    initial_height = frog.height
    frog.resize(1.0, 1.0)
    assert frog.width == initial_width
    assert frog.height == initial_height

def test_reposition(frog):
    """
    Test that the Frog repositions correctly based on scaling factors.
    """
    initial_x = frog.x
    initial_y = frog.y
    frog.reposition(2.0, 1.5)
    assert frog.x == initial_x * 2.0
    assert frog.y == initial_y * 1.5

def test_reposition_with_no_change(frog):
    """
    Test that repositioning with a factor of 1 does not change the Frog's position.
    """
    initial_x = frog.x
    initial_y = frog.y
    frog.reposition(1.0, 1.0)
    assert frog.x == initial_x
    assert frog.y == initial_y
