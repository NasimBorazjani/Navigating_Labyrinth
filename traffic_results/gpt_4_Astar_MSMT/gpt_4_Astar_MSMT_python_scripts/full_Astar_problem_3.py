
import heapq

def initialize():
   # Define the initial state and the goal state of the problem, represented as 2d tuples
   initial_state = ((7, 7))
   goal_state = ((1, 2))   
  
   # Encoding other variables given in the problem statement
   num_rows = 9
   num_cols = 9
   matrix = [[10, 14, 4, 16, 'x', 17, 5, 'x', 'x'],
             [5, 20, 16, 3, 1, 8, 'x', 16, 19],
             [1, 'x', 5, 13, 3, 15, 19, 15, 'x'],
             ['x', 16, 13, 20, 'x', 8, 'x', 'x', 'x'],
             ['x', 16, 'x', 17, 11, 1, 'x', 15, 'x'],
             [10, 'x', 14, 11, 5, 7, 12, 'x', 5],
             [7, 'x', 15, 'x', 15, 8, 3, 6, 7],
             ['x', 12, 14, 'x', 'x', 'x', 16, 3, 13],
             [19, 5, 10, 'x', 'x', 'x', 9, 7, 14]]
   districts = {1: range(0, 2), 2: range(2, 7), 3: range(7, 9)}

   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0

   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state, {1: False, 2: False, 3: True})]
  
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

       # Generate all valid actions from the current state, which includes moving to any of the neighboring cells
       # Generate the coordinates of the neighboring cells
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = state[0] + d_row, state[1] + d_col
           # Check if the move is valid, ie if the coordinate of the cell to be moved to is a valid coordinate within the bounds of the board and the cell is not closed
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and matrix[new_row][new_col] != 'x':
               # The move is valid, generate the new state
               new_state = (new_row, new_col)
               # The cost so far is the sum of the travel times, as our objective is to minimize the travel time
               new_cost = g + matrix[new_row][new_col]
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   new_visited_districts = visited_districts.copy()
                   for district, rows in districts.items():
                       if new_row in rows:
                           new_visited_districts[district] = True
                   heapq.heappush(queue, (g + heuristic(new_state, goal_state), new_cost, actions + [new_state], new_state, new_visited_districts))
                  
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the Manhattan distance (the shortest path) of the current position from the goal position
   # The heuristic relaxes the constraint that a cell can only be moved to if it's not closed and presumes we can move to the goal position by moving to any of the neighboring cells
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving to a neighboring coordinate is always 1, which is exactly the decrease in the Manhattan distance, if the cell is moved toward its goal position, otherwise the estimated cost of the successor node is the same or higher, and he heuristic estimate for the goal state is 0, as the distance of the current position from its goal position would be 0 in the goal state.
   h = abs(state[0] - goal[0]) + abs(state[1] - goal[1])
   return h


print(a_star())
