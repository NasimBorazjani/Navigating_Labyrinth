
from collections import deque

def bfs(board, words):
    rows, cols = len(board), len(board[0])
    word_pos = {word: pos for pos, word in enumerate(words)}
    visited, queue = set(), deque([(board, [], 0)])
    
    while queue:
        curr_board, swaps, pos = queue.popleft()
        key = str(curr_board)
        
        if key in word_pos and (key not in visited or len(swaps) < len(visited[key])):
            visited[key] = swaps
            continue
        
        if pos == cols * rows - 1:
            continue
        
        r, c = divmod(pos, cols)
        for dr, dc in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                new_board = [row.copy() for row in curr_board]
                new_board[r][c], new_board[nr][nc] = new_board[nr][nc], new_board[r][c]
                new_pos = pos + 1 if r == nr else pos + dc
                queue.append((new_board, swaps + [dr * dc], new_pos))

    return visited

def solve(board, words):
    result = bfs(board, words)
    return {word: result[str(list(map(list, [['_'] + row[1:] for row in board]] + [['_'] + word]))] for word in words}

board = [['o', 'k', 's', 't', 'a', 'r'], ['b', 'y', 'n', 'i', 'a', 'a'], ['s', 'a', '_', 'b', 'a', 'r'], ['m', 'o', 'p', 'e', 'n', 'u'], ['v', 'o', 'm', 'e', 'a', 'r']]
words = ['katar', 'bonsai', 'sambar', 'mopane', 'voyeur']
print(solve(board, words))
