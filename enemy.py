# Manages enemy behavior, including spawning, movement, and attack patterns.
import pygame
import random
from util import *

class Enemy:
    def __init__(self, screen, x, y, type, scaleFactor=1, wave=1):
        self.screen = screen
        self.x = x
        self.y = y
        self.scaleFactor = scaleFactor
        self.type = type if type is not None else 1 if random.random() < 0.7 else 2
        self.size = 40 * self.scaleFactor
        # Load images
        self.enemy_image = pygame.image.load('assets\images\enemyShip.png')
        self.enemy_type2_image = pygame.image.load('assets\images\enemyUFO.png')
        self.image = self.enemy_image if self.type == 1 else self.enemy_type2_image
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.mask = pygame.mask.from_surface(self.image)
        self.angle = 0
        self.wave = wave
        self.bounce = 0
        # Additional attributes...

    def draw(self):
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        self.screen.blit(rotated_image, (self.x, self.y))

    def move(self):
        if self.type == 1:
            # movement pattern for type 1
            if self.wave == 1:
                if self.x < SCREEN_WIDTH and self.bounce == 0: 
                    self.x += 1
                    self.y += 1
                    self.angle += 1
                elif self.x == SCREEN_WIDTH or self.bounce == 1: 
                    self.bounce = 1
                    self.x -= 1
                    self.y += 1
                    self.angle += 1
                elif self.y == 0 and self.bounce == 1:
                    self.bounce = 0

        elif self.type == 2:
            if self.wave == 1:
                if self.x < SCREEN_WIDTH and self.bounce == 0: 
                    self.x += 1
                    self.angle += 1
                elif self.x == SCREEN_WIDTH or self.x == 0:
                    self.bounce = 1 if self.bounce == 0 else 0
                    self.x -= 1
                    self.y -= SCREEN_HEIGHT // 4
                    self.angle += 1
        # Translate the movement logic based on self.wave and score
        # Update self.x, self.y, and self.angle

    @classmethod
    def spawn(cls, screen, x, wave, scaleFactor=1):
        return cls(screen, x, 0, wave, scaleFactor)

# You'll need to translate the rotateImage function logic and integrate it with the draw method.
