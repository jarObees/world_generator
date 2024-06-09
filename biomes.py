weights_island = [3, 2, 1, 1, 1, 1, 1.2]
weights_lakes = [1, 1, 1, 0.5, 2, 1, 2]

class Biomes:
    def __init__(self, min, max):
        self.min_perlin = min
        self.max_perlin = max
        # Rank from lowest to highest
        self.biomes = {
            "deep_ocean": (23, 91, 99),
            "ocean": (51, 150, 163),
            "shallow_ocean": (81, 219, 237),
            "beach": (219, 227, 61),
            "nature": (60, 130, 49),
            "mountain": (125, 125, 125),
            "snow": (255, 255, 255)
        }
        self.default_weights = [1 for _ in range(len(self.biomes))]
        self.max_biome_heights = []

    def gen_biomes(self, weights=weights_lakes):
        if weights is None:
            weights = self.default_weights
        weight_sum = sum(weights)

        # Calculate max elevation for each biome in biomes_list, using weight values.
        max_biome_heights = []
        prev_elevation = 0
        for i, biome in enumerate(self.biomes):
            max_elevation = (weights[i] / weight_sum) + prev_elevation
            max_biome_heights.append(max_elevation)
            prev_elevation = max_elevation
        max_biome_heights[-1] = 1

        self.max_biome_heights = max_biome_heights






