import pygame
import pytest
from constants import GAME_DURATION, INITIAL_FLY_COUNT
from frog import Frog
from game_state import GameState
from screen_manager import ScreenManager

@pytest.fixture
def game_state():
    """
    Fixture to create a GameState instance.
    """
    return GameState()

@pytest.fixture
def frog(screen_manager):
    """
    Fixture to create a Frog instance.
    """
    pygame.init()  # Ensure pygame is initialized in the test environment
    x = screen_manager.width / 2
    y = screen_manager.height / 2
    width = screen_manager.width / 10
    height = screen_manager.width / 12
    return Frog(x, y, width, height)

@pytest.fixture
def screen_manager():
    """
    Fixture to create a ScreenManager instance.
    """
    return ScreenManager()

def test_initialization(game_state):
    """
    Test that the game state initializes with the correct values.
    """
    assert game_state.countdown_time == 0
    assert game_state.frog == None
    assert game_state.flies == []
    assert game_state.score == 0
    assert game_state.score_popups == []
    assert game_state.fly_width == 0
    assert game_state.fly_height == 0

def test_reset(game_state, screen_manager, frog):
    """
    Test that reset works correctly.
    """
    game_state.reset(screen_manager.width, screen_manager.height)
    assert game_state.countdown_time == GAME_DURATION
    assert game_state.score == 0
    assert game_state.score_popups == []
    assert game_state.fly_width == screen_manager.width / 25
    assert game_state.fly_height == screen_manager.width / 25

    assert game_state.frog.x == frog.x
    assert game_state.frog.y == frog.y
    assert game_state.frog.width == frog.width
    assert game_state.frog.height == frog.height
    assert len(game_state.flies) == INITIAL_FLY_COUNT
