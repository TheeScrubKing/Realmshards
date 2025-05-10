# File: /tower-defense-game/tower-defense-game/src/main.py

from systems.game_loop import GameLoop
import pygame
import sys


def show_start_screen(screen):
    """Display the start screen."""
    font = pygame.font.Font(None, 74)
    text = font.render("Realmshards", True, (255, 255, 255))
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
                print("Key pressed! Starting the game...")  # Debugging message
                return  # Exit the start screen when any key is pressed


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Runeshards")

    # Show the start screen
    show_start_screen(screen)

    # Initialize the game loop
    try:
        game_loop = GameLoop()
    except Exception as e:
        print(f"Error initializing GameLoop: {e}")  # Debugging message
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
            print(f"Error during game loop: {e}")  # Debugging message
            running = False

        # Cap the frame rate
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
