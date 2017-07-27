__author__ = 'dmadden'
import pygame
from pygame.locals import *
from walker import Walker
from structures.triangle import Triangle
from structures.square import Square
from structures.picture import Picture


W, H = (800, 600)

structure = Picture
walker = Walker(W, H, structure)

def update(surface, walker):
    draw(surface, walker.cur_pos)
    walker.walk()

def draw(surface, point):
    pygame.draw.circle(surface, (255,255,255), point, 1, 1)

def main():
    pygame.init()
    surface = pygame.display.set_mode((W, H))
    surface.fill((0))
    running = True
    iters = 0
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                running = False
                break
        if running:
            update(surface, walker)
            if iters > 20000:
                pygame.display.update()
                iters = 0
        iters += 1



if __name__ == "__main__":
    main()