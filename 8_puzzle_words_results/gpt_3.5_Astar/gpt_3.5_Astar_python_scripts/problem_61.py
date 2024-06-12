
import heapq
import math


def a_star():
    # Define the initial state of the board as a 2d tuple
    initial_state = (('u', 'a', '_', 'r'),
                     ('h', 'e', 'm', 'e'),
                     ('m', 'i', 'i', 'p'),
                     ('v', 'a', 'v', 'j'),
                     ('f', 'i', 'm', 'i'))
    target_words = ['aer', 'hume', 'mimp', 'viva', 'fiji']
    num_rows = 5
    num_cols = 4

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Unpack the state to get the current board configuration
        board = [list(row) for row in state]
        # Flatten the board to check if it matches the target words
        current_words = [''.join(row).replace('_', '') for row in board]
        if current_words == target_words:
            return actions

        # Find the position of the blank space
        blank_pos = [(i, j) for i in range(num_rows) for j in range(num_cols) if board[i][j] == '_'][0]

        # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighbors
        for d_row, d_col in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            new_row, new_col = blank_pos[0] + d_row, blank_pos[1] + d_col
            # Check if the new position is valid
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                # Generate the new state
                new_board = [list(row) for row in board]
                new_board[blank_pos[0]][blank_pos[1]], new_board[new_row][new_col] = new_board[new_row][new_col], new_board[blank_pos[0]][blank_pos[1]]
                new_state = tuple(tuple(row) for row in new_board)
                # The cost of the new state is the number of swaps made, as the task is to minimize the number of swaps required
                new_cost = g + 1

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_board, target_words), new_cost, actions + [(d_row, d_col)], new_state))
    return None


def heuristic(board, target_words):
    # An admissible and consistent heuristic for this problem is the count of characters that are not in the correct position in each row
    # This heuristic relaxes the constraint that only the blank space can be moved, as it considers the number of characters that need to be swapped to reach the goal state
    # It is admissible because it never overestimates the cost to reach the goal, as each character that is not in the correct position must be swapped at least once
    # It's consistent because swapping a character reduces the heuristic cost of the successor node by 1, which is equal to the cost of reaching the successor node
    # Thus h(n) is always less than or equal to c(n, n’)(equal to 1) + h(n’)
    h = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != '_' and board[i][j] != target_words[i][j]:
                h += 1
    return h


print(a_star())
