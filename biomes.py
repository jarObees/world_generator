from dataclasses import dataclass, field
import json
from typing import List, Tuple, Union, Optional
from config import *
from perlin_noise import PerlinNoise
from random import randint
import numpy as np
import math as m

@dataclass
class Biome:
    name: str
    color: Tuple[int, int, int]
    weight: Union[int, float]
    sub_biomes: Optional[List['Biome']] = field(default=None)
    max_elevation: float = field(default=None)


class Biomes:
    def __init__(self, min: float, max: float, col_max: int, row_max: int):
        self.min_perlin = min
        self.max_perlin = max
        self.biomes_data: dict = self._biomes_file_load()
        self.biomes: List[Biome] = self._gen_biomes()
        self.terrain_col_max = col_max
        self.terrain_row_max = row_max

    def _biomes_file_load(self) -> dict:
        try:
            with open('biomes_config.json', 'r') as file:
                biomes = json.load(file)
            return biomes
        except FileNotFoundError:
            raise FileNotFoundError("ERROR: 'biomes_config.json' not found.")
        except json.JSONDecodeError:
            raise ValueError("ERROR: Failed to decode JSON from 'biomes_config'.json.")

    def _raise_error(self, error_type, value, parent):
        raise error_type(f"ERROR: {value} not detected in {parent}")

    def _extract_biome(self, name, data) -> Biome:
        try:
            color = tuple(data['color'])
            weight = data['weight']
        except KeyError as e:
            self._raise_error(KeyError, str(e), name)
        return Biome(name=name, color=color, weight=weight, is_sub=False)

    def _extract_sub_biomes(self, biome_data) -> List[Biome]:
        sub_biomes = []
        if 'sub_biomes' in biome_data and biome_data['sub_biomes'] is not None:
            for sub_name, sub_data in biome_data['sub_biomes'].items():
                if 'color' in sub_data:
                    sub_color = tuple(sub_data['color'])
                else:
                    self._raise_error(KeyError, 'color', sub_name)
                if 'weight' in sub_data:
                    sub_weight = sub_data['weight']
                else:
                    self._raise_error(KeyError, 'weight', sub_name)
                sub_biome = Biome(sub_name, sub_color, sub_weight, True)
                sub_biomes.append(sub_biome)
        return sub_biomes
    """
    get's all the biome info (name, color, and weight) from json file, then checks for sub_biomes
    and get's all their potential info (again, name, color and weight), and then at the end creates a complete biome class.
    """
    def _get_biome_weights(self, is_sub: bool, sub_biomes=None) -> list[Union[int, float]]:
        biome_weights = []
        if is_sub:
            biome_weights.append(3)
            for biome in sub_biomes:
                weight = biome.weight
                biome_weights.append(weight)
        else:
            for biome_data in self.biomes_data.values():
                if 'weight' in biome_data:
                    weight = biome_data['weight']
                    biome_weights.append(weight)
                else:
                    raise KeyError("'weight' key not found!")
        return biome_weights

    #List of max biome elevations going from lowest to highest elevation. Matches order of bioems in biomes_data file.
    # Used for generating correct color in Tile object.
    # Sets the max height for each biome in passed in list of biomes.
    #gives us a value between 0 and 1
    def _get_max_biome_heights(self, biomes, is_sub: bool):
        biome_weights: list = self._get_biome_weights(is_sub, sub_biomes=biomes)
        weight_sum = sum(biome_weights)

        # Calculate max elevation for each biome in biomes_list, using weight values.
        prev_elevation = 0

        for i in range(len(biomes)):
            max_elevation = (biome_weights[i] / weight_sum) + prev_elevation
            biomes[i].max_elevation = max_elevation
            prev_elevation = max_elevation

    def _extract_biomes(self) -> list[Biome]:
        biomes = []
        for biome_name, biome_data in self.biomes_data.items():
            biome = self._extract_biome(biome_name, biome_data)
            sub_biomes = self._extract_sub_biomes(biome_data)
            biome.sub_biomes = sub_biomes
            biomes.append(biome)
        return biomes

    # TODO: generate new perlin noise. generate max heights, etc using similar methods as before. ignore the fuckin spaghetti code
    def gen_sub_biomes(self):
        for biome in self.biomes:
            self._get_max_biome_heights(biome.sub_biomes, is_sub=True)
            noise = PerlinNoise(ocatves=OCTAVES, seed=randint(1, 10**5))
            temp_array = np.zeros((self.terrain_col_max, self.terrain_row_max))
            for x in range(self.terrain_col_max):
                for y in range(self.terrain_row_max):
                    self.temp_array[x][y] = (noise([x / self.column_max, y / self.row_max]))
                    perlin_value = noise([x / self.terrain_col_max, y / self.terrain_row_max])
                    normalized_value = (perlin_value - -m.sqrt(1/2)) / (perlin_value - m.sqrt(1/2))
                    temp_array[x][y] = normalized_value
            for sub_biome in biome.sub_biomes:
                noise = PerlinNoise(octaves=OCTAVES, seed=randint(1, 10**5))
                norm_value =

    def _gen_biomes(self) -> List[Biome]:
        biomes = self._extract_biomes()
        self._get_max_biome_heights(biomes, is_sub=False)
        return biomes





