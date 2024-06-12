
import heapq
import math


def a_star():
    # Define the target words and the initial state of the board
    target_words = ['chank', 'hormic', 'tigtag', 'tornal', 'zythum']
    initial_state = [['o', 'c', 'a', 'a', 'n', 'k'],
                     ['h', 'm', 'r', 'l', 'i', 'g'],
                     ['h', 'i', 'o', 't', 'u', 'g'],
                     ['t', 'n', 'r', 't', 'a', 'c'],
                     ['z', 'y', 't', 'h', '_', 'm']]
    num_rows = 5
    num_cols = 6

    visited_costs = {}
    visited_costs[str(initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state matches the target words
        if check_target_words(state, target_words):
            return actions

        # Find the position of the blank space
        blank_pos = find_blank_position(state)

        # Generate all possible actions from the current state, which includes swapping the blank space with its 4 diagonal neighbors
        for d_row, d_col in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            new_row, new_col = blank_pos[0] + d_row, blank_pos[1] + d_col
            # Check if the new position is within the bounds of the board
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                # Generate the new state by swapping the blank space with the neighboring tile
                new_state = [list(row) for row in state]
                new_state[blank_pos[0]][blank_pos[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_pos[0]][blank_pos[1]]
                new_state_str = str(new_state)
                # The cost of the new state is the number of swaps made, as the task is to minimize the number of swaps required
                new_cost = g + 1

                if new_state_str not in visited_costs or new_cost < visited_costs[new_state_str]:
                    visited_costs[new_state_str] = new_cost
                    # Calculate the heuristic cost based on the number of misplaced characters in each row
                    h = heuristic(new_state, target_words)
                    heapq.heappush(queue, (g + h, new_cost, actions + [(d_row, d_col)], new_state))

    return None


def check_target_words(state, target_words):
    # Check if the rows of the state spell out the target words
    for i, word in enumerate(target_words):
        if ''.join(state[i]) != word:
            return False
    return True


def find_blank_position(state):
    # Find the position of the blank space in the state
    for i, row in enumerate(state):
        for j, char in enumerate(row):
            if char == '_':
                return (i, j)
    return None


def heuristic(state, target_words):
    # Calculate the heuristic cost based on the number of misplaced characters in each row
    h = 0
    for i, word in enumerate(target_words):
        for j, char in enumerate(word):
            if state[i][j] != char:
                h += 1
    return h


print(a_star())
