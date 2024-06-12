
from collections import deque

def bfs(board, words):
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    start = (board, None)
    visited = set()
    queue = deque([(start, [])])

    while queue:
        (current_board, direction), move_seq = queue.popleft()
        if current_board[1:] == [list(word) for word in words]:
            return move_seq
        for i in range(len(current_board)):
            for j in range(len(current_board[0])):
                if current_board[i][j] == '_':
                    for move in moves:
                        ni, nj = i + move[0], j + move[1]
                        if 0 <= ni < len(current_board) and 0 <= nj < len(current_board[0]):
                            new_board = [list(row) for row in current_board]
                            new_board[i][j], new_board[ni][nj] = new_board[ni][nj], new_board[i][j]
                            new_state = (tuple(map(tuple, new_board)), move)
                            if new_state not in visited:
                                visited.add(new_state)
                                queue.append((new_state, move_seq + [move]))

initial_board = [['g', 'f', 't', 'i', 'm'], ['a', 'l', 'a', 'a', 'e'], ['n', 's', '_', 'i', 'e'], ['f', 'p', 'o', 'k', 'y'], ['z', 'o', 'r', 'a', 'r']]
words = ['frim', 'agate', 'askip', 'floey', 'zonar']
print(bfs(initial_board, words))
