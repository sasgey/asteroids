import pygame
import constants
from circleshape import CircleShape  # assuming you already have circleshape.py

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0  # initial rotation angle in degrees

    # --- Triangle shape for the ship ---
    def triangle(self):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    # --- Draw the player ship ---
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        # Unit vector pointing up
        direction = pygame.Vector2(0, -1).rotate(self.rotation)  # -1 because screen y increases downward
        # Scale by speed and dt
        displacement = direction * constants.PLAYER_SPEED * dt
        # Update position
        self.position += displacement * constants.PLAYER_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        # Rotation
        if keys[pygame.K_a]:
            self.rotate(-dt)  # rotate left
        if keys[pygame.K_d]:
            self.rotate(dt)   # rotate right

        # Forward/backward movement
        if keys[pygame.K_w]:
            self.move(dt)     # move forward
        if keys[pygame.K_s]:
            self.move(-dt)    # move backward      