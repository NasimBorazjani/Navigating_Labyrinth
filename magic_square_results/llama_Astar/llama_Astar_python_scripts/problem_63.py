
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[None, None, 63, None], [None, 44, None, 36], [50, None, None, 60], [None, 52, 38, 64]]
   # Define the goal state, with the sums of the rows and columns
   goal_state = (None, 207, 208, None, 173, 208, None, 201)
   # Define the constraints on the sums of the rows and columns
   row_sums = [None, 173, 208, None]
   col_sums = [None, 207, 208, None]
   # Define the range of numbers that can be used to replace 'x'
   num_range = range(30, 67)


   visited_costs = {}
   visited_costs[tuple(row[:] for row in initial_state)] = 0


   queue = [(0, 0, [], initial_state)]


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state_sums(state) == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with a number from the num_range
       for row_ind in range(len(state)):
           for col_ind in range(len(state[row_ind])):
               if state[row_ind][col_ind] is None:
                   for num in num_range:
                       # Generate the new state
                       new_state = [row[:] for row in state]
                       new_state[row_ind][col_ind] = num
                       # The cost so far is the number of numbers replaced, as the task is to minimize the number of numbers replaced
                       new_cost = g + 1


                       # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                       if state_sums(new_state) == goal_state and (new_state not in visited_costs or new_cost < visited_costs[tuple(new_state)]):
                           visited_costs[tuple(new_state)] = new_cost
                           heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [(row_ind, col_ind, num)], new_state))
   return None


def state_sums(state):
   # Calculate the sums of the rows and columns of the state
   row_sums = [sum(row) for row in state]
   col_sums = [sum(state[i][j] for i in range(len(state))) for j in range(len(state[0]))]
   # Calculate the sum of the diagonal
   diagonal_sum = sum(state[i][i] for i in range(len(state)))
   return tuple(row_sums + col_sums + [diagonal_sum])


def heuristic(state, goal):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sums of rows, columns, and the diagonal and the goal sums
   # This heuristic relaxes the constraint that the sum of the numbers in the grid must be as low as possible
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be a non-negative number
   # It's consistent because moving a number from one cell to another results in a decrease in the heuristic cost of the successor node by a max of the difference between the old and new sums, which is equal to the cost of reaching the successor node
   return sum(abs(state_sums(state)[i] - goal[i]) for i in range(len(goal)))


print(a_star())
