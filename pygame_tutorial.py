import pygame, sys

pygame.init()
clock = pygame.time.Clock()

# Game Variables
fps = 60
screen_width = 800
screen_height = 600

# Game Display Settings
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tutorial Game")

while True:
    # check for the user to exit the window and then quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    clock.tick(fps)