
import heapq

def initialize():
   # Define the initial state and the goal state of the problem, represented as tuples
   initial_state = (5, 7)
   goal_state = (2, 1)
  
   # Encoding other variables given in the problem statement
   num_rows = 9
   num_cols = 9
   matrix = [[13, 'x', 'x', 3, 10, 20, 3, 'x', 5],
             ['x', 'x', 'x', 'x', 20, 16, 'x', 'x', 17],
             [3, 14, 18, 8, 1, 20, 14, 'x', 7],
             [13, 3, 6, 10, 7, 4, 6, 6, 1],
             [10, 12, 2, 'x', 11, 'x', 10, 8, 11],
             ['x', 'x', 'x', 11, 6, 18, 13, 20, 17],
             ['x', 'x', 16, 'x', 4, 17, 7, 10, 15],
             ['x', 7, 16, 6, 19, 4, 7, 'x', 'x'],
             ['x', 11, 18, 'x', 'x', 'x', 3, 8, 'x']]
   districts = {1: range(0, 3), 2: range(3, 5), 3: range(5, 9)}

   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0

   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state, {1: False, 2: False, 3: True})]
  
   return initial_state, goal_state, num_rows, num_cols, matrix, districts, visited_costs, queue
  
def a_star():
  
   initial_state, goal_state, num_rows, num_cols, matrix, districts, visited_costs, queue = initialize()

   while queue:
       _, g, actions, state, visited_districts = heapq.heappop(queue)

       # Check if the current state is the goal state
       if state == goal_state and all(visited_districts.values()):
           return actions

       # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring cells
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = state[0] + d_row, state[1] + d_col
           # Check if the new state would be valid, ie if the coordinate of the cell to move to is a valid coordinate within the bounds of the matrix and the cell is not 'x'
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and matrix[new_row][new_col] != 'x':
               # Generate the new state
               new_state = (new_row, new_col)
               # The cost so far is the sum of the travel times, as our objective is to minimize the total travel time 
               new_cost = g + matrix[new_row][new_col]
               # Update the visited districts
               new_visited_districts = visited_districts.copy()
               for district, rows in districts.items():
                   if new_row in rows:
                       new_visited_districts[district] = True

               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [new_state], new_state, new_visited_districts))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the Manhattan distance (the shortest path) of the current position from the goal position
   # The heuristic relaxes the constraint that a cell can only be moved to if it's not 'x' and presumes we can move to the goal position by moving to any of the neighboring cells
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving to a neighboring coordinate is always greater than or equal to 1, which is exactly the decrease in the Manhattan distance, if the cell is moved toward its goal position, otherwise the estimated cost of the successor node is the same or higher, and he heuristic estimate for the goal state is 0, as the distance of the goal position from itself would be 0.
   h = abs(state[0] - goal[0]) + abs(state[1] - goal[1])
   return h


print(a_star())
