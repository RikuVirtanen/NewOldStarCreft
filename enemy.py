import pygame
import random
import os

from pygame.locals import RLEACCEL


class Enemy(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load(os.path.join("images", "alien.png")).convert()
        self.surf.set_colorkey((255, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(width + 20, width + 100),
                random.randint(0, height),
            )
        )
        self.speed = random.randint(5, 10)
        
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()