
import numpy as np
import heapq


def a_star():
   # Define the initial state of the grid
   initial_state = np.array([['x', '47', 'x', '55'],
                             ['29', '34', 'x', 'x'],
                             ['16', 'x', 'x', '35'],
                             ['x', '26', 'x', 'x']])
  
   # Encoding other variables given in the problem statement
   num_rows = 4
   num_cols = 4
   # The range of numbers that can be used to replace the 'x's
   numbers = set(range(12, 58))


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   # The initial state must be mapped to a tuple first to avoid the error: visited_costs[initial_state] = 0 TypeError: unhashable type: 'numpy.ndarray'
   visited_costs[tuple(map(tuple, initial_state))] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is where all the 'x's have been replaced with unique integers from the given range
       if 'x' not in state:
           return actions


       # If the state has at least 1 remaining unknown number, ie 'x', generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
       # Find the next 'x' in the grid
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   # Get the set of numbers that are already in the grid
                   present_numbers = set([int(num) for row in state for num in row if num != 'x'])
                   # The set of available numbers is the difference between the set of all numbers in the range and the set of numbers that are already in the grid
                   available_numbers = numbers - present_numbers
                   for num in available_numbers:
                       # Generate the new state
                       new_state = state.copy()
                       new_state[i][j] = str(num)
                       # Check if the new state is valid, ie the numbers in each row and column are strictly increasing or decreasing
                       if all(sorted(row) == list(row) or sorted(row, reverse=True) == list(row) for row in new_state) and all(sorted(new_state[:,col]) == list(new_state[:,col]) or sorted(new_state[:,col], reverse=True) == list(new_state[:,col]) for col in range(num_cols)):
                           # The cost so far is the sum of the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
                           # Avoid this: ValueError: invalid literal for int() with base 10: 'x' and TypeError: '<' not supported between instances of 'int' and 'str'    when comparing the elements of a row/column or when calculating the sums for the new_cost by filtering out the 'x's first
                           new_cost = sum(int(num) for num in new_state[0] if num != 'x') + sum(int(num) for num in new_state[:, -1] if num != 'x') + sum(int(new_state[i][i]) for i in range(num_rows) if new_state[i][i] != 'x')
                           # The new state must be mapped to a tuple first to avoid the error: visited_costs[new_state] = 0 TypeError: unhashable type: 'numpy.ndarray'
                           new_state_tuple = tuple(map(tuple, new_state))
                           if new_state_tuple not in visited_costs or new_cost < visited_costs[new_state_tuple]:
                               visited_costs[new_state_tuple] = new_cost
                               # The action is a tuple of the row index of the 'x', the column index of the 'x', and the value of the number that replaces the 'x'
                               heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, num)], new_state))
                   break
           else:
               continue
           break
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the minimum available numbers that can be used to replace the remaining 'x's in the grid
   # The heuristic relaxes the constraints that the numbers in each row and column must be strictly increasing or decreasing and that each number can only appear once in the grid; ie It presumes we can replace the 'x's with any of the available numbers
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' with a number is the number itself, which is always greater than or equal to the minimum available number, the decrease in the heuristic cost
   # Ensure all fo the variables are defined in the heurisitc implementation
   numbers = set(range(12, 58))
   present_numbers = set([int(num) for row in state for num in row if num != 'x'])
   available_numbers = numbers - present_numbers
   num_xs = sum(1 for row in state for num in row if num == 'x')
   return sum(sorted(list(available_numbers))[:num_xs])


print(a_star())
