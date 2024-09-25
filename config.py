"""
For biomes_config.json, biome (not sub_biome) order matters; they are listed from lowest to highest elevation.
"""
# Window Settings
WIN_WIDTH = 800
WIN_HEIGHT = 800
FPS = 8

TILE_SIZE: int = 4
TILE_ROWS: int = 124
TILE_COLUMNS: int = 124

# Temperature Settings
POLES: bool = True
TEMP_CONST: float = 0.1

# Perlin Noise Settings.
OCTAVES = 8
RAND_SEED = True
UNIQUE_SEED = 1

# Biome Settings. Length of WEIGHTS_ lists must match length of BIOMES. Higher weight means more of that biome.
"""
BIOMES = {
            "deep_ocean": (23, 91, 99),
            "ocean": (51, 150, 163),
            "shallow_ocean": (81, 219, 237),
            "beach": (219, 227, 61),
            "nature": (60, 130, 49),
            "mountain": (125, 125, 125),
            "snow": (255, 255, 255),
        }

WEIGHTS_ISLAND = [3, 2, 1, 1, 1, 1, 1.2]
WEIGHTS_FORESTS = [1, 1, 1, 0.5, 2, 1, 2]

WEIGHTS = WEIGHTS_FORESTS
"""
SUB_BIOMES = True