from dataclasses import dataclass, field
import json
from typing import List, Tuple, Union, Optional

@dataclass
class Biome:
    name: str
    color: Tuple[int, int, int]
    weight: Union[int, float]
    is_sub: bool
    sub_biomes: Optional[List['Biome']] = field(default=None)
    max_elevation: float = field(default=None)


class Biomes:
    def __init__(self, min: float, max: float):
        self.min_perlin = min
        self.max_perlin = max
        self.biomes_data: dict = self._biomes_file_load()
        self.biomes = self.gen_biomes()

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
    def _get_biome_weights(self):
        biome_weights = []
        for biome_data in self.biomes_data.values():
            if 'weight' in biome_data:
                weight = biome_data['weight']
                biome_weights.append(weight)
            else:
                raise KeyError("'weight' key not found!")
        return biome_weights

    #List of max biome elevations going from lowest to highest elevation. Matches order of bioems in biomes_data file.
    # Used for generating correct color in Tile object.
    def _get_max_biome_heights(self, biomes):
        biome_weights = self._get_biome_weights()
        weight_sum = sum(biome_weights)

        # Calculate max elevation for each biome in biomes_list, using weight values.
        prev_elevation = 0

        for i in range(len(biomes)):
            max_elevation = (biome_weights[i] / weight_sum) + prev_elevation
            biomes[i].max_elevation = max_elevation
            prev_elevation = max_elevation

    def _extract_biomes(self):
        biomes = []
        for biome_name, biome_data in self.biomes_data.items():
            biome = self._extract_biome(biome_name, biome_data)
            sub_biomes = self._extract_sub_biomes(biome_data)
            biome.sub_biomes = sub_biomes
            biomes.append(biome)
        return biomes

    def gen_biomes(self) -> List[Biome]:
        biomes = self._extract_biomes()
        self._get_max_biome_heights(biomes)
        return biomes






