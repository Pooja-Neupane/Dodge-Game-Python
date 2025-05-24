import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🚧 Dodge the Falling Blocks 🚧")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLOCK_COLOR = (255, 0, 0)
PLAYER_COLOR = (0, 0, 255)

# Player properties
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT - player_size
player_speed = 7

# Block properties
block_size = 50
block_speed = 5
block_list = []

# Font
font = pygame.font.SysFont("comicsans", 30)

# Clock
clock = pygame.time.Clock()

# Score
score = 0

# Function to create new block
def drop_blocks(block_list):
    if len(block_list) < 10:
        x_pos = random.randint(0, WIDTH - block_size)
        y_pos = 0
        block_list.append([x_pos, y_pos])

# Function to draw blocks
def draw_blocks(block_list):
    for block in block_list:
        pygame.draw.rect(screen, BLOCK_COLOR, (block[0], block[1], block_size, block_size))

# Function to update block positions
def update_blocks(block_list):
    global score
    for block in block_list:
        block[1] += block_speed
        if block[1] > HEIGHT:
            block_list.remove(block)
            score += 1

# Collision detection
def check_collision(player_x, player_y, block_list):
    for block in block_list:
        if (player_x < block[0] + block_size and
            player_x + player_size > block[0] and
            player_y < block[1] + block_size and
            player_y + player_size > block[1]):
            return True
    return False

# Game loop
game_over = False
while not game_over:
    screen.fill(WHITE)

    # Event listener
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Key control
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    # Drop blocks
    drop_blocks(block_list)
    update_blocks(block_list)
    draw_blocks(block_list)

    # Draw player
    pygame.draw.rect(screen, PLAYER_COLOR, (player_x, player_y, player_size, player_size))

    # Check collision
    if check_collision(player_x, player_y, block_list):
        game_over_text = font.render("Game Over! Score: " + str(score), True, BLACK)
        screen.blit(game_over_text, (WIDTH//2 - 150, HEIGHT//2))
        pygame.display.update()
        pygame.time.delay(2000)
        game_over = True
        break

    # Display score
    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(30)
