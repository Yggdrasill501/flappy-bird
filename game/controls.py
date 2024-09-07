"""This module contains functions to check for user input events."""
from game.button.button import Button
import pygame

def check_quit(event: pygame.event.Event) -> bool:
    """Check if the user wants to quit the game.

    :param event: pygame.event.Event, pygame event.
    :return: bool, True if the user wants to quit the game.
    """
    if event.type == pygame.QUIT:
        return True
    return False

def check_start_flying(event: pygame.event.Event, flying: bool, game_over: bool) -> bool:
    """Check if the game should start flying (mouse or key press).

    :param event: pygame.event.Event, pygame event.
    :param flying: bool, True if the bird is flying.
    :param game_over: bool, True if the game is over.
    :return: bool, True if the game should start flying.
    """
    if event.type == pygame.MOUSEBUTTONDOWN and not flying and not game_over:
        return True
    return False

def check_jump() -> bool:
    """Check if the bird should jump (mouse press).

    :return: bool, True if the bird should jump.
    """
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            return True
    return False

def check_reset_button(button: Button) -> bool:
    """Check if the reset button is clicked.

    :param button: Button, button object.
    :return: bool, True if the reset button is clicked.
    """
    return button.draw(pygame.display.get_surface())
