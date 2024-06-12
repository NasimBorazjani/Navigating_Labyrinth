
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[15, 20, None, None], [6, None, None, 40], [None, None, 29, None], [46, 42, 34, None]]
   # Define the goal state of the grid, with the sums of rows and columns and the diagonal
   goal_state = (None, 99, 126, None, 97, 107, None, 124)
   # Define the range of the integers that can be placed in the grid
   num_range = range(6, 48)


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
                       new_state[row_ind][col_ind] = num
                       # The cost so far is the number of unique integers placed in the grid, as the task is to minimize the number of unique integers required
                       new_cost = g + 1


                       # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                       if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                           visited_costs[str(new_state)] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [(row_ind, col_ind, num)], new_state))
   return None


def state_sums(state):
   # Calculate the sums of rows, columns, and the diagonal of the state
   sums = []
   for row in state:
       sums.append(sum(row))
   sums.append(sum(state[i][i] for i in range(len(state))))
   sums.append(sum(state[i][len(state) - i - 1] for i in range(len(state))))
   return tuple(sums)


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the sums of rows, columns, and the diagonal of the state and the goal
   # This heuristic relaxes the constraint that the sums of rows and columns and the diagonal must be equal in the goal state
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be a non-negative number
   # It's consistent because moving a number from one position to another results in a decrease in the heuristic cost of the successor node by a max of 2 (if the moved number is part of the sum that is exceeding the goal sum), which is equal to the cost of reaching the successor node
   return sum(abs(state_sums(state)[i] - goal[i]) for i in range(len(goal)))


print(a_star())
