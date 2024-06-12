
import heapq
import math


def a_star():
    # Define the target words and the initial state of the board
    target_words = ['soft', 'tunny', 'apama', 'forum']
    initial_board = [['u', 's', 'o', 'f', 't'], ['t', 'a', 'n', 'n', 'y'], ['a', 'p', '_', 'm', 'o'], ['f', 'u', 'r', 'a', 'm']]
    num_rows = 4
    num_cols = 5

    visited_costs = {}
    visited_costs[str(initial_board)] = 0

    queue = [(0, 0, [], initial_board)]

    while queue:
        _, g, actions, board = heapq.heappop(queue)

        # Check if the current board matches the target words
        if check_board(board, target_words):
            return actions

        # Find the position of the blank space
        blank_pos = find_blank(board)

        # Generate all possible actions from the current state, which includes swapping the blank space with its 4 diagonal neighbors
        for d_row, d_col in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            new_row, new_col = blank_pos[0] + d_row, blank_pos[1] + d_col
            # Check if the new position is within the bounds of the board
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                # Generate the new board after swapping the blank space
                new_board = [list(row) for row in board]
                new_board[blank_pos[0]][blank_pos[1]], new_board[new_row][new_col] = new_board[new_row][new_col], new_board[blank_pos[0]][blank_pos[1]]
                new_board_str = str(new_board)
                # Calculate the cost of the new state
                new_cost = g + 1

                if new_board_str not in visited_costs or new_cost < visited_costs[new_board_str]:
                    visited_costs[new_board_str] = new_cost
                    heapq.heappush(queue, (g + heuristic(board, target_words), new_cost, actions + [(d_row, d_col)], new_board))
    return None


def check_board(board, target_words):
    # Check if the board matches the target words
    for i, word in enumerate(target_words):
        if ''.join(board[i]) != word:
            return False
    return True


def find_blank(board):
    # Find the position of the blank space
    for i in range(len(board)):
        for j in range(len(board[0]):
            if board[i][j] == '_':
                return (i, j)


def heuristic(board, target_words):
    # Calculate the heuristic cost based on the number of characters that are not in the correct position
    h = 0
    for i, word in enumerate(target_words):
        for j in range(len(word)):
            if board[i][j] != word[j]:
                h += 1
    return h


print(a_star())
