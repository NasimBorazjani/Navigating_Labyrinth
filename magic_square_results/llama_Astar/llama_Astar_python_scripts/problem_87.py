
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[72, 76, 68, 69], [56, None, None, None], [49, None, None, 43], [None, None, 61, None]]
   # Define the goal state, with the sums of the rows and columns
   goal_state = (None, 258, 247, None, 233, 237, None, 242)
   # Define the range of the numbers that can be in the grid
   num_range = range(37, 84)


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[str(initial_state)] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state_sums(state) == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with a number from the range
       for row_ind in range(len(state)):
           for col_ind in range(len(state[row_ind])):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   for num in num_range:
                       new_state[row_ind][col_ind] = num
                       # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                       new_cost = g + 1


                       # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                       if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                           visited_costs[str(new_state)] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [(row_ind, col_ind, num)], new_state))
   return None


def state_sums(state):
   # Calculate the sums of the rows and columns of the state
   sums = [None] * 8
   for row_ind in range(len(state)):
       sums[row_ind * 2] = sum(state[row_ind])
   for col_ind in range(len(state[0])):
       sums[col_ind * 2 + 1] = sum(state[row_ind][col_ind] for row_ind in range(len(state)))
   sums[-1] = sum(state[row_ind][col_ind] for row_ind in range(len(state)) for col_ind in range(len(state[row_ind])) if row_ind != col_ind)
   return tuple(sums)


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the sums of the rows and columns in the current state and the goal state
   # This heuristic relaxes the constraint that the sums of the rows and columns must be equal in the goal state
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be a non-negative number
   # It's consistent because moving a number from one cell to another results in a decrease in the heuristic cost of the successor node by a max of 2 (if the moved number is part of the sum that is different in the current state and goal state), which is equal to the cost of reaching the successor node
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] is not None:
               h += abs(state_sums(state)[i * 2 + j % 2] - goal[i * 2 + j % 2])
   return h


print(a_star())