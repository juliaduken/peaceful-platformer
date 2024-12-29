# Peaceful Platformer

Welcome to the *Peaceful Platformer* game! This README will guide you through setting up and running the game locally, as well as explain the functionality of the different files.

## Getting Started

### Prerequisites
Make sure you have the following installed:
- Python 3.9 or higher
- pip (Python package manager)
- Git
- Visual Studio Code (recommended IDE)

### Cloning the Repository
1. Open a terminal and navigate to the directory where you'd like to clone the repository.
2. Run the following command to clone the repository:

```
git clone https://github.com/yourusername/peaceful-platformer.git
cd peaceful-platformer
```

### Setting Up the Environment
1. Open the project in Visual Studio Code.
2. Create a virtual environment by running the following in the terminal: ```python -m venv .venv```
3. Activate the virtual environment:
- *On Windows:* ```.venv\Scripts\activate```
- *On macOS/Linux:* ```source .venv/bin/activate```
4. Install the required dependencies by running the following in the terminal: 
```pip install -r requirements.txt```

### Running the Game
To run the game, run ```python game.py``` in your terminal. Press the start button, and enjoy!

## How to Play
In *Peaceful Platformer*, your goal is to explore the game world, collect treasures, and score as many points as possible while navigating platforms and climbing ladders. Here’s everything you need to know to play:
### Controls
*Movement*
Left Arrow (←): Move left.
Right Arrow (→): Move right.
*Jumping*
Spacebar: Jump. You can also combine this with the arrow keys for directional jumps.
*Climbing Ladders*
Up Arrow (↑): Climb up a ladder.
Down Arrow (↓): Climb down or drop through a platform.
*Interacting with Chests*
E Key: Open a nearby chest to collect treasure and score points.

### Scoring System
*Opening Chests:* Each chest you open awards 10 points.

## File Descriptions
### Core Game Files
*game.py:* Contains the main game loop, initializes the game window, and manages updates and rendering for all components​
*settings.py:* Defines global constants such as screen dimensions, colors, player settings, and asset paths​

### Gameplay Components
*player.py:* Handles the player's behavior, including movement, jumping, climbing ladders, and interacting with chests​
*platform.py:* Represents platforms in the game, including their position and collision detection​
*ladder.py:* Represents ladders, allowing the player to climb between platforms​
*chest.py:* Represents treasure chests that the player can open to gain points​

### Game Managers
managers.py: Contains managers for platforms, ladders, and chests to handle their creation, updates, and rendering​

### Visuals and Screens
*background.py:* Manages background elements such as dirt and moving clouds​
*screens.py:* Handles different game screens, such as the start and game over screens​
