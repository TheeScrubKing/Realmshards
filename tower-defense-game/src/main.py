# File: /tower-defense-game/tower-defense-game/src/main.py

import pygame
from systems.game_loop import GameLoop

def main():
    pygame.init()
    game = GameLoop()
    game.run()
    pygame.quit()

if __name__ == "__main__":
    main()