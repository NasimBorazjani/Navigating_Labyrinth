
import heapq


def a_star():
   # Define the initial state and the goal state of the problem, represented as tuples
   initial_state = (2, 12)
   goal_state = (10, 1)
   # Define the map of the park
   park_map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1],
               [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
               [0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0],
               [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
               [0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1],
               [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
               [0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0],
               [1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0],
               [1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
               [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
               [1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1]]
   num_rows = len(park_map)
   num_cols = len(park_map[0])


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state, 0)]


   while queue:
       _, g, actions, state, num_diagonal_jumps = heapq.heappop(queue)


       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes jumping to any of the 8 adjacent trampolines
       for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
           new_row, new_col = state[0] + d_row, state[1] + d_col
           # Check if the new state would be valid, ie the new position must be within the bounds of the park and the trampoline at the new position must not be broken
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and park_map[new_row][new_col] == 0:
               # Generate the new state
               new_state = (new_row, new_col)
               # The cost so far is the number of jumps made, as the task is to minimize the number of jumps required to reach the goal state
               new_cost = g + 1
               # If the jump was diagonal, increment the count of diagonal jumps
               new_num_diagonal_jumps = num_diagonal_jumps + 1 if abs(d_row) == abs(d_col) else num_diagonal_jumps
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The heuristic is the Manhattan distance from the current state to the goal state
                   h = abs(new_row - goal_state[0]) + abs(new_col - goal_state[1])
                   # If the number of diagonal jumps is less than 4, add 4 - num_diagonal_jumps to the heuristic, as we must make at least 4 diagonal jumps
                   if new_num_diagonal_jumps < 4:
                       h += 4 - new_num_diagonal_jumps
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_state], new_state, new_num_diagonal_jumps))
   return None


print(a_star())
