import pygame
import random

class Background:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.stars = [(random.randint(0, width), random.randint(0, height)) for _ in range(100)]

    def update(self):
        for star in self.stars:
            pygame.draw.circle(self.screen, (255, 255, 255), star, 2)
        self.stars = [(x, y+0.5 if y < self.height else 0) for x, y in self.stars]




