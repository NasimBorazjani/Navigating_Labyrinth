
import heapq

def shortest_path(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    def get_neighbors(r, c):
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] != 'x':
                yield nr, nc

    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    queue = [(0, start, [])]
    visited = set()

    while queue:
        cost, node, path = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            path = path + [node]
            if node == end:
                return path
            for neighbor in get_neighbors(*node):
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + matrix[neighbor[0]][neighbor[1]], neighbor, path))

    return None

def main():
    matrix = [
        [15, 1, 'x', 3, 'x', 9, 15, 8, 17, 'x', 'x', 6, 'x', 12, 3],
        ['x', 'x', 'x', 14, 'x', 7, 18, 6, 14, 2, 19, 15, 'x', 'x', 'x'],
        [4, 3, 'x', 10, 8, 4, 16, 13, 6, 'x', 18, 10, 14, 'x', 'x'],
        ['x', 'x', 'x', 10, 'x', 14, 10, 7, 'x', 'x', 'x', 4, 2, 19, 3],
        [5, 'x', 10, 'x', 18, 12, 20, 15, 'x', 'x', 11, 11, 1, 10, 19],
        [8, 'x', 13, 'x', 'x', 'x', 16, 7, 'x', 'x', 2, 18, 11, 'x'],
        [12, 'x', 15, 'x', 6, 'x', 'x', 'x', 18, 3, 14, 3, 6],
        ['x', 6, 13, 19, 19, 'x', 7, 12, 18, 5, 'x', 1, 4, 18, 11],
        [5, 'x', 18, 12, 4, 3, 7, 'x', 16, 1, 'x', 16, 2, 'x'],
        ['x', 'x', 'x', 'x', 18, 'x', 14, 15, 1, 'x', 'x', 'x', 'x', 9, 'x'],
        ['x', 13, 'x', 7, 7, 'x', 16, 10, 'x', 'x', 'x', 'x', 8, 'x'],
        ['x', 'x', 19, 18, 8, 18, 'x', 'x', 12, 'x', 13, 'x', 17, 12, 7],
        ['x', 'x', 'x', 'x', 7, 7, 13, 17, 'x', 'x', 'x', 'x', 'x', 9, 5],
        [9, 'x', 9, 'x', 8, 'x', 'x', 17, 4, 12, 12, 12],
        [8, 1, 11, 'x', 'x', 'x', 'x', 15, 'x', 'x', 2, 16, 'x', 15]
    ]

    start, end = (7, 14), (2, 4)
    path = shortest_path(matrix, start, end)
    print(path)

if __name__ == "__main__":
    main()
