import pygame
import random

# Initialize pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Screen dimensions
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Paddle dimensions and speed
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 60
PADDLE_SPEED = 5

# Ball dimensions and speed
BALL_WIDTH = 15
BALL_VELOCITY = 5
ball_x_velocity = BALL_VELOCITY
ball_y_velocity = BALL_VELOCITY

# Create screen and clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pong')
clock = pygame.time.Clock()

# Score Initialization
font = pygame.font.Font(None, 74)
player_score = 0
ai_score = 0

# Define the ball and paddles
ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_WIDTH // 2, SCREEN_HEIGHT // 2 - BALL_WIDTH // 2, BALL_WIDTH, BALL_WIDTH)
left_paddle = pygame.Rect(0, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(SCREEN_WIDTH - PADDLE_WIDTH, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Define AI movement for the right paddle
def ai_paddle_movement(paddle, ball):
    if ball.y > paddle.y + paddle.height / 2:
        paddle.y += PADDLE_SPEED
    elif ball.y < paddle.y + paddle.height / 2:
        paddle.y -= PADDLE_SPEED

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s] and left_paddle.bottom < SCREEN_HEIGHT:
        left_paddle.y += PADDLE_SPEED
    
    # AI movement for the right paddle
    ai_paddle_movement(right_paddle, ball)

    ball.x += ball_x_velocity
    ball.y += ball_y_velocity

    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_y_velocity = -ball_y_velocity

    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_x_velocity = -ball_x_velocity

    if ball.left <= 0:
        ai_score += 1
        ball.x = SCREEN_WIDTH // 2 - BALL_WIDTH // 2
        ball.y = SCREEN_HEIGHT // 2 - BALL_WIDTH // 2
        ball_x_velocity = BALL_VELOCITY

    if ball.right >= SCREEN_WIDTH:
        player_score += 1
        ball.x = SCREEN_WIDTH // 2 - BALL_WIDTH // 2
        ball.y = SCREEN_HEIGHT // 2 - BALL_WIDTH // 2
        ball_x_velocity = -BALL_VELOCITY

    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT))
    
    # Display the scores
    player_text = font.render(str(player_score), True, WHITE)
    screen.blit(player_text, (SCREEN_WIDTH / 4, 10))
    ai_text = font.render(str(ai_score), True, WHITE)
    screen.blit(ai_text, (3 * SCREEN_WIDTH / 4, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()