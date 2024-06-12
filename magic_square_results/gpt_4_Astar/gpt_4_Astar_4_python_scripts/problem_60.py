
import heapq


def a_star():
   # Define the initial state of the grid, the range of unique integers, and the sums of the rows, columns, and diagonal
   initial_state = (('45', '53', 'x', 'x'), ('x', 'x', 'x', 'x'), ('47', 'x', 'x', 'x'), ('35', 'x', '52', 'x'))
   unique_integers = set(str(i) for i in range(23, 55))
   row_sums = [None, 166, 165, None]
   col_sums = [None, 173, 166, None]
   diagonal_sum = 131


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
       # The goal state is where all of the 'x's in the grid are replaced with unique integers such that the sum of the specified rows, columns, and diagonal equals the given amounts
       if all(cell != 'x' for row in state for cell in row):
           # Check if the sums of the rows, columns, and diagonal in the current state match the given sums
           if all(sum(int(cell) for cell in row if cell != 'x') == row_sum for row, row_sum in zip(state, row_sums) if row_sum is not None) and \
              all(sum(int(state[i][j]) for i in range(4) if state[i][j] != 'x') == col_sum for j, col_sum in enumerate(col_sums) if col_sum is not None) and \
              sum(int(state[i][3 - i]) for i in range(4) if state[i][3 - i] != 'x') == diagonal_sum:
               return actions


       # Generate all possible actions from the current state, which includes replacing the next x in the grid with any of the available unique integers
       for i in range(4):
           for j in range(4):
               if state[i][j] == 'x':
                   for num in unique_integers - set(cell for row in state for cell in row if cell != 'x'):
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = num
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the sum of all of the numbers in the grid, as the task is to minimize the sum of all of the numbers in the grid
                       new_cost = g + int(num)


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state), new_cost, actions + [(i, j, int(num))], new_state))
                   break
           else:
               continue
           break
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the minimum available unique integers that can replace the remaining 'x's in the grid
   # The heuristic relaxes the constraints that the sum of the rows, columns, and diagonal must equal the given amounts and presumes we can replace the 'x's with any of the available unique integers
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of replacing an 'x' with a unique integer is the value of the integer, which is always greater than or equal to the minimum available unique integer, the decrease in the heuristic estimate
   return sum(int(num) for num in sorted(set(str(i) for i in range(23, 55)) - set(cell for row in state for cell in row if cell != 'x'))[:sum(1 for row in state for cell in row if cell == 'x')])


print(a_star())
