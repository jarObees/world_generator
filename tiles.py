TILE_SIZE = 4

class Tile:
    def __init__(self, elevation, temperature):
        self.elevation = elevation
        self.temperature = temperature
        self.tile_size = TILE_SIZE
        self.biome = None
        self.color = None

    def get_biome(self, biomes):
        for i, (biome, color) in enumerate(biomes.biomes.items()):
            if self.elevation <= biomes.max_biome_heights[i]:
                self.biome = biome
                self.color = color
                break