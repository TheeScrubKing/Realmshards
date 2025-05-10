# Tower Defense Game

## Overview
This is a simple tower defense game where players can build towers to defend against waves of enemies. The game features multiple levels, various tower types, and different enemy types, each with unique abilities and behaviors.

## Project Structure
```
tower-defense-game
├── src
│   ├── main.py                # Entry point of the game
│   ├── towers                 # Contains tower classes
│   │   ├── __init__.py
│   │   ├── basic_tower.py
│   │   ├── advanced_tower.py
│   │   └── special_tower.py
│   ├── enemies                # Contains enemy classes
│   │   ├── __init__.py
│   │   ├── enemy_types.py
│   │   └── enemy_paths.py
│   ├── levels                 # Contains level definitions
│   │   ├── __init__.py
│   │   ├── level1.py
│   │   ├── level2.py
│   │   └── level3.py
│   ├── systems                # Contains game systems
│   │   ├── __init__.py
│   │   ├── game_loop.py
│   │   ├── collision.py
│   │   └── scoring.py
│   └── utils                  # Contains utility functions
│       ├── __init__.py
│       └── helpers.py
├── requirements.txt           # Lists dependencies
└── README.md                  # Project documentation
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd tower-defense-game
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Gameplay Mechanics
- Players can place different types of towers to attack incoming enemies.
- Each tower has unique properties such as damage, range, and special abilities.
- Enemies will follow predefined paths and have varying health and speed.
- The game consists of multiple levels, each increasing in difficulty.

## Credits
- Developed by [Your Name]
- Inspired by classic tower defense games.