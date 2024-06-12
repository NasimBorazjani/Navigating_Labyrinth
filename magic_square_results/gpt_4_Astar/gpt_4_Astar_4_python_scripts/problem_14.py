
import heapq


def a_star():
   # Define the initial state of the grid, the range of unique integers, and the sums of the specified row, column, and diagonal
   initial_state = (('x', '32', 'x'), ('38', 'x', 'x'), ('x', 'x', 'x'))
   num_range = set(str(i) for i in range(28, 58))
   row_1_sum = 134
   col_1_sum = 143
   diag_sum = 131
   num_rows = 3
   num_cols = 3


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
       # The goal state is where all of the numbers in the grid are unique integers in the given range, and the sum of the specified row, column, and diagonal equal the given amounts
       if all(cell != 'x' for row in state for cell in row) and sum(int(cell) for cell in state[1]) == row_1_sum and sum(int(state[i][1]) for i in range(num_rows)) == col_1_sum and sum(int(state[i][num_rows - 1 - i]) for i in range(num_rows)) == diag_sum:
           return actions


       # Generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   for num in num_range - set(cell for row in state for cell in row if cell != 'x'):
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = num
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the sum of all of the numbers in the grid, as the task is to minimize the sum of all of the numbers in the grid
                       new_cost = g + int(num)


                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state, num_range), new_cost, actions + [(i, j, int(num))], new_state))
                   return None
   return None


def heuristic(state, num_range):
   # An admissible and consistent heuristic for this problem is the sum of the smallest available numbers that can replace the remaining 'x's in the grid
   # This heuristic is admissible because it always opts for the action that results in the lowest sum of all of the numbers in the grid, ensuring it never overestimates the cost to reach the goal
   # The heuristic is consistent as the estimated cost of the next node is higher if a number is removed from the grid, or equal or less by at most the smallest available number (equal to the cost of reaching the successor node, ie the number added to the grid) as the maximum number that can be added to the grid is the largest available number, which is always greater than the smallest available number used in the heuristic. Thus h(n) can never be greater than c(n, n’)(equal to the smallest available number) + h(n’)
   h = 0
   available_nums = sorted(int(num) for num in num_range - set(cell for row in state for cell in row if cell != 'x'))
   for i in range(sum(1 for row in state for cell in row if cell == 'x')):
       h += available_nums[i]
   return h


print(a_star())
