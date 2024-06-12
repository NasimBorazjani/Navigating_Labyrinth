
import heapq


def a_star():
   # Define the initial state of the magic square grid, with unknown numbers represented as 'x'
   initial_state = [['x', 'x', 'x'], ['x', 'x', 'x'], [22, 'x', 'x']]
   goal_sum = 82
   num_rows = 3
   num_cols = 3


   visited_costs = {}
   visited_costs[str(initial_state)] = 0


   queue = []
   # No actions taken in the initial state
   heappush(queue, (0, 0, [], initial_state))


   while queue:
       _, g, actions, state = heappop(queue)


       # If the sum of the first row, first column, and diagonal equals the goal sum, return the actions taken
       if check_goal(state, goal_sum):
           return actions


       # Generate all possible actions from the current state, which includes replacing 'x' with unique integers in the given range
       for row in range(num_rows):
           for col in range(num_cols):
               if state[row][col] == 'x':
                   for num in range(20, 40):
                       new_state = [row[:] for row in state]
                       new_state[row][col] = num
                       new_cost = g + num
                       if str(new_state) not in visited_costs or new_cost < visited_costs[str(new_state)]:
                           visited_costs[str(new_state)] = new_cost
                           heappush(queue, (new_cost + heuristic(new_state, goal_sum), new_cost, actions + [(row, col, num)], new_state))
   return None


def heuristic(state, goal_sum):
   # An admissible and consistent heuristic is the difference between the sum of the numbers in the grid and the goal sum
   # The heuristic relaxes the constraint that the numbers must be unique and within a certain range, presuming that the numbers can be any integer
   # It is admissible because it never overestimates the cost to reach the goal, as the sum of the numbers in the grid can only increase
   # It is consistent because the estimated cost of the next node is higher if a number is added to the grid, or equal or less by at most 1 (equal to the cost of reaching the successor node, ie one action) as the maximum value that can be added to the grid is 1, which is exactly the decrease in the heuristic estimate
   h = 0
   for row in state:
       for num in row:
           if num != 'x':
               h += num
   return abs(h - goal_sum)


def check_goal(state, goal_sum):
   # Check if the sum of the first row, first column, and diagonal equals the goal sum
   row_sum = sum(state[0])
   col_sum = sum(row[0] for row in state)
   diag_sum = state[0][2] + state[1][1] + state[2][0]
   return row_sum == goal_sum and col_sum == goal_sum and diag_sum == goal_sum


print(a_star())
