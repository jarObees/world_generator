from config import *
from terrain import Terrain
import pygame
import sys

pygame.init()

# Pygame Setup
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("World Generator")
clock = pygame.time.Clock()


def main():
    terrain = Terrain(111, 111)
    terrain.generate()
    #terrain.plot()

    while True:
        print("I AM LOOPING")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit
        terrain.trouble_shoot()
        terrain.draw(window)

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()