import os
import random

from PIL import Image


class NFT:
    WEIGHTS = {}

    def __init__(self, layers, size, layers_path):
        self.layers = layers
        self.size = tuple(size)
        self.layers_path = layers_path
        self.add_weights()

    def add_weights(self):
        for layer in self.layers:
            if layer not in NFT.WEIGHTS:
                path = os.path.join(self.layers_path, layer)
                NFT.WEIGHTS[layer] = {}
                element_list = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
                element_list = [x.split('.')[0] for x in element_list]
                for e in element_list:
                    el, weight = e.split('#')
                    NFT.WEIGHTS[layer][el] = int(weight)

    def create_image(self):
        random_rgb = tuple([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])
        image = Image.new('RGB', self.size, color=random_rgb)

        for layer in self.layers:
            # Create weighted list
            layer_weight_list = []
            for key, value in NFT.WEIGHTS[layer].items():
                layer_weight_list += [key] * value
            # Pick one element from the list
            layer_element = random.choice(layer_weight_list)
            # Get the path of the selected element then paste it (already layer-ordered)
            path = os.path.join(self.layers_path, layer)
            layer_path = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and layer_element in f][0]
            layer_img = Image.open(os.path.join(path, layer_path), 'r').convert("RGBA")
            image.paste(layer_img, (0, 0), layer_img)

        return image

    def create_metadata(self):
        pass
