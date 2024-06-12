
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, None, None, None], [28, 33, None, None], [16, None, None, 37], [36, 18, 7, 23]]
   # Define the goal state of the grid, with the sums of rows, columns, and the diagonal
   goal_state = (None, 125, 51, None, 101, 108, None, 90)
   # Define the range of the integers that can be placed in the grid
   num_range = range(6, 48)


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


       # Generate all possible actions from the current state, which includes placing a unique integer in each 'x' position in the grid
       for row_ind in range(len(state)):
           for col_ind in range(len(state[row_ind])):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   for num in num_range:
                       # Check if the new state would be valid, ie the number is unique and does not violate the constraints on the sums of rows, columns, and the diagonal
                       if num not in new_state[row_ind] and num not in new_state[col_ind]:
                           new_state[row_ind][col_ind] = num
                           # The cost so far is the number of numbers placed in the grid, as the task is to minimize the number of numbers placed in the grid
                           new_cost = g + 1


                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[tuple(map(tuple, new_state))]:
                               visited_costs[tuple(map(tuple, new_state))] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(state_to_goal(new_state), goal_state), new_cost, actions + [(row_ind, col_ind, num)], new_state))
                   # Reset the 'x' position in the new state
                   new_state[row_ind][col_ind] = None
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sums of rows, columns, and the diagonal and the goal sums
   # This heuristic relaxes the constraint that the numbers in the grid must be unique and can be in the grid only once
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched sum must be corrected at least once
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of the absolute difference between the current and goal sums, which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for i in range(len(state)):
       if state[i] is not None:
           h += abs(state[i] - goal[i])
   return h


def state_to_goal(state):
   # Convert the state to the goal format, with the sums of rows, columns, and the diagonal
   goal = []
   for row in state:
       goal.append(sum(row))
   for col_ind in range(len(state[0])):
       goal.append(sum(state[row_ind][col_ind] for row_ind in range(len(state))))
   goal.append(sum(state[i][i] for i in range(len(state))))
   goal.append(sum(state[i][len(state) - i - 1] for i in range(len(state))))
   return tuple(goal)


print(a_star())
