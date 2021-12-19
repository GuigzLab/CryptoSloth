import copy
import random
import os
from datetime import datetime
from PIL import Image
import configparser

from src.helpers import DotDict
from src.NFT import NFT


class NFTGenerator:
    def __init__(self):
        self.weighted_layers = {
            "accessories": 5,
            "eyewear": 50,
            "headwear": 50,
            "body": 10,
        }
        self.multiple_layers_chance = 10
        self.sort_order = {
            "head": 0,
            "body": 1,
            "eyewear": 2,
            "headwear": 3,
            "accessories": 4,
        }
        self.config = DotDict(self.get_config())
        print(self.config)

    @staticmethod
    def get_config():
        config = configparser.ConfigParser()
        config.read("config.ini")
        conf = {}
        for v in config["GENERAL"].items():
            conf[v[0]] = v[1]

        conf['edition_size'] = int(conf['edition_size'])

        for v in config["IMAGE"].items():
            conf[v[0]] = v[1]

        conf['size'] = [int(x.strip()) for x in conf['size'].split('x')]

        layers = [x.strip() for x in conf['layers'].split(';')]
        weights = [int(x) for x in conf['layer_weights'].split(';')]
        conf['layers'] = {}
        conf['layer_weights'] = {}
        for i, l in enumerate(layers):
            conf['layers'][l] = i
            conf['layer_weights'][l] = weights[i]

        conf['multiple_layers_chance'] = int(conf['multiple_layers_chance'])

        print(weights)

        return conf

    def generate(self):
        nft_list = []

        weight_list = []
        permanent_layers = []
        for key, value in self.config.layer_weights.items():
            if value <= 0:
                permanent_layers.append(key)
            else:
                weight_list += [key] * value

        # Generate src for each art
        for i in range(self.config.edition_size):
            temp_weight_list = copy.deepcopy(weight_list)
            layers = [random.choice(temp_weight_list)]
            temp_weight_list = [x for x in temp_weight_list if x != layers[-1]]
            while random.randrange(100) < self.config.multiple_layers_chance and len(temp_weight_list) > 0:
                layers.append(random.choice(temp_weight_list))
                temp_weight_list = [x for x in temp_weight_list if x != layers[-1]]
            # Images always have heads
            layers += permanent_layers
            # Sort list using layer order
            layers.sort(key=lambda val: self.config.layers[val])

            edition = NFT(layers=layers, size=self.config.size, layers_path=self.config.layers_path)
            nft_list.append(edition.create_image())

        dirname = os.path.join(self.config.output_path, datetime.now().strftime("%m-%d-%Y %H-%M-%S"))
        os.makedirs(dirname, exist_ok=True)
        for n, nft in enumerate(nft_list):
            nft.save(os.path.join(dirname, f"{n}.png"))
        # Generate animated GIF
        self.generate_prewiew_gif(nft_list, dirname)

    @staticmethod
    def generate_prewiew_gif(images, dirname):
        if images and len(images) > 1:
            # images = [image.quantize(method=Image.MEDIANCUT) for image in images]
            images[0].save(os.path.join(dirname, "preview.gif"), format='GIF', save_all=True, append_images=images[1:],
                           optimize=False, duration=500, loop=0)
