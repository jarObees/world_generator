# Window Settings
WIN_WIDTH = 400
WIN_HEIGHT = 400
FPS = 8
TILE_SIZE = 1

# Generation settings
POLES = True

# Perlin Noise Settings.
OCTAVES = 8
RAND_SEED = True
UNIQUE_SEED = 1

# Dictionary holds biome names and their associated colors (in RGB)
BIOMES = {
            "deep_ocean": (23, 91, 99),
            "ocean": (51, 150, 163),
            "shallow_ocean": (81, 219, 237),
            "beach": (219, 227, 61),
            "nature": (60, 130, 49),
            "mountain": (125, 125, 125),
            "snow": (255, 255, 255)
        }

# Some example setups of potential weights you can assign to each biome respectively.
# Higher number indicates a larger favoring towards that biome tile.
WEIGHTS_ISLAND = [3, 2, 1, 1, 1, 1, 1.2]
WEIGHTS_LAKES = [1, 1, 1, 0.5, 2, 1, 2]

WEIGHTS = WEIGHTS_ISLAND
