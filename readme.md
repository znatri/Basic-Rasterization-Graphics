# Basic Rasterization Graphics Project

This project is a simple implementation of rasterization in computer graphics, which involves converting geometric primitives such as points, lines, and polygons into a raster format suitable for rendering on a display. The project is designed for educational purposes, helping students understand the fundamentals of rasterization and its role in computer graphics.

## Project Overview

The main goal of this project is to practice the basic principles of rasterization, including:

- Drawing points and lines using Bresenham's line algorithm
- Filling polygons using scanline algorithm
- Implementing transformations, such as translation, scaling, and rotation
- Clipping lines and polygons using Cohen-Sutherland and Sutherland-Hodgman algorithms

The project is developed using C++ and OpenGL, and it provides a simple user interface to interact with the implemented features.

## Getting Started

### Prerequisites

- C++ compiler with C++11 support
- OpenGL and GLUT libraries

### Compiling and Running the Project

1. Clone the repository:
```bat
git clone https://github.com/znatri/cs3451_p1_rasterization.git
```
2. Navigate to the project directory:
```bat
cd cs3451_p1_rasterization
```
3. Compile the project:
```bat
make
```
4. Run the compiled executable:
```bat
./rasterization
```


## Usage

The user interface allows you to interact with the implemented features through keyboard shortcuts:

- `P`: Draw points
- `L`: Draw lines
- `F`: Fill polygons
- `T`: Apply translation
- `S`: Apply scaling
- `R`: Apply rotation
- `C`: Clip lines and polygons

## Contributing

This project is for educational purposes and is not actively maintained. However, if you have any suggestions, issues, or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Acknowledgments

The project was developed as part of the CS3451 - Computer Graphics course at Georgia Institute of Technology.
