import tkinter as tk
import random

def find_shortest_path(grid):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1)] # 8 directions of movement
    start = (0, 0) # top left corner starting point
    end = (len(grid) -1, len(grid[0]) - 1) # ending point, bottom right
    visited = set() # set keeps track of visited cells
    queue =[(start, 1)] # starting call and its distance

    if grid[0][0] == 1 or grid[-1][-1] == 1: # If start or finished are blocked, return -1
        return -1, []

    while queue:
        current, distance = queue.pop(0) # Dequeue a cell and its distance
        if current == end: # return the distance if it reaches the end point
            return distance, reconstruct_path(visited, start, end, grid)
        visited.add(current)

        for dx, dy in directions: # exploring neighbor cells
            x, y = current[0] + dx, current[1] + dy
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and (x, y) not in visited and grid[x][y] == 0:
                queue.append(((x, y), distance + 1)) # add neighbor to queue and update distance

    return -1, [] # if unreachable

def reconstruct_path(visited, start, end, grid):
    path = [end]
    current = end
    while current != start:
        for neighbor in get_neighbors(current, grid):
            if neighbor in visited and abs(neighbor[0] - current[0]) <= 1 and abs(neighbor[1] - current[1]) <= 1:
                path.append(neighbor)
                current = neighbor
                break
    path.reverse()
    return path

def get_neighbors(cell, grid):
    x, y = cell
    neighbors = [(x + dx, y + dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if (dx != 0 or dy != 0)]
    valid_neighbors = [(nx, ny) for nx, ny in neighbors if 0 <= nx < len(grid) and 0 <= ny < len(grid[0])]
    return valid_neighbors

def generate_random_grid(rows, cols, obstacle_density):
    grid = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if random.random() < obstacle_density:
                grid[i][j] = 1
    return grid

def visualize_path():
    rows = 10
    cols = 10
    obstacle_density = 0.3

    grid = generate_random_grid(rows, cols, obstacle_density)
    shortest_path_length, shortest_path = find_shortest_path(grid)

    root = tk.Tk()
    root.title("Shortest Path Visualization")

    canvas = tk.Canvas(root, width=cols * 40, height=rows * 40)
    canvas.pack()

    for i in range(rows):
        for j in range(cols):
            x0 = j * 40
            y0 = i * 40
            x1 = x0 + 40
            y1 = y0 + 40

            color = "black" if grid[i][j] == 1 else "white"
            canvas.create_rectangle(x0, y0, x1, y1, fill=color)

            if (i, j) in shortest_path:
                canvas.create_rectangle(x0, y0, x1, y1, fill="green")

    shortest_path_label = tk.Label(root, text=f"Shortest Path Length: {shortest_path_length}")
    shortest_path_label.pack()

    root.mainloop()

visualize_path()
