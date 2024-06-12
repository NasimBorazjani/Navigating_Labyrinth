
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[48, None, None, None], [54, None, None, None], [None, 64, 44, 83], [82, 68, 51, None]]
   # Define the goal state, with the sums of rows and columns and the diagonal
   goal_state = (None, 267, 236, None, 270, 234, None, 301)
   # Define the range of the integers that can be placed in the grid
   num_range = range(41, 93)


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


       # Generate all possible actions from the current state, which includes placing a unique integer from the range in any of the 'x' positions in the grid
       for row_ind in range(len(state)):
           for col_ind in range(len(state[row_ind])):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   for num in num_range:
                       # Check if the new state would be valid, ie the number is not already in the row or column
                       if num not in new_state[row_ind] and num not in list(zip(*new_state))[col_ind]:
                           new_state[row_ind][col_ind] = num
                           new_state = [tuple(row) for row in new_state]
                           # The cost so far is the number of actions made, as the task is to minimize the number of actions required to fill the grid
                           new_cost = g + 1


                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                           if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                               visited_costs[str(new_state)] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), g + 1, actions + [(row_ind, col_ind, num)], new_state))
                   # Reset the 'x' position in the grid
                   new_state[row_ind][col_ind] = None
   return None


def state_sums(state):
   # Calculate the sums of rows and columns and the diagonal of the current state
   sums = [sum(row) for row in state]
   sums.append(sum(list(zip(*state))[0]) + list(zip(*state))[1][2] - list(zip(*state))[1][0])
   return tuple(sums)


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the sums of rows and columns and the diagonal in the current state and the goal state
   # This heuristic relaxes the constraint that the sums of rows and columns and the diagonal must be equal in the goal state
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched sum must be adjusted by a positive amount
   # It's consistent because moving a number from one position to another results in a decrease in the heuristic cost of the successor node by a max of 2 (if the moved number is part of the mismatched sum), which is equal to the cost of reaching the successor node
   h = 0
   for s, g in zip(state_sums(state), goal):
       if s != g:
           h += abs(s - g)
   return h


print(a_star())
