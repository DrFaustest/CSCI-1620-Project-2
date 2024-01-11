#Handles the overall game logic and ties together all other components. It should control game states, score tracking, and level progression.
import pygame
from background import Background
from player import Player
from enemy import Enemy
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
        initial_x = self.screen_width // 2
        initial_y = 0
        enemy_type = 1
        self.enemies = [Enemy(screen, initial_x, initial_y, enemy_type)]

    def start(self):
        # Initialize game start
        play_button_img = pygame.image.load("assets\images\Library of the unused\png\Buttons\Rect-Medium\PlayText\Default.png")
        play_button_rect = play_button_img.get_rect()
        play_button_rect.center = (self.screen_width // 2, self.screen_height // 2)

        # Draw game start screen
        self.screen.fill((0, 0, 0))
        self.background.update()
        self.screen.blit(play_button_img, play_button_rect)

        # Check for mouse click
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
                mouse_pos = event.pos
                if play_button_rect.collidepoint(mouse_pos):
                    self.state = "PLAYING"

    def update(self):
        self.keys = pygame.key.get_pressed()
        self.key_pressed_left = self.keys[pygame.K_LEFT]
        self.key_pressed_right = self.keys[pygame.K_RIGHT]
        # ... event handling for key presses ...
        if self.key_pressed_left:
            self.player.move_left()
        if self.key_pressed_right:
            self.player.move_right()
        for enemy in self.enemies:
            enemy.move()

    def draw(self):
        # Draw game entities
        self.screen.fill((0, 0, 0))
        self.background.update()
        if not self.key_pressed_left and not self.key_pressed_right:
            self.player.update()
        self.player.draw(self.screen)
        for enemy in self.enemies:
            enemy.draw()

    def game_over(self):
        # Handle game over logic
        pass