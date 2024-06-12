
import heapq
import math


def a_star():
    # Define the target words and the initial state of the board
    target_words = ['codo', 'snook', 'jeans', 'boral', 'funky', 'payed']
    initial_state = [['n', 'c', 'a', 'd', 'o'], ['s', 'n', 'o', 'o', 'k'], ['y', 'e', 'o', 'n', '_'], ['b', 'j', 'r', 'o', 'l'], ['f', 'u', 'a', 'k', 'a'], ['p', 'e', 'y', 's', 'd']]
    num_rows = 6
    num_cols = 5

    visited_costs = {}
    visited_costs[str(initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        if is_goal_state(state, target_words):
            return actions

        # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighboring tiles
        for i in range(num_rows):
            for j in range(num_cols):
                if state[i][j] == '_':
                    for d_row, d_col in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                        new_row, new_col = i + d_row, j + d_col
                        if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                            new_state = [list(row) for row in state]
                            new_state[i][j], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[i][j]
                            new_state_str = str(new_state)
                            new_cost = g + 1

                            if new_state_str not in visited_costs or new_cost < visited_costs[new_state_str]:
                                visited_costs[new_state_str] = new_cost
                                h = heuristic(new_state, target_words)
                                heapq.heappush(queue, (g + h, new_cost, actions + [(i, j, new_row, new_col)], new_state))
    return None


def is_goal_state(state, target_words):
    # Check if the current state matches the target words
    for i in range(len(target_words)):
        if ''.join(state[i]) != target_words[i]:
            return False
    return True


def heuristic(state, target_words):
    # The heuristic is the sum of the differences between the current state and the target words
    h = 0
    for i in range(len(target_words)):
        for j in range(len(target_words[i])):
            if state[i][j] != target_words[i][j]:
                h += 1
    return h


print(a_star())
