
import heapq


def a_star():
   # Define the initial state of the grid, the range of unique integers, and the sums of the specified rows, columns, and diagonal
   initial_state = (('47', 'x', 'x'), ('x', 'x', 'x'), ('x', 'x', 'x'))
   num_rows = 3
   num_cols = 3
   unique_integers = set(str(i) for i in range(26, 66))
   col_1_sum = 93
   row_1_sum = 135
   diagonal_sum = 106


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = []
   # No actions taken in the initial state
   heappush(queue, (0, 0, [], initial_state))


   while queue:
       _, g, actions, state = heappop(queue)


       # If the state has no remaining unknown numbers, ie 'x', check if the sums of the specified rows, columns, and diagonal equal the given amounts
       if 'x' not in state:
           # Convert the elements of the grid to integers to calculate the sums
           state_int = [[int(cell) for cell in row] for row in state]
           if sum(state_int[1]) == row_1_sum and sum(row[1] for row in state_int) == col_1_sum and sum(state_int[i][2 - i] for i in range(num_rows)) == diagonal_sum:
               return actions


       # If the state has at least 1 remaining unknown number, ie 'x', generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   for number in unique_integers - set(cell for row in state for cell in row):
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = number
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the sum of all of the numbers in the grid, as the task is to minimize the sum of all of the numbers in the grid
                       new_cost = g + int(number)


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           h = heuristic(state, unique_integers)
                           # In the problem statement the grid is indexed starting from 0, thus must add 1 to the bucket_ind
                           heappush(queue, (new_cost + h, new_cost, actions + [(i, j, int(number))], new_state))
                   # After replacing an 'x' with a number, break the loop to avoid replacing multiple 'x's in one action
                   break
           else:
               continue
           break
   return None




def heuristic(state, unique_integers):
   # An admissible and consistent heuristic for this problem is the sum of the smallest remaining unique integers that can replace the remaining 'x's in the grid
   # The heuristic relaxes the constraints that the sums of the specified rows, columns, and diagonal must equal the given amounts; ie It presumes we can replace the 'x's with any of the remaining unique integers
   # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' with a number is the number itself, which is always greater than or equal to the smallest remaining unique integer, the decrease in the heuristic estimate
   remaining_numbers = sorted(int(number) for number in unique_integers - set(cell for row in state for cell in row))
   return sum(remaining_numbers[:sum(row.count('x') for row in state)])


print(a_star())
