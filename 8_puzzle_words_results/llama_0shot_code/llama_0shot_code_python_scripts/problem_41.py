
from collections import deque

def bfs(init_board, words):
    # Define the 4 possible moves
    moves = [(-1, 1), (1, 1), (-1, -1), (1, -1)]
    # Initialize the queue with the initial state and the empty list of moves
    queue = deque([(init_board, [])])
    # Initialize the set of visited states with the initial state
    visited = set([str(init_board)])
    # Define the goal state
    goal_state = ['_'.join(word) for word in words]

    while queue:
        board, swaps = queue.popleft()
        if board == goal_state:
            return swaps
        for move in moves:
            new_board = swap(board, move)
            if str(new_board) not in visited:
                visited.add(str(new_board))
                queue.append((new_board, swaps + [move]))

def swap(board, move):
    blank_row, blank_col = find_blank(board)
    new_blank_row, new_blank_col = blank_row + move[0], blank_col + move[1]
    new_board = [row.copy() for row in board]
    new_board[blank_row][blank_col], new_board[new_blank_row][new_blank_col] = new_board[new_blank_row][new_blank_col], new_board[blank_row][blank_col]
    return new_board

def find_blank(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '_':
                return i, j
