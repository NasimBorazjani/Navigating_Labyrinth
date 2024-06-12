
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, None, None, 40], [34, 37, None, None], [None, 43, None, 22], [None, None, None, 47]]
   # Define the goal state of the grid, with the sums of rows and columns
   goal_state = (None, 137, 162, None, 141, 135, None, 151)
   # Define the range of numbers that can be used to replace 'x's
   num_range = range(22, 54)


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
                       if new_state_to_tuple(new_state) not in visited_costs or new_cost < visited_costs[new_state_to_tuple(new_state)]:
                           visited_costs[new_state_to_tuple(new_state)] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [(row_ind, col_ind, num)], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current state and the goal state
   # This heuristic relaxes the constraint that the sum of the numbers in the grid must be as low as possible
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be a non-negative number
   # It's consistent because moving a number from one position to another reduces the heuristic cost of the successor node by a max of 2 (if the moved number's difference with the goal is 2), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for row_ind in range(len(state)):
       for col_ind in range(len(state[row_ind])):
           if state[row_ind][col_ind] is not None:
               h += abs(state[row_ind][col_ind] - goal[row_ind * 2 + col_ind])
   return h


def state_to_goal(state):
   # Define the goal state of the grid, with the sums of rows and columns
   return (None, sum(state[0]), sum(state[1]), None, sum(state[2]), sum(state[3]), None, sum(state[0]) + sum(state[2]) - sum(state[1]) - sum(state[3]))


def new_state_to_tuple(state):
   # Convert the new state to a tuple to be used as a key in the visited_costs dictionary
   return tuple(tuple(row) for row in state)


print(a_star())
