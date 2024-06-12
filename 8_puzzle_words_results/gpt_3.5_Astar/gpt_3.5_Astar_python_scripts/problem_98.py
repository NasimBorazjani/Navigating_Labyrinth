
import heapq
import math


def a_star():
    # Define the target words and the initial state of the board
    target_words = ['rafty', 'lapped', 'angina', 'lanose', 'acnida']
    initial_state = [['a', 'r', 'o', 'f', 'n', 'y'],
                     ['l', 'g', 'p', 'p', 'e', 'a'],
                     ['a', 'n', 'n', 'i', '_', 'a'],
                     ['l', 't', 'n', 'd', 's', 'e'],
                     ['a', 'c', 'a', 'i', 'd', 'a']]
    num_rows = 5
    num_cols = 6

    visited_costs = {}
    visited_costs[str(initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        if is_goal_state(state, target_words):
            return actions

        # Find the position of the blank space in the current state
        blank_pos = find_blank_position(state)

        # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighbors
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
                    # Calculate the heuristic cost for the new state
                    h = heuristic(new_state, target_words)
                    heapq.heappush(queue, (g + h, new_cost, actions + [(d_row, d_col)], new_state))
    return None


def is_goal_state(state, target_words):
    # Check if the rows of the state spell out the target words
    for i, word in enumerate(target_words):
        if ''.join(state[i]) != word:
            return False
    return True


def find_blank_position(state):
    # Find the position of the blank space in the state
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == '_':
                return (i, j)
    return None


def heuristic(state, target_words):
    # The heuristic is the sum of the differences between the characters in the state and the target words
    h = 0
    for i, word in enumerate(target_words):
        for j in range(len(word)):
            if state[i][j] != word[j]:
                h += 1
    return h


print(a_star())