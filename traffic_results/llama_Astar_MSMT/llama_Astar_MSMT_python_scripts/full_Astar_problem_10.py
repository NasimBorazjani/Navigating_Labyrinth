
import heapq


def initialize():
   # Define the initial state of the city as a 2d tuple
   initial_state = (('x', 'x', 6, 'x', 7, 9, 4, 11),
                   ('x', 3, 'x', 6, 5, 3, 15, 'x', 3),
                   ('x', 'x', 'x', 4, 'x', 9, 1, 8, 'x'),
                   (15, 18, 1, 6, 5, 10, 6, 14, 8),
                   (18, 10, 7, 18, 2, 'x', 'x', 'x', 7),
                   (11, 9, 16, 'x', 11, 'x', 11, 'x', 17),
                   (7, 'x', 18, 'x', 8, 10, 20, 6, 'x'),
                   (15, 4, 17, 'x', 16, 2, 12, 16, 'x'),
                   (9, 10, 18, 17, 9, 6, 7, 'x', 15))
   num_rows = 9
   num_cols = 8
   start_pos = (3, 0)
   end_pos = (6, 6)
   districts = [(0, 3), (4, 6), (7, 8)]


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, start_pos, end_pos, districts, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, start_pos, end_pos, districts, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if start_pos == end_pos and all(any(start_pos[0] <= row <= end_pos[0] and row_start <= start_pos[1] <= row_end for row_start, row_end in districts) for row in range(num_rows)):
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops if it's not an 'x' and it's in a different district
       for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
           new_pos = (start_pos[0] + d_row, start_pos[1] + d_col)
           if (0 <= new_pos[0] < num_rows and 0 <= new_pos[1] < num_cols and
               state[new_pos[0]][new_pos[1]] != 'x' and
               any(start_pos[0] <= row <= new_pos[0] and row_start <= start_pos[1] <= row_end for row_start, row_end in districts) and
               any(row_start <= new_pos[0] <= row_end and start_pos[1] <= col <= new_pos[1] for row_start, row_end in districts)):
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               number_to_be_moved = new_state[start_pos[0]][start_pos[1]]
               new_state[start_pos[0]][start_pos[1]] = 'x'
               new_state[new_pos[0]][new_pos[1]] = number_to_be_moved
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of moves made, as our objective is to minimize the number of moves required
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, end_pos, districts), new_cost, actions + [(start_pos, new_pos)], new_state))
                  
   return None


def heuristic(state, end_pos, districts):
   # An admissible and consistent heuristic is the sum of the Manhattan distances (the shortest path) of each workshop from its goal position
   # The heuristic relaxes the constraint that a workshop can only be moved to a neighboring workshop in a different district
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving a workshop to a neighboring workshop is always 1, which is exactly the decrease in the Manhattan distance, if the workshop is moved toward its goal position, otherwise the estimated cost of the successor node is the same or higher, and he heuristic estimate for the goal state is 0, as the distance of each workshop from its goal position would be 0 in the goal state.
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           # Can't compare integers with "x" when finding the goal position of each workshop
           if state[i][j] != 'x':
               # Get goal position of each workshop
               goal_row, goal_col = [(x, y) for x in range(len(state)) for y in range(len(state[x])) if state[x][y] == state[i][j]][0]
               # Add the the Manhattan distance of the current and goal coordinates of the workshop to the estimate
               h += abs(i - goal_row) + abs(j - goal_col)
   return h


print(a_star())
