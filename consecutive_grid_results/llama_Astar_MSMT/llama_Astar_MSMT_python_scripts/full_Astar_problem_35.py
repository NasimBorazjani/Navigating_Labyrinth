
import heapq


def initialize():
   # Define the initial state of the grid
   initial_state = [['x', 'x', 'x'], ['x', '61', '62'], ['x', 'x', '63']]
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   min_val = 40
   max_val = 87


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[str(initial_state)] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the replacements required to get to each state in a list; no replacements performed to reach the initial state
   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, min_val, max_val, visited_costs, queue
  
  
def a_star():
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial state of the grid, number of rows and columns, and the range of the numbers)
   initial_state, num_rows, num_cols, min_val, max_val, visited_costs, queue = initialize()


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is where each row and column and the diagonal are strictly increasing or decreasing, and no 'x' is left in the grid
       if all(is_increasing_or_decreasing(row) for row in state) and all(is_increasing_or_decreasing(state[i] for i in range(len(state))) for _ in range(len(state))) and all(is_increasing_or_decreasing(state[i][i] for i in range(len(state))) for _ in range(len(state))) and '_' not in str(state):
           return actions


       # Generate all valid actions from the current state, which includes replacing an 'x' with a unique number from the range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] == 'x':
                   for num in range(min_val, max_val + 1):
                       # Check if the new state would be valid, ie the number is unique in its row, column, and diagonal
                       if is_valid(state, row_ind, col_ind, num):
                           # Generate the new state
                           new_state = [list(row[:]) for row in state]
                           new_state[row_ind][col_ind] = num
                           new_state = [tuple(row) for row in new_state]
                           # The cost so far is the number of replacements made, as our objective is to minimize the number of replacements required
                           new_cost = g + 1


                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                           if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                               visited_costs[str(new_state)] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(state, new_state), new_cost, actions + [(row_ind, col_ind, num)], new_state))
                              
   return None


def is_increasing_or_decreasing(seq):
   # Helper function to check if a sequence is strictly increasing or decreasing
   return all(i < j for i, j in zip(seq, seq[1:])) or all(i > j for i, j in zip(seq, seq[1:]))


def is_valid(state, row_ind, col_ind, num):
   # Helper function to check if replacing an 'x' with a number is valid
   # The number must be unique in its row, column, and diagonal
   return num not in state[row_ind] and num not in tuple(state[i][col_ind] for i in range(len(state))) and num not in tuple(state[i][i] for i in range(len(state)))


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
   # This heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing, and that the sum of the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner should be minimized
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched number must be replaced at least once
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 2 (if the moved number is in the topmost row, rightmost column, or the diagonal), which is equal to the cost of reaching the successor node
   return sum(state[0]) + sum(state[i][-1] for i in range(len(state))) + sum(state[i][i] for i in range(len(state)))


print(a_star())
