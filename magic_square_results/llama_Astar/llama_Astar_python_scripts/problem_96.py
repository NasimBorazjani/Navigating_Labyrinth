
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, None, None, None], [None, 52, 20, None], [41, 13, None, None], [54, None, 16, 11]]
   # Define the goal state of the grid, with the sums of rows, columns, and diagonal
   goal_state = (None, 148, 109, None, None, 105, None, None, None, 115, None, None, 134)
   # Define the range of integers that can be used to replace 'x's
   num_range = range(11, 63)


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


       # Generate all possible actions from the current state, which includes replacing an 'x' with a unique integer from the range
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
                       if new_state_to_tuple(new_state) not in visited_costs or new_cost < visited_costs[new_state_to_tuple(new_state)]:
                           visited_costs[new_state_to_tuple(new_state)] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [(row_ind, col_ind, num)], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current state and the goal state
   # This heuristic relaxes the constraint that the sum of the numbers in the grid must be as low as possible
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be a non-negative number
   # It's consistent because moving a number from one position to another results in a decrease in the heuristic cost of the successor node by a max of 2 (if the moved number is the same in the current state and goal state), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for row_ind in range(len(state)):
       for col_ind in range(len(state[row_ind])):
           # Calculate the absolute difference between the current state and the goal state
           h += abs(state[row_ind][col_ind] - goal[row_ind * len(state) + col_ind])
   return h


def state_to_goal(state):
   # Convert the state to the goal format
   return tuple(sum(row[i] for row in state) if i % len(state) != 0 else None for i in range(len(state) * len(state[0])))


def new_state_to_tuple(new_state):
   # Convert the new state to a tuple for dictionary key
   return tuple(tuple(row) for row in new_state)


print(a_star())
