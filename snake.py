import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
CELL_SIZE = WIDTH // 20
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gyurcsány Ferenc Snake Game")

clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 24)

snake_image = pygame.image.load("head.png")
food_image = pygame.image.load("dk.png")
bg_image = pygame.image.load("gradient.jpeg")

snake_image = pygame.transform.scale(snake_image, (CELL_SIZE, CELL_SIZE))
food_image = pygame.transform.scale(food_image, (CELL_SIZE, CELL_SIZE))
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))


def draw_snake(snake):
    for segment in snake:
        screen.blit(snake_image, segment)


def draw_food(food):
    screen.blit(food_image, food)


def main():
    snake = [(CELL_SIZE * 4, CELL_SIZE * 4), (CELL_SIZE * 3, CELL_SIZE * 4),
             (CELL_SIZE * 2, CELL_SIZE * 4)]
    direction = "RIGHT"

    food = (random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
            random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)

    score = 0

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_UP
                        or event.key == pygame.K_w) and direction != "DOWN":
                    direction = "UP"
                elif (event.key == pygame.K_DOWN
                      or event.key == pygame.K_s) and direction != "UP":
                    direction = "DOWN"
                elif (event.key == pygame.K_LEFT
                      or event.key == pygame.K_a) and direction != "RIGHT":
                    direction = "LEFT"
                elif (event.key == pygame.K_RIGHT
                      or event.key == pygame.K_d) and direction != "LEFT":
                    direction = "RIGHT"

        x, y = snake[0]
        if direction == "UP":
            y -= CELL_SIZE
        elif direction == "DOWN":
            y += CELL_SIZE
        elif direction == "LEFT":
            x -= CELL_SIZE
        elif direction == "RIGHT":
            x += CELL_SIZE

        new_head = (x, y)
        snake.insert(0, new_head)

        if new_head == food:
            score += 1
            food = (random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                    random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)
        else:
            snake.pop()

        if (x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT
                or new_head in snake[1:]):
            game_over(score)

        screen.blit(bg_image, (0, 0))
        draw_snake(snake)
        draw_food(food)

        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(10 + score // 5)


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
