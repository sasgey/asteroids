import pygame
import constants

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
    
    def wrap_position(self):
        """Move object to opposite screen edge if it leaves the screen."""
        if self.position.x < -self.radius:
            self.position.x = constants.SCREEN_WIDTH + self.radius
        elif self.position.x > constants.SCREEN_WIDTH + self.radius:
            self.position.x = -self.radius

        if self.position.y < -self.radius:
            self.position.y = constants.SCREEN_HEIGHT + self.radius
        elif self.position.y > constants.SCREEN_HEIGHT + self.radius:
            self.position.y = -self.radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collides_with(self, other):
        """
        Check if this CircleShape collides with another CircleShape.

        Args:
            other (CircleShape): Another circle to check collision with.

        Returns:
            bool: True if the circles collide, False otherwise.
        """
        distance = self.position.distance_to(other.position)
        return distance <= self.radius + other.radius