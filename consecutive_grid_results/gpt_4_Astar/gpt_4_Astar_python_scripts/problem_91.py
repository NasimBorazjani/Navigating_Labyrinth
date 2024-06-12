
import heapq
import numpy as np


def a_star():
   # Define the initial state of the grid, as a 2d tuple
   initial_state = (('x', 'x', '38', 'x'), ('x', 'x', '33', 'x'), ('16', 'x', '28', '47'), ('14', 'x', 'x', '52'))
   # Define the range of numbers that can be used to replace the 'x's
   numbers_range = set(range(14, 70))
   # Define the numbers that are already in the grid
   numbers_in_grid = set([int(number) for row in initial_state for number in row if number != 'x'])
   # Define the numbers that are available to replace the 'x's
   available_numbers = numbers_range - numbers_in_grid
   # Define the size of the grid
   grid_size = 4


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state, available_numbers)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state, available_numbers = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is where all the 'x's have been replaced with unique integers from the given range, and the numbers in each row and column are in strictly increasing or decreasing order
       if 'x' not in [number for row in state for number in row]:
           return actions


       # Generate all possible actions from the current state, which includes replacing the next 'x' in the grid with any of the available unique integers
       for number in available_numbers:
           # Find the next 'x' in the grid
           for i in range(grid_size):
               for j in range(grid_size):
                   if state[i][j] == 'x':
                       # Replace the 'x' with the current number
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = str(number)
                       new_state = tuple(tuple(row) for row in new_state)
                       # Check if the new state is valid, ie the numbers in each row and column are in strictly increasing or decreasing order
                       if all(is_increasing_or_decreasing([int(number) for number in row if number != 'x']) for row in new_state) and all(is_increasing_or_decreasing([int(new_state[i][j]) for i in range(grid_size) if new_state[i][j] != 'x']) for j in range(grid_size)):
                           # The cost so far is the sum of the numbers in the topmost row, the rightmost column, and the main diagonal
                           new_cost = sum(int(number) for number in new_state[0] if number != 'x') + sum(int(new_state[i][grid_size - 1]) for i in range(grid_size) if new_state[i][grid_size - 1] != 'x') + sum(int(new_state[i][i]) for i in range(grid_size) if new_state[i][i] != 'x')
                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, number)], new_state, available_numbers - {number}))
                           break
               else:
                   continue
               break
   return None


def is_increasing_or_decreasing(numbers):
   # Check if a list of numbers is in strictly increasing or decreasing order
   return all(numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1)) or all(numbers[i] > numbers[i + 1] for i in range(len(numbers) - 1))


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the number of 'x's in the grid
   # The heuristic relaxes the constraints that the numbers in each row and column must be in strictly increasing or decreasing order, and that the sum of the numbers in the topmost row, the rightmost column, and the main diagonal must be minimized; ie it presumes we can replace any 'x' with any available number
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' with a number is the number itself, which is always greater than or equal to 1, the decrease in the number of 'x's
   return sum(1 for row in state for number in row if number == 'x')


print(a_star())
