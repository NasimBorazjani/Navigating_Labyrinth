
import heapq
import math


def a_star():
    # Define the target words and the initial state of the board
    target_words = ['rea', 'yeni', 'maam', 'apii', 'hevi', 'earl']
    initial_state = [['e', 'r', '_', 'a'],
                     ['y', 'i', 'n', 'm'],
                     ['a', 'a', 'a', 'm'],
                     ['a', 'v', 'i', 'e'],
                     ['i', 'e', 'p', 'i'],
                     ['e', 'h', 'r', 'l']]
    num_rows = 6
    num_cols = 4

    visited_costs = {}
    visited_costs[str(initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state is the goal state where each row spells the corresponding word
        if all(''.join(row) == target_words[i] for i, row in enumerate(state)):
            return actions

        # Find the position of the blank space in the current state
        blank_pos = [(i, j) for i in range(num_rows) for j in range(num_cols) if state[i][j] == '_'][0]

        # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighbors
        for d_row, d_col in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            new_row, new_col = blank_pos[0] + d_row, blank_pos[1] + d_col
            # Check if the new position is valid
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                # Generate the new state by swapping the blank space with the neighbor
                new_state = [list(row) for row in state]
                new_state[blank_pos[0]][blank_pos[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_pos[0]][blank_pos[1]]
                new_state_str = str(new_state)
                # Calculate the cost of the new state
                new_cost = g + 1

                if new_state_str not in visited_costs or new_cost < visited_costs[new_state_str]:
                    visited_costs[new_state_str] = new_cost
                    # Calculate the heuristic cost based on the number of characters that are not in the correct position in each row
                    h = heuristic(new_state, target_words)
                    heapq.heappush(queue, (g + h, new_cost, actions + [(d_row, d_col)], new_state))
    return None


def heuristic(state, target_words):
    # Calculate the heuristic cost based on the number of characters that are not in the correct position in each row
    h = 0
    for i, row in enumerate(state):
        for j, char in enumerate(row):
            if char != target_words[i][j]:
                h += 1
    return h


print(a_star())
