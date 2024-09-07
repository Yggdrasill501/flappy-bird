"""Module with pipe sprite."""
import pygame
from game.settings import PIPE_GAP, SCROLL_SPEED

class Pipe(pygame.sprite.Sprite):
    """Pipe sprite."""

    def __init__(self, x: int, y: int, position: int):
        """Initialize the pipe with its position.

        :param x: int, the x-coordinate of the pipe.
        :param y: int, the y-coordinate of the pipe.
        :param position: int, the position of the pipe (-1 for bottom, 1 for top).
        """
        super().__init__()
        self.image = pygame.image.load("assets/pipe.png")
        self.rect = self.image.get_rect()

        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - PIPE_GAP // 2]
        else:
            self.rect.topleft = [x, y + PIPE_GAP // 2]

    def update(self) -> None:
        """Move the pipe across the screen.

        :return: None
        """
        self.rect.x -= SCROLL_SPEED
        if self.rect.right < 0:
            self.kill()
