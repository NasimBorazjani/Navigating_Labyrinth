
import heapq


def initialize():
   # Define the initial state of the trampolines as a 2d tuple
   initial_state = ((1, 0, 1, 0, 0, 0, 0, 0, 0),
                   (1, 1, 0, 0, 1, 0, 0, 1, 1),
                   (0, 0, 0, 0, 0, 0, 0, 1, 1),
                   (0, 0, 1, 0, 0, 0, 1, 1, 0),
                   (1, 0, 0, 0, 1, 1, 0, 0, 1),
                   (0, 0, 0, 0, 1, 0, 0, 0, 0),
                   (1, 0, 0, 0, 1, 0, 0, 0, 1),
                   (0, 0, 1, 1, 1, 1, 1, 1, 0),
                   (1, 1, 0, 1, 0, 0, 1, 0, 0))
   num_rows = 9
   num_cols = 9
   start = (0, 7)
   goal = (7, 1)
   # The number of diagonal jumps required
   num_diagonal_jumps = 3


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, start, goal, num_diagonal_jumps, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, start, goal, num_diagonal_jumps, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if start == goal and g == num_diagonal_jumps:
           return actions


       # Generate all valid actions from the current state, which includes moving to any of the 8 adjacent trampolines
       for row_offset in range(-1, 2):
           for col_offset in range(-1, 2):
               # Check if the new position is within the grid and not the same as the current position
               new_row, new_col = start[0] + row_offset, start[1] + col_offset
               if 0 <= new_row < num_rows and 0 <= new_col < num_cols and (new_row, new_col) != start:
                   # Check if the new position is not broken
                   if state[new_row][new_col] == 0:
                       # Calculate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[start[0]][start[1]] = 1
                       new_state[new_row][new_col] = 0
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the number of jumps made, as we are trying to minimize the number of jumps
                       new_cost = g + 1
                      
                       # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The heuristic is the Manhattan distance between the current position and the goal, plus the number of diagonal jumps required
                           h = abs(new_row - goal[0]) + abs(new_col - goal[1]) + num_diagonal_jumps - g
                           heapq.heappush(queue, (new_cost + h, new_cost, actions + [(start[0], start[1])], new_state))
                          
                           # Update the start position
                           start = (new_row, new_col)
   return None


print(a_star())
