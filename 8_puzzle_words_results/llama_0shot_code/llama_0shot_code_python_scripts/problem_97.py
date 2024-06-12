
from collections import deque

def bfs(board, words):
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = set()
    queue = deque([(board, [])])
    target = [list(word) for word in words]

    while queue:
        board, move_seq = queue.popleft()
        if board == target:
            return move_seq
        for i, j in moves:
            new_board, new_move = swap(board, (0, 0), (0, 1), i, j)
            if new_board not in visited:
                visited.add(new_board)
                queue.append((new_board, move_seq + [new_move]))

def swap(board, start, end, i, j):
    new_board = [row[:] for row in board]
    new_board[start[0]][start[1]], new_board[end[0]][end[1]] = new_board[end[0]][end[1]], new_board[start[0]][start[1]]
    new_end = (end[0] + i, end[1] + j)
    return new_board, (start, new_end)

initial_board = [['e', 'b', 'v', 'r', 'l', 't'], ['m', 'u', 'r', 'm', 'i', 'r'], ['h', 'o', 'a', 'a', '_', 'e'], ['c', 'n', 'i', 's', 'e', 's'], ['t', 'i', 'l', 'p', 'y', 'h']]
words = ['burst', 'merril', 'monase', 'chivey', 'tilpah']
print(bfs(initial_board, words))
