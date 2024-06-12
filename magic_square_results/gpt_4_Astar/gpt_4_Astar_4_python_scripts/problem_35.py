
import heapq


def a_star():
   # Define the initial state of the grid, as a 2d tuple
   initial_state = (('x', 'x', 'x'), (80, 48, 'x'), ('x', 'x', 'x'))
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   col_1_sum = 153
   row_1_sum = 186
   diagonal_sum = 188
   # The range of unique integers that can be used to replace 'x's
   available_numbers = set(range(40, 90))


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is where all 'x's have been replaced with unique integers such that the sum of column 1, row 1, and the diagonal from the top right to the bottom left corner of the grid equal the given amounts
       if all(cell != 'x' for row in state for cell in row) and sum(int(cell) for cell in state[1]) == row_1_sum and sum(int(state[i][1]) for i in range(num_rows)) == col_1_sum and sum(int(state[i][num_cols - 1 - i]) for i in range(num_rows)) == diagonal_sum:
           return actions


       # Generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   for number in available_numbers - set(int(cell) for row in state for cell in row if cell != 'x'):
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = number
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the sum of all of the numbers in the grid, as the task is to minimize the sum of all of the numbers in the grid
                       new_cost = g + number


                       # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, number)], new_state))
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the minimum available number for each remaining 'x' in the grid
   # This heuristic is admissible because it always opts for the action that fills the grid with the smallest available number, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a number is removed from the grid, or equal or less by at most the smallest available number (equal to the cost of reaching the successor node, ie one action) as the maximum number that can be added to the grid is the largest available number, which is always greater than the smallest available number. Thus h(n) can never be greater than c(n, n’)(equal to the smallest available number) + h(n’)
   h = 0
   # Get the smallest available number
   smallest_available_number = min(set(range(40, 90)) - set(int(cell) for row in state for cell in row if cell != 'x'))
   # Count the number of 'x's in the grid
   num_xs = sum(1 for row in state for cell in row if cell == 'x')
   h = smallest_available_number * num_xs
   return h


print(a_star())
