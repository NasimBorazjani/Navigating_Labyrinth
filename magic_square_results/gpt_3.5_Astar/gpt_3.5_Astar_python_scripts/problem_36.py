
import heapq


def a_star():
   # Define the initial state of the magic square grid, with 'x' representing unknown values
   initial_state = [['x', 'x', 'x'], ['x', 'x', 'x'], [69, 71, 'x']]
   # Define the goal sums for each row, column, and diagonal
   goal_sums = [152, 198, 195]
   # Define the range of unique integers that can be placed in the grid
   unique_integers = list(range(40, 90))


   visited_costs = {}
   visited_costs[str(initial_state)] = 0


   queue = []
   # No actions taken in the initial state
   heappush(queue, (0, 0, [], initial_state))


   while queue:
       _, g, actions, state = heappop(queue)


       # If the current state satisfies all the constraints, return the actions taken
       if check_constraints(state, goal_sums):
           return actions


       # Generate all possible actions from the current state, which includes replacing 'x' with unique integers in the grid
       for i in range(3):
           for j in range(3):
               if state[i][j] == 'x':
                   for num in unique_integers:
                       new_state = [row[:] for row in state]
                       new_state[i][j] = num
                       new_cost = g + num
                       # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                       if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                           visited_costs[str(new_state)] = new_cost
                           heappush(queue, (new_cost + heuristic(new_state, goal_sums), new_cost, actions + [(i, j, num)], new_state))
   return None


def check_constraints(state, goal_sums):
   # Check if the sum of each row, column, and diagonal in the grid matches the goal sums
   row_sums = [sum(row) for row in state]
   col_sums = [sum(col) for col in zip(*state)]
   diag_sum1 = state[0][2] + state[1][1] + state[2][0]
   diag_sum2 = sum(state[i][i] for i in range(3))
   return row_sums == goal_sums and col_sums == goal_sums and diag_sum1 == goal_sums[2] and diag_sum2 == goal_sums[2]


def heuristic(state, goal_sums):
   # An admissible and consistent heuristic is the sum of the differences between the current sum of each row, column, and diagonal and the goal sum
   # This heuristic relaxes the constraint that each number must be unique and presumes we can place any number in the grid
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be minimized to reach the goal
   # It is consistent because the estimated cost of the next node is higher if a number is placed in a position that increases the difference between the current sum and the goal sum, or equal or less by at most the difference between the current sum and the goal sum, which is exactly the cost of reaching the successor node
   h = 0
   row_sums = [sum(row) for row in state]
   col_sums = [sum(col) for col in zip(*state)]
   diag_sum1 = state[0][2] + state[1][1] + state[2][0]
   diag_sum2 = sum(state[i][i] for i in range(3))
   for i in range(3):
       h += abs(row_sums[i] - goal_sums[i]) + abs(col_sums[i] - goal_sums[i])
   h += abs(diag_sum1 - goal_sums[2]) + abs(diag_sum2 - goal_sums[2])
   return h


print(a_star())
