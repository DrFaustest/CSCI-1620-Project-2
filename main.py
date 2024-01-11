import pygame
from background import Background
from player import Player
from game import Game
from util import *

def main():
    # Initialize Pygame
    pygame.init()

    # Set up the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Space Shooter Game")

    # Set up the background
    background = Background(screen, SCREEN_WIDTH, SCREEN_HEIGHT)

    # Set up the clock
    clock = pygame.time.Clock()
    clock.tick(60)

    # Set up the player
    start_x = screen_width // 2
    start_y = screen_height - 85  # 50 pixels from the bottom of the screen
    player = Player(start_x, start_y, screen_width)

    game = Game(screen)

    # Main game loop
    running = True
    while running:
        if game.state == "START":
            game.start()
        elif game.state == "PLAYING":
            game.update()
            game.draw()
        elif game.state == "GAME OVER":
            game.game_over()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Game logic goes here

        # Update the screen
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
