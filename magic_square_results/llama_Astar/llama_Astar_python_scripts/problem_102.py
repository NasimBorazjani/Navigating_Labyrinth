
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[44, None, None, None], [90, 52, None, 91], [None, 58, None, 62], [None, 80, None, None]]
   # Define the goal state, with the sums of the rows and columns
   goal_state = (None, 279, 306, None, 315, 234, None, 264)
   # Define the range of the integers that can be placed in the grid
   integer_range = range(36, 93)


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
                   # Place a unique integer in the current 'x' position
                   new_state[row_ind][col_ind] = integer_range.pop(0)
                   new_state = [tuple(row) for row in new_state]
                   # The cost so far is the number of integers placed, as the task is to minimize the number of integers placed to reach the goal state
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(state_to_goal(new_state), goal_state), g + 1, actions + [(row_ind, col_ind, new_state[row_ind][col_ind])], new_state))
   return None


def state_to_goal(state):
   # Convert the state to the goal format, with the sums of the rows and columns
   goal = [None] * 8
   for row_ind in range(len(state)):
       goal[row_ind * 2] = sum(state[row_ind])
   for col_ind in range(len(state[0])):
       goal[col_ind * 2 + 1] = sum(state[row_ind][col_ind] for row_ind in range(len(state)))
   goal[-1] = sum(state[row_ind][col_ind] for row_ind in range(len(state)) for col_ind in range(len(state[0])) if row_ind != col_ind)
   return tuple(goal)


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the sums of the rows and columns in the current state and the goal state
   # This heuristic relaxes the constraint that the integers must be unique and can be placed in any order
   # It is admissible because it never overestimates the cost to reach the goal, as each mismatched sum must be corrected by a unique integer
   # It's consistent because moving a unique integer from one position to another reduces the heuristic cost of the successor node by a max of 1 (if the moved integer's sum matches the goal sum for that row or column), which is equal to the cost of reaching the successor node
   h = 0
   for i in range(len(state)):
       h += abs(state[i] - goal[i * 2])
   for i in range(len(state[0])):
       h += abs(sum(state[row_ind][i] for row_ind in range(len(state))) - goal[i * 2 + 1])
   h += abs(sum(state[row_ind][col_ind] for row_ind in range(len(state)) for col_ind in range(len(state[0])) if row_ind != col_ind) - goal[-1])
   return h


print(a_star())
