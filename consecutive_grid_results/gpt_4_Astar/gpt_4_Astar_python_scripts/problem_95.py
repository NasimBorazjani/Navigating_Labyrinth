
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple
   initial_state = (('x', 'x', 'x', 'x'), ('25', '32', '40', '46'), ('27', 'x', '39', '42'), ('x', '34', '38', '41'))
  
   # Encoding other variables given in the problem statement
   num_rows = 4
   num_cols = 4
   min_num = 13
   max_num = 73
   # The set of all possible numbers that can be added to the grid
   available_nums = set(range(min_num, max_num + 1))


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state, available_nums)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state, available_nums = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is where all the 'x's have been replaced with unique integers from the given range
       if 'x' not in np.array(state).flatten():
           return actions


       # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   for num in available_nums:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = str(num)
                       new_state = tuple(tuple(row) for row in new_state)
                       # Check if the new state is valid, ie the numbers in each row and column are strictly increasing or decreasing
                       if all(sorted(row) == list(row) or sorted(row, reverse=True) == list(row) for row in new_state) and all(sorted(col) == list(col) or sorted(col, reverse=True) == list(col) for col in zip(*new_state)):
                           # The cost so far is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left corner to the bottom-right corner
                           new_cost = sum(int(num) for num in new_state[0] if num != 'x') + sum(int(new_state[i][-1]) for i in range(num_rows) if new_state[i][-1] != 'x') + sum(int(new_state[i][i]) for i in range(num_rows) if new_state[i][i] != 'x')
                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               # The actions is valid, generate the new state
                               heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, num)], new_state, available_nums - {num}))
                   break
           else:
               continue
           break
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the count of 'x's in the grid
   # This heuristic relaxes the constraints that the numbers in each row and column must be strictly increasing or decreasing and that each number in the grid must be unique; ie It presumes we can replace any 'x' with any number
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the estimated cost of the next node is higher if an 'x' is replaced with a number, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum number that can be added to the grid is the maximum number in the range, which is exactly the number used to replace the 'x' in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   return sum(row.count('x') for row in state)


print(a_star())
