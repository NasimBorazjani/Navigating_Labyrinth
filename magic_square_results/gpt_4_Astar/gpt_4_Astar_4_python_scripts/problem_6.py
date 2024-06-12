
import heapq


def a_star():
   # Define the initial state of the grid, as a 2d tuple
   initial_state = (('x', 20, 'x'), ('x', 'x', 'x'), ('x', 'x', 33))
  
   # Encoding other variables given in the problem statement
   num_rows = 3
   num_cols = 3
   # The range of unique integers that can be used to replace 'x's in the grid
   available_numbers = set(range(19, 44))
   # The sum of the numbers in the grid that are not 'x'
   initial_sum = sum(int(cell) for row in initial_state for cell in row if cell != 'x')
   # The numbers in the range that are already in the grid
   initial_numbers = set(int(cell) for row in initial_state for cell in row if cell != 'x')
   # The numbers in the range that are not in the grid
   initial_available_numbers = available_numbers - initial_numbers


   visited_costs = {}
   visited_costs[initial_state] = initial_sum


   queue = []
   # No actions taken in the initial state
   heappush(queue, (0, initial_sum, [], initial_state, initial_available_numbers))


   while queue:
       _, g, actions, state, available_numbers = heapq.heappop(queue)


       # If the state has no remaining unknown numbers, ie 'x', check if it is a goal state
       if 'x' not in state:
           # The goal state is where the sum of column 1, row 1, and the diagonal from the top right to the bottom left corner of the grid equal the given amounts
           if sum(int(state[i][1]) for i in range(num_rows)) == 82 and sum(int(state[1][j]) for j in range(num_cols)) == 82 and sum(int(state[i][num_cols - 1 - i]) for i in range(num_rows)) == 96:
               return actions


       # If the state has at least 1 remaining unknown number, ie 'x', generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   for number in available_numbers:
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = number
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the sum of all of the numbers in the grid, as the task is to minimize the sum of all of the numbers in the grid
                       new_cost = g + number


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           # The new number must be removed from the set of available numbers
                           new_available_numbers = available_numbers - {number}
                           heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, number)], new_state, new_available_numbers))
                   # After generating all possible actions from the current state, break the loop to avoid generating duplicate states
                   break
           else:
               continue
           break
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the minimum remaining numbers that can be added to the grid to replace the 'x's
   # This heuristic is admissible because it always underestimates the cost to reach the goal state, as it presumes we can always add the smallest remaining numbers to the grid, which is not always possible due to the constraints on the sum of the rows, columns, and diagonal
   # The heuristic is consistent because the estimated cost of the next node is higher if a number is added to the grid, or equal or less by at most the smallest remaining number (equal to the cost of reaching the successor node, ie the number added to the grid) as the minimum number that can be added to the grid is the smallest remaining number, which is exactly the number added to the grid in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to the smallest remaining number) + h(n’)
   h = 0
   # The minimum remaining numbers that can be added to the grid to replace the 'x's
   min_remaining_numbers = sorted(range(19, 44), reverse=True)[:sum(1 for row in state for cell in row if cell == 'x')]
   h = sum(min_remaining_numbers)
   return h


print(a_star())
