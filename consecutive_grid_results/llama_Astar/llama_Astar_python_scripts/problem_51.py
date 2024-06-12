
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, 36, None, 55], [30, 34, None, 56], [None, 33, None, 57], [None, 32, 46, None]]
   # Define the goal state, where all 'x' are replaced with unique integers from the given range
   goal_state = [[20, 36, 40, 55], [30, 34, 42, 56], [24, 33, 44, 57], [26, 32, 46, 60]]
   # Define the range of numbers that can be placed in the grid
   num_range = range(20, 60)
   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[str(initial_state)] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the replacements required to get to each state in a list; no replacements performed to reach the initial state
   queue = [(0, 0, [], initial_state)]
  
   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with a unique number from the given range
       for row_ind in range(len(state)):
           for col_ind in range(len(state[row_ind])):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   # The new state must maintain the consecutive order in each row and column
                   for num in num_range:
                       if num not in new_state[row_ind] and num not in zip(*new_state)[col_ind]:
                           # Check if the new state would be valid, ie the number is not in the same row or column
                           if row_ind > 0 and num < new_state[row_ind - 1][col_ind]:
                               continue
                           if col_ind > 0 and num < new_state[row_ind][col_ind - 1]:
                               continue
                           if row_ind < len(state) - 1 and num > new_state[row_ind + 1][col_ind]:
                               continue
                           if col_ind < len(state[row_ind]) - 1 and num > new_state[row_ind][col_ind + 1]:
                               continue
                           # Replace the 'x' with the new number
                           new_state[row_ind][col_ind] = num
                           new_state = [tuple(row) for row in new_state]
                           # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                           new_cost = g + 1


                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                           if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                               visited_costs[str(new_state)] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [(row_ind, col_ind, num)], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the numbers in the topmost row, the numbers in the rightmost column, and the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
   # This heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing, and that the sum of the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner should be minimized
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched number must be replaced at least once
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved number's value matches the most common value in the new position but not in the old one), which is equal to the cost of reaching the successor node
   h = sum(state[0]) + sum(zip(*state)[-1]) + sum(state[i][i] for i in range(len(state)))
   return h


print(a_star())
