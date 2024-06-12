
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[35, None, 51, None], [None, None, None, 23], [None, 32, 31, 52], [None, None, None, None]]
   # Define the goal state, with the sums of the rows and columns
   goal_state = (None, 148, 157, None, 138, 149, None, 133)
  
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
       # Iterate through the grid
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               # Check if the current position is empty
               if state[row_ind][col_ind] is None:
                   # Generate all possible numbers that can be placed in the current position
                   for num in range(22, 54):
                       # Check if the new state would be valid, ie the new state must maintain the constraints on the sums of the rows and columns
                       new_state = [list(row[:]) for row in state]
                       new_state[row_ind][col_ind] = num
                       if is_valid(new_state):
                           new_state = tuple(tuple(row) for row in new_state)
                           # The cost so far is the number of swaps made, as our objective is to minimize the number of swaps required to reach the goal state 
                           new_cost = g + 1
                          
                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [(row_ind, col_ind, num)], new_state))
                              
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the sum of the absolute differences between the current sums of the rows and columns and the goal sums
   # This heuristic relaxes the constraint that a tile can only be swapped with the empty spot and presumes we can move the tiles to their goal position by swapping them with any of the other tiles
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving a tile to a neighboring coordinate is always 1, which is exactly the decrease in the Manhattan distance, if the tile is moved toward its goal position, otherwise the estimated cost of the successor node is the same or higher, and he heuristic estimate for the goal state is 0, as the distance of each tile from its goal position would be 0 in the goal state.
   h = 0
   for row_ind in range(len(state)):
       for col_ind in range(len(state[row_ind])):
           if state[row_ind][col_ind] is not None:
               h += abs(sum(state[row_ind]) - goal[row_ind]) + abs(sum(state[col_ind] for state in state) - goal[len(state) + col_ind])
   return h


def is_valid(state):
   # Check if the current state is valid, ie if the sums of the rows and columns and the diagonal equal the goal sums
   for row_ind in range(len(state)):
       if sum(state[row_ind]) != goal[row_ind]:
           return False
   for col_ind in range(len(state[0])):
       if sum(state[row_ind][col_ind] for row_ind in range(len(state))) != goal[len(state) + col_ind]:
           return False
   if sum(state[row_ind][col_ind] for row_ind, col_ind in enumerate(range(len(state) - 1, -1, -1))) != goal[-1]:
       return False
   return True


print(a_star())
