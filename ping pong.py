import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Game variables
paddle_width = 10
paddle_height = 100
paddle_speed = 5
ball_size = 20
ball_speed = 5

# Player settings
player1_score = 0
player2_score = 0

# Paddle positions
player1_y = (screen_height - paddle_height) // 2
player2_y = (screen_height - paddle_height) // 2

# Ball position and velocity
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_dx = random.choice([-1, 1]) * ball_speed
ball_dy = random.choice([-1, 1]) * ball_speed

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_y > 0:
        player1_y -= paddle_speed
    if keys[pygame.K_s] and player1_y < screen_height - paddle_height:
        player1_y += paddle_speed
    if keys[pygame.K_UP] and player2_y > 0:
        player2_y -= paddle_speed
    if keys[pygame.K_DOWN] and player2_y < screen_height - paddle_height:
        player2_y += paddle_speed

    # Move the ball
    ball_x += ball_dx
    ball_y += ball_dy

    # Ball collision with walls
    if ball_y <= 0 or ball_y >= screen_height - ball_size:
        ball_dy *= -1

    # Ball collision with paddles
    if ball_x <= paddle_width and player1_y <= ball_y <= player1_y + paddle_height:
        ball_dx *= -1
    elif ball_x >= screen_width - paddle_width - ball_size and player2_y <= ball_y <= player2_y + paddle_height:
        ball_dx *= -1

    # Ball out of bounds
    if ball_x <= 0:
        player2_score += 1
        ball_x = screen_width // 2
        ball_y = screen_height // 2
        ball_dx = random.choice([-1, 1]) * ball_speed
        ball_dy = random.choice([-1, 1]) * ball_speed
    elif ball_x >= screen_width - ball_size:
        player1_score += 1
        ball_x = screen_width // 2
        ball_y = screen_height // 2
        ball_dx = random.choice([-1, 1]) * ball_speed
        ball_dy = random.choice([-1, 1]) * ball_speed

    # Clear the screen
    screen.fill(black)

    # Draw paddles and ball
    pygame.draw.rect(screen, white, (0, player1_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, white, (screen_width - paddle_width, player2_y, paddle_width, paddle_height))
    pygame.draw.ellipse(screen, white, (ball_x, ball_y, ball_size, ball_size))

    # Display scores
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"{player1_score} - {player2_score}", True, white)
    screen.blit(score_text, (screen_width // 2 - 36, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
