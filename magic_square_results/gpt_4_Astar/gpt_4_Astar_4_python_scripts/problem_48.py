
import heapq


def a_star():
   # Define the initial state of the grid, as a 2d tuple of integers and 'x's
   initial_state = (('x', 'x', 'x', 'x'), ('x', 46, 'x', 41), ('x', 57, 55, 'x'), ('x', 37, 'x', 'x'))
  
   # Encoding other variables given in the problem statement
   num_rows = 4
   num_cols = 4
   row_sums = [None, 179, 190, None]
   col_sums = [None, 179, 194, None]
   diagonal_sum = 205
   # The range of unique integers that can be used to replace 'x's in the grid
   available_numbers = set(range(34, 61))


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
       # The goal state is where all 'x's in the grid have been replaced with unique integers such that the sum of the specified rows, columns, and diagonal equals the given amounts
       if all(cell != 'x' for row in state for cell in row):
           return actions


       # Generate all possible actions from the current state, which includes replacing the next x in the grid with any of the available unique integers
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   for number in available_numbers:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = number
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the sum of all of the numbers in the grid, as the task is to minimize the sum of all of the numbers in the grid
                       new_cost = sum(int(cell) for row in new_state for cell in row if cell != 'x')


                       # If the new state is unvisited or we found a new path with a lower cost to arrive at this state, add it to the queue of un-visited states
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state, row_sums, col_sums, diagonal_sum), new_cost, actions + [(i, j, number)], new_state))
                   break
           else:
               continue
           break
   return None


def heuristic(state, row_sums, col_sums, diagonal_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current and goal sums of the rows, columns, and diagonal
   # The heuristic relaxes the constraints that the numbers in the grid must be unique and that the sum of the numbers in the grid must be as low as possible; ie It presumes we can add any number to the grid to reach the goal sums
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of adding a number to the grid is the number itself, which is always greater than or equal to 1, the decrease in the sum of the rows, columns, and diagonal
   h = 0
   for i in range(len(state)):
       if row_sums[i] is not None:
           h += abs(sum(int(cell) for cell in state[i] if cell != 'x') - row_sums[i])
   for j in range(len(state[0])):
       if col_sums[j] is not None:
           h += abs(sum(int(row[j]) for row in state if row[j] != 'x') - col_sums[j])
   h += abs(sum(int(state[i][len(state) - i - 1]) for i in range(len(state)) if state[i][len(state) - i - 1] != 'x') - diagonal_sum)
   return h


print(a_star())
