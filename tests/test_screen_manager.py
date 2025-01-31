import pytest
from screen_manager import ScreenManager
from constants import BACKGROUND_COLOR, INITIAL_SCREEN_WIDTH, INITIAL_SCREEN_HEIGHT

@pytest.fixture
def screen_manager():
    """
    Fixture to create a ScreenManager instance.
    """
    return ScreenManager()

def test_initialization(screen_manager):
    """
    Test that the screen manager initializes with the correct values.
    """
    assert screen_manager.width == INITIAL_SCREEN_WIDTH
    assert screen_manager.height == INITIAL_SCREEN_HEIGHT
    assert screen_manager.background_color == BACKGROUND_COLOR
    assert screen_manager.screen is not None

def test_resize(screen_manager):
    """
    Test that resizing works correctly.
    """
    screen_manager.resize(500, 500)
    assert screen_manager.width == 500
    assert screen_manager.height == 500
    assert screen_manager.previous_width == INITIAL_SCREEN_WIDTH
    assert screen_manager.previous_height == INITIAL_SCREEN_HEIGHT

def test_screen_clear(screen_manager):
    """
    Test that the screen clears with the correct color.
    """
    screen_manager.clear()
    assert screen_manager.screen.get_at((0, 0))[:3] == BACKGROUND_COLOR

def test_scaling_factors(screen_manager):
    """
    Test that scaling factos are calculated correctly.
    """
    screen_manager.resize(500, 500)
    width_scale, height_scale = screen_manager.get_scaling_factors()
    assert width_scale == 500 / INITIAL_SCREEN_WIDTH
    assert height_scale == 500 / INITIAL_SCREEN_HEIGHT
