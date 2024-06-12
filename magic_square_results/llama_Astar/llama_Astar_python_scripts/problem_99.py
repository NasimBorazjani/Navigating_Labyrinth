
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, None, None, 67], [62, None, 32, 77], [66, None, 34, None], [None, None, 73, 35]]
   # Define the goal state, with the sums of rows and columns and the diagonal
   goal_state = (None, 239, 192, None, 220, 184, None, 199)
   # Define the range of the integers that can be placed in the grid
   num_range = range(30, 87)


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


       # Generate all possible actions from the current state, which includes placing a unique integer in each 'x' position
       for row_ind in range(len(state)):
           for col_ind in range(len(state[row_ind])):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   for num in num_range:
                       # Check if the new state would be valid, ie placing the number in the current position does not violate the constraints on the sums of rows, columns, and the diagonal
                       if state_to_goal(new_state, row_ind, col_ind, num) == goal_state:
                           # Place the number in the current position
                           new_state[row_ind][col_ind] = num
                           new_state = [tuple(row) for row in new_state]
                           # The cost so far is the number of actions taken, as the task is to minimize the number of actions required to fill the grid with the unique integers
                           new_cost = g + 1


                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                               visited_costs[new_state] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), g + 1, actions + [(row_ind, col_ind, num)], new_state))
   return None


def state_to_goal(state, row_ind=None, col_ind=None, num=None):
   # Convert the state to the goal state representation
   goal_state = []
   for row in range(len(state)):
       for col in range(len(state[row])):
           if state[row][col] is None:
               goal_state.append(None)
           else:
               goal_state.append(sum(state[row][col:]) + sum(state[row+1:], []))
   if row_ind is not None and col_ind is not None and num is not None:
       goal_state[row_ind * 4 + col_ind] = num
   return tuple(goal_state)


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current state and the goal state
   # This heuristic relaxes the constraint that the unique integers must be unique, as it does not take into account the uniqueness of the integers
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be a non-negative number
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 2 (if the moved number is the same in the current state and goal state), which is equal to the cost of reaching the successor node
   h = 0
   for i in range(len(state)):
       for j in range(len(state[i])):
           if state[i][j] is not None:
               h += abs(state[i][j] - goal[i * 4 + j])
   return h


print(a_star())
