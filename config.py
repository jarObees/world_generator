# Window Settings
WIN_WIDTH = 800
WIN_HEIGHT = 800
FPS = 8
TILE_SIZE = 4

# Generation settings
POLES = True

# Perlin Noise Settings.
OCTAVES = 8
RAND_SEED = True
UNIQUE_SEED = 1

# Biome Settings. Length of WEIGHTS_ lists must match length of BIOMES.
BIOMES = {
            "deep_ocean": (23, 91, 99),
            "ocean": (51, 150, 163),
            "shallow_ocean": (81, 219, 237),
            "beach": (219, 227, 61),
            "nature": (60, 130, 49),
            "mountain": (125, 125, 125),
            "snow": (255, 255, 255)
        }

WEIGHTS_ISLAND = [3, 2, 1, 1, 1, 1, 1.2]
WEIGHTS_LAKES = [1, 1, 1, 0.5, 2, 1, 2]

WEIGHTS = WEIGHTS_ISLAND
