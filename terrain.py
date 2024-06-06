from perlin_noise import PerlinNoise
from tiles import Tile
from biomes import Biomes
import matplotlib.pyplot as plt
import numpy as np
import random
import math as m


class Terrain:
    # TO: DO X_MAX AND Y_MAX SHOULD BE THE OTHER WAY AROUND.
    def __init__(self, row_max, column_max):
        self.column_max = row_max
        self.row_max = column_max
        self.terrain = np.zeros((self.column_max, self.row_max))
        self.tiles = [[None for column in range(column_max)] for row in range(row_max)]

        # Values generated in class have range [-sqrt(N/4), sqrt(N/4)] where N is the number of dimensions
        self.min = -m.sqrt(1/2)
        self.max = m.sqrt(1/2)
        # Order from lowest to highest.
        self.biomes = Biomes(self.min, self.max)

    def _normalize(self, noise_value):
        new_noise_value = (noise_value - self.min) / (self.max - self.min)
        return new_noise_value

    def plot_temp(self, array):
        plt.imshow(array, cmap='gray')
        plt.colorbar()
        plt.show()

    #TODO: Make this work with even dimensions.
    def _gen_temperature(self, poles, temp_const=0.1) -> list[float]:
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

    def generate(self, octaves, seed=random.randint(1, 1000), poles=True):
        # Biome Setup
        self.biomes.gen_biomes()

        # Generate Tiles
        noise = PerlinNoise(octaves=octaves, seed=seed)
        temperatures: list[float] = self._gen_temperature(poles)
        for x in range(self.column_max):
            for y in range(self.row_max):
                self.terrain[x][y] = self._normalize(noise([x / self.column_max, y / self.row_max]))
                elevation = self.terrain[x][y]
                temperature = temperatures[x][y]
                # Create Tile object
                self.tiles[x][y] = Tile(elevation, temperature)
                #TODO Generate the correct biome in the passed-in Tile.
                self.tiles[x][y].gen_biome(self.biomes)

    def plot(self):
        plt.imshow(self.terrain, cmap='gray')
        plt.colorbar()
        plt.show()

    def draw(self):
        for x in range(self.column_max):
            for y in range(self.row_max):
                self.tiles[x][y].draw()
        pass
        #for x in range