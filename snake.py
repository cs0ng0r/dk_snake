import pygame
import random
import sys

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 50
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gyurcsány Ferenc Snake Game")

# Timing
clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont("Arial", 24)

# Load images
snake_image = pygame.image.load("head.png")  # Replace with your snake image
food_image = pygame.image.load("dk.png")  # Replace with your food image
bg_image = pygame.image.load(
    "gradient.jpeg")  # Replace with your gradient background

# Scale images to match cell size or screen size
snake_image = pygame.transform.scale(snake_image, (CELL_SIZE, CELL_SIZE))
food_image = pygame.transform.scale(food_image, (CELL_SIZE, CELL_SIZE))
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))


def draw_snake(snake):
    for segment in snake:
        screen.blit(snake_image, segment)


def draw_food(food):
    screen.blit(food_image, food)


def main():
    snake = [(100, 100), (80, 100), (60, 100)]
    direction = "RIGHT"
    change_to = direction

    # Food
    food = (random.randrange(0, WIDTH // CELL_SIZE) * CELL_SIZE,
            random.randrange(0, HEIGHT // CELL_SIZE) * CELL_SIZE)

    # Score
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and direction != "DOWN":
            change_to = "UP"
        if keys[pygame.K_DOWN] and direction != "UP":
            change_to = "DOWN"
        if keys[pygame.K_LEFT] and direction != "RIGHT":
            change_to = "LEFT"
        if keys[pygame.K_RIGHT] and direction != "LEFT":
            change_to = "RIGHT"

        direction = change_to

        # Move snake
        x, y = snake[0]
        if direction == "UP":
            y -= CELL_SIZE
        if direction == "DOWN":
            y += CELL_SIZE
        if direction == "LEFT":
            x -= CELL_SIZE
        if direction == "RIGHT":
            x += CELL_SIZE

        new_head = (x, y)
        snake.insert(0, new_head)

        # Eat food
        if new_head == food:
            score += 1
            food = (random.randrange(0, WIDTH // CELL_SIZE) * CELL_SIZE,
                    random.randrange(0, HEIGHT // CELL_SIZE) * CELL_SIZE)
        else:
            snake.pop()

        # Collision detection (Game Over)
        if (x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT
                or new_head in snake[1:]):
            game_over(score)

        # Update screen
        screen.blit(bg_image, (0, 0))  # Draw background
        draw_snake(snake)
        draw_food(food)

        # Display score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(10)


def game_over(score):
    screen.fill(BLACK)
    game_over_text = font.render("Vége!", True, WHITE)
    score_text = font.render(f"Végeredmény: {score}", True, WHITE)
    screen.blit(
        game_over_text,
        (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 50))
    screen.blit(score_text,
                (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
