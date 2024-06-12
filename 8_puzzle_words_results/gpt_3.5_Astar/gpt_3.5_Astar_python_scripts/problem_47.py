
import heapq
import math


def a_star():
    # Define the initial state of the board as a 2d tuple
    initial_state = (('r', 'p', '_', 'n', 'n', 'o'),
                     ('u', 'o', 'c', 'o', 'i', 'n'),
                     ('l', 'n', 'h', 'i', 'g', 'e'),
                     ('b', 'd', 'i', 'n', 'k', 's'))
    target_words = ['pongo', 'urchin', 'ondine', 'blinks']
    num_rows = 4
    num_cols = 6

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Unpack the state to get the current board configuration
        board = [list(row) for row in state]
        # Flatten the board to check if it matches the target words
        flat_board = [cell for row in board for cell in row]
        flat_board = ''.join(flat_board)

        # Check if the current board configuration matches the target words
        if flat_board == ''.join(target_words):
            return actions

        # Find the position of the blank space in the board
        blank_pos = [(i, j) for i, row in enumerate(board) for j, cell in enumerate(row) if cell == '_'][0]

        # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighbors
        for d_row, d_col in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            new_row, new_col = blank_pos[0] + d_row, blank_pos[1] + d_col
            # Check if the new position is within the bounds of the board
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                # Generate the new state by swapping the blank space with the neighbor
                new_board = [list(row) for row in board]
                new_board[blank_pos[0]][blank_pos[1]], new_board[new_row][new_col] = new_board[new_row][new_col], new_board[blank_pos[0]][blank_pos[1]]
                new_state = tuple(tuple(row) for row in new_board)
                # The cost of the new state is the number of swaps made, as the task is to minimize the number of swaps required
                new_cost = g + 1

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # Calculate the heuristic cost to estimate the distance to the goal state
                    h = heuristic(new_board, target_words)
                    heapq.heappush(queue, (g + h, new_cost, actions + [(d_row, d_col)], new_state))
    return None


def heuristic(board, target_words):
    # The heuristic function calculates the number of characters that are not in the correct position in the board compared to the target words
    # This heuristic is admissible because it never overestimates the cost to reach the goal state, as each character that is not in the correct position must be swapped at least once
    # It is consistent because swapping a character to the correct position reduces the heuristic cost of the successor node by 1, which is equal to the cost of reaching the successor node
    flat_board = [cell for row in board for cell in row]
    flat_board = ''.join(flat_board)
    h = sum([1 for i in range(len(flat_board)) if flat_board[i] != ''.join(target_words)[i]])
    return h


print(a_star())
