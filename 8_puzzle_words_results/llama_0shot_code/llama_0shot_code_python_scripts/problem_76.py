
from collections import deque

def bfs(start, target_words):
    queue = deque([(start, [])])
    visited = set()
    moves = {'_': {'u': '_', 'd': '_', 'l': '_', 'r': '_'},
             'u': {'u': 'l', 'd': 'r', 'l': 'd', 'r': 'u'},
             'd': {'u': 'r', 'd': 'l', 'l': 'u', 'r': 'd'},
             'l': {'u': 'u', 'd': 'd', 'l': 'r', 'r': 'l'},
             'r': {'u': 'd', 'd': 'u', 'l': 'u', 'r': 'l'}}

    def get_word(board, i):
        return ''.join(board[i])

    def get_board(board, move):
        new_board = [list(row) for row in board]
        x, y = new_board[0].index('_'), 0
        new_board[0][x], new_board[y][x] = new_board[y][x], '_'
        return new_board

    while queue:
        board, swaps = queue.popleft()
        state = ''.join(board)
        if state in visited:
            continue
        visited.add(state)
        for i in range(1, len(board)):
            for move in moves:
                new_board = get_board(board, move)
                new_state = ''.join(new_board)
                if get_word(new_board, i) == target_words[i] and new_state not in visited:
                    queue.append((new_board, swaps + [move]))
        if get_word(board, 0) == target_words[0]:
            return swaps
    return None

initial_board = [['h', 'q', 'n', 'a', '_'], ['b', 'y', 'a', 'd', 'g'], ['d', 'e', 'c', 'a', 'o'], ['h', 'o', 'n', 'u', 'r'], ['p', 'i', 'c', 'k', 'y']]
target_words = ['quad', 'bhang', 'decay', 'honor', 'picky']

result = bfs(initial_board, target_words)
print(result)
