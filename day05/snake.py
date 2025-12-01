import pygame, random

# Initialize pygame
pygame.init()

# Set display window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("~~SNEKE~~")

# Set FSP and clock
FPS = 20
clock = pygame.time.Clock()

# Set game values
SNAKE_SIZE = 20
head_x = WINDOW_WIDTH // 2
head_y = WINDOW_HEIGHT + 100 / 2
snake_dx = 0
snake_dy = 0
score = 0
# Set colors
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
RED = (255, 0, 0)
DARKRED = (150, 0, 0)
WHITE = (255, 255, 255)

# Set fonts
font = pygame.font.SysFont('gabriola', 48)
# Set text

title_text = font.render("~~Snake~~", True, GREEN, DARKRED)  # make a text object
title_rect = title_text.get_rect()  # gets the box containing the text object
title_rect.center = (WINDOW_WIDTH // 2,
                     WINDOW_HEIGHT // 2)  # places the box containing the text object's center to the middle of the screen.

score_text = font.render("Score:0 " + str(score), True, GREEN, DARKRED)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

game_over_text = font.render("Game Over!", True, GREEN, DARKRED)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2

continue_text = font.render("Press Any Key to Continue", True, GREEN, DARKRED)
continue_rect = continue_text.get_rect()
continue_rect.center = WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2

pick_up_sound = pygame.mixer.Sound("pickup_sound.wav")
# Set images (in this case, use simple rects...so just create their coordinates)
# For a rectangle you need (top-left x, top-left y, width, height)
apple_coord = (500, 500, SNAKE_SIZE, SNAKE_SIZE)
apple_rect = pygame.draw.rect(display_surface, RED, apple_coord)

head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
head_rect = pygame.draw.rect(display_surface, GREEN, head_coord)

body_coords = []


# The main game loop
running = True
is_paused = False
while running:
    # Check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Move the snake
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_dx = -1 * SNAKE_SIZE
                snake_dy = 0
            if event.key == pygame.K_RIGHT:
                snake_dx = SNAKE_SIZE
                snake_dy = 0
            if event.key == pygame.K_DOWN:
                snake_dy = SNAKE_SIZE
                snake_dx = 0
            if event.key == pygame.K_UP:
                snake_dy = -1 * SNAKE_SIZE
                snake_dx = 0

    # Add the head coordinate to the first index of the body coordinate list
    # This will essentilalyl move all of the snakes body by one position in the list
    body_coords.insert(0, head_coord)
    body_coords.pop()

    # Update the x,y position of the snakes head and make a new coordinate
    snake_dx = head_dx
    snake_dy = head_y
    head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)

    # Check for game over
    if head_rect.left < 0 or head_rect.right > WINDOW_WIDTH or head_rect.top < 0 or head_rect.bottom > WINDOW_HEIGHT or head_coord in body_coords:

    # Check for collisions

    # Update HUD

    # Fill the surface

    # Blit HUD

    # Blit assets

    # Update display and tick clock

# End the game
pygame.quit()
