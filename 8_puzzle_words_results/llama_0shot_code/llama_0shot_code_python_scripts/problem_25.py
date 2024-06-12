
from collections import deque

def bfs(board, words):
    queue = deque([(board, words, [])])
    visited = set()
    while queue:
        current_board, current_words, swaps = queue.popleft()
        current_state = "".join(["".join(row) for row in current_board])
        if current_state in visited:
            continue
        visited.add(current_state)
        if current_words == []:
            return swaps
        for i in range(len(current_board)):
            for j in range(len(current_board[0])):
                if current_board[i][j] == '_':
                    for di, dj in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:
                        new_i, new_j = i + di, j + dj
                        if 0 <= new_i < len(current_board) and 0 <= new_j < len(current_board[0]):
                            new_board = [row.copy() for row in current_board]
                            new_board[i][j], new_board[new_i][new_j] = new_board[new_i][new_j], new_board[i][j]
                            queue.append((new_board, current_words[1:], swaps + [f"({i},{j})({new_i},{new_j})"]))
        return None

initial_board = [['i', 'g', 'u', 'h', 'a'], ['n', 'o', 's', 'u', 's'], ['c', 'n', 'g', 'a', '_'], ['j', 'u', 'u', 'p', 'h']]
target_words = ["guha", "nisus", "uncap", "jough"]

swaps = bfs(initial_board, target_words)
print(swaps)
