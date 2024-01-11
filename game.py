#Handles the overall game logic and ties together all other components. It should control game states, score tracking, and level progression.
import pygame
from background import Background
from player import Player
from util import *

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.state = "START"
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT
        self.start_y = self.screen_height - 85
        self.start_x = self.screen_width // 2
        self.player = Player(self.start_x, self.start_y, self.screen_width)
        self.background = Background(screen, self.screen_width, self.screen_height)

    def start(self):
        # Initialize game start


    def update(self):
        # Update game entities
        # Get the state of all keys
        keys = pygame.key.get_pressed()
        key_pressed_left = keys[pygame.K_LEFT]  # Check if the left arrow key is pressed
        key_pressed_right = keys[pygame.K_RIGHT]  # Check if the right arrow key is pressed

        # ... event handling for key presses ...
        if key_pressed_left:
            self.player.move_left()
        if key_pressed_right:
            self.player.move_right()

    def draw(self):
        # Draw game entities
        self.screen.fill((0, 0, 0))
        self.background.update()
        if not key_pressed_left and not key_pressed_right:
            self.player.update()
        self.player.draw(self.screen)

    def game_over(self):
        # Handle game over logic
