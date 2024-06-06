
class Biomes:
    def __init__(self, min, max):
        self.min_perlin = min
        self.max_perlin = max
        # Rank from lowest to highest
        self.biomes_list = [
            "deep_ocean",
            "ocean",
            "shallow_ocean",
            "beach",
            "nature",
            "mountain",
            "snow"
        ]
        self.default_weights = [1 for _ in range(len(self.biomes_list))]
        self.max_biome_heights = []

    def gen_biomes(self, weights=None):
        if weights is None:
            weights = self.default_weights
        weight_sum = sum(weights)
        perlin_range = self.max_perlin - self.min_perlin

        # Calculate max elevation for each biome in biomes_list, using weight values.
        max_biome_heights = []
        prev_elevation = self.min_perlin
        for i, biome in enumerate(self.biomes_list):
            max_elevation = perlin_range * (weights[i] / weight_sum) + prev_elevation
            max_biome_heights.append(max_elevation)
            prev_elevation = max_elevation
        max_biome_heights[-1] = self.max_perlin

        self.max_biome_heights = max_biome_heights






