import pygame
import os

# Initialize important systems
pygame.font.init() # Initialize the font engine
pygame.mixer.init() # Initialize the sound system

# Game Settings Section ------------

# Setup window attributes
HEIGHT, WIDTH = 500, 900 # Size of the window
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Tutorial Game')

# Color constants in RGB format
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

# Create border that seperates the two spaceships and constrains where they can fly
BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

# Variables to hold the sound files that will be used when shooting and
# when bullets hit other spaceship
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Grenade_1.mp3'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Gun_Silencer.mp3'))

# Create fonts for the Health and Winner displays
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

# Other variables
FPS = 60 # Max frames per second
VEL = 5 # Move by this number of pixels each move (velocity of ships)
BULLET_VEL = 7 # Move by this number of pixes (velocity of bullets)
MAX_BULLETS = 3
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40 # Used to resize the spaceship pictures

# Identify custom event for when the yellow/red spaceship is hit
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

# Load, scale and rotate spaceship images
YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

# Load and scale the background space image
SPACE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))

# Game function section ------------

# Function that handles drawing the game graphics and objects
def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    # Load background image of space
    WIN.blit(SPACE, (0,0))
    # Draw the border between the two ships in the middle of the screen
    pygame.draw.rect(WIN, BLACK, BORDER)

    # Setup and display the health of each spaceship
    red_health_text = HEALTH_FONT.render("Health: " + str(red_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health), 1, WHITE)
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10, 10))

    # Draw the spaceships on the scren in their correct location
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    # Draw any bullets that have been fired
    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    pygame.display.update()

# Function that handles movement for the yellow spaceship
def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0: #left
        yellow.x -= VEL 
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x: #right
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0: #up
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15: #down
        yellow.y += VEL

# Function that handles movement of the red spaceship
def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width: #left
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH: #right
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0: #up
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 15: #down
        red.y += VEL

# Function that handles moving bullets and detecting collisions
def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)

# Function that display who the winner is in middle of screen
def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

# Main function of program where execution starts
def main():

    # Spaceship objects
    red = pygame.Rect(700,300,SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100,300,SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    
    # Empty lists to store bullets that have been fired
    red_bullets = []
    yellow_bullets = []

    # Health of each spaceship
    red_health = 10
    yellow_health = 10

    # Game clock that triggers how often we update the game (FPS)
    clock = pygame.time.Clock()

    # Game loop that is always true until we exit the window
    run = True
    while run:
        clock.tick(FPS) # ensure we do not run too fast; lock FPS at 60
        
        # Check every event and respond to those that we care about
        for event in pygame.event.get():

            # User has clicked the X and wishes to exit the game
            if event.type == pygame.QUIT:
                run = False
                exit()

            if event.type == pygame.KEYDOWN: # A key has been pressed

                # Yellow spaceship uses the Left Control button to fire
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    yellow_bullet = pygame.Rect(yellow.x + yellow.height, yellow.y + yellow.width//2, 10, 5)
                    yellow_bullets.append(yellow_bullet)
                    BULLET_FIRE_SOUND.play()

                # Red spaceship uses the Right Control button to fire
                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    red_bullet = pygame.Rect(red.x, red.y + SPACESHIP_WIDTH//2, 10, 5)
                    red_bullets.append(red_bullet)
                    BULLET_FIRE_SOUND.play()
            
            # Respond to our custom events that indicate that a spaceship 
            # has been hit by a bullet
            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()
            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()

        # Determine if the game has been won or not and by whom
        winner_text = ""
        if red_health <= 0:
            winner_text = "Yellow Wins!"
        if yellow_health <= 0:
            winner_text = "Red Wins!"
        # There is a winner
        if winner_text != "":
            draw_winner(winner_text)
            break
        
        # Use this method so that we can handle more than one 
        # key being pressed at same time
        keys_pressed = pygame.key.get_pressed()
        # Pass keys pressed to key press handlers for each spaceship
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)

        # Call bullet handler function
        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        # Draw window and update
        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)
    # Once game is over and we are out of infinite loop, restart the game
    main()

# If this file is not being used as an import, call the main function to run it
if __name__ == '__main__': # indicates that the file we are in is the one running program
    main()