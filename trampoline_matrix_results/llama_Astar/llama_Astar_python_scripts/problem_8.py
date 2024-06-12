
import heapq


def a_star():
   # Define the initial state of the trampoline park, as a 2d tuple
   initial_state = ((0, 1, 1, 1, 0, 0, 0, 1, 0),
                   (0, 1, 1, 0, 1, 0, 1, 0, 0),
                   (1, 0, 1, 1, 1, 1, 0, 0, 1),
                   (0, 0, 1, 0, 1, 1, 1, 0, 1),
                   (1, 0, 1, 1, 0, 1, 1, 0, 1),
                   (1, 1, 1, 1, 1, 0, 0, 0, 0),
                   (0, 0, 1, 1, 1, 0, 0, 0, 1),
                   (1, 1, 1, 0, 0, 0, 0, 1, 1),
                   (1, 1, 1, 0, 0, 0, 0, 1, 1))
  
   # Encoding other variables given in the problem statement
   num_rows = 9
   num_cols = 9
   num_diagonal_jumps = 3


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the jumps required to get to each state in a list; no jumps performed to reach the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if (state[8][3] == 0):
           return actions


       # Generate all possible actions from the current state, which includes jumping to any of the 8 adjacent trampolines, as long as they are not broken
       for row_diff in range(-1, 2):
           for col_diff in range(-1, 2):
               # Check if the new state would be valid, ie the jump must not exceed the grid boundaries and the number of diagonal jumps must be exactly 3
               if (0 <= row_diff + row_diff + 8 - col_diff < num_rows and
                   0 <= col_diff + col_diff + 3 - row_diff < num_cols and
                   abs(row_diff) + abs(col_diff) == num_diagonal_jumps):
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   new_state[row_diff + 8][col_diff + 3] = 1
                   new_state = tuple(tuple(row) for row in new_state)
                   # The cost so far is the number of jumps made, as the task is to minimize the number of jumps required to reach the goal state
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(row_diff + 8, col_diff + 3)], new_state))
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the Manhattan distance from the current state to the goal state
   # This heuristic is admissible because it never overestimates the cost to reach the goal, as each diagonal jump is counted as 2 units in the Manhattan distance
   # It is consistent because moving a jump from one diagonal to another reduces the heuristic cost of the successor node by a max of 2 (if the moved jump is a diagonal one), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for row in range(9):
       for col in range(9):
           if state[row][col] == 1:
               h += abs(row - 8) + abs(col - 3)
   return h


print(a_star())
