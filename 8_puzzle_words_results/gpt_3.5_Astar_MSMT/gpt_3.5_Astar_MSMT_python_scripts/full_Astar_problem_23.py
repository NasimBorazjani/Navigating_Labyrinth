
import heapq

def initialize():
    # Define the target words and the initial state of the board as a 2D tuple
    target_words = ['song', 'amish', 'hiper', 'agley']
    initial_state = (('m', 's', '_', 'n', 'g'),
                     ('a', 'o', 'i', 'e', 'h'),
                     ('h', 'i', 'p', 'e', 's'),
                     ('a', 'g', 'l', 'r', 'y'))
    num_rows = len(initial_state)
    num_cols = len(initial_state[0])

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = []
    # No actions taken in the initial state
    heapq.heappush(queue, (0, 0, [], initial_state))
  
    return initial_state, num_rows, num_cols, target_words, visited_costs, queue

def a_star():
    initial_state, num_rows, num_cols, target_words, visited_costs, queue = initialize()

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state matches the goal state, where each row spells out the corresponding word in the list of target words
        if all(''.join(row) == word for row, word in zip(state, target_words)):
            return actions

        # Find the position of the blank space
        blank_pos = [(i, row.index('_')) for i, row in enumerate(state) if '_' in row][0]

        # Generate all possible actions from the current state, which includes swapping the blank space with any of its 4 diagonal neighboring tiles
        for d_row, d_col in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
            new_row, new_col = blank_pos[0] + d_row, blank_pos[1] + d_col

            # Check if the new coordinate is within the bounds of the board
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                # Generate the new state by performing the swap
                new_state = [list(row[:]) for row in state]
                new_state[blank_pos[0]][blank_pos[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_pos[0]][blank_pos[1]]
                new_state = tuple(tuple(row) for row in new_state)
                # The cost of reaching the new state is the number of swaps performed so far
                new_cost = g + 1

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + 1, new_cost, actions + [(d_row, d_col)], new_state))

    return None

print(a_star())
