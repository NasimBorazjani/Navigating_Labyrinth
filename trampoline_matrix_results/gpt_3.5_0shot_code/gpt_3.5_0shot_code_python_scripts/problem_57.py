
from queue import Queue

# Define the grid of trampolines
grid = [
    [1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0]
]

# Define the starting and ending positions
start = (11, 2)
end = (3, 10)

# Define the possible moves
moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

# Perform BFS to find the shortest path
def bfs(grid, start, end):
    q = Queue()
    q.put([start])
    
    while not q.empty():
        path = q.get()
        current = path[-1]
        
        if current == end:
            return path
        
        for move in moves:
            new_pos = (current[0] + move[0], current[1] + move[1])
            if 0 <= new_pos[0] < len(grid) and 0 <= new_pos[1] < len(grid[0]) and grid[new_pos[0]][new_pos[1]] == 0:
                new_path = list(path)
                new_path.append(new_pos)
                q.put(new_path)

# Find the shortest path
shortest_path = bfs(grid, start, end)

# Print the shortest path
print(shortest_path)
