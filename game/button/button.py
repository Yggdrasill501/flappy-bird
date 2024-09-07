"""Package for button to restart game."""
import pygame

class Button:
    """Button to restart game."""""

    def __init__(self, x: int, y: int, image: pygame.Surface):
        """Initialize the button with its image and position.

        :param x: int, the x-coordinate of the button.
        :param y: int, the y-coordinate of the button.
        :param image: pygame.Surface, the image to be used for the button.
        """
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, screen: pygame.Surface) -> bool:
        """Draw the button on the screen and check if clicked.

        :param screen: pygame.Surface, the screen to draw the button on.
        :return: bool, True if the button is clicked.
        """
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1:
            action = True
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action
