
import heapq
import copy


def a_star():
    # Define the initial state of the board and the target words
    initial_state = [['o', 's', '_', 'n'], ['k', 'i', 'r', 'i'], ['n', 'u', 'b', 'o'], ['u', 'f', 'a', 'l']]
    target_words = ['sin', 'kori', 'bufo', 'unal']
    num_rows = 4
    num_cols = 4

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

        # Generate all possible actions from the current state, which includes swapping the blank space with its diagonal neighbors
        for d_row, d_col in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            new_row, new_col = blank_pos[0] + d_row, blank_pos[1] + d_col
            # Check if the new position is within the bounds of the board
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                # Create a new state by swapping the blank space with the diagonal neighbor
                new_state = copy.deepcopy(state)
                new_state[blank_pos[0]][blank_pos[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_pos[0]][blank_pos[1]]
                new_state_str = str(new_state)
                # Calculate the cost of the new state
                new_cost = g + 1

                if new_state_str not in visited_costs or new_cost < visited_costs[new_state_str]:
                    visited_costs[new_state_str] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state, target_words), new_cost, actions + [(d_row, d_col)], new_state))
    return None


def check_target_words(state, target_words):
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
    # The heuristic is the sum of the number of characters that are not in the correct position in each row
    h = 0
    for i in range(len(target_words)):
        for j in range(len(target_words[i])):
            if state[i][j] != target_words[i][j]:
                h += 1
    return h


print(a_star())
