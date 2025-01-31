# Fly-Catcher
A fun and interactive Python game where a frog catches flies! Test your reflexes and aim as you help the frog gobble up flies using the arrow keys.

## Description
Fly Catcher is a simple yet engaging game built with Python and Pygame. The game features a frog that moves using the **arrow keys** (up, down, left, right) to catch flies. Players score points by catching as many flies as possible. It's a perfect project to enjoy and showcase the basics of game development in Python.

## Installation
To set up the game on your local machine:

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/JoceG/Fly-Catcher.git

2. Navigate to the project directory:
   ```bash
   cd fly-catcher
   
3. Install the required dependencies. Make sure you have Python installed on your system:
   ```bash
   pip install pygame

4. Run the game:
   ```bash
   python main.py

## Running Tests
To run the tests for Fly Catcher:

1. Install pytest if you haven’t already:
   ```bash
   pip install pytest
2. Navigate to the tests folder and run the tests:
   ```bash
   cd Fly-Catcher/tests
   ```
   ```bash
   pytest

## Usage
- Use the arrow keys (up, down, left, right) to move the frog.
- Catch as many flies as you can to increase your score.
- Regular flies add 1 point to your score.
- Gold flies (special flies) add 5 seconds to the timer.
- The game lasts for 2 minutes. Once the timer runs out, the game is over.

## Future Work
Here are some planned features and improvements for Fly Catcher:

- **Error Handling**: Implement error handling for edge cases or unexpected inputs.
- **Unit Tests**: Expand unit testing coverage to improve robustness.
- **Obstacle Mechanics**: Introduce obstacles that the frog needs to avoid while catching flies.
- **Difficulty Levels**: Add different difficulty levels (easy, medium, hard) to enhance gameplay.
- **High Score Tracking**: Add a system to track and store high scores locally or online.
- **Multiplayer Mode**: Allow two players to compete to catch the most flies.
- **Sound Effects**: Incorporate sound effects for catching flies and background music.
