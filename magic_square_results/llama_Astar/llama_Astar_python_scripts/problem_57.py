
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' represented as None
   initial_state = [[42, None, 41, None], [None, 48, None, None], [None, 39, 30, 52], [None, None, 40, None]]
   # Define the goal state, with the sums of the rows and columns
   goal_state = (None, 170, 162, None, 191, 157, None)
   # Define the sum of the diagonal
   diagonal_sum = 171
   # Define the range of the integers
   integer_range = range(28, 60)
   # Define the number of rows and columns
   num_rows = 4
   num_cols = 4


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[tuple(map(tuple, initial_state))] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the swaps required to get to each state in a list; no swaps performed to reach the initial state
   queue = [(0, 0, [], initial_state)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if check_goal(state, goal_state, diagonal_sum):
           return actions


       # Generate all valid actions from the current state, which includes replacing any of the 'x's with a unique integer from the range
       for row_ind in range(num_rows):
           for col_ind in range(num_cols):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [list(row[:]) for row in state]
                   for integer in integer_range:
                       # Replace the 'x' with the integer
                       new_state[row_ind][col_ind] = integer
                       # Check if the new state is valid, ie if the sums of the rows, columns, and diagonal are as required
                       if check_valid(new_state, goal_state, diagonal_sum):
                           # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                           new_cost = g + 1


                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                           if new_state not in visited_costs or new_cost < visited_costs[tuple(map(tuple, new_state))]:
                               visited_costs[tuple(map(tuple, new_state))] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state, diagonal_sum), new_cost, actions + [(row_ind, col_ind, integer)], new_state))
                   # Reset the 'x' in the current state
                   new_state[row_ind][col_ind] = None


def check_goal(state, goal_state, diagonal_sum):
   # Check if the current state is the goal state
   # The goal state is reached if the sums of the rows, columns, and diagonal are as required
   sums = get_sums(state)
   if sums == goal_state and sums[0] + sums[1] + sums[2] + sums[3] + sums[4] + sums[5] + sums[6] == diagonal_sum:
       return True
   return False


def check_valid(state, goal_state, diagonal_sum):
   # Check if the current state is valid
   sums = get_sums(state)
   if sums == goal_state and sums[0] + sums[1] + sums[2] + sums[3] + sums[4] + sums[5] + sums[6] == diagonal_sum:
       return True
   return False


def get_sums(state):
   # Get the sums of the rows and columns
   sums = [sum(row) for row in state]
   sums.append(sum(state[i][i] for i in range(len(state))))
   sums.append(sum(state[i][len(state) - 1 - i] for i in range(len(state))))
   return tuple(sums)


def heuristic(state, goal_state, diagonal_sum):
   # An admissible and consistent heuristic for this problem is the sum of the absolute differences between the current sums of the rows, columns, and diagonal and the goal sums
   # This heuristic relaxes the constraint that the sums of the rows and columns must be as required, and the sum of the diagonal must be as required
   # It is admissible because it never overestimates the cost to reach the goal, as each incorrect sum must be corrected by a positive amount
   # It's consistent because moving a number from one position to another results in a decrease in the heuristic cost of the successor node by a max of 2 (if the moved number is part of the incorrect sum), which is equal to the cost of reaching the successor node
   h = 0
   sums = get_sums(state)
   goal_sums = list(goal_state)
   for i in range(len(sums)):
       h += abs(sums[i] - goal_sums[i])
   return h


print(a_star())
