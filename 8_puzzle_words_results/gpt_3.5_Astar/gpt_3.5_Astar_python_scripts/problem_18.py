
import heapq
import math


def a_star():
    # Define the initial state of the board as a 2d tuple
    initial_state = (('o', 'm', 'y', 'i'), ('g', 'd', 'o', 'e'), ('_', 'o', 'b', 'd'), ('p', 'o', 'c', 'k'))
    target_words = ['moi', 'good', 'boyd', 'peck']
    num_rows = 4
    num_cols = 4

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        if is_goal_state(state, target_words):
            return actions

        # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighbors
        for d_row, d_col in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            new_row, new_col = find_blank_space(state)
            new_row += d_row
            new_col += d_col

            # Check if the new coordinate is valid
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                # Generate the new state
                new_state = [list(row[:]) for row in state]
                new_state[new_row][new_col], new_state[find_blank_space(state)[0]][find_blank_space(state)[1]] = new_state[find_blank_space(state)[0]][find_blank_space(state)[1]], new_state[new_row][new_col]
                new_state = tuple(tuple(row) for row in new_state)
                # The cost of each action is 1
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


def find_blank_space(state):
    # Find the coordinates of the blank space in the state
    for i, row in enumerate(state):
        for j, char in enumerate(row):
            if char == '_':
                return i, j
    return -1, -1


def heuristic(state, target_words):
    # The heuristic is the sum of the differences between the current state and the target words
    h = 0
    for i, word in enumerate(target_words):
        for j, char in enumerate(word):
            if state[i][j] != char:
                h += 1
    return h


print(a_star())
