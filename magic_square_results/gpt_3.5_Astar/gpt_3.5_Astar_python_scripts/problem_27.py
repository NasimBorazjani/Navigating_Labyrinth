
import heapq


def a_star():
   # Define the initial state of the magic square, with unknown numbers represented as 'x'
   initial_state = [['47', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x']]
   # Define the goal state, which is the magic square with the specified sums in the rows, columns, and diagonal
   goal_state = [['47', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x']]
   # Define the range of unique integers that can be placed in the grid
   unique_integers = list(range(26, 66))


   visited_costs = {}
   visited_costs[str(initial_state)] = 0


   queue = []
   # No actions taken in the initial state
   heappush(queue, (0, 0, [], initial_state))


   while queue:
       _, g, actions, state = heappop(queue)


       # If the current state is the goal state, return the actions taken
       if state == goal_state:
           return actions


       # Generate all possible actions from the current state, which includes replacing 'x' with unique integers in the grid
       for row in range(3):
           for col in range(3):
               if state[row][col] == 'x':
                   for num in unique_integers:
                       new_state = [row[:] for row in state]
                       new_state[row][col] = str(num)
                       # Calculate the sum of the rows, columns, and diagonal in the new state
                       row_sums = [sum([int(num) for num in row]) for row in new_state]
                       col_sums = [sum([int(new_state[row][col]) for row in range(3)]) for col in range(3)]
                       diagonal_sum = sum([int(new_state[i][2-i]) for i in range(3)])
                       # Check if the sums meet the specified conditions
                       if row_sums[0] == 135 and col_sums[0] == 93 and diagonal_sum == 106:
                           new_state_str = str(new_state)
                           new_cost = g + num
                           if new_state_str not in visited_costs or new_cost < visited_costs[new_state_str]:
                               visited_costs[new_state_str] = new_cost
                               heappush(queue, (new_cost, new_cost, actions + [(row, col, num)], new_state))
   return None


print(a_star())
