import pygame, sys, os, random

class Crosshair(pygame.sprite.Sprite):
    def __init__(self, picture_path, gun_sound):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.gunshot = pygame.mixer.Sound(gun_sound)
    def shoot(self):
        self.gunshot.play()
        pygame.sprite.spritecollide(crosshair, target_group, True)
    def update(self):
        self.rect.center = pygame.mouse.get_pos()

class Target(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load(os.path.join('Assets', 'bg_blue.png'))
background = pygame.transform.scale(background, (screen_width, screen_height))
pygame.mouse.set_visible(False)

# Crosshair
crosshair = Crosshair(os.path.join('Assets', 'crosshair_outline_small.png'), os.path.join('Assets', 'gunshot2.wav'))
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

# Targets
target_group = pygame.sprite.Group()
for target in range(30):
    new_target = Target(os.path.join('Assets', 'duck_target_white.png'), random.randrange(0,screen_width), random.randrange(0,screen_height))
    target_group.add(new_target)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()

    pygame.display.flip()
    screen.blit(background, (0,0))
    target_group.draw(screen) # draw targets first before the crosshair or they will be behind
    crosshair_group.draw(screen)
    crosshair_group.update()
    clock.tick(60)