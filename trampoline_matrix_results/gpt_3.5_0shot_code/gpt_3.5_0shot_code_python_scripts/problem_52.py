
def find_shortest_path(grid, start, end):
    def is_valid_move(row, col):
        return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 0
    
    def get_diagonal_moves(row, col):
        moves = []
        for i in range(-1, 2, 2):
            for j in range(-1, 2, 2):
                new_row, new_col = row + i, col + j
                if is_valid_move(new_row, new_col):
                    moves.append((new_row, new_col))
        return moves
    
    def get_adjacent_moves(row, col):
        moves = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i != 0 or j != 0:
                    new_row, new_col = row + i, col + j
                    if is_valid_move(new_row, new_col):
                        moves.append((new_row, new_col))
        return moves
    
    def bfs():
        queue = [(start, [start])]
        while queue:
            current, path = queue.pop(0)
            if current == end and len(path) == 9:
                return path
            if len(path) > 9:
                continue
            for move in get_diagonal_moves(*current):
                if move not in path:
                    queue.append((move, path + [move]))
        return None
    
    path = bfs()
    return path

grid = [
    [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
    [0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1],
    [0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0],
    [1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0]
]

start = (8, 1)
end = (1, 11)

path = find_shortest_path(grid, start, end)
print(path)
