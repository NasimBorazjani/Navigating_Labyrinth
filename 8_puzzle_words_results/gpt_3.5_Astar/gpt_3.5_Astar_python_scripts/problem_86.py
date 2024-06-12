
import heapq
import math


def a_star():
    # Define the initial state of the board as a 2d tuple
    initial_state = (('e', 'm', 'a', 't', 'a'),
                     ('p', 'k', 'n', 'u', 'l'),
                     ('u', 'h', 'r', 'u', 'm'),
                     ('m', 't', 'r', 'u', 't'),
                     ('o', 'r', '_', 'k', 'e'),
                     ('e', 't', 'a', 'h', 'a'))
    target_words = ['muta', 'penal', 'thrum', 'murut', 'troke', 'ekaha']
    num_rows = 6
    num_cols = 5

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Unpack the state to get the current position of the blank space
        blank_pos = [(i, j) for i, row in enumerate(state) for j, cell in enumerate(row) if cell == '_'][0]

        # Check if the current state is the goal state
        if is_goal_state(state, target_words):
            return actions

        # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighbors
        for d_row, d_col in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            new_row, new_col = blank_pos[0] + d_row, blank_pos[1] + d_col
            # Check if the new position is valid
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                # Generate the new state by swapping the blank space with the neighboring tile
                new_state = [list(row) for row in state]
                new_state[blank_pos[0]][blank_pos[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_pos[0]][blank_pos[1]]
                new_state = tuple(tuple(row) for row in new_state)
                # The cost of the new state is the number of swaps made, as the task is to minimize the number of swaps required
                new_cost = g + 1

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # Calculate the heuristic cost to estimate the distance to the goal state
                    h = heuristic(new_state, target_words)
                    heapq.heappush(queue, (g + h, new_cost, actions + [(d_row, d_col)], new_state))
    return None


def is_goal_state(state, target_words):
    # Check if the rows of the state spell out the target words
    for i, word in enumerate(target_words):
        if ''.join(state[i]).replace('_', '') != word:
            return False
    return True


def heuristic(state, target_words):
    # The heuristic is the sum of the differences between the current state and the target words
    # This heuristic is admissible because it never overestimates the cost to reach the goal state
    # It is consistent because the estimated cost of the next node is higher if the current state differs more from the target words, which is equal to the cost of reaching the successor node
    h = 0
    for i, word in enumerate(target_words):
        h += sum(1 for a, b in zip(state[i], word) if a != b)
    return h


print(a_star())
