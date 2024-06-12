
from collections import deque

def bfs(board, words):
    initial_board = "".join(["".join(row) for row in board])
    initial_state = (initial_board, "")
    visited = {initial_board: ""}
    queue = deque([initial_state])
    while queue:
        current_board, swap_actions = queue.popleft()
        current_state = [current_board[i:i+len(words[0])] for i in range(0, len(current_board), len(words[0]))]
        if current_state == words:
            return swap_actions
        for i in range(len(current_state)):
            for j in range(len(current_state[i])):
                if current_state[i][j] == "_":
                    for dx, dy in [(-1, 1), (1, 1), (-1, -1), (1, -1)]: # up-right, down-right, up-left, down-left
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < len(current_state) and 0 <= ny < len(current_state[0]):
                            new_board = list(current_board)
                            new_board[i*len(words[0])+j], new_board[nx*len(words[0])+ny] = new_board[nx*len(words[0])+ny], new_board[i*len(words[0])+j]
                            new_board = "".join(new_board)
                            new_state = (new_board, swap_actions + " " + str((i, j, nx, ny)))
                            if new_board not in visited:
                                visited[new_board] = swap_actions + " " + str((i, j, nx, ny))
                                queue.append(new_state)
    return None

board = [['o', 'l', '_', 'z'], ['c', 'i', 'o', 's'], ['e', 'n', 'o', 's'], ['c', 'e', 'z', 'o'], ['g', 'a', 's', 't']]
words = ["liz", "coos", "enos", "coze", "gast"]
print(bfs(board, words))
