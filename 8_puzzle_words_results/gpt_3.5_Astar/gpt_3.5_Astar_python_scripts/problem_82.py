
import heapq
import math


def a_star():
    # Define the target words and the initial state of the board
    target_words = ['wah', 'axed', 'tine', 'cest', 'fico', 'pyin']
    initial_board = [['x', 'w', 'y', 'h'], ['a', 't', 'e', 'a'], ['n', 'i', '_', 'e'], ['c', 'c', 's', 't'], ['d', 'i', 'e', 'o'], ['p', 'f', 'i', 'n']]
    num_rows = len(initial_board)
    num_cols = len(initial_board[0])

    visited_costs = {}
    visited_costs[str(initial_board)] = 0

    queue = [(0, 0, [], initial_board)]

    while queue:
        _, g, actions, board = heapq.heappop(queue)

        # Check if the current board state matches the target words
        if is_target(board, target_words):
            return actions

        # Find the position of the blank space in the board
        blank_pos = find_blank(board)

        # Generate all possible actions from the current state, which includes swapping the blank space with its 4 diagonal neighbors
        for d_row, d_col in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            new_row, new_col = blank_pos[0] + d_row, blank_pos[1] + d_col

            # Check if the new position is within the bounds of the board
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                # Create a new board state by swapping the blank space with the neighboring tile
                new_board = [list(row) for row in board]
                new_board[blank_pos[0]][blank_pos[1]], new_board[new_row][new_col] = new_board[new_row][new_col], new_board[blank_pos[0]][blank_pos[1]]
                new_board_str = str(new_board)
                new_cost = g + 1

                # Check if the new state is unvisited or has a lower cost
                if new_board_str not in visited_costs or new_cost < visited_costs[new_board_str]:
                    visited_costs[new_board_str] = new_cost
                    # Add the action to the list of actions
                    heapq.heappush(queue, (g + heuristic(new_board, target_words), new_cost, actions + [(d_row, d_col)], new_board))

    return None


def is_target(board, target_words):
    # Check if the rows of the board match the target words
    for i, word in enumerate(target_words):
        if ''.join(board[i]) != word:
            return False
    return True


def find_blank(board):
    # Find the position of the blank space in the board
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '_':
                return (i, j)
    return None


def heuristic(board, target_words):
    # The heuristic function calculates the total number of characters that are not in the correct position
    h = 0
    for i, word in enumerate(target_words):
        for j, char in enumerate(word):
            if board[i][j] != char:
                h += 1
    return h


print(a_star())
