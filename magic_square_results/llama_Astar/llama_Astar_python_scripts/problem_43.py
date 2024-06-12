
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, 51, 39, None], [None, None, 48, 37], [54, None, None, None], [None, None, None, 53]]
   # Define the goal state, with the sums of rows and columns and the diagonal
   goal_state = (None, 212, 185, None, 180, 202, None, 193)
  
   # Encoding other variables given in the problem statement
   num_rows = 4
   num_cols = 4


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


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
       for row in range(num_rows):
           for col in range(num_cols):
               if state[row][col] is None:
                   # The actions is valid, generate the new state
                   new_state = [list(row[:]) for row in state]
                   # Replace the 'x' with a unique integer from the given range
                   new_state[row][col] = get_unique_integer(new_state)
                   new_state = tuple(tuple(row) for row in new_state)
                   # The cost so far is the number of swaps made, as our objective is to minimize the number of swaps required to reach the goal state 
                   new_cost = g + 1
                  
                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [(row, col, new_state[row][col])], new_state))
                      
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the sum of the absolute differences between the current sums of rows, columns, and the diagonal and the goal sums
   # This heuristic relaxes the constraint that a 'x' can only be replaced with a unique integer from the given range
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched sum must be corrected at least once
   # The heuristic is consistent because moving a 'x' to a unique integer from the given range reduces the heuristic cost of the successor node by a max of 1 (if the moved integer's sum matches the goal sum), which is equal to the cost of reaching the successor node
   h = 0
   for row in range(len(state)):
       for col in range(len(state[row])):
           if state[row][col] is not None:
               # Calculate the current sum of the row or column or the diagonal
               current_sum = sum(state[i][col] for i in range(row, row + 2)) if col < 2 else sum(state[row][i] for i in range(col, col + 2)) if row < 2 else sum(state[i][i] for i in range(4))
               # Add the absolute difference between the current sum and the goal sum to the estimate
               h += abs(current_sum - goal[row][col])
   return h


def get_unique_integer(state):
   # Generate a list of all unique integers in the given range
   unique_integers = list(range(35, 62))
   # Remove the integers that are already in the state
   for row in state:
       for num in row:
           if num is not None:
               unique_integers.remove(num)
   # Return the first unique integer in the list
   return unique_integers[0]


print(a_star())
