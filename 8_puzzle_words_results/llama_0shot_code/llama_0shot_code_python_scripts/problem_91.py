
from collections import deque

def bfs(board, words):
    target = ','.join(words)
    visited = set()
    q = deque([(board, '')])
    while q:
        current, swaps = q.popleft()
        key = ''.join(current)
        if key in visited:
            continue
        visited.add(key)
        if key == target:
            return swaps
        for i, j in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            for x, y in [(i, j), (i, -j), (-i, j), (-i, -j)]:
                ni, nj = i + 1, j + 1
                if 0 <= ni < len(current) and 0 <= nj < len(current[0]) and current[ni][nj] == '_':
                    new_board = [list(row) for row in current]
                    new_board[ni][nj], new_board[ni - x][nj - y] = new_board[ni - x][nj - y], new_board[ni][nj]
                    q.append(([''.join(row) for row in new_board], swaps + ' ' + 'udrl'[['dr', 'ur', 'dl', 'ul'].index(('d' if x == 1 else 'u') + ('r' if y == 1 else 'l'))]))
    return None

board = [['t', 'p', 'c', 'p', 'o', 'y'], ['s', 'e', 'o', 't', 'k', 's'], ['p', 'i', 'w', 't', '_', 'l'], ['s', 'n', 'a', 'y', 'h', 'a'], ['c', 'a', 'e', 'c', 'p', 'n']]
words = ['peppy', 'stocky', 'pistol', 'swathe', 'cancan']
print(bfs(board, words))
