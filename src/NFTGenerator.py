import copy

from PIL import Image
import random
import os
from datetime import datetime


class NFTGenerator:
    def __init__(self, n=10):
        self.edition_size = n
        self.assets_directory = "assets"
        self.weighted_layers = {
            "accessories": 5,
            "eyewear": 50,
            "headwear": 50,
            "body": 1,
        }
        self.multiple_layers_chance = 10
        self.sort_order = {
            "head": 0,
            "body": 1,
            "eyewear": 2,
            "headwear": 3,
            "accessories": 4,
        }

    def generate(self):
        # elements = []
        # for root, subdirectories, files in os.walk(self.assets_directory):
        #     for subdirectory in subdirectories:
        #         print(os.path.join(root, subdirectory))
        #     for file in files:
        #         elements.append(os.path.join(root, file))
        #
        # # elements = [x for x in elements if "sloth" not in x]
        # img = Image.open('assets/head/basic.png', 'r').convert("RGBA")
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

        weight_list = []
        for key, value in self.weighted_layers.items():
            weight_list += [key] * value

        print(weight_list)

        # Generate layers for each art
        for i in range(self.edition_size):
            temp_weight_list = copy.deepcopy(weight_list)
            layers = [random.choice(temp_weight_list)]
            temp_weight_list = [x for x in temp_weight_list if x != layers[-1]]
            while random.randrange(100) < self.multiple_layers_chance and len(temp_weight_list) > 0:
                layers.append(random.choice(temp_weight_list))
                temp_weight_list = [x for x in temp_weight_list if x != layers[-1]]
            # Sort list using layer order
            layers.sort(key=lambda val: self.sort_order[val])
            print(layers)

    def prewiew_gif(self):
        pass
