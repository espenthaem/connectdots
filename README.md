# Connectdots
A simple Python module, to detect and connect the green, blue and red dot on a given image. 
The implementation assumes that the input images have a black background, and contain no more than 3 dots, 
1 of each aforementioned color. 

## Installation
From the root directory, simply run ```pip install .```

## Usage
```
from connectdots import connect_dots


connect_dots("mpsi_task.png")
```
