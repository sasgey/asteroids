import pygame, constants

def main():
    # Initialize pygame
    pygame.init()
    
    # Set up the screen
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    
    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Step 3: Draw everything
        # Fill the screen with black
        screen.fill((0, 0, 0))  # RGB color for black

        # Refresh the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
