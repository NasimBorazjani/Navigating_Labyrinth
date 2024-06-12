
import heapq


def initialize():
   # Define the initial state of the grid, with 'x' representing unknown values
   initial_state = [['x', 'x', 'x'],
                    ['x', 'x', 'x'],
                    ['40', 'x', '71']]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   goal_col_sum = [183, 194, 161]


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[tuple(map(tuple, initial_state))] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the coordinates and values of the replaced 'x's in the grid in a list; no replacements performed to reach the initial state
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, goal_col_sum, visited_costs, queue
  
  
def a_star():
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial state of the grid, number of rows and columns, and the goal column sums)
   initial_state, num_rows, num_cols, goal_col_sum, visited_costs, queue = initialize()


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is when the sum of all the numbers in the grid is the lowest possible and the sum of the specified rows, columns, and diagonal equals the given amounts
       if sum(sum(row) for row in state) == 161 and all(sum(row[i] for row in state) == goal_col_sum[i] for i in range(num_cols)) and sum(state[i][i] for i in range(num_rows)) == goal_col_sum[-1]:
           return actions


       # Generate all possible actions from the current state, which includes replacing any of the 'x's with a unique integer from the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] == 'x':
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   for num in range(40, 90):
                       if num not in new_state:
                           # Replace the 'x' with the unique integer
                           new_state[row_ind][col_ind] = num
                           new_state = [tuple(row) for row in new_state]
                           # The cost so far is the number of replacements made, as our objective is to minimize the number of replacements required to reach the goal state
                           new_cost = g + 1


                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                           if tuple(tuple(row) for row in new_state) not in visited_costs or new_cost < visited_costs[tuple(tuple(row) for row in new_state)]:
                               visited_costs[tuple(tuple(row) for row in new_state)] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state, goal_col_sum), new_cost, actions + [(row_ind, col_ind, num)], new_state))
                              
   return None


def heuristic(state, goal_col_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current column sums and the goal column sums
   # This heuristic relaxes the constraint that the sum of all the numbers in the grid must be as low as possible
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be non-negative
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by the absolute difference between the old and new column sums, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for i in range(len(goal_col_sum)):
       h += abs(sum(state[j][i] for j in range(len(state))) - goal_col_sum[i])
   return h


print(a_star())
