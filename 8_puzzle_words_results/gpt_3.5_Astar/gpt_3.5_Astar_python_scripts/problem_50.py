
import heapq
import math


def a_star():
    # Define the target words and the initial state of the board
    target_words = ['humus', 'bywork', 'cereus', 'clarty']
    initial_board = [['y', 'h', 'r', 'm', '_', 's'],
                     ['b', 'o', 'w', 'k', 'r', 'u'],
                     ['r', 'e', 'l', 'e', 'u', 's'],
                     ['c', 'c', 'a', 'u', 't', 'y']]
    num_rows = 4
    num_cols = 6

    visited_costs = {}
    visited_costs[str(initial_board)] = 0

    queue = [(0, 0, [], initial_board)]

    while queue:
        _, g, actions, board = heapq.heappop(queue)

        # Check if the current board state matches the target words
        if ["".join(row) for row in board] == target_words:
            return actions

        # Find the position of the blank space in the board
        blank_pos = [(i, j) for i in range(num_rows) for j in range(num_cols) if board[i][j] == '_'][0]

        # Generate all possible actions from the current state, which includes swapping the blank space with its 4 diagonal neighbors
        for d_row, d_col in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            new_row, new_col = blank_pos[0] + d_row, blank_pos[1] + d_col
            # Check if the new position is within the bounds of the board
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                # Generate the new board state after swapping the blank space
                new_board = [list(row) for row in board]
                new_board[blank_pos[0]][blank_pos[1]], new_board[new_row][new_col] = new_board[new_row][new_col], new_board[blank_pos[0]][blank_pos[1]]
                new_board = tuple(tuple(row) for row in new_board)
                # Calculate the cost of the new state
                new_cost = g + 1

                if str(new_board) not in visited_costs or new_cost < visited_costs[str(new_board)]:
                    visited_costs[str(new_board)] = new_cost
                    # Calculate the heuristic cost for the new state
                    h = heuristic(new_board, target_words)
                    heapq.heappush(queue, (g + h, new_cost, actions + [(d_row, d_col)], new_board))
    return None


def heuristic(board, target_words):
    # The heuristic function calculates the number of characters that are not in the correct position in each row
    # This heuristic is admissible because it underestimates the cost to reach the goal state, as each character not in the correct position will require at least one swap to reach the goal state
    # The heuristic is consistent because moving a character to the correct position reduces the heuristic cost of the successor node by 1, which is equal to the cost of reaching the successor node
    h = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != '_' and board[i][j] != target_words[i][j]:
                h += 1
    return h


print(a_star())
