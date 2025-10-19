import pygame
from circleshape import CircleShape
import constants

class Shot(CircleShape):
    # Will be assigned to groups in main.py
    containers = None

    def __init__(self, x, y):
        super().__init__(x, y, constants.SHOT_RADIUS)
        self.lifetime = constants.SHOT_LIFETIME
        pygame.sprite.Sprite.__init__(self, self.containers)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        # Countdown lifetime
        self.lifetime -= dt
        if self.lifetime <= 0:
            self.kill()
            return
    
        # Wrap shot position around screen edges
        self.wrap_position()