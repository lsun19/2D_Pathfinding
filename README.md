# Navmesh Pathfinding

## Introduction

This program involves implementing a bidirectional A* search algorithm to find paths in navmeshes created from user-provided images. The program builds navmeshes from images and uses a given Python template for the pathfinding function. The input is a navmesh, and the output is an image showing the path from a source to a destination. Source and destination points are defined interactively through a provided Python program.

## Getting Started

### Prerequisites

- Python 3.x
- SciPy library installed

### Running the Program

1. To test the pathfinder, navigate to the `/src` folder and execute the following command:

```bash
python nm_interactive.py ../input/homer.png ../input/homer.png.mesh.pickle 2

```

2. The parameters represent the image file to display (must be a PNG), a binary file containing the navmesh representation of the given image (.mesh.pickle), and a subsampling factor for scaling down large images.

3. Upon running this code, a new window will display the image parameter. Use your cursor to click on the image to define the source (first click) and destination (second click) points. After the second click, the find_path function within nm_pathfinder.py is called to compute the path.

### Base Code Overview

- /input and three Python files (/src) comprise the provided base code:
   - src/nm_interactive.py: Main interactive program
   - src/nm_meshbuilder.py: Builds navmeshes from images, producing .mesh.pickle files.
   - src/nm_pathfinder.py: Contains the find_path function for implementing the bidirectional A* algorithm.
- input/homer.png.mesh.pickle: Binary data file created by nm_meshbuilder.py, representing the navmesh.

### Creating a Custom Map
1. Find and save an image suitable for conversion to a black-and-white occupancy map.
2. Create a black-and-white version of the image using a photo editor and save it as a PNG.
3. Run the navmesh builder program to produce .mesh.pickle and a visualization of the navmesh.
4. Run your pathfinding program with the original PNG file, the pickled mesh data, and a suitable subsampling factor.

#### Example command:

```bash
python nm_meshbuilder.py your_image.png
python nm_interactive.py your_image-orig.png your_image.png.mesh.pickle 1
```
