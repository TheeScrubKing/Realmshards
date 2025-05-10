"""
Main module for the Realmshards Tower Defense Game.
"""

import sys
import pygame
from systems.game_loop import GameLoop


def show_start_screen(screen):
    """Display the start screen."""
    font = pygame.font.Font(None, 74)
    text = font.render("Realmshards", True, (255, 255, 255))
    subtext = pygame.font.Font(None, 36).render(
        "Press any key to start", True, (200, 200, 200)
    )

    while True:
        screen.fill((0, 0, 0))
        screen.blit(text, (screen.get_width() //
                    2 - text.get_width() // 2, 200))
        screen.blit(subtext, (screen.get_width() //
                    2 - subtext.get_width() // 2, 300))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                print("Key pressed! Starting the game...")
                return
            elif event.type == pygame.QUIT:
                print("Quit event detected. Exiting...")
                pygame.quit()
                sys.exit()

        pygame.display.flip()


def main():
    """Main function to initialize and run the game."""
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Realmshards")

    # Show the start screen
    show_start_screen(screen)

    # Initialize the game loop
    try:
        game_loop = GameLoop()
    except Exception as e:
        print(f"Error initializing GameLoop: {e}")
        pygame.quit()
        sys.exit()

    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update and render the game
        try:
            game_loop.update_game_state()
            game_loop.render_game(screen)
        except Exception as e:
            print(f"Error during game loop: {e}")
            running = False

        # Cap the frame rate
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
