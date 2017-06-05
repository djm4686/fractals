__author__ = 'dmadden'
import pygame
from pygame.locals import *
from walker import Walker
from structures.triangle import Triangle


W, H = (800, 600)

structure = Triangle
walker = Walker(W, H, structure)

def update(surface, walker):
    draw(surface, walker.cur_pos)
    walker.walk()

def draw(surface, point):
    pygame.draw.circle(surface, (0,0,0), point, 2)

def main():
    pygame.init()
    surface = pygame.display.set_mode((W, H))
    surface.fill((255,255,255))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                break
        update(surface, walker)
        pygame.display.update()



if __name__ == "__main__":
    main()