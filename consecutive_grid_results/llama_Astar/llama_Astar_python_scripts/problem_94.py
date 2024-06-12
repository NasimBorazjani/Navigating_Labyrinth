
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' replaced by None
   initial_state = [[91, 57, None, 45], [41, 49, None, None], [None, None, 49, None], [None, 46, 47, 73]]
   # Define the range of numbers
   num_range = range(39, 94)
   # Define the goal state, where all 'x' are replaced by unique numbers from the range
   goal_state = [[None for _ in row] for row in initial_state]
   # Define the initial cost as 0
   initial_cost = 0
   # Initialize the visited costs dictionary
   visited_costs = {}
   visited_costs[tuple(tuple(row) for row in initial_state)] = initial_cost
   # Initialize the priority queue with the initial state
   queue = [(initial_cost, initial_cost, [], initial_state)]


   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with a unique number from the range
       for row_ind, row in enumerate(state):
           for col_ind, cell in enumerate(row):
               if cell is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   # Replace the 'x' with a unique number from the range
                   new_state[row_ind][col_ind] = next(num_range)
                   new_state = [tuple(row) for row in new_state]
                   # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [(row_ind, col_ind, new_state[row_ind][col_ind])], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the numbers in the current state and the goal state
   # This heuristic relaxes the constraint that the numbers in the grid must be strictly increasing or decreasing, and that the sum of the numbers in the topmost row, the rightmost column, and the diagonal must be minimized
   # It is admissible because it never overestimates the cost to reach the goal, as each difference between the current state and the goal state must be at least 0
   # It's consistent because moving a number from one state to another reduces the heuristic cost of the successor node by a max of 1 (if the moved number is the same in the current state and the goal state), which is equal to the cost of reaching the successor node
   h = 0
   for row_ind, row in enumerate(state):
       for col_ind, cell in enumerate(row):
           if cell is not None:
               goal_cell = goal[row_ind][col_ind]
               if goal_cell is not None:
                   h += abs(cell - goal_cell)
   return h


print(a_star())
