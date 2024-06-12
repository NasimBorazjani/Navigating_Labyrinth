
import heapq


def initialize():
   # Define the initial state of the city as a 2d tuple
   initial_state = (('x', 'x', 'x', 'x', '13', 'x', 'x', '3', '8'),
                   ('x', '18', '19', '19', '2', '9', 'x', 'x', 'x'),
                   ('15', 'x', '6', 'x', 'x', 'x', '13', '13', '4'),
                   ('7', 'x', '4', '10', 'x', '11', '10', '17', 'x'),
                   ('2', '7', 'x', 'x', '8', '16', '4', '1', '4'),
                   ('x', 'x', 'x', '5', '16', '15', 'x', '17', '10'),
                   ('x', 'x', 'x', '5', '14', '9', '3', '15', 'x'),
                   ('x', '6', '4', 'x', 'x', 'x', '18', 'x', 'x'),
                   ('17', 'x', '19', 'x', '1', '4', '8', 'x', '8'))
   num_rows = 9
   num_cols = 9
   start = (2, 8)
   end = (6, 3)
   districts = [(0, 2), (3, 5), (6, 8)]


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, start, end, districts, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, start, end, districts, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if start == end:
           return actions


       # Generate all possible actions from the current state, which includes moving to a neighboring workshop in a valid direction
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = start[0] + d_row, start[1] + d_col
           # Check if the new position is valid, ie within the bounds of the city and not a closed workshop
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and state[new_row][new_col] != 'x':
               # The actions is valid, generate the new state
               new_state = [list(row[:]) for row in state]
               number_to_be_moved = new_state[new_row][new_col]
               # Do the move
               new_state[start[0]][start[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[start[0]][start[1]]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of moves made, as our objective is to minimize the number of moves required to reach the goal workshop
               new_cost = g + int(number_to_be_moved)
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, end, districts), new_cost, actions + [(start[0], start[1], new_row, new_col)], new_state))
                  
   return None


def heuristic(state, end, districts):
   # An admissible and consistent heuristic is the sum of the Manhattan distances (the shortest path) of each district from the current state to the end state
   # The heuristic relaxes the constraint that a district must be visited in order
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the cost of moving a district to a neighboring district is always 1, which is exactly the decrease in the Manhattan distance, if the district is moved toward the end state, otherwise the estimated cost of the successor node is the same or higher, and he heuristic estimate for the goal state is 0, as the distance of each district from the end state would be 0 in the goal state.
   h = 0
   for district in districts:
       # Get the coordinates of the workshops in the district
       district_workshops = [(i, j) for i in range(district[0], district[1] + 1) for j in range(num_cols) if state[i][j] != 'x']
       # Add the the Manhattan distance of the current and end coordinates of the district to the estimate
       h += min(abs(i - end[0]) + abs(j - end[1]) for i, j in district_workshops)
   return h


print(a_star())
