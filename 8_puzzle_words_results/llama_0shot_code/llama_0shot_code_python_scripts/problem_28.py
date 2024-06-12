
from collections import deque

def bfs(initial_board, target_words):
    queue = deque([(initial_board, [])])
    target_words = set(target_words)
    smallest_swap_sequence = None

    while queue:
        board, swaps = queue.popleft()
        if board[2][0] in target_words:
            if smallest_swap_sequence is None or len(swaps) < len(smallest_swap_sequence):
                smallest_swap_sequence = swaps
            target_words.remove(board[2][0])
            if not target_words:
                break
        for i in range(2):
            for j in range(2):
                if i == 0 and j == 1: continue
                new_board = [row.copy() for row in board]
                new_board[i][j], new_board[1-i][1-j] = new_board[1-i][1-j], new_board[i][j]
                queue.append((new_board, swaps + [f"({i},{j})->{1-i},{1-j}"]))

    return smallest_swap_sequence

initial_board = [['a', 'a', 'e', 'e', 'y'], ['h', 'a', 'i', 't', 'h'], ['_', 'r', 'k', 'n', 't'], ['m', 'k', 'n', 'o', 'o']]
target_words = ["akey", "haikh", "trone", "manto"]

print(bfs(initial_board, target_words))
