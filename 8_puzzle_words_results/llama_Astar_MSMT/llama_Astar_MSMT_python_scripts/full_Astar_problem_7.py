
import heapq


def initialize():
    # Define the initial state of the board
    initial_state = [['u', 'c', 'r', 'y'], ['d', 'n', 'n', 'r'], ['_', 'u', 'm', 'p'], ['k', 'e', 'e', 'e']]
    target_words = ['cry', 'dune', 'rump', 'knee']
    num_rows = 4
    num_cols = 4

    visited_costs = {}
    visited_costs[tuple(row[:] for row in initial_state)] = 0

    queue = [(0, 0, [], initial_state)]
   
    return initial_state, target_words, num_rows, num_cols, visited_costs, queue
  
def a_star():
  
    initial_state, target_words, num_rows, num_cols, visited_costs, queue = initialize()


    while queue:
        _, g, actions, state = heapq.heappop(queue)


        # If the current state is the goal state
        if state == [list(word) for word in target_words]:
            return actions


        # Generate all possible actions from the current state
        for row in range(num_rows):
            for col in range(num_cols):
                # Check if moving the blank tile in any of the 4 diagonal directions results in a valid state
                for new_row, new_col in [(row - 1, col - 1), (row - 1, col + 1), (row + 1, col - 1), (row + 1, col + 1)]:
                    if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                        temp_state = [list(row[:]) for row in state]
                        temp_state[row][col], temp_state[new_row][new_col] = temp_state[new_row][new_col], temp_state[row][col]
                        # Generate the new state
                        new_state = tuple(tuple(row) for row in temp_state)
                        # The cost so far is the number of actions taken
                        new_cost = g + 1


                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            # The heuristic function is not needed in this problem as the goal state is always reachable and the cost of reaching the goal state is always the same, thus the cost of reaching the goal state is the cost of reaching the current state
                            heapq.heappush(queue, (new_cost + 1, new_cost, actions + [(row, col, new_row, new_col)], new_state))
   return None


print(a_star())
