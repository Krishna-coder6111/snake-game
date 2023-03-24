#importing libraries needed
import pygame
import sys
import random
import time

#initializing pygame
pygame.init()

#defining colours, screen dimensions and game speed
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20

GAME_SPEED = 10


class Snake:
    """
    Snake class representing the snake in the game.
    """
    def __init__(self):
        self.body = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = (GRID_SIZE, 0)

    def move(self):
        """
        Move the snake in the direction it is heading.
        """
        head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
        self.body.insert(0, head)
        self.body.pop()

    def grow(self):
        """
        Grow the snake by adding a new segment to its body.
        """
        self.body.append(self.body[-1])

    def collides_with_self(self):
        """
        Check if the snake's head collides with its body.
        """
        return self.body[0] in self.body[1:]

    def collides_with_wall(self):
        """
        Check if the snake's head collides with the screen boundaries.
        """
        x, y = self.body[0]
        return x < 0 or x >= SCREEN_WIDTH or y < 0 or y >= SCREEN_HEIGHT

    def change_direction(self, new_direction):
        """
        Change the direction of the snake.
        """
        if (new_direction[0] != -self.direction[0]) and (new_direction[1] != -self.direction[1]):
            self.direction = new_direction


class Food:
    """
    Food class representing the food in the game.
    """
    def __init__(self):
        self.position = self.generate_position()

    def generate_position(self):
        """
        Generate a new random position for the food.
        """
        x = random.randrange(0, SCREEN_WIDTH, GRID_SIZE)
        y = random.randrange(0, SCREEN_HEIGHT, GRID_SIZE)
        return (x, y)

def draw_text(screen, text, size, x, y, color=WHITE):
    """
    Draw text on the screen.
    """
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)

def start_screen():
    """
    Display the start screen with instructions to begin the game.
    """
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Snake Game')
    clock = pygame.time.Clock()

    while True:
        screen.fill(BLACK)
        draw_text(screen, 'Snake Game - by Krishna Singh', 64, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
        draw_text(screen, 'Press any key to start', 32, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                return

        clock.tick(GAME_SPEED)

def game_loop():
    """
    Runs the game loop
    """
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Snake Game')
    clock = pygame.time.Clock()

    snake = Snake()
    food = Food()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction((0, -GRID_SIZE))
                elif event.key == pygame.K_DOWN:
                    snake.change_direction((0, GRID_SIZE))
                elif event.key == pygame.K_LEFT:
                    snake.change_direction((-GRID_SIZE, 0))
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction((GRID_SIZE, 0))

        snake.move()

        if snake.collides_with_wall() or snake.collides_with_self():
            return

        if snake.body[0] == food.position:
            snake.grow()
            food = Food()

        screen.fill(BLACK)

        for segment in snake.body:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

        pygame.draw.rect(screen, RED, (food.position[0], food.position[1], GRID_SIZE, GRID_SIZE))

        pygame.display.flip()
        clock.tick(GAME_SPEED)

def end_screen():
    """
    Plays the end screen when any of the end conditions are met:
     - snake collides with itself
     - snake collides with border
    """
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Snake Game')
    clock = pygame.time.Clock()

    while True:
        screen.fill(BLACK)
        draw_text(screen, 'Game Over', 64, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
        draw_text(screen, 'Press any key to play again', 32, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                return

        clock.tick(GAME_SPEED)

def main():
    """
    Main method of the game initializes game functions
    """
    start_screen()
    while True:
        game_loop()
        end_screen()

#runs the game
if __name__ == "__main__":
    main()