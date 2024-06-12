
import heapq


def initialize():
   # Define the initial state of the matrix map
   initial_state = (('4', '13', 'x', '9', 'x', 'x', 'x', 'x', 'x'),
                   ('1', '11', 'x', '16', '5', '7', '12', '16', 'x'),
                   ('12', '11', 'x', '14', 'x', 'x', '12', 'x', '3'),
                   ('9', '11', 'x', '9', '10', 'x', 'x', 'x', 'x'),
                   ('20', '2', 'x', '1', '16', '12', '18', '17', '10'),
                   ('10', '13', '4', '15', '13', '2', '20', '3', '15'),
                   ('x', '6', '13', '1', '8', '20', '14', '11', '3'),
                   ('14', 'x', '9', 'x', 'x', '13', '19', '10', 'x'),
                   ('12', 'x', '18', '1', 'x', 'x', '9', 'x', 'x'))
   num_rows = 9
   num_cols = 9
   # The start and end positions of Ben
   start_pos = (3, 1)
   end_pos = (5, 8)
   # The districts in the city
   districts = [(0, 2), (3, 4), (5, 8)]


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


       # Generate all possible actions from the current state, which includes moving Ben to a neighboring workshop
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_pos = (start_pos[0] + d_row, start_pos[1] + d_col)
           # Check if the new position is valid, ie within the bounds of the matrix map and not a closed workshop
           if (0 <= new_pos[0] < num_rows and 0 <= new_pos[1] < num_cols and state[new_pos[0]][new_pos[1]] != 'x'):
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[start_pos[0]][start_pos[1]] = 'x'
               new_state[new_pos[0]][new_pos[1]] = 'B'
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, end_pos, districts), new_cost, actions + [new_pos], new_state))
                  
   return None


def heuristic(state, end_pos, districts):
   # An admissible and consistent heuristic is the sum of the Manhattan distances (the shortest path) of Ben to the end position and the number of districts not visited
   # This heuristic relaxes the constraint that Ben can only move to a neighboring workshop
   # It is admissible as it never overestimates the cost to reach the goal, as each move of Ben is a decrease in the Manhattan distance
   # It's consistent because moving Ben to a neighboring workshop reduces the heuristic cost of the successor node by a max of 1 (if the moved workshop is in a different district), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for row in range(len(state)):
       for col in range(len(state[row])):
           if state[row][col] == 'B':
               h += abs(row - end_pos[0]) + abs(col - end_pos[1])
   for district in districts:
       if not any(district[0] <= row <= district[1] for row in range(num_rows) for col in range(num_cols) if state[row][col] == 'B'):
           h += 1
   return h


print(a_star())
