
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' replaced by None
   initial_state = [[85, 73, 59, None], [None, None, 66, 70], [None, 59, None, None], [40, 41, 79, 82]]
   # Define the range of numbers
   num_range = range(31, 87)
   # Define the goal state, where all 'x' are replaced by unique numbers from the range
   goal_state = [[None for _ in range(4)] for _ in range(4)]
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
       for row_ind in range(4):
           for col_ind in range(4):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   # Choose a unique number from the range
                   new_num = num_range.pop(0)
                   # Replace the 'x' with the chosen number
                   new_state[row_ind][col_ind] = new_num
                   new_state = [tuple(row) for row in new_state]
                   # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(state, goal_state), g + 1, actions + [(row_ind, col_ind, new_num)], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the numbers in the current state and the goal state
   # This heuristic relaxes the constraint that the numbers in the grid must be strictly increasing or decreasing, and that the sum of the top row, rightmost column, and diagonal must be minimized
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be a non-negative number
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 2 (if the moved number is the same in the current state and goal state), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for row_ind in range(4):
       for col_ind in range(4):
           if state[row_ind][col_ind] is not None:
               h += abs(state[row_ind][col_ind] - goal[row_ind][col_ind])
   return h


print(a_star())
