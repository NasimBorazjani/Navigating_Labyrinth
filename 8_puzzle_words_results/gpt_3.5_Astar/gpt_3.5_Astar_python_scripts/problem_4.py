
import heapq
import math


def a_star():
    # Define the target words and the initial state of the board
    target_words = ['map', 'cere', 'drub', 'velo']
    initial_state = [['_', 'm', 'u', 'p'], ['c', 'e', 'r', 'a'], ['d', 'r', 'e', 'b'], ['v', 'e', 'l', 'o']]
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

            # Check if the new coordinate is valid
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                # Generate the new state by swapping the blank space with the neighboring tile
                new_state = [list(row) for row in state]
                new_state[new_row][new_col], new_state[find_blank_space(state)[0]][find_blank_space(state)[1]] = new_state[find_blank_space(state)[0]][find_blank_space(state)[1]], new_state[new_row][new_col]
                new_state = str(new_state)
                # The cost of the new state is the number of swaps made, as the task is to minimize the number of swaps required
                new_cost = g + 1

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    h = heuristic(new_state, target_words)
                    heapq.heappush(queue, (g + h, new_cost, actions + [(new_row, new_col)], eval(new_state)))
    return None


def is_goal_state(state, target_words):
    # Check if the current state matches the target words
    for i in range(len(target_words)):
        if ''.join(state[i]) != target_words[i]:
            return False
    return True


def find_blank_space(state):
    # Find the coordinates of the blank space in the current state
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == '_':
                return i, j
    return -1, -1


def heuristic(state, target_words):
    # An admissible and consistent heuristic for this problem is the count of characters that are not in the correct position in each row
    # This heuristic relaxes the constraint that only the blank space can be moved
    # It is admissible because it never overestimates the cost to reach the goal, as each character that is not in the correct position must be moved at least once
    # It's consistent because moving a character from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved character is in the correct position in the new row but not in the old one), which is equal to the cost of reaching the successor node
    # Thus h(n) is always less than or equal to c(n, n’)(equal to 1) + h(n’)
    # And the cost of the goal state is 0, as all rows will match the target words
    h = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != target_words[i][j]:
                h += 1
    return h


print(a_star())
