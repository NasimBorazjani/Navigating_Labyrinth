
import heapq


def initialize():
   # Define the initial state of the matrix as a 2d tuple
   initial_state = (('x', 15, 'x', 18, 8, 6, 11, 'x', 7),
                   (9, 10, 18, 9, 2, 16, 9, 8, 'x'),
                   (14, 'x', 'x', 10, 18, 'x', 13, 12, 14),
                   (11, 18, 4, 11, 14, 2, 20, 'x', 15),
                   (12, 'x', 'x', 8, 10, 'x', 'x', 10, 11),
                   (5, 19, 20, 15, 11, 'x', 14, 'x', 18),
                   ('x', 5, 'x', 'x', 'x', 'x', 9, 'x'),
                   ('x', 'x', 18, 'x', 'x', 4, 'x', 17, 13),
                   ('x', 7, 17, 'x', 'x', 'x', 'x', 7, 19))
   num_rows = 9
   num_cols = 9
   # The start and end positions of Ben
   start_pos = (3, 0)
   end_pos = (4, 8)
   # The districts and their row ranges
   districts = [(0, 2), (3, 4), (5, 8)]


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], start_pos)]
  
   return initial_state, num_rows, num_cols, start_pos, end_pos, districts, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, start_pos, end_pos, districts, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == end_pos:
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring cells
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_pos = (state[0] + d_row, state[1] + d_col)
           # Check if the new position is valid, ie within the bounds of the matrix and not an x
           if (0 <= new_pos[0] < num_rows and 0 <= new_pos[1] < num_cols and initial_state[new_pos[0]][new_pos[1]] != 'x' and
               # The new position must be in a district different from the current position
               any(start <= new_pos[0] <= end for start, end in districts if start != state[0] // 3 * 3 <= new_pos[0] <= end)):
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required
               new_cost = g + initial_state[new_pos[0]][new_pos[1]]
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_pos not in visited_costs or new_cost < visited_costs[new_pos]:
                   visited_costs[new_pos] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_pos, end_pos), new_cost, actions + [new_pos], new_pos))
                  
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the Manhattan distance between the current state and the goal state
   # This heuristic is admissible because it never overestimates the cost to reach the goal
   # It is consistent because moving to a neighboring cell increases the heuristic cost of the successor node by a max of 1 (if the moved cell is in a different district), which is equal to the cost of reaching the successor node
   return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
