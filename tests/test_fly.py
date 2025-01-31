import pygame
import pytest
from constants import FLY_LEFT, FLY_RIGHT
from fly import Fly
from screen_manager import ScreenManager

@pytest.fixture
def screen_manager():
    """
    Fixture to create a ScreenManager instance.
    """
    return ScreenManager()

@pytest.fixture
def fly(screen_manager):
    """
    Fixture to create a Fly instance with random position.
    """
    pygame.init()  # Ensure pygame is initialized in the test environment
    return Fly(screen_manager.width, screen_manager.height, width=30.0, height=30.0)

def test_initialization(fly, screen_manager):
    """
    Test that the Fly initializes with correct attributes.
    """
    assert fly.width == 30
    assert fly.height == 30
    assert fly.speed == 2

    assert fly.img_left == FLY_LEFT
    assert fly.img_right == FLY_RIGHT
    
    assert 0 <= fly.x <= screen_manager.width - fly.width
    assert 0 <= fly.y <= screen_manager.height - fly.height

def test_generate_valid_movement(fly):
    """
    Test that the Fly initializes with valid movement directions. 
    """
    assert not (fly.movement["left"] and fly.movement["right"])
    assert not (fly.movement["up"] and fly.movement["down"])
    assert any(fly.movement.values())

def surfaces_are_equal(surface1, surface2):
    """
    Helper function to compare two Pygame surfaces.
    """
    return pygame.image.tostring(surface1, "RGBA") == pygame.image.tostring(surface2, "RGBA")

def test_update_image(fly):
    """
    Test that the fly's image updates correctly based on movement.
    """
    fly.movement["right"] = True
    fly.movement["left"] = False
    fly.update_image()
    assert fly.facing_left == False  # Should be facing right now
    assert surfaces_are_equal(fly.img, pygame.transform.scale(fly.img_right, (int(fly.width), int(fly.height))))
    
    fly.movement["left"] = True
    fly.movement["right"] = False
    fly.update_image()
    assert fly.facing_left == True  # Should be facing left now
    assert surfaces_are_equal(fly.img, pygame.transform.scale(fly.img_left, (int(fly.width), int(fly.height))))

def test_move(fly, screen_manager):
    """
    Test that the Fly moves correctly based on the movement directions.
    """
    fly.x = 250
    fly.y = 250
    
    fly.movement = {"left": False, "right": True, "up": False, "down": False}
    fly.move(screen_manager.width, screen_manager.height)
    assert fly.x == 250 + fly.speed

    fly.movement = {"left": True, "right": False, "up": False, "down": False}
    fly.move(screen_manager.width, screen_manager.height)
    assert fly.x == 250

    fly.movement = {"left": False, "right": False, "up": True, "down": False}
    fly.move(screen_manager.width, screen_manager.height)
    assert fly.y == 250 - fly.speed

def test_check_edges(fly, screen_manager):
    """
    Test that the fly correctly handles screen edge collisions.
    """
    fly.x = 0  # Left edge
    fly.movement["left"] = True
    fly.check_edges(screen_manager.width, screen_manager.height)
    assert not fly.movement["left"]
    assert any([fly.movement["right"], fly.movement["up"], fly.movement["down"]])

    fly.x = screen_manager.width - fly.width  # Right edge
    fly.movement["right"] = True
    fly.check_edges(screen_manager.width, screen_manager.height)
    assert not fly.movement["right"]
    assert any([fly.movement["left"], fly.movement["up"], fly.movement["down"]])
    
def test_resize(fly):
    """
    Test that the resize function updates the fly's dimensions.
    """
    fly.resize(50, 50)
    assert fly.width == 50
    assert fly.height == 50

def test_reposition(fly):
    """
    Test that the reposition function scales the fly's position correctly.
    """
    fly.x = 100
    fly.y = 100
    fly.reposition(1.5, 2.0)
    assert fly.x == 150
    assert fly.y == 200
