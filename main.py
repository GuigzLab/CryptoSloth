from PIL import Image
import random
import os
from datetime import datetime

from src.NFTGenerator import NFTGenerator

if __name__ == '__main__':

    gen = NFTGenerator(10)
    gen.generate()
