
import heapq
import math


def a_star():
    # Define the initial state of the board as a 2d tuple
    initial_state = (('_', 'd', 'a', 'u', 'n', 'k'),
                     ('a', 'r', 'm', 'r', 'r', 'e'),
                     ('d', 'i', 'u', 'l', 'l', 't'),
                     ('c', 'd', 'u', 'r', 'a', 'c'),
                     ('m', 'i', 'g', 'a', 'o', 'h'))
    target_words = ['drunk', 'armure', 'diglot', 'caudal', 'mirach']
    num_rows = 5
    num_cols = 6

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # If the current state matches the target words, return the actions taken
        if is_target_state(state, target_words):
            return actions

        # Find the position of the blank space in the current state
        blank_pos = find_blank_position(state)

        # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighbors
        for d_row, d_col in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            new_row, new_col = blank_pos[0] + d_row, blank_pos[1] + d_col
            # Check if the new position is within the bounds of the board
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                # Generate the new state by swapping the blank space with the neighboring tile
                new_state = swap_tiles(state, blank_pos, (new_row, new_col))
                new_cost = g + 1

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # Calculate the heuristic cost based on the number of misplaced characters in each row
                    h = heuristic(new_state, target_words)
                    heapq.heappush(queue, (g + h, new_cost, actions + [(d_row, d_col)], new_state))

    return None


def is_target_state(state, target_words):
    # Check if the current state matches the target words
    for i, word in enumerate(target_words):
        if ''.join(state[i]).replace('_', '') != word:
            return False
    return True


def find_blank_position(state):
    # Find the position of the blank space in the current state
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == '_':
                return (i, j)
    return None


def swap_tiles(state, pos1, pos2):
    # Swap the positions of two tiles in the state
    new_state = [list(row) for row in state]
    new_state[pos1[0]][pos1[1]], new_state[pos2[0]][pos2[1]] = new_state[pos2[0]][pos2[1]], new_state[pos1[0]][pos1[1]]
    return tuple(tuple(row) for row in new_state)


def heuristic(state, target_words):
    # Calculate the heuristic cost based on the number of misplaced characters in each row
    h = 0
    for i, word in enumerate(target_words):
        for j in range(len(state[0])):
            if state[i][j] != '_' and state[i][j] != word[j]:
                h += 1
    return h


print(a_star())
