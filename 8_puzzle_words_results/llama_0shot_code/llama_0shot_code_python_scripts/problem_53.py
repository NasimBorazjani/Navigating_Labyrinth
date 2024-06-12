
from collections import deque

def bfs(board):
    target_words = ["limen", "somers", "spooky", "dogtie"]
    queue = deque([(board, [])])
    visited = set()

    while queue:
        current_board, path = queue.popleft()
        current_str = "".join(["".join(row) for row in current_board])
        if current_str == "".join(target_words):
            return path
        if current_str not in visited:
            visited.add(current_str)
            for i in range(len(current_board)):
                for j in range(len(current_board[0])):
                    if current_board[i][j] == '_':
                        for dx, dy in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:
                            new_x, new_y = i + dx, j + dy
                            if 0 <= new_x < len(current_board) and 0 <= new_y < len(current_board[0]):
                                new_board = [list(row) for row in current_board]
                                new_board[i][j], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[i][j]
                                queue.append((new_board, path + [dx, dy]))

    return None

initial_board = [['o', 'l', 's', 'm', '_', 'n'], ['s', 'o', 'm', 'e', 'r', 'k'], ['s', 'p', 'i', 'o', 'e', 'y'], ['d', 'o', 'g', 't', 'i', 'e']]

print(bfs(initial_board))
