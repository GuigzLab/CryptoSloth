import copy

from PIL import Image
import random
import os
from datetime import datetime

from src.NFT import NFT


class NFTGenerator:
    def __init__(self, n=10):
        self.edition_size = n
        self.layers_directory = "layers"
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
        self.nft_list = [()]

    def generate(self):
        # elements = []
        # for root, subdirectories, files in os.walk(self.assets_directory):
        #     for subdirectory in subdirectories:
        #         print(os.path.join(root, subdirectory))
        #     for file in files:
        #         elements.append(os.path.join(root, file))
        #
        # # elements = [x for x in elements if "sloth" not in x]
        # img = Image.open('layers/head/basic#1.png', 'r').convert("RGBA")
        #
        # dirname = os.path.join("sloths", datetime.now().strftime("%m-%d-%Y %H-%M-%S"))
        # os.makedirs(dirname, exist_ok=True)
        # for n, e in enumerate(elements):
        #     random_rgb = tuple([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])
        #     print(random_rgb)
        #
        #     background = Image.new('RGB', (500, 500), color=random_rgb)
        #     background.paste(img, (0, 0), img)
        #     element = Image.open(e, 'r').convert("RGBA")
        #     background.paste(element, (0, 0), element)
        #
        #     background.save(os.path.join(dirname, f"{n}.png"))
        # TODO - Generate a list of NFTs, then save them to a directory

        nft_list = []

        weight_list = []
        for key, value in self.weighted_layers.items():
            weight_list += [key] * value

        # Generate src for each art
        for i in range(self.edition_size):
            temp_weight_list = copy.deepcopy(weight_list)
            layers = [random.choice(temp_weight_list)]
            temp_weight_list = [x for x in temp_weight_list if x != layers[-1]]
            while random.randrange(100) < self.multiple_layers_chance and len(temp_weight_list) > 0:
                layers.append(random.choice(temp_weight_list))
                temp_weight_list = [x for x in temp_weight_list if x != layers[-1]]
            # Images always have heads
            layers.append("head")
            # Sort list using layer order
            layers.sort(key=lambda val: self.sort_order[val])

            edition = NFT(layers)
            nft_list.append(edition.create_image())

        dirname = os.path.join("sloths", datetime.now().strftime("%m-%d-%Y %H-%M-%S"))
        os.makedirs(dirname, exist_ok=True)
        for n, nft in enumerate(nft_list):
            nft.save(os.path.join(dirname, f"{n}.png"))
        # Generate animated GIF
        self.generate_prewiew_gif(nft_list, dirname)

    @staticmethod
    def generate_prewiew_gif(images, dirname):
        if images:
            images = [image.quantize(method=Image.MEDIANCUT) for image in images]
            images[0].save(os.path.join(dirname, "preview.gif"), format='GIF', save_all=True, append_images=images[1:],
                           optimize=False, duration=500, loop=0)
