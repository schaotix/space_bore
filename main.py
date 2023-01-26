import pygame
from pygame.locals import *
import random
import math

pygame.init()
pygame.mixer.init()

hit = pygame.mixer.Sound("assets/explosion.wav") # Created with jsfxr https://sfxr.me/
endgame = pygame.mixer.Sound("assets/gameover.wav") # Created with jsfxr https://sfxr.me/
size = width, height = (1200, 800)
font = pygame.font.SysFont("Times", 30, True)
screen = pygame.display.set_mode(size)
red = (255, 0, 0)
pygame.display.set_caption("Spacer - Michael Mandeville 2023")
bg_img = pygame.image.load("assets/space.jpg")
hit_cooldown = pygame.USEREVENT + 1
game_over = pygame.USEREVENT + 2
pygame.display.update()


class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.ship = pygame.image.load("assets/ship.png")
        self.ship_loc = self.ship.get_rect()
        self.ship_loc.center = width / 2, height * 0.8
        self.cooldown = False
        self.life = 5
        self.level = 0
        self.vel = 1

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[K_RIGHT] and ship.ship_loc[0] <= width:
            self.ship_loc.move_ip(self.vel, 0)
            if self.ship_loc[0] > width:
                self.ship_loc[0] = 0
        if keys[K_LEFT] and self.ship_loc[0] >= 0:
            self.ship_loc.move_ip(-self.vel, 0)
            if self.ship_loc[0] < 0:
                self.ship_loc[0] = width
        if self.ship_loc.colliderect(rock.rock_loc):
            self.shipHit()

    def shipHit(self):
        if not self.cooldown:
            self.cooldown = True
            pygame.time.set_timer(hit_cooldown, 1000)
            self.life -= 1
            if self.life > 0:
                pygame.mixer.Sound.play(hit)
                print("Hit!")
            else:
                pygame.event.post(pygame.event.Event(game_over))
            pygame.display.update()


class Rock(object):
    def __init__(self):
        self.rock = pygame.image.load("assets/rock.png")
        self.rock_loc = self.rock.get_rect()
        self.rock_loc.center = -200, -200
        self.vel = 1


ship = Ship()
rock = Rock()


def updateScore():
    score = ship.level * 100
    return score


def updateRock():
    column = random.randint(0, 1200)
    rock.rock_loc[1] += rock.vel
    if rock.rock_loc[1] > height:
        rock.rock_loc[1] = -200
        rock.rock_loc.center = column, -200


def endTitle(score):
    pygame.mixer.Sound.play(endgame)
    if score > 0:
        final = font.render("Congratulations, your score is " + str(score), True, (0, 0, 255))
        screen.fill(red)
        screen.blit(final, (350, 400))
    else:
        final = font.render("Oh no! The universe is doomed!", True, (0, 0, 255))
        screen.fill(red)
        screen.blit(final, (400, 400))
    pygame.display.update()
    pygame.time.delay(3000)
    return False


def redrawGameWindow():
    screen.blit(bg_img, (0, 0))
    screen.blit(ship.ship, ship.ship_loc)
    screen.blit(rock.rock, rock.rock_loc)
    level = font.render("Level: " + str(ship.level), True, (255, 255, 255))
    text = font.render("Life: " + str(ship.life), True, (255, 0, 0))
    screen.blit(level, (50, 50))
    screen.blit(text, (50, 100))
    pygame.display.update()


def main():
    counter = 0
    running = True
    while running:

        counter += 1
        if counter == 3028:
            rock.vel += 0.25
            counter = 0
            ship.level += 1

        for event in pygame.event.get():
            if event.type == QUIT:
                print(f"Congratulations, your score is: {(updateScore())}")
                running = False
            if event.type == hit_cooldown:
                ship.cooldown = False
                pygame.time.set_timer(hit_cooldown, 0)
            if event.type == game_over:
                running = endTitle(updateScore())

        ship.update()
        updateRock()
        redrawGameWindow()

    pygame.quit()


if __name__ == "__main__":
    main()
