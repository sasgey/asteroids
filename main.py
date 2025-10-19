import pygame
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot
import constants

def main():
    # Initialize pygame
    pygame.init()
    
    # Set up the screen
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroid Game")

    # Create a clock to manage frame rate
    clock = pygame.time.Clock()
    dt = 0

    # --- Create groups ---
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # --- Set containers BEFORE creating instances ---
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    Shot.containers = (shots, updatables, drawables)
    AsteroidField.containers = (updatables,)

    # --- Create the player at the center of the screen ---
    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

    # --- Create asteroid field ---
    field = AsteroidField()

    # --- Game loop ---
    while True:
        # --- Handle events ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit the game

        # --- Update all updatable objects ---
        updatables.update(dt)

        # --- Collision detection ---

        # Player vs asteroid collision
        # spritecollideany() checks if a single sprite hits any sprite in a group.
        if pygame.sprite.spritecollideany(player, asteroids):
            print("Game over!")
            return  # Exit the game

        # Bullet vs asteroid collision
        # groupcollide() checks for collisions between all members of two groups.
        # The two 'True' arguments tell Pygame to automatically .kill() (remove)
        # both the shot and the asteroid that collided.
        asteroids_hit = pygame.sprite.groupcollide(shots, asteroids, True, True)

        # Now, we loop ONLY through the asteroids that were hit and split them.
        for asteroid in asteroids_hit:
            asteroid.split()

        # --- Draw everything ---
        screen.fill((0, 0, 0))  # RGB color for black
        for drawable in drawables:
            drawable.draw(screen)  # Draw each object individually

        # --- Refresh the display ---
        pygame.display.flip()

        # --- Control the frame rate ---
        dt = clock.tick(60) / 1000  # Limit to 60 FPS, convert ms → seconds

if __name__ == "__main__":
    main()
    # Quit pygame after the loop exits
    pygame.quit()
