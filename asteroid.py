import pygame
from circleshape import CircleShape
import constants

class Asteroid(CircleShape):
    # Will be assigned to groups in main.py
    containers = None

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        pygame.sprite.Sprite.__init__(self, self.containers)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (200, 200, 200),  # light gray
            (int(self.position.x), int(self.position.y)),
            self.radius,
            2
        )

    def update(self, dt):
        self.position += self.velocity * dt

