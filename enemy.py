# Manages enemy behavior, including spawning, movement, and attack patterns.
import pygame
import random
from util import *

class Enemy:
    def __init__(self, screen, x, y, type, scaleFactor=1, wave=1):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = 0.5 * scaleFactor
        self.scaleFactor = scaleFactor
        self.game_boundaries = (5, 5, SCREEN_WIDTH-10, SCREEN_HEIGHT-10)
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
        left, top, right, bottom = self.game_boundaries
        
        if self.type == 1:
            # Movement pattern for type 1
            if self.wave == 1:
                if self.x < right and self.bounce == 0: 
                    self.x += self.speed
                    self.y += self.speed
                    self.angle = 1
                elif self.x >= right or self.bounce == 1:
                    self.bounce = 1
                    self.x -= self.speed
                    self.y += self.speed
                    self.angle = -1
                elif self.y <= top and self.bounce == 1:
                    self.bounce = 0

        elif self.type == 2:
            # Movement pattern for type 2
            if self.wave == 1:
                if self.x < right and self.bounce == 0:
                    self.x += self.speed
                    self.angle = 1
                elif self.x >= right or self.x <= left:
                    self.bounce = 1 if self.bounce == 0 else 0
                    self.x -= self.speed
                    self.y -= bottom // 4
                    self.angle = -1

            # Translate the movement logic based on self.wave and score
            # Update self.x, self.y, and self.angle

    @classmethod
    def spawn(cls, screen, x, wave, scaleFactor=1):
        return cls(screen, x, 0, wave, scaleFactor)

# You'll need to translate the rotateImage function logic and integrate it with the draw method.
