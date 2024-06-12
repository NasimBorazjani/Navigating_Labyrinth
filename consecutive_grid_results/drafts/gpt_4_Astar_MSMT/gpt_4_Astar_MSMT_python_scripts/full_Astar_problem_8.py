
import heapq
import numpy as np


def initialize():
   # Define the initial state of the grid, as a 2d tuple
   initial_state = (('x', 'x', 'x'), ('x', 36, 44), ('x', 34, 'x'))
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   range_start = 19
   range_end = 52
   # The set of available numbers includes all numbers in the range that are not already in the grid
   available_numbers = set(range(range_start, range_end)) - set([num for row in initial_state for num in row if isinstance(num, int)])


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state, available_numbers)]
  
   return num_rows, num_cols, range_start, range_end, visited_costs, queue
  
  
def a_star():
   # The initialize function initializes and returns the visited_costs dictionary and the priority queue and encodes all of the variables given in the problem (ie the initial state of the grid, dimensions of the grid, and the range of numbers)
   num_rows, num_cols, range_start, range_end, visited_costs, queue = initialize()


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state, available_numbers = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is where all the numbers in the grid are known, ie there are no 'x's in the grid
       if all(isinstance(num, int) for row in state for num in row):
           return actions


       # Generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   for num in available_numbers:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = num
                       new_state = tuple(tuple(row) for row in new_state)
                       # Check if the new state is valid, ie the numbers in each row and column are strictly increasing or decreasing
                       if all(row[i] < row[i + 1] for row in new_state for i in range(len(row) - 1)) or all(row[i] > row[i + 1] for row in new_state for i in range(len(row) - 1)):
                           if all(new_state[i][j] < new_state[i + 1][j] for i in range(len(new_state) - 1) for j in range(len(new_state[i]))) or all(new_state[i][j] > new_state[i + 1][j] for i in range(len(new_state) - 1) for j in range(len(new_state[i]))):
                               # The cost so far is the sum of the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
                               new_cost = sum(int(num) for num in new_state[0] if isinstance(num, int)) + sum(int(new_state[i][-1]) for i in range(num_rows) if isinstance(new_state[i][-1], int)) + sum(int(new_state[i][i]) for i in range(num_rows) if isinstance(new_state[i][i], int))


                               # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
                               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                                   visited_costs[new_state] = new_cost
                                   # The new set of available numbers is the old set minus the number added to the grid
                                   new_available_numbers = available_numbers - {num}
                                   heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, num)], new_state, new_available_numbers))
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the minimum remaining numbers that need to be added to the grid
   # The heuristic relaxes the constraints that the numbers in each row and column must be strictly increasing or decreasing and that each number can only be used once, and presumes we can add the smallest remaining numbers to the grid
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of adding a number to the grid is the number itself, which is always greater than or equal to the smallest remaining number, the decrease in the heuristic cost
   h = 0
   remaining_numbers = list(range(range_start, range_end))
   for i in range(num_rows):
       for j in range(num_cols):
           if state[i][j] == 'x':
               h += min(remaining_numbers)
               remaining_numbers.remove(min(remaining_numbers))
   return h


print(a_star())
