
import heapq
import math


def a_star():
    # Define the initial state of the board as a 2d tuple
    initial_state = (('e', 'b', 'v', 'r', 'l', 't'),
                     ('m', 'u', 'r', 'm', 'i', 'r'),
                     ('h', 'o', 'a', 'a', '_', 'e'),
                     ('c', 'n', 'i', 's', 'e', 's'),
                     ('t', 'i', 'l', 'p', 'y', 'h'))
    target_words = ['burst', 'merril', 'monase', 'chivey', 'tilpah']
    num_rows = 5
    num_cols = 6

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
            # Check if the new position is within the bounds of the board
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                # Generate the new state by swapping the blank space with the neighboring tile
                new_state = [list(row) for row in state]
                new_state[blank_pos[0]][blank_pos[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_pos[0]][blank_pos[1]]
                new_state = tuple(tuple(row) for row in new_state)
                # The cost of the new state is the number of swaps made, as the task is to minimize the number of swaps required
                new_cost = g + 1

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, target_words), new_cost, actions + [(d_row, d_col)], new_state))
    return None


def is_goal_state(state, target_words):
    # Check if the current state matches the target words
    for i, word in enumerate(target_words):
        if ''.join(state[i]) != word:
            return False
    return True


def heuristic(state, target_words):
    # An admissible and consistent heuristic for this problem is the sum of the number of characters that are not in the correct position in each row
    # This heuristic relaxes the constraint that only the blank space can be moved, as it considers the number of characters that need to be swapped to reach the goal state
    # It is admissible because it never overestimates the cost to reach the goal, as each character that is not in the correct position must be swapped at least once
    # It's consistent because moving a character from one position to another reduces the heuristic cost of the successor node by 1, which is equal to the cost of reaching the successor node
    # Thus h(n) is always less than or equal to c(n, n’)(equal to 1) + h(n’)
    h = 0
    for i, word in enumerate(target_words):
        for j, char in enumerate(word):
            if state[i][j] != char:
                h += 1
    return h


print(a_star())
