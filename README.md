# Generative art engine 🦥
Create generative art using python and Pillow library.

## Installation 🛠️
You need to install [Pillow](https://pypi.org/project/Pillow/) and [configparser](https://pypi.org/project/configparser/).
```shell
pip install Pillow configparser
```

## Usage ▶
### Configuration ⚙
To get a custom generation, please change values in the [config file](config.ini) respecting the format already existing.  

|          Option          	| Description                                                                                                     	|
|:------------------------:	|-(----------------------------------------------------------------------------------------------------------------	|
| `edition_size`           	| Number of images to be generated.                                                                               	|
| `output_path`            	| Name of the output directory.                                                                                   	|
| `size`                   	| Image size in pixels.                                                                                           	|
| `layers_path`            	| Name of the folder containing layers.                                                                           	|
| `layers`                 	| Names of layers, separated by a semicolon.                                                                      	|
| `layer_weights`          	| Layer weights, separated by a semicolon. A value below zero means that the layer will be present on all images. 	|
| `multiple_layers_chance` 	| Chances of getting an extra layer. Cumulative.                                                                  	|

Create your different layers as folders in the 'layers' directory, and add all the layer assets in these directories. You can name the assets anything as long as it has a rarity weight attached in the file name like so: example `element#70.png`.

### Generation 🖼
```shell
python3 main.py [...options]
```

Options :
* --rarity (coming soon)
* --dna (coming soon)
* --preview (coming soon)

## Roadmap 🗺
- [x] Random image generation
- [x] Add weights to layers
- [x] Add weights to elements
- [x] GIF preview
- [x] Add a config file
- [ ] Write image metadata
