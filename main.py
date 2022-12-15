import pygame
from pygame.locals import *
import random

size = width, height = (1200, 800)

pygame.init()
running = True
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Space Bore")

clock = pygame.time.Clock()
ship = pygame.image.load("ship.png")
rock = pygame.image.load("rock.png")
bg_img = pygame.image.load("space.jpg")
ship_vel = 3
rock_vel = 3

rock_loc = rock.get_rect()
first_col = width / 4 + random.randint(1, 300)
second_col = width / 4 + random.randint(301, 600)
third_col = width / 4 + random.randint(601, 900)
fourth_col = width / 4 + random.randint(901, 1200)

ship_loc = ship.get_rect()
ship_loc.center = width / 2, height * 0.8

pygame.display.update()


def drawGameBoard():
    screen.blit(bg_img, (0, 0))
    screen.blit(ship, ship_loc)
    screen.blit(rock, rock_loc)
    pygame.display.update()


while running:
    clock.tick(240)
    rock_loc[1] += rock_vel
    if rock_loc[1] > height:
        rock_loc[1] = -200
        coord = random.randint(0, 4)
        if coord == 0:
            rock_loc.center = first_col, -200
        if coord == 1:
            rock_loc.center = second_col, -200
        if coord == 2:
            rock_loc.center = third_col, -200
        if coord == 3:
            rock_loc.center = fourth_col, -200

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[K_RIGHT] and ship_loc[0] <= width:
        ship_loc[0] += ship_vel
        if ship_loc[0] > width:
            ship_loc[0] = 0
    if keys[K_LEFT] and ship_loc[0] >= 0:
        ship_loc[0] -= ship_vel
        if ship_loc[0] < 0:
            ship_loc[0] = width

    # Game Over - IN PROGRESS
    if ship_loc[0] == rock_loc[1]+72:
        print("BOOM!")

    drawGameBoard()

pygame.quit()
