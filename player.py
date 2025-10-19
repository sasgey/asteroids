import pygame
from circleshape import CircleShape
from shot import Shot
import constants

class Player(CircleShape):
    containers = None  # Will be set in main.py

    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0  # initial rotation angle in degrees
        self.shoot_timer = 0  # countdown timer for shooting cooldown

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

    # --- Move the player forward/backward ---
    def move(self, dt):
        # Unit vector pointing up
        direction = pygame.Vector2(0, -1).rotate(self.rotation)  # -1 because screen y increases downward
        # Calculate velocity
        velocity = direction * constants.PLAYER_SPEED
        # Update position
        self.position += velocity * dt

    # --- Shoot a bullet ---
    def shoot(self):
        if self.shoot_timer <= 0:
            shot = Shot(self.position.x, self.position.y)
            # Velocity points in the direction player is facing
            shot.velocity = pygame.Vector2(0, -1).rotate(self.rotation) * constants.PLAYER_SHOOT_SPEED
            # Add the shot to its containers
            if Shot.containers:
                for group in Shot.containers:
                    group.add(shot)
            self.shoot_timer = constants.PLAYER_SHOOT_COOLDOWN  # reset cooldown

    # --- Update player each frame ---
    def update(self, dt):
        keys = pygame.key.get_pressed()

        # Rotation
        if keys[pygame.K_a]:
            self.rotation -= constants.PLAYER_TURN_SPEED * dt
        if keys[pygame.K_d]:
            self.rotation += constants.PLAYER_TURN_SPEED * dt

        # Movement
        if keys[pygame.K_w]:
            self.move(dt)     # move forward
        if keys[pygame.K_s]:
            self.move(-dt)    # move backward

        # Shooting
        if keys[pygame.K_SPACE]:
            self.shoot()

        # Decrease cooldown timer
        if self.shoot_timer > 0:
            self.shoot_timer -= dt

        # Wrap player around screen edges
        self.wrap_position()