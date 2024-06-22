from config import *

class Tile:
    def __init__(self, elevation, temperature):
        self.elevation = elevation
        self.temperature = temperature
        self.tile_size = TILE_SIZE
        self.biome = None
        self.sub_biome = None
        self.color = None

    def get_biome(self, biomes):
        for i, biome in enumerate(biomes.biomes):
            if self.elevation <= biome.max_elevation:
                self.biome = biome
                self.color = biome.color
                break