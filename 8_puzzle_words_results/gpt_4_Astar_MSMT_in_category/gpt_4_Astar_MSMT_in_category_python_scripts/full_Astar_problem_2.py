
import heapq


def initialize():
   # Define the initial state and the goal state of the puzzle, represented as 4x4 tuples
   initial_state = (('o', 'a', 'u', 'o'), ('p', 'r', 'l', 'e'), ('f', 'a', '_', 'f'), ('m', 'k', 'd', 'd'))
   goal_state = (('_', 'a', 'k', 'o'), ('p', 'o', 'l', 'e'), ('r', 'a', 'f', 'f'), ('m', 'u', 'd', 'd'))   
  
   # Encoding other variables given in the problem statement
   num_rows = 4
   num_cols = 4


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the swaps required to get to each state in a list; no swaps performed to reach the initial state
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, goal_state, num_rows, num_cols, visited_costs, queue
  
  
def a_star():
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial and goal board and dimensions of the puzzle board)
   initial_state, goal_state, num_rows, num_cols, visited_costs, queue = initialize()


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
       if state == goal_state:
           return actions


       # Generate all valid actions from the current state, which includes swapping any of the tiles neighboring the empty spot, with the empty spot
       # Generate the coordinates of the tiles neighboring "_"
       empty_row, empty_col = [(i, j) for i in range(num_rows) for j in range(num_cols) if state[i][j] == '_'][0]
       for d_row, d_col in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:
           swap_row, swap_col = empty_row + d_row, empty_col + d_col
           # Check if the swap is valid, ie if the coordinate of the tile to be swapped is a valid coordinate within the bounds of the board
           if 0 <= swap_row < num_rows and 0 <= swap_col < num_cols:
               # The actions is valid, generate the new state
               new_state = [list(row[:]) for row in state]
               # Do the swap
               new_state[empty_row][empty_col], new_state[swap_row][swap_col] = new_state[swap_row][swap_col], new_state[empty_row][empty_col]
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the number of swaps made, as our objective is to minimize the number of swaps required to reach the goal state 
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The direction of the swap is determined by the change in the row and column indices of the empty spot
                   if d_row == -1 and d_col == 1:
                       direction = 'up-right'
                   elif d_row == 1 and d_col == 1:
                       direction = 'down-right'
                   elif d_row == -1 and d_col == -1:
                       direction = 'up-left'
                   elif d_row == 1 and d_col == -1:
                       direction = 'down-left'
                   heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [direction], new_state))
                  
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the sum of the Manhattan distances (the shortest path) of each tile from its goal position
   # The heuristic relaxes the constraint that a tile can only be swapped with the empty spot and presumes we can move the tiles to their goal position by swapping them with any of the other tiles
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving a tile to a neighboring coordinate is always 1, which is exactly the decrease in the Manhattan distance, if the tile is moved toward its goal position, otherwise the estimated cost of the successor node is the same or higher, and he heuristic estimate for the goal state is 0, as the distance of each tile from its goal position would be 0 in the goal state.
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           # Can't compare integers with "_" when finding the goal position of each tile, thus ignore the "_" tile
           if state[i][j] != '_':
               # Get goal position of each tile
               goal_row, goal_col = [(x, y) for x in range(len(goal)) for y in range(len(goal[x])) if goal[x][y] == state[i][j]][0]
               # Add the the Manhattan distance of the current and goal coordinates of the tile to the estimate
               h += abs(i - goal_row) + abs(j - goal_col)
   return h


print(a_star())