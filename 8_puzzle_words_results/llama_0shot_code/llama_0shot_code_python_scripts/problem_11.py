
from collections import deque

def bfs(board, words):
    rows, cols = len(board), len(board[0])
    word_len = len(words[0]) + 1
    word_rows = word_len // cols
    total_words = len(words)
    words = [words[i:i+word_rows] for i in range(0, len(words), word_rows)]
    words = [''.join(word) for row in words for word in row]
    visited = set()
    queue = deque([(board, [], 0, 0)])
    directions = [(0, 1), (1, 1), (1, 0), (1, -1)]
    while queue:
        curr_board, swaps, r, c = queue.popleft()
        key = str(curr_board)
        if key in visited:
            continue
        visited.add(key)
        if curr_board[r][c] == '_':
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and curr_board[nr][nc] != '_':
                    new_board = [row.copy() for row in curr_board]
                    new_board[r][c], new_board[nr][nc] = new_board[nr][nc], new_board[r][c]
                    new_swaps = swaps + [(r, c, dr, dc)]
                    if len(new_swaps) + 1 == len(words):
                        return new_swaps[::-1] + [(nr, nc, -dr, -dc)]
                    queue.append((new_board, new_swaps, nr, nc))
        else:
            nr, nc = r, c + 1
            if nc < cols and curr_board[nr][nc] == '_':
                new_board = [row.copy() for row in curr_board]
                new_board[r][c], new_board[nr][nc] = new_board[nr][nc], new_board[r][c]
                new_swaps = swaps + [(r, c, 0, 1)]
                queue.append((new_board, new_swaps, nr, nc))
    return []

initial_board = [['o', 'b', 'e', 'd'], ['c', 'o', 'd', 'u'], ['w', 'a', '_', 'p'], ['y', 'u', 'l', 'p']]
words = ['bud', 'codo', 'waup', 'yelp']
print(bfs(initial_board, words))
