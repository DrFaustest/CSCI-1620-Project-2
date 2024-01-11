import pygame
from background import Background
from player import Player

def main():
    # Initialize Pygame
    pygame.init()

    # Set up the game window
    screen_width = 1500
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Space Shooter Game")

    # Set up the background
    background = Background(screen, screen_width, screen_height)

    # Set up the clock
    clock = pygame.time.Clock()
    clock.tick(60)

    # Set up the player
    start_x = screen_width // 2
    start_y = screen_height - 85  # 50 pixels from the bottom of the screen
    player = Player(start_x, start_y, screen_width)

    # Main game loop
    running = True
    while running:
         # Get the state of all keys
        keys = pygame.key.get_pressed()
        key_pressed_left = keys[pygame.K_LEFT]  # Check if the left arrow key is pressed
        key_pressed_right = keys[pygame.K_RIGHT]  # Check if the right arrow key is pressed

        # ... event handling for key presses ...
        if key_pressed_left:
            player.move_left()
        if key_pressed_right:
            player.move_right()

        screen.fill((0, 0, 0))
        background.update()
        if not key_pressed_left and not key_pressed_right:
            player.update()
        player.draw(screen)

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
