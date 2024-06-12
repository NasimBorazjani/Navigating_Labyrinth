
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' replaced by None
   initial_state = [[25, None, None, 57], [39, 45, 56, None], [43, None, 58, None], [46, None, 65, 69]]
   # Define the range of numbers
   num_range = range(21, 71)
   # Define the goal state, where all 'x' are replaced by unique numbers from the range
   goal_state = [[i for i in row if i is not None] for row in initial_state]
   # Define the initial cost as 0
   initial_cost = 0
   # Initialize the visited costs dictionary
   visited_costs = {}
   visited_costs[tuple(tuple(row) for row in initial_state)] = initial_cost
   # Initialize the priority queue with the initial state
   queue = [(0, 0, [], initial_state)]


   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with a unique number from the range
       for row_ind in range(len(state)):
           for col_ind in range(len(state[row_ind])):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   new_state[row_ind][col_ind] = next(num for num in num_range if num not in new_state[row_ind])
                   new_state = [tuple(row) for row in new_state]
                   # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [(row_ind, col_ind, new_state[row_ind][col_ind])], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the numbers in the topmost row, the numbers in the rightmost column, and the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
   # This heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched number must be replaced at least once
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved number is the same in the new position), which is equal to the cost of reaching the successor node
   h = 0
   h += sum(state[0])
   h += sum(state[i][-1] for i in range(len(state)))
   h += sum(state[i][i] for i in range(len(state)))
   return h


print(a_star())
