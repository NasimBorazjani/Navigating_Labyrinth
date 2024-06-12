
import heapq
import math


def a_star():
    # Define the target words and the initial state of the board
    target_words = ['wolf', 'stunt', 'lammy', 'faded']
    initial_board = [['t', 'w', 'y', 'l', '_'], ['s', 'a', 'u', 'f', 't'], ['o', 'a', 'e', 'm', 'n'], ['f', 'l', 'd', 'm', 'd']]
    num_rows = 4
    num_cols = 5

    visited_costs = {}
    visited_costs[str(initial_board)] = 0

    queue = [(0, 0, [], initial_board)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state is the goal state where each row spells the corresponding word
        if all(''.join(row) == word for row, word in zip(state, target_words)):
            return actions

        # Find the position of the blank space in the current state
        blank_pos = [(i, j) for i in range(num_rows) for j in range(num_cols) if state[i][j] == '_'][0]

        # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighbors
        for d_row, d_col in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            new_row, new_col = blank_pos[0] + d_row, blank_pos[1] + d_col
            # Check if the new position is within the bounds of the board
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                # Generate the new state by swapping the blank space with the neighbor
                new_state = [list(row) for row in state]
                new_state[blank_pos[0]][blank_pos[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_pos[0]][blank_pos[1]]
                # Encode the new state as a string to store in the visited_costs dictionary
                new_state_str = str(new_state)
                # The cost of the new state is the number of swaps made, as the task is to minimize the number of swaps required
                new_cost = g + 1

                if new_state_str not in visited_costs or new_cost < visited_costs[new_state_str]:
                    visited_costs[new_state_str] = new_cost
                    # Calculate the heuristic cost to estimate the remaining cost to reach the goal state
                    h = heuristic(new_state, target_words)
                    heapq.heappush(queue, (g + h, new_cost, actions + [(d_row, d_col)], new_state))

    return None


def heuristic(state, target_words):
    # The heuristic function calculates the total number of characters that are not in the correct position in each row
    # This heuristic is admissible because it underestimates the cost to reach the goal state, as each swap can only move one character to the correct position
    # It is consistent because the estimated cost of the next node is higher if characters are not in the correct position, and the cost of moving a character to the correct position is 1 (equal to the cost of reaching the successor node)
    h = 0
    for row, word in zip(state, target_words):
        for i in range(len(row)):
            if row[i] != '_' and row[i] != word[i]:
                h += 1
    return h


print(a_star())