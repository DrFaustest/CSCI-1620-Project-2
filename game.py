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
        play_button = pygame.Rect(100, 100, 200, 50)  # Example position and size
        quit_button = pygame.Rect(100, 200, 200, 50)  # Example position and size

        # Drawing the buttons
        pygame.draw.rect(self.screen, [255, 0, 0], play_button)  # Red play button
        pygame.draw.rect(self.screen, [0, 255, 0], quit_button)  # Green quit button

        # Check for mouse click
        click = pygame.mouse.get_pressed()
        if click[0] == 1:  # Left mouse button
            mouse_pos = pygame.mouse.get_pos()
            if play_button.collidepoint(mouse_pos):
                self.state = "PLAYING"
            elif quit_button.collidepoint(mouse_pos):
                pygame.quit()
                exit()


    def update(self):
        self.keys = pygame.key.get_pressed()
        self.key_pressed_left = self.keys[pygame.K_LEFT]
        self.key_pressed_right = self.keys[pygame.K_RIGHT]
        # ... event handling for key presses ...
        if self.key_pressed_left:
            self.player.move_left()
        if self.key_pressed_right:
            self.player.move_right()

    def draw(self):
        # Draw game entities
        self.screen.fill((0, 0, 0))
        self.background.update()
        if not self.key_pressed_left and not self.key_pressed_right:
            self.player.update()
        self.player.draw(self.screen)

    def game_over(self):
        # Handle game over logic
        pass