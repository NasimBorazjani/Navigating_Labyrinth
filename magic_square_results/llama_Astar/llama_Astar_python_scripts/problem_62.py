
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, None, None, None], [40, 39, 32, 53], [46, None, 58, None], [None, None, 43, 51]]
   # Define the goal state, with the sums of the rows, columns, and diagonal
   goal_state = (None, 199, 194, None, 164, 210, None, 197)
   # Define the range of the integers that can be placed in the grid
   integer_range = range(30, 67)
   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[tuple(map(tuple, initial_state))] = 0
   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], initial_state)]
  
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state_to_goal(state) == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes placing a unique integer in each 'x' position
       for row_ind in range(len(state)):
           for col_ind in range(len(state[row_ind])):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   # Place a unique integer in the 'x' position
                   for integer in integer_range:
                       if integer not in new_state[row_ind] + new_state[row_ind + 1] + new_state[row_ind + 2] + new_state[row_ind + 3]:
                           new_state[row_ind][col_ind] = integer
                           new_state = [tuple(row) for row in new_state]
                           # The cost so far is the number of integers placed, as the task is to minimize the number of integers placed
                           new_cost = g + 1


                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(state_to_goal(new_state), goal_state), new_cost, actions + [(row_ind, col_ind, integer)], new_state))
                               # Remove the integer from the 'x' position
                               new_state[row_ind][col_ind] = None
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current state and the goal state
   # This heuristic relaxes the constraint that the integers can only be placed in the 'x' positions
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched integer must be placed at least once
   # It's consistent because moving an integer from one position to another reduces the heuristic cost of the successor node by a max of 2 (if the moved integer's difference with the goal is 2), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for row_ind in range(len(state)):
       for col_ind in range(len(state[row_ind])):
           if state[row_ind][col_ind] is not None:
               h += abs(state[row_ind][col_ind] - goal[row_ind * 2 + col_ind])
   return h


def state_to_goal(state):
   # Convert the state to the goal format, with the sums of the rows, columns, and diagonal
   goal = [None, sum(state[0]), sum(state[1]), None, sum(state[2]), sum(state[3]), None, sum(state[0]) + sum(state[1]) + sum(state[2]) + sum(state[3])]
   return tuple(goal)


print(a_star())
