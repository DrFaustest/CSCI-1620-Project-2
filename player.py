import pygame

class Player:
    def __init__(self, x, y, screen_width):
        self.x = x
        self.y = y
        self.speed = 1
        self.image_normal = pygame.image.load('assets\images\player.png')
        self.image_left = pygame.image.load('assets\images\playerLeft.png')
        self.image_right = pygame.image.load('assets\images\playerRight.png')
        self.current_image = self.image_normal
        self.rect = self.current_image.get_rect(topleft=(self.x, self.y))
        self.screen_width = screen_width

    def draw(self, screen):
        screen.blit(self.current_image, self.rect)

    def move_left(self):
        self.current_image = self.image_left
        self.rect.x -= self.speed
        self.rect.x = max(self.rect.x, 0)  # Prevent moving off-screen

    def move_right(self):
        self.current_image = self.image_right
        self.rect.x += self.speed
        self.rect.x = min(self.rect.x, self.screen_width - self.rect.width)  # Prevent moving off-screen

    def update(self):
        # Reset to normal image when not moving
        self.current_image = self.image_normal

