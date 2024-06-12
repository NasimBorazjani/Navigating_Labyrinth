
import heapq
import math


def a_star():
    # Define the target words and the initial state of the board
    target_words = ['biwa', 'ramal', 'monte', 'spink', 'width', 'mover']
    initial_board = [['a', 'b', 'n', 'w', 'a'],
                     ['r', 'd', 'm', 'p', 'l'],
                     ['h', 'o', 'a', 't', '_'],
                     ['s', 'm', 'i', 'i', 'k'],
                     ['w', 'i', 'o', 't', 'n'],
                     ['m', 'e', 'v', 'e', 'r']]
    num_rows = 6
    num_cols = 5

    visited_costs = {}
    visited_costs[str(initial_board)] = 0

    queue = [(0, 0, [], initial_board)]

    while queue:
        _, g, actions, board = heapq.heappop(queue)

        # Check if the current board state matches the target words
        if check_board(board, target_words):
            return actions

        # Find the position of the blank space in the board
        blank_pos = find_blank_position(board)

        # Generate all possible actions from the current state, which includes swapping the blank space with its 4 diagonal neighbors
        for d_row, d_col in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            new_row, new_col = blank_pos[0] + d_row, blank_pos[1] + d_col
            # Check if the new position is within the bounds of the board
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                # Create a new board state by swapping the blank space with the neighboring tile
                new_board = [list(row) for row in board]
                new_board[blank_pos[0]][blank_pos[1]], new_board[new_row][new_col] = new_board[new_row][new_col], new_board[blank_pos[0]][blank_pos[1]]
                new_board_str = str(new_board)
                # Calculate the cost of the new state
                new_cost = g + 1

                if new_board_str not in visited_costs or new_cost < visited_costs[new_board_str]:
                    visited_costs[new_board_str] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_board, target_words), new_cost, actions + [(d_row, d_col)], new_board))
    return None


def check_board(board, target_words):
    # Check if the board state matches the target words
    for i, word in enumerate(target_words):
        if i == 0:
            # First word has m-1 characters
            if ''.join(board[i][:len(word)]) != word:
                return False
        else:
            if ''.join(board[i][:len(word)]) != word:
                return False
    return True


def find_blank_position(board):
    # Find the position of the blank space in the board
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '_':
                return (i, j)
    return None


def heuristic(board, target_words):
    # The heuristic function calculates the number of characters that are not in the correct position in each row
    # This heuristic is admissible because it underestimates the cost to reach the goal state, as each swap can only move one character to the correct position
    # The heuristic is consistent because the estimated cost of the next node is higher if a character is moved further from its correct position, which is equal to the cost of reaching the successor node
    h = 0
    for i, word in enumerate(target_words):
        if i == 0:
            # First word has m-1 characters
            h += sum(1 for x, y in zip(board[i][:len(word)], word) if x != y)
        else:
            h += sum(1 for x, y in zip(board[i][:len(word)], word) if x != y)
    return h


print(a_star())
