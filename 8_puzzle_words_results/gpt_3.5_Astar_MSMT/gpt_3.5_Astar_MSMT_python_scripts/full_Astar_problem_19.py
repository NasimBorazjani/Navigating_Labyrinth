
import heapq

def initialize():
    # Define the target words and the initial state of the board as a 2D list
    target_words = ['aeon', 'plier', 'gazon', 'ileum']
    initial_state = [['l', 'a', 'e', 'o', 'n'],
                     ['p', 'z', 'i', 'n', 'r'],
                     ['l', 'a', 'g', 'o', '_'],
                     ['i', 'e', 'e', 'u', 'm']]
    num_rows = len(initial_state)
    num_cols = len(initial_state[0])

    visited_costs = {}
    visited_costs[tuple(map(tuple, initial_state))] = 0

    queue = [(0, 0, [], initial_state)]

    return initial_state, target_words, num_rows, num_cols, visited_costs, queue

def a_star():
    initial_state, target_words, num_rows, num_cols, visited_costs, queue = initialize()

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Get the current position of the blank space
        blank_pos = [(i, j) for i in range(num_rows) for j in range(num_cols) if state[i][j] == '_'][0]

        # Check if we have reached the goal state where each row spells out a target word
        if all(''.join(row) == word for row, word in zip(state, target_words)):
            return actions

        # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighbors
        for d_row, d_col in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            new_row, new_col = blank_pos[0] + d_row, blank_pos[1] + d_col

            # Check if the new position for the blank space is within the bounds of the board
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                # Create a new state by swapping the blank space with the neighboring tile
                new_state = [list(row) for row in state]
                new_state[blank_pos[0]][blank_pos[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_pos[0]][blank_pos[1]]
                new_state = tuple(map(tuple, new_state))
                new_cost = g + 1

                # If the new state is unvisited or a lower cost path to reach it has been found, add it to the queue
                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + 1, new_cost, actions + [(d_row, d_col)], new_state))
    
    return None

print(a_star())
