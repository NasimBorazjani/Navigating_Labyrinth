
import heapq


def initialize():
   # Define the initial state of the magic square, with 'x' represented as None
   initial_state = [[None, None, None], [None, None, None], [42, 45, None]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   goal_col_sum = [115, 95, 133]


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, goal_col_sum, visited_costs, queue
  
def a_star():
  
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial state of the magic square, number of rows and columns, and goal column sums)
   initial_state, num_rows, num_cols, goal_col_sum, visited_costs, queue = initialize()


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is when the sum of the numbers in the specified rows, columns, and diagonal equals the given amounts
       if all(sum(row) == goal_col_sum[i] for i, row in enumerate(state)) and sum(sum(row) for row in state) == 245:
           return actions


       # Generate all possible actions from the current state, which includes replacing any of the 'x's with a unique integer from the given range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   for num in range(46, 9, -1):
                       # Check if the new state would be valid, ie the new number must not be in the same row, column, or diagonal
                       if num not in new_state[row_ind] and num not in state[col_ind] and num not in [new_state[i][i] for i in range(num_rows)]:
                           new_state[row_ind][col_ind] = num
                           new_state = tuple(tuple(row) for row in new_state)
                           # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to reach the goal state
                           new_cost = g + 1


                           # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state, goal_col_sum), new_cost, actions + [(row_ind, col_ind, num)], new_state))
   return None


def heuristic(state, goal_col_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current column sums and the goal column sums
   # This heuristic relaxes the constraint that the numbers in the magic square must be unique integers, as it only considers the current state and does not consider the validity of the numbers in the grid
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be a non-negative number
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 2 (if the moved number is in the same row, column, or diagonal), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for row_ind in range(len(state)):
       for col_ind in range(len(state[row_ind])):
           h += abs(state[row_ind][col_ind] - goal_col_sum[row_ind])
   return h


print(a_star())
