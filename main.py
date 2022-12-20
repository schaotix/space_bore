import pygame
from pygame.locals import *
import random
import sys


# Basic initializations
pygame.init()
size = width, height = (1200, 800)
running = True
font = pygame.font.SysFont("Times", 30, True)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Space Bore")
bg_img = pygame.image.load("space.jpg")
endgame = font.render("YOU LOSE AND THE GALAXY IS LOST.", True, (255, 0, 0))
hit_cooldown = pygame.USEREVENT + 1
pygame.display.update()


class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.ship = pygame.image.load("ship.png")
        self.ship_loc = self.ship.get_rect()
        self.ship_loc.center = width / 2, height * 0.8
        self.cooldown = False
        self.life = 5
        self.score = 0
        self.vel = 1

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[K_RIGHT] and ship.ship_loc[0] <= width:
            self.ship_loc[0] += self.vel
            if self.ship_loc[0] > width:
                self.ship_loc[0] = 0
        if keys[K_LEFT] and self.ship_loc[0] >= 0:
            self.ship_loc[0] -= self.vel
            if self.ship_loc[0] < 0:
                self.ship_loc[0] = width
        if self.ship_loc.colliderect(rock.rock_loc):
            self.shipHit()
        if not self.ship_loc.colliderect(rock.rock_loc) and \
            rock.rock_loc.y >= 800:
            print("score")

    def shipHit(self):
        if not self.cooldown:
            self.cooldown = True
            pygame.time.set_timer(hit_cooldown, 1000)
            self.life -= 1
            if self.life > 0:
                print("Hit!")
            else:
                sys.exit()
            pygame.display.update()


def updateRock():
    column = random.randint(0, 1200)
    rock.rock_loc[1] += rock.vel
    if rock.rock_loc[1] > height:
        rock.rock_loc[1] = -200
        rock.rock_loc.center = column, -200


class Rock(object):
    def __init__(self):
        self.rock = pygame.image.load("rock.png")
        self.rock_loc = self.rock.get_rect()
        self.rock_loc.center = -200, -200
        self.vel = 1


def redrawGameWindow():
    screen.blit(bg_img, (0, 0))
    screen.blit(ship.ship, ship.ship_loc)
    screen.blit(rock.rock, rock.rock_loc)
    score = font.render("Score: " + str(ship.score), True, (255, 255, 255))
    text = font.render("Life: " + str(ship.life), True, (255, 0, 0))
    screen.blit(score, (50, 50))
    screen.blit(text, (50, 100))
    pygame.display.update()


ship = Ship()
rock = Rock()
while running:

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == hit_cooldown:
            ship.cooldown = False
            pygame.time.set_timer(hit_cooldown, 0)

    ship.update()
    updateRock()

    redrawGameWindow()

pygame.quit()
