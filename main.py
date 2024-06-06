from terrain import Terrain
import matplotlib.pyplot as plt
import pygame
import sys

pygame.init()
WIN_WIDTH = 800
WIN_HEIGHT = 800
CELL_SIZE = 20
FPS = 8

# Pygame Setup
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("World Generator")
clock = pygame.time.Clock()


def main():
    # x and y
    terrain = Terrain(101, 201)
    terrain.generate(octaves=4)
    terrain.plot()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit

            terrain.draw()
            pygame.display.update()
            clock.tick(FPS)

if __name__ == "__main__":
    main()