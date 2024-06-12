
import heapq


def initialize():
   # Define the initial state of the city map as a 2d tuple
   initial_state = (('10', '14', '4', '16', 'x', '17', '5', 'x', 'x'),
                   ('5', '20', '16', '3', '1', '8', 'x', '16', '19'),
                   ('1', 'x', '5', '13', '3', '15', '19', '15', 'x'),
                   ('x', '16', '13', '20', 'x', '8', 'x', 'x', 'x'),
                   ('x', '16', 'x', '17', '11', '1', 'x', '15', 'x'),
                   ('10', 'x', '14', '11', '5', '7', '12', 'x', '5'),
                   ('7', 'x', '15', 'x', '15', '8', '3', '6', '7'),
                   ('x', '12', '14', 'x', 'x', 'x', '16', '3', '13'),
                   ('19', '5', '10', 'x', 'x', 'x', '9', '7', '14'))
   num_rows = 9
   num_cols = 9
   start = (7, 7)
   end = (1, 2)
   districts = [(0, 1), (2, 6), (7, 8)]


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
           # Check if the new position is valid, ie within the bounds of the city map and not a closed workshop
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and state[new_row][new_col] != 'x':
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               number_to_be_moved = new_state[new_row][new_col]
               # Do the move
               new_state[start[0]][start[1]], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[start[0]][start[1]]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of moves made, as our objective is to minimize the number of moves required to reach the goal workshop
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, end, districts), new_cost, actions + [(start, (new_row, new_col), number_to_be_moved)], new_state))
                  
   return None


def heuristic(state, end, districts):
   # An admissible and consistent heuristic is the sum of the Manhattan distances (the shortest path) of each workshop from its goal position
   # The heuristic relaxes the constraint that a workshop can only be moved to a neighboring workshop
   # Thus the heuristic reports a lower estimate on the cost to reach goal workshop and is admissible
   # The heuristic is consistent because the cost of moving a workshop to a neighboring workshop is always 1, which is exactly the decrease in the Manhattan distance, if the workshop is moved toward its goal position, otherwise the estimated cost of the successor node is the same or higher, and he heuristic estimate for the goal state is 0, as the distance of each workshop from its goal position would be 0 in the goal state.
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           # Can't compare integers with "x" when finding the goal position of each workshop, thus ignore the "x" workshops
           if state[i][j] != 'x':
               # Get goal position of each workshop
               goal_row, goal_col = [(x, y) for x in range(len(state)) for y in range(len(state[x])) if state[x][y] == state[i][j]][0]
               # Add the the Manhattan distance of the current and goal coordinates of the workshop to the estimate
               h += abs(i - goal_row) + abs(j - goal_col)
   return h


print(a_star())
