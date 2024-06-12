
import heapq


def initialize():
   # Define the initial state of the city map as a 2d tuple
   initial_state = (('13', 'x', 'x', '3', '10', '20', '3', 'x', '5'),
                   ('x', 'x', 'x', 'x', '20', '16', 'x', 'x', '17'),
                   ('3', '14', '18', '8', '1', '20', '14', 'x', '7'),
                   ('13', '3', '6', '10', '7', '4', '6', '6', '1'),
                   ('10', '12', '2', 'x', '11', 'x', '10', '8', '11'),
                   ('x', 'x', 'x', '11', '6', '18', '13', '20', '17'),
                   ('x', 'x', '16', 'x', '4', '17', '7', '10', '15'),
                   ('x', '7', '16', '6', '19', '4', '7', 'x', 'x'),
                   ('x', '11', '18', 'x', 'x', 'x', '3', '8', 'x'))
   num_rows = 9
   num_cols = 9
   start_pos = (5, 7)
   end_pos = (2, 1)
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
       if start_pos == end_pos and all(any(start_pos[0] >= district[0] and start_pos[0] <= district[1] for district in districts) for start_pos in actions):
           return actions


       # Generate all possible actions from the current state, which includes moving to a neighboring workshop in a valid direction
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_pos = (start_pos[0] + d_row, start_pos[1] + d_col)
           # Check if the new position is valid, ie within the bounds of the city map and not a closed workshop
           if (0 <= new_pos[0] < num_rows and 0 <= new_pos[1] < num_cols and state[new_pos[0]][new_pos[1]] != 'x'):
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               number_to_be_moved = new_state[start_pos[0]][start_pos[1]]
               new_state[start_pos[0]][start_pos[1]] = 'x'
               new_state[new_pos[0]][new_pos[1]] = number_to_be_moved
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of moves made, as our objective is to minimize the number of moves required to reach the goal state
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, end_pos, districts), new_cost, actions + [(start_pos, new_pos)], new_state))
                  
   return None


def heuristic(state, end_pos, districts):
   # An admissible and consistent heuristic is the sum of the Manhattan distances (the shortest path) of each workshop from its goal position
   # The heuristic relaxes the constraint that a workshop can only be moved to a neighboring workshop
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
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
