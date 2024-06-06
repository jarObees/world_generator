

class Tile:
    def __init__(self, elevation, temperature):
        self.elevation = elevation
        self.temperature = temperature
        self.biome = None

    def gen_biome(self, biomes):
        for i, biome in enumerate(biomes):
            if self.elevation <= biomes.max_biome_heights[i]:
                self.biome = biome

    def draw(self):




