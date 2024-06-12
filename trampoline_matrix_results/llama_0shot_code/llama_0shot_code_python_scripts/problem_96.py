
from collections import deque

def is_valid(pos, grid, visited, current):
    x, y = pos
    if x<0 or x>=len(grid) or y<0 or y>=len(grid[0]) or grid[x][y]==1 or visited[x][y] or pos==current:
        return False
    return True

def get_neighbors(pos, grid, visited):
    x, y = pos
    neighbors = [(x-2, y-1), (x-2, y+1), (x-1, y-2), (x-1, y+2), (x+1, y-2), (x+1, y+2), (x+2, y-1), (x+2, y+1)]
    valid_neighbors = []
    for neighbor in neighbors:
        if is_valid(neighbor, grid, visited, pos):
            valid_neighbors.append(neighbor)
    return valid_neighbors

def find_path(grid, start, destination):
    visited = [[False]*len(grid[0]) for _ in range(len(grid))]
    queue = deque([(start, [start])])
    visited[start[0]][start[1]] = True

    while queue:
        pos, path = queue.popleft()
        if pos == destination:
            return path[::-1] # return path from destination to start

        neighbors = get_neighbors(pos, grid, visited)
        for neighbor in neighbors:
            queue.append((neighbor, path + [neighbor]))
            visited[neighbor[0]][neighbor[1]] = True

    return [] # return empty list if no path is found

grid = [[1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0],
        [1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1],
        [1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0],
        [0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1],
        [0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0],
        [0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1]]

start = (3, 10)
destination = (13, 0)

path = find_path(grid, start, destination)
print(path)
