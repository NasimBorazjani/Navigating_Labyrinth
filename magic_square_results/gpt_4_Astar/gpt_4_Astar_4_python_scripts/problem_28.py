
import heapq


def a_star():
   # Define the initial state of the grid, as a 3x3 tuple of strings
   initial_state = (('51', 'x', 'x'), ('x', 'x', 'x'), ('x', 'x', 'x'))
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   # The range of unique integers that can be used to replace 'x's in the grid
   numbers = set(str(i) for i in range(26, 66))
   # The sum of the numbers in the first column, second row, and the diagonal from the top right to the bottom left corner of the grid
   col_1_sum = 107
   row_1_sum = 124
   diagonal_sum = 108


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[initial_state] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state, numbers)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state, available_numbers = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is where all of the 'x's in the grid are replaced with unique integers such that the sum of the first column, second row, and the diagonal from the top right to the bottom left corner of the grid equal the given amounts
       if 'x' not in (cell for row in state for cell in row) and sum(int(cell) for cell in state[0]) == col_1_sum and sum(int(cell) for cell in state[1]) == row_1_sum and sum(int(state[i][2 - i]) for i in range(num_rows)) == diagonal_sum:
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
                       # The cost so far is the sum of the numbers in the grid, as the task is to minimize the sum of all of the numbers in the grid
                       new_cost = g + int(number)


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The new number must be removed from the set of available numbers
                           new_available_numbers = available_numbers - {number}
                           heapq.heappush(queue, (new_cost + heuristic(new_state, col_1_sum, row_1_sum, diagonal_sum), new_cost, actions + [(i, j, int(number))], new_state, new_available_numbers))
                   return None
   return None


def heuristic(state, col_1_sum, row_1_sum, diagonal_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the sum of the first column, second row, and the diagonal from the top right to the bottom left corner of the grid in the current state and the given amounts
   # The heuristic relaxes the constraints that the numbers in the grid must be unique and that the sum of the numbers in the grid must be minimized; ie It presumes we can add any number to the grid to reach the given sums
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of moving from one state to an adjacent state is the number added to the grid, which is always greater than or equal to 1, the decrease in the absolute difference between the sum of the first column, second row, and the diagonal from the top right to the bottom left corner of the grid in the current state and the given amounts
   h = 0
   h += abs(sum(int(cell) for cell in state[0]) - col_1_sum)
   h += abs(sum(int(cell) for cell in state[1]) - row_1_sum)
   h += abs(sum(int(state[i][2 - i]) for i in range(len(state))) - diagonal_sum)
   return h


print(a_star())
