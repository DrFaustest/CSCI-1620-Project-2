# Manages enemy behavior, including spawning, movement, and attack patterns.
import pygame
import random

class Enemy:
    def __init__(self, screen, x, y, wave, scaleFactor=1, type=None):
        self.screen = screen
        self.x = x
        self.y = y
        self.scaleFactor = scaleFactor
        self.type = type if type is not None else 1 if random.random() < 0.7 else 2
        self.size = 40 * self.scaleFactor
        self.wave = wave
        # Load images
        self.enemy_image = pygame.image.load('assets\images\enemyShip.png')
        self.enemy_type2_image = pygame.image.load('assets\images\enemyUFO.png')
        self.image = self.enemy_image if self.type == 1 else self.enemy_type2_image
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.mask = pygame.mask.from_surface(self.image)
        # Additional attributes...

    def draw(self):
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        self.screen.blit(rotated_image, (self.x, self.y))

    def move(self, score):
        # Translate the movement logic based on self.wave and score
        # Update self.x, self.y, and self.angle

    @classmethod
    def spawn(cls, screen, x, wave, scaleFactor=1):
        return cls(screen, x, 0, wave, scaleFactor)

# You'll need to translate the rotateImage function logic and integrate it with the draw method.
