import sys

import pygame

class BlueScreen:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Rocket")

        # Load image and center it
        self.image = pygame.image.load('rocket.bmp')
        self.image_rect = self.image.get_rect()
        self.image_rect.center = self.screen.get_rect().center

    def run_game(self):
        """Start the main loop for the game."""
        speed = 5
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.image_rect.x -= speed
            if keys[pygame.K_RIGHT]:
                self.image_rect.x += speed
            if keys[pygame.K_UP]:
                self.image_rect.y -= speed
            if keys[pygame.K_DOWN]:
                self.image_rect.y += speed

            # Redraw the screen during each pass through the loop.
            self.screen.fill('black')
            self.screen.blit(self.image, self.image_rect)

            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = BlueScreen()
    ai.run_game()