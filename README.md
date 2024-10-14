# Maze Solver Application

## Description
This Python program solves mazes represented as grids of characters. It finds a path from the starting point 'S' to the exit 'E', avoiding walls ('#') and navigating through open spaces ('.'). The solution is determined using the Breadth-First Search (BFS) algorithm, which guarantees the shortest path from the start to the exit, if one exists.

The program can display the maze and provide an optional step-by-step animation of the solution for a selected maze. The animation showcases how the algorithm moves through the maze until it finds the exit.

## Input
The mazes are provided as text files (`maze1.txt`, `maze2.txt`, `maze3.txt`) with the following symbols:
- `'S'`: Starting point.
- `'E'`: Exit point.
- `'#'`: Walls that cannot be crossed.
- `'.'`: Open passages where movement is allowed.

Each maze is guaranteed to have exactly one start ('S') and one exit ('E').

## Algorithm Explanation
The algorithm used is **Breadth-First Search (BFS)**, which is ideal for finding the shortest path in an unweighted grid-like structure. The BFS explores all possible movements level by level from the starting point, ensuring that the first time it reaches the exit, it does so via the shortest path.

### BFS Steps:
1. **Initialization**: A queue is initialized with the starting point ('S'), along with an empty path.
2. **Exploration**: At each step, the algorithm checks the four possible moves (UP, DOWN, LEFT, RIGHT). If the move leads to an open space ('.') and hasn't been visited yet, it adds that position to the queue and continues.
3. **Termination**: When the algorithm reaches the exit ('E'), it returns the path taken to get there.
4. **Backtracking**: If no more moves are possible and the exit hasn't been reached, the algorithm declares that no solution exists.

### Animation (Optional)
The program includes an animation option that visualizes the pathfinding process step by step. The user is prompted via a dialog to select one of the mazes to animate. If chosen, the program pauses at each move and updates the maze display to show the algorithm's current position.

## Execution Guide

### Prerequisites
- Ensure Python 3.x is installed on your system.
- Install the `tkinter` library (usually included by default with Python).

### Steps to Execute the Program
1. Ensure that you have the maze text files (`maze1.txt`, `maze2.txt`, `maze3.txt`) saved in the `../mazes/` directory relative to the Python script.
2. Open a terminal and navigate to the directory containing `maze_solver.py`.
3. Run the Python script:

   ```bash
   python maze_solver.py

Developed by Edoardo Caporin.