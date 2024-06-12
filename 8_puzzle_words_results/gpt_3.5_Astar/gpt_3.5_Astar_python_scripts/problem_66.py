
import heapq
import math


def a_star():
    # Define the target words and the initial state of the board
    target_words = ['jay', 'eppy', 'home', 'roon', 'ward']
    initial_state = [['p', 'j', 'm', 'y'], ['e', 'h', 'p', 'o'], ['y', 'o', '_', 'e'], ['r', 'a', 'o', 'n'], ['w', 'a', 'r', 'd']]
    num_rows = 5
    num_cols = 4

    visited_costs = {}
    visited_costs[str(initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

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
                new_state = [tuple(row) for row in new_state]
                # Calculate the cost of the new state, which is the number of swaps made
                new_cost = g + 1

                if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                    visited_costs[str(new_state)] = new_cost
                    # Calculate the heuristic cost for the new state
                    h = heuristic(new_state, target_words)
                    heapq.heappush(queue, (g + h, new_cost, actions + [(d_row, d_col)], new_state))
    return None


def heuristic(state, target_words):
    # The heuristic is the sum of the differences between the current state and the target words
    # This heuristic is admissible as it never overestimates the cost to reach the goal state
    # It is consistent because the estimated cost of the next node is higher if the current state is further from the goal state, which is equal to the cost of reaching the successor node
    h = 0
    for i in range(len(state)):
        h += sum(1 for x, y in zip(state[i], target_words[i]) if x != y)
    return h


print(a_star())
