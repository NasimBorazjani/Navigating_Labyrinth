
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, None, 80, 72], [44, None, 39, None], [None, 70, 64, None], [None, 67, None, 42]]
   # Define the goal state, with the sums of the rows, columns, and diagonal
   goal_state = (None, 252, 238, None, 221, 257, None, 221)
  
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


       # Generate all valid actions from the current state, which includes replacing any of the 'x's with a unique integer from the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] is None:
                   # The actions is valid, generate the new state
                   new_state = [list(row[:]) for row in state]
                   # Replace the 'x' with a unique integer from the given range
                   new_state[row_ind][col_ind] = 37
                   # Check if the new state is valid, ie if the sums of the rows, columns, and diagonal are as required
                   if is_valid(new_state):
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the number of swaps made, as our objective is to minimize the number of swaps required to reach the goal state 
                       new_cost = g + 1
                      
                       # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [(row_ind, col_ind, 37)], new_state))
                          
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the sum of the absolute differences between the current sums of rows, columns, and diagonal and the goal sums
   # This heuristic relaxes the constraint that a 'x' can only be replaced with a unique integer from the given range
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched 'x' must be replaced at least once
   # The heuristic is consistent because moving a 'x' from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved 'x's new position has the same sum as the old one), which is equal to the cost of reaching the successor node
   h = 0
   for row_ind in range(len(state)):
       for col_ind in range(len(state[row_ind])):
           if state[row_ind][col_ind] is None:
               h += 37
   return h


def is_valid(state):
   # Check if the sums of the rows, columns, and diagonal are as required
   # The sums of the rows and columns are calculated by summing up the numbers in each row and column
   # The sum of the diagonal is calculated by summing up the numbers in the positions (i, i) for i in the range of the number of rows or columns
   # The sums are then compared with the goal sums
   row_sums = [sum(row) for row in state]
   col_sums = [sum(state[i][j] for i in range(len(state))) for j in range(len(state[0]))]
   diagonal_sum = sum(state[i][i] for i in range(len(state)))
   return row_sums == [None, 252, 238, None] and col_sums == [None, 221, 257, None] and diagonal_sum == 221


print(a_star())
