
import heapq


def a_star():
   # Define the initial state of the magic square grid, with 'x' representing unknown values
   initial_state = [['x', '20', 'x'], ['x', 'x', 'x'], ['x', 'x', '33']]
   # Define the goal sums for the rows, columns, and diagonal
   goal_sums = [82, 82, 96]
   # Define the range of unique integers that can be placed in the grid
   unique_integers = list(range(19, 44))


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
                       new_state[i][j] = str(num)
                       new_cost = g + num
                       if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                           visited_costs[str(new_state)] = new_cost
                           heappush(queue, (new_cost + heuristic(new_state, goal_sums), new_cost, actions + [(i, j, num)], new_state))
   return None


def check_constraints(state, goal_sums):
   # Check if the sums of rows, columns, and diagonal match the goal sums
   row_sums = [sum([int(num) for num in row if num != 'x']) for row in state]
   col_sums = [sum([int(state[i][j]) for i in range(3) if state[i][j] != 'x']) for j in range(3)]
   diagonal_sum1 = sum([int(state[i][i]) for i in range(3) if state[i][i] != 'x'])
   diagonal_sum2 = sum([int(state[i][2-i]) for i in range(3) if state[i][2-i] != 'x'])
   return row_sums == goal_sums[:2] and col_sums == goal_sums[:2] and diagonal_sum1 == goal_sums[2] and diagonal_sum2 == goal_sums[2]


def heuristic(state, goal_sums):
   # An admissible and consistent heuristic is the sum of the differences between the current sum of each row, column, and diagonal and the goal sum
   # This heuristic relaxes the constraint that the sum of the numbers in the grid must match the goal sums, presuming we can adjust the numbers to match the goal sums
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be adjusted to reach the goal sum
   # It is consistent because the estimated cost of the next node is higher if the sum of a row, column, or diagonal is further from the goal sum, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum amount that can be added to the sum is 1, which is exactly the decrease in the heuristic estimate
   h = 0
   row_sums = [sum([int(num) for num in row if num != 'x']) for row in state]
   col_sums = [sum([int(state[i][j]) for i in range(3) if state[i][j] != 'x']) for j in range(3)]
   diagonal_sum1 = sum([int(state[i][i]) for i in range(3) if state[i][i] != 'x'])
   diagonal_sum2 = sum([int(state[i][2-i]) for i in range(3) if state[i][2-i] != 'x'])
   for i in range(3):
       h += abs(row_sums[i] - goal_sums[i])
       h += abs(col_sums[i] - goal_sums[i])
   h += abs(diagonal_sum1 - goal_sums[2])
   h += abs(diagonal_sum2 - goal_sums[2])
   return h


print(a_star())
