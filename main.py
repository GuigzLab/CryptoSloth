from PIL import Image
import random
import os
from datetime import datetime


def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def generate_random_hex():
    random_number = random.randint(0, 16777215)
    hex_number = str(hex(random_number))
    hex_number = '#' + hex_number[2:]
    print('A  Random Hex Color Code is :', hex_number)
    return hex_number


if __name__ == '__main__':

    elements = []
    directory = "assets"
    for root, subdirectories, files in os.walk(directory):
        for subdirectory in subdirectories:
            print(os.path.join(root, subdirectory))
        for file in files:
            elements.append(os.path.join(root, file))

    elements = [x for x in elements if "sloth" not in x]
    img = Image.open('assets/sloth.png', 'r').convert("RGBA")

    dirname = os.path.join("sloths", datetime.now().strftime("%m-%d-%Y %H-%M-%S"))
    os.makedirs(dirname, exist_ok=True)
    for n, e in enumerate(elements):
        random_rgb = tuple([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])
        print(random_rgb)

        background = Image.new('RGB', (500, 500), color=random_rgb)
        background.paste(img, (0, 0), img)
        element = Image.open(e, 'r').convert("RGBA")
        background.paste(element, (0, 0), element)

        background.save(os.path.join(dirname, f"{n}.png"))
