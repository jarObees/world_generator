from config import *
from tiles import Tile
from biomes import Biomes
from perlin_noise import PerlinNoise
import matplotlib.pyplot as plt
import numpy as np
import math as m
import pygame, random


class Terrain:
    def __init__(self, column_max, row_max):
        self.column_max = row_max
        self.row_max = column_max
        self.terrain = np.zeros((self.column_max, self.row_max))
        self.tiles = [[None for _ in range(column_max)] for _ in range(row_max)]

        # Values generated in class have range [-sqrt(N/4), sqrt(N/4)] where N is the number of dimensions
        self.min = -m.sqrt(1/2)
        self.max = m.sqrt(1/2)
        # Order from lowest to highest.
        self.biomes = Biomes(self.min, self.max)

    # Normalizes noise_values to a range [0, 1] for easier use in Tile.gen_biome method.
    def _normalize(self, noise_value: float) -> float:
        norm_value = (noise_value - self.min) / (self.max - self.min)
        return norm_value

    def plot_temp(self, array):
        plt.imshow(array, cmap='gray')
        plt.colorbar()
        plt.show()

    #TODO: Make this work with even dimensions.
    def _gen_temperature(self, poles: bool, temp_const=0.1) -> list[float]:
        if poles:
            temps = np.zeros_like(self.terrain)
            # if odd
            if self.row_max % 2 != 0:
                # Since extreme poles will be modified by -temp_const value and equator will be temp_const
                temp_range = 2 * temp_const
                equator = self.row_max // 2
                for i in range(equator):
                    # Start at poles, and move row by row closer to equator.
                    # For every additional row add + temp_range / (midpoint - 1), so that it adds equal values up to
                    # But not including the center row (equator), since we know this value to be the temp_const
                    temp_adjustment = -temp_const + i*(temp_range / equator)
                    temps[i, :] = temp_adjustment
                    temps[-(i + 1), :] = temp_adjustment
                temps[equator, :] = temp_const

                #self.plot_temp(temps)
                return temps

    def generate(self):
        if RAND_SEED:
            seed = random.randint(1, 10**5)
        else:
            seed = UNIQUE_SEED

        self.biomes.gen_biomes()
        terrain_temps = self._gen_temperature(POLES)

        # Generates tiles with elevation and terrain_temps based off of normalized perlin noise.
        noise = PerlinNoise(octaves=OCTAVES, seed=seed)
        for x in range(self.column_max):
            for y in range(self.row_max):
                self.terrain[x][y] = self._normalize(noise([x / self.column_max, y / self.row_max]))
                elevation = self.terrain[x][y]
                temperature = terrain_temps[x][y]
                # Create Tile object
                self.tiles[x][y] = Tile(elevation, temperature)
                self.tiles[x][y].get_biome(self.biomes)

    def plot(self):
        plt.imshow(self.terrain, cmap='gray')
        plt.colorbar()
        plt.show()

    def draw(self, window):
        for x in range(self.column_max):
            for y in range(self.row_max):
                tile = self.tiles[x][y]
                color = tile.color
                print(color)
                pygame.draw.rect(window, color, (x * tile.tile_size, y * tile.tile_size, tile.tile_size, tile.tile_size))

    def trouble_shoot(self):
        for x in range(self.column_max):
            for y in range(self.row_max):
                tile = self.tiles[x][y]
                if tile.biome is None:
                    print("HERE!!")
                    print("OK")