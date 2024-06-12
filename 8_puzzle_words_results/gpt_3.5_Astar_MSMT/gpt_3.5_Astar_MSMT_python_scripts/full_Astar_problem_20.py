
import heapq

def initialize():
    # Define the initial state of the board as a 2D list of characters
    initial_state = [['r', 's', 'w', 'o', 'g'], ['t', 'n', 'e', 'm', 'a'], ['m', 'o', '_', 'u', 's'], ['a', 'w', 'i', 'r', 'i']]
    num_rows = len(initial_state)
    num_cols = len(initial_state[0])
    target_words = ['snog', 'trema', 'mosur', 'awiwi']

    visited_costs = {}
    visited_costs[str(initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    return initial_state, num_rows, num_cols, target_words, visited_costs, queue

def a_star():
  
    initial_state, num_rows, num_cols, target_words, visited_costs, queue = initialize()

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Convert the state to a string to check if it matches the target words
        state_str = str(state)
        if all(''.join(row) == target_words[i] for i, row in enumerate(state)):
            return actions

        # Find the position of the blank space ('_')
        blank_row, blank_col = [(i, j) for i in range(num_rows) for j in range(num_cols) if state[i][j] == '_'][0]

        # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighboring tiles
        for d_row, d_col in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            new_row, new_col = blank_row + d_row, blank_col + d_col
            # Check if the new position is within the bounds of the board
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                # Perform the swap action by creating a new state with the blank space swapped with the neighboring tile
                new_state = [list(row) for row in state]
                new_state[blank_row][blank_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_row][blank_col]

                # Encode the new state as a string for dictionary lookup
                new_state_str = str(new_state)
                new_cost = g + 1

                if new_state_str not in visited_costs or new_cost < visited_costs[new_state_str]:
                    visited_costs[new_state_str] = new_cost
                    heapq.heappush(queue, (g + 1, new_cost, actions + [(d_row, d_col)], new_state))

    return None

print(a_star())
