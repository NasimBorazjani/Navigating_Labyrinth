
from collections import deque

def bfs(graph, start, end):
    queue = deque([(start, 0, [start])])
    visited = set()
    while queue:
        (node, diagonals, path) = queue.popleft()
        if node not in visited:
            visited.add(node)
            for next_node, jump_type in graph[node]:
                new_path = path + [next_node]
                if next_node == end:
                    return new_path
                else:
                    queue.append((next_node, diagonals + jump_type, new_path))
    return None

def main():
    grid = [
        [1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1],
        [1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1],
        [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1],
        [0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0],
        [1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0],
        [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1]
    ]

    graph = {}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                node = (i, j)
                graph[node] = []
                for x, y in [(-1, -1), (-1, 1), (1, -1), (1, 1), (-2, 0), (0, -2), (0, 2), (2, 0)]:
                    ni, nj = i + x, j + y
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[i]) and grid[ni][nj] == 0:
                        graph[node].append(((ni, nj), 2 if x * y == -1 else 1))

    start, end = (0, 11), (12, 2)
    path = bfs(graph, start, end)
    print(path)

if __name__ == "__main__":
    main()
