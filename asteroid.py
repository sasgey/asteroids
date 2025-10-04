import pygame
import random
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

    def split(self):
        # Remove the current asteroid
        self.kill()

        # Stop if this asteroid is already at the minimum size
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return

        # --- Splitting logic ---
        # Pick a random angle between 20° and 50° for the split
        random_angle = random.uniform(20, 50)

        # Create two new velocity vectors rotated in opposite directions
        velocity_1 = self.velocity.rotate(random_angle) * 1.2
        velocity_2 = self.velocity.rotate(-random_angle) * 1.2

        # Calculate new (smaller) radius
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS

        # Spawn two smaller asteroids at the same position
        Asteroid(self.position.x, self.position.y, new_radius).velocity = velocity_1
        Asteroid(self.position.x, self.position.y, new_radius).velocity = velocity_2