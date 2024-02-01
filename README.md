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
