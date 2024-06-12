
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[32, 75, 36, None], [None, 83, None, None], [None, 77, 58, 44], [None, 60, None, None]]
   # Define the goal state, with the sums of the rows and columns
   goal_state = (None, 244, 251, None, 295, 204, None, 237)
  
   # Encoding other variables given in the problem statement
   num_rows = 4
   num_cols = 4


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[tuple(map(tuple, initial_state))] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the swaps required to get to each state in a list; no swaps performed to reach the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
       if state == goal_state:
           return actions


       # Generate all valid actions from the current state, which includes swapping any of the tiles neighboring the empty spot, with the empty spot
       # Generate the coordinates of the tiles neighboring "_"
       for row_ind, row in enumerate(state):
           for col_ind, value in enumerate(row):
               if value is None:
                   # The actions is valid, generate the new state
                   new_state = [list(row[:]) for row in state]
                   # Replace the 'x' with a unique integer from the given range
                   new_state[row_ind][col_ind] = get_unique_integer(new_state)
                   new_state = [tuple(row) for row in new_state]
                   new_state = tuple(tuple(row) for row in new_state)
                   # The cost so far is the number of swaps made, as our objective is to minimize the number of swaps required to reach the goal state 
                   new_cost = g + 1
                  
                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [(row_ind, col_ind, new_state[row_ind][col_ind])], new_state))
                      
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the sum of the absolute differences between the current state and the goal state
   # This heuristic relaxes the constraint that a tile can only be swapped with the empty spot and presumes we can move the tiles to their goal position by swapping them with any of the other tiles
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving a tile to a neighboring coordinate is always 1, which is exactly the decrease in the Manhattan distance, if the tile is moved toward its goal position, otherwise the estimated cost of the successor node is the same or higher, and he heuristic estimate for the goal state is 0, as the distance of each tile from its goal position would be 0 in the goal state.
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           # Can't compare integers with "_" when finding the goal position of each tile, thus ignore the "_" tile
           if state[i][j] != '_':
               # Get goal position of each tile
               goal_value = goal[i][j]
               # Add the the absolute difference of the current and goal values of the tile to the estimate
               h += abs(state[i][j] - goal_value)
   return h


def get_unique_integer(state):
   # Generate a list of all the unique integers in the given range
   unique_integers = list(range(30, 87))
   # Remove the integers that are already in the state
   for row in state:
       for value in row:
           if value in unique_integers:
               unique_integers.remove(value)
   # Return the first unique integer in the range
   return unique_integers[0]


print(a_star())
