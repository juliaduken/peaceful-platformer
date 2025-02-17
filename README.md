# 🧚🏻‍♀️✨ Peaceful Platformer ✨🧚🏻‍♀️

Welcome to the *Peaceful Platformer* game! This README will guide you through setting up and running the game locally, as well as explain the functionality of the different files.

**Please note:** This is not a fully functioning game. Additionally, the terminal still contains some debugging outputs. It was meant as a project to help me learn Pygame through creating movement and collision detection with images. I drew the art for the game and used ChatGPT & Stack Overflow to help me learn about Pygame! 🎨💭

**Functionality:** The game includes a score keeping mechanism, detects collisions with moving enemies, and allows for opening chests and climbing ladders. The platforms generate randomly for a set distance, ensuring that they are close enough together. Ladders generate randomly on platforms greater than a certain height. The game camera is based on player location throughout the game. I created a new branch called camera that changed this mechanism as it was causing challenges to implement a final boss at the end. Consequently, I stopped development and moved on to another project. I learned a lot while coding this and really enjoyed it. 

## 🕹️ Gameplay

<div align="center">
    <img src="https://i.postimg.cc/fRwd23LY/image.png" width="500" height="300">
</div>

## 🛠️ Getting Started

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
git clone https://github.com/juliaduken/peaceful-platformer.git
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

## 🎮 How to Play
In *Peaceful Platformer*, your goal is to explore the game world, collect treasures, and score as many points as possible while navigating platforms and climbing ladders. 
### Controls
*Movement*<br>
    - Left Arrow (←): Move left.<br>
    - Right Arrow (→): Move right.<br><br>
*Jumping*<br>
    - Spacebar: Jump. You can also combine this with the arrow keys for directional jumps.<br><br>
*Climbing Ladders*<br>
    - Up Arrow (↑): Climb up a ladder.<br>
    - Down Arrow (↓): Climb down or drop through a platform.<br><br>
*Interacting with Chests*<br>
    - E Key: Open a nearby chest to collect treasure and score points.

### Scoring System
Each chest you open awards 10 points.

## 📂 File Descriptions
### Core Game Files
- *game.py:* Contains the main game loop, initializes the game window, and manages updates and rendering for all components​<br>
- *settings.py:* Defines global constants such as screen dimensions, colors, player settings, and asset paths​

### Gameplay Components
- *player.py:* Handles the player's behavior, including movement, jumping, climbing ladders, and interacting with chests​<br>
- *platform.py:* Represents platforms in the game, including their position and collision detection​​<br>
- *ladder.py:* Represents ladders, allowing the player to climb between platforms​​<br>
- *chest.py:* Represents treasure chests that the player can open to gain points​​<br>

### Game Managers
- *managers.py:* Contains managers for platforms, ladders, and chests to handle their creation, updates, and rendering​

### Visuals and Screens
- *background.py:* Manages background elements such as dirt and moving clouds​ <br>
- *screens.py:* Handles different game screens, such as the start and game over screens​
