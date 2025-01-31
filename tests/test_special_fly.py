import pygame
import pytest
from special_fly import SpecialFly
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
    Fixture to create a SpecialFly instance with default size and random position.
    """
    pygame.init()  # Ensure pygame is initialized in the test environment
    return SpecialFly(screen_manager.width, screen_manager.height, width=30.0, height=30.0)

def test_initialization(fly, screen_manager):
    """
    Test that the Fly initializes with correct attributes.
    """
    assert fly.width == 30
    assert fly.height == 30
    assert fly.speed == 2
    assert 0 <= fly.x <= screen_manager.width - int(fly.width)
    assert 0 <= fly.y <= screen_manager.height - int(fly.height)

def test_set_valid_movement(fly):
    """
    Test that the Fly initializes with valid movement directions. 
    """
    assert not (fly.movement["left"] and fly.movement["right"])
    assert not (fly.movement["up"] and fly.movement["down"])
    assert any([fly.movement["left"], fly.movement["right"], fly.movement["up"], fly.movement["down"]])

def test_adjust_movement(fly, screen_manager):
    """
    Tests the adjust_movement method of the SpecialFly class. It ensures that the fly
    correctly changes its movement direction when it is near the center of the screen.
    """
    # Test when the fly is in the left half and moving left
    fly.x = screen_manager.width // 4  # Position near the left half
    fly.movement["left"] = True
    fly.adjust_movement(screen_manager.width, screen_manager.height)
    assert fly.movement["left"] is False
    assert fly.movement["right"] is True
    
    # Test when the fly is in the right half and moving right
    fly.x = 3 * screen_manager.width // 4  # Position near the right half
    fly.movement["right"] = True
    fly.adjust_movement(screen_manager.width, screen_manager.height)
    assert fly.movement["right"] is False
    assert fly.movement["left"] is True

def test_move(fly, screen_manager):
    """
    Test that the Fly moves correctly based on the movement directions.
    """
    fly.x = 250
    fly.y = 250
    
    fly.movement["left"] = False
    fly.movement["right"] = True
    fly.movement["up"] = True
    fly.movement["down"] = False
    
    fly.move(screen_manager.width, screen_manager.height)
    
    assert fly.x == 252
    assert fly.y == 248

def test_move_past_edge(fly, screen_manager):
    """
    Test that the Fly registers moving off edge correctly.
    """
    fly.x = 4 - fly.width
    fly.y = 250
    
    fly.movement["left"] = True
    fly.movement["right"] = False
    fly.movement["up"] = False
    fly.movement["down"] = False
    
    on_screen = fly.move(screen_manager.width, screen_manager.height)
    assert on_screen == True # barely on-screen
    
    on_screen = fly.move(screen_manager.width, screen_manager.height)
    assert fly.x == 0 - fly.width
    assert fly.y == 250
    assert on_screen == False # barely off-screen
      
def test_resize(fly):
    """
    Test that the Fly resizes correctly based on scaling factors.
    """
    initial_width = fly.width
    initial_height = fly.height
    width_scale = 2.0
    height_scale = 1.5
    fly.resize(initial_width * width_scale, initial_height * height_scale)
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
    initial_width = fly.width
    initial_height = fly.height
    width_scale = 2.0
    height_scale = 1.5

    # Resize and reposition
    fly.resize(initial_width * width_scale, initial_height * height_scale)
    fly.reposition(width_scale, height_scale)

    # Validate changes
    assert fly.width == 60
    assert fly.height == 45
    assert fly.x == initial_x * width_scale
    assert fly.y == initial_y * height_scale
