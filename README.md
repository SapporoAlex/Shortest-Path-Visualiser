# Shortest Path Visualization
This project provides a Tkinter GUI application that visualizes a randomly generated grid with the shortest path highlighted in green, using a breadth-first search algorithm.

<img src="https://github.com/SapporoAlex/Shortest-Path-Visualiser/blob/main/1.jpg" width="500" height="500">

## Dependencies
Tkinter (Standard library)
Random (Standard library)

## Installation
Clone the repository to your local machine:

```bash
git clone https://github.com/SapporoAlex/Shortest-Path-Visualiser.git
```

Navigate to the project directory:

```bash
cd shortest-path-visualiser
```

Usage
Run the `BFS SPA.py` script to launch the application:

`BFS SPA.py`
A Tkinter window will open displaying a randomly generated grid. The shortest path, if available, will be highlighted in green, and the length of the shortest path will be displayed beneath the grid.

Click the "Reset" button to regenerate the grid and visualize a new shortest path.

## Algorithm
The visualization utilizes a breadth-first search (BFS) algorithm to find the shortest path from the top-left corner to the bottom-right corner of the grid. The BFS algorithm explores all possible paths in the grid, guaranteeing the shortest path is found.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
