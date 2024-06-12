
import heapq


def a_star():
   # Define the initial state of the grid, the goal sums of the rows, columns, and diagonal, and the range of numbers that can be used to fill the grid
   initial_state = (('39', '47', 'x', 'x'), ('x', 'x', 'x', '40'), ('63', '82', '59', 'x'), ('x', '78', 'x', 'x'))
   goal_sums_rows = [None, 234, 271, None]
   goal_sums_cols = [None, 295, 200, None]
   goal_sum_diag = 248
   num_rows = 4
   num_cols = 4
   available_numbers = set(range(36, 93))


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
       if all(cell != 'x' for row in state for cell in row) and all(sum(int(cell) for cell in row if cell != 'x') == goal_sums_rows[i] or goal_sums_rows[i] is None for i, row in enumerate(state)) and all(sum(int(state[j][i]) for j in range(num_rows) if state[j][i] != 'x') == goal_sums_cols[i] or goal_sums_cols[i] is None for i in range(num_cols)) and sum(int(state[i][num_cols - i - 1]) for i in range(num_rows) if state[i][num_cols - i - 1] != 'x') == goal_sum_diag:
           return actions


       # Generate all possible actions from the current state, which includes replacing the next x in the grid with any of avaiable unique integers (all numbers in the range - numbers present in the current state) in the range 
       for i in range(num_rows):
           for j in range(num_cols):
               if state[i][j] == 'x':
                   for number in available_numbers - set(cell for row in state for cell in row if cell != 'x'):
                       # Generate the new state
                       new_state = [list(row[:]) for row in state]
                       new_state[i][j] = str(number)
                       new_state = tuple(tuple(row) for row in new_state)
                       # The cost so far is the sum of the numbers in the grid, as the task is to minimize the sum of all of the numbers in the grid
                       new_cost = g + number


                       # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                       if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                           visited_costs[new_state] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state, goal_sums_rows, goal_sums_cols, goal_sum_diag), new_cost, actions + [(i, j, number)], new_state))
                   break
           else:
               continue
           break
   return None


def heuristic(state, goal_sums_rows, goal_sums_cols, goal_sum_diag):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sums of the rows, columns, and diagonal and their goal sums
   # The heuristic relaxes the constraints that the numbers in the grid must be unique and that the sum of the numbers in the grid must be minimized, and presumes we can add any number to the grid to reach the goal sums
   # Thus the heuristic reports a lower estimate on the cost to reach the goal state and is admissible
   # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of adding a number to the grid is the number itself, which is always greater than or equal to 1, the decrease in the absolute difference between the current and goal sums of the rows, columns, and diagonal
   h = 0
   for i in range(len(state)):
       if goal_sums_rows[i] is not None:
           h += abs(sum(int(cell) for cell in state[i] if cell != 'x') - goal_sums_rows[i])
   for i in range(len(state[0])):
       if goal_sums_cols[i] is not None:
           h += abs(sum(int(state[j][i]) for j in range(len(state)) if state[j][i] != 'x') - goal_sums_cols[i])
   h += abs(sum(int(state[i][len(state) - i - 1]) for i in range(len(state)) if state[i][len(state) - i - 1] != 'x') - goal_sum_diag)
   return h


print(a_star())
