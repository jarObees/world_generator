from config import *

class Biomes:
    def __init__(self, min, max):
        self.min_perlin = min
        self.max_perlin = max
        # Rank from lowest to highest
        self.biomes = BIOMES
        self.max_biome_heights = []

    def gen_biomes(self):
        weight_sum = sum(WEIGHTS)

        # Calculate max elevation for each biome in biomes_list, using weight values.
        max_biome_heights = []
        prev_elevation = 0
        for i, biome in enumerate(self.biomes):
            max_elevation = (WEIGHTS[i] / weight_sum) + prev_elevation
            max_biome_heights.append(max_elevation)
            prev_elevation = max_elevation

        self.max_biome_heights = max_biome_heights






