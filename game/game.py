"""Game module to run the game."""
import pygame
import random
from game.bird.bird import Bird
from game.pipe.pipe import Pipe
from game.button.button import Button
from game.settings import *
import game.controls as controls


class Game:
    """Game class to run the game."""
    def __init__(self) -> None:
        """Initialize the game.

        :return: None.
        """
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Flappy Bird')
        self.clock = pygame.time.Clock()
        self.pipe_group = pygame.sprite.Group()
        self.bird_group = pygame.sprite.Group()
        self.flappy = Bird(100, SCREEN_HEIGHT // 2)
        self.bird_group.add(self.flappy)
        self.button = Button(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 100, BUTTON_IMG)
        self.ground_scroll = 0
        self.score = 0
        self.pass_pipe = False
        self.last_pipe = pygame.time.get_ticks() - PIPE_FREQUENCY
        self.flying = False
        self.game_over = False

    def draw_text(self, text, font, text_col, x, y) -> None:
        """Draw text on the screen.

        :param text: str, text to draw.
        :param font: pygame.font.Font, font object.
        :param text_col: tuple, text color.
        :param x: int, x-coordinate.
        :param y: int, y-coordinate.
        :return: None.
        """
        img = font.render(text, True, text_col)
        self.screen.blit(img, (x, y))

    def reset_game(self) -> None:
        """Reset the game.

        :return: None.
        """
        self.pipe_group.empty()
        self.flappy.rect.center = (100, SCREEN_HEIGHT // 2)
        self.score = 0

    def run(self) -> None:
        """Run the game.

        :return: None.
        """
        running = True
        while running:
            self.clock.tick(FPS)
            self.screen.blit(BG, (0, 0))

            self.pipe_group.draw(self.screen)
            self.bird_group.draw(self.screen)
            self.bird_group.update()

            self.screen.blit(GROUND_IMG, (self.ground_scroll, 768))

            if self.flying and not self.game_over:
                self.generate_pipes()
                self.pipe_group.update()
                self.update_ground()

            self.check_collisions()
            self.display_score()

            # Handle continuous flying by checking for clicks while flying
            if self.flying and not self.game_over:
                if controls.check_jump():
                    self.flappy.vel = -10  # Apply the jump velocity to the bird

            if self.game_over and controls.check_reset_button(self.button):
                self.game_over = False
                self.flying = False
                self.reset_game()

            # Handling user input via the controls module
            for event in pygame.event.get():
                if controls.check_quit(event):
                    running = False
                if controls.check_start_flying(event, self.flying, self.game_over):
                    self.flying = True

            pygame.display.update()

        pygame.quit()

    def generate_pipes(self) -> None:
        """Generate pipes.

        :return: None.
        """
        time_now = pygame.time.get_ticks()
        if time_now - self.last_pipe > PIPE_FREQUENCY:
            pipe_height = random.randint(-100, 100)
            btm_pipe = Pipe(SCREEN_WIDTH, SCREEN_HEIGHT // 2 + pipe_height, -1)
            top_pipe = Pipe(SCREEN_WIDTH, SCREEN_HEIGHT // 2 + pipe_height, 1)
            self.pipe_group.add(btm_pipe)
            self.pipe_group.add(top_pipe)
            self.last_pipe = time_now

    def update_ground(self) -> None:
        """Update the ground.

        :return: None.
        """
        self.ground_scroll -= SCROLL_SPEED
        if abs(self.ground_scroll) > 35:
            self.ground_scroll = 0

    def check_collisions(self) -> None:
        """Check for collisions.

        :return: None.
        """
        global GAME_OVER
        if pygame.sprite.groupcollide(self.bird_group, self.pipe_group, False, False) or self.flappy.rect.top < 0:
            self.game_over = True
        if self.flappy.rect.bottom >= 768:
            self.game_over = True
            self.flying = False

    def display_score(self) -> None:
        """Display the score.

        :return: None.
        """
        if len(self.pipe_group) > 0:
            bird = self.bird_group.sprites()[0]
            first_pipe = self.pipe_group.sprites()[0]
            if bird.rect.left > first_pipe.rect.left and bird.rect.right < first_pipe.rect.right and not self.pass_pipe:
                self.pass_pipe = True
            if self.pass_pipe and bird.rect.left > first_pipe.rect.right:
                self.score += 1
                self.pass_pipe = False
        self.draw_text(str(self.score), FONT, WHITE, SCREEN_WIDTH // 2, 20)
