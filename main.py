import pygame, constants

def main():
    # Initialize pygame
    pygame.init()
    
    # Set up the screen
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroid Game")

    # Create a clock to manage frame rate
    clock = pygame.time.Clock()

    # Delta time variable (seconds since last frame)
    dt = 0
    
    # Game loop
    while True:
        # --- Handle events ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit the game
        
        # --- Draw everything ---
        screen.fill((0, 0, 0))  # RGB color for black

        # Refresh the display
        pygame.display.flip()

        # --- Control the frame rate ---
        dt = clock.tick(60) / 1000  # Limit to 60 FPS, convert ms → seconds

if __name__ == "__main__":
    main()

    # Quit pygame after the loop exits
    pygame.quit()
