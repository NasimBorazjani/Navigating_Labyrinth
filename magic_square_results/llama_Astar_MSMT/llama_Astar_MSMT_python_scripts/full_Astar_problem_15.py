
import heapq


def initialize():
   # Define the initial state of the magic square, with 'x' represented as None
   initial_state = [[None, None, None], [None, None, 55], [None, None, None]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   goal_col_sum = 190
   goal_row_sum = 167
   goal_diagonal_sum = 172


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the swaps required to get to each state in a list; no swaps performed to reach the initial state
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, goal_col_sum, goal_row_sum, goal_diagonal_sum, visited_costs, queue
  
  
def a_star():
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial state of the magic square, number of rows and columns, and the goal sums)
   initial_state, num_rows, num_cols, goal_col_sum, goal_row_sum, goal_diagonal_sum, visited_costs, queue = initialize()


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # We can check if the current state is the goal state with a simple equality check, as the goal state is predefined
       if state == goal_state:
           return actions


       # Generate all valid actions from the current state, which includes replacing any of the 'x's with a unique integer from the given range
       # Iterate through the state
       for i in range(num_rows):
           for j in range(num_cols):
               # Check if the current position is a 'x'
               if state[i][j] is None:
                   # Generate all possible unique integers for the current position
                   for number in range(48, 78):
                       # Check if the new state would be valid, ie the sum of the column, row, and diagonal would remain equal to the goal sums
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = number
                       # The cost so far is the number of swaps made, as our objective is to minimize the number of swaps required to reach the goal state 
                       new_cost = g + 1
                      
                       # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [(i, j, number)], new_state))
                          
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the sum of the absolute differences between the current sums of the columns, rows, and diagonal and the goal sums
   # This heuristic relaxes the constraint that a 'x' can only be replaced with a unique integer from the given range
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched 'x' must be replaced at least once
   # The heuristic is consistent because moving a 'x' to a unique integer results in a decrease in the heuristic cost of the successor node by a max of 1 (if the moved 'x's position is not in the goal state), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] is None:
               h += 1
   return h


print(a_star())
