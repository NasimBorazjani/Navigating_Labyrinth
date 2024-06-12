
from collections import deque

# Map data
data = """1 1 0 0 0 1 0 1 1 0 1 0 0
0 0 0 0 0 1 1 1 1 1 0 1 1
1 0 1 0 1 1 1 0 0 0 0 0 0
0 0 0 0 1 1 1 1 1 0 0 0 1
1 0 0 1 0 0 1 1 1 1 1 0 1
1 0 0 0 0 1 1 0 0 0 1 1 1
1 1 1 0 0 1 1 0 1 1 0 0 0
1 0 1 1 1 0 0 1 0 1 1 1 1
0 1 1 1 0 1 1 1 0 1 0 1 1
0 0 1 0 0 0 0 0 1 1 0 1 0
1 0 1 0 1 1 0 1 0 1 0 1 0
1 1 1 0 0 1 1 0 0 1 1 0 1
0 1 1 0 0 0 1 0 1 0 0 0 0"""

# Convert the data into a 2D list
map_data = [list(map(int, line.split())) for line in data.split('\n') if line]

# Check if a move is valid
def is_valid(x, y, visited, map_data):
    return (0 <= x < len(map_data) and 0 <= y < len(map_data[0]) and 
            map_data[x][y] == 0 and not visited[x][y])

# BFS function
def bfs(start, end, map_data):
    # Define the 8 possible moves
    moves = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)]
    # Initialize the visited matrix and the queue
    visited = [[False]*len(map_data[0]) for _ in range(len(map_data))]
    queue = deque([(start, [start])])
    # Start the BFS
    while queue:
        x, y, path = queue.popleft()
        if (x, y) == end:
            return path
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, visited, map_data):
                visited[nx][ny] = True
                queue.append(((nx, ny), path + [(nx, ny)]))
    return None

# Test the BFS function
start, end = (11, 8), (1, 0)
path = bfs(start, end, map_data)
print(path)
