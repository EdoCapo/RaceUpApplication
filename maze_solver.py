from collections import deque
import time
import tkinter as tk
from tkinter import simpledialog

# Define movements for convenience (UP, DOWN, LEFT, RIGHT)
MOVEMENTS = {
    'UP': (-1, 0),
    'DOWN': (1, 0),
    'LEFT': (0, -1),
    'RIGHT': (0, 1)
}


# Function to check if a position is within bounds and not a wall
def is_valid_move(maze, visited, x, y):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != '#' and not visited[x][y]


# Breadth-First Search (BFS) algorithm to find the shortest path
def bfs(maze, start, end):
    queue = deque([(start, [])])  # Queue stores tuples (position, path to reach that position)
    visited = [[False] * len(maze[0]) for _ in range(len(maze))]
    visited[start[0]][start[1]] = True

    while queue:
        (x, y), path = queue.popleft()

        # Check if we reached the end
        if (x, y) == end:
            return path

        # Explore all possible moves
        for move, (dx, dy) in MOVEMENTS.items():
            nx, ny = x + dx, y + dy
            if is_valid_move(maze, visited, nx, ny):
                visited[nx][ny] = True
                queue.append(((nx, ny), path + [move]))

    return None  # No path found


# Function to solve the maze
def solve_maze(maze, animate=False):
    start = None
    end = None

    # Find the positions of 'S' (start) and 'E' (end)
    for i, row in enumerate(maze):
        for j, char in enumerate(row):
            if char == 'S':
                start = (i, j)
            elif char == 'E':
                end = (i, j)

    if not start or not end:
        raise ValueError("Maze must contain one start 'S' and one exit 'E'.")

    # Run BFS to find the solution
    path = bfs(maze, start, end)

    if path:
        print("Path to exit:", path)
        if animate:
            animate_solution(maze, start, path)
    else:
        print("No solution exists.")


# Function to animate the solution step-by-step
def animate_solution(maze, start, path):
    current_position = start
    maze_copy = [list(row) for row in maze]

    print("Animating solution:")
    for move in path:
        time.sleep(0.5)  # Delay to slow down the animation
        maze_copy[current_position[0]][current_position[1]] = 'S'

        # Print the maze at each step
        for row in maze_copy:
            print("".join(row))
        print()

        # Move to the next position
        dx, dy = MOVEMENTS[move]
        current_position = (current_position[0] + dx, current_position[1] + dy)


# Function to prompt for animation
def ask_for_animation():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Ask the user if they want to see the animation
    user_input = simpledialog.askstring("Maze Animation",
                                        "Do you want to see the step-by-step animation for maze 1, 2, or 3? Type the number (or 'no' to skip):")

    return user_input


def load_and_solve_mazes(file_list):
    for maze_file in file_list:
        print(f"\n--- Solving maze from {maze_file} ---")

        # Load the maze from the current text file
        with open(maze_file, "r") as f:
            maze = [line.strip() for line in f.readlines()]

        # Print the maze
        print("Maze layout:")
        for row in maze:
            print(row)

        # Solve the maze
        solve_maze(maze)


if __name__ == "__main__":
    # List of maze files
    maze_files = ["./mazes/maze1.txt", "./mazes/maze2.txt", "./mazes/maze3.txt"]

    # Ask the user if they want to see an animation
    user_choice = ask_for_animation()

    # Solve each maze, optionally animating one maze based on user input
    if user_choice in ['1', '2', '3']:
        maze_index = int(user_choice) - 1
        print(f"\n--- Solving maze {user_choice} with animation ---")
        with open(maze_files[maze_index], "r") as f:
            maze = [line.strip() for line in f.readlines()]

        print("Maze layout:")
        for row in maze:
            print(row)

        # Solve the selected maze with animation
        solve_maze(maze, animate=True)
    else:
        # Solve all mazes without animation
        load_and_solve_mazes(maze_files)
