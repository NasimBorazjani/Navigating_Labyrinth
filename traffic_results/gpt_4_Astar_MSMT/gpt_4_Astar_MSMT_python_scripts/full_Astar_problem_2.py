
import heapq

def initialize():
   # Define the initial state and the goal state of the problem, represented as 2d tuples
   initial_state = ((2, 2))
   goal_state = ((5, 8))   
  
   # Encoding other variables given in the problem statement
   num_rows = 9
   num_cols = 9
   matrix = [['x', 13, 9, 'x', 'x', 16, 6, 18, 7],
             ['x', 3, 11, 'x', 'x', 5, 7, 'x', 19],
             [8, 'x', 2, 5, 6, 12, 9, 10, 7],
             [12, 1, 6, 20, 19, 18, 12, 'x', 14],
             [16, 5, 10, 3, 'x', 'x', 'x', 1, 9],
             ['x', 3, 'x', 'x', 'x', 'x', 'x', 'x', 4],
             [7, 10, 'x', 1, 'x', 'x', 17, 'x', 8],
             ['x', 5, 'x', 'x', 'x', 17, 'x', 9, 'x'],
             [13, 16, 8, 15, 'x', 2, 'x', 1, 2]]
   districts = {1: range(0, 2), 2: range(2, 5), 3: range(5, 9)}

   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0

   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state, {1: False, 2: True, 3: False})]
  
   return initial_state, goal_state, num_rows, num_cols, matrix, districts, visited_costs, queue
  
  
def a_star():
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial and goal board and dimensions of the puzzle board)
   initial_state, goal_state, num_rows, num_cols, matrix, districts, visited_costs, queue = initialize()

   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state, visited_districts = heapq.heappop(queue)

       # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
       if state == goal_state and all(visited_districts.values()):
           return actions

       # Generate all valid actions from the current state, which includes moving to any of the neighboring workshops
       # Generate the coordinates of the neighboring workshops
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = state[0] + d_row, state[1] + d_col
           # Check if the move is valid, ie if the coordinate of the workshop to be moved to is a valid coordinate within the bounds of the city and is not a closed workshop
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and matrix[new_row][new_col] != 'x':
               # The move is valid, generate the new state
               new_state = (new_row, new_col)
               # The cost so far is the travel time to the new workshop, as our objective is to minimize the travel time 
               new_cost = g + matrix[new_row][new_col]
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # Update the visited districts
                   new_visited_districts = visited_districts.copy()
                   for district, rows in districts.items():
                       if new_row in rows:
                           new_visited_districts[district] = True
                   heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [new_state], new_state, new_visited_districts))
                  
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the Manhattan distance (the shortest path) of the current workshop from the goal workshop
   # The heuristic relaxes the constraint that a workshop can only be moved to if it is a neighboring workshop and presumes we can move to the goal workshop directly from the current workshop
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving to a neighboring workshop is always greater than or equal to 1, which is exactly the decrease in the Manhattan distance, if the workshop is moved toward its goal position, otherwise the estimated cost of the successor node is the same or higher, and he heuristic estimate for the goal state is 0, as the distance of the goal workshop from itself would be 0.
   h = abs(state[0] - goal[0]) + abs(state[1] - goal[1])
   return h


print(a_star())
