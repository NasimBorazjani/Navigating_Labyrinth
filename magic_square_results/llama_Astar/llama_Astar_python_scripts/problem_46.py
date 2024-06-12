
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, None, None, None], [None, 37, None, 41], [48, None, None, None], [49, None, 46, 38]]
   # Define the goal state of the grid, with the sums of rows, columns, and diagonal
   goal_state = (None, 151, 189, None, 180, 176, None, 184)
   # Define the range of the integers that can be placed in the grid
   num_range = range(35, 62)


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[tuple(map(tuple, initial_state))] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state_to_goal(state) == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes placing a unique integer from the range in any of the 'x' positions in the grid
       for row_ind in range(len(state)):
           for col_ind in range(len(state[row_ind])):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   for num in num_range:
                       new_state[row_ind][col_ind] = num
                       # The cost so far is the number of unique integers placed in the grid, as the task is to minimize the number of unique integers required
                       new_cost = g + 1


                       # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                       if new_state not in visited_costs or new_cost < visited_costs[tuple(map(tuple, new_state))]:
                           visited_costs[tuple(map(tuple, new_state))] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(state_to_goal(new_state), goal_state), new_cost, actions + [(row_ind, col_ind, num)], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the sums of rows, columns, and diagonal in the current state and the goal state
   # This heuristic relaxes the constraint that the unique integers must be unique, as it does not take into account the uniqueness of the integers
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched sum must be corrected at least once
   # It's consistent because moving a unique integer from one position to another results in a decrease in the heuristic cost of the successor node by a max of 2 (if the moved integer's sum matches the goal sum for a row, column, or diagonal but not in the old state), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for i in range(len(state)):
       if state[i] is not None:
           h += abs(state[i] - goal[i])
   return h


def state_to_goal(state):
   # Convert the state to the goal format by calculating the sums of rows, columns, and diagonal
   goal = []
   for row in state:
       goal.append(sum(row))
   goal.append(sum(state[i][i] for i in range(len(state))))
   goal.append(sum(state[i][len(state) - 1 - i] for i in range(len(state))))
   return tuple(goal)


print(a_star())
