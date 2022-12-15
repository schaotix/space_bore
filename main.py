import pygame
from pygame.locals import *
import random

# Basic initializations
pygame.init()
size = width, height = (1200, 800)
running = True
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Space Bore")
bg_img = pygame.image.load("space.jpg")

# Screen setup variables
first_col = width / 4 + random.randint(0, 300)
second_col = width / 4 + random.randint(301, 600)
third_col = width / 4 + random.randint(601, 900)
fourth_col = width / 4 + random.randint(901, 1200)


class Ship(object):
    def __init__(self):
        self.ship = pygame.image.load("ship.png")
        self.ship_loc = self.ship.get_rect()
        self.ship_loc.center = width / 2, height * 0.8
        self.vel = 1

class Rock(object):
    def __init__(self):
        self.rock = pygame.image.load("rock.png")
        self.rock_loc = self.rock.get_rect()
        self.rock_loc.center = -200, -200
        self.vel = 1

pygame.display.update()

ship = Ship()
rock = Rock()
while running:
    rock.rock_loc[1] += rock.vel
    if rock.rock_loc[1] > height:
        rock.rock_loc[1] = -200
        coord = random.randint(0, 4)
        if coord == 0:
            rock.rock_loc.center = first_col, -200
        if coord == 1:
            rock.rock_loc.center = second_col, -200
        if coord == 2:
            rock.rock_loc.center = third_col, -200
        if coord == 3:
            rock.rock_loc.center = fourth_col, -200

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[K_RIGHT] and ship.ship_loc[0] <= width:
        ship.ship_loc[0] += ship.vel
        if ship.ship_loc[0] > width:
            ship.ship_loc[0] = 0
    if keys[K_LEFT] and ship.ship_loc[0] >= 0:
        ship.ship_loc[0] -= ship.vel
        if ship.ship_loc[0] < 0:
            ship.ship_loc[0] = width

    # Game Over
    #if ship_loc[0] == rock_loc[1]+72:
        #print("BOOM!")

    screen.blit(bg_img, (0, 0))
    screen.blit(ship.ship, ship.ship_loc)
    screen.blit(rock.rock, rock.rock_loc)
    pygame.display.update()

pygame.quit()
