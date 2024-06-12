
from collections import deque

def bfs(init_board, target_words):
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # up-right, down-right, up-left, down-left
    target_board = [''.join(target_words[i:i+len(init_board[0])-1] + [target_words[i+1]]) for i in range(len(target_words))]
    target_board = '\n'.join(target_board)
    init_board = '\n'.join([''.join(row) for row in init_board])
    visited = set()
    queue = deque([(init_board, '')])
    while queue:
        board, move = queue.popleft()
        if board == target_board:
            return move
        if board not in visited:
            visited.add(board)
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == '_':
                        for move_ in moves:
                            ni, nj = i + move_[0], j + move_[1]
                            if 0 <= ni < len(board) and 0 <= nj < len(board[i]) and board[ni][nj] != '_':
                                new_board = list(board)
                                new_board[i], new_board[ni] = new_board[ni], new_board[i]
                                new_board = ''.join(new_board)
                                queue.append((new_board, move + (move_ if move_ != (0, 1) else 'u')))  # use 'u' to represent up-right

init_board = [['v', 't', 'u', 'i'], ['o', 'w', 'e', 'i'], ['y', 'd', '_', 'c'], ['d', 'i', 'e', 'm']]
target_words = ['twi', 'ovey', 'udic', 'diem']
print(bfs(init_board, target_words))
