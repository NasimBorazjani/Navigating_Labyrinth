
from collections import deque

def bfs(board, words):
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    start = (tuple(board[0]), board[1], board[2], board[3], board[4])
    end = (tuple(words[0]), words[1], words[2], words[3], words[4])
    visited = set([start])
    queue = deque([([], start)])

    while queue:
        moves, state = queue.popleft()
        if state == end:
            return moves
        for i, j in moves:
            new_board = swap(state, i, j)
            if new_board not in visited:
                visited.add(new_board)
                new_moves = moves + [(i, j)]
                queue.append((new_moves, new_board))

def swap(state, i, j):
    board = list(state[0])
    x, y = state[1].index('_'), state[1].index('_')
    board[x], board[y] = board[y], board[x]
    return (tuple(board), state[1], state[2], state[3], state[4])

board = [['r', 's', 'c', 'v', 'a'], ['b', 'b', 'y', 'r', 'e'], ['u', 'i', '_', 'n', 'i'], ['p', 'n', 'g', 'i', 'l'], ['l', 'i', 'y', 'n', 'e']]
words = ['siva', 'bryce', 'birny', 'pugil', 'linne']
print(bfs(board, words))
