
import heapq


def initialize():
   # Define the initial state of the city map as a 2d tuple
   initial_state = (('6', '9', '19', 'x', '5', '9', 'x', '15', 'x'),
                   ('8', '10', '16', 'x', 'x', 'x', '5', '11', '4'),
                   ('5', '11', '20', '1', '14', '16', '7', '1', '5'),
                   ('10', '5', '3', '5', '12', '8', 'x', 'x', '2'),
                   ('16', '15', '15', '14', 'x', '13', '10', 'x', '10'),
                   ('6', '4', '7', '13', 'x', 'x', 'x', 'x', '13'),
                   ('x', '1', '6', '3', 'x', 'x', '17', '9', '5'),
                   ('x', '11', 'x', '9', 'x', 'x', 'x', 'x', 'x'),
                   ('x', 'x', 'x', '18', 'x', '2', 'x', 'x', '12'))
   num_rows = 9
   num_cols = 9
   # Define the districts and their row ranges
   districts = [(0, 1), (2, 4), (5, 8)]
   # Define the start and end positions
   start = (1, 8)
   end = (4, 0)


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, districts, start, end, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, districts, start, end, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if (start, end) in actions:
           return actions


       # Generate all possible actions from the current state, which includes moving to a neighboring workshop in a valid direction
       for row_diff in [-1, 0, 1]:
           for col_diff in [-1, 0, 1]:
               # Check if the new state would be valid, ie the move is within the grid and the destination is not a closed workshop
               if (row_diff != 0 or col_diff != 0) and 0 <= start[0] + row_diff < num_rows and 0 <= start[1] + col_diff < num_cols and state[start[0] + row_diff][start[1] + col_diff] != 'x':
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   new_state[start[0]][start[1]] = 'x'
                   new_state[start[0] + row_diff][start[1] + col_diff] = '1'
                   new_state = tuple(tuple(row) for row in new_state)
                   # The cost so far is the number of moves made, as the task is to minimize the number of moves required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, end), new_cost, actions + [(start[0] + row_diff, start[1] + col_diff)], new_state))
                  
   return None


def heuristic(state, end):
   # An admissible and consistent heuristic for this problem is the Manhattan distance from the current position to the end position
   # This heuristic is admissible because it never overestimates the cost to reach the goal, as each move is either horizontal or vertical
   # It is consistent because moving to a neighboring workshop increases the heuristic cost of the successor node by a max of 1 (if the moved workshop is not in the same district as the current workshop), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = abs(start[0] - end[0]) + abs(start[1] - end[1])
   return h


print(a_star())
