
import heapq
import math


def a_star():
    # Define the target words and the initial state of the board
    target_words = ['jin', 'grun', 'sita', 'boba', 'rump', 'wang']
    initial_board = [['r', 'j', 't', 'n'], ['g', 'a', 'u', 'i'], ['n', 'i', '_', 'a'], ['b', 's', 'b', 'o'], ['m', 'u', 'a', 'p'], ['w', 'r', 'n', 'g']]
    num_rows = 6
    num_cols = 4

    visited_costs = {}
    visited_costs[str(initial_board)] = 0

    queue = [(0, 0, [], initial_board)]

    while queue:
        _, g, actions, board = heapq.heappop(queue)

        # Convert the board to a string to check if it matches the target words
        board_str = str(board)
        if all(''.join(row) == target_words[i] for i, row in enumerate(board)):
            return actions

        # Find the position of the blank space in the board
        blank_pos = [(i, j) for i in range(num_rows) for j in range(num_cols) if board[i][j] == '_'][0]

        # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighbors
        for d_row, d_col in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            new_row, new_col = blank_pos[0] + d_row, blank_pos[1] + d_col
            # Check if the new position is within the bounds of the board
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                # Generate the new board after swapping the blank space with the neighbor
                new_board = [list(row) for row in board]
                new_board[blank_pos[0]][blank_pos[1]], new_board[new_row][new_col] = new_board[new_row][new_col], new_board[blank_pos[0]][blank_pos[1]]
                # Convert the new board to a string for comparison
                new_board_str = str(new_board)
                # Calculate the cost of the new state
                new_cost = g + 1

                if new_board_str not in visited_costs or new_cost < visited_costs[new_board_str]:
                    visited_costs[new_board_str] = new_cost
                    # Calculate the heuristic cost for the new state
                    h = heuristic(new_board, target_words)
                    heapq.heappush(queue, (g + h, new_cost, actions + [(d_row, d_col)], new_board))
    return None


def heuristic(board, target_words):
    # The heuristic is the sum of the differences between the current board and the target words
    # This heuristic is admissible because it underestimates the cost to reach the goal state, as it assumes that the blank space can be swapped with any character to reach the target word
    # The heuristic is consistent because the cost of moving the blank space to a neighbor is always 1, which is equal to the cost of reaching the successor node
    h = 0
    for i, row in enumerate(board):
        h += sum(1 for j in range(len(row)) if row[j] != target_words[i][j])
    return h


print(a_star())
