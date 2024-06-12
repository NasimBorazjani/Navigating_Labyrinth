
from collections import deque

def bfs(init_board):
    moves = deque([(init_board, '')])
    visited = set()
    target_words = ['ekka', 'bifer', 'magma', 'dinka', 'brett']
    
    while moves:
        board, path = moves.popleft()
        if board[2][2] == '_':
            continue
        if board[1:] == [list(word) for word in target_words]:
            return path
        for i in range(2):
            for j in range(2, 4):
                if 0 <= i < len(board) and 0 <= j < len(board[0]):
                    new_board = [row.copy() for row in board]
                    new_board[i][j], new_board[2][2] = new_board[2][2], new_board[i][j]
                    new_board_str = str(new_board)
                    if new_board_str not in visited:
                        visited.add(new_board_str)
                        moves.append((new_board, path + 'ur' if i == 0 and j == 2 else 'dr'))
    return None

init_board = [['i', 'e', 'k', 'k', 'a'], ['b', 'e', 'f', 'a', 'r'], ['g', 'a', '_', 'm', 'e'], ['d', 'i', 'n', 'k', 'a'], ['b', 'r', 'm', 't', 't']]
print(bfs(init_board))
