
import heapq
import math


def a_star():
    # Define the target words and the initial state of the board
    target_words = ['hay', 'werf', 'rudd', 'frib']
    initial_state = [['e', 'h', 'r', 'y'], ['w', 'f', 'r', 'r'], ['_', 'u', 'd', 'd'], ['f', 'a', 'i', 'b']]
    num_rows = 4
    num_cols = 4

    visited_costs = {}
    visited_costs[str(initial_state)] = 0

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

            # Check if the new position is valid
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                new_state = [list(row) for row in state]
                new_state[new_row][new_col], new_state[find_blank_space(state)[0]][find_blank_space(state)[1]] = new_state[find_blank_space(state)[0]][find_blank_space(state)[1]], new_state[new_row][new_col]
                new_state_str = str(new_state)
                new_cost = g + 1

                if new_state_str not in visited_costs or new_cost < visited_costs[new_state_str]:
                    visited_costs[new_state_str] = new_cost
                    h = heuristic(new_state, target_words)
                    heapq.heappush(queue, (g + h, new_cost, actions + [(new_row, new_col)], new_state))

    return None


def is_goal_state(state, target_words):
    # Check if the current state matches the target words
    for i in range(len(target_words)):
        if ''.join(state[i]) != target_words[i]:
            return False
    return True


def find_blank_space(state):
    # Find the position of the blank space in the state
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == '_':
                return i, j
    return -1, -1


def heuristic(state, target_words):
    # Calculate the heuristic as the sum of the differences between the characters in the state and the target words
    h = 0
    for i in range(len(target_words)):
        for j in range(len(target_words[i])):
            if state[i][j] != target_words[i][j]:
                h += 1
    return h


print(a_star())
