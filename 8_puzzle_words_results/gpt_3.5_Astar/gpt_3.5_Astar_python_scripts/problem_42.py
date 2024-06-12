
import heapq
import math


def a_star():
    # Define the initial state of the board as a 2d tuple
    initial_state = (('_', 'j', 'a', 'r', 'e', 'b'),
                     ('z', 'o', 'y', 's', 'i', 'i'),
                     ('r', 'e', 'r', 's', 't', 'y'),
                     ('g', 'e', 'i', 'q', 'u', 'a'))
    target_words = ['jerib', 'zoysia', 'reesty', 'griqua']
    num_rows = 4
    num_cols = 6

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Unpack the state to get the current board configuration
        board = [list(row) for row in state]
        current_words = [''.join(row).replace('_', '') for row in board]

        # Check if the current board configuration matches the target words
        if current_words == target_words:
            return actions

        # Find the position of the blank space
        blank_pos = [(i, j) for i in range(num_rows) for j in range(num_cols) if board[i][j] == '_'][0]

        # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighbors
        for d_row, d_col in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:
            new_row, new_col = blank_pos[0] + d_row, blank_pos[1] + d_col
            # Check if the new position is within the bounds of the board
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                # Create a new board configuration by swapping the blank space with the neighboring tile
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
    # The heuristic function calculates the number of characters that are not in the correct position in each row
    # This heuristic is admissible because it underestimates the cost to reach the goal state, as each character not in the correct position will require at least one swap to reach the goal state
    # The heuristic is consistent because moving a character to the correct position reduces the heuristic cost of the successor node by 1, which is equal to the cost of reaching the successor node
    h = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != '_' and board[i][j] != target_words[i][j]:
                h += 1
    return h


print(a_star())
