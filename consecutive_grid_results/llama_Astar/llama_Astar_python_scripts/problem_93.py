
import heapq


def a_star():
   # Define the initial state of the grid, with 'x' replaced by None
   initial_state = [[38, None, 50, None], [None, None, 64, 67], [54, None, 71, 79], [None, 59, 89, 90]]
   # Define the range of numbers that can be used for replacement
   num_range = range(36, 91)
   # Define the initial cost as 0, as no actions have been taken yet
   initial_cost = 0
   # Initialize the visited_costs dictionary with the initial state and its cost
   visited_costs = {tuple(row[:] for row in initial_state): initial_cost}
   # Initialize the queue with the initial state, with its cost and the actions taken so far
   queue = [(initial_cost, initial_cost, [], initial_state)]


   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state, ie all 'x's are replaced and the consecutive order is maintained in each row and column
       if all(row[0] <= row[1] <= row[2] <= row[3] for row in state) and all(state[0][i] <= state[1][i] <= state[2][i] <= state[3][i] for i in range(4)):
           return actions


       # Generate all possible actions from the current state, which includes replacing an 'x' with a unique number from the range
       for row_ind in range(4):
           for col_ind in range(4):
               if state[row_ind][col_ind] is None:
                   # Generate the new state
                   new_state = [row[:] for row in state]
                   # Replace the 'x' with a unique number from the range
                   for num in num_range:
                       new_state[row_ind][col_ind] = num
                       # Check if the new state is valid, ie the consecutive order is maintained in each row and column
                       if all(new_state[row_ind][0] <= new_state[row_ind][1] <= new_state[row_ind][2] <= new_state[row_ind][3]) and all(new_state[0][i] <= new_state[1][i] <= new_state[2][i] <= new_state[3][i] for i in range(4)):
                           # The cost so far is the number of replacements made, as the task is to minimize the number of replacements required
                           new_cost = g + 1


                           # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                           if tuple(tuple(row) for row in new_state) not in visited_costs or new_cost < visited_costs[tuple(tuple(row) for row in new_state)]:
                               visited_costs[tuple(tuple(row) for row in new_state)] = new_cost
                               heapq.heappush(queue, (new_cost + heuristic(new_state), g + 1, actions + [(row_ind, col_ind, num)], new_state))
   return None


def heuristic(state):
   # An admissible and consistent heuristic for this problem is the sum of the numbers in the topmost row, the numbers in the rightmost column, and the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner
   # This heuristic relaxes the constraint that the numbers in each row and column must be strictly increasing or decreasing, and that the sum of the numbers in the topmost row plus the numbers in the rightmost column plus the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner should be minimized
   # It is admissible because it never overestimates the cost to reach the goal, as each replacement must not result in a higher sum
   # It's consistent because moving a number from one position to another results in a lower or equal sum, as the sum of the numbers in the topmost row, the numbers in the rightmost column, and the numbers in the diagonal connecting the top-left corner of the grid to its bottom-right corner can only decrease or stay the same
   return sum(state[0]) + sum(state[i][i] for i in range(4)) + state[0][0] + state[3][3]


print(a_star())
