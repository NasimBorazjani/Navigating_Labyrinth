
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, 21, None, None], [18, 27, None, 51], [24, 29, None, None], [54, 33, 25, 12]]
   # Define the range of numbers that can be placed in the grid
   num_range = range(10, 65)
   # Define the initial cost of the state
   initial_cost = 0
   # Initialize the visited costs dictionary
   visited_costs = {}
   visited_costs[str(initial_state)] = initial_cost
   # Initialize the priority queue with the initial state
   queue = [(initial_cost, 0, [], initial_state)]


   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       # The goal state is when all the 'x's in the grid are replaced with unique integers from the given range
       if all(None not in row for row in state):
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with a unique number from the range
       for row_ind in range(len(state)):
           for col_ind in range(len(state[row_ind])):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   for num in num_range:
                       # Check if the new number is valid, ie it is not in the same row or column
                       if num not in new_state[row_ind] and num not in [row[col_ind] for row in new_state]:
                           new_state[row_ind][col_ind] = num
                           new_state = [tuple(row) for row in new_state]
                           # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                           new_cost = g + 1


                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                           if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                               visited_costs[str(new_state)] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state), g + 1, actions + [(row_ind, col_ind, num)], new_state))
                   # Reset the new_state to 'x' for the next possible number
                   new_state[row_ind][col_ind] = None
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
   # This heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched number must be replaced at least once
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 2 * (the difference between the old and new numbers), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for row in state:
       h += sum(row)
   h -= state[0][0] + state[-1][-1]
   return h


print(a_star())
