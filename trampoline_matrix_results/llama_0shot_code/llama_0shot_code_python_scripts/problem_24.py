
from collections import deque

def bfs(graph, start, end, max_diagonal):
    queue = deque([(start, 0, 0, [start])])
    visited = set([start])
    while queue:
        node, diagonal, steps, path = queue.popleft()
        if node == end:
            return path
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, diagonal + (abs(neighbor[0] - node[0]) + abs(neighbor[1] - node[1])) % 2, steps + 1, path + [neighbor]))
                if steps == max_diagonal * 2:
                    break
    return None

def main():
    grid = [
        [1, 1, 1, 1, 0, 1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 0, 0, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 1, 0, 0, 1, 1, 1, 0, 0]
    ]

    graph = {}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                graph[(i, j)] = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                if i > 0 and j > 0:
                    graph[(i, j)].append((i-1, j-1))
                if i > 0 and j < len(grid[i]) - 1:
                    graph[(i, j)].append((i-1, j+1))
                if i < len(grid) - 1 and j > 0:
                    graph[(i, j)].append((i+1, j-1))
                if i < len(grid) - 1 and j < len(grid[i]) - 1:
                    graph[(i, j)].append((i+1, j+1))

    start = (9, 9)
    end = (4, 1)
    path = bfs(graph, start, end, 3)
    print(path)

if __name__ == "__main__":
    main()
