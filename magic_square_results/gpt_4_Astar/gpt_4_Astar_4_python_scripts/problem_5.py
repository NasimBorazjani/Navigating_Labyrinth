
import heapq


def a_star():
   # Define the initial state of the grid, as a 2d tuple
   initial_state = (('x', 'x', 'x'), ('x', 'x', 'x'), ('22', 'x', 'x'))
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   # The range of unique integers that can be used to replace 'x's in the grid
   available_numbers = set(str(i) for i in range(20, 40))
   # The sum of the specified row, column, and diagonal
   target_sum = 82


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
       # The goal state is where all 'x's in the grid have been replaced with unique integers such that the sum of the specified row, column, and diagonal equals the given amounts
       if all(cell != 'x' for row in state for cell in row) and sum(int(cell) for cell in state[1]) == target_sum and sum(int(state[i][i]) for i in range(num_rows)) == target_sum and sum(int(state[i][num_cols - i - 1]) for i in range(num_rows)) == target_sum:
           return actions


       # Generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   for number in available_numbers - set(cell for row in state for cell in row if cell != 'x'):
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = number
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the sum of all of the numbers in the grid, as the task is to minimize the sum of all of the numbers in the grid
                       new_cost = g + int(number)


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state, target_sum), new_cost, actions + [(i, j, int(number))], new_state))
   return None


def heuristic(state, target_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the sum of the specified row, column, and diagonal and the target sum
   # The heuristic relaxes the constraints that the numbers in the grid must be unique and that the sum of the specified row, column, and diagonal must equal the target sum; ie It presumes we can replace any 'x' in the grid with any number in the range
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' in the grid with a number is the number itself, which is always greater than or equal to 20, the decrease in the absolute difference between the sum of the specified row, column, and diagonal and the target sum
   h = 0
   # When calculating the sum of rows, columns, or diagonal of an intermediate state, first convert any element of the grid equal to 'x' to a 0, to avoid these error "ValueError: invalid literal for int() with base 10: 'x'" and "TypeError: unsupported operand type(s) for +: 'int' and 'str'"
   h += abs(sum(int(cell) if cell != 'x' else 0 for cell in state[1]) - target_sum)
   h += abs(sum(int(state[i][i]) if state[i][i] != 'x' else 0 for i in range(num_rows)) - target_sum)
   h += abs(sum(int(state[i][num_cols - i - 1]) if state[i][num_cols - i - 1] != 'x' else 0 for i in range(num_rows)) - target_sum)
   return h


print(a_star())
