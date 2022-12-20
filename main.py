import pygame
from pygame.locals import *
import random


# Basic initializations
pygame.init()
size = width, height = (1200, 800)
running = True
font = pygame.font.SysFont("Times", 30, True)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Space Bore")
bg_img = pygame.image.load("space.jpg")
hit_cooldown = pygame.USEREVENT + 1
pygame.display.update()


class Ship(object):
    def __init__(self):
        self.ship = pygame.image.load("ship.png")
        self.ship_loc = self.ship.get_rect()
        self.ship_loc.center = width / 2, height * 0.8
        self.cooldown = False
        self.vel = 1

    def shipHit(self):
        if not self.cooldown:
            self.cooldown = True
            pygame.time.set_timer(hit_cooldown, 1000)
            print("Hit!")
            pygame.display.update()


class Rock(object):
    def __init__(self):
        self.rock = pygame.image.load("rock.png")
        self.rock_loc = self.rock.get_rect()
        self.rock_loc.center = -200, -200
        self.vel = 1


def incomingRock():
    column = random.randint(0, 1200)
    rock.rock_loc[1] += rock.vel
    if rock.rock_loc[1] > height:
        rock.rock_loc[1] = -200
        rock.rock_loc.center = column, -200


def moveShip():
    keys = pygame.key.get_pressed()
    if keys[K_RIGHT] and ship.ship_loc[0] <= width:
        ship.ship_loc[0] += ship.vel
        if ship.ship_loc[0] > width:
            ship.ship_loc[0] = 0
    if keys[K_LEFT] and ship.ship_loc[0] >= 0:
        ship.ship_loc[0] -= ship.vel
        if ship.ship_loc[0] < 0:
            ship.ship_loc[0] = width


def redrawGameWindow():
    screen.blit(bg_img, (0, 0))
    screen.blit(ship.ship, ship.ship_loc)
    screen.blit(rock.rock, rock.rock_loc)
    pygame.display.update()


ship = Ship()
rock = Rock()
while running:
    incomingRock()

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    moveShip()

    if ship.ship_loc.colliderect(rock.rock_loc):
        print("BOOM!")
    #if (ship.ship_loc[1] <= rock.rock_loc[1] + rock.rock_loc[2] <= ship.ship_loc[1] + ship.ship_loc[2] and
        #ship.ship_loc[0] <= rock.rock_loc[0] + rock.rock_loc[3] <= ship.ship_loc[0] + ship.ship_loc[3]) or \
        #(rock.rock_loc[1] + rock.rock_loc[2] >= ship.ship_loc[1] and
        #ship.ship_loc[0] + ship.ship_loc[3] >= rock.rock_loc[0] >= ship.ship_loc[0]):

    redrawGameWindow()

pygame.quit()
