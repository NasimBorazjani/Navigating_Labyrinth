
import heapq
import math


def a_star():
    # Define the target words and the initial state of the board
    target_words = ['ned', 'wham', 'royt', 'hell', 'miek']
    initial_board = [['h', 'n', '_', 'd'], ['w', 'r', 'a', 'e'], ['e', 'o', 'y', 't'], ['h', 'e', 'l', 'm'], ['m', 'i', 'l', 'k']]
    num_rows = 5
    num_cols = 4

    visited_costs = {}
    visited_costs[str(initial_board)] = 0

    queue = [(0, 0, [], initial_board)]

    while queue:
        _, g, actions, board = heapq.heappop(queue)

        # Check if the current board matches the target words
        if all(''.join(row) == target_words[i] for i, row in enumerate(board)):
            return actions

        # Find the position of the blank space
        blank_pos = [(i, j) for i in range(num_rows) for j in range(num_cols) if board[i][j] == '_'][0]

        # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighbors
        for d_row, d_col in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            new_row, new_col = blank_pos[0] + d_row, blank_pos[1] + d_col
            # Check if the new position is valid
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                # Generate the new board after swapping the blank space
                new_board = [list(row) for row in board]
                new_board[blank_pos[0]][blank_pos[1]], new_board[new_row][new_col] = new_board[new_row][new_col], new_board[blank_pos[0]][blank_pos[1]]
                new_board = str(new_board)
                # The cost of the new state is the number of swaps made
                new_cost = g + 1

                if new_board not in visited_costs or new_cost < visited_costs[new_board]:
                    visited_costs[new_board] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_board, target_words), new_cost, actions + [(d_row, d_col)], eval(new_board))
    return None


def heuristic(board, target_words):
    # An admissible and consistent heuristic for this problem is the sum of the differences between the characters in the current board and the target words
    # This heuristic relaxes the constraint that only the blank space can be moved, assuming that all characters can be moved to their correct positions
    # It is admissible because it never overestimates the cost to reach the goal, as each character moved to its correct position reduces the heuristic cost
    # It is consistent because moving a character to its correct position reduces the heuristic cost of the successor node by 1, which is equal to the cost of reaching the successor node
    h = 0
    for i, row in enumerate(board):
        h += sum(1 for j, char in enumerate(row) if char != target_words[i][j])
    return h


print(a_star())
