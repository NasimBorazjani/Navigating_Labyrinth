
import heapq
import math


def a_star():
    # Define the target words and the initial state of the board
    target_words = ['twi', 'ovey', 'udic', 'diem']
    initial_state = [['v', 't', 'u', 'i'], ['o', 'w', 'e', 'i'], ['y', 'd', '_', 'c'], ['d', 'i', 'e', 'm']]
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

        # Find the position of the blank space in the current state
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
                    heapq.heappush(queue, (g + heuristic(new_state, target_words), new_cost, actions + [(d_row, d_col)], new_state))
    return None


def is_goal_state(state, target_words):
    # Check if the rows of the state spell out the target words
    for i in range(len(target_words)):
        if ''.join(state[i]) != target_words[i]:
            return False
    return True


def find_blank_position(state):
    # Find the position of the blank space in the state
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == '_':
                return (i, j)
    return None


def heuristic(state, target_words):
    # An admissible and consistent heuristic for this problem is the count of characters that are not in the correct position in each row
    # This heuristic relaxes the constraint that only the blank space can be moved
    # It is admissible because it never overestimates the cost to reach the goal, as each misplaced character must be moved at least once
    # It's consistent because moving a character from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved character is in the correct position in the new row but not in the old one), which is equal to the cost of reaching the successor node
    # Thus h(n) is always less than or equal to c(n, n’)(equal to 1) + h(n’)
    # And the cost of the goal state is 0, as all rows will spell out the target words
    h = 0
    for i in range(len(target_words)):
        for j in range(len(state[i])):
            if state[i][j] != target_words[i][j]:
                h += 1
    return h


print(a_star())
