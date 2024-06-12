
import heapq


def initialize():
   # Define the initial state of the magic square, with 'x' represented as None
   initial_state = [[None, None, 62], [None, None, None], [None, None, 56]]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   goal_column_sum = 212
   goal_row_sum = 193
   goal_diagonal_sum = 217


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, goal_column_sum, goal_row_sum, goal_diagonal_sum, visited_costs, queue
  
def a_star():
  
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial state of the magic square, dimensions of the square, and the goal sums)
   initial_state, num_rows, num_cols, goal_column_sum, goal_row_sum, goal_diagonal_sum, visited_costs, queue = initialize()


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is when the sums of the specified rows, columns, and diagonal equal the given amounts
       if sum(state[0][2:]) == goal_row_sum and sum(state[1][2:]) == goal_column_sum and state[0][0] + state[1][1] + state[2][2] == goal_diagonal_sum:
           return actions


       # Generate all possible actions from the current state, which includes replacing any of the 'x's with a unique integer from the given range
       for row in range(num_rows):
           for col in range(num_cols):
               if state[row][col] is None:
                   # The possible unique integers are between 50 and 84
                   for num in range(50, 85):
                       # Check if the new state would be valid, ie the sum of the specified rows, columns, and diagonal remain equal to the goal amounts
                       new_state = [list(row[:]) for row in state]
                       new_state[row][col] = num
                       # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to reach the goal state
                       new_cost = g + 1


                       # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(row, col, num)], new_state))
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sums of the specified rows, columns, and diagonal and the goal sums
   # This heuristic relaxes the constraint that the sum of all numbers in the grid must be as low as possible
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched sum must be adjusted at least once
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of the absolute difference between the current and goal sums, which is equal to the cost of reaching the successor node
   h = 0
   h += abs(sum(state[0][2:]) - goal_row_sum)
   h += abs(sum(state[1][2:]) - goal_column_sum)
   h += abs(state[0][0] + state[1][1] + state[2][2] - goal_diagonal_sum)
   return h


print(a_star())
