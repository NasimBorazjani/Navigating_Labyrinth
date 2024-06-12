
import heapq


def initialize():
    # Define the initial state of the puzzle as a 2d tuple
    initial_state = (('46', '50', '97'),
                     ('92', '49', '99'),
                     ('91', '25', '_'))
    num_rows = 3
    num_cols = 3

    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]
   
    return initial_state, num_rows, num_cols, visited_costs, queue
  
def a_star():
  
    initial_state, num_rows, num_cols, visited_costs, queue = initialize()


    while queue:
        _, g, actions, state = heapq.heappop(queue)


        # If the current state is the goal state, return the actions taken
        if state == (('9', '8', '7'),
                     ('6', '5', '4'),
                     ('3', '2', '_')):
            return actions


        # Generate all possible actions from the current state, which includes swapping the empty spot with any of the 8 neighboring tiles
        for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            new_row, new_col = state.index('_') // num_cols + d_row, state.index('_') % num_cols + d_col
            # Check if the new state is valid, ie the new spot is within the bounds of the grid
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                # Generate the new state
                new_state = list(state)[:]
                new_state[new_row * num_cols + new_col], new_state[state.index('_')] = new_state[state.index('_')], new_state[new_row * num_cols + new_col]
                new_state = tuple(tuple(new_state[i:i + num_cols]) for i in range(0, len(new_state), num_cols))
                # The cost of the new state is the number of actions taken, as the task is to minimize the number of actions required to solve the puzzle
                new_cost = g + 1


                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # The heuristic function is not needed in this problem as the goal state is always the same, and the shortest path to it is unique
                    heapq.heappush(queue, (new_cost, new_cost, actions + [new_state[new_row][new_col]], new_state))
    return None


print(a_star())
