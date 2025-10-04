import pygame
from circleshape import CircleShape
import constants

class Shot(CircleShape):
    # Will be assigned to groups in main.py
    containers = None

    def __init__(self, x, y):
        super().__init__(x, y, constants.SHOT_RADIUS)
        pygame.sprite.Sprite.__init__(self, self.containers)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (255, 255, 0),  # yellow
            (int(self.position.x), int(self.position.y)),
            self.radius
        )

    def update(self, dt):
        self.position += self.velocity * dt

