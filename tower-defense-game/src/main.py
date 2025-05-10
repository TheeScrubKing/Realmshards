# File: /tower-defense-game/tower-defense-game/src/main.py

from systems.game_loop import GameLoop
import pygame
import sys


def show_start_screen(screen):
    """Display the start screen."""
    font = pygame.font.Font(None, 74)
    text = font.render("Runeshards", True, (255, 255, 255))
    subtext = pygame.font.Font(None, 36).render(
        "Press any key to start", True, (200, 200, 200))

    while True:
        screen.fill((0, 0, 0))
        screen.blit(text, (screen.get_width() //
                    2 - text.get_width() // 2, 200))
        screen.blit(subtext, (screen.get_width() //
                    2 - subtext.get_width() // 2, 300))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return  # Exit the start screen when any key is pressed


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Runeshards")

    # Show the start screen
    show_start_screen(screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
