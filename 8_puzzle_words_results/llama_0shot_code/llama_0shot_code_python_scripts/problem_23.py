
from collections import deque

def bfs(board, words):
    initial_board = "".join(["".join(row) for row in board])
    queue = deque([(initial_board, "")])
    visited = set([initial_board])

    while queue:
        current_board, actions = queue.popleft()
        if current_board == "".join(words):
            return actions

        for i in range(len(current_board)):
            if current_board[i] == '_':
                for j in [-1 + len(current_board), 1 + len(current_board), -len(board), len(board)]:
                    new_board = current_board[:i] + current_board[i+1:i+j] + '_' + current_board[i+j]
                    new_board = new_board[:i+j] + current_board[i] + new_board[i+j+1:]
                    if new_board not in visited:
                        queue.append((new_board, actions + "urdl"[j-1::-1]))
                        visited.add(new_board)

    return None

board = [['m', 's', '_', 'n', 'g'], ['a', 'o', 'i', 'e', 'h'], ['h', 'i', 'p', 'e', 's'], ['a', 'g', 'l', 'r', 'y']]
words = ['song', 'amish', 'hiper', 'agley']

print(bfs(board, words))
