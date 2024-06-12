
import heapq


def initialize():
   # Define the initial state of the grid, with 'x' representing unknown values
   initial_state = [['x', 'x', 'x'],
                    ['x', 'x', 'x'],
                    ['x', '70', 'x']]

   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   goal_col_sum = 191
   goal_row_sum = 194
   goal_diagonal_sum = 186

   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0

   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the swaps required to get to each state in a list; no swaps performed to reach the initial state
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, goal_col_sum, goal_row_sum, goal_diagonal_sum, visited_costs, queue
  
  
def a_star():
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial grid, dimensions of the grid, and the goal sums)
   initial_state, num_rows, num_cols, goal_col_sum, goal_row_sum, goal_diagonal_sum, visited_costs, queue = initialize()


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # We can check if the current state is the goal state by checking if the sums of the columns, rows, and diagonal match the goal sums
       if sum(state[i][0] for i in range(num_rows)) == goal_col_sum and sum(state[0][i] for i in range(num_cols)) == goal_row_sum and state[0][0] + state[1][1] + state[2][2] == goal_diagonal_sum:
           return actions


       # Generate all valid actions from the current state, which includes replacing any of the 'x's with a unique integer from the given range
       for row in range(num_rows):
           for col in range(num_cols):
               if state[row][col] == 'x':
                   # The actions is valid, generate the new state
                   new_state = [list(row[:]) for row in state]
                   # Replace the 'x' with a unique integer from the given range
                   new_state[row][col] = 48
                   new_state = tuple(tuple(row) for row in new_state)
                   # The cost so far is the number of swaps made, as our objective is to minimize the number of swaps required to reach the goal state 
                   new_cost = g + 1
                  
                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_col_sum, goal_row_sum, goal_diagonal_sum), new_cost, actions + [(row, col, 48)], new_state))
                      
   return None


def heuristic(state, goal_col_sum, goal_row_sum, goal_diagonal_sum):
   # An admissible and consistent heuristic is the sum of the absolute differences between the current sums of the columns, rows, and diagonal and the goal sums
   # This heuristic relaxes the constraint that the sums of the columns, rows, and diagonal must be equal to the goal sums
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched sum must be adjusted at least once
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved number's sum matches the goal sum for that row, column, or diagonal but not in the old position), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   h += abs(sum(state[i][0] for i in range(len(state))) - goal_col_sum)
   h += abs(sum(state[0][i] for i in range(len(state[0]))) - goal_row_sum)
   h += abs(state[0][0] + state[1][1] + state[2][2] - goal_diagonal_sum)
   return h


print(a_star())
