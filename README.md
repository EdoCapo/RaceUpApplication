# RaceUpApplication - Maze Solver

## Description
This Python program solves a maze that is represented as a grid of characters. The goal is to find a path from the starting point 'S' to the exit 'E', avoiding walls ('#') and walking through open spaces ('.').

The program uses the Breadth-First Search (BFS) algorithm to find the shortest path from the start to the exit. If a path exists, it prints the sequence of moves ('UP', 'DOWN', 'LEFT', 'RIGHT') that lead to the exit. If no path exists, it prints a message indicating that the solution is not possible.

## Input
The maze is provided as a text file where:
- 'S' is the starting point.
- 'E' is the exit.
- '#' represents walls.
- '.' represents open spaces.

## Execution Guide
1. Ensure you have Python installed on your system.
2. Save the maze in a file named `maze.txt` in the same directory as the Python script. You can use the provided example mazes.
3. Run the Python script `maze_solver.py` from the command line:

   ```bash
   python maze_solver.py
