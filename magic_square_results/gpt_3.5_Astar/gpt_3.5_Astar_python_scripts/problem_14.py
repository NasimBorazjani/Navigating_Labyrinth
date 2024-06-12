
import heapq


def a_star():
   # Define the initial state of the magic square problem, with the grid represented as a 2D list
   initial_state = [['x', '32', 'x'], ['38', 'x', 'x'], ['x', 'x', 'x']]
   # Define the goal sums for each row, column, and diagonal
   goal_sums = [134, 143, 131]
   # Define the range of unique integers that can be placed in the grid
   unique_integers = list(range(28, 58))


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
                       # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
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
   return row_sums == goal_sums[:3] and col_sums == goal_sums[:3] and diagonal_sum1 == goal_sums[2] and diagonal_sum2 == goal_sums[2]


def heuristic(state, goal_sums):
   # An admissible and consistent heuristic is the sum of the differences between the current sum of each row, column, and diagonal and the goal sum
   # This heuristic relaxes the constraint that each number must be unique, and the sum of the numbers in the grid is minimized
   # It is admissible because it never overestimates the cost to reach the goal, as each difference must be minimized to reach the goal
   # It is consistent because the estimated cost of the next node is higher if a number is replaced with a larger number, or equal or less by at most 1 (equal to the cost of reaching the successor node) as the maximum difference that can be reduced is 1
   row_sums = [sum([int(num) for num in row if num != 'x']) for row in state]
   col_sums = [sum([int(state[i][j]) for i in range(3) if state[i][j] != 'x']) for j in range(3]
   diagonal_sum1 = sum([int(state[i][i]) for i in range(3) if state[i][i] != 'x'])
   diagonal_sum2 = sum([int(state[i][2-i]) for i in range(3) if state[i][2-i] != 'x'])
   h = sum([abs(row_sums[i] - goal_sums[i]) for i in range(3)])
   h += sum([abs(col_sums[i] - goal_sums[i]) for i in range(3)])
   h += abs(diagonal_sum1 - goal_sums[2])
   h += abs(diagonal_sum2 - goal_sums[2])
   return h


print(a_star())
