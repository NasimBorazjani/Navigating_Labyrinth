
import heapq
import math


def a_star():
    # Define the initial state of the board as a 2d tuple
    initial_state = (('o', 't', 'p', 't'), ('c', 'u', 'm', 'u'), ('d', 'e', 'k', 'l'), ('w', 'l', 'r', 'o'), ('e', 'a', '_', 'a'), ('b', 't', 's', 'h'))
    target_words = ['tut', 'come', 'kell', 'word', 'tapa', 'bush']
    num_rows = 6
    num_cols = 4

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Unpack the state to get the current words in each row
        current_words = [''.join(row) for row in state]

        # If the current words match the target words, return the actions taken
        if current_words == target_words:
            return actions

        # Find the position of the blank space in the current state
        blank_pos = [(i, j) for i, row in enumerate(state) for j, tile in enumerate(row) if tile == '_'][0]

        # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighbors
        for d_row, d_col in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            new_row, new_col = blank_pos[0] + d_row, blank_pos[1] + d_col
            # Check if the new position is valid
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                # Generate the new state by swapping the blank space with the neighboring tile
                new_state = [list(row) for row in state]
                new_state[blank_pos[0]][blank_pos[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_pos[0]][blank_pos[1]]
                new_state = tuple(tuple(row) for row in new_state)
                # The cost of this state is the number of swaps made, as the task is to minimize the number of swaps required
                new_cost = g + 1

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # Calculate the heuristic cost to reach the goal state from the current state
                    h = heuristic(new_state, target_words)
                    heapq.heappush(queue, (g + h, new_cost, actions + [(d_row, d_col)], new_state))
    return None


def heuristic(state, target_words):
    # The heuristic function calculates the total number of characters that are not in the correct position in each row
    # This heuristic is admissible because it never overestimates the cost to reach the goal state, as each character not in the correct position must be swapped at least once
    # It is consistent because swapping a character to the correct position reduces the heuristic cost of the successor node by 1, which is equal to the cost of reaching the successor node
    h = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != target_words[i][j]:
                h += 1
    return h


print(a_star())
