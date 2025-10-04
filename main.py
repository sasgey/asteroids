import pygame, constants
from player import Player
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

    # --- Create the player at the center of the screen ---
    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    updatables.add(player)
    drawables.add(player)

    # Game loop
    while True:
        # --- Handle events ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit the game

        # --- Update player ---
        player.update(dt)

        # --- Draw everything ---
        screen.fill((0, 0, 0))  # RGB color for black
        for drawable in drawables:
            drawable.draw(screen)  # Draw each object individually

        # Refresh the display
        pygame.display.flip()

        # --- Control the frame rate ---
        dt = clock.tick(60) / 1000  # Limit to 60 FPS, convert ms → seconds

if __name__ == "__main__":
    main()

    # Quit pygame after the loop exits
    pygame.quit()
