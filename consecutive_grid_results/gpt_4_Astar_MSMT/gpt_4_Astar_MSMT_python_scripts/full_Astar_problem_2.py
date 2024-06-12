
import heapq
import numpy as np


def initialize():
   # Define the initial state of the grid, as a 2d tuple
   initial_state = (('10', '15', '39'), ('x', '27', '29'), ('x', 'x', 'x'))
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   available_numbers = set(range(8, 41)) - set(int(i) for row in initial_state for i in row if i != 'x')


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state, available_numbers)]
  
   return num_rows, num_cols, available_numbers, visited_costs, queue


def a_star():
  
   num_rows, num_cols, available_numbers, visited_costs, queue = initialize()


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state, available_numbers = heapq.heappop(queue)


       # Check of the current state is the goal state
       # The goal state is where each cell in the grid contains a unique number and the numbers in each row and column are consecutive
       if 'x' not in [i for row in state for i in row] and all(is_consecutive(row) for row in state) and all(is_consecutive([state[i][j] for i in range(num_rows)]) for j in range(num_cols)):
           return actions


       # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique numbers
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   for number in available_numbers:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = str(number)
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the sum of the numbers in the topmost row, the rightmost column, and the diagonal from the top-left corner to the bottom-right corner
                       new_cost = sum(int(i) for i in new_state[0]) + sum(int(new_state[i][num_cols - 1]) for i in range(num_rows)) + sum(int(new_state[i][i]) for i in range(num_rows))
                       # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, number)], new_state, available_numbers - {number}))
   return None


def is_consecutive(lst):
   # Helper function to check if the numbers in a list are consecutive
   lst = [int(i) for i in lst]
   return sorted(lst) == list(range(min(lst), max(lst)+1))


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the minimum available number for each 'x' in the grid
   # This heuristic is admissible because it never overestimates the cost to reach the goal, as each 'x' must be replaced with at least one number from the available numbers
   # It's consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' with a number is the number itself, which is always greater than or equal to the minimum available number
   return sum(min(available_numbers) for i in state for j in i if j == 'x')


print(a_star())
