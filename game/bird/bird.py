"""Module with bird sprite."""
import pygame
from game.settings import GAME_OVER, FLYING

class Bird(pygame.sprite.Sprite):
    """Sprite brid."""

    def __init__(self, x: int, y: int):
        """Initialize the bird with position and animation frames.

        :param x: int, the x-coordinate of the bird.
        :param y: int, the y-coordinate of the bird.
        """
        super().__init__()
        self.images = [pygame.image.load(f'assets/bird{num}.png') for num in range(1, 4)]
        self.index = 0
        self.counter = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=(x, y))
        self.vel = 0
        self.clicked = False

    def update(self) -> None:
        """Update the bird's position and animation.

        :return: None
        """
        if self.vel < 8:
            self.vel += 0.5  # Apply gravity
        if self.rect.bottom < 768:
            self.rect.y += int(self.vel)

        self.animate()
        self.image = pygame.transform.rotate(self.images[self.index], self.vel * -2)

    def animate(self) -> None:
        """Handle the bird's wing flap animation.

        :return: None
        """
        self.counter += 1
        if self.counter > 5:
            self.counter = 0
            self.index = (self.index + 1) % len(self.images)
