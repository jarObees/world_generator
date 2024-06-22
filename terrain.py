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

    # Generates temp_modifiers that will be summed with perlin noise to create new "temp" value for tile.
    def gen_temperature_mod(self) -> list[float]:
        if POLES:
            temps_mod = np.zeros_like(self.terrain)
            temp_range = 2 * TEMP_CONST
            equator = self.row_max // 2
            if self.row_max % 2 != 0:
                for i in range(equator):
                    # Calculate temperature adjustment for each row
                    temp_adjustment = -TEMP_CONST + i * (temp_range / equator)
                    temps_mod[i, :] = temp_adjustment
                    temps_mod[-(i + 1), :] = temp_adjustment
                temps_mod[equator, :] = TEMP_CONST
            else:
                for i in range(equator - 1):
                    temp_adjustment = -TEMP_CONST + i * (temp_range / equator)
                    temps_mod[i, :] = temp_adjustment
                    temps_mod[-(i + 1), :] = temp_adjustment
                temps_mod[equator, :] = TEMP_CONST
                temps_mod[equator - 1, :] = TEMP_CONST
            return temps_mod

    def generate(self):
        if RAND_SEED:
            seed = random.randint(1, 10**5)
        else:
            seed = UNIQUE_SEED

        # Generates tiles with elevation and terrain_temps based off of normalized perlin noise.
        terrain_temps = self.gen_temperature_mod()
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