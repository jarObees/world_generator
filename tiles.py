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

    def get_sub_biome(self):
        for i, sub_biome in enumerate(self.biome.sub_biomes):
            if sub_biome. #TODO <= sub_biome.max_elevation:
                self.sub_biome = sub_biome
                self.color = sub_biome.color
                break