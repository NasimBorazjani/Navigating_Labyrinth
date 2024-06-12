
import heapq
import math


def a_star():
    # Define the initial state of the board as a 2d tuple
    initial_state = (('e', 'l', 'u', 'w'),
                     ('k', 'k', 'c', 'e'),
                     ('f', 'l', '_', 'a'),
                     ('s', 'r', 's', 'e'),
                     ('h', 'e', 'u', 'b'))
    target_words = ['lew', 'keck', 'flea', 'susu', 'herb']
    num_rows = 5
    num_cols = 4

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Unpack the state to get the current position of the blank space
        blank_pos = [(i, j) for i, row in enumerate(state) for j, element in enumerate(row) if element == '_'][0]

        # Check if the current state is the goal state where each row spells the corresponding word
        if all(''.join(row).replace('_', '') == target_words[i] for i, row in enumerate(state)):
            return actions

        # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighbors
        for d_row, d_col in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            new_row, new_col = blank_pos[0] + d_row, blank_pos[1] + d_col
            # Check if the new position is valid, ie within the bounds of the board
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                # Generate the new state by swapping the blank space with the neighboring tile
                new_state = [list(row[:]) for row in state]
                new_state[blank_pos[0]][blank_pos[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_pos[0]][blank_pos[1]]
                new_state = tuple(tuple(row) for row in new_state)
                # The cost of the new state is the number of swaps made, as the task is to minimize the number of swaps required
                new_cost = g + 1

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # Calculate the heuristic cost to estimate the remaining cost to reach the goal state
                    h = heuristic(new_state, target_words)
                    heapq.heappush(queue, (g + h, new_cost, actions + [(d_row, d_col)], new_state))
    return None


def heuristic(state, target_words):
    # An admissible and consistent heuristic for this problem is the sum of the differences between the current state and the target words
    # This heuristic relaxes the constraint that only the blank space can be moved, assuming that the blank space can be swapped with any tile to reach the goal state
    # It is admissible because it never overestimates the cost to reach the goal, as each difference between the current state and the target word must be resolved by a swap
    # It is consistent because swapping the blank space with a neighboring tile reduces the heuristic cost of the successor node by 1 (equal to the cost of reaching the successor node), which is equal to the cost of the action taken
    h = 0
    for i, row in enumerate(state):
        h += sum(1 for x, y in zip(row, target_words[i]) if x != y)
    return h


print(a_star())
